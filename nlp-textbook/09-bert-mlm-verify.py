"""自写验证脚本：BERT 式 MLM 的遮词策略、只在遮住位置算损失，
以及 ALBERT 词嵌入因式分解的参数账、ELECTRA 全位置信号对比。
clean-room 示例，无教材代码。只用 numpy + 标准库，固定随机种子可复现。"""
import numpy as np

rng = np.random.default_rng(42)

# ---------- 1) 造一句示意文本（按词切分） ----------
tokens = ["水豚", "性格", "十分", "温顺", "且", "没有", "攻击性", "它", "只", "吃",
          "水草", "和", "树叶", "游客", "喂", "它", "水果", "时", "它", "慢慢", "走", "过来"]
n = len(tokens)
print(f"原句 ({n} 个 token): {' '.join(tokens)}")

# ---------- 2) MLM 遮词：选中约 15%，再按 80/10/10 处理 ----------
# BERT 的做法：被选中的位置里，80% 换成 [MASK]，10% 换成随机词，10% 保持原样。
# 保持原样和换随机词，是为了让模型不能只盯着 [MASK] 学（真实文本里没有 [MASK]）。
mask_prob = 0.15
selected = rng.random(n) < mask_prob
# 保证至少选中 3 个，演示才看得清（真实训练靠大批量自然达到约 15%）
if selected.sum() < 3:
    selected[rng.choice(n, size=3, replace=False)] = True
sel_idx = np.where(selected)[0]

vocab = list(dict.fromkeys(tokens))  # 示意词表
corrupted = tokens.copy()
actions = {}
for i in sel_idx:
    r = rng.random()
    if r < 0.80:
        corrupted[i] = "[MASK]"
        actions[i] = "80% -> [MASK]"
    elif r < 0.90:
        corrupted[i] = vocab[rng.integers(len(vocab))]
        actions[i] = "10% -> 随机词"
    else:
        actions[i] = "10% -> 保持原样"
print(f"\n选中位置 {sel_idx.tolist()} (占比 {selected.mean():.0%}, 目标约 15%)")
for i in sel_idx:
    print(f"  位置 {i}: 原词 '{tokens[i]}' -> 输入 '{corrupted[i]}'  [{actions[i]}]")
print(f"遮改后输入: {' '.join(corrupted)}")

# ---------- 3) 只在遮住位置算损失：labels 其余位置设为 -100（忽略） ----------
# 用一组示意 logits（真实模型由编码器输出，这里用固定种子随机数模拟分数）
V = len(vocab)
tok2id = {t: k for k, t in enumerate(vocab)}
logits = rng.normal(0, 1.5, size=(n, V))
# 给正确词一点人为优势，纯为让 loss 数字落在合理区间，不影响掩码逻辑演示
for i in sel_idx:
    logits[i, tok2id[tokens[i]]] += 2.0

labels = np.full(n, -100)  # -100 = 不计损失（PyTorch CrossEntropy 的 ignore_index 约定）
for i in sel_idx:
    labels[i] = tok2id[tokens[i]]

def cross_entropy_at(logit_row, label_id):
    z = logit_row - logit_row.max()
    log_softmax = z - np.log(np.exp(z).sum())
    return -log_softmax[label_id]

per_pos = [cross_entropy_at(logits[i], labels[i]) if labels[i] != -100 else None
           for i in range(n)]
masked_losses = [x for x in per_pos if x is not None]
mlm_loss = float(np.mean(masked_losses))
print(f"\nlabels (仅选中位置保留真实 id, 其余 -100 表示忽略): {labels.tolist()}")
print(f"计损失位置数: {len(masked_losses)}/{n} —— 只有被选中的位置产生 MLM 梯度信号")
print(f"MLM loss (仅遮住位置的平均交叉熵): {mlm_loss:.4f}")
# 反证：如果错误地对全部位置算 loss，数值会被大量'没被遮'的简单位置稀释
all_loss = float(np.mean([cross_entropy_at(logits[i], tok2id[tokens[i]]) for i in range(n)]))
print(f"对照 (错误做法, 全部位置都算): {all_loss:.4f} —— 口径不同, 不能和 MLM loss 直接比大小")

# ---------- 4) ELECTRA 的 RTD：每个位置都判'原词还是被替换词' ----------
print(f"\n信号密度对比 (同一句 {n} 个 token):")
print(f"  BERT / MLM : {len(masked_losses)} 个位置算 loss ({len(masked_losses)/n:.0%})")
print(f"  ELECTRA / RTD: {n} 个位置算 loss (100%) —— 生成器换掉几个词, 判别器逐词验真假")
print(f"  密度倍数: {n / len(masked_losses):.1f}x —— 这就是 ELECTRA 用更少算力追上 BERT 的关键一招")

# ---------- 5) ALBERT 词嵌入因式分解：一笔参数账 ----------
Vv, H, E = 30000, 768, 128  # 词表大小、隐藏维度、ALBERT 的低维嵌入
bert_emb = Vv * H
albert_emb = Vv * E + E * H
print(f"\nALBERT 词嵌入参数账 (词表 V={Vv}, 隐藏 H={H}, 低维 E={E}):")
print(f"  BERT  直接嵌入 V x H       : {bert_emb:,} 参数")
print(f"  ALBERT 两步嵌入 V x E + E x H: {albert_emb:,} 参数")
print(f"  压缩倍数: {bert_emb / albert_emb:.2f}x —— 先把词压到 {E} 维, 再升到 {H} 维")
print("\n结论: BERT 靠'遮住猜回'学双向表示; 三个改进版分别赢在训得更狠(RoBERTa)、"
      "参数更省(ALBERT)、每个位置都出信号(ELECTRA)。")
