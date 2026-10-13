"""自写验证脚本：三种 Transformer 架构的注意力可见性与预测方式对比。
clean-room 示例，无教材代码。只用 numpy。"""
import numpy as np

np.set_printoptions(linewidth=120, suppress=True)

def show(name, mask):
    print(f"\n{name} (1=能看见, 0=被挡住) 行=正在处理的位置, 列=能看的来源位置")
    print(mask.astype(int))

n = 5  # 序列长度示意
# 1) Encoder-only: 双向自注意力，谁都能看全序列
enc_mask = np.ones((n, n))
show("Encoder-only 自注意力", enc_mask)
print(f"可见对数: {int(enc_mask.sum())}/{n*n} —— 每个位置平均能看 {enc_mask.sum()/n:.1f} 个位置")

# 2) Decoder-only: 因果掩码，只能看自己和左边
dec_mask = np.tril(np.ones((n, n)))
show("Decoder-only 因果自注意力", dec_mask)
print(f"可见对数: {int(dec_mask.sum())}/{n*n} —— 第 i 个位置只能看 i+1 个（含自己），未来一律挡住")

# 3) Encoder-Decoder: 编码器双向 + 解码器因果 + 交叉注意力（解码每个位置看全部输入）
m = 4  # 输入长度
cross_mask = np.ones((n, m))
show("Encoder-Decoder 交叉注意力 (行=输出位置, 列=输入位置)", cross_mask)
print(f"交叉可见对数: {int(cross_mask.sum())}/{n*m} —— 输出端每个位置都能回看全部输入")

# 注意力分数演示：同一个 QK 分数矩阵，套不同掩码后 softmax 的差别
scores = np.array([[2.0, 1.0, 0.0, -1.0, -2.0]] * n, dtype=float)
def masked_softmax(s, mask):
    s2 = np.where(mask > 0, s, -1e9)
    e = np.exp(s2 - s2.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)
print("\n同一行分数 [2,1,0,-1,-2] 套掩码后，第 3 个位置（index=2）的注意力权重:")
print(" Encoder-only :", np.round(masked_softmax(scores, enc_mask)[2], 3), "-> 左右都能分到权重")
print(" Decoder-only :", np.round(masked_softmax(scores, dec_mask)[2], 3), "-> 右边两个位置权重严格为 0，没偷看未来")

# 预测方式对比：一条长度 n 的序列，三种架构各能产生几个训练信号
# Encoder-only(MLM): 只在被遮住的位置算 loss，示意遮 15%（下面用 20 个 token 的句子算）
print(f"\n训练信号对比（以 20 个 token 的句子示意）:")
print(f" Encoder-only / MLM   : 遮住约 15% -> 约 {round(20*0.15)} 个位置算 loss（双向看上下文，猜被遮的词）")
print(f" Decoder-only / 自回归 : 每个位置预测下一个词 -> {20-1} 个位置算 loss（信号密度最高）")
print(f" Encoder-Decoder / seq2seq: 输入 20 词、输出 12 词 -> 输出端 {12} 个位置算 loss（条件是整段输入）")
print("\n结论: 可见性决定任务形态 —— 全看=理解, 只看左边=生成, 分开看=转换。")
