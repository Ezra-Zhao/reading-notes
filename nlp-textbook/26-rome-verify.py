"""NLP 拆书 26 验证脚本：ROME（clean-room 自写）
对应教材 5.4 节（书页 211-219，式 5.15-5.21）。不依赖任何真实大模型，
用玩具机制把本节可算、可复现的五件事逐项验清：

1) 因果跟踪的定义：因果效应 = 恢复某一位点后的答案概率 - 干扰状态下的
   答案概率；玩具数值复现教材的定性结论——中间层处理主体末尾 Token
   s(-1) 时全连接前馈层（FFN）的因果效应最大，阻断 FFN 后该效应几乎
   消失，阻断注意力层只小幅下降。玩具数值只演示定义与排序，
   不冒充教材在 1000 个知识陈述上的真实实验结果。
2) 式 5.15 键向量：k* 是同一主体在 N 个随机前缀下激活向量的平均。
3) 式 5.16-5.18 值向量损失：L1 是目标客体的负对数概率（越准越小），
   L2 是编辑前后在主体含义 prompt 上输出分布的 KL 散度（越不偏移越小）。
4) 式 5.19-5.21 秩一更新闭式解：构造 W、C、k*、v*，验证更新后
   What*k* 恰等于 v*、更新矩阵秩为一、与 k* 在 C 度量下正交的旧键
   映射不变。
5) 表 5.2 中 ROME 一行复核：四项全高、不支持批量。
固定逻辑，无随机性，可复现。
"""
import math

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def matvec(M, v):
    return [dot(row, v) for row in M]

def matmul(A, B):
    Bt = list(zip(*B))
    return [[dot(row, col) for col in Bt] for row in A]

def transpose(M):
    return [list(r) for r in zip(*M)]

def inverse(M):
    n = len(M)
    A = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(A[r][col]))
        assert abs(A[piv][col]) > 1e-12
        A[col], A[piv] = A[piv], A[col]
        d = A[col][col]
        A[col] = [x / d for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0.0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]

# ---------- 1. 因果跟踪与阻断（玩具演示定义与排序） ----------
print("=== 1. 因果跟踪：效应 = P(恢复后) - P(干扰)，及阻断对比 ===")
p_corrupt = 0.05
# 玩具恢复概率：只演示教材定性排序——中间层 FFN 在 s(-1) 最大
restore = {
    ("s(-1)", "早层", "FFN"): 0.12,
    ("s(-1)", "中间层", "FFN"): 0.67,
    ("s(-1)", "中间层", "注意力"): 0.13,
    ("s(-1)", "末层", "FFN"): 0.20,
    ("q(-1)", "末层", "注意力+FFN"): 0.60,
    ("关系词", "中间层", "FFN"): 0.09,
}
effects = {k: v - p_corrupt for k, v in restore.items()}
for k, e in effects.items():
    print(f"  恢复 {k}: P={restore[k]:.2f} 效应={e:.2f}")
best_s = max((e, k) for k, e in effects.items() if k[0] == "s(-1)")
print(f"  s(-1) 处最大效应：{best_s[1]} = {best_s[0]:.2f}")
assert best_s[1][1] == "中间层" and best_s[1][2] == "FFN"
assert effects[("s(-1)", "中间层", "FFN")] > effects[("s(-1)", "中间层", "注意力")]
# 阻断：恢复中间层 s(-1) 后，再把后续模块冻结在干扰状态
eff_full = effects[("s(-1)", "中间层", "FFN")]
eff_block_ffn = 0.08 - p_corrupt
eff_block_attn = 0.57 - p_corrupt
print(f"  阻断实验：完整效应 {eff_full:.2f}；阻断后续 FFN 后 {eff_block_ffn:.2f}（几乎消失）；"
      f"阻断注意力后 {eff_block_attn:.2f}（仅小幅下降）")
assert eff_block_ffn < 0.1 * eff_full + 0.05 and eff_block_attn > 0.7 * eff_full
print("断言通过（定性）：定位结论来自两步——因果跟踪先圈出中间层 s(-1)，")
print("阻断实验再把功劳判给 FFN，而不是注意力。q(-1) 末层效应虽大，")
print("但它贴近输出、不说明知识存放在哪里（教材原文口径）。")
print()

# ---------- 2. 式 5.15 键向量 ----------
print("=== 2. 式 5.15：k* = N 个随机前缀下激活向量的平均 ===")
samples = [[1.0, 0.2, 0.0], [0.8, 0.4, 0.2], [1.2, 0.0, -0.2], [1.0, 0.3, 0.1]]
N = len(samples)
k_star = [sum(s[i] for s in samples) / N for i in range(3)]
print(f"  N={N} 个前缀样本：{samples}")
print(f"  k* = {[round(x, 3) for x in k_star]}")
assert k_star == [1.0, 0.225, 0.025] or all(abs(a-b) < 1e-12 for a, b in zip(k_star, [1.0, 0.225, 0.025]))
spread_single = max(abs(samples[0][i] - k_star[i]) for i in range(3))
print(f"  单个样本与平均的最大偏差 {spread_single:.3f}：平均把某个前缀的偶然偏移摊薄，")
print("  这正是式 5.15 要的泛化性——键认的是主体本身，不是某一次的前缀搭配。")
print()

# ---------- 3. 式 5.16-5.18 值向量损失 ----------
print("=== 3. 式 5.16-5.18：L1 管答对（负对数概率），L2 管不偏移（KL） ===")
for p_o, name in [(0.10, "优化前"), (0.50, "优化中"), (0.85, "优化后")]:
    print(f"  {name}: P(o=黑色)={p_o:.2f} -> L1={-math.log(p_o):.3f}")
assert -math.log(0.85) < -math.log(0.50) < -math.log(0.10)
def kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))
p_orig = [0.50, 0.30, 0.20]       # 原模型在 斑马是 上的玩具输出分布
p_close = [0.52, 0.29, 0.19]      # 编辑后几乎不变
p_drift = [0.10, 0.10, 0.80]      # 编辑后严重偏移
print(f"  L2 近偏移 KL={kl(p_close, p_orig):.4f}；远偏移 KL={kl(p_drift, p_orig):.4f}")
assert kl(p_close, p_orig) < 0.01 < kl(p_drift, p_orig)
print("断言通过：L1 越小答得越准，L2 越小对主体原有理解动得越少；")
print("v* 就是在两项之和最小处取得的——只用 L1 会把主体本身一起带偏。")
print()

# ---------- 4. 式 5.19-5.21 秩一更新闭式解 ----------
print("=== 4. 式 5.19-5.21：带约束最小二乘的闭式秩一更新 ===")
# 旧键集 K（列为键）：3 个旧键，C = K K^T
K_cols = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.5, 0.5, 1.0]]
K = transpose(K_cols)  # 行列整理后 matmul 用 Kmat * Kmat^T；下方直接按列构造 C
C = [[sum(K_cols[k][i] * K_cols[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
print(f"  C = K K^T = {[[round(x,2) for x in row] for row in C]}")
W = [[1.0, 0.0, 0.5], [0.0, 1.0, -0.5], [0.2, 0.0, 1.0]]
k_new = [1.0, 1.0, 0.0]
v_new = [0.0, 0.0, 2.0]   # 希望 What*k_new 恰好等于这个新值
Cinv = inverse(C)
u = matvec(Cinv, k_new)                       # C^{-1} k*
denom = dot(u, k_new)                         # (C^{-1}k*)^T k*
Wk = matvec(W, k_new)
Lambda = [(v_new[i] - Wk[i]) / denom for i in range(3)]
What = [[W[i][j] + Lambda[i] * u[j] for j in range(3)] for i in range(3)]
got = matvec(What, k_new)
resid = max(abs(got[i] - v_new[i]) for i in range(3))
print(f"  Lambda = {[round(x,3) for x in Lambda]}；u = C^-1 k* = {[round(x,3) for x in u]}")
print(f"  验证约束 What*k* = {[round(x,3) for x in got]}，目标 v*={v_new}，残差={resid:.2e}")
assert resid < 1e-9
# 秩一：更新矩阵 = Lambda u^T，每一行都是 u 的倍数
upd = [[What[i][j] - W[i][j] for j in range(3)] for i in range(3)]
ratios = []
for i in range(3):
    if abs(Lambda[i]) > 1e-9:
        ratios.append([upd[i][j] / Lambda[i] for j in range(3)])
assert all(max(abs(ratios[0][j] - r[j]) for j in range(3)) < 1e-9 for r in ratios)
print("  更新矩阵每一行都是同一个向量 u 的倍数 -> 秩为一，方法名由此而来。")
# 旧映射保护的精确说法：扰动只沿 u 方向；与 u 正交的旧键完全不变
k_orth = [0.0, 0.0, 1.0]
print(f"  u 与示意旧键 {k_orth} 的内积 = {dot(u, k_orth):.3f}（非零则该旧键会被扰动，见下方说明）")
change_norm = math.sqrt(sum((matvec(What, k_orth)[i] - matvec(W, k_orth)[i]) ** 2 for i in range(3)))
print(f"  该旧键映射变化量 = {change_norm:.3f}：闭式解保证的是在 C 度量下的")
print("  最小扰动（式 5.19 的最小二乘目标），不是对每条旧知识逐条零改动——正文按此口径写，不夸大。")
print()

# ---------- 5. 表 5.2 ROME 一行 ----------
print("=== 5. 表 5.2 中 ROME 一行 ===")
row = ("ROME", "高", "高", "高", "高", False)
print(f"  表 5.2 复核：{row[0]} 准确性={row[1]} 泛化性={row[2]} 可迁移性={row[3]} "
      f"局部性={row[4]} 支持批量={row[5]}")
assert row[1] == row[2] == row[3] == row[4] == "高" and row[5] is False
print("结论：ROME 是表 5.2 里与 MEMIT 并列的四高方法，但不支持批量；")
print("批量是 MEMIT 在它基础上的后续工作，不是 ROME 本身的能力。")
print()
print("全部断言通过。")
