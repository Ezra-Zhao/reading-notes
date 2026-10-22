"""NLP 拆书 17 验证脚本：Prompt 应用（clean-room 自写）
演示四件事：
1) Agent 四模块的最小闭环：配置/记忆/规划/行动，规划把大任务拆成子任务，
   行动模块按子任务调工具（查表/计算），结果写回记忆，最后汇总
2) Self-Instruct 的过滤环节：新生成的指令与任务池做词面重叠检查，
   重叠过高判为近重复、丢弃；分类任务先定标签再造输入的顺序演示
3) Text-to-SQL：自建 sqlite 小库，按问题模板生成 SQL 并真实执行；
   再演示一致性输出：多条候选 SQL 按执行结果投票，选票数最高的结果
4) GPTs 式配置拼装：Description + Instructions 本质就是一段结构化 Prompt，
   用第 16 篇的四件套体检思路检查它齐不齐
只用标准库，固定数据，可复现。
"""
import json
import re
import sqlite3
from collections import Counter

# ---------- 1. Agent 最小闭环 ----------
PROFILE = {"role": "仓库值班助理", "goal": "回答库存问题并给出补货建议"}
MEMORY = []  # 长期记忆的玩具版：只存本轮查到的事实

TOOLS = {
    "lookup_stock": lambda sku: {"A箱": 12, "B箱": 3}.get(sku, 0),
    "reorder_point": lambda sku: {"A箱": 10, "B箱": 10}.get(sku, 0),
}

def plan(task):
    """规划模块的玩具版：按关键词把任务拆成固定的子任务序列。"""
    steps = []
    for sku in ("A箱", "B箱"):
        if sku in task:
            steps.append(("lookup_stock", sku))
            steps.append(("reorder_point", sku))
    return steps

def act(steps):
    """行动模块：逐个子任务调工具，结果写回记忆。"""
    results = {}
    for tool, sku in steps:
        val = TOOLS[tool](sku)
        MEMORY.append(f"{tool}({sku})={val}")
        results.setdefault(sku, {})[tool] = val
    return results

print("=== 1. Agent 四模块闭环 ===")
print("配置模块:", PROFILE["role"], "|", PROFILE["goal"])
task = "看看A箱和B箱库存，低于补货点就提醒"
steps = plan(task)
print("规划模块拆出子任务:", steps)
res = act(steps)
for sku, r in sorted(res.items()):
    flag = "需要补货" if r["lookup_stock"] < r["reorder_point"] else "库存够"
    print(f"汇总: {sku} 库存={r['lookup_stock']} 补货点={r['reorder_point']} -> {flag}")
print("记忆模块已写入:", len(MEMORY), "条事实")
print()

# ---------- 2. Self-Instruct：生成后过滤 ----------
def bow(text):
    return set(re.findall(r"[一-鿿]|[a-z]+", text.lower()))

def max_overlap(new, pool):
    nb = bow(new)
    if not nb:
        return 0.0
    return max((len(nb & bow(old)) / len(nb) for old in pool), default=0.0)

pool = ["判断下面句子的情感是积极还是消极", "把下面的句子翻译成英文"]
candidates = ["判断下面句子的情感是积极还是消极呢", "给下面的仓库通知写一个标题"]
print("=== 2. Self-Instruct 过滤（近重复丢弃） ===")
for c in candidates:
    ov = max_overlap(c, pool)
    verdict = "丢弃（与任务池近重复）" if ov > 0.7 else "保留（新任务）"
    print(f"候选: {c} | 最高重叠={ov:.2f} -> {verdict}")
# 分类任务的数据生成顺序：先定标签，再按标签造输入，避免标签与内容对不上
label_first = {"指令": "判断句子情感", "标签": "消极", "输入": "货车晚点六小时，客户把订单退了。"}
print("分类数据（先标签后输入）:", label_first)
print()

# ---------- 3. Text-to-SQL：生成、执行、按执行结果投票 ----------
con = sqlite3.connect(":memory:")
con.executescript("""
CREATE TABLE Owners(owner_id INTEGER, name TEXT, state TEXT);
CREATE TABLE Raccoons(owner_id INTEGER, name TEXT, age INTEGER);
INSERT INTO Owners VALUES (1,'张三','CA'),(2,'李四','WA');
INSERT INTO Raccoons VALUES (1,'Peter',3),(2,'Mimi',2);
""")
question_sql = ("SELECT a.name FROM Owners AS a JOIN Raccoons AS b "
                "ON a.owner_id = b.owner_id WHERE b.name = 'Peter'")
rows = con.execute(question_sql).fetchall()
print("=== 3. Text-to-SQL ===")
print("问题: 宠物 Peter 的主人叫什么？")
print("SQL:", question_sql)
print("执行结果:", rows)

# 同一个问题（Peter 的主人叫什么）的四条候选 SQL：写法不同，结果分三组
candidates_sql = [
    question_sql,
    ("SELECT name FROM Owners WHERE owner_id IN "
     "(SELECT owner_id FROM Raccoons WHERE name = 'Peter')"),
    ("SELECT a.name FROM Owners AS a JOIN Raccoons AS b "
     "ON a.owner_id = b.owner_id WHERE b.name = 'Mimi'"),
    "SELECT name FROM Owners",
]
print("一致性投票（同一问题，按执行结果分组）:")
results = [tuple(con.execute(s).fetchall()) for s in candidates_sql]
for s, r in zip(candidates_sql, results):
    print(f"  结果={r} <- {s[:52]}...")
winner, votes = Counter(results).most_common(1)[0]
print(f"胜出结果: {winner}（{votes}/{len(results)} 票）")
print()

# ---------- 4. GPTs 式配置：本质是一段结构化 Prompt ----------
gpt_config = {
    "name": "库存小助手",
    "description": "帮小仓库查库存、算保本量、提醒补货",
    "instructions": "判断用户的需求类型；针对库存问题先查数再回答；"
                    "以 JSON 格式返回最终结果，字段为 结论 与 依据。",
}
def check_gpt(cfg):
    issues = []
    if not cfg.get("description"):
        issues.append("缺 Description（用户不知道它能干什么）")
    ins = cfg.get("instructions", "")
    if not any(v in ins for v in ("判断", "查", "返回", "计算")):
        issues.append("Instructions 缺明确动词")
    if "JSON" not in ins and "格式" not in ins:
        issues.append("Instructions 没写输出格式")
    return issues

print("=== 4. GPTs 配置体检 ===")
print("配置拼装长度:", len(json.dumps(gpt_config, ensure_ascii=False)), "字符")
print("体检结果:", check_gpt(gpt_config) or "无（描述/指令/格式齐全）")
print("空配置体检:", check_gpt({"name": "x", "description": "", "instructions": "随便聊聊"}))
