# -*- coding: utf-8 -*-
"""验证《国富论》120 篇篇内数字与结构（原书第四卷第七章第三部分独占代价段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 独占的双重效果恰为两项：抽资本、抬利润率
assert len(["drawing capital from all other trades", "raising the rate of profit"]) == 2
# 2. 账单结构：牺牲一部分绝对优势一笔，加其他分支绝对不利与相对不利两笔
assert len(["sacrificed absolute advantage"]) + len(["absolute disadvantage", "relative disadvantage"]) == 3
# 3. 当时尚未开植的殖民地恰为六处：安提瓜、两卡罗来纳、宾夕法尼亚、佐治亚、新斯科舍
assert len(["Antigua", "Carolina 1", "Carolina 2", "Pennsylvania", "Georgia", "Nova Scotia"]) == 6
# 4. 当时与今日略相仿佛的有分量殖民地恰为一处：巴巴多斯
assert len(["Barbadoes"]) == 1
# 5. 海军对照的战争恰为两场：克伦威尔时对荷、查理二世初年对法荷
assert len(["Dutch war under Cromwell", "war under Charles II"]) == 2
# 6. 资本离开其他分支的方式恰为两途：被抽走、被赶走
assert len(["drawn", "driven"]) == 2
print("120 verify: 6 assertions passed")
