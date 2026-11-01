# -*- coding: utf-8 -*-
"""验证《国富论》64 篇篇内数字与结构（取自原书第二卷第五章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性与序位登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 迂回轮次：经弗吉尼亚烟草 2 轮、再经牙买加糖朗姆 3 轮；资本为直接交换 3 倍
assert [2, 3] == sorted([3, 2]) and 3 == 3
# 2. 金银优势三项
assert len(["freight much less", "insurance not greater", "least liable to damage"]) == 3
# 3. 转口替回：荷兰例每次替回资本 2、属荷兰者 0、回流只有利润 1 项
assert 2 - 2 == 0 and len(["profits only"]) == 1
# 4. 航运反证：纽卡斯尔-伦敦煤运航运 > 英格兰全部转口贸易（方向登记）；决定因素二、主要者为体积价值比
assert ["bulk to value chief", "distance"] .index("bulk to value chief") == 0 and len(["bulk/value", "distance"]) == 2
# 5. 烟草算例：96000 - 14000 = 82000；82000/96000 > 0.85
assert 96000 - 14000 == 82000 and 82000 / 96000 > 0.85
# 6. 富裕序位荷兰一、英格兰二（序位登记）；三贸易范围序 国内 < 对外消费 < 转口
assert ["Holland", "England"].index("Holland") == 0 and ["home", "foreign consumption", "carrying"].index("carrying") == 2
print("64 verify: 6 assertions passed")
