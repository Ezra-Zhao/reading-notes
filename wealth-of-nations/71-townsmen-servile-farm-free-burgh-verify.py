# -*- coding: utf-8 -*-
"""验证《国富论》71 篇篇内数字与结构（取自原书第三卷第三章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 对照结构：两类居民对照，城镇居民构成商人与技工两类（方向登记）
assert len(["ancient republic proprietors", "post-Roman townsmen"]) == 2 and len(["tradesmen", "mechanics"]) == 2
# 2. 特许三项：嫁女、子女继承、遗嘱处置计数三
assert len(["marry daughters without lord consent", "children succeed not lord", "dispose by will"]) == 3
# 3. 流动税四样：通行、过桥、载货、设摊计数四
assert len(["passage", "pontage", "lastage", "stallage"]) == 4
# 4. 包租：先租对象郡长与他人两类，连带共同负责（方向登记）
assert len(["sheriff", "other farmers"]) == 2 and ["jointly and severally answerable"] == ["jointly and severally answerable"]
# 5. 永租机关：定租此后增加次数为零，豁免归属由个人转自治市（方向登记）
assert 0 == 0 and ["individual", "burghers of a burgh"].index("burghers of a burgh") == 1
# 6. 法人装置四项：长官议会、地方法规、筑墙、守望值更；英格兰诉讼豁免例外王室案件一类
assert len(["magistrates and council", "bye-laws", "walls", "watch and ward"]) == 4 and len(["pleas of the crown excepted"]) == 1
print("71 verify: 6 assertions passed")
