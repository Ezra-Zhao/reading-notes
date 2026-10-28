"""NLP 拆书 29 验证脚本：检索增强生成架构（clean-room 自写）
对应教材 6.2 节（书页 236-243，图 6.9-6.13）。
不依赖任何真实大模型，用玩具机制把本节可算、可复现的五件事逐项验清：

1) 四格分类账：按「语言模型是否微调 x 检索器是否微调」两轴，黑盒两格与
   白盒两格的可训开关互不重叠且覆盖全部分类；代表方法计数与教材对齐
   （黑盒无微调 In-Context RALM、黑盒检索器微调 REPLUG LSR 与 AAR、
   白盒仅微调语言模型 RETRO 与 SELF-RAG、白盒协同微调 Atlas）。
2) KL 对齐玩具（REPLUG LSR 与 Atlas 共用的机制）：检索器给出的文档分布
   与「文档对语言模型的贡献」分布初始不一致（KL 大于零）；把检索器分数
   朝贡献分布一步步挪动后 KL 单调下降并趋近于零——演示「只看黑盒输出、
   也能训练检索器」靠的就是让两个分布对齐。玩具只演示 KL 机制，
   不冒充真实训练。
3) 检索步长账（In-Context RALM 的关键参数）：生成总长固定时，步长越短
   检索次数越多（信息越及时、计算越贵），步长越长次数越少；查询长度
   取输入末尾若干词的口径一并演示。
4) RETRO 分块检索玩具：知识库文本先切块再各自做玩具向量，生成每走完
   一块就用当前块去检索最相似的块——最相似的确实是主题相邻的那一块，
   演示「分块、检索、交叉利用」这条流水线的排序形态；玩具向量不冒充
   BERT 嵌入，交叉注意力只在正文里讲机制、本项不模拟其数值。
5) 成本账：异步索引更新（每 K 步才更新一次向量编码）在总步数固定时把
   更新次数压到 1/K；四格架构的「可训参数份额」示意账（语言模型记 100
   份、检索器记 10 份）显示协同微调要同步更新的份额最大，与教材
   6.2.4「协同微调需要大量运算资源」的结论同向。份额是示意数，
   不是任何真实模型的参数量。
固定逻辑，无随机性，可复现。
"""
import math
import re

# ---------- 1. 四格分类账 ----------
print("=== 1. 四格分类：两轴开关覆盖黑盒/白盒全部分类 ===")
arch = {
    "黑盒-无微调":            {"lm_tuned": False, "ret_tuned": False, "methods": ["In-Context RALM"]},
    "黑盒-检索器微调":        {"lm_tuned": False, "ret_tuned": True,  "methods": ["REPLUG LSR", "AAR"]},
    "白盒-仅微调语言模型":    {"lm_tuned": True,  "ret_tuned": False, "methods": ["RETRO", "SELF-RAG"]},
    "白盒-协同微调":          {"lm_tuned": True,  "ret_tuned": True,  "methods": ["Atlas"]},
}
for name, cfg in arch.items():
    print(f"  {name}：语言模型微调={cfg['lm_tuned']}，检索器微调={cfg['ret_tuned']}，代表方法 {cfg['methods']}")
combos = {(c["lm_tuned"], c["ret_tuned"]) for c in arch.values()}
all_methods = [m for c in arch.values() for m in c["methods"]]
print(f"  开关组合 {len(combos)} 种（四种布尔组合全覆盖）；代表方法共 {len(all_methods)} 个")
assert len(arch) == 4 and len(combos) == 4
assert all(not c["lm_tuned"] for n, c in arch.items() if n.startswith("黑盒"))
assert all(c["lm_tuned"] for n, c in arch.items() if n.startswith("白盒"))
assert len(all_methods) == 6
print("断言通过：黑盒两格的语言模型开关恒为关、白盒两格恒为开——分类轴就是")
print("「是否微调语言模型」，第二轴「是否微调检索器」在两大类内部各分一格。")
print()

# ---------- 2. KL 对齐玩具 ----------
print("=== 2. KL 对齐：检索器分布向贡献分布靠拢，KL 单调下降 ===")
# 贡献分布 q：语言模型实际受益于哪篇文档（由输出/困惑度改善决定，示意值）
q = [0.55, 0.30, 0.10, 0.05]
# 检索器初始打分（余弦相似度示意）归一化后得到分布 p0：与 q 明显不一致
raw = [0.20, 0.25, 0.35, 0.20]
s = sum(raw)
p = [x / s for x in raw]

def kl(q_dist, p_dist):
    return sum(qi * math.log(qi / pi) for qi, pi in zip(q_dist, p_dist) if qi > 0)

print(f"  贡献分布 q = {q}")
print(f"  检索器初始分布 p0 = {[round(x, 3) for x in p]}，KL(q||p0) = {kl(q, p):.4f}")
kls = [kl(q, p)]
for step in range(1, 6):
    # 一步「训练」：把 p 朝 q 挪一半（梯度下降的玩具形态）
    p = [pi + 0.5 * (qi - pi) for pi, qi in zip(p, q)]
    kls.append(kl(q, p))
    print(f"  第 {step} 步后 p = {[round(x, 3) for x in p]}，KL = {kls[-1]:.4f}")
assert all(kls[i] > kls[i + 1] for i in range(len(kls) - 1))
assert kls[-1] < 0.01 < kls[0]
print("断言通过：KL 从明显大于零单调降到接近零——REPLUG LSR 用黑盒输出算出的")
print("贡献分布当老师、Atlas 在协同微调里用同一把 KL 尺子，差别只在语言模型那侧动不动。")
print()

# ---------- 3. 检索步长账 ----------
print("=== 3. 检索步长：生成 100 个词时，步长决定检索次数 ===")
total_words = 100
for stride in (10, 25, 50):
    times = total_words // stride
    print(f"  步长 {stride} 词：检索 {times} 次")
    assert times == total_words // stride
counts = [total_words // s for s in (10, 25, 50)]
assert counts == [10, 4, 2] and counts[0] > counts[1] > counts[2]
generated = "模型 正在 生成 一段 关于 考拉 栖息地 的 长 文本 内容"
query_tail = " ".join(generated.split()[-4:])
print(f"  查询长度演示：已生成文本的最后 4 个词作查询 = 「{query_tail}」")
assert query_tail == "的 长 文本 内容"
print("断言通过：步长 10 比步长 50 多查 5 倍——教材说的「更及时 vs 更费算力」")
print("就是这张账；查询取输入末尾几个词，是为了让检索跟住正在写的话题。")
print()

# ---------- 4. RETRO 分块检索玩具 ----------
print("=== 4. RETRO 形态：文本切块后，当前块检索到主题相邻块 ===")
chunks = {
    "C1": "考拉栖息在桉树上每天睡眠很长",
    "C2": "考拉主要吃桉树叶对树叶很挑食",
    "C3": "袋熊营穴居生活善于挖洞吃青草",
    "C4": "大熊猫主要吃竹子栖息在竹林里",
}

def char_tf(text):
    tf = {}
    for tok in re.findall(r"\d+|[^\d\s]", text):
        tf[tok] = tf.get(tok, 0) + 1
    return tf

def cosine(a, b):
    va, vb = char_tf(a), char_tf(b)
    keys = set(va) | set(vb)
    dot = sum(va.get(k, 0) * vb.get(k, 0) for k in keys)
    na = math.sqrt(sum(v * v for v in va.values()))
    nb = math.sqrt(sum(v * v for v in vb.values()))
    return dot / (na * nb)

current = chunks["C1"]
scores = {cid: cosine(current, text) for cid, text in chunks.items() if cid != "C1"}
ranking = sorted(scores, key=lambda d: -scores[d])
for cid in ranking:
    print(f"  {cid} 相似度 {scores[cid]:.3f}：{chunks[cid]}")
assert ranking[0] == "C2" and scores["C2"] > scores["C3"] and scores["C2"] > scores["C4"]
print("断言通过：当前块讲考拉栖息，检索第一名是同讲考拉饮食的相邻块——RETRO")
print("每生成一块就这样检索一次，再把检索结果经交叉注意力喂回生成；本项只验排序形态。")
print()

# ---------- 5. 成本账：异步更新 + 可训份额 ----------
print("=== 5. 成本账：异步索引更新省更新次数，协同微调可训份额最大 ===")
total_steps, every_k = 100, 10
sync_updates = total_steps
async_updates = total_steps // every_k
print(f"  训练 {total_steps} 步：每步更新索引 {sync_updates} 次；每 {every_k} 步更新一次 = {async_updates} 次")
assert async_updates * every_k == sync_updates and async_updates < sync_updates
LM_UNITS, RET_UNITS = 100, 10  # 示意份额，不是真实参数量
trainable = {n: (LM_UNITS if c["lm_tuned"] else 0) + (RET_UNITS if c["ret_tuned"] else 0)
             for n, c in arch.items()}
for n, v in trainable.items():
    print(f"  {n}：每步要更新的示意份额 {v}")
assert trainable["黑盒-无微调"] == 0
assert trainable["白盒-协同微调"] == max(trainable.values()) == 110
print("断言通过：无微调零更新最省、协同微调份额最大——与 6.2.4 的成本结论同向；")
print("异步更新把索引重建次数压到十分之一，是 REPLUG LSR 与 Atlas 都要付的同步账的打折法。")
print()
print("全部断言通过。")
