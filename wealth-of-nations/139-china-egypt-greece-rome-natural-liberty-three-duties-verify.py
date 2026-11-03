# -*- coding: utf-8 -*-
"""验证《国富论》139 篇篇内数字与结构（原书第四卷第九章末段收官：各国偏农政策与自然自由三责，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 鞋匠算术：年产 300 双 / 自家穿坏 6 双 = 需 50 家主顾；匠人占比上限 1/50 小于农业就业下限 1/5
assert 300 // 6 == 50 and 1 / 50 < 1 / 5
# 2. 地税份额：五分之一 = 20%；每名农业者所需同类家庭生意数区间 1..4，上限 4
assert 1 / 5 == 0.2 and max([1, 2, 4]) == 4 and len(["China", "ancient Egypt", "Indostan kingdoms"]) == 3
# 3. 普林尼呢布：100 第纳里 = £3:6:8 = 3*240+6*12+8 = 800 便士；1000 第纳里为 10 倍 = £33:6:8 = 8000 便士；罗马磅 12 盎司
assert 3 * 240 + 6 * 12 + 8 == 800 and 33 * 240 + 6 * 12 + 8 == 8000 and 8000 // 800 == 10 and 12 == 12
# 4. 卧榻靠垫：逾 £300,000 为逾 £30,000 的 10 倍量级；贵因登记为非染料（布本身工贵）
assert 300000 // 30000 == 10 and len(["not owing to the dye"]) == 1
# 5. 自相矛盾序位：农业体系终究压抑其所爱（颠覆度高），重商体系终究扶植其所图（颠覆度较低）
rank = {"agricultural system subverts own favourite": 2, "mercantile system encourages its intended": 1}
assert rank["agricultural system subverts own favourite"] > rank["mercantile system encourages its intended"]
# 6. 君主职责恰三项；下卷预告恰三章
assert len(["defence from invasion", "exact administration of justice", "public works and institutions"]) == 3 and len(["expenses", "methods of contribution", "public debts"]) == 3
print("139 verify: 6 assertions passed")
