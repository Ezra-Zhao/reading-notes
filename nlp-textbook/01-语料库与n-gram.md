# NLP 读书笔记（01）：语料库与 n-gram——语言模型的"数数"时代

> 来源：中文 NLP 教材（浙江大学），《Foundations of LLMs》讲义第一章 1.1 节
> 覆盖：PDF 第 8–13 页（书页码 1–6）· 本篇为 clean-room 重写，代码为自写示例

## 一句话核心观点

语言模型本质上只回答一个问题——"下一个词最可能是什么"；而 n-gram 用最朴素的办法回答它：去历史文本里数一数，这个搭配出现过多少次。

## 详细解读

### 1. 语料库：语言模型的"粮食"

语料库（Corpus）就是大规模收集来的真实文本集合。模型从哪里学"人话"？就从这里。语料库越大、越干净，模型学到的语言规律就越靠谱。

书里举了一个迷你语料库帮助理解——5 句关于长颈鹿的话（大意：脖子长是长颈鹿最醒目的特征；长脖子让它看起来优雅、吃得方便；能看到动物园隐蔽角落；和人类一样只有七节颈椎；语言模型也像长颈鹿的脖子一样在不断进化）。麻雀虽小，五脏俱全：**语料库就是"被切成一句一句的真实语言样本"**。

### 2. Token：先把句子切成"词"

在数数之前，要先把文本切成基本单位 Token。对中文可以按字切，对英文可以按词切。切完之后，一句话就变成一个序列：w1, w2, …, wN。

### 3. n-gram：连续 n 个词就是一个"搭配"

- n=1 叫 unigram（单个词）
- n=2 叫 bigram（两个连续词，如"我 爱"）
- n=3 叫 trigram（三个连续词，如"我 爱 你"）

n 越大，记住的"搭配习惯"越长，但需要的语料也越多。

### 4. 核心公式：概率 = 数数

bigram 的条件概率这样算：

P(wi | wi-1) = C(wi-1, wi) / C(wi-1)

翻译成大白话：**"在 wi-1 出现过的所有地方，有多少次它后面紧跟着 wi"**。分子是"（wi-1, wi）这个二元组出现了几次"，分母是"wi-1 总共出现了几次"。推广到 n-gram：

P(wi | wi-n+1 … wi-1) = C(wi-n+1 … wi) / C(wi-n+1 … wi-1)

整句话的概率，就是把每个位置的条件概率连乘起来（链式法则）。

### 5. 手写代码：从零实现一个 bigram 模型

```python
from collections import Counter

# 自造的迷你语料库（注意：示例为自写，非书中原文）
corpus = [
    "小猫 爱 吃 鱼",
    "小猫 爱 睡觉",
    "小狗 爱 吃 骨头",
    "小狗 爱 跑步",
    "小猫 不 爱 洗澡",
]

def train_bigram(corpus):
    bigram_counts = Counter()   # C(wi-1, wi)
    unigram_counts = Counter()  # C(wi-1)
    for sent in corpus:
        words = sent.split()
        for w in words:
            unigram_counts[w] += 1
        for a, b in zip(words, words[1:]):
            bigram_counts[(a, b)] += 1
    return bigram_counts, unigram_counts

def bigram_prob(prev, word, bigram_counts, unigram_counts):
    # P(word | prev) = C(prev, word) / C(prev)
    if unigram_counts[prev] == 0:
        return 0.0
    return bigram_counts[(prev, word)] / unigram_counts[prev]

bc, uc = train_bigram(corpus)
print(bigram_prob("爱", "吃", bc, uc))    # 爱出现5次，后面跟"吃"2次 -> 0.4
print(bigram_prob("小猫", "爱", bc, uc))   # 小猫出现3次，后面跟"爱"2次 -> 0.667
print(bigram_prob("小猫", "不", bc, uc))   # 小猫出现3次，后面跟"不"1次 -> 0.333

def sentence_prob(sent, bc, uc):
    words = sent.split()
    p = 1.0
    for a, b in zip(words, words[1:]):
        p *= bigram_prob(a, b, bc, uc)
    return p

print(sentence_prob("小猫 爱 吃 鱼", bc, uc))  # (2/3) * 0.4 * 0.5 ≈ 0.133
```

跑一下就明白：**n-gram 模型没有任何"理解"，它只是一张巨大的搭配频率表**。但就是这张表，让机器第一次能量化"这句话像不像人话"。

## 我的思考/应用

1. **n-gram 是今天大模型的"曾祖父"**。GPT 们做的事和它一模一样——预测下一个词，只是把"数数"换成了神经网络。理解 n-gram，就理解了语言模型的任务定义本身。
2. **中文分词天然适配**：中文没有空格，"切词"这一步本身就是学问。按字切（unigram over 字）是最省事的起点，很多中文 n-gram 实验都这么干。
3. **输入法联想就是 bigram**：你手机打字时候选词的排序，背后很可能就是一张 n-gram 频率表。下次看到"联想"可以想想它在查哪张表。

## 视频脚本要点（动画短片用）

1. 开场钩子："机器怎么学会说人话？最早的答案笨到可爱——数数。"
2. 动画演示语料库：5 句话变成 5 张卡片，Token 切分像切面包一样逐词落下。
3. 可视化 bigram 查表：输入"小猫"，高亮所有"小猫→？"的搭配，柱状图显示"爱 3 次、不 1 次"，概率条动态算出 0.75。
4. 一句话点题："没有理解，只有统计——但这就是语言模型的起点。"
5. 结尾悬念："可如果一句话从没出现过，概率就是 0 吗？下集讲 n-gram 的致命软肋：平滑。"
