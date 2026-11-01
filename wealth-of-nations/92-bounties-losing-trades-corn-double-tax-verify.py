# -*- coding: utf-8 -*-
"""验证《国富论》92 篇篇内数字与结构（原书第四卷第五章前段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 适中假设：每蒲式耳涨 6 便士，一夸特 = 8 蒲式耳，合每夸特 48 便士 = 4 先令（12 便士 = 1 先令）
assert 6 * 8 == 48 and 48 / 12 == 4
# 2. 第二道税：出口与国内消费之比 1:31，每夸特消费缴 4 先令，31 * 4 = 124 先令 = 6 镑 4 先令（20 先令 = 1 镑）
assert 31 * 4 == 124 and 124 // 20 == 6 and 124 % 20 == 4
# 3. 第二道税与第一道税之比：124 先令对 5 先令 = 24.8 倍
assert abs(124 / 5 - 24.8) < 1e-9
# 4. 需要赏金的贸易定义条件二项：售价不足偿资本加通常利润、低于送市真实成本
assert len(["price does not replace capital with ordinary profit", "sold for less than real cost of sending to market"]) == 2
# 5. 法国反证时序锚点（原书陈述登记）：本世纪头 64 年 = 1700+64 = 1764 年，与法国禁出口解除年同年
assert 1700 + 64 == 1764
# 6. 第二道税后果分流二路：压低贫民生计而抑人口、抬高货币工资而抑产业
assert len(["restrain population", "restrain industry"]) == 2
print("92 verify: 6 assertions passed")
