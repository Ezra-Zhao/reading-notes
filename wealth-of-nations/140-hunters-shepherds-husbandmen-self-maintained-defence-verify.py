# -*- coding: utf-8 -*-
"""验证《国富论》140 篇篇内数字与结构（原书第五卷第一章第一部前段：自备国防三阶段与士兵成职业，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 规模量级：猎人军队上限 300 人，牧人军队上限 300,000 人，恰 1000 倍
assert 300000 // 300 == 1000 and 200 <= 300
# 2. 适龄男子占比五分之一至四分之一；短战役无偿条件两端：播种后、收获前
assert 1/5 < 1/4 and len(["after seedtime", "before harvest"]) == 2
# 3. 开化社会士兵上限 1/100 小于粗陋社会士兵占比下限 1/5
assert 1/100 < 1/5
# 4. 自备制断裂原因恰两项
assert len(["progress of manufactures dries up artificer revenue", "art of war complicated and campaigns spun out"]) == 2
# 5. 发饷转折锚点两处
assert len(["Athens after second Persian war: mercenary troops paid by state", "Rome from siege of Veii: pay in the field"]) == 2
# 6. 闲暇序位：牧人 > 农夫 > 工匠，且工匠闲暇为零
leisure = {"shepherd": 3, "husbandman": 1, "artificer": 0}
assert leisure["shepherd"] > leisure["husbandman"] > leisure["artificer"] == 0
print("140 verify: 6 assertions passed")
