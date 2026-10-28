"""NLP 拆书 31 验证脚本：生成增强（clean-room 自写）
对应教材 6.4 节（书页 256-270，图 6.17-6.26）。
不依赖任何真实大模型，用玩具机制把本节可算、可复现的五件事逐项验清：

1) 盲目增强之害：模型本可答对的问题，喂入名称相近的噪声文档后
   答案被污染——演示「非必要不增强」为何同时关乎效率与质量；
   本项是关键词污染的玩具复现，不冒充真实模型的生成过程。
2) 何时增强的判据账：多次回答一致性（已知高、未知低）与流行度
   阈值（流行实体判已知、不流行判未知）两个外部观测判据的方向；
   另如实演示直接询问的过度自信翻车（未知问题也自称不需要帮助）。
3) 何处增强三位置账：输入端拼接的 Token 成本、中间层向量融合的
   紧凑性、输出端矫正对文档质量的依赖（好文档纠对、坏文档纠错）。
4) 多次增强账：单次检索解不了两跳问题，分解后两步接力可解；
   模糊问题渐进细化后叶节点答案数大于单答，覆盖更全。
5) 降本增效账：按困惑度删低信息 Token 后长度减半且关键信息词
   全保留；重复文档的 KV 缓存复用使重复计算次数下降。
固定逻辑，无随机性，可复现。
"""

# ---------- 1. 盲目增强之害 ----------
print("=== 1. 非必要不增强：噪声文档把答对的题带偏 ===")
clean_answer = "树袋熊主要栖息在桉树林，白天多在树上休息"
noisy_doc = "袋熊营穴居生活，善于挖洞，以青草野菜为食，为夜行动物"
# 玩具生成规则：答案词表 = 原答案词 + 文档高频生活习性词（模拟模型混淆近名实体）
polluted_answer = "树袋熊栖息在森林，利用挖洞能力在地洞中建造巢穴，以青草野菜为食，为夜行动物"
print(f"  无增强答案：{clean_answer}")
print(f"  喂入袋熊文档后：{polluted_answer}")
assert "挖洞" not in clean_answer and "挖洞" in polluted_answer
assert "青草" in polluted_answer and "夜行动物" in polluted_answer
print("断言通过：原答案里没有的挖洞/青草/夜行三项，全从近名噪声文档")
print("串入——盲目增强不是免费保险，可能把对的改错（图 6.17/6.18 口径）。")
print()

# ---------- 2. 何时增强的判据 ----------
print("=== 2. 何时增强：一致性与流行度判据，直接询问会翻车 ===")
from collections import Counter

def consistency(answers):
    return Counter(answers).most_common(1)[0][1] / len(answers)

known_answers = ["栖息在澳大利亚桉树林"] * 5
unknown_answers = ["约32000个", "26558个", "约18000个", "26558个", "约9000个"]
print(f"  已知问题五次回答一致性 = {consistency(known_answers):.2f}")
print(f"  未知问题五次回答一致性 = {consistency(unknown_answers):.2f}")
assert consistency(known_answers) == 1.0 and consistency(unknown_answers) == 0.4
# 流行度阈值（玩具浏览量，演示教材以维基页面浏览量作伪统计量的口径）
popularity = {"考拉（物种本身）": 950000, "考拉基因数量": 1200}
threshold = 100000
judged = {k: ("已知，不增强" if v >= threshold else "未知，需增强") for k, v in popularity.items()}
for k, v in judged.items():
    print(f"  {k}：浏览量 {popularity[k]} -> {v}")
assert judged["考拉（物种本身）"].startswith("已知") and judged["考拉基因数量"].startswith("未知")
# 直接询问的过度自信：未知问题上模型自称不需要帮助（教材指出的失效模式）
direct_ask = {"考拉是什么动物": False, "2023年考拉数量": False}  # False=自称不需要外部帮助
print(f"  直接询问自称不需要帮助的问题数 = {sum(1 for v in direct_ask.values() if not v)}/2（含它其实答不对的 2023 年数量题）")
assert direct_ask["2023年考拉数量"] is False
print("断言通过：一致性与流行度都能把已知/未知分开（方向成立），而")
print("直接询问在未知题上同样自称不需要——过度自信是教材明说的坑。")
print()

# ---------- 3. 何处增强 ----------
print("=== 3. 何处增强：输入端贵在长度，中间层胜在紧凑，输出端押在文档质量 ===")
doc_text = "2023年调整后的考拉种群估计数在86000至176000只之间调查方法另有说明" * 3
question = "2023年考拉数量大约有多少"
input_tokens = len(doc_text) + len(question)
middle_vectors = 4  # 玩具：整篇文档压成 4 个向量槽位喂交叉注意力
print(f"  输入端拼接：文档+问题共 {input_tokens} 个字符级 Token 一并进上下文")
print(f"  中间层融合：同一文档只占 {middle_vectors} 个向量槽位")
assert input_tokens > 100 and middle_vectors < input_tokens // 10
draft = "5000到8000只"
good_doc = "86000至176000只"
bad_doc = "袋熊约14天完成消化"
def correct(draft_answer, doc):
    return "86000至176000只" if "86000" in doc else draft_answer + "（被坏文档带偏）"
print(f"  输出端矫正（好文档）：{draft} -> {correct(draft, good_doc)}")
print(f"  输出端矫正（坏文档）：{draft} -> {correct(draft, bad_doc)}")
assert correct(draft, good_doc) == "86000至176000只" and "带偏" in correct(draft, bad_doc)
print("断言通过：输入端直观但长度成本最高，中间层紧凑但要改结构，")
print("输出端是后处理——成败押在检索文档本身对不对（REFEED 口径）。")
print()

# ---------- 4. 多次增强 ----------
print("=== 4. 多次增强：分解式两跳接力，渐进式多叶覆盖 ===")
kb = {
    "最能睡的动物是什么": "考拉（树袋熊），每天睡约22小时",
    "考拉爱吃什么": "桉树叶，每天约500克鲜叶",
    "中国的国宝动物爱吃什么": "熊猫爱吃竹子",
    "澳洲的国宝动物考拉爱吃什么": "考拉爱吃桉树叶",
    "澳洲的国宝动物袋鼠爱吃什么": "袋鼠爱吃杂草和灌木",
}
single = kb.get("世界上睡眠时间最长的动物爱吃什么")
print(f"  单次直查复合问题：{single}")
assert single is None
step1 = kb["最能睡的动物是什么"]
step2 = kb["考拉爱吃什么"]
final = "世界上睡眠时间最长的动物是考拉，爱吃桉树叶"
print(f"  分解第一跳：{step1}；第二跳：{step2}；合成：{final}")
assert "考拉" in step1 and "桉树叶" in step2 and "桉树叶" in final
leaves = [kb[k] for k in kb if "国宝动物" in k and "吃什么" in k]
print(f"  模糊问题「国宝动物爱吃什么」渐进细化叶节点 {len(leaves)} 条：{leaves}")
assert len(leaves) == 3
print("断言通过：复合问题一次查不到，拆成两跳就通；模糊问题不硬选")
print("一个答案，细化成多条路径再整合，覆盖 3 个有效解答（TOC 口径）。")
print()

# ---------- 5. 降本增效 ----------
print("=== 5. 降本增效：困惑度删冗余，KV 缓存复用省重算 ===")
tokens = [("考拉", 8.2), ("主要", 1.1), ("以", 0.9), ("桉树叶", 7.5),
          ("为食", 3.2), ("的", 0.5), ("一种", 1.3), ("动物", 2.8)]
kept = [t for t, s in tokens if s >= 2.0]
print(f"  压缩前 {len(tokens)} 个 Token，删低困惑度后保留 {len(kept)} 个：{kept}")
assert kept == ["考拉", "桉树叶", "为食", "动物"] and len(kept) == len(tokens) // 2
queries_docs = [["D1", "D2"], ["D1", "D3"], ["D1", "D2"], ["D4"]]
computed = set()
total_slots = sum(len(q) for q in queries_docs)
for q in queries_docs:
    for d in q:
        computed.add(d)  # 已算过的文档 KV 直接命中缓存，不再重算
print(f"  4 次查询共涉及 {total_slots} 个文档槽，实际计算不同文档 {len(computed)} 个：{sorted(computed)}")
assert total_slots == 7 and len(computed) == 4
print("断言通过：低困惑度 Token 携带信息少、可删，关键信息词全留下；")
print("重复文档的 KV 只算一次，7 个槽的活 4 次计算干完（RAGCache 口径）。")
print()
print("全部断言通过。")
