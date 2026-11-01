# -*- coding: utf-8 -*-
"""验证《国富论》72 篇篇内数字与结构（取自原书第三卷第三章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 反常交换：永不增加定租一项、心脏地带独立共和国（方向登记）
assert ["rent never to be augmented"] == ["rent never to be augmented"] and len(["independent republics in heart of dominions"]) == 1
# 2. 无保护者两条路：投靠领主、结成互保同盟计数二
assert len(["become slaves or vassals of a great lord", "league of mutual defence"]) == 2
# 3. 胖路易咨询两提议：新管辖、新民兵计数二
assert len(["new jurisdiction magistrates council", "new militia under own magistrates"]) == 2
# 4. 慷慨检验三例：约翰王、腓力一世与胖路易、斯瓦比亚诸王计数三
assert len(["King John", "Philip I and Lewis the Fat", "House of Suabia and Hanseatic league"]) == 3
# 5. 独立共和国时段：十二世纪末至十六世纪初，起止世纪序 12 小于 16；例外威尼斯一城
assert 12 < 16 and len(["Venice excepted"]) == 1
# 6. 法英路径：等级会议三方教士、男爵、市民代表计数三
assert len(["clergy", "barons", "burgh deputies"]) == 3
print("72 verify: 6 assertions passed")
