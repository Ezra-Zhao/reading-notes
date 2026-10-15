"""自写验证脚本：T5 的 Span Corruption（整段遮掉、哨兵标记、解码器只生成被遮片段）、
BART 的五种加噪（以演示其中三种可直接落地的），以及 Encoder-Decoder 交叉注意力形状账。
clean-room 示例，无教材代码。只用 numpy + 标准库，固定随机种子可复现。"""
import numpy as np

rng = np.random.default_rng(7)

tokens = ["水豚", "性格", "十分", "温顺", "且", "没有", "攻击性", "它", "只", "吃",
          "水草", "和", "树叶", "游客", "喂", "它", "水果", "时", "它", "慢慢", "走", "过来"]
n = len(tokens)
print(f"原句 ({n} 个 token): {' '.join(tokens)}")

# ---------- 1) T5 Span Corruption：遮的是连续片段，不是单个词 ----------
# BERT 遮散词，T5 遮整段：随机选若干连续 span，总量约占 15%，
# 每个 span 在输入里换成一个独一无二的哨兵记号 <X>、<Y> ...
# 解码器的目标不是重写全句，而是只输出被挖掉的片段：<X> 片段1 <Y> 片段2 <Z>
spans = [(1, 3), (10, 12)]  # [性格 十分] 与 [水草 和] 被挖掉（示意，真实训练随机采样）
sentinels = ["<X>", "<Y>"]
corrupt = []
span_of = {}
pos = 0
for k, (a, b) in enumerate(spans):
    corrupt.extend(tokens[pos:a])
    corrupt.append(sentinels[k])
    span_of[sentinels[k]] = tokens[a:b]
    pos = b
corrupt.extend(tokens[pos:])
target = []
for k, s in enumerate(sentinels):
    target.append(s)
    target.extend(span_of[s])
target.append("<Z>")  # 结束哨兵
masked_tokens = sum(b - a for a, b in spans)
print(f"\nT5 Span Corruption:")
print(f"  编码器输入 ({len(corrupt)} 个): {' '.join(corrupt)}")
print(f"  解码器目标 ({len(target)} 个): {' '.join(target)}")
print(f"  被挖 token: {masked_tokens}/{n} = {masked_tokens / n:.0%} (目标约 15%)")
print(f"  关键账: 解码器只需生成 {len(target)} 个 token，而不是重写全句 {n} 个 —— 训练更省")

# ---------- 2) BART 加噪一：Token Deletion（删词，模型要自己发现哪里少了） ----------
del_mask = rng.random(n) < 0.15
if del_mask.sum() == 0:
    del_mask[rng.integers(n)] = True
deleted = [t for t, d in zip(tokens, del_mask) if not d]
print(f"\nBART 加噪演示:")
print(f"  Token Deletion 删掉 {del_mask.sum()} 个: 输入 {len(deleted)} 个 token, "
      f"没有任何占位符 —— 模型必须靠语义发现'哪里缺了词'")

# ---------- 3) BART 加噪二：Text Infilling（整段换成一个 [MASK]，段长服从 Poisson） ----------
lam = 3.0
span_len = int(rng.poisson(lam))
if span_len < 2:
    span_len = 3  # 演示下限: 段长至少 2 才看得出'整段换一个记号'(真实训练可为 0, 即纯插入)
start = 5
infilled = tokens[:start] + ["[MASK]"] + tokens[start + span_len:]
print(f"  Text Infilling: 段长服从 Poisson(lambda={lam}), 本次取 {span_len}, "
      f"从位置 {start} 起 {span_len} 个 token 换成 1 个 [MASK]")
print(f"    输入: {' '.join(infilled)}")
print(f"    和 T5 的差别: BART 的解码目标是重构全文 {n} 个 token; T5 只生成被挖片段")

# ---------- 4) BART 加噪三：Sentence Permutation + Document Rotation（句序与起点） ----------
sentences = [["水豚", "性格", "温顺"], ["它", "只", "吃", "水草"], ["游客", "很", "喜欢", "它"]]
order = rng.permutation(len(sentences))
if (order == np.arange(len(sentences))).all():
    order = order[::-1]  # 本次种子恰好抽到原序, 演示改为逆序, 逻辑不变
permuted = [sentences[i] for i in order]
print(f"  Sentence Permutation: 原句序 [0, 1, 2] -> 打乱为 {order.tolist()}")
rot = 4
rotated = tokens[rot:] + tokens[:rot]
print(f"  Document Rotation: 文档从第 {rot} 个 token 起旋转, 模型要先找出'真正的开头'在哪")

# ---------- 5) 交叉注意力：解码器的 Q 去查编码器的 K/V ----------
d = 8
enc_len, dec_len = len(corrupt), len(target)
H_enc = rng.normal(0, 1, size=(enc_len, d))   # 编码器输出：源句每个位置一个向量
H_dec = rng.normal(0, 1, size=(dec_len, d))   # 解码器当前状态
scores = H_dec @ H_enc.T / np.sqrt(d)          # (dec_len, enc_len)
attn = np.exp(scores - scores.max(axis=1, keepdims=True))
attn = attn / attn.sum(axis=1, keepdims=True)
print(f"\n交叉注意力形状账:")
print(f"  编码器输出 H_enc: {H_enc.shape}  (源句 {enc_len} 个位置 x {d} 维)")
print(f"  注意力权重: {attn.shape}  每一行和 = {attn.sum(axis=1)[0]:.3f} (应为 1)")
print(f"  含义: 解码器每生成一个 token, 都重新回头看一遍源句全部位置, 按相关性加权取信息")
print(f"  参数量级对照 (教材表): T5 0.6 亿 (Small) 到 110 亿 (11B); BART 1.4 亿 (Base) 到 4 亿 (Large)")

print("\n结论: Encoder-Decoder = 编码器先把源句读懂, 解码器边回头看边逐词写;"
      " T5 的花招是'任务全变文本题 + 只生成被挖片段', BART 的花招是'把文本弄坏再重构全文'。")
