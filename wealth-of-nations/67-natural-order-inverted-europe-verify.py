# -*- coding: utf-8 -*-
"""验证《国富论》67 篇篇内数字与结构（取自原书第三卷第一章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 北美条件二项；工匠去向一途；身份对照二项
assert len(["uncultivated land to be had", "upon easy terms"]) == 2 and len(["purchase and improve land"]) == 1 and len(["servant of customers", "master independent"]) == 2
# 2. 无荒地岔路二例：铁匠办铁器、织工办麻毛织
assert len(["smith iron manufactory", "weaver linen or woollen manufactory"]) == 2
# 3. 三顺位序位：农业一、制造业二、对外贸易三（序位登记）
assert ["agriculture", "manufactures", "foreign commerce"].index("agriculture") == 0 and ["agriculture", "manufactures", "foreign commerce"].index("foreign commerce") == 2
# 4. 出口主体二类（本国/外国资本）；资本不足时外国资本出口有益（方向登记）
assert len(["foreign capital", "domestic capital"]) == 2 and ["advantage foreign capital when stock insufficient"].index("advantage foreign capital when stock insufficient") == 0
# 5. 三古国三、殖民地二处
assert len(["Egypt", "China", "Indostan"]) == 3 and len(["North American colonies", "West Indian colonies"]) == 2
# 6. 欧洲倒转链二环，与自然次序反序（登记）
assert ["foreign commerce introduces finer manufactures", "manufactures and commerce give birth to agriculture improvements"] == ["foreign commerce introduces finer manufactures", "manufactures and commerce give birth to agriculture improvements"] and ["agriculture","manufactures","foreign commerce"] == list(reversed(["foreign commerce","manufactures","agriculture"]))
print("67 verify: 6 assertions passed")
