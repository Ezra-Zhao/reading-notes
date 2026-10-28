"""NLP 拆书 28 验证脚本：检索增强生成简介（clean-room 自写）
对应教材第六章章首（书页 229）与 6.1 节（书页 230-235，图 6.1-6.8）。
不依赖任何真实大模型，用玩具机制把本节可算、可复现的五件事逐项验清：

1) 结构计数：训练数据致幻三问题、模型自身致幻四因素、RAG 三组件、
   本章三优化问题（检索优化五子项、增强优化四子项），与教材逐项对齐。
2) 知识过时例的区间算术：无 RAG 回答区间 5,000-8,000 与正确区间
   86,000-176,000 完全不相交（错答上限还不到正确下限的十分之一），
   说明这不是误差而是知识截面停在旧年份。数字为教材图 6.1/6.5 口径。
3) 玩具检索器：记号级 TF-IDF 余弦相似度（连续数字串算一个记号）下，
   查询「2023年的考拉数量」的第一名是含正确区间的文档；名称相近的
   袋熊干扰文档（自加）得分更低但大于零，演示「检索得到相关文档」
   与「相近不等于相关」的分寸。注：本项实测翻过两次车——纯字频余弦
   与单字 TF-IDF 都把 2016 年旧文档排到了第一（字面重叠多、数字字符
   偶然重叠），把年份按整串记号算、并用 TF-IDF 给判别性记号加权后
   才排对；翻车过程保留在代码注释里——字面相似不等于相关，
   是检索的常态难题，不是玩具独有的问题。
4) 同一生成器、参数零改动：无检索时吐出记住的旧答案（错），把检索
   文档拼进 Prompt 后从文档中抽出正确区间（对）——演示 RAG 的核心
   优势「不更新内部知识也能改对答案」，生成器参数前后逐项不变。
5) 别名悖论（图 6.2/6.3 的机制演示）：知识库里明明存着双向别名映射，
   一步直答的启发式仍会答成「两种动物」，先查别名再答的两步法答对
   ——演示「知识在库里，不等于一次生成就能用对」。玩具只演示逻辑
   形态，不冒充教材在 ChatGPT 上的真实实验。
固定逻辑，无随机性，可复现。
"""
import math
import re

# ---------- 1. 结构计数 ----------
print("=== 1. 结构计数：致幻成因 / RAG 组件 / 三优化问题 ===")
train_causes = ["知识过时", "知识边界", "知识偏差"]
model_factors = ["知识长尾", "曝光偏差", "对齐不当", "解码偏差"]
components = ["外部知识库 Corpus", "检索器 Retriever", "生成器 Generator（大语言模型）"]
opt_questions = ["优化检索器与生成器的协作", "优化检索过程", "优化增强过程"]
retrieval_sub = ["知识库构建", "查询增强", "检索器", "检索效率增强", "重排优化"]
augment_sub = ["何时增强", "何处增强", "多次增强", "降本增效（知识压缩与缓存加速）"]
print(f"  训练数据致幻 {len(train_causes)} 类：{train_causes}")
print(f"  模型自身致幻因素 {len(model_factors)} 个：{model_factors}")
print(f"  RAG 组件 {len(components)} 个：{components}")
print(f"  本章优化问题 {len(opt_questions)} 个；检索子项 {len(retrieval_sub)} 个；增强子项 {len(augment_sub)} 个")
assert len(train_causes) == 3 and len(model_factors) == 4
assert len(components) == 3 and len(opt_questions) == 3
assert len(retrieval_sub) == 5 and len(augment_sub) == 4
print("断言通过：计数与教材 6.1 节及章首目录口径逐项对齐。")
print()

# ---------- 2. 知识过时例的区间算术 ----------
print("=== 2. 知识过时：错答区间与正确区间完全不相交 ===")
wrong_lo, wrong_hi = 5000, 8000
right_lo, right_hi = 86000, 176000
overlap = not (wrong_hi < right_lo or right_hi < wrong_lo)
print(f"  无 RAG 回答：{wrong_lo}-{wrong_hi}；正确（教材引 2023 年估计）：{right_lo}-{right_hi}")
print(f"  两区间相交？{overlap}；错答上限/正确下限 = {wrong_hi / right_lo:.3f}（不到十分之一）")
assert not overlap and wrong_hi < right_lo / 10
print("断言通过：这是知识截面停在训练截止年份的系统性错误，不是小误差。")
print("说明：教材脚注注明其所用 ChatGPT 版本训练数据截止到 2022 年（本章撰写时口径）。")
print()

# ---------- 3. 玩具检索器：记号级 TF-IDF 余弦 ----------
print("=== 3. 玩具检索器：相关文档排第一，相近文档不等于相关文档 ===")
corpus = {
    "D1": "2023年调整后的考拉种群估计数在86000至176000只之间",
    "D2": "2016年研究人员估计全澳大利亚考拉总数为329000只",
    "D3": "考拉调查方法指南已经制定并与主要专家进行了测试",
    "D4": "袋熊与考拉同为有袋类动物，袋熊营穴居生活善于挖洞以青草野菜为食",
}

def char_tf(text):
    # 分词口径：连续数字串算一个记号（2023 与 2016 是两个不同的年份记号，
    # 不按单个数字字符算重叠），其余按单字。首版按单数字字符算时，
    # 2016 年文档靠数字 2/0 的偶然重叠再次险些排到第一，故改此口径。
    tf = {}
    for tok in re.findall(r"\d+|[^\d\s]", text):
        tf[tok] = tf.get(tok, 0) + 1
    return tf

DOC_TFS = {doc_id: char_tf(text) for doc_id, text in corpus.items()}
N_DOCS = len(corpus)

def idf(ch):
    df = sum(1 for tf in DOC_TFS.values() if ch in tf)
    return math.log((N_DOCS + 1) / (df + 1)) + 1.0

def tfidf_vec(text):
    return {ch: n * idf(ch) for ch, n in char_tf(text).items()}

def cosine(a, b):
    va, vb = tfidf_vec(a), tfidf_vec(b)
    keys = set(va) | set(vb)
    dot = sum(va.get(k, 0) * vb.get(k, 0) for k in keys)
    na = math.sqrt(sum(v * v for v in va.values()))
    nb = math.sqrt(sum(v * v for v in vb.values()))
    return dot / (na * nb)

query = "2023年的考拉数量大约有多少"
scores = {doc_id: cosine(query, text) for doc_id, text in corpus.items()}
ranking = sorted(scores, key=lambda d: -scores[d])
for doc_id in ranking:
    print(f"  {doc_id} 相似度 {scores[doc_id]:.3f}：{corpus[doc_id]}")
assert ranking[0] == "D1"
assert 0 < scores["D4"] < scores["D1"]
print("断言通过：D1 第一；袋熊文档 D4 与查询有字面重叠（得分大于零）但排不进第一，")
print("仅靠字面相近捞回来的文档，正是后文要防的噪声来源（本篇只演示排序，不冒充真实检索器）。")
print()

# ---------- 4. 同一生成器，参数零改动 ----------
print("=== 4. 参数零改动：无检索答错，拼入检索文档后答对 ===")
PARAMS = {"memorized_koala_2023": "5000-8000", "cutoff_year": 2022}
params_before = dict(PARAMS)

def generate(question, context=None):
    """玩具生成器：有上下文先按问题年份在上下文里抽区间，没有就用记住的旧答案。"""
    if context:
        year = re.search(r"(20\d{2})", question)
        for line in context.splitlines():
            if year and year.group(1) in line:
                m = re.search(r"(\d{4,6})\D{0,4}(\d{4,6})", line)
                if m:
                    return f"{m.group(1)}-{m.group(2)}"
    return PARAMS["memorized_koala_2023"]

q = "2023年的考拉数量大约有多少？"
ans_bare = generate(q)
prompt = q + "\n参考文档：" + corpus["D1"]
ans_rag = generate(q, context=corpus["D1"])
print(f"  拼入的 Prompt：{prompt}")
print(f"  无 RAG 回答：{ans_bare}（错）；带 RAG 回答：{ans_rag}（对）")
print(f"  生成器参数前后一致？{PARAMS == params_before}（{PARAMS}）")
assert ans_bare == "5000-8000" and ans_rag == "86000-176000"
assert PARAMS == params_before
print("断言通过：答案变对靠的是 Prompt 里多了一篇文档，不是一次参数更新——")
print("这正是教材说的核心优势：避开内部更新的计算成本与灾难性遗忘风险。")
print()

# ---------- 5. 别名悖论：知识在库里，一步直答仍答错 ----------
print("=== 5. 别名悖论：有知识，不等于一次生成就用对 ===")
KB = {"考拉": "树袋熊", "树袋熊": "考拉"}  # 双向别名，知识本身完整无缺

def answer_direct(a, b):
    """一步直答的坏启发式：名字不同就猜成两种动物。"""
    return "同种动物" if a == b else "两种不同的动物"

def answer_two_step(a, b):
    """两步法：先查别名再判断。"""
    return "同种动物" if KB.get(a) == b or KB.get(b) == a else "两种不同的动物"

direct = answer_direct("考拉", "树袋熊")
two_step = answer_two_step("考拉", "树袋熊")
print(f"  知识库别名映射：{KB}（双向都在，知识不缺）")
print(f"  一步直答「考拉和树袋熊是什么关系」：{direct}（错，对应图 6.2 型翻车）")
print(f"  先查别名再答：{two_step}（对，对应图 6.3 型自证）")
assert direct == "两种不同的动物" and two_step == "同种动物"
assert KB["考拉"] == "树袋熊" and KB["树袋熊"] == "考拉"
print("断言通过：同一份知识，一步直答翻车、分解后答对——教材由此把这类幻觉")
print("归因于模型自身（长尾/曝光偏差/对齐不当/解码偏差），而非知识缺失。")
print()
print("全部断言通过。")
