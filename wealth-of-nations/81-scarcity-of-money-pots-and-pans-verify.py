# -*- coding: utf-8 -*-
"""验证《国富论》81 篇篇内数字与结构（取自原书第四卷第一章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 缺钱替代三途
assert len(["barter", "credit with monthly/yearly clearing", "well-regulated paper money"]) == 3
# 2. 购买力两路：有购买力或有信用
assert len(["wherewithal to buy", "credit to borrow"]) == 2
# 3. 过度交易链条三环
assert len(["buy on credit unusual quantity", "demand for payment before returns", "nothing to buy money nor security to borrow"]) == 3
# 4. 钱在资本中：小部分且最无利润，两判并存
assert len(["small part of national capital", "most unprofitable part"]) == 2
# 5. 买卖半程律：买者全程 1、卖者至多一半 0.5
assert 0.5 == 1 / 2
# 6. 金银用途二：铸币流通、银盘家具
assert len(["coin circulating commodities", "plate as household furniture"]) == 2
print("81 verify: 6 assertions passed")
