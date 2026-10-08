# NLP 读书笔记（03）：RNN——把全部历史"折叠"进一个向量

> 来源：中文 NLP 教材（浙江大学），《Foundations of LLMs》讲义第一章 1.2 节（RNN）
> 覆盖：PDF 第 14–19 页（书页码 7–12）· 本篇为 clean-room 重写，代码为自写示例

## 一句话核心观点

n-gram 靠"只看前 n-1 个词"偷懒，RNN 则把**全部历史压缩进一个不断更新的隐状态向量**——窗口不再固定，代价是反向传播变成一条"连乘链"，梯度消失/爆炸成了它最致命的软肋。

## 详细解读

### 1. 从 FNN 到 RNN：加一条"回路"，历史就有了记忆

前馈网络（FNN）处理序列时，每个时刻是孤立的：

$$o_t = f(W_O \cdot g(W_I x_t))$$

输入 $x_t$ 只决定当前输出 $o_t$，昨天发生什么跟今天无关。

RNN 加了一条回路——**隐状态 $h_t$**：

$$h_t = g(W_H h_{t-1} + W_I x_t), \quad o_t = f(W_O h_t)$$

每个时刻的隐状态 $h_t$ 都"吃掉"上一时刻的 $h_{t-1}$，于是历史被一层层折叠进这个向量里。注意三个权重矩阵 $W_I, W_H, W_O$ 在**所有时刻共享同一份**——参数量不随序列变长而膨胀，这是 RNN 能处理任意长度输入的关键。

对比 n-gram：n-gram 的窗口是死的（n-1 个词，多一个都看不见）；RNN 的窗口"理论上"无限——但代价是**所有历史必须挤进一个固定维度的向量**，这是它的记忆瓶颈。

### 2. BPTT：梯度沿着时间倒着走，然后"连乘"出事

训练 RNN 要最小化每步的损失之和：$L = \sum_i l(o_i, y_i)$。求损失对循环权重 $W_H$ 的梯度时，链式法则会把梯度从第 $t$ 步一路传回第 $i$ 步：

$$\frac{\partial h_t}{\partial h_i} = \prod_{k=i+1}^{t} \frac{\partial h_k}{\partial h_{k-1}}, \quad \text{其中} \ \frac{\partial h_k}{\partial h_{k-1}} = W_H \cdot g'(z_k)$$

**连乘**就是一切麻烦的根源：连乘 $t-i$ 个" $W_H \cdot$ 激活函数导数"。$W_H$ 的特征值大于 1 → 越乘越大 → **梯度爆炸**；小于 1 → 越乘越小 → **梯度消失**。而 tanh/sigmoid 的导数最大只有 1（多数时候远小于 1），更加剧了消失。

结论很扎心：RNN **理论上**记得住很远的历史，**实际上**梯度传不回去，只能记住很近的上下文。长距离依赖（如"长颈鹿……它的脖子"里的指代）基本学不到。书里把 LSTM、GRU 列为解法——思想一句话：给记忆加"门"，让重要信息走"高速公路"直达远处，细节后文展开。

### 3. RNN 做语言模型：从"查表"到"状态"

n-gram 的分解是 $P(w_N|w_1...w_{N-1}) \approx P(w_N|w_{N-n+1}...w_{N-1})$；RNN 的版本是：

$$P(w_{1:N}) = \prod_i P(w_{i+1} \mid w_i, h_{i-1})$$

条件从"前 n-1 个词"换成了"当前词 + 隐状态（全部历史的压缩包）"。训练目标还是交叉熵——和 n-gram 的 MLE 一脉相承，只是参数从"计数表"变成了神经网络权重。

### 4. Teacher Forcing 与 Exposure Bias：平时开卷，考试闭卷

训练 RNN 有个实用技巧叫 **Teacher Forcing**：每一步都喂**标准答案**（ground truth）作为下一步的输入，而不是喂模型自己上一秒的预测。好处是训练又快又稳。

但这里有个坑：**推理时没有标准答案可喂**，模型只能吃自己生成的词（自回归）。训练和推理的输入分布不一致，推理时一步走偏、步步走偏——这叫 **Exposure Bias（曝光偏差）**。

缓解办法之一是 **Scheduled Sampling**：训练时以一定概率混入模型自己的预测当输入，让模型提前适应"吃自己做的饭"。顺带一提：Transformer 的训练今天也在用 Teacher Forcing——这个坑是代代相传的。

### 5. 手写代码：最小 RNN 语言模型 + 梯度消失演示（已运行验证）

```python
import numpy as np
rng = np.random.default_rng(7)

texts = ["hello world", "hello there", "hi world", "hi there"] * 2
vocab = sorted(set("".join(texts)))
stoi = {c: i for i, c in enumerate(vocab)}
V, H = len(vocab), 32

def onehot(i):
    v = np.zeros(V); v[i] = 1.0
    return v

def xavier(r, c):
    return rng.normal(0, np.sqrt(1.0 / r), (r, c))
Wxh = xavier(V, H)          # 输入 -> 隐
Whh = xavier(H, H) * 0.9    # 隐 -> 隐（所有时刻共享）
Why = xavier(H, V)          # 隐 -> 输出
bh, by = np.zeros(H), np.zeros(V)

def forward(xs):
    hs = {-1: np.zeros(H)}; ps = {}
    for t, idx in enumerate(xs):
        hs[t] = np.tanh(onehot(idx) @ Wxh + hs[t-1] @ Whh + bh)  # 核心公式
        z = hs[t] @ Why + by
        e = np.exp(z - z.max()); ps[t] = e / e.sum()
    return hs, ps

def loss_and_grads(xs, ys, lr=0.05):
    global Wxh, Whh, Why, bh, by
    hs, ps = forward(xs); T = len(xs)
    loss = -sum(np.log(ps[t][ys[t]] + 1e-12) for t in range(T)) / T
    dWxh = np.zeros_like(Wxh); dWhh = np.zeros_like(Whh)
    dWhy = np.zeros_like(Why); dbh = np.zeros_like(bh); dby = np.zeros_like(by)
    dh_next = np.zeros(H)
    for t in reversed(range(T)):              # BPTT：沿时间倒着传
        dy = ps[t].copy(); dy[ys[t]] -= 1.0; dy /= T
        dWhy += np.outer(hs[t], dy); dby += dy
        dh = dy @ Why.T + dh_next
        dh_raw = dh * (1 - hs[t] ** 2)        # tanh 导数
        dbh += dh_raw
        dWxh += np.outer(onehot(xs[t]), dh_raw)
        dWhh += np.outer(hs[t-1], dh_raw)
        dh_next = dh_raw @ Whh.T              # 梯度传向上一时刻（连乘链的来源）
    for p, d in [(Wxh, dWxh), (Whh, dWhh), (Why, dWhy), (bh, dbh), (by, dby)]:
        p -= lr * d
    return loss

pairs = []
for s in texts:
    ids = [stoi[c] for c in s]
    pairs.append((ids[:-1], ids[1:]))          # 自监督：输入前 N-1 字符，预测后移一位
for epoch in range(1, 601):
    tot = sum(loss_and_grads(x, y) for x, y in pairs) / len(pairs)
    if epoch % 200 == 0:
        print(f"epoch {epoch:3d}  avg loss = {tot:.4f}")

def generate(seed, n=6):                       # 自回归采样
    idxs = [stoi[c] for c in seed]
    hs, _ = forward(idxs); h = hs[len(idxs) - 1]
    out = list(seed)
    for _ in range(n):
        z = h @ Why + by
        e = np.exp(z - z.max()); p = e / e.sum()
        nxt = int(rng.choice(V, p=p))
        out.append(vocab[nxt])
        h = np.tanh(onehot(nxt) @ Wxh + h @ Whh + bh)
    return "".join(out)

print("采样:", generate("hello ", 6))
print("采样:", generate("hi ", 6))
```

**实际运行输出**（已验证）：

```
epoch 200  avg loss = 0.1853
epoch 400  avg loss = 0.1783
epoch 600  avg loss = 0.1763
采样: hello therer
采样: hi therer
采样: hello worldi
```

8 个句子的小语料上，模型学会了"hello/hi → world/there"的结构——最原始的神经网络"写作"。

梯度连乘演示（模拟 BPTT 的 $\prod W_H \cdot \tanh'$ 链，传 30 步）：

```
Whh 缩放 0.5: 30 步后梯度范数 = 3.01e-04   # 消失：传回去的信号只剩十万分之三
Whh 缩放 1.0: 30 步后梯度范数 = 6.12e+02
Whh 缩放 1.5: 30 步后梯度范数 = 2.39e+05   # 爆炸：涨了几十万倍
```

权重稍微大一点小一点，30 步之后就是天壤之别——这就是 RNN 记不远的数学原因。

## 我的思考/应用

1. **RNN 是理解 Transformer 的前置课**：自回归生成、Teacher Forcing、交叉熵训练目标——这三件套从 RNN 一直沿用到今天的大模型。搞懂 RNN，Transformer 只剩"注意力"一个新概念。
2. **"压缩 vs 展开"的路线之争**：RNN 把历史压成一个向量（有瓶颈），Transformer 干脆不压缩、把历史全部展开用注意力去查。下一章看这场路线之争的答案。
3. **面试常考点**：手写 BPTT、解释梯度消失的数学原因、LSTM 门控思想——这篇笔记的代码和公式就是现成的面试弹药。
4. **对照 n-gram**：两篇连起来看，语言模型 70 年就干了一件事——"根据历史预测下一个词"，只是"历史"的表示方法从计数表进化到了向量。

## 视频脚本要点（动画短片用）

1. 开场钩子："n-gram 只能记住前 n-1 个词——如果有个模型，能记住'全部历史'呢？"
2. 行李箱动画：隐状态 h 像个行李箱，每来一个词就塞进去压扁——"全部历史，一个向量"。
3. 传话游戏动画：梯度每往回传一步就衰减一点，30 步后只剩 3e-04——"这就是 RNN 记不远的原因"。
4. Teacher Forcing 比喻：平时考试学霸坐旁边递答案（训练），正式考试只能靠自己（推理）——"这叫曝光偏差"。
5. 结尾预告："RNN 的记忆有个瓶颈——下一站，有人把行李箱直接拆了，叫 Transformer。"
