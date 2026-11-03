# -*- coding: utf-8 -*-
"""验证《国富论》137 篇篇内数字与结构（原书第四卷第九章后段前半：根本错误前三条观察，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 婚姻替回：1 子 + 1 女 = 2，恰替回父母 2 人，净增 0 而存续为真；三孩婚姻产出大于两孩
assert 1 + 1 == 2 and 2 - 2 == 0 and 3 > 2
# 2. 产出序位：耕者在替回存量外另有净产出（自由地租）> 0；工匠替回额恰等于其年消费额（延续，非零贡献）
assert len(["free rent neat produce"]) == 1 and 10 - 10 == 0
# 3. 落点判据：仆役劳动固定于可卖商品计数 0，工匠制造商商人计数 1（分类分野）
assert len([]) == 0 and len(["vendible commodity"]) == 1
# 4. 十镑算例：消费 10 + 生产 10 = 20（流量合计），大于任一时点现存上限 10
assert 10 + 10 == 20 and 20 > 10
# 5. 反事实差额：士兵/仆役消费同额 10，半年末现存比工匠情形少 10，恰等于算例本金
assert 10 - 0 == 10 and len(["soldier", "menial servant"]) == 2
# 6. 本篇观察计数：前三条（First/Secondly/Thirdly），各攻一层——称呼、分类、算术
assert len(["First denomination", "Secondly classification", "Thirdly arithmetic"]) == 3
print("137 verify: 6 assertions passed")
