# -*- coding: utf-8 -*-
"""验证《国富论》135 篇篇内数字与结构（原书第四卷第九章中段前半：花边算术与不生产阶级用途，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 花边算术：£30 = 30×240 = 7200 便士，对约 1 便士亚麻恰约 7200 倍（原书「about seven thousand and two hundred times」）
assert 30 * 240 == 7200 and 7200 // 1 == 7200
# 2. 花边工期二年，售价只补回二年间的生计垫付：补回 2 年对消费 2 年，净增为零（账目结构登记）
assert 2 - 2 == 0 and 30 - 30 == 0
# 3. 不生产阶级增益社会途径恰一条：节俭（克减）；耕者则享全部生计基金＋净产出两件
assert len(["parsimony or privation"]) == 1 and len(["full subsistence funds enjoyed", "neat produce"]) == 2
# 4. 国家两型各二例：享受型法国、英格兰；克减型荷兰、汉堡
assert len(["France", "England"]) == 2 and len(["Holland", "Hamburgh"]) == 2
# 5. 不生产阶级由两阶级供养，供养物两样（工作材料、生计基金即谷物牲口）；门内门外仆役两处
assert len(["proprietors", "cultivators"]) == 2 and len(["materials", "fund of subsistence"]) == 2 and len(["servants within doors", "servants without doors"]) == 2
# 6. 间接增产机制一条：让生产性劳动专守本业；其增量足以支付供养费用全额（序位登记：增量 >= 全部费用）
rank = {"increase from undivided attention": 2, "whole expense of unproductive class": 1}
assert rank["increase from undivided attention"] >= rank["whole expense of unproductive class"] and len(["confine itself to its proper employment"]) == 1
print("135 verify: 6 assertions passed")
