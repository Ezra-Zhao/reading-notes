"""NLP 拆书 20 验证脚本：参数选择方法（clean-room 自写）
演示五件事：
1) BitFit 参数账：按 BERT-base 量级逐项数权重与偏置——只训偏置时可训量
   约为万分之九，与教材 0.08%-0.09% 同一量级（差异在归一化偏置是否计入）；
   分类头另计、量级可忽略。
2) 基于规则的「只训顶层」：只训最后 1/4 层时，可训量 = 全部层参数的 25%
   （占整模型约五分之一），教材称其可达全量微调约 90% 的性能。
3) PaFi 选参：从一张权重矩阵里挑绝对值最小的 1% 当可训参数，
   验证被挑中者的平均绝对值远小于全体（挑的是「最轻」的参数）。
4) Child-tuning_F：伯努利掩码 M_t ~ Bernoulli(p_F) 逐元素屏蔽梯度（式 4.7），
   被屏蔽的参数在掩码梯度更新（式 4.6）后逐位不变；掩码每步重抽，
   长期看每个参数都会轮到（随机正则的覆盖面）。
5) Child-tuning_D：用费舍尔信息（式 4.8，梯度平方的样本平均）给参数排重要性，
   取前 p_D 比例组成子网络 C；在一个只有前 4 维带任务信号的合成任务上，
   验证 Fisher 排序能把带信号的维度挑进子网络，且只训子网络即可显著降损。
只用标准库 + numpy，固定随机种子，可复现。
"""
import numpy as np

rng = np.random.default_rng(42)

# ---------- 1. BitFit 参数账（BERT-base 量级） ----------
print("=== 1. BitFit 参数账 ===")
d, ffn, L, vocab = 768, 3072, 12, 30522
# 每层权重：QKV 3d^2 + 注意力输出 d^2 + FFN 两个矩阵 d*ffn + ffn*d
layer_w = 3 * d * d + d * d + 2 * d * ffn
# 每层偏置：QKV 3d + 注意力输出 d + FFN ffn+d + 两处 LayerNorm 2d
layer_b = 3 * d + d + ffn + d + 2 * d
emb = vocab * d + 512 * d + 2 * d + 2 * d          # 词/位置/类型嵌入 + 嵌入层 LN(含偏置2d近似)
pooler = d * d + d                                  # 池化层权重+偏置
total = emb + L * (layer_w + layer_b) + pooler
bias_total = L * layer_b + d + d                    # 各层偏置 + 池化偏置 + 嵌入 LN 偏置
head = d * 2 + 2                                    # 二分类头（权重+偏置）
print(f"整模型总参数 ≈ {total:,}")
print(f"全部偏置 ≈ {bias_total:,}，占比 = {bias_total/total*100:.3f}%（教材口径 0.08%-0.09%）")
print(f"分类头另计 {head:,} 个，与偏置合计占比 = {(bias_total+head)/total*100:.3f}%")
print()

# ---------- 2. 只训最后 1/4 层 ----------
print("=== 2. 规则选层：只训最后 1/4 层 ===")
top_layers = L // 4
top_params = top_layers * (layer_w + layer_b)
print(f"只训最后 {top_layers}/{L} 层：可训 = {top_params:,}，占全部层参数的 "
      f"{top_params/(L*(layer_w+layer_b))*100:.1f}%，占整模型 {top_params/total*100:.1f}%")
print("教材口径：Lee 等人只训 BERT/RoBERTa 最后四分之一层，可达全量微调约 90% 的性能。")
print()

# ---------- 3. PaFi：挑绝对值最小的参数 ----------
print("=== 3. PaFi：挑 |w| 最小者 ===")
W = rng.normal(0, 0.02, size=(768, 768))
k = int(0.01 * W.size)
flat = np.abs(W).ravel()
thresh = np.partition(flat, k)[k]
mask_pafi = np.abs(W) <= thresh
print(f"矩阵 {W.shape} 共 {W.size:,} 个参数，挑最小 1% = {mask_pafi.sum():,} 个")
print(f"被挑中参数平均 |w| = {np.abs(W[mask_pafi]).mean():.5f}，全体平均 |w| = {np.abs(W).mean():.5f}")
print()

# ---------- 4. Child-tuning_F：伯努利掩码 ----------
print("=== 4. Child-tuning_F：伯努利掩码梯度更新 ===")
n = 100_000
W0 = rng.normal(size=n)
G = rng.normal(size=n)                      # 假想梯度
pF, eta = 0.3, 0.1
M = (rng.random(n) < pF).astype(float)      # M_t ~ Bernoulli(p_F)，式 (4.7)
W1 = W0 - eta * (G * M)                     # 掩码梯度更新，式 (4.6)
changed = W1 != W0
print(f"p_F={pF}：本步实际被更新的参数比例 = {changed.mean()*100:.1f}%")
print(f"被屏蔽参数逐位不变：max|Δ| = {np.abs(W1[M == 0] - W0[M == 0]).max():.1e}")
steps, ever = 200, np.zeros(n, dtype=bool)
for _ in range(steps):
    ever |= rng.random(n) < pF
print(f"掩码每步重抽、连抽 {steps} 步后：曾被更新过的参数覆盖率 = {ever.mean()*100:.2f}%")
print()

# ---------- 5. Child-tuning_D：费舍尔信息选参 ----------
print("=== 5. Child-tuning_D：费舍尔信息选子网络 ===")
# 合成任务：20 维输入，只有前 4 维带信号（ planted ），其余为噪声维
N, dim, signal_dims = 512, 20, 4
X = rng.normal(size=(N, dim))
w_true = np.zeros(dim); w_true[:signal_dims] = [1.5, -1.2, 1.0, 0.8]
y = X @ w_true + rng.normal(0, 0.5, size=N)
sigma2 = 1.0
w = np.zeros(dim)
# 费舍尔信息（高斯对数似然）：F_i = (1/|D|) * sum_j ( d log p(y_j|x_j)/d w_i )^2 ，式 (4.8)
resid = y - X @ w                            # (N,)
grads = (resid[:, None] * X) / sigma2        # (N, dim) 每样本每参数的梯度
fisher = (grads ** 2).mean(axis=0)
pD = 0.25
topk = int(pD * dim)
C = np.argsort(-fisher)[:topk]               # 费舍尔最高的前 p_D 比例
print(f"带信号维度 0..{signal_dims-1} 的 Fisher 均值 = {fisher[:signal_dims].mean():.3f}，"
      f"噪声维度均值 = {fisher[signal_dims:].mean():.3f}")
print(f"取前 {int(pD*100)}%（{topk}/{dim}）组成子网络 C = {sorted(C.tolist())}，"
      f"命中带信号维度 {(np.isin(C, np.arange(signal_dims))).sum()}/{signal_dims} 个")

def run_masked(mask, steps=300, lr=0.05):
    ww = np.zeros(dim)
    for _ in range(steps):
        g = -(X.T @ (y - X @ ww)) / N        # MSE 梯度
        ww = ww - lr * (g * mask)            # 只更新子网络内的参数，式 (4.6)
    return ((y - X @ ww) ** 2).mean()

mask_child = np.isin(np.arange(dim), C).astype(float)
mask_full = np.ones(dim)
print(f"初始 MSE = {(y**2).mean():.3f}")
print(f"只训子网络 C（{int(mask_child.sum())} 个参数）：300 步后 MSE = {run_masked(mask_child):.3f}")
print(f"全量微调（{dim} 个参数）：        300 步后 MSE = {run_masked(mask_full):.3f}")
