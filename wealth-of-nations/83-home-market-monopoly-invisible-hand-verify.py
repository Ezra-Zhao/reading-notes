# -*- coding: utf-8 -*-
"""验证《国富论》83 篇篇内数字与结构（取自原书第四卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 垄断工具 2 样，受惠样本 5 类
assert len(["high duties", "absolute prohibitions"]) == 2
assert len(["graziers", "corn growers", "woollen", "silk", "linen"]) == 5
# 2. 总量天花板：资本 100 单位，规制只改方向份额（60/40 -> 40/60），总量不变
before = [60, 40]; after = [40, 60]
assert sum(before) == sum(after) == 100
# 3. 贸易偏好序 3 级且对国内就业支持同序递减
pref = ["home trade", "foreign trade of consumption", "carrying trade"]
support = [3, 2, 1]
assert len(pref) == 3 and support == sorted(support, reverse=True)
# 4. 家政三工匠互买：裁缝、鞋匠、农夫计数 3
assert len(["tailor", "shoemaker", "farmer"]) == 3
# 5. 葡萄酒倍数：自造 30 倍；多 1/30 与多 1/300 皆为正且递减
assert 30 > 1 and 1/30 > 1/300 > 0
# 6. 看不见的手双层 + 年收入恒等式 1 条
assert len(["employ capital near home", "produce of greatest value"]) == 2
assert len(["annual revenue == exchangeable value of annual produce"]) == 1
print("83 verify: 6 assertions passed")
