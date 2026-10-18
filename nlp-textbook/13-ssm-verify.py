"""非Transformer架构验证代码 (13): SSM离散化/递归与卷积等价 / RWKV衰减加权 / Mamba选择性步长 / TTT测试时一步更新
自写示例, numpy + 标准库, 固定随机种子可复现. 无教材代码.
"""
import numpy as np

rng = np.random.default_rng(13)

print("=" * 72)
print("1) SSM 离散化: 连续状态方程 -> 离散递归 (双线性/Tustin 近似)")
print("=" * 72)
# 标量 SSM 玩具: x'(t) = A x(t) + B u(t), y = C x ; A<0 保证稳定(记忆会衰减)
A, B, C = -0.5, 1.0, 1.0
Delta = 0.5  # 步长
A_bar = (1 + Delta * A / 2) / (1 - Delta * A / 2)
B_bar = Delta * B / (1 - Delta * A / 2)
C_bar = C
print(f"A={A}, Delta={Delta} -> A_bar={A_bar:.4f}, B_bar={B_bar:.4f}")
print("A_bar 在 (0,1) 之间: 每走一步, 旧记忆乘上它衰减一次 —— 这就是 SSM 的'记性旋钮'.")

print()
print("=" * 72)
print("2) 同一个 SSM 的两副面孔: 递归算 vs 卷积核算, 结果必须一致")
print("=" * 72)
u = rng.normal(size=12)
# 面孔一: 递归 (推理时用, 每步 O(1), 只需上一个状态)
x = 0.0
y_rec = []
for uk in u:
    x = A_bar * x + B_bar * uk
    y_rec.append(C_bar * x)
y_rec = np.array(y_rec)
# 面孔二: 卷积核 K_k = C * A_bar^k * B_bar, y = K * u (训练时用, 可并行)
K = np.array([C_bar * (A_bar ** k) * B_bar for k in range(len(u))])
y_conv = np.convolve(u, K)[: len(u)]
print("卷积核 K (越往后权重越小 = 远处记忆越淡):")
print(np.round(K, 3))
print(f"递归 vs 卷积 最大误差 = {np.abs(y_rec - y_conv).max():.2e}  (应 ~0: 同一模型, 两种算法)")
print("训练走卷积 -> 能并行; 推理走递归 -> 每步只算一次. 这是 SSM 兼得两头便宜的根.")

print()
print("=" * 72)
print("3) 复杂度账: 注意力按平方涨, SSM/递归按线性涨")
print("=" * 72)
for n in (128, 1024, 8192, 65536):
    print(f"序列 {n:6d}: 注意力两两打分 ~{n*n:>14,} 次 | SSM 递归 ~{n:>8,} 步 (每步常数工作)")
print("序列翻 512 倍, 注意力账翻 262144 倍, SSM 账只翻 512 倍.")

print()
print("=" * 72)
print("4) RWKV 的 WKV: 带指数衰减的加权平均 (旧信息按 e^{-w*距离} 变淡)")
print("=" * 72)
w = 0.35  # 每通道的衰减率 (玩具标量版)
vals = np.array([10.0, 0.0, 0.0, 0.0, 2.0])  # 第1个 token 是个大信号
keys = np.zeros(5)  # 简化: key 全 0, 只看衰减本身
t = 4  # 站在第 5 个位置回望
weights = np.exp(-(t - np.arange(t + 1)) * w + keys)
wkv = (weights * vals).sum() / weights.sum()
print(f"衰减权重 (从旧到新): {np.round(weights / weights.sum(), 3)}")
print(f"WKV 输出 = {wkv:.3f}: 4 步前的大信号 10 还剩可见影响, 但已被新信息稀释")
print("RWKV 训练时像 Transformer 一样并行算这组权重, 推理时把它折回递归、只维护两个累加量.")

print()
print("=" * 72)
print("5) Mamba 的选择性: 步长 Delta 由输入决定 —— 重要输入大步写入, 噪声小步略过")
print("=" * 72)
def softplus(z):
    return np.log1p(np.exp(-np.abs(z))) + np.maximum(z, 0)
# 玩具: 输入幅度大 -> 线性层给出大 Delta 原始值 -> softplus 后步长大
raw = np.array([-2.0, -0.5, 0.5, 2.5])  # Linear(x) 的玩具输出: 噪声->大信号
deltas = softplus(raw)
print(f"输入强度 raw={raw} -> Delta={np.round(deltas, 3)}")
print(f"大信号的步长是噪声的 {deltas[-1]/deltas[0]:.1f} 倍: 同一个状态, 该记的使劲记, 该忘的轻轻放.")
print("经典 SSM 的 A/B/C/Delta 对所有输入一视同仁; Mamba 让 B/C/Delta 随输入变, 这是它追上注意力的关键一手.")

print()
print("=" * 72)
print("6) TTT: 测试时训练 —— 用当前输入做一步梯度更新, 损失当场下降")
print("=" * 72)
# 玩具自监督任务: 内层小模型 f(z; W)=W*z, 目标是把 K 视图映到 V 视图: loss=||W*(thetaK*x)-thetaV*x||^2
thetaK, thetaV = 0.8, 1.5
W = 0.0  # 内层模型初始权重 ('隐状态'本身就是一个模型)
eta = 0.1
xs = [1.0, 2.0, -1.0, 0.5, 1.5]
for step, xt in enumerate(xs):
    pred = W * (thetaK * xt)
    target = thetaV * xt
    loss = (pred - target) ** 2
    grad = 2 * (pred - target) * (thetaK * xt)
    W = W - eta * grad
    new_loss = (W * (thetaK * xt) - target) ** 2
    print(f"步 {step+1}: x={xt:+.1f} 更新前loss={loss:.3f} -> 更新后loss={new_loss:.3f}  W={W:.3f} (真值 W*={thetaV/thetaK:.3f})")
print("每读一个新 token 就学一步: 隐状态不再是一个向量, 而是一个一直在被现学现改的小模型.")
