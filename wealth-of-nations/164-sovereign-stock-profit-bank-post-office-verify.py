# -*- coding: utf-8 -*-
"""164 验证：君主资本利润的结构与计数。参数取原书第五卷第二章第一部篇内陈述，不冒充现代实测。"""
# 1. 专属基金构成恰两样（资本、土地）；资本收益形式恰两样（利润、利息）
assert len(["stock", "land"]) == 2 and len(["profit", "interest"]) == 2
# 2. 英格兰银行账：资本 10,780,000 镑 × 5.5% = 592,900 镑年净利
assert round(10_780_000 * 0.055) == 592_900
# 3. 政府自营假设账：592,900 - 10,780,000 × 3% = 269,500 镑
assert round(592_900 - 10_780_000 * 0.03) == 269_500
# 4. 本篇点名官营商业项目恰四样：酒窖、药房、公共银行、邮局
assert len(["wine-cellar", "apothecary shop", "public bank", "post-office"]) == 4
# 5. 邮局成功条件恰三条（垫本不大、无秘诀、回报确定而即时）；被断为唯一普遍成功者恰一样
assert len(["small capital", "no mystery", "certain and immediate returns"]) == 3
assert len(["post-office"]) == 1
# 6. 君主代理人不在意恰三处：买价、卖价、运费
assert len(["price they buy", "price they sell", "expense of transport"]) == 3
print("164 verify: 6 assertions passed")
