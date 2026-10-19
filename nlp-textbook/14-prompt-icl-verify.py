"""NLP 拆书 14 验证脚本：Prompt 与上下文学习（clean-room 自写）
演示四件事：
1) 同一任务的 zero-shot / one-shot / few-shot Prompt 拼装差异
2) 分词"生育率"(fertility) 的粗估：中英文每 token 覆盖字符数
3) 示例顺序效应：用一个玩具最近邻分类器模拟"示例怎么摆会影响预测"
4) 标签分布偏斜：示例全给同一标签时，玩具分类器会被带偏
只用标准库，固定数据，可复现。
"""
import re
from collections import Counter

# ---------- 1. Prompt 拼装 ----------
TASK = "判断下面句子的情感为积极还是消极。"
EXAMPLES = [
    ("小浣熊背了一箱干脆面走来，小浣熊手舞足蹈迎接。", "积极"),
    ("小浣熊吃了麻辣味干脆面，辣得肚子疼。", "消极"),
    ("小浣熊吃了烧烤味干脆面，脸上露出满意的笑容。", "积极"),
]
QUERY = "小浣熊连续吃了20包烧烤味干脆面，撑得肚子疼。"

def build_prompt(examples, query):
    parts = [TASK]
    for text, label in examples:
        parts.append(f"句子：{text}\n情感：{label}")
    parts.append(f"句子：{query}\n情感：")
    return "\n".join(parts)

for name, ex in [("zero-shot", []), ("one-shot", EXAMPLES[:1]),
                 ("few-shot", EXAMPLES)]:
    p = build_prompt(ex, QUERY)
    print(f"--- {name}: {len(p)} 字符, 示例 {len(ex)} 条 ---")
    print(p)
    print()

# ---------- 2. fertility 粗估 ----------
# 玩具分词：英文按空格+标点切词并按 ~4 字符/token 估算；中文按字估算 0.75 字/token 量级仅作演示
def toy_tokens_en(text):
    return re.findall(r"[A-Za-z]+|\d+|[^\sA-Za-z\d]", text)

def toy_tokens_zh(text):
    return list(re.sub(r"\s+", "", text))

en = "Prompt engineering is the practice of designing inputs for language models."
zh = "提示工程是为语言模型设计输入的实践方法。"
et, zt = toy_tokens_en(en), toy_tokens_zh(zh)
print("=== fertility 粗估（玩具分词，仅看量级）===")
print(f"英文: {len(en)} 字符 / {len(et)} token = {len(en)/len(et):.2f} 字符/token")
print(f"中文: {len(zh)} 字符 / {len(zt)} 字, 若按教材量级 ~1.3 字/token -> 约 {len(zt)/1.3:.1f} token")
print("教材实测口径: 中文约 1.3 字/token、英文约 0.7 词/token 量级（各模型词表不同）")
print()

# ---------- 3+4. 玩具分类器看顺序与标签偏斜 ----------
# 关键词打分分类器：统计正/负面词命中；示例的作用用"先验偏置"模拟：
# few-shot 中最后一条示例的标签给 +bias（近因效应），整体标签比例给先验。
POS = {"满意", "笑容", "手舞足蹈", "迎接", "好吃"}
NEG = {"疼", "辣得", "撑", "难吃", "哭"}

def toy_predict(query, examples, recency_bias=0.6):
    score = 0.0
    for w in POS:
        if w in query: score += 1
    for w in NEG:
        if w in query: score -= 1
    if examples:
        labels = [lab for _, lab in examples]
        prior = sum(1 if l == "积极" else -1 for l in labels) / len(labels)
        score += 0.5 * prior                      # 标签比例先验
        score += recency_bias if labels[-1] == "积极" else -recency_bias  # 近因
    return "积极" if score > 0 else "消极"

print("=== 顺序与偏斜效应（玩具模拟）===")
q2 = "小浣熊吃了新口味干脆面，脸上有点疼。"  # 信号含糊的句子
balanced = EXAMPLES                                   # 积极,消极,积极
flipped = [EXAMPLES[1], EXAMPLES[0], EXAMPLES[2]]     # 换顺序，末条仍积极
skewed = [EXAMPLES[0], EXAMPLES[2],
          ("小浣熊收到一箱干脆面，开心得跳起来。", "积极")]  # 全积极
for name, ex in [("原始顺序(末条=积极)", balanced),
                 ("示例全为积极(偏斜)", skewed)]:
    print(f"{name}: 对含糊句子的预测 = {toy_predict(q2, ex)}")
print(f"零示例基线: {toy_predict(q2, [])}")
print("结论(演示): 示例的标签比例与末条顺序会系统性带偏预测——选例要平衡、要代表性。")
print("示例标签分布:", Counter(lab for _, lab in EXAMPLES))
