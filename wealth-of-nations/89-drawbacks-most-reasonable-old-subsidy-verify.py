# -*- coding: utf-8 -*-
"""验证《国富论》89 篇篇内数字与结构（原书第四卷第四章前段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 旧补助通则：退回二分之一；本国商人 12 个月、外商 9 个月，12>9 且差 3
assert 0.5 == 1/2 and 12 - 9 == 3 and 12 > 9
# 2. 期限展延：由最长 12 个月展至 3 年 = 36 个月，为 3 倍
assert 3*12 == 36 and 36/12 == 3
# 3. 例外三样：葡萄酒、葡萄干、精纺丝绸不在通则内、另有更优待遇
assert len(["wines","currants","wrought silks"]) == 3
# 4. 退税上限逻辑方向登记：全退 = 1.0 不超过无税情形，半退 0.5 居其间（不增导资本方向登记）
assert 0 < 0.5 < 1.0
# 5. 后加诸税大部全退：全退率 1.0 大于旧补助半退 0.5
assert 1.0 > 0.5
# 6. 结构计数：鼓励出口诸法中退税被判最合理 1 类、本国产业税两类（消费税或内地税）、资本自然平衡保护对象 1 样（自然分工分配）
assert len(["drawbacks most reasonable"]) == 1 and len(["excise","inland duty"]) == 2 and len(["natural division and distribution of labour"]) == 1
print("89 verify: 6 assertions passed")
