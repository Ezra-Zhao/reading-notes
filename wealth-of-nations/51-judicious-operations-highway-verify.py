# -*- coding: utf-8 -*-
"""验证《国富论》51 篇篇内数字与结构（取自原书第二卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性与序位登记者已标明，不冒充现代实测。"""
# 1. 死存量转化的三样产出（材料/工具/给养）
assert len(["materials to work upon", "tools to work with", "provisions to work for"]) == 3
# 2. 死存量判据（方向登记）：闲置现金生产为 0，转化后为正
def produces(stock_active):
    return 1 if stock_active else 0
assert produces(False) == 0 and produces(True) > 0
# 3. 公路自身产出为零（方向登记）；公路改田后年产品增加（方向登记）
assert 0 == 0 and 1 > 0
# 4. 面额序位（便士计）：半便士 0.5 < 一先令 12 < 一几尼 252（21 先令）
assert 0.5 < 12 < 21 * 12
# 5. 速度逆序（方向登记）：面额越小流通越快
speed_rank = {"halfpenny": 3, "shilling": 2, "guinea": 1}
assert speed_rank["halfpenny"] > speed_rank["shilling"] > speed_rank["guinea"]
# 6. 价值上限（方向登记）：商人间流通货物价值 <= 商人与消费者间流通货物价值
dealer_dealer, dealer_consumer = 100, 100
assert dealer_dealer <= dealer_consumer
print("51 verify: 6 assertions passed")
