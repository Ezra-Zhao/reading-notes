# -*- coding: utf-8 -*-
"""验证《国富论》82 篇篇内数字与结构（取自原书第四卷第一章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 战费结构：逾 90M、新债 75M、差逾 15M；海外逾 2/3 即逾 60M
assert 90_000_000 - 75_000_000 == 15_000_000
assert 90_000_000 * 2 // 3 == 60_000_000
# 2. 存量往返：夸大估 30M ×2 = 60M 仍小于 90M；18M 估算 90/18 = 5 次量级
assert 30_000_000 * 2 < 90_000_000 and 90_000_000 // 18_000_000 == 5
# 3. 年流量对照：1761 年逾 19M 逾西葡年入 6M 的三倍；四个月战费约 19M/3 > 6M
assert 19_000_000 > 3 * 6_000_000 and 19_000_000 / 3 > 6_000_000
# 4. 银盘跌价链：今价 1/3、同支出购量 3 倍
assert abs(1 / 3 * 3 - 1) < 1e-9
# 5. 积存三部分与付账三途
assert len(["circulating money", "plate of private families", "treasure of the prince"]) == 3
assert len(["accumulated gold and silver", "annual produce of manufactures", "annual rude produce"]) == 3
# 6. 收官结构：真利 2、限制 2 类、鼓励 4 样、手段合计 6
assert len(["carry out surplus", "bring back what is wanted / widen market"]) == 2
assert 2 + 4 == 6
print("82 verify: 6 assertions passed")
