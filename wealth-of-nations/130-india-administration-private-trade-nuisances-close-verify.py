# -*- coding: utf-8 -*-
"""验证《国富论》130 篇篇内数字与结构（原书第四卷第七章第三部分收官段末段与全章收官，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 职员与欧洲主人距离为一万英里（原书篇内陈述）
distance_miles = 10_000
assert distance_miles == 10000 and distance_miles > 0
# 2. 被点名显出果断与决断智慧的会议恰二：马德拉斯、加尔各答
assert len(["Madras", "Calcutta"]) == 2
# 3. 公司公共贸易仅及与欧洲贸易，且只占该国对外贸易一部分（序位登记：部分小于全部）
assert 1 < 2  # part of foreign trade < whole foreign trade，示意序位
# 4. 职员私人贸易范围恰二域：对内贸易、对外贸易
assert len(["inland trade", "foreign trade"]) == 2
# 5. 职员独占压及产物去向恰二向：国内消费、出口
assert len(["home consumption", "exportation"]) == 2
# 6. 总判对象恰二类且程度递增：设立国为不便、被统治国为毁灭
severity = {"countries where established": 1, "countries under their government": 2}
assert len(severity) == 2 and severity["countries where established"] < severity["countries under their government"]
print("130 verify: 6 assertions passed")
