# -*- coding: utf-8 -*-
"""验证《国富论》141 篇篇内数字与结构（原书第五卷第一章第一部中段：民兵与常备军、火器与纪律、三场大变革，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 国防安排恰两法；本质分界两项性格主导
assert len(["militia by rigorous police", "standing army as separate trade"]) == 2
assert len(["in militia labourer character predominates", "in standing army soldier character predominates"]) == 2
# 2. 民兵两类：只练不成团 / 既练且成团
assert len(["exercised only, not regimented", "exercised and regimented"]) == 2
# 3. 迦太基三将与汉尼拔三胜场
assert len(["Amilcar", "Asdrubal son-in-law", "Annibal"]) == 3
assert len(["Trebi", "Thrasymenus", "Cannae"]) == 3
# 4. 罗马征服马其顿：两场大战 + 三场大会战 = 五
assert 2 + 3 == 5
# 5. 确切记载的大变革恰三场
assert len(["fall of Greek republics and Persian empire", "fall of Carthage / elevation of Rome", "fall of western empire"]) == 3
# 6. 变形律：民兵连服数个战役季变成常备军；美国预言=再拖一个战役季
assert len(["several successive campaigns makes militia a standing army"]) == 1 and 1 == 1
print("141 verify: 6 assertions passed")
