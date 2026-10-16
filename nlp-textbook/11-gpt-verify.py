"""GPT 家族验证代码 (11): 因果掩码 / 参数量估算 / 自回归生成 / 上下文学习玩具演示
自写示例, numpy + 标准库, 固定随机种子可复现. 无教材代码.
"""
import numpy as np

rng = np.random.default_rng(7)

print("=" * 72)
print("1) 因果掩码: Decoder-only 每个词只能看自己和左边的词")
print("=" * 72)
n = 6
scores = rng.normal(size=(n, n))
mask = np.where(np.triu(np.ones((n, n), dtype=bool), k=1), -1e9, 0.0)
masked = scores + mask
e = np.exp(masked - masked.max(axis=1, keepdims=True))
attn = e / e.sum(axis=1, keepdims=True)
np.set_printoptions(precision=2, suppress=True, linewidth=100)
print("注意力权重 (行=当前词, 列=被看的词):")
print(attn)
upper = attn[np.triu_indices(n, k=1)]
print(f"上三角(未来位置)权重最大值 = {upper.max():.2e}  (应约等于 0: 没偷看未来)")
print(f"每行权重和 = {attn.sum(axis=1)}  (应全为 1)")

print()
print("=" * 72)
print("2) 参数量估算: 每层约 12*d^2 (注意力 4d^2 + 前馈 8d^2), 外加词嵌入 vocab*d")
print("   对照教材表 2.4 (单位: 亿)")
print("=" * 72)
VOCAB = 50257  # GPT-2/3 词表量级, GPT-1 为 50257 同量级近似

def approx_params(layers, d):
    return layers * 12 * d * d + VOCAB * d

configs = [
    ("GPT-1",      12,  768,   1.17),
    ("GPT-2 Small", 12, 768,   1.24),
    ("GPT-2 XL",   48, 1600,  15.0),
    ("GPT-3 175B", 96, 12288, 1750.0),
]
prev = None
for name, L, d, book in configs:
    est = approx_params(L, d) / 1e8
    ratio = f"  (约为上一个的 {est/prev:.1f} 倍)" if prev else ""
    print(f"{name:12s} 层数={L:3d} d={d:6d}  估算={est:9.2f} 亿  教材={book:8.2f} 亿  误差={(est-book)/book*100:+.1f}%{ratio}")
    prev = est
print("说明: 估算忽略偏置/归一化/位置嵌入, 与教材数差几个百分点属正常;")
print("      量级对得上, 说明 '参数主要长在注意力的 4d^2 和前馈的 8d^2 里'.")

print()
print("=" * 72)
print("3) 自回归生成: 每一步只用已生成的词预测下一个词 (贪心)")
print("=" * 72)
# 手工转移表: 一个极小的 '语言模型', 只为演示自回归回路本身
trans = {
    "<S>": {"水豚": 1.0},
    "水豚": {"性格": 0.7, "喜欢": 0.3},
    "性格": {"温顺": 1.0},
    "温顺": {"，": 1.0},
    "，": {"它": 1.0},
    "它": {"只": 1.0},
    "只": {"吃": 1.0},
    "吃": {"水草": 0.8, "树叶": 0.2},
    "水草": {"</S>": 1.0},
    "喜欢": {"游泳": 1.0},
    "游泳": {"</S>": 1.0},
}
seq = ["<S>"]
for step in range(12):
    nxt_dist = trans[seq[-1]]
    nxt = max(nxt_dist, key=nxt_dist.get)
    print(f"步骤 {step+1}: 已有 {seq} -> 候选 {nxt_dist} -> 选 '{nxt}'")
    if nxt == "</S>":
        break
    seq.append(nxt)
print("生成结果:", "".join(seq[1:]))
print(f"关键账: 训练时一句话有 {len(seq)-1} 个位置, 每个位置都是一道'猜下一个词'的题,")
print("        一次前向就批改全部题 (Teacher Forcing); 生成时则必须一步一步往外掏.")

print()
print("=" * 72)
print("4) 上下文学习 (ICL) 玩具演示: 不改任何权重, 只改提示, 模型行为就变")
print("=" * 72)
# 玩具 '模型': 规则 = 从提示里的示例现学映射; 提示之外一无所知.
def toy_model(prompt_pairs, query):
    table = dict(prompt_pairs)          # 只读提示, 不写任何 '参数'
    return table.get(query, "不知道")

pairs = [("cat", "猫"), ("dog", "狗"), ("bird", "鸟")]
print("零样本 (提示里没示例): toy_model([], 'cat') =", toy_model([], "cat"))
print("少样本 (提示里给 3 对示例): toy_model(示例, 'dog') =", toy_model(pairs, "dog"))
print("同一组参数 (这里是空表起步), 行为差别全部来自提示内容 —— 这就是 ICL 的核心:")
print("学习发生在上下文里, 不发生在权重里. GPT-3 把规模做大后, 这种'现学'强到能顶替微调.")
