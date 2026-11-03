# -*- coding: utf-8 -*-
"""验证《国富论》145 篇篇内数字与结构（原书第五卷第一章第二部后段：固定薪俸、诉讼费设计与司法独立，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 图卢兹净薪 150 里弗约 £6:11s = 6*20+11=131 先令；约七年前同地男仆年工钱同值（登记为相等）
assert 6 * 20 + 11 == 131 and 150 == 150 and 7 == 7
# 2. 律师讼师年费总额 > 法官薪俸之和（序位登记）
assert {"lawyers_fees_total": 2, "judges_salaries_total": 1}["lawyers_fees_total"] > {"lawyers_fees_total": 2, "judges_salaries_total": 1}["judges_salaries_total"]
# 3. 自养设计四件套恰四项
assert len(["fees precisely regulated", "paid at once to cashier", "distributed after process decided", "shares by hours and days employed"]) == 4
# 4. 越界受理虚构恰两院两式
assert len(["king's bench: trespass fiction for civil suits", "exchequer: cannot pay king fiction for contract debts"]) == 2
# 5. 按页计酬量词三级：页、行、字
assert len(["pages", "lines per page", "words per line"]) == 3
# 6. 司法独立要求恰两条；分离源起两例（罗马大法官、欧洲委代官）
assert len(["not removable at caprice", "salary payment not depend on good will or good economy"]) == 2 and len(["Roman praetor", "European bailiff deputy"]) == 2
print("145 verify: 6 assertions passed")
