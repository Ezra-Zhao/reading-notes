"""NLP 拆书 21 验证脚本：低秩适配方法 LoRA（clean-room 自写）
演示七件事：
1) LoRA 参数账（教材式 4.9）：W = W0 + alpha*B*A，B 为 d x r、A 为 r x k，
   可训量 = r*(d+k)，远小于全量 d*k；以教材锚点 LLaMA2-7B 的 FFN 矩阵
   11008 x 4096 = 45,088,768、r=4 时 LoRA 只需 60,416 复算互证。
2) 合并等价与零初始化：A 初始化为 0 时 DeltaW = 0（教材口径：B 随机高斯、A 置零）、模型与原模型逐位一致；
   训练后把 alpha*B*A 合并回 W0，合并写法与旁路写法的前向输出逐位一致
   （推理零增负的数学根据）。
3) 低秩性质：rank(B*A) <= r，用数值秩验证增量矩阵的秩被 r 卡住。
4) 只训 A、B 的降损演示：在一个合成线性任务上冻结 W0、只训 A 与 B，
   损失显著下降并接近全量微调；同时报告两者可训量之比。
5) ReLoRA 合并-重初始化（教材式 4.10）：每训一段就把 alpha*B*A 合并进 W、
   再把 B 清零重开新一轮；多轮后总增量的秩可超过单个 r（分段低秩、累计高秩）。
6) AdaLoRA 正交正则（教材式 4.11/4.12）：DeltaW = P * Lambda * Q，
   正则项 R = ||P^T P - I||_F^2 + ||Q Q^T - I||_F^2 在 P、Q 正交时为 0、否则为正。
7) DoRA 分解（教材式 4.13）与 LoRAHub 组合（教材式 4.15）：
   DoRA 把 W0 按列拆成幅度 m 与方向 V/||V||_c，重构与原矩阵逐位一致；
   LoRAHub 按权重 w_i 线性组合多个 LoRA 的 A 与 B 再相乘，演示组合公式可算、
   且组合增量不等于各增量简单相加（交叉项的存在）。
只用标准库 + numpy，固定随机种子，可复现。
"""
import numpy as np

rng = np.random.default_rng(42)

# ---------- 1. LoRA 参数账（式 4.9） ----------
print("=== 1. LoRA 参数账：可训量 r*(d+k) 对全量 d*k ===")
def lora_params(d, k, r):
    return r * (d + k)
# 教材锚点：LLaMA2-7B 一个 FFN 矩阵 11008 x 4096，r=4
d, k, r = 11008, 4096, 4
full = d * k
lp = lora_params(d, k, r)
print(f"LLaMA2-7B FFN 矩阵 {d} x {k} = {full:,} 个参数")
print(f"r={r} 时 LoRA 可训 = ({d}x{r}) + ({r}x{k}) = {lp:,}，仅为全量的 {lp/full*100:.3f}%，省 {(full/lp):.1f} 倍")
for d2, k2, r2 in [(4096, 4096, 8), (4096, 4096, 16), (768, 768, 4)]:
    print(f"d=k={d2}, r={r2}: 全量 {d2*k2:,} vs LoRA {lora_params(d2,k2,r2):,} "
          f"({lora_params(d2,k2,r2)/(d2*k2)*100:.2f}%)")
print()

# ---------- 2. 合并等价与零初始化 ----------
print("=== 2. 零初始化与合并等价（推理零增负）===")
d, k, r, alpha = 32, 24, 4, 2.0
W0 = rng.normal(0, 0.1, size=(d, k))
B = rng.normal(0, 0.1, size=(d, r))      # B 随机高斯初始化（教材口径）
A = np.zeros((r, k))                      # A 零初始化 -> 起点 DeltaW = 0
x = rng.normal(size=(5, k))
dW0 = alpha * (B @ A)
print(f"A=0 时 DeltaW 最大绝对值 = {np.abs(dW0).max():.1e}（严格为 0，起点即原模型）")
# 模拟训练后 A、B 均不再为零
B = rng.normal(0, 0.1, size=(d, r))
A = rng.normal(0, 0.1, size=(r, k))
y_branch = x @ (W0 + alpha * (B @ A)).T if False else (W0 @ x.T).T + alpha * (B @ (A @ x.T)).T  # 旁路写法
W_merged = W0 + alpha * (B @ A)
y_merged = (W_merged @ x.T).T                                                             # 合并写法
print(f"旁路写法与合并写法前向最大差 = {np.abs(y_branch - y_merged).max():.2e}（数值误差量级，即等价）")
print("结论：训完把 alpha*B*A 加回 W0 得到单个矩阵，推理时不再多算任何一步。")
print()

# ---------- 3. 低秩性质 ----------
print("=== 3. 低秩性质：rank(B*A) <= r ===")
for r3 in [2, 4, 8]:
    A3 = rng.normal(size=(r3, 64))
    B3 = rng.normal(size=(48, r3))
    rank = np.linalg.matrix_rank(B3 @ A3)
    print(f"r={r3}: DeltaW 形状 (48, 64)，数值秩 = {rank}（<= r 成立：{rank <= r3}）")
print()

# ---------- 4. 只训 A、B 降损 ----------
print("=== 4. 只训 A、B：合成任务降损（冻结 W0）===")
# 合成任务：真实目标映射 W_true = W0 + 一个真实低秩增量（秩 3）
d, k, r_true, r = 64, 48, 3, 4
W0 = rng.normal(0, 0.3, size=(d, k))
Bt = rng.normal(0, 0.3, size=(d, r_true)); At = rng.normal(0, 0.3, size=(r_true, k))
W_true = W0 + Bt @ At
X = rng.normal(size=(256, k))
Y = X @ W_true.T
def mse(W):
    return float(np.mean((X @ W.T - Y) ** 2))
print(f"初始 MSE（只用 W0）= {mse(W0):.4f}")
# 全量微调对照（梯度下降训整个 d x k）
Wf = W0.copy(); lr = 0.02
for _ in range(500):
    G = (2 / X.shape[0]) * ((X @ Wf.T - Y).T @ X)
    Wf -= lr * G
print(f"全量微调 500 步后 MSE = {mse(Wf):.2e}（可训 {d*k} 个参数）")
# LoRA：只训 A、B
A = np.zeros((r, k)); B = rng.normal(0, 0.1, size=(d, r)); alpha = 1.0
lr = 0.02
for _ in range(500):
    pred = X @ (W0 + alpha * (B @ A)).T
    E = pred - Y                                   # (n, d)
    GA = alpha * (B.T @ ((2 / X.shape[0]) * (E.T @ X)))   # dL/dA
    GB = alpha * ((2 / X.shape[0]) * (E.T @ (X @ A.T)))    # dL/dB
    A -= lr * GA; B -= lr * GB
print(f"LoRA(r={r}) 500 步后 MSE = {mse(W0 + alpha * (B @ A)):.2e}（可训 {r*(d+k)} 个参数，为全量的 {r*(d+k)/(d*k)*100:.1f}%）")
print()

# ---------- 5. ReLoRA：合并-重初始化（式 4.10） ----------
print("=== 5. ReLoRA：分段合并后总增量秩超过单个 r ===")
d, k, r = 40, 40, 4
W = rng.normal(0, 0.1, size=(d, k))
W_start = W.copy()
for i in range(4):
    Ai = rng.normal(size=(r, k)); Bi = rng.normal(size=(d, r))
    W = W + 1.0 * (Bi @ Ai)          # 式 4.10：W_i <- W_i + alpha * B_i * A_i，随后 B、A 重初始化
total_rank = np.linalg.matrix_rank(W - W_start)
print(f"单轮秩上限 r = {r}；合并 4 轮后总增量数值秩 = {total_rank}（> r：{total_rank > r}）")
print("结论：每轮仍只训低秩增量，靠合并-重开把累计秩堆高，是 ReLoRA 逼近全量训练的机制。")
print()

# ---------- 6. AdaLoRA 正交正则（式 4.11/4.12） ----------
print("=== 6. AdaLoRA：SVD 式参数化与正交正则 ===")
d, k, r = 16, 12, 4
P = rng.normal(size=(d, r)); Q = rng.normal(size=(r, k)); lam = np.abs(rng.normal(size=r))
dW_ada = P @ np.diag(lam) @ Q
print(f"DeltaW = P diag(lambda) Q，形状 {dW_ada.shape}，数值秩 = {np.linalg.matrix_rank(dW_ada)}（<= r）")
def ortho_reg(P, Q):
    return float(np.sum((P.T @ P - np.eye(P.shape[1])) ** 2) + np.sum((Q @ Q.T - np.eye(Q.shape[0])) ** 2))
# 用 QR 造一组正交的 P、Q
P_orth, _ = np.linalg.qr(rng.normal(size=(d, r)))
Q_orth_raw, _ = np.linalg.qr(rng.normal(size=(k, r))); Q_orth = Q_orth_raw.T
print(f"随机 P、Q 的正则 R = {ortho_reg(P, Q):.3f}（> 0）")
print(f"正交 P、Q 的正则 R = {ortho_reg(P_orth, Q_orth):.2e}（约 0，与式 4.12 一致）")
print()

# ---------- 7. DoRA 分解（式 4.13）与 LoRAHub 组合（式 4.15） ----------
print("=== 7. DoRA 列范数分解与 LoRAHub 加权组合 ===")
W0 = rng.normal(0, 0.5, size=(8, 6))
m = np.linalg.norm(W0, axis=0, keepdims=True)          # m in R^{1 x k}：每列的幅度
V_dir = W0 / m                                          # 方向矩阵：每列单位范数
W_recon = m * V_dir
print(f"m 形状 = {m.shape}（1 x k）；重构与原矩阵最大差 = {np.abs(W_recon - W0).max():.2e}（逐位一致）")
print(f"方向矩阵每列范数 = {np.round(np.linalg.norm(V_dir, axis=0), 6)}（全为 1）")
# LoRAHub：两个现成 LoRA 模块，按权重组合 A 与 B 再相乘（式 4.15）
r = 3; d, k = 8, 6
A1 = rng.normal(size=(r, k)); B1 = rng.normal(size=(d, r))
A2 = rng.normal(size=(r, k)); B2 = rng.normal(size=(d, r))
w1, w2 = 0.7, 0.3
m_combined = (w1 * B1 + w2 * B2) @ (w1 * A1 + w2 * A2)   # (sum w_i B_i)(sum w_i A_i)
naive_sum = w1 * (B1 @ A1) + w2 * (B2 @ A2)
cross = w1 * w2 * (B1 @ A2 + B2 @ A1)
print(f"LoRAHub 组合增量与朴素加权和之差 = {np.abs(m_combined - (w1**2 * (B1 @ A1) + w2**2 * (B2 @ A2) + cross)).max():.2e}")
print(f"组合增量 != 朴素加权和：最大差 = {np.abs(m_combined - naive_sum).max():.4f}（交叉项 w1*w2*(B1A2+B2A1) 真实存在）")
print("结论：LoRAHub 组合的是 A、B 两侧因子而非增量本身，权重需另行学得，不能当成增量的简单平均。")
