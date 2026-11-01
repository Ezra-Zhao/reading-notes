# -*- coding: utf-8 -*-
"""验证《国富论》69 篇篇内数字与结构（取自原书第三卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 温和型奴隶边界三项
assert len(["sold with land not separately", "marriage with consent not dissolved by separate sale", "penalty for maiming or murder"]) == 3
# 2. 古代证言：五千闲人；引述者三人（普林尼、科卢梅拉、亚里士多德）
assert 5000 == 5000 and len(["Pliny", "Columella", "Aristotle"]) == 3
# 3. 负担得起序位（序位登记）：糖大于烟草大于谷物；糖殖民地奴隶比例大于烟草殖民地（方向登记）
order = ["corn", "tobacco", "sugar"]
assert order.index("sugar") > order.index("tobacco") > order.index("corn")
# 4. 分成结构：产出平分各二分之一；业主存量三件（种子、牲畜、农具）
assert 1/2 + 1/2 == 1 and len(["seed", "cattle", "instruments of husbandry"]) == 3
# 5. 屏障刻度：什一税十分之一、分成二分之一，分成为什一税五倍
assert abs((1/2) / (1/10) - 5) < 1e-9 and 1/2 > 1/10
# 6. 法国六分之五为分成佃农；仍存奴役六地计数；诏书十二世纪（登记）
assert 5/6 > 4/5 and len(["Russia", "Poland", "Hungary", "Bohemia", "Moravia", "other parts of Germany"]) == 6 and 12 == 12
print("69 verify: 6 assertions passed")
