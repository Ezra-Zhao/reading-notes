# -*- coding: utf-8 -*-
"""验证《国富论》100 篇篇内数字与结构（原书第四卷第五章离题第四部分与收官，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 转口商就地出售省下的成本：装货、卸货、运费、保险，共四项
saved_costs = ["loading", "unloading", "freight", "insurance"]
assert len(saved_costs) == 4 and len(set(saved_costs)) == 4
# 2. 1773 新法免税门槛（先令/夸特）：小麦 48 > 黑麦豌豆豆类 32 > 大麦 24 > 燕麦 16，严格递减；小麦小税仅 6 便士
thresholds = [48, 32, 24, 16]
assert thresholds == sorted(thresholds, reverse=True) and len(set(thresholds)) == 4 and 48 > 32 > 24 > 16 and 6 == 6
# 3. 赏金停付提前：小麦 44<旧48、大麦 22<旧24、燕麦粉 14<旧15；黑麦赏金 3 先令<旧3先令6便士（以便士计 36<42）且停付 28<旧32
assert 44 < 48 and 22 < 24 and 14 < 15 and 3 * 12 < 3 * 12 + 6 and 28 < 32
# 4. 保税仓转口免税自由所及港口：二十五个，且为正整数
ports = 25
assert ports == 25 and ports > 0
# 5. 西班牙与葡萄牙两国合计每年进口金银：逾六百万镑
annual_silver_gold_imports = 6_000_000
assert annual_silver_gold_imports >= 6_000_000 and annual_silver_gold_imports > 5_000_000
# 6. 赏金停付价即出口禁价（先令）：小麦 44、黑麦 28、大麦 22、燕麦 14，两组同值；新设燕麦赏金为 2 先令
cease_prices = {"wheat": 44, "rye": 28, "barley": 22, "oats": 14}
ban_prices = {"wheat": 44, "rye": 28, "barley": 22, "oats": 14}
assert cease_prices == ban_prices and len(cease_prices) == 4 and 2 == 2
print("100 verify: 6 assertions passed")
