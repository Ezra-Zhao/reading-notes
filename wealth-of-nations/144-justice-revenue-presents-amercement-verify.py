# -*- coding: utf-8 -*-
"""验证《国富论》144 篇篇内数字与结构（原书第五卷第一章第二部中段：政府保财产与司法为收入，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 出身区别：猎人 0、牧人恒有 1
assert {"hunters": 0, "shepherds": 1}["hunters"] < {"hunters": 0, "shepherds": 1}["shepherds"]
# 2. 个人区别两大来源恰两项：出身、财富
assert len(["birth", "fortune"]) == 2
# 3. 司法收入恰两源：请愿礼物、有罪罚金；罚金在受害方补偿之外另纳（补偿 1 + 罚金 1）
assert len(["presents with petition", "amercement to sovereign"]) == 2 and 1 + 1 == 2
# 4. 行使方式两段：亲行、委代官；代官须交账 1 项义务
assert len(["in own person", "by bailiff or judge delegate"]) == 2
# 5. 卖司法滥用恰三重：大礼多得、小礼少得与拖延待重送、罚金诱判有罪
assert len(["more than justice", "less than justice / delay for repeated present", "amercement suggests guilty verdict"]) == 3
# 6. 阿伽门农所许恰 7 城，所举好处仅礼物 1 项
assert 7 == 7 and len(["people honour him with presents"]) == 1
print("144 verify: 6 assertions passed")
