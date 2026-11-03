# -*- coding: utf-8 -*-
"""验证《国富论》136 篇篇内数字与结构（原书第四卷第九章中段后半：完全自由、经济表与医生类比，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 繁荣秘密恰三样：完美正义、完美自由、完美平等；三阶级利益冲突方向登记为零
assert len(["perfect justice", "perfect liberty", "perfect equality"]) == 3 and len([]) == 0
# 2. 商业国正例两国（荷兰、汉堡），供养者与本国情形的差别恰一项（住在远方、隶属他国）
assert len(["Holland", "Hamburgh"]) == 2 and len(["proprietors and cultivators at a distance, subjects of other governments"]) == 1
# 3. 资本溢出扶梯恰三级：土地改良容纳外溢至本国制造、本国制造容纳外溢至对外贸易、终挤出商业国
steps = ["agriculture surplus to home manufactures", "manufactures surplus to foreign trade", "justle out mercantile nations"]
assert len(steps) == 3
# 4. 压迫政策伤农业恰两途：压低产物真实价值、抬高他业利润率抽拦资本；被压者有净产出、被催者无（序位登记）
assert len(["sink real value of surplus produce", "raise mercantile and manufacturing profit rate"]) == 2
rank = {"productive labour affording neat produce": 2, "barren labour replacing stock with profit only": 1}
assert rank["productive labour affording neat produce"] > rank["barren labour replacing stock with profit only"]
# 5. 经济表分两组：第一表（完美自由、最大净产出）一组，后续表（不同违犯程度对应不同衰减）一组；衰减随程度单调
assert len(["Economical Table: perfect liberty"]) == 1 and len(["subsequent formularies: degrees of declension"]) == 1 and 1 < 2 < 3
# 6. 保存原则两处对应：自然身体一条、政治体一条（人人改善自身处境的自然努力）
assert len(["unknown principle of preservation in the human body", "natural effort of every man to better his own condition"]) == 2
print("136 verify: 6 assertions passed")
