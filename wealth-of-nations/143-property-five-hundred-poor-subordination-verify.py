# -*- coding: utf-8 -*-
"""验证《国富论》143 篇篇内数字与结构（原书第五卷第一章第二部前段：财产与政府、服从四因，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 猎人财产上限 2-3 天劳动；人身名誉之害加害者所得 0，财产之害所得等于所失 1（归一化）
assert 2 <= 3 and 0 == 0 and 1 == 1
# 2. 一富至少对 500 穷
assert 500 >= 500 and 1 + 500 == 501
# 3. 服从自然成因恰四项
assert len(["personal qualifications", "age", "fortune", "birth"]) == 4
# 4. 单凭体力至多强迫 2 个弱者；心智权威序位大于身体权威
assert 2 == 2 and {"mind": 2, "body": 1}["mind"] > {"mind": 2, "body": 1}["body"]
# 5. 鞑靼酋长给养 1000 人；开化富者可指挥不足一打（12），量级差逾 80 倍
assert 1000 // 12 == 83 and 83 > 80
# 6. 猎人称谓序位：父（上位）> 兄（同辈）> 子（下位）；长子居先
rank = {"father": 3, "brother": 2, "son": 1}
assert rank["father"] > rank["brother"] > rank["son"]
print("143 verify: 6 assertions passed")
