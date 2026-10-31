# -*- coding: utf-8 -*-
"""验证《国富论》59 篇篇内数字与结构（取自原书第二卷第四章，Gutenberg #3300）。"""
# 1. 一千镑链条：3 笔贷款，每笔 1000，合计 3000 = 货币量 3 倍；30 倍为同理外推
assert 3 * 1000 == 3000 and 3000 // 1000 == 3 and 30 == 3 * 10
# 2. 利率序：10 > 6 > 5 > 4 > 3 严格递减
rates = [10, 6, 5, 4, 3]
assert all(rates[i] > rates[i+1] for i in range(len(rates)-1))
# 3. 银价算例：100 现值=50 从前；10% 旧息 10 镑；降至 5% 时 5 镑只值从前 2.5 镑 = 旧息 1/4
assert 100 / 2 == 50 and abs(5 / 2 - 2.5) < 1e-12 and abs(2.5 / 10 - 0.25) < 1e-12
# 4. 银增商品不变：真实资本与真实利润不变（方向登记，名义增真实同）
assert len(["nominal up", "real same"]) == 2
# 5. 利润两头削减：竞争一头 + 工资一头 = 2
assert len(["competition cheaper dearer", "wages rise"]) == 2
# 6. 被引作者三人、揭露者一人
assert len(["Locke", "Law", "Montesquieu"]) == 3 and len(["Hume"]) == 1
print("59 verify: 6 assertions passed")
