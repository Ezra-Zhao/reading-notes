"""NLP 拆书 22 验证脚本：PEFT 实践与应用（clean-room 自写）
对应教材 4.5 节（书页 174-178）。不依赖 transformers/peft 库，
用纯标准库 + numpy 把本节可算的账与可复现的机制逐项验清：

1) 三类配置的参数账：Prompt Tuning 的 num_virtual_tokens、
   Prefix Tuning 的逐层前缀、LoRA 的 r / target_modules，
   按教材给的旋钮口径复算可训量，说明"旋钮即账单"。
2) 配置校验（仿 HF-PEFT 风格的本地校验器）：缩放 alpha/r、
   dropout 合法区间、虚拟词数 10-20 建议区间、目标模块名合法性，
   非法配置必须被拦下，合法配置放行。
3) FinSQL 第一段"提示构造"里的表列检索：用词重叠打分从多张表里
   挑出与问题相关的表与字段（检索器机制的最小复现）。
4) FinSQL 第三段"输出校准"：候选 SQL 先做语法小修（全角符号、
   多余空格、关键字大小写归一），再用 Self-Consistency 多数投票
   选出一致答案；演示投票能压过单个错误候选。
5) TabLLM 的表格序列化：一行表格 -> 一句自然语言，
   并拼出少样本提示（序列化文本 + 问题 + 答案槽），
   与教材图 4.11 的句式逐项对齐（自编数据）。
6) 插件仓库的存储账（FinSQL 用 LoRAHub 融合多 LoRA 的前提）：
   一份底座 + N 份小 LoRA 文件，对比 N 份全量模型副本的总存储。
固定随机种子，可复现。
"""
import re
from collections import Counter

# ---------- 1. 三类配置的参数账 ----------
print("=== 1. 三类配置的参数账：旋钮即账单 ===")
hidden, layers, vocab_note = 4096, 32, ""
# Prompt Tuning：只训 num_virtual_tokens 个虚拟词的嵌入
for nvt in [10, 20]:
    print(f"Prompt Tuning: num_virtual_tokens={nvt} -> 可训 = {nvt} x {hidden} = {nvt*hidden:,}")
# Prefix Tuning：每层为 key 与 value 各备一份前缀（简化口径：2 * nvt * hidden / 层）
for nvt in [10, 20]:
    per_layer = 2 * nvt * hidden
    print(f"Prefix Tuning: num_virtual_tokens={nvt} -> 每层 {per_layer:,}，{layers} 层共 {per_layer*layers:,}"
          f"（约为 Prompt Tuning 的 {per_layer*layers//(nvt*hidden)} 倍，贵在逐层）")
# LoRA：可训量 = 目标矩阵数 x r x (d+k)；以 4096x4096 方阵、每层 q/k/v/o 四个矩阵为例
def lora_trainable(r, n_mat, d=4096, k=4096):
    return n_mat * r * (d + k)
for r in [4, 8, 16]:
    qv = lora_trainable(r, 2) * layers
    all4 = lora_trainable(r, 4) * layers
    print(f"LoRA r={r}: 只挂 q,v 每层 {lora_trainable(r,2):,}，全模型 {qv:,}；"
          f"挂 q,k,v,o 全模型 {all4:,}（目标模块翻倍，账单翻倍）")
print("缩放系数 alpha/r（教材：lora_alpha 控制权重大小）：")
for r, alpha in [(4, 8), (8, 16), (16, 16)]:
    print(f"  r={r}, alpha={alpha} -> 有效缩放 {alpha/r:.2f}")
print()

# ---------- 2. 配置校验（仿 HF-PEFT 风格） ----------
print("=== 2. 配置校验：非法配置必须被拦下 ===")
VALID_TARGETS = {"q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"}

def validate_lora_config(cfg):
    errs = []
    if cfg["r"] <= 0:
        errs.append("r 必须为正")
    if cfg["lora_alpha"] <= 0:
        errs.append("lora_alpha 必须为正")
    if not (0.0 <= cfg["lora_dropout"] < 1.0):
        errs.append("lora_dropout 必须在 [0,1) 内")
    bad = [m for m in cfg["target_modules"] if m not in VALID_TARGETS]
    if bad:
        errs.append(f"未知目标模块: {bad}")
    return errs

def validate_prompt_config(cfg):
    warns = []
    if not (10 <= cfg["num_virtual_tokens"] <= 20):
        warns.append(f"num_virtual_tokens={cfg['num_virtual_tokens']} 在教材建议区间 10-20 之外")
    if cfg["prompt_tuning_init"] not in {"RANDOM", "TEXT"}:
        warns.append("prompt_tuning_init 只接受 RANDOM / TEXT")
    return warns

good = {"r": 8, "lora_alpha": 16, "lora_dropout": 0.01, "target_modules": ["q_proj", "v_proj"]}
bad = {"r": 8, "lora_alpha": 16, "lora_dropout": 1.5, "target_modules": ["q_proj", "bogus_proj"]}
print(f"合法 LoRA 配置校验错误数 = {len(validate_lora_config(good))}（应为 0）")
print(f"非法 LoRA 配置被拦: {validate_lora_config(bad)}")
print(f"虚拟词数 20 的提示配置警告 = {validate_prompt_config({'num_virtual_tokens': 20, 'prompt_tuning_init': 'TEXT'})}（应为空）")
print(f"虚拟词数 100 的提示配置警告 = {validate_prompt_config({'num_virtual_tokens': 100, 'prompt_tuning_init': 'TEXT'})}")
print()

# ---------- 3. 表列检索（FinSQL 提示构造的最小复现） ----------
print("=== 3. 表列检索：先挑相关的表，再让模型写 SQL ===")
SCHEMA = {
    "accounts": ["account_id", "holder_name", "balance", "open_date"],
    "loans": ["loan_id", "account_id", "amount", "interest_rate", "status"],
    "stocks": ["stock_id", "symbol", "price", "trade_date"],
}
QUESTION = "find accounts whose balance is above 10000 and list holder name"
STOP = {"find", "whose", "is", "and", "list", "the", "a"}
qwords = {w for w in re.findall(r"[a-z_]+", QUESTION.lower())} - STOP
def score_table(cols):
    hits = sum(1 for c in cols if any(w in c or c in w for w in qwords))
    return hits
ranked = sorted(SCHEMA.items(), key=lambda kv: -score_table(kv[1]))
for name, cols in ranked:
    print(f"  表 {name}: 命中字段数 = {score_table(cols)}，字段 = {cols}")
top_table, top_cols = ranked[0]
kept = [c for c in top_cols if any(w in c or c in w for w in qwords)] or top_cols
print(f"检索结果：主表 = {top_table}，带入提示的字段 = {kept}（无关表 stocks/loans 不进提示，省上下文）")
print()

# ---------- 4. 输出校准 + Self-Consistency（FinSQL 第三段） ----------
print("=== 4. 输出校准与自洽投票：先修语法，再投票 ===")
def calibrate(sql):
    s = sql.replace("；", ";").replace("，", ",").replace("＝", "=")
    s = re.sub(r"\s+", " ", s).strip().rstrip(";")
    # 关键字归一为大写（只处理句首与常见关键字，避免动到字符串内容；本演示候选均为简单句）
    for kw in ["select", "from", "where"]:
        s = re.sub(rf"\b{kw}\b", kw.upper(), s, flags=re.I)
    return s

candidates_raw = [
    "select holder_name from accounts where balance > 10000",
    "SELECT holder_name FROM accounts WHERE balance > 10000；",
    "SELECT holder_name FROM accounts WHERE balance > 10000",
    "SELECT holder_name FROM accounts WHERE balance > 5000",
    "SELECT  holder_name  FROM  accounts  WHERE  balance  >  10000",
]
calibrated = [calibrate(c) for c in candidates_raw]
for raw, cal in zip(candidates_raw, calibrated):
    fixed = "（已修）" if raw != cal else ""
    print(f"  候选: {cal} {fixed}")
winner, votes = Counter(calibrated).most_common(1)[0]
print(f"自洽投票胜出（{votes}/5 票）: {winner}")
print("结论：同一问题采样多条 SQL，执行结果/文本一致者占多数时，偶发错误被投票压过。")
print()

# ---------- 5. TabLLM 序列化 ----------
print("=== 5. TabLLM 序列化：一行表格变成一句话 ===")
def serialize_row(row):
    parts = []
    label = {"age": "age", "education": "education", "gain": "gain"}
    for col in ["age", "education", "gain"]:
        parts.append(f"The {label[col]} is {row[col]}.")
    return " ".join(parts)

row = {"age": 42, "education": "Master", "gain": 594}
sent = serialize_row(row)
print(f"序列化结果: {sent}")
assert sent == "The age is 42. The education is Master. The gain is 594."
few_shot = (
    "The age is 28. The education is Master. The gain is 1024. "
    "Question: Does this person earn more than 50000 dollars? Yes or no? Answer: Yes\n"
    + sent + " Question: Does this person earn more than 50000 dollars? Yes or no? Answer:"
)
print("少样本提示拼装（1 个示例 + 待答行）:")
print(f"  {few_shot}")
print(f"提示总词数（空格切分）= {len(few_shot.split())}：表格没有被喂成表格，是被'翻译'成了模型最熟的自然语言。")
print()

# ---------- 6. 插件仓库存储账 ----------
print("=== 6. 插件仓库存储账：一份底座 + N 份小文件 ===")
base_gb = 14.0          # 7B 模型半精度约 14GB（量级演示）
lora_mb = 80.0          # 一份 LoRA 文件量级演示（r 与挂载范围不同会变）
for n in [1, 10, 100]:
    hub = base_gb + n * lora_mb / 1024
    full = n * base_gb
    print(f"任务数 N={n}: 插件仓库式 = {hub:.1f} GB vs 全量副本式 = {full:.0f} GB（省 {full/hub:.1f} 倍）")
print("结论：FinSQL 能用 LoRAHub 融合多个 LoRA，前提正是适配成果被存成可组合的小文件，而非整模型副本。")
