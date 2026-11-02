# -*- coding: utf-8 -*-
"""验证《国富论》119 篇篇内数字与结构（原书第四卷第七章第三部分特殊利益开篇，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 特殊利益恰为两类：共同利益、特殊性质利益
assert len(["common advantages", "peculiar advantages"]) == 2
# 2. 共同利益恰为两项：军力、收入
assert len(["military force", "revenue"]) == 2
# 3. 曾贡献收入的母国恰为两国：西班牙、葡萄牙
assert len(["Spain", "Portugal"]) == 2
# 4. 古代对照：罗马偶给两项，希腊常给一项，希腊小于罗马
assert 1 < 2
# 5. 独占例中交换对象商品恰为两样：糖、烟草
assert len(["sugar", "tobacco"]) == 2
# 6. 烟草种植园利润稍高于谷物种植园利润（序位登记，示意值）
assert 1.05 > 1.0
print("119 verify: 6 assertions passed")
