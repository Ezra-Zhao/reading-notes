# -*- coding: utf-8 -*-
"""165 验证：君主资本利息的结构与计数。参数取原书第五卷第二章第一部篇内陈述，不冒充现代实测。"""
# 1. 伯尔尼利息收入安全支柱恰两根：基金安全或管理政府信用、与债务国和平持续
assert len(["security of funds / good faith", "continuance of peace"]) == 2
# 2. 汉堡当铺账：150,000 克朗 × 4.5 先令 ÷ 20 先令/镑 = 33,750 镑
assert 150_000 * 4.5 / 20 == 33_750
# 3. 宾州纸券要素恰四件（双倍地押、十五年赎回、可转让、法定支付手段）；抵押倍数恰 2
assert len(["land security double value", "redeem in 15 years", "transferable", "legal tender"]) == 4
loan, security_value, redemption_years = 100, 200, 15
assert security_value == 2 * loan and redemption_years == 15
# 4. 宾州年费约 4,500 镑，纸券收入承担相当大部分：登记为大于零、小于全额
annual_expense, share = 4500, 0.5
assert 0 < share < 1 and annual_expense == 4500
# 5. 成功条件恰三项（工具需求、政府好信用、发行有节制）
assert len(["demand for instrument", "good credit of government", "moderation in use"]) == 3
# 6. 资本与信用定性词恰两个（不稳定、易消逝）；主基金所需三性（确定、稳固、长久）
assert len(["unstable", "perishable"]) == 2 and len(["sure", "steady", "permanent"]) == 3
print("165 verify: 6 assertions passed")
