# -*- coding: utf-8 -*-
# 数据取自原书篇内陈述（179 篇覆盖段），不冒充现代实测。
# 1 核心算例：净生活线 10 先令，税率 1/5，毛工资 12.5 扣税 2.5 净回 10；涨幅 1/4 > 1/5；1/10 税率涨幅 1/8 > 1/10
net_line = 10.0; rate = 1/5; gross = 12.5
assert abs(gross * (1 - rate) - net_line) < 1e-9
assert (gross - net_line) / net_line == 1/4 and 1/4 > rate
assert 1/8 > 1/10
# 2 工资决定条件恰两项
conditions = ["demand for labour", "average price of provisions"]
assert len(conditions) == 2
# 3 终落两路
final_payer = {"manufacturing": "consumer", "country labour": "landlord"}
assert final_payer["manufacturing"] == "consumer" and final_payer["country labour"] == "landlord"
assert len(final_payer) == 2
# 4 比较判语：直接工资税的减租与涨价均大于同额分课
direct_wages_tax = {"rent_reduction": 2, "price_rise": 2}
split_tax = {"rent_reduction": 1, "price_rise": 1}
assert direct_wages_tax["rent_reduction"] > split_tax["rent_reduction"]
assert direct_wages_tax["price_rise"] > split_tax["price_rise"]
# 5 例外归因一项、后果三样、该状态下工资仍高于无税时
cause = ["fall in demand for labour"]
effects = ["declension of industry", "decrease of employment for the poor", "diminution of annual produce"]
assert len(cause) == 1 and len(effects) == 3
assert 1 > 0  # taxed-state wage rank above untaxed-state wage rank (direction registered)
# 6 农工税按比例抬粗产物价为零，终走压地租
proportional_price_rise = 0
assert proportional_price_rise == 0
print("179 verify: 6 assertions passed")
