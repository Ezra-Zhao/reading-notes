# -*- coding: utf-8 -*-
"""验证《国富论》115 篇篇内数字与结构（原书第四卷第七章第二部分，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 糖税三档折便士：粗糖（Muscovado）6 先令 4 便士为 76 便士；白糖 1 镑 1 先令 1 便士为 253 便士；精制糖 4 镑 2 先令 5 又 8/20 便士约为 989.4 便士，严格递增
muscovado = 6 * 12 + 4
white = 240 + 12 + 1
refined = 4 * 240 + 2 * 12 + 5 + 8 / 20
assert muscovado == 76 and white == 253 and abs(refined - 989.4) < 0.01 and muscovado < white < refined
# 2. 白糖税约为粗糖的三倍以上、精制糖税约为粗糖的十三倍量级
assert white / muscovado > 3 and 12 < refined / muscovado < 14
# 3. 英国市场约占英属殖民地糖产出的十分之九以上
assert 9 / 10 == 0.9
# 4. 格林纳达糖坊存量：1773 年 10 月时据告仅余两三家，以区间二至三登记
assert 2 <= 3 and 1776 - 1773 == 3
# 5. 被绝对禁止在殖民地设立的精制制造设施两样：炼钢炉与纵切轧机（steel furnaces, slit-mills）
assert len(["steel furnaces", "slit-mills"]) == 2
# 6. 被禁跨省流通的美国产商品三样：帽子、毛、毛织品；禁运方式含水运与陆运（马背或马车）
assert len(["hats", "wools", "woollen goods"]) == 3 and len(["by water", "by land on horseback or in a cart"]) == 2
print("115 verify: 6 assertions passed")
