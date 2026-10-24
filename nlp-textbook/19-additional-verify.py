"""NLP 拆书 19 验证脚本：附加参数方法（clean-room 自写）
演示五件事：
1) Prompt-tuning 参数账：m 个虚拟 token、维度 d，可训参数 = m*d；
   m=20、d=1024 时正好 20,480，与教材给 T5-XXL 的口径互证；
   并演示 [P; X] 拼接后的形状 (m+n) x d。
2) Prefix-tuning 参数账：每层存 Pk、Pv 两份前缀，可训量 = 2 * L * l * d，
   比 Prompt-tuning 多付 L 倍量级，换来逐层干预。
3) Adapter 参数账：瓶颈 r<<d 时单个 Adapter 约 2dr+d+r，
   与全量 d*d 对比；并实际跑一遍 下投影->非线性->上投影->残差 的前向，
   验证残差在适配器权重为零时严格还原输入（摘掉即还原）。
4) AdapterFusion 组合：用注意力式加权把 N 个单任务 Adapter 的输出融成一个，
   权重和为 1，融合结果是各 Adapter 输出的凸组合。
5) Proxy-tuning 解码时调制：s_tilde = s_M + s_M+ - s_M-，
   用玩具词表演示小模型对的 logits 差如何翻转大模型的 top-1，
   且专家与反专家相同时调制量为零（无专家信号则不动大模型）。
只用标准库 + numpy，固定随机种子，可复现。
"""
import numpy as np

rng = np.random.default_rng(42)

# ---------- 1. Prompt-tuning ----------
print("=== 1. Prompt-tuning 参数账 ===")
for m, d in [(1, 1024), (20, 1024), (100, 1024), (20, 4096)]:
    print(f"m={m:3d}, d={d}: 可训参数 = {m*d:,}")
print("教材口径互证: m=20, d=1024 -> 20,480（T5-XXL 11B 全量参数的约 0.0002%）")
n, d = 12, 8
X = rng.normal(size=(n, d))          # 真实输入嵌入
P = rng.normal(size=(20, d))         # 可训软提示
PX = np.concatenate([P, X], axis=0)  # [P; X]
print(f"拼接演示: X {X.shape} + P {(20, d)} -> [P;X] {PX.shape}（序列变长 m+n，维度不变）")
print()

# ---------- 2. Prefix-tuning ----------
print("=== 2. Prefix-tuning 参数账（每层 Pk + Pv）===")
def prefix_params(L, l, d):
    return 2 * L * l * d
for L, l, d in [(12, 10, 768), (24, 10, 1024), (32, 20, 4096)]:
    print(f"L={L} 层, 前缀长 l={l}, d={d}: 可训参数 = {prefix_params(L, l, d):,}")
print("对照: 同配置 Prompt-tuning 只在输入端付一份 m*d；Prefix 逐层付，干预更深、账也更厚。")
print("注: 训练时前缀常由 MLP 重参数化生成以求稳定，推理时只保留 Pk/Pv 本身。")
print()

# ---------- 3. Adapter ----------
print("=== 3. Adapter 参数账与前向 ===")
def adapter_params(d, r):
    # Wd: d x r, Wu: r x d, 偏置 d + r（按教材口径 2dr + d + r）
    return 2 * d * r + d + r
for d, r in [(1024, 8), (1024, 64), (4096, 64)]:
    ap = adapter_params(d, r)
    print(f"d={d}, r={r}: 单个 Adapter = {ap:,}，占同层 d*d={d*d:,} 的 {ap/(d*d):.2%}")
d, r = 16, 4
H = rng.normal(size=(5, d))
Wd = rng.normal(size=(d, r)) * 0.1
Wu = rng.normal(size=(r, d)) * 0.1
def adapter_forward(H, Wd, Wu):
    return np.maximum(0, H @ Wd) @ Wu + H   # ReLU + 残差，对应教材式 (4.1) 的结构
out = adapter_forward(H, Wd, Wu)
zero_out = adapter_forward(H, np.zeros_like(Wd), np.zeros_like(Wu))
print(f"前向形状: H {H.shape} -> A {out.shape}（形状不变，只改数值）")
print(f"零权重时与输入的最大差: {np.abs(zero_out - H).max():.2e}（严格为 0 = 摘掉/未训时还原底座行为）")
print(f"两 Adapter/层 x 24 层 (d=1024, r=64): {2*24*adapter_params(1024,64):,} 参数")
print()

# ---------- 4. AdapterFusion ----------
print("=== 4. AdapterFusion 注意力式融合 ===")
# 3 个单任务 Adapter 对同一输入给出不同输出向量（玩具演示）
adapter_outputs = np.array([[1.0, 0.0, 0.2],
                            [0.1, 1.0, 0.3],
                            [0.2, 0.2, 1.0]])
query = np.array([1.0, 0.9, 0.1])  # 当前层输入充当 Query，与各 Adapter 输出算相关性
scores = adapter_outputs @ query / np.sqrt(3)
weights = np.exp(scores) / np.exp(scores).sum()  # softmax
fused = weights @ adapter_outputs
print(f"融合权重: {np.round(weights, 3)}，权重和 = {weights.sum():.3f}")
print(f"融合输出: {np.round(fused, 3)}（各 Adapter 输出的加权组合，偏向与当前输入最相关的 Adapter）")
print()

# ---------- 5. Proxy-tuning ----------
print("=== 5. Proxy-tuning logits 调制（教材式 4.3/4.4）===")
vocab = ["的", "猫", "量子", "报告"]
s_M   = np.array([2.0, 1.2, 0.5, 1.8])   # 大模型（未微调）原始 logits
s_pos = np.array([1.0, 1.1, 2.6, 1.2])   # 专家小模型（已微调）logits
s_neg = np.array([1.9, 1.0, 0.4, 1.6])   # 反专家小模型（未微调）logits
s_tilde = s_M + s_pos - s_neg            # 式 (4.3)
def top1(s):
    p = np.exp(s) / np.exp(s).sum()
    return vocab[int(np.argmax(s))], round(float(p.max()), 3)
print(f"调制前大模型 top-1: {top1(s_M)}")
print(f"调制后代理模型 top-1: {top1(s_tilde)}（小模型对的偏好差把大模型推向微调方向，未动大模型一个参数）")
s_same = s_M + s_pos - s_pos
print(f"专家=反专家时调制量恒为 0: max|s_tilde - s_M| = {np.abs(s_same - s_M).max():.1f}")
print("代价提示: 每步解码要多跑专家+反专家两个小模型的前向，省的是训练与显存，付的是推理算力。")
