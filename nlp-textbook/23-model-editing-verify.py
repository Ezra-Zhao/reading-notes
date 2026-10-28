"""NLP 拆书 23 验证脚本：模型编辑简介（clean-room 自写）
对应教材 5.1 节（书页 186-194）。不依赖任何真实大模型，
用一个字典式玩具模型把本节可算的定义与公式逐项验清：

1) 定义 5.1 的分段函数：编辑后模型 M* 在目标问题与相关问题上
   输出新答案 yk，在无关问题上原样转发编辑前模型 M 的输出。
2) 四个带公式的性质：准确性式 (5.1)、泛化性式 (5.2)、
   可迁移性式 (5.3)、局部性式 (5.4)，在斑马示例上逐项复算；
   并演示一个"只背原句"的坏编辑：Acc=1 但 Gen/Port 不满。
3) 朴素微调式坏编辑的副作用：把"黑色"过度泛化到无关问题，
   局部性 Loc 掉分——量化"牵一发而动全身"。
4) 知识关联的涟漪：知识点连通图上，一次编辑的波及范围
   随跳数扩大，说明范围控制为何是核心挑战。
5) 表 5.1 数据集规模账：测试集规模排序与量级对比
   （数字逐项抄自教材表 5.1）。
固定逻辑，无随机性，可复现。
"""

# ---------- 玩具模型：字典式问答 ----------
BASE = {
    "斑马的皮肤是什么颜色的？": "肉色",          # 编辑前的错误答案（教材图 5.1）
    "剃毛后的斑马是什么颜色的？": "肉色",          # 泛化问法，编辑前同样答错
    "请告诉我斑马的肤色": "肉色",
    "皮肤颜色为黑色的马是什么马？": "斑马",        # 可迁移：反向问题，答案不是"黑色"
    "斑马的皮肤颜色是否与其毛发颜色相同？": "不相同",  # 可迁移：推理问题
    "黑白条纹相间的马的皮肤是什么颜色的？": "这种马是斑马，皮肤是黑色的",  # 可迁移：实体替换，答案 yi 是整句、不同于 yk
    "赤兔马的皮肤是什么颜色的？": "赤红色",        # 局部性：无关问题
    "斑马喜欢吃什么？": "草",
    "鸵鸟会飞吗？": "不会",
}

XK = "斑马的皮肤是什么颜色的？"
YK = "黑色"

def base_model(x):
    return BASE[x]

# ---------- 1. 定义 5.1：分段函数 ----------
print("=== 1. 定义 5.1：编辑后模型是分段函数 ===")
RELATED = {XK, "剃毛后的斑马是什么颜色的？", "请告诉我斑马的肤色"}

def edited_model(x):
    """M*(x) = yk 若 x=xk 或与 xk 相关；否则 M(x)。"""
    if x in RELATED:
        return YK
    return base_model(x)

for q in [XK, "请告诉我斑马的肤色", "斑马喜欢吃什么？"]:
    print(f"  {q} -> 编辑前 {base_model(q)} / 编辑后 {edited_model(q)}")
assert edited_model(XK) == YK
assert edited_model("斑马喜欢吃什么？") == base_model("斑马喜欢吃什么？")
print("断言通过：相关问题改答新答案，无关问题原样转发。")
print()

# ---------- 2. 四个性质公式 ----------
print("=== 2. 四个性质：式 (5.1)-(5.4) 在斑马示例上复算 ===")
DG = [("剃毛后的斑马是什么颜色的？", YK), ("请告诉我斑马的肤色", YK)]  # 泛化集：答案同为 yk
DP = [("皮肤颜色为黑色的马是什么马？", "斑马"),
      ("斑马的皮肤颜色是否与其毛发颜色相同？", "不相同"),
      ("黑白条纹相间的马的皮肤是什么颜色的？", "这种马是斑马，皮肤是黑色的")]  # 可迁移集：答案 yi != yk（逐题自有答案）
DL = ["赤兔马的皮肤是什么颜色的？", "斑马喜欢吃什么？", "鸵鸟会飞吗？"]  # 局部性集：与 xk 无关

def ind(cond):
    return 1 if cond else 0

acc = ind(edited_model(XK) == YK)
gen = sum(ind(edited_model(x) == y) for x, y in DG) / len(DG)
port = sum(ind(edited_model(x) == y) for x, y in DP) / len(DP)
loc = sum(ind(edited_model(x) == base_model(x)) for x in DL) / len(DL)
print(f"理想编辑：Acc={acc:.2f} Gen={gen:.2f} Port={port:.2f} Loc={loc:.2f}")

def lazy_model(x):
    """坏编辑：只背下原句，换个问法就露馅；可迁移题一律回 yk。"""
    if x == XK:
        return YK
    if x in RELATED:
        return base_model(x)
    if x in {q for q, _ in DP}:
        return YK
    return base_model(x)

acc2 = ind(lazy_model(XK) == YK)
gen2 = sum(ind(lazy_model(x) == y) for x, y in DG) / len(DG)
port2 = sum(ind(lazy_model(x) == y) for x, y in DP) / len(DP)
loc2 = sum(ind(lazy_model(x) == base_model(x)) for x in DL) / len(DL)
print(f"背原句的坏编辑：Acc={acc2:.2f} Gen={gen2:.2f} Port={port2:.2f} Loc={loc2:.2f}")
print("结论：Acc 满分不等于编辑成功——只背原句时 Gen=0、可迁移题全错 Port 低，")
print("这正是教材把四性质分开度量的原因：准确性只是入场券。")
print()

# ---------- 3. 过度泛化的局部性代价 ----------
print("=== 3. 朴素微调式坏编辑：改过头，局部性掉分 ===")
def overfit_model(x):
    """把'黑色'当成一切皮肤问题的答案（过拟合到单个知识点的示意）。"""
    if "皮肤" in x or "肤色" in x:
        return YK
    return base_model(x)

loc3 = sum(ind(overfit_model(x) == base_model(x)) for x in DL) / len(DL)
hit = [x for x in DL if overfit_model(x) != base_model(x)]
print(f"过度泛化编辑：Loc={loc3:.2f}，被误伤的无关问题 = {hit}")
print("结论：编辑范围放得越宽，Gen 可能越好看，Loc 掉得越狠；")
print("五性质要在同一张成绩单上一起看，单看一项都会被骗。")
print()

# ---------- 4. 知识涟漪：波及范围随跳数扩大 ----------
print("=== 4. 知识涟漪：牵一发而动全身的图上演示 ===")
GRAPH = {
    "斑马皮肤颜色": ["斑马毛发颜色", "斑马物种特征"],
    "斑马毛发颜色": ["黑白条纹成因"],
    "斑马物种特征": ["马科动物分类", "斑马食性"],
    "黑白条纹成因": ["伪装与驱虫假说"],
    "马科动物分类": ["赤兔马归属"],
    "斑马食性": [],
    "伪装与驱虫假说": [],
    "赤兔马归属": [],
}
def ripple(start, hops):
    seen, frontier = {start}, {start}
    for _ in range(hops):
        nxt = {v for u in frontier for v in GRAPH.get(u, [])} - seen
        seen |= nxt
        frontier = nxt
    return seen - {start}

for h in [1, 2, 3]:
    r = ripple("斑马皮肤颜色", h)
    print(f"  {h} 跳内波及知识点数 = {len(r)}：{sorted(r)}")
print("结论：知识点不是孤岛；编辑范围的判定本质是在关联图上划界，")
print("划小了泛化不够，划大了局部性受伤——定义 5.1 里'相关/无关'四个字最难。")
print()

# ---------- 5. 表 5.1 数据集规模账 ----------
print("=== 5. 表 5.1 数据集规模账（测试集，数字抄自教材表 5.1） ===")
TABLE51 = {
    "zsRE": 244173, "COUNTERFACT": 21919, "WikiGen": 68000,
    "T-REx-1000": 1000, "ParaRel": 253448, "NQ-SituatedQA": 67000,
    "MQuAKE-CF": 9218, "FEVER": 10444, "ConvSent": 15989,
    "VitaminC-FC": 55197, "SCOTUS": 931,
}
ranked = sorted(TABLE51.items(), key=lambda kv: -kv[1])
for name, n in ranked[:5]:
    print(f"  {name}: 测试集 {n:,}")
print(f"  最大 ParaRel 与最小 SCOTUS 之比 = {ranked[0][1]/TABLE51['SCOTUS']:.1f} 倍")
print(f"  zsRE 训练集 = 测试集 = 244,173（表内少见的等量配置，抄自表 5.1）")
print("结论：评测集从千级到二十五万级不等，跨论文比编辑成绩前先对齐数据集与口径。")
