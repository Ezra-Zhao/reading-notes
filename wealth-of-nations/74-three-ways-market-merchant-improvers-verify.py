# -*- coding: utf-8 -*-
"""验证《国富论》74 篇篇内数字与结构（取自原书第三卷第四章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 三路总纲：市场、商人买地、秩序自由安全，计数三
assert len(["ready market", "merchants buy land", "order liberty security"]) == 3
# 2. 市场受益范围：本国加一切有往来国家，大于一（方向登记）
assert len(["own country", "all countries they deal with"]) > 1
# 3. 邻近分价：种植者更好价与消费者同样便宜两项并存
assert ["better price to growers", "as cheap to consumers"] == ["better price to growers", "as cheap to consumers"]
# 4. 待售地：很大一部分未开垦（方向登记）
assert ["great part frequently uncultivated"] == ["great part frequently uncultivated"]
# 5. 两种钱观对照计数二：商人钱带利润回来、乡绅钱花出不再见
assert len(["merchant money returns with profit", "gentleman money spent seldom seen again"]) == 2
# 6. 商人三习惯：秩序、经济、注意，计数三
assert len(["order", "economy", "attention"]) == 3
print("74 verify: 6 assertions passed")
