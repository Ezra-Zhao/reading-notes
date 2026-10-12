"""NLP 笔记 07 自写验证脚本：缩放定律（Scaling Laws）
公式取自教材 2.1.1 节（Kaplan-McCandlish 2020 与 Chinchilla 2022 的公开常数），
代码为本笔记独立手写，绘制曲线 + 数值验证。
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------- 1. Kaplan-McCandlish (OpenAI, 2020) ----------------
# L(N) = (Nc/N)^aN, L(D) = (Dc/D)^aD
aN, Nc = -0.076, 8.8e13
aD, Dc = -0.095, 5.4e13

def L_kaplan_N(N):
    return (Nc / N) ** aN

def L_kaplan_D(D):
    return (Dc / D) ** aD

# Kaplan 组合形式（论文 eq.2.13）：L(N,D) = ((Nc/N)^(aN/aD) + Dc/D)^aD
def L_kaplan_joint(N, D):
    return ((Nc / N) ** (aN / aD) + Dc / D) ** aD

# ---------------- 2. Chinchilla (DeepMind, 2022) ----------------
# L(N,D) = E + A/N^a + B/D^b
E, A, B = 1.69, 406.4, 410.7
ca, cb = 0.34, 0.28

def L_chin(N, D):
    return E + A / N ** ca + B / D ** cb

# Chinchilla 解析最优分配（在 6ND=C 约束下对 L 求导，解得）：
# N = G * (C/6)^a, D = C/(6N), 其中 a=cb/(ca+cb), G=(ca*A/(cb*B))^(1/(ca+cb))
a_exp = cb / (ca + cb)
G = (ca * A / (cb * B)) ** (1 / (ca + cb))

def chin_optimal(C):
    N = G * (C / 6) ** a_exp
    D = C / (6 * N)
    return N, D

def kaplan_optimal(C):
    # 在 6ND=C 约束下数值最小化 Kaplan 组合 loss
    logN = np.linspace(np.log10(1e6), np.log10(C / 6 / 1e6), 2000)
    N = 10 ** logN
    D = C / (6 * N)
    L = L_kaplan_joint(N, D)
    i = int(np.argmin(L))
    return N[i], D[i], L[i]

# ---------------- 3. 画 Kaplan loss 随 N / D 下降曲线 ----------------
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

N_rng = np.logspace(6, 13, 200)      # 参数量 1e6 -> 1e13
axes[0].loglog(N_rng, L_kaplan_N(N_rng))
axes[0].set_xlabel("model params N")
axes[0].set_ylabel("loss L(N) = (Nc/N)^aN")
axes[0].set_title("Kaplan: loss vs params (log-log)")
axes[0].grid(True, which="both", alpha=0.3)

D_rng = np.logspace(9, 15, 200)      # 数据 1e9 -> 1e15 tokens
axes[1].loglog(D_rng, L_kaplan_D(D_rng))
axes[1].set_xlabel("tokens D")
axes[1].set_ylabel("loss L(D) = (Dc/D)^aD")
axes[1].set_title("Kaplan: loss vs data (log-log)")
axes[1].grid(True, which="both", alpha=0.3)

plt.tight_layout()
plt.savefig("/home/hatch/workspace/github/reading-notes/nlp-textbook/scaling-curves.png", dpi=110)
print("plot saved: scaling-curves.png")

# Kaplan 的 0.73/0.27 来自原论文"固定算力下最优模型尺寸"的实证拟合
# （不是直接对联合 loss 求导），此处用历史锚点做分配对比：
#   - Kaplan 派：以 GPT-3 (175B 参数/300B tokens, C=3.15e23) 为锚（Kaplan 时代的代表作）
#   - Chinchilla 派：以 Chinchilla (70B 参数/1.4T tokens, C=5.88e23) 为锚
# 指数来自两篇论文的公开结论（教材 2.1.1 节），对比的是"分配斜率"的差异。
KAP_ANCHOR = dict(N=175e9, D=300e9)   # GPT-3
KAP_EXP_N, KAP_EXP_D = 0.73, 0.27
CHIN_ANCHOR = dict(N=70e9, D=1.4e12)  # Chinchilla
CHIN_EXP_N, CHIN_EXP_D = 0.46, 0.54

def kaplan_optimal(C):
    Ck = 6 * KAP_ANCHOR["N"] * KAP_ANCHOR["D"]
    N = KAP_ANCHOR["N"] * (C / Ck) ** KAP_EXP_N
    D = KAP_ANCHOR["D"] * (C / Ck) ** KAP_EXP_D
    return N, D

def chin_optimal_hist(C):
    Cc = 6 * CHIN_ANCHOR["N"] * CHIN_ANCHOR["D"]
    N = CHIN_ANCHOR["N"] * (C / Cc) ** CHIN_EXP_N
    D = CHIN_ANCHOR["D"] * (C / Cc) ** CHIN_EXP_D
    return N, D

print("\n== 固定算力 C 下的最优分配对比（6ND=C；指数为论文公开结论） ==")
print(f"{'C (FLOP)':>11} | {'Kaplan 派 N':>10} {'Kaplan 派 D':>10} | "
      f"{'Chinchilla 派 N':>13} {'Chinchilla 派 D':>10}")
for C in [1e21, 1e22, 1e23, 3.15e23, 5.88e23]:
    Nk, Dk = kaplan_optimal(C)
    Nh, Dh = chin_optimal_hist(C)
    print(f"{C:>11.2e} | {Nk/1e9:>7.1f}B  {Dk/1e12:>7.2f}T | "
          f"{Nh/1e9:>10.1f}B  {Dh/1e12:>7.2f}T")
    assert abs(6 * Nk * Dk / C - 1) < 0.02 and abs(6 * Nh * Dh / C - 1) < 0.02

# ---------------- 5. Chinchilla vs GPT-3：同等算力、以小胜大 ----------------
gpt3 = dict(N=175e9, D=300e9)        # GPT-3：175B 参数，300B tokens
chin = dict(N=70e9, D=1.4e12)        # Chinchilla：70B 参数，1.4T tokens

def stats(tag, N, D):
    C = 6 * N * D
    return dict(tag=tag, C=C, loss=L_chin(N, D))

s_gpt3 = stats("GPT-3 (175B/300B)", **gpt3)
s_chin = stats("Chinchilla (70B/1.4T)", **chin)
print("\n== Chinchilla 公式下的两模型对比 ==")
for s in (s_gpt3, s_chin):
    print(f"{s['tag']}: C = {s['C']:.3e} FLOP, 预测 loss = {s['loss']:.4f}")
print(f"算力比 (Chinchilla/GPT-3) = {s_chin['C']/s_gpt3['C']:.2f}")
print(f"loss 差 (Chinchilla - GPT-3) = {s_chin['loss']-s_gpt3['loss']:.4f}  "
      f"(负值=Chinchilla 更优)")

# 按 Chinchilla 派的公式反推：如果把 GPT-3 的算力按 Chinchilla 最优重配
# （chin_optimal 是从 6ND=C 约束下对公式求导得到的解析解）
N_star, D_star = chin_optimal(s_gpt3["C"])
L_star = L_chin(N_star, D_star)
Nk_gpt3, Dk_gpt3 = kaplan_optimal(s_gpt3["C"])
print(f"\n== 若把 GPT-3 的算力 ({s_gpt3['C']:.2e} FLOP) 重新分配 ==")
print(f"  Kaplan 派思路   : N={Nk_gpt3/1e9:7.1f}B 参数, D={Dk_gpt3/1e12:5.2f}T tokens "
      f"(实际就是 GPT-3 本身)")
print(f"  Chinchilla 最优  : N={N_star/1e9:7.1f}B 参数, D={D_star/1e12:5.2f}T tokens, "
      f"预测 loss={L_star:.4f}")
print(f"  -> 同样的钱，Chinchilla 派会把参数砍到约 1/7，数据喂到约 7 倍")
