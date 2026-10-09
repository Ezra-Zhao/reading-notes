# NLP 读书笔记（04）：Transformer——把"行李箱"拆了，让每个词直接看历史

> 来源：中文 NLP 教材（浙江大学），《Foundations of LLMs》讲义第一章 1.3 节（Transformer）
> 覆盖：PDF 第 20–24 页（书页码 13–17）· 本篇为 clean-room 重写，代码为自写示例

## 一句话核心观点

RNN 把全部历史**压缩**进一个向量（有瓶颈），Transformer 干脆**不压缩**——每个位置用注意力直接读取全部历史，任意两个词之间的路径从 O(n) 降到 O(1)；代价是 O(n²) 的计算量，以及四个精巧组件的配合。

## 详细解读

### 1. 路线之争的答案：从"压缩历史"到"直查历史"

上一篇的结论很扎心：RNN 理论上记得住全部历史，实际上梯度传不回去，只能记住很近的上下文。Transformer 的回答非常决绝：**既然压缩会丢东西，那就别压缩了**——把历史全部摊开展示，每个词想看多远就看多远。

代价也很直接：n 个词两两之间都要算一次相似度，计算量是 O(n²)。RNN 是 O(n) 时间但必须串行（第 t 步等第 t-1 步），Transformer 是 O(n²) 计算但**完全并行**——训练时所有位置同时算。这笔 trade-off 在 GPU 时代是划算的：算力便宜，串行等待才贵。

### 2. 注意力层：每个词给自己配三个"身份"

Transformer 的输入是一串词向量 ${x_1, x_2, \dots, x_t}$。注意力层给每个词发三个"身份牌"——用三个学出来的矩阵投影得到：

$$q_i = W_q x_i, \quad k_i = W_k x_i, \quad v_i = W_v x_i$$

- **query（q）**："我想找什么"——当前词发出的提问；
- **key（k）**："我有什么"——每个历史词贴出的标签；
- **value（v）**："我的内容"——真正要搬运的信息。

第 $t$ 个词的输出是所有历史词 value 的加权平均，权重看 query 和 key 有多"对得上"：

$$\text{Attention}(x_t) = \sum_{i=1}^{t} \alpha_{t,i} v_i, \quad \alpha_{t,i} = \text{softmax}(\text{sim}(q_t, k_i))$$

直觉：词 $t$ 拿着自己的问题（q），去翻所有历史词的标签（k），谁对得上就多抄谁的内容（v）。"它"这个词的 q 和"小猫"的 k 最对得上，指代关系**一步直达**——RNN 要把这个关系从 30 步外"传话"回来，传到就只剩渣了。

### 3. 前馈层：模型的"知识仓库"

注意力只负责"搬运"信息，真正的"加工"在全连接前馈层：

$$\text{FFN}(v) = \max(0, W_1 v + b_1) W_2 + b_2$$

可以把它理解成 **key-value 记忆库**：第一层矩阵 $W_1$ 像一排"探测器"，检测输入里有没有某种模式（比如"这是主语""这是个地名"）；ReLU 把没触发的关掉；第二层 $W_2$ 把触发的模式翻译成输出。大模型的大部分参数和"知识"其实存在这里——注意力是"查资料"，前馈层是"做判断"。

### 4. 层归一化 + 残差连接：为什么能堆上百层

光有上面两个还不够——堆 100 层，信号要么爆炸要么消失。两个"稳定器"解决：

- **层归一化（LayerNorm）**：把每个位置的向量拉回均值 0、方差 1（再学两个缩放参数调回去）。$LN(v_i) = \alpha \frac{v_i - \mu}{\delta} + \beta$。作用：不管前面几层把数值搞成什么样，到这里都"复位"一下，训练不跑飞。
- **残差连接**：每层的输出 = 输入 + 该层算出的增量（$x + \text{Layer}(x)$）。最坏情况这一层学个 0，信号原样通过——**深层网络退化不成浅层网络的性能下限被保住了**，梯度也有一条"直通车"往回走。

书里还提了一个细节：**Post-LN vs Pre-LN**。把归一化放在残差"加完之后"（Post-LN，原始 Transformer）还是"加之前"（Pre-LN）？Post-LN 堆太深会出现"表示坍缩"（representation collapse）——各层输出越来越像，深度白堆了。Pre-LN 更稳定，是今天大模型堆上百层的标配。

### 5. 三种架构：Encoder-Only、Encoder-Decoder、Decoder-Only

同一个 Transformer 积木，三种搭法，对应三类任务：

| 架构 | 结构 | 代表 | 擅长 |
|---|---|---|---|
| Encoder-Only | 只要编码器 | BERT | 理解：分类、问答、 embedding |
| Encoder-Decoder | 编码器 + 解码器 | T5 | 转换：翻译、摘要（输入输出都整段） |
| Decoder-Only | 只要解码器 | GPT-3 | 生成：续写、对话（今天大模型的主流） |

Decoder 里有个特殊设计叫**交叉注意力**：解码器每层的 query 来自自己前一层的输出，key/value 来自编码器最后一层——相当于解码时"一边写、一边回头查原文"。

### 6. 训练：目标和 RNN 是同一套

以 Decoder-Only 为例，训练目标和 RNN 时代一脉相承——还是"根据历史预测下一个词"：

$$P(w_{1:N}) = \prod_{i=1}^{N-1} P(w_{i+1} \mid w_{1:i}), \quad \ell_{CE} = -\log o_i[w_{i+1}]$$

每个位置输出词表上的概率分布，对真实下一个词取交叉熵；全部位置平均就是总损失。Teacher Forcing 也原样继承：训练时喂标准答案，推理时自回归——曝光偏差这个坑，Transformer 一个没躲掉。

### 7. 手写代码：最小自注意力 + O(1) 路径演示（已运行验证）

```python
import numpy as np
rng = np.random.default_rng(11)

def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)

def self_attention(X, Wq, Wk, Wv, causal=False):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    scores = Q @ K.T / np.sqrt(Q.shape[1])
    if causal:  # 未来位置填 -inf：训练时不许偷看
        scores = np.where(np.triu(np.ones_like(scores), k=1).astype(bool),
                          -1e9, scores)
    A = softmax(scores)
    return A @ V, A

# 4 个词的人工 embedding：词4("它")语义靠近词1("小猫")
X = np.array([
    [1.0, 0.1, 0.0],   # 词1 小猫
    [0.0, 1.0, 0.1],   # 词2 追
    [0.1, 0.0, 1.0],   # 词3 毛线球
    [0.9, 0.2, 0.1],   # 词4 它（指代词1）
])
d = X.shape[1]
Wq = Wk = Wv = np.eye(d)   # 单位矩阵：相似度退化为点积，演示更直观

out, A = self_attention(X, Wq, Wk, Wv)
print(np.round(A, 3)); print("每行和:", np.round(A.sum(axis=1), 6))

# O(1) 路径：词1清零，词4输出立刻变——直连，无连乘衰减
X2 = X.copy(); X2[0] = 0.0
out2, _ = self_attention(X2, Wq, Wk, Wv)
print("词1清零 -> 词4输出变化 L1 =", round(float(np.abs(out[3]-out2[3]).sum()), 4))

# mini block：注意力 + 前馈，各带残差与层归一化
def layer_norm(v, eps=1e-6):
    return (v - v.mean(-1, keepdims=True)) / (v.std(-1, keepdims=True) + eps)

W1, b1 = rng.normal(0, 0.5, (d, 8)), np.zeros(8)
W2, b2 = rng.normal(0, 0.5, (8, d)), np.zeros(d)
h, _ = self_attention(X, Wq, Wk, Wv, causal=True)
h = layer_norm(X + h)
y = layer_norm(h + np.maximum(0, h @ W1 + b1) @ W2 + b2)
print("block 输出形状:", y.shape, "| NaN:", bool(np.isnan(y).any()))
```

**实际运行输出**（已验证）：

```
[[0.319 0.189 0.189 0.303]
 [0.21  0.356 0.21  0.224]
 [0.211 0.211 0.356 0.222]
 [0.304 0.202 0.2   0.294]]
每行和: [1. 1. 1. 1.]
词1清零 -> 词4输出变化 L1 = 0.3062
block 输出形状: (4, 3) | NaN: False
```

"它"（第 4 行）对"小猫"（第 1 列）的注意力是 0.304，明显高于对"追"（0.202）——**指代关系一步捕获**，这正是 RNN 用 30 步传话传丢的东西。词 1 清零后词 4 的输出变化 0.3062：影响是直达的，没有连乘链衰减。

## 我的思考/应用

1. **O(n²) 是 Transformer 的"原罪"也是护城河**：上下文越长越贵——这就是为什么长上下文是稀缺能力、按 token 收费。今天所有"长文本优化"（稀疏注意力、KV cache、FlashAttention）都是在给这个 O(n²) 还债。
2. **面试弹药**：手写 self-attention（QKV + softmax + 掩码）是算法岗必考题，这篇的代码就是 30 行版本；再进一步要能讲清 Post-LN vs Pre-LN 和表示坍缩。
3. **对照 RNN 的进化线**：n-gram（查表）→ RNN（压缩成向量）→ Transformer（不压缩、直接查）。三代只干一件事——"根据历史预测下一个词"，变的是"历史"的表示方式。这个框架能串起整个语言模型史。
4. **FFN 存知识、注意力做推理**：调大模型时"知识问答翻车"多半怪 FFN 存的知识，"指代/长距离理解翻车"多半怪注意力——定位问题先分清这两层。

## 视频脚本要点（动画短片用）

1. 开场钩子："RNN 把全部历史塞进一个行李箱——有人觉得箱子太小，直接把箱子拆了。"
2. 相亲角动画：每个词发三张牌——"我想找什么"(query)、"我有什么"(key)、"我的干货"(value)，对上眼就加权平均。
3. 传话 vs 直连对比：RNN 30 步传话剩 3e-04，Transformer "它"看"小猫"一步 0.304——"距离不再是问题，代价是两两都要算一遍。"
4. 积木动画：注意力（查资料）+ 前馈（做判断）+ 归一化（复位）+ 残差（直通车），四块积木叠 100 层不塌。
5. 结尾预告："Transformer 只是'会看'——下一个词怎么'选出来'，下回讲解放码器的骰子：贪心、束搜索与温度。"
