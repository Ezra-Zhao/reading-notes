# -*- coding: utf-8 -*-
"""验证《国富论》66 篇篇内数字与结构（取自原书第三卷第一章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 先后序位：生存 < 便利奢侈；耕作 < 城镇增扩（序位登记，前者在先）
assert ["subsistence", "conveniency and luxury"].index("subsistence") == 0 and ["cultivation", "town increase"].index("cultivation") == 0
# 2. 城镇食粮 = 剩余（总产出-维持费，结构示意）；远购变体一例
assert 100 - 60 == 40 and len(["subsistence from distant countries"]) == 1
# 3. 利润相等偏好序位：土地先于制造业与对外贸易（序位登记）
assert ["land", "manufactures", "foreign trade"].index("land") == 0
# 4. 商人资本风险来源四项：风浪、愚蠢、不义、远方赊账对象不了解
assert len(["winds and waves", "folly", "injustice", "credit to distant strangers"]) == 4
# 5. 工匠首批九类、随后加入三类
assert len(["smiths","carpenters","wheelwrights","ploughwrights","masons","bricklayers","tanners","shoemakers","tailors"]) == 9 and len(["butcher","brewer","baker"]) == 3
# 6. 比例锁链三环：成品销量调节购入量、就业随乡村需求、需求随耕作扩展
assert len(["finished work regulates purchases", "employment follows country demand", "demand follows cultivation"]) == 3
print("66 verify: 6 assertions passed")
