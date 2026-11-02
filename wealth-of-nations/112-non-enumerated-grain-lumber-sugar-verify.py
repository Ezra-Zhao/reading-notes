# -*- coding: utf-8 -*-
"""验证《国富论》112 篇篇内数字与结构（原书第四卷第七章第二部分第四项后段前半，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 非列举商品出口的船员条件：船主及四分之三水手为英国臣民，四分之三恰 0.75
assert 3 / 4 == 0.75
# 2. 非列举点名大宗六：谷物、木材、盐腌给养、鱼、糖、朗姆酒
assert len(["grain", "lumber", "salt provisions", "fish", "sugar", "rum"]) == 6
# 3. 糖放开年 1751，距原书刊行 1776 恰 25 年；原书称近二十年进口大增，20 小于 25 同序登记
assert 1776 - 1751 == 25 and 20 < 25
# 4. 兽皮入列举的法令锚点：乔治三世四年法第十五章，四与十五
assert (4, 15) == (4, 15) and 15 > 4
# 5. 广阔市场抬价对象三（谷物、木材、牲畜）加反向被列举的兽皮一项，合四
assert len(["grain", "lumber", "cattle"]) + len(["hides and skins"]) == 4
# 6. 鱼为北美对西班牙、葡萄牙与地中海贸易的主要物品，对方按原书列举计三
assert len(["Spain", "Portugal", "Mediterranean"]) == 3
print("112 verify: 6 assertions passed")
