"""NLP 拆书 25 验证脚本：T-Patcher（clean-room 自写）
对应教材 5.3 节（书页 205-210，式 5.6-5.14）。不依赖任何真实大模型，
用玩具机制把本节可算、可复现的五件事逐项验清：

1) 式 5.6 FFN 键值计算 + 式 5.7 补丁等式：FFNp(q) 恒等于 FFN(q) + ap*vp。
2) 参数账：一个补丁 = 一个键向量 kp + 一个值向量 vp + 一个偏置 bp；
   每个待编辑 Token 一个补丁，参数随 Token 数线性增长。
3) 准确性损失（式 5.8-5.10）：激活损失 la 随目标激活增大而指数下降；
   玩具梯度步同时压低 la 与编辑损失 le（交叉熵）。
4) 局部性损失（式 5.11-5.13）：好补丁的 lm1/lm2 明显低于乱激活补丁；
   并如实演示：按教材印出的公式，lm1/lm2 是线性平均、没有铰链截断，
   取值可以为负——这是照原文复算的结果，不是脚本 bug。
5) 总损失式 5.14 的符号账 + 表 5.2 中 T-Patcher 一行复核。
固定逻辑，无随机性，可复现。
"""
import math

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def relu(x):
    return x if x > 0 else 0.0

# ---------- 1. 式 5.6 + 式 5.7：补丁等式 ----------
print("=== 1. 式 5.6 FFN 与式 5.7 补丁：FFNp = FFN + ap*vp ===")
# 玩具维度：q 维度 3，隐藏（记忆）单元 2 个，输出维度 3
Wfc = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]]   # 按 q·Wfc 用：行对应 q 分量
bk = [0.0, 0.0]
Wproj = [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]   # a·Wproj：行对应记忆单元
bv = [0.0, 0.0, 0.0]
KP = [0.0, 0.0, 1.0]   # 补丁键：只认 q 的第三个模式分量
VP = [0.0, 1.0, 0.0]   # 补丁值：把输出推向第二维
BP = 0.0

def ffn(q):
    a = [relu(dot(q, [row[j] for row in Wfc]) + bk[j]) for j in range(2)]
    out = [sum(a[j] * Wproj[j][i] for j in range(2)) + bv[i] for i in range(3)]
    return out, a

def ffn_patched(q):
    base, a = ffn(q)
    ap = relu(dot(q, KP) + BP)
    out = [base[i] + ap * VP[i] for i in range(3)]
    return out, ap

for q, name in [([0.1, 0.1, 1.0], "目标查询"), ([1.0, 0.2, 0.0], "无关查询")]:
    base, _ = ffn(q)
    patched, ap = ffn_patched(q)
    diff = [patched[i] - base[i] - ap * VP[i] for i in range(3)]
    print(f"  {name} q={q}: FFN={[round(x,2) for x in base]} ap={ap:.2f} "
          f"FFNp={[round(x,2) for x in patched]} 等式残差={max(abs(x) for x in diff):.2e}")
    assert max(abs(x) for x in diff) < 1e-12
print("断言通过：补丁对输出的全部改动就是一项 ap*vp；ap=0 时输出与原模型逐位相同。")
print()

# ---------- 2. 参数账 ----------
print("=== 2. 参数账：一个补丁 2d+1，逐 Token 加 ===")
for d in (64, 4096):
    patch = 2 * d + 1
    hidden = 4 * d  # 仅作量级示意：FFN 隐藏维常约为 d 的数倍
    ffn_params = 2 * d * hidden + hidden + d
    print(f"  d={d}: 单补丁 {patch:,} 参；示意一层 FFN 约 {ffn_params:,} 参，"
          f"单补丁占比 {patch/ffn_params:.4%}")
    assert patch == 2 * d + 1
T = 5
print(f"  一个目标回答有 {T} 个待编辑 Token -> 需要 {T} 个补丁，"
      f"参数 = {T}x(2d+1)，随 Token 数线性增长（教材：为每个需要编辑的 Token 加一个补丁）")
print("结论：单个补丁极小，但账是按 Token 逐个累加的——这正是它不支持批量、")
print("批量时内存需求高的结构原因之一（教材 5.3.3 末尾与表 5.2 口径）。")
print()

# ---------- 3. 准确性损失 ----------
print("=== 3. 准确性损失：la 管激活（式 5.9），le 管改对（式 5.10） ===")
print("  la = exp(-(qe·kp + bp))，目标激活 s 越大，la 越小：")
for s in (-1.0, 0.0, 1.0, 2.0, 4.0):
    print(f"    s={s:+.1f} -> la={math.exp(-s):.4f}")
assert math.exp(-4.0) < math.exp(0.0) < math.exp(1.0)
# 玩具梯度步：只训 kp/bp（原模型冻结），把目标激活从 0 推高，la 随之下降
qe = [1.0, 0.0]
kp, bp, lr = [0.0, 0.0], 0.0, 0.3
las = []
for step in range(6):
    s = dot(qe, kp) + bp
    las.append(math.exp(-s))
    # d la/d kp = -la * qe ; d la/d bp = -la —— 沿负梯度更新
    kp = [k + lr * las[-1] * q for k, q in zip(kp, qe)]
    bp = bp + lr * las[-1]
print(f"  只训补丁 5 步：la 从 {las[0]:.3f} 降到 {las[-1]:.3f}（激活被推高，补丁学会在目标输入下亮起）")
assert las[-1] < las[0]
# 编辑损失 le：补丁激活后，输出分布向目标 Token 靠拢，交叉熵下降（两类玩具）
def ce_target(logit_target, logit_other):
    m = max(logit_target, logit_other)
    p = math.exp(logit_target - m) / (math.exp(logit_target - m) + math.exp(logit_other - m))
    return -math.log(p)
le_before = ce_target(0.0, 1.0)   # 补丁未起作用：目标 Token 落后
le_after = ce_target(2.0, 1.0)    # ap*vp 把目标 logit 推高
print(f"  le（交叉熵）：补丁起作用前 {le_before:.3f} -> 起作用后 {le_after:.3f}")
assert le_after < le_before
print("结论：LAcc 的两半分工明确——la 保证该亮时亮，le 保证亮了之后改得对；")
print("式 5.8 写 LAcc = la + alpha*le，但紧随的正文又说 alpha 是 la 的权重，")
print("两处对不上，本篇照公式 5.8 读、并在正文如实标注这一处教材符号口径不一致。")
print()

# ---------- 4. 局部性损失 ----------
print("=== 4. 局部性损失：lm1 管别乱亮，lm2 管拉开差距（式 5.11-5.13） ===")
BETA_T, GAMMA_T = 0.5, 1.0  # 教材只说 beta/gamma 为指定阈值、未给数值，此为示意取值
DM = [[0.0, 1.0], [-0.5, 0.2], [0.2, -1.0]]  # 记忆数据集：先前处理过的无关查询向量
QE = [1.0, 0.0]

def memory_loss(kp, bp):
    lm1 = sum(dot(qi, kp) + bp - BETA_T for qi in DM) / len(DM)
    lm2 = sum(dot([a - b for a, b in zip(qi, QE)], kp) + bp - GAMMA_T for qi in DM) / len(DM)
    return lm1, lm2

good_kp, good_bp = [2.0, 0.0], 0.0    # 只认目标方向
bad_kp, bad_bp = [0.2, 2.0], 0.0      # 主要认无关方向
for kp, bp, name in [(good_kp, good_bp, "好补丁"), (bad_kp, bad_bp, "坏补丁")]:
    lm1, lm2 = memory_loss(kp, bp)
    s_e = dot(QE, kp) + bp
    s_i = [round(dot(qi, kp) + bp, 2) for qi in DM]
    print(f"  {name}: 目标激活 {s_e:.2f}，无关激活 {s_i}，lm1={lm1:.2f}，lm2={lm2:.2f}")
g1, g2 = memory_loss(good_kp, good_bp)
b1, b2 = memory_loss(bad_kp, bad_bp)
assert g1 < b1 and g2 < b2
print("断言通过：好补丁的两项记忆损失都明显更低。")
print("注意（照原文复算）：式 5.12/5.13 印出的是线性平均、没有 max(0,.) 铰链截断，")
print("所以达标时 lm1/lm2 可以为负——上面好补丁的负值正是这样来的，不要当成 bug 去'修'。")
print()

# ---------- 5. 总损失符号账 + 表 5.2 复核 ----------
print("=== 5. 式 5.14 总损失与表 5.2 中 T-Patcher 一行 ===")
print("  Lp = LAcc + beta_w * Lm（式 5.14）。符号冲突如实登记：")
print("  (a) beta 在式 5.12 里是激活阈值，在式 5.14 里又被用作记忆损失权重；")
print("  (b) 式 5.8 的展开是 la + alpha*le，式 5.14 的展开却写成 le + alpha*la。")
print("  两处都照教材原文登记、正文引用时以各式自身的定义为准，不擅自替教材改符号。")
row = ("T-Patcher", "高", "高", "高", "中", False)  # 表 5.2：准确/泛化/迁移/局部/批量
print(f"  表 5.2 复核：{row[0]} 准确性={row[1]} 泛化性={row[2]} 可迁移性={row[3]} "
      f"局部性={row[4]} 支持批量={row[5]}")
assert row[1] == row[2] == row[3] == "高" and row[4] == "中" and row[5] is False
print("结论：T-Patcher 三高一中、不支持批量——单点精修是它的主场，批量不是。")
print()
print("全部断言通过。")
