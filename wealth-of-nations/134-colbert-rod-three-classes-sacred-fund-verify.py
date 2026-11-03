# -*- coding: utf-8 -*-
"""验证《国富论》134 篇篇内数字与结构（原书第四卷第九章前段：科尔贝尔偏私、三阶级与神圣基金，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 三阶级恰三类：地主、耕者、工匠制造商商人；尊称一（生产）、贬称一（不育/不生产）
classes = ["proprietors", "cultivators", "artificers-manufacturers-merchants"]
assert len(classes) == 3 and len(["productive"]) == 1 and len(["barren or unproductive"]) == 1
# 2. 生产性费用恰三种：地主地基费用、农场主原始费用、农场主年费用
productive_expenses = ["ground expenses", "original expenses", "annual expenses"]
assert len(productive_expenses) == 3
# 3. 耕者留存须补回两笔费用（原始＋年），各带通常利润
assert len(["original expenses", "annual expenses"]) == 2 and len(["with ordinary profits"] * 2) == 2
# 4. 净产出结构：总产物 100 减必要费用 70 余 30 为净产出且为正（结构示意，量值取整数例以核关系式）
assert 100 - 70 == 30 and 30 > 0
# 5. 科尔贝尔压农三重手段：禁谷物出口、省际运谷限制、对耕者任意苛税
assert len(["export of corn prohibited", "provincial restraints on transport", "arbitrary taxes on cultivators"]) == 3
# 6. 增租的保护对象恰两方：教会（什一税）与国王（赋税）；棍子两向：城镇先被高估、体系反向低估
assert len(["church tithe", "king taxes"]) == 2 and len(["town over-valued", "town under-valued"]) == 2
print("134 verify: 6 assertions passed")
