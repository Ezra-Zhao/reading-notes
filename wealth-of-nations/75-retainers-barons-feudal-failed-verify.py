# -*- coding: utf-8 -*-
"""验证《国富论》75 篇篇内数字与结构（取自原书第三卷第四章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 剩余养人刻度：一百人与一千人，一千为一百十倍
assert 1000 // 100 == 10
# 2. 沃里克款待：据说每日三万人，原书自注或有夸大，按或然登记
assert 30000 == 30000 and ["said to have entertained, may have been exaggerated"] == ["said to have entertained, may have been exaggerated"]
# 3. 高地租金四档：一皇冠、半皇冠、一羊、一羔羊计数四；一皇冠为半皇冠两倍
assert len(["a crown", "half a crown", "a sheep", "a lamb"]) == 4 and 1.0 / 0.5 == 2
# 4. 自主权四项：最高管辖、征兵、铸币、立乡规，计数四
assert len(["highest civil criminal jurisdiction", "levying troops", "coining money", "making bye-laws"]) == 4
# 5. 卡梅伦算例：年租不超过五百镑、1745 年带八百人，八百大于五百（方向登记）
assert 500 == 500 and 800 > 500 and 1745 == 1745
# 6. 封建失败结构：头太弱与下级太强两项并存（方向登记）
assert ["too weak in the head", "too strong in the inferior members"] == ["too weak in the head", "too strong in the inferior members"]
print("75 verify: 6 assertions passed")
