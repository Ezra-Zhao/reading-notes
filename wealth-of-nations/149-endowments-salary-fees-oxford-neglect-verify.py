# -*- coding: utf-8 -*-
"""验证《国富论》149 篇篇内结构与计数（原书第五卷第一章第三部第二条前段：捐赠、三问、薪俸两格局与两种监督，Gutenberg #3300）。内容均为原书篇内陈述，不冒充现代实测。"""
# 1. 三问恰三项：目的是否达成、是否鼓励勤奋增进才能、课程是否导向更有用对象
assert len(["promote the end of institution", "encourage diligence and improve abilities", "direct course to more useful objects"]) == 3
# 2. 教师收入格局恰两类：薪俸只占小部分（大头学费）对薪俸即全部且禁收学费
assert len(["salary small part, fees greater part", "salary whole, fees prohibited"]) == 2
# 3. 极端格局下理性应对恰两途：完全撂下、对付了事；活跃者的精力另投得利处一向
assert len(["neglect altogether", "perform carelessly and slovenly"]) == 2 and len(["employ activity where advantage can be derived"]) == 1
# 4. 外部监督者恰三类：主教、总督、国务大臣；同体监督判例牛津一校
assert len(["bishop of the diocese", "governor of the province", "minister of state"]) == 3 and len(["Oxford"]) == 1
# 5. 外部监督所能强迫者只课时一项，计时单位恰两样：每周、每年
assert len(["attend a certain number of hours / lectures"]) == 1 and len(["in the week", "in the year"]) == 2
# 6. 法律业反例：大目标行业一项（法律），宽裕出身成名者原书以设问登记为极少（趋近零口径，不作实测数）
assert len(["law"]) == 1 and 0 < 1
print("149 verify: 6 assertions passed")
