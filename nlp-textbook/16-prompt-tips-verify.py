"""NLP 拆书 16 验证脚本：Prompt 技巧（clean-room 自写）
演示四件事：
1) 规范 Prompt 的四件套拼装与体检：任务说明/上下文/问题/输出格式齐不齐、
   任务说明里的动词与类别词明不明确（模糊版 vs 明确版对照）
2) 输出格式的可用性差距：JSON 一行代码可解析，自由文本只能靠脆弱的字符串硬抠
3) 复杂问题拆解：分步引导（先算两个子问题）+ 归纳总结（再合成最终答案）
4) CoT 适用性决策：按教材三因素（任务类别/模型规模/是否已内化推理）给出用不用链的判定
只用标准库，固定数据，可复现。
"""
import json
import re

# ---------- 1. 四件套拼装与体检 ----------
CLEAR_VERBS = {"判断", "分类", "生成", "翻译", "总结", "提取", "改写"}
VAGUE_VERBS = {"处理", "操作", "弄一下", "看看"}

def build_prompt(task, context, question, fmt):
    return (f"### {task}\n"
            f"针对此问题有如下示例：\n{context}\n"
            f"### 待处理的内容：{question}\n"
            f"### 以 {fmt} 格式返回最终结果。")

def check_prompt(task, has_context, has_question, fmt):
    issues = []
    if not any(v in task for v in CLEAR_VERBS):
        issues.append("任务说明缺明确动词")
    if any(v in task for v in VAGUE_VERBS):
        issues.append("任务说明含模糊动词")
    if not has_context:
        issues.append("缺上下文/示例")
    if not has_question:
        issues.append("缺问题")
    if not fmt:
        issues.append("缺输出格式")
    return issues

good_task = "判断下面句子的情感为积极还是消极"
bad_task = "处理下面的句子"
ctx = "# 示例1：仓库漏水，货全泡了。\\n消极\n# 示例2：新货提前三天到仓。\\n积极"
q = "司机说这趟货比预计早到两小时，客户当场加了单。"
fmt = '{"结果": " "}'

print("=== 1. 四件套体检 ===")
p = build_prompt(good_task, ctx, q, fmt)
print("拼装长度:", len(p), "字符；分隔符 ### 出现", p.count("###"), "次")
print("明确版问题清单:", check_prompt(good_task, True, True, fmt) or "无（四件套齐、动词明确）")
print("模糊版问题清单:", check_prompt(bad_task, False, True, ""))
print()

# ---------- 2. 输出格式：JSON 可解析 vs 自由文本硬抠 ----------
structured = '{"结果": "积极"}'
free_text = "这句话的情感是积极的情感。"
print("=== 2. 输出格式可用性 ===")
print("JSON 解析:", json.loads(structured)["结果"], "（一行代码直接取字段）")
m = re.search(r"是(.+?)的情感", free_text)
print("自由文本硬抠:", m.group(1) if m else "解析失败",
      "（靠正则猜位置，换个说法就抠错）")
try:
    json.loads('{"结果": 积极"}')  # 缺引号的坏 JSON
    print("坏 JSON: 居然解析成功（不应发生）")
except json.JSONDecodeError:
    print("坏 JSON: 解析报错 -> 格式不规范时程序立刻能发现，而不是静默用错")
print()

# ---------- 3. 复杂问题拆解：分步引导 + 归纳总结 ----------
# 自编题：一间小仓库一天要发多少个标准箱，才够覆盖当天的固定开支？
# 子问题1：一天固定开支是多少？ 子问题2：每个标准箱的毛利是多少？
daily_cost = 240 + 60 + 100          # 租金 240 + 人工 60 + 杂费 100 = 400 元
margin_per_box = 25 - 17             # 售价 25 - 成本 17 = 8 元/箱
boxes = daily_cost / margin_per_box  # 归纳总结
print("=== 3. 复杂问题拆解 ===")
print(f"子问题1（日固定开支）: 240+60+100 = {daily_cost} 元")
print(f"子问题2（单箱毛利）: 25-17 = {margin_per_box} 元/箱")
print(f"归纳总结: {daily_cost} / {margin_per_box} = {boxes:.0f} 箱/天才保本")
print()

# ---------- 4. CoT 适用性决策（教材三因素的规则版） ----------
def cot_advice(task_kind, params_b, reasoning_tuned):
    """task_kind: reasoning（多步推理）/ simple（一步分类问答）
    params_b: 参数量（十亿）；reasoning_tuned: 是否已做过推理类指令微调。"""
    if task_kind == "simple":
        return "不用 CoT：一步任务标准提示已够，硬上链只烧 token"
    if reasoning_tuned:
        return "可不用显式 CoT：推理已内化进模型，先直答、不行再加链"
    if params_b < 20:
        return "慎用 CoT：小模型链容易不连贯，可能还不如直答，先小样实测"
    return "用 CoT：多步推理 + 大模型 + 未内化推理，正是链的主场"

cases = [
    ("情感分类", "simple", 1750, False),
    ("多步算术", "reasoning", 1750, False),
    ("多步算术", "reasoning", 13, False),
    ("多步算术", "reasoning", 1750, True),
]
print("=== 4. CoT 适用性决策 ===")
for name, kind, pb, tuned in cases:
    print(f"{name}（{pb}B 参数, 推理微调={tuned}）-> {cot_advice(kind, pb, tuned)}")
