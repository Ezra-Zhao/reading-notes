"""NLP 拆书 32 验证脚本：RAG 实践与应用（clean-room 自写）
对应教材 6.5 节（书页 271-278，图 6.27-6.28）。第六章收尾、本教材最后一节。
不依赖 LangChain/LlamaIndex/Chroma/OpenAI 等真实框架与任何真实大模型，
用纯标准库玩具机制把本节可算、可复现的五件事逐项验清：

1) 分块账：教材示例 chunk_size=1000、chunk_overlap=200；玩具缩小为
   size=10、overlap=3，验分块覆盖原文、相邻块确有重叠、块数公式成立；
2) 极简 RAG 全链：加载->分块->玩具向量->检索 top-2->拼上下文->生成，
   答案只能出自检索到的上下文（有据），且换问题检索结果随之变；
3) 链的组装顺序：模拟 LCEL 式管道 context(检索|格式化) 与 question 直通，
   再经 prompt->llm->解析，验执行轨迹顺序与字段完整；
4) Agent 抱考拉例：配置/记忆/计划/行动四模块协同——记忆未命中时行动
   模块外检，计划整合后输出两个教材地点（龙柏/科伦宾）；
5) 多模态垂域：图像+文本双特征融合检索医学知识库，融合检索 top-1
   命中教材案例答案「心肌肥大」，且单模态各有一路会排错，说明为何要融合。
固定逻辑，无随机性，可复现。玩具数值只演示机制方向，不冒充真实框架实测。
"""

# ---------- 1. 分块账 ----------
print("=== 1. 分块：长文档切成带重叠的小块 ===")
doc = "考拉栖息在澳大利亚桉树林每天睡约二十二小时以桉树叶为食"  # 27 字玩具文档
size, overlap = 10, 3
step = size - overlap
chunks = [doc[i:i + size] for i in range(0, len(doc), step)]
print(f"  原文 {len(doc)} 字，chunk_size={size}，overlap={overlap}，共 {len(chunks)} 块：{chunks}")
assert len(chunks) == 4 and chunks[0] == doc[:10]
assert chunks[0][-overlap:] == chunks[1][:overlap]  # 相邻块共享 overlap 段
assert chunks[-1] == doc[21:] and len(chunks[-1]) == 6
print("断言通过：相邻块确有 3 字重叠（信息不断茬）、末块收全尾巴；")
print("教材正式参数是 1000/200，道理相同：块太大塞不进上下文，太小丢上下文。")
print()

# ---------- 2. 极简 RAG 全链 ----------
print("=== 2. 极简 RAG 全链：检索到什么，答案里才有什么 ===")
kb = [
    "考拉每天睡约22小时，主要以桉树叶为食",
    "熊猫主要以竹子为食，生活在中国山区",
    "袋鼠以杂草和灌木为食，是澳大利亚国宝",
    "树袋熊又称考拉，栖息在澳大利亚桉树林",
]
def vec(text, vocab):
    return [text.count(w) for w in vocab]
vocab = ["考拉", "桉树叶", "睡", "竹子", "袋鼠", "杂草"]
def retrieve(query, topk=2):
    qv = vec(query, vocab)
    scored = []
    for d in kb:
        dv = vec(d, vocab)
        scored.append((sum(a * b for a, b in zip(qv, dv)), d))
    scored.sort(key=lambda x: -x[0])
    return [d for s, d in scored[:topk] if s > 0]
def rag_answer(query):
    ctx = retrieve(query)
    # 玩具生成器：只复述上下文里与问句共享关键词的句子，无上下文则拒答
    if not ctx:
        return "上下文里没有依据，不编造"
    return "；".join(ctx)
a1 = rag_answer("考拉睡多久吃什么")
print(f"  问「考拉睡多久吃什么」-> {a1}")
assert "22小时" in a1 and "桉树叶" in a1 and "竹子" not in a1
a2 = rag_answer("袋鼠吃什么")
print(f"  问「袋鼠吃什么」-> {a2}")
assert "杂草" in a2 and "22小时" not in a2
a3 = rag_answer("火星上有水吗")
print(f"  问「火星上有水吗」-> {a3}")
assert a3.startswith("上下文里没有依据")
print("断言通过：换问题、检索结果与答案随之变；库里没有的，玩具生成器")
print("明确拒答——RAG 的有据，不只在答对时，也在没依据时不硬编。")
print()

# ---------- 3. 链的组装顺序 ----------
print("=== 3. LCEL 式组装：检索与直通并行，再过 prompt/llm/解析 ===")
trace = []
def stage(name, fn):
    def wrap(x):
        trace.append(name)
        return fn(x)
    return wrap
retriever = stage("retriever", lambda q: retrieve(q))
format_docs = stage("format_docs", lambda ds: "\n\n".join(ds))
prompt = stage("prompt", lambda d: f"上下文：{d['context']}\n问题：{d['question']}\n只据上下文回答")
llm = stage("llm", lambda p: p.split("上下文：")[1].split("\n问题")[0].replace("\n\n", "；"))
parser = stage("parser", lambda s: s.strip())
ctx = format_docs(retriever("考拉睡多久吃什么"))
out = parser(llm(prompt({"context": ctx, "question": "考拉睡多久吃什么"})))
print(f"  执行轨迹：{' -> '.join(trace)}")
print(f"  链输出：{out}")
assert trace == ["retriever", "format_docs", "prompt", "llm", "parser"]
assert "22小时" in out
print("断言通过：context 一路由检索再格式化、question 一路直通，两路在")
print("prompt 处汇合——这正是教材 LCEL 代码的骨架（字段名 context/question）。")
print()

# ---------- 4. Agent 抱考拉例 ----------
print("=== 4. Agent 四模块：记忆未命中就外检，计划整合再输出 ===")
profile = {"role": "熟悉澳洲生活的向导", "goal": "帮用户合法抱考拉"}
memory = {"已知": "科伦宾野生动物保护区可以合法拥抱考拉"}  # 教材图 6.27 记忆格
external = {
    "允许抱考拉的地点": ["布里斯班的龙柏考拉动物园", "黄金海岸的科伦宾野生动物保护区"],
    "与考拉互动的规定": "须在昆士兰州持牌场所、按场馆时段与饲养员指引",
}
plan_steps = ["查找允许抱考拉的地点信息", "了解当前与考拉互动的规定", "考虑从当前位置到选定地点的交通方式"]
hits = []
for step in plan_steps[:2]:
    if step not in memory:
        hits.append(step)  # 记忆没有 -> 行动模块调用工具外检（RAG 在记忆/计划/行动三处介入）
recommend = external["允许抱考拉的地点"]
print(f"  配置：{profile['role']}；计划 {len(plan_steps)} 步；需外检 {len(hits)} 步")
print(f"  输出推荐：{'、'.join(recommend)}")
assert len(plan_steps) == 3 and len(hits) == 2
assert any("龙柏" in r for r in recommend) and any("科伦宾" in r for r in recommend)
print("断言通过：配置定角色、计划拆三步、记忆先查、外检补缺、整合输出——")
print("教材五步流程（配置/规划/检索/整合决策/输出）与图 6.27 两个地点对齐。")
print()

# ---------- 5. 多模态垂域检索 ----------
print("=== 5. 多模态垂域：图像+文本融合检索，单模态会排错 ===")
# 每例：(图像特征, 文本特征, 结论)；查询在原点，距离均为玩具一维示意：
# 正确例两模态都中等近（各 0.3），诱饵例各有一模态极近（0.1）另一模态远（0.9）
cases = [
    ((0.3, 0.0), (0.3, 0.0), "心肌肥大"),
    ((0.1, 0.0), (0.9, 0.0), "肺炎"),
    ((0.9, 0.0), (0.1, 0.0), "胸腔积液"),
]
q_img, q_txt = (0.0, 0.0), (0.0, 0.0)
def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5
by_img = min(cases, key=lambda c: dist(q_img, c[0]))[2]
by_txt = min(cases, key=lambda c: dist(q_txt, c[1]))[2]
by_fused = min(cases, key=lambda c: dist(q_img, c[0]) + dist(q_txt, c[1]))[2]
print(f"  只看图像最近：{by_img}；只看文本最近：{by_txt}；双模态融合最近：{by_fused}")
assert by_img == "肺炎" and by_txt == "胸腔积液" and by_fused == "心肌肥大"
print("断言通过：单看任一模态都会排错，融合后才命中教材 X 光案例的答案")
print("「心肌肥大」——垂域多模态 RAG 必须融合不同模态，道理在此（图 6.28）。")
print()
print("全部断言通过。")
