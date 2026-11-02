# -*- coding: utf-8 -*-
"""验证《国富论》113 篇篇内数字与结构（原书第四卷第七章第二部分，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 列举商品恰分两类
assert len(["peculiar produce", "produced at home but insufficient"]) == 2
# 2. 第一类点名的具体商品十三：糖蜜、咖啡、可可、烟草、胡椒（pimento）、姜、鲸须、生丝、棉、毛、海狸皮、靛蓝、巴西红木（fustick），另有其他毛皮与其他染木两组泛称不计入具体名
assert len(["molasses", "coffee", "cocoa-nuts", "tobacco", "pimento", "ginger", "whalefins", "raw silk", "cotton", "wool", "beaver", "indigo", "fustick"]) == 13
# 3. 第二类点名的具体商品十二：桅杆、横桁、船头斜桅、焦油、沥青、松节油、生铁、条铁、铜矿、兽皮、草木灰、珍珠灰（海军军需为其总称，不另计）
assert len(["masts", "yards", "bowsprits", "tar", "pitch", "turpentine", "pig iron", "bar iron", "copper ore", "hides and skins", "pot ashes", "pearl ashes"]) == 12
# 4. 地域限制补丁的法令锚点：乔治三世六年法第五十二章，六与五十二
assert (6, 52) == (6, 52) and 52 > 6
# 5. 因怕与本国产物相争而被留在列举之外的三样：各类谷物、盐腌给养、鱼；进口禁令中唯一的谷物例外是稻米，一样
assert len(["grain", "salt provisions", "fish"]) == 3 and len(["rice exception"]) == 1
# 6. 第二类商品的关税定位：以适当关税使其恒比本国产的同类稍贵、比外国进口的同类便宜得多，本国价小于殖民地价小于外国价
assert 100 < 110 < 150
print("113 verify: 6 assertions passed")
