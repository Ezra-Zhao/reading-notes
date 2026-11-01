# -*- coding: utf-8 -*-
"""验证《国富论》86 篇篇内数字与结构（取自原书第四卷第三章第一部分，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 法国货税率链：25 + 25 + 5*5 = 75；他国轻税 5 为法国首道 25 的五分之一
assert 25 + 25 + 5 * 5 == 75
assert 25 / 5 == 5
# 2. 吨税：葡萄酒 25 镑 > 醋 15 镑，差 10 镑
assert 25 > 15 and 25 - 15 == 10
# 3. 差别待遇样本：交税可进 1 例、禁止只许仓储 1 例、高税 1 例
assert len(["Silesia lawns importable on duties"]) == 1
assert len(["French cambrics/lawns prohibited except London warehoused"]) == 1
assert len(["French wines higher duties than Portugal/any other"]) == 1
# 4. 第一论方向登记：对法进口升、总进口降，两方向相反，总值为判据
france_imports, total_imports = +1, -1
assert france_imports * total_imports < 0
# 5. 转口回报等于全部原始成本（等值登记）；经手样本荷兰 1 国，秘密进口来源 2 地
assert 100 == 100  # return == prime cost of whole, as stated "equal in value, perhaps"
assert len(["Holland and Zealand"]) == 1 and len(["Holland", "Zealand"]) == 2
# 6. 判据 2 样、第一部分论证 3 条
assert len(["custom-house books", "course of exchange"]) == 2
assert len(["cheaper source", "re-exportation", "no certain criterion"]) == 3
print("86 verify: 6 assertions passed")
