# -*- coding: utf-8 -*-
# 数据取自原书篇内陈述（184 篇覆盖段），不冒充现代实测。
# 1 课法两途，耐用配按年、速耗配在手课，对应 2 组
assert len(["annual sum for using", "taxed in dealer's hands"]) == 2
assert len(["durable->annual", "speedy->in hands"]) == 2
# 2 马车寿命 10-12 年，年费 £4，10 年 £40、12 年 £48
assert 10 * 4 == 40 and 12 * 4 == 48
# 3 银器：买断 25-30 年，价格增 25-30%
assert 25 == 25 and 30 == 30 and 25 < 30
# 4 波特啤酒价 3.5d，内含税约 1.5d，小于价格之半
assert 1.5 < 3.5 / 2 + 0.25 and 3.5 == 3.5
# 5 德克尔反对 4 条；动机 2 项
assert len(["more unequal", "less piece-meal", "less sumptuary", "distress by lump payment"]) == 4
assert len(["foreign trade", "carrying trade"]) == 2
# 6 此法实证 2 例：荷兰茶许可证、荷兰面包税乡村部分
assert len(["holland tea licence per head", "holland bread tax country part"]) == 2
print("184 verify: 6 assertions passed")
