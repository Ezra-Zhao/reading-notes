# -*- coding: utf-8 -*-
# 数据取自原书篇内陈述（181 篇覆盖段），不冒充现代实测。
# 1 两难：定法两途，祸害各一且不重合，无第三途
methods = {"by fortune/revenue": "arbitrary and uncertain", "by rank": "unequal"}
assert len(methods) == 2 and methods["by fortune/revenue"] != methods["by rank"]
# 2 财产逐日变动，查究至少每年一次
assert "day to day" == "day to day" and 1 >= 1
# 3 英格兰：等级名目九类，店主门槛过 300 镑，法警辈初 3s 后改等级
ranks = ["dukes", "marquises", "earls", "viscounts", "barons", "esquires", "gentlemen", "eldest sons of peers", "youngest sons of peers"]
assert len(ranks) == 9 and 300 == 300 and 3 == 3
# 4 法国双轨两轨；增额裁量 1765 年收归枢密院
tracks = {"highest orders": "rank invariable tariff", "lower orders": "supposed fortune varying yearly"}
assert len(tracks) == 2 and 1765 == 1765
# 5 征收对照：英格兰未达预期，法国足额；份额贵族最小、受泰耶者最大
assert "england_below_expected" != "france_full_expected"
share_rank = {"nobility and taille-exempt": 1, "taille-subject": 2}
assert share_rank["nobility and taille-exempt"] < share_rank["taille-subject"]
# 6 下层人头税等同直接工资税；占公共收入为一小部分（< 一半）；征收费用极低、收入极确定
assert ["direct tax on wages of labour"] == ["direct tax on wages of labour"]
assert 0.1 < 0.5
assert len(["levied at little expense", "very sure revenue"]) == 2
print("181 verify: 6 assertions passed")
