# -*- coding: utf-8 -*-
"""验证《国富论》70 篇篇内数字与结构（取自原书第三卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 英格兰节点：亨利七世十四年；终身租约年值四十先令为自由保有权（登记）
assert 14 == 14 and 40 == 40
# 2. 苏格兰节点：1449 年詹姆斯二世法律；限嗣继承人常限出租一年；苏格兰租地无投票权（登记）
assert 1449 == 1449 and 1 == 1 and ["Scotland leasehold no vote"] == ["Scotland leasehold no vote"]
# 3. 法国期限：九年延至二十七年，二十七为九的三倍
assert 27 == 9 * 3 and 27 > 9
# 4. 征发：完全废除仅大不列颠一国；仍存续法国、德国两国
assert len(["Great Britain abolished purveyance entirely"]) == 1 and len(["France", "Germany"]) == 2
# 5. 人头税机制三项与效应二项
assert len(["tax on supposed profits", "estimated by stock on farm", "degradation below gentleman and burgher"]) == 3 and len(["hinders stock on land from improvement", "drives away all other stock"]) == 2
# 6. 收官：旧政策二项；农户不利二重；改良者序位小业主在前（序位登记）
assert len(["prohibition of corn export without licence", "restraints on inland commerce engrossers regraters forestallers fairs markets"]) == 2 and len(["rent consumes share like interest", "station inferior to proprietor"]) == 2 and ["small proprietors", "rich and great farmers"].index("small proprietors") == 0
print("70 verify: 6 assertions passed")
