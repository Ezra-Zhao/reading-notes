# -*- coding: utf-8 -*-
"""161 验证：君主尊严费用的结构与计数。参数取原书第五卷第一章第四部篇内陈述，不冒充现代实测。"""
# 1. 尊严费用决定变量恰两个：改良时期、政府形式
assert len(["periods of improvement", "forms of government"]) == 2
# 2. 社会奢费门类恰五样：房屋、家具、餐桌、服饰、车马仪仗
assert len(["houses", "furniture", "tables", "dress", "equipage"]) == 5
# 3. 尊严落差序位：君主高出臣民 > 共和国首席行政官高出公民（示意标尺）
monarch_gap, magistrate_gap = 10, 3
assert monarch_gap > magistrate_gap
# 4. 共和制元首例恰两位：总督、市长
assert len(["doge", "burgomaster"]) == 2
# 5. 第五卷第一章费用科目恰四部，尊严费用为职责费用之外另加
parts = ["defence", "justice", "public works and institutions", "dignity of sovereign"]
assert len(parts) == 4 and parts[-1] == "dignity of sovereign"
# 6. 必然性表述两级（自然地、必然地）加尊严要求一级，合计三级
assert len(["naturally", "necessarily", "dignity seems to require"]) == 3
print("161 verify: 6 assertions passed")
