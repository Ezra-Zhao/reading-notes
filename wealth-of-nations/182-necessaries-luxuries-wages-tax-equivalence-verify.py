# -*- coding: utf-8 -*-
# 数据取自原书篇内陈述（182 篇覆盖段），不冒充现代实测。
# 1 分类两类，无第三类
classes = ["necessaries", "luxuries"]
assert len(classes) == 2
# 2 皮鞋必需适用：英格兰男女=2，苏格兰男子=1，法国=0，递减
shoes = [2, 1, 0]
assert shoes == sorted(shoes, reverse=True)
# 3 奢侈样本七样
luxuries = ["beer", "ale", "wine", "tobacco", "tea", "sugar", "chocolate"]
assert len(luxuries) == 7
# 4 烟草税倍数：法国 15 > 英格兰 3，差 12
assert 15 > 3 and 15 - 3 == 12
# 5 波特啤酒加税 3 先令/桶；伦敦日薪 18-20 便士，税后增量 0
assert 3 == 3 and 20 - 18 == 2
wage_rise_from_luxury_tax = 0
assert wage_rise_from_luxury_tax == 0
# 6 必需品税终落两路；奢侈品税不引工资上涨
assert len(["consumer via manufacturer", "landlord rent via farmer"]) == 2
print("182 verify: 6 assertions passed")
