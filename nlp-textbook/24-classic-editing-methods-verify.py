"""NLP 拆书 24 验证脚本：模型编辑经典方法（clean-room 自写）
对应教材 5.2 节（书页 194-204）。不依赖任何真实大模型，
用玩具机制把本节可算、可复现的五件事逐项验清：

1) 知识缓存法路由：门控单元判相关/不相关，相关走推理模块、
   不相关走原始模型（教材图 5.5 斑马/鸵鸟例子）。
2) 附加参数法：FFN 键值存储体 + 补丁项 ap*vp——补丁只在被
   激活时改输出、无关输入激活近零；参数账：补丁远小于本体。
3) 元学习双层优化式 (5.5) 的玩具数值版：先有元知识时，
   新编辑任务内层收敛步数明显少于从零开始。
4) 定位依据：FFN 键值实验的玩具复刻——key 与同模式 query
   内积大、value 经输出嵌入得到的分布与真实下文高度相关。
5) 表 5.2 方法比较账：逐项抄自教材表 5.2，统计四性质全高、
   支持批量等结论，复核正文引用。
固定逻辑，无随机性（伪随机用固定种子），可复现。
"""
import math

# ---------- 1. 知识缓存法：门控路由 ----------
print("=== 1. 知识缓存法：门控单元先判相关，再分流 ===")
EDIT_CACHE = {"斑马的肤色": "黑色"}  # 编辑缓存：知识点 -> 修正值（示意）

def base_model(q):
    return {"鸵鸟会飞吗？": "不会", "斑马的皮肤是什么颜色的？": "肉色"}.get(q, "原始模型作答")

def gate(q):
    """门控单元（示意：关键词相关性判定；真实系统用分类或噪声对比估计训练）。"""
    return any(k in q for k in ("斑马", "肤色", "皮肤", "黑色的马"))

def inference_module(q, knowledge):
    """推理模块：拿原问题 + 缓存知识，给出修正后答案（示意）。"""
    if "皮肤为黑色的马是什么马" in q:
        return "斑马"
    return knowledge

def cache_model(q):
    if gate(q):
        return inference_module(q, EDIT_CACHE["斑马的肤色"])
    return base_model(q)

cases = [("斑马的皮肤是什么颜色的？", "黑色"),
         ("皮肤为黑色的马是什么马？", "斑马"),
         ("鸵鸟会飞吗？", "不会")]
for q, want in cases:
    got = cache_model(q)
    print(f"  {q} -> 门控={'相关' if gate(q) else '不相关'} -> {got}")
    assert got == want
print("断言通过：相关问题走推理模块改答，无关问题原样走原始模型。")
print("代价提示：原始模型参数一个没动，新知识只活在缓存里——查得到才改得对。")
print()

# ---------- 2. 附加参数法：FFN 键值 + 补丁 ----------
print("=== 2. 附加参数法：补丁项 ap*vp 只在激活时改输出 ===")
# 玩具 FFN：2 个原有键值对 + 1 个补丁键值对，向量维度 3（纯手算示意）
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def relu(x):
    return x if x > 0 else 0.0

KEYS = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]       # 原有键
VALS = [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]       # 原有值（输出分布示意）
KP = [0.0, 0.0, 1.0]                             # 补丁键：只认第三个模式
VP = [0.0, 1.0, 0.0]                             # 补丁值：把输出推向第二维（新答案）
BP = 0.0

def ffn(q, with_patch):
    acts = [relu(dot(q, k)) for k in KEYS]
    out = [sum(a * v[i] for a, v in zip(acts, VALS)) for i in range(3)]
    ap = 0.0
    if with_patch:
        ap = relu(dot(q, KP) + BP)
        out = [o + ap * vp for o, vp in zip(out, VP)]
    return out, ap

q_target = [0.1, 0.1, 1.0]   # 与补丁键对齐的查询（目标知识点）
q_other = [1.0, 0.2, 0.0]    # 与补丁键正交的查询（无关问题）
o0, _ = ffn(q_target, False)
o1, ap1 = ffn(q_target, True)
o2, ap2 = ffn(q_other, True)
print(f"  目标查询：无补丁输出={[round(x,2) for x in o0]} 有补丁={[round(x,2) for x in o1]} 补丁激活 ap={ap1:.2f}")
print(f"  无关查询：补丁激活 ap={ap2:.2f}（近零 = 不误伤）")
assert ap1 > 0.9 and ap2 == 0.0
# 参数账：设本体 FFN 一层 d=4096、中间维 16384，补丁每知识点 2*d_mid 示意过高；
# 按教材口径补丁是“有限数量神经元”：每个补丁 = 1 个键向量(d) + 1 个值向量(d_model) + 1 偏置
d_in, d_model = 64, 64
patch_params = d_in + d_model + 1
base_params = d_in * 16384 + 16384 * d_model  # 仅示意一层 FFN 的量级
print(f"  参数账（示意维度）：单个补丁 {patch_params} 个参数，本体一层 FFN 约 {base_params:,} 个，占比 {patch_params/base_params:.4%}")
print("结论：附加参数法把改动收进补丁——本体冻结、补丁可训可拆；")
print("代价是补丁随知识点数增长，存储与逐个训练的账要另算（表 5.2：T-Patcher 不支持批量）。")
print()

# ---------- 3. 元学习：双层优化的玩具数值版 ----------
print("=== 3. 元学习法：有元知识时，内层收敛更快（式 5.5 玩具版） ===")
# 玩具编辑任务：把标量参数 theta 调到任务目标 t。内层 = 从起点做梯度下降。
def inner_steps(start, target, lr=0.5, tol=0.01):
    th, steps = start, 0
    while abs(th - target) > tol and steps < 1000:
        th += lr * (target - th)  # 对 0.5*(th-target)^2 的梯度步
        steps += 1
    return steps

targets = [2.0, 2.2, 1.8, 2.1, 1.9]  # 一族相近的编辑任务
cold = [inner_steps(0.0, t) for t in targets]          # 无元知识：每次从 0 开始
meta_init = sum(targets) / len(targets)                # 元知识（外层学到的好起点，示意）
warm = [inner_steps(meta_init, t) for t in targets]    # 有元知识：从好起点开始
print(f"  任务目标 {targets}")
print(f"  冷启动内层步数 {cold}（合计 {sum(cold)}）；元知识起点 {meta_init:.2f} 后步数 {warm}（合计 {sum(warm)}）")
assert sum(warm) < sum(cold)
print("结论：元训练（外层）先交一笔学费，换每次编辑（内层）少走弯路；")
print("学费本身不便宜——教材对 ENN 的评语正是大型模型上训练成本高。")
print()

# ---------- 4. 定位依据：FFN 键值实验玩具复刻 ----------
print("=== 4. 定位编辑法依据：key 认模式，value 管下文（图 5.8 玩具版） ===")
# 三个 query 前缀（示意向量）：都以“斑马的”结尾的归一类
QUERIES = {"动物园里最吸引孩子们注意的是斑马的": [0.9, 0.1],
           "研究人员正在分析斑马的": [0.85, 0.15],
           "在草原上，我们看见了一群斑马的": [0.95, 0.05],
           "厨师正在切洋葱的": [0.1, 0.9]}
K2 = [1.0, 0.0]  # 候选键向量
scores = {q: round(dot(v, K2), 2) for q, v in QUERIES.items()}
for q, s in scores.items():
    print(f"  key·query = {s:.2f}  <- {q}")
top = max(scores, key=scores.get)
assert "斑马" in top and scores["厨师正在切洋葱的"] < 0.2
# 实验 2：value 与输出嵌入相乘 -> 下文分布（示意：value 本身即分布倾向）
V2 = {"条纹": 0.62, "皮毛": 0.21, "鬃毛": 0.17}
best = max(V2, key=V2.get)
print(f"  value 对应下文分布 {V2}，最大概率词 = {best}（与真实下文‘条纹’一致）")
assert best == "条纹"
print("结论：键认出‘斑马的’这类前缀模式、值指向‘条纹’这类下文——")
print("FFN 可看作键值存储体，这正是 KN 定位知识神经元、ROME 更新整个 FFN 的出发点。")
print()

# ---------- 5. 表 5.2 方法比较账 ----------
print("=== 5. 表 5.2 方法比较（逐项抄自教材表 5.2） ===")
# (方法, 门派, 准确性, 泛化性, 可迁移性, 局部性, 支持批量)
TABLE52 = [
    ("SERAC", "知识缓存法", "高", "高", "低", "高", True),
    ("CaliNET", "附加参数法", "低", "低", None, "中", True),
    ("T-Patcher", "附加参数法", "高", "高", "高", "中", False),
    ("KE", "元学习法", "低", "低", None, "高", True),
    ("MEND", "元学习法", "中", "高", "中", "高", True),
    ("KN", "定位编辑法", "中", "低", None, "中", False),
    ("ROME", "定位编辑法", "高", "高", "高", "高", False),
    ("MEMIT", "定位编辑法", "高", "高", "高", "高", True),
]
all_high = [m[0] for m in TABLE52 if m[2] == m[3] == m[4] == m[5] == "高"]
batch = [m[0] for m in TABLE52 if m[6]]
print(f"  共 {len(TABLE52)} 个方法；四性质全高：{all_high}")
print(f"  支持批量编辑：{batch}（{len(batch)}/{len(TABLE52)}）")
print(f"  唯一四高又支持批量：{[m for m in all_high if m in batch]}")
untested_port = [m[0] for m in TABLE52 if m[4] is None]
print(f"  可迁移性未测（表中标 -）：{untested_port}")
assert all_high == ["ROME", "MEMIT"]
assert [m for m in all_high if m in batch] == ["MEMIT"]
print("结论：表内没有全能选手——SERAC 快而不能迁移，ROME 全高而不支持批量，")
print("MEMIT 是 ROME 的批量扩展版；选型先看任务要批量还是要单点极致。")
print()
print("全部断言通过。")
