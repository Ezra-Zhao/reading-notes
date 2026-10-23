"""NLP 拆书 18 验证脚本：参数高效微调全景（clean-room 自写）
演示四件事：
1) 参数账：同一组权重矩阵，全量微调 / LoRA / BitFit / Prompt-tuning 各自要训多少参数
2) 显存账：按 Adam 口径（权重 fp32 + 梯度 fp32 + 一阶/二阶动量各 fp32）估算训练态显存，
   对照教材表 4.1 的量级（全量在 80GB 卡上 OOM、LoRA 装得下）
3) 低秩直觉：真实更新若本身近低秩，r 很小的 LoRA 式分解就能抓住绝大部分能量；
   若更新是满秩噪声，低秩近似立刻露馅——LoRA 的赌注一目了然
4) 三大家族分诊：按"动的是什么"把教材点名的方法路由到附加/选择/低秩三家
只用标准库 + numpy，固定随机种子，可复现。
"""
import numpy as np

rng = np.random.default_rng(42)

# ---------- 1. 参数账：以一个注意力投影矩阵为例 ----------
d, k = 1024, 1024          # 一张权重矩阵 W ∈ R^{d×k}
full = d * k
for r in (4, 8, 16):
    lora = r * (d + k)     # A ∈ R^{r×k} + B ∈ R^{d×r}
    print(f"LoRA r={r:2d}: 可训参数={lora:,}，占全量 {lora/full:.2%}")
bitfit = k                 # 只训这张矩阵对应的偏置向量（长度 k）
print(f"BitFit（只训偏置）: 可训参数={bitfit:,}，占全量 {bitfit/full:.2%}")
m, d_model = 20, 1024      # Prompt-tuning：m 个虚拟 token 的嵌入
pt = m * d_model
print(f"Prompt-tuning（{m} 个虚拟 token）: 可训参数={pt:,}，占单矩阵全量 {pt/full:.2%}")
print(f"单矩阵全量: {full:,}")
print()

# 放大到一个 7B 量级模型的粗账（只算量级，不冒充精确架构数）
total = 7_000_000_000
print("=== 7B 量级粗账 ===")
print(f"全量微调可训参数: {total:,}（100%）")
print(f"LoRA 若覆盖主要投影且占比 0.5%: 约 {int(total*0.005):,}")
print(f"BitFit 教材口径占比 0.08%–0.09%: 约 {int(total*0.0008):,}–{int(total*0.0009):,}")
print()

# ---------- 2. 显存账：Adam 训练态 ----------
def adam_gb(n_params):
    # fp32 权重 4B + fp32 梯度 4B + Adam m/v 各 4B = 16B/可训参数；
    # 冻结参数只需存权重（按 bf16 推理式存放计 2B），无梯度无动量
    return n_params * 16 / 1e9

def mixed_gb(total_params, trainable):
    # 冻结底座只存 bf16 权重（2B/参数，无梯度无动量）；
    # 可训参数按 Adam 口径 16B/参数。省显存的大头来自这档切换。
    frozen = total_params - trainable
    return (trainable * 16 + frozen * 2) / 1e9

print("=== 显存账（Adam 口径估算）===")
print(f"7B 全量微调训练态: 约 {adam_gb(total):.0f} GB（未含激活）-> 单张 24GB/80GB 都吃紧或 OOM")
print(f"7B LoRA（可训 0.5%）训练态: 约 {mixed_gb(total, total*0.005):.1f} GB（未含激活）")
print("教材表 4.1 实测对照：T0_3B 全量 47.14GB GPU vs LoRA 14.4GB；")
print("  mt0-xxl(12B) 与 bloomz-7b1(7B) 全量在 80GB 卡上 OOM，LoRA 分别 56GB / 32GB 装下")
print()

# ---------- 3. 低秩直觉 ----------
def lowrank_capture(delta, r):
    u, s, vt = np.linalg.svd(delta, full_matrices=False)
    approx = (u[:, :r] * s[:r]) @ vt[:r]
    err = np.linalg.norm(delta - approx) / np.linalg.norm(delta)
    return 1 - err

# 场景 A：真实更新由少数方向主导（近低秩）
a_true = rng.normal(size=(256, 8)); b_true = rng.normal(size=(8, 256))
delta_low = a_true @ b_true + 0.01 * rng.normal(size=(256, 256))
# 场景 B：真实更新是满秩噪声
delta_full = rng.normal(size=(256, 256))
for r in (4, 8, 16):
    print(f"r={r:2d}: 近低秩更新捕获率 {lowrank_capture(delta_low, r):.1%} | "
          f"满秩噪声更新捕获率 {lowrank_capture(delta_full, r):.1%}")
print("参数对比: 满秩 256x256=65,536；r=8 的低秩分解只需 8x(256+256)=4,096")
print()

# ---------- 4. 三大家族分诊 ----------
FAMILY = {
    "Adapter-tuning": "附加参数（在层间插入小模块）",
    "Prompt-tuning": "附加参数（在输入端加可训软提示）",
    "Prefix-tuning": "附加参数（在各层注意力前加可训前缀）",
    "Proxy-tuning": "附加参数（用大小模型 logits 差代理调制）",
    "BitFit": "参数选择（只训原有偏置）",
    "Child-tuning": "参数选择（每步只更新一个子网络）",
    "FishMask": "参数选择（按 Fisher 信息挑重要参数训）",
    "LoRA": "低秩适配（冻结 W，只训低秩增量 BA）",
    "AdaLoRA": "低秩适配（秩预算自适应分配）",
    "DyLoRA": "低秩适配（一次训练兼容多个秩）",
    "DoRA": "低秩适配（权重拆成幅度与方向再低秩调方向）",
}
print("=== 三大家族分诊（教材 4.1.2 点名方法）===")
for name, fam in FAMILY.items():
    print(f"{name:16s} -> {fam}")
