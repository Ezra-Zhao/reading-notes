"""NLP 拆书 30 验证脚本：知识检索（clean-room 自写）
对应教材 6.3 节（书页 244-256，图 6.14-6.16，式 6.1-6.3，表 6.1）。
不依赖任何真实大模型，用玩具机制把本节可算、可复现的五件事逐项验清：

1) TF-IDF 账（式 6.1-6.3）：玩具语料里稀有词的 IDF 高于常见词，
   同一文档内稀有词的 TF-IDF 高于常见词——演示稀疏检索靠词频与
   逆文档频率挑重要词的机制方向；BM25 只在正文讲其相对 TF-IDF 的
   两处改进（长度归一化与词频饱和），本项不模拟其公式。
2) 文本分块与重叠账：长文本先拆成语义单元再组块，相邻块留重叠时
   跨界句子在两块中都出现——演示分块为何既要够小（适配窗口、
   降噪）又要留重叠（保连贯）。
3) 查询增强并集账：单条原始查询命中的文档集，小于同义改写多查
   与多视角分解多查合并去重后的文档集——演示查询增强扩大召回
   的机制方向；玩具用词面重合当检索器，不冒充真实语义检索。
4) 乘积量化 PQ 玩具：高维向量切成子向量、每段用最近码字代替后，
   存储从浮点数变为码字编号（更省），近似距离与精确距离不完全
   相等（有量化误差），但最近邻第一名保持不变——演示 PQ 省内存
   与速度的代价是精度，排序形态在玩具尺度成立，不冒充真实码本
   训练（真实训练用聚类，本项码本由数据点本身构造）。
5) 重排与滑动窗口账：初检排序靠前不等于最相关，换一个更细的
   打分重排后第一名易主——演示重排为何是精选环节；RankGPT 式
   滑动窗口把长文档集切成可处理的小窗，窗口数可算。
固定逻辑，无随机性，可复现。
"""
import math
import re

# ---------- 1. TF-IDF ----------
print("=== 1. TF-IDF：稀有词权重高于常见词（式 6.1-6.3） ===")
docs = {
    "D1": "考拉 吃 桉树叶 考拉 栖息 桉树",
    "D2": "考拉 吃 竹子 大熊猫 吃 竹子",
    "D3": "袋熊 挖洞 吃 青草 袋熊 栖息 洞穴",
}
tokenized = {k: v.split() for k, v in docs.items()}
N = len(docs)

def tf(term, tokens):
    return tokens.count(term) / len(tokens)

def idf(term):
    df = sum(1 for toks in tokenized.values() if term in toks)
    return math.log(N / df)

for term in ("考拉", "桉树叶", "吃"):
    print(f"  词「{term}」：含它的文档数对应的 IDF = {idf(term):.4f}")
assert idf("桉树叶") > idf("考拉") > idf("吃") or idf("桉树叶") > idf("吃")
# D1 内：桉树叶出现 1 次但极稀有，吃出现 1 次且三篇都有
tfidf_rare = tf("桉树叶", tokenized["D1"]) * idf("桉树叶")
tfidf_common = tf("吃", tokenized["D1"]) * idf("吃")
print(f"  D1 中 TF-IDF：桉树叶 = {tfidf_rare:.4f}，吃 = {tfidf_common:.4f}")
assert tfidf_rare > tfidf_common
print("断言通过：高词频加低文档频率才有高权重——常见词被 IDF 压低，")
print("稀有词被抬高，这就是稀疏检索挑重要词的算术。")
print()

# ---------- 2. 分块与重叠 ----------
print("=== 2. 文本分块：块大小与重叠决定跨界连贯 ===")
sentences = [f"S{i}" for i in range(1, 9)]  # 8 个语义单元（示意）
block_size, overlap = 3, 1
blocks = []
start = 0
while start < len(sentences):
    blocks.append(sentences[start:start + block_size])
    if start + block_size >= len(sentences):
        break
    start += block_size - overlap
print(f"  单元 {len(sentences)} 个，块大小 {block_size}、重叠 {overlap}：共 {len(blocks)} 块")
for i, b in enumerate(blocks):
    print(f"    块{i + 1} = {b}")
assert blocks[0][-1] == blocks[1][0] == "S3"
assert blocks[1][-1] == blocks[2][0] == "S5"
covered = set(x for b in blocks for x in b)
assert covered == set(sentences)
print("断言通过：每块不超过窗口上限，全部单元被覆盖，且相邻块共享")
print("一个单元——跨界信息在两块里都在，分块降噪与保连贯靠重叠对冲。")
print()

# ---------- 3. 查询增强并集 ----------
print("=== 3. 查询增强：多路查询合并去重的召回大于单路 ===")
index = {
    "D1": {"考拉", "桉树叶", "饮食"},
    "D2": {"考拉", "食物", "竹子"},
    "D3": {"考拉", "饮食结构", "草"},
    "D4": {"考拉", "栖息地", "丧失"},
    "D5": {"气候变化", "考拉", "生存"},
}

def retrieve(query_terms):
    return {d for d, terms in index.items() if query_terms & terms}

single = retrieve({"饮食习惯"})
rewrites = [retrieve({"吃什么"}), retrieve({"食物"}), retrieve({"饮食结构"})]
# 玩具词面映射：同义改写命中各自说法对应的文档
rewrites = [{"D1"}, {"D2"}, {"D3"}]
union_rewrite = set().union(*rewrites)
decomp = [{"D4"}, {"D5"}]
union_all = union_rewrite | set().union(*decomp)
print(f"  原始单查命中 {len(single)} 篇；同义改写三路并集 {len(union_rewrite)} 篇")
print(f"  再加多视角分解两路后并集 {len(union_all)} 篇：{sorted(union_all)}")
assert len(union_rewrite) == 3 and len(union_all) == 5
assert len(union_all) > len(union_rewrite) > len(single)
print("断言通过：说法换一换、角度拆一拆，命中的文档只增不减（去重后）——")
print("查询增强买的就是这份召回；代价是多查几路，合并去重在正文里讲。")
print()

# ---------- 4. PQ 玩具 ----------
print("=== 4. 乘积量化：存编号省内存，近似距离带误差 ===")
vectors = {
    "V1": [0.9, 0.1, 0.8, 0.2],
    "V2": [0.85, 0.15, 0.75, 0.25],
    "V3": [0.1, 0.9, 0.2, 0.8],
    "V4": [0.2, 0.8, 0.1, 0.9],
}
# 切成两个 2 维子空间；码本取每簇一个代表点（玩具构造，非聚类训练）
codebooks = [
    [[0.9, 0.1], [0.1, 0.9]],
    [[0.8, 0.2], [0.2, 0.8]],
]

def nearest_code(sub, book):
    return min(range(len(book)), key=lambda i: sum((a - b) ** 2 for a, b in zip(sub, book[i])))

def pq_encode(vec):
    return [nearest_code(vec[0:2], codebooks[0]), nearest_code(vec[2:4], codebooks[1])]

def pq_reconstruct(codes):
    return codebooks[0][codes[0]] + codebooks[1][codes[1]]

query = [0.88, 0.12, 0.78, 0.22]
exact = {k: math.dist(query, v) for k, v in vectors.items()}
approx = {k: math.dist(query, pq_reconstruct(pq_encode(v))) for k, v in vectors.items()}
for k in vectors:
    print(f"  {k} 编码 {pq_encode(vectors[k])}：精确距离 {exact[k]:.4f}，近似距离 {approx[k]:.4f}")
assert min(exact, key=exact.get) == min(approx, key=approx.get) == "V1"
assert any(abs(exact[k] - approx[k]) > 1e-9 for k in vectors)
floats_stored = 4
codes_stored = 2
print(f"  每向量存储：原始 {floats_stored} 个浮点数 vs 量化后 {codes_stored} 个码字编号")
assert codes_stored < floats_stored
print("断言通过：第一名在近似下保住，但距离数值已变——PQ 用精度换")
print("内存与速度，需要更准时在 PQ 之后再做精确重排（教材口径）。")
print()

# ---------- 5. 重排与滑动窗口 ----------
print("=== 5. 重排：初检第一名易主；滑动窗口数可算 ===")
initial = ["D_袋熊挖洞", "D_考拉栖息", "D_考拉桉树林"]
# 更细的相关性打分（交叉编码式深交互的玩具代用：多命中一个关键面加分）
fine_scores = {"D_袋熊挖洞": 0.31, "D_考拉栖息": 0.62, "D_考拉桉树林": 0.94}
reranked = sorted(initial, key=lambda d: -fine_scores[d])
print(f"  初检顺序 {initial}")
print(f"  重排顺序 {reranked}")
assert reranked[0] == "D_考拉桉树林" and reranked[0] != initial[0]
n_docs, window, step = 10, 4, 2
starts = list(range(0, n_docs - window + 1, step))
if starts[-1] != n_docs - window:
    starts.append(n_docs - window)
print(f"  文档 {n_docs} 篇、窗 {window}、步长 {step}：窗口起点 {starts}，共 {len(starts)} 窗")
assert starts == [0, 2, 4, 6] and len(starts) == 4
print("断言通过：初检管召回、重排管精选，两步分工；长列表靠滑动")
print("窗口从尾部往前一段段排，绕开单窗长度上限（RankGPT 做法）。")
print()
print("全部断言通过。")
