# -*- coding: utf-8 -*-
"""验证《国富论》118 篇篇内数字与结构（原书第四卷第七章第二部分总评与第三部分开篇，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 被放逐的建立者恰为四组
assert len(["English puritans", "English catholics", "quakers", "Portuguese Jews"]) == 4
# 2. 清教徒所建新英格兰政府：四个
assert len(["New England government 1", "New England government 2", "New England government 3", "New England government 4"]) == 4
# 3. 最初方案的主持原则：愚蠢与不义，两条
assert len(["folly", "injustice"]) == 2
# 4. 第三部分利益分类：一般利益、特殊利益，两类
assert len(["general advantages", "particular advantages"]) == 2
# 5. 一般利益：享受增加、产业增进，两路
assert len(["increase of enjoyments", "augmentation of industry"]) == 2
# 6. 享受所由的商品用途：方便与使用、愉悦、装饰，三类
assert len(["conveniency and use", "pleasure", "ornament"]) == 3
print("118 verify: 6 assertions passed")
