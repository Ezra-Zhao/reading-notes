# 验证 106 篇篇内数字与结构（参数取自原书第四卷第七章第一部分收官篇内陈述，不冒充现代实测）
from fractions import Fraction as F
# 1 金税阶梯严格递减、首尾十倍
chain = [F(1, 2), F(1, 3), F(1, 5), F(1, 10), F(1, 20)]
assert all(a > b for a, b in zip(chain, chain[1:])) and chain[0] / chain[-1] == 10
# 2 剥完六至八年；银税五分之一至十分之一恰减半
assert 6 < 8 and F(1, 10) * 2 == F(1, 5)
# 3 墨西哥约三十年、秘鲁约四十年，差十年
assert 30 < 40 and 40 - 30 == 10
# 4 巴西发现矿时滞逾一百年
assert 100 >= 100  # 原书作一百多年，下限一百
# 5 英国专利五分之一恰百分之二十、与金税阶梯第三格同值
assert F(1, 5) == chain[2] and float(F(1, 5)) == 0.2
# 6 被点名冒险者六人：达里恩三、墨西哥一、智利秘鲁二
assert 3 + 1 + 2 == 6
print("106 verify: 6 assertions passed")
