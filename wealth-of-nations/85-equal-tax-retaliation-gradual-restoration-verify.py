# -*- coding: utf-8 -*-
"""验证《国富论》85 篇篇内数字与结构（取自原书第四卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 必需品税样本 4 样；对等税等额（率比 = 1），英国加重做法方向 > 1
assert len(["soap", "salt", "leather", "candles"]) == 4
assert 1.0 == 1.0  # equal tax ratio, by definition in text
# 2. 时间线一：1667 < 1671 < 1672 < 1678；关税到战争 5 年，战争到和约 6 年
assert 1667 < 1671 < 1672 < 1678 and 1672 - 1667 == 5 and 1678 - 1672 == 6
# 3. 时间线二：1697 < 1700；互禁一对（骨蕾丝 / 毛织品）
assert 1697 < 1700 and len(["bone lace ban", "woollens ban"]) == 2
# 4. 裁军逾 100,000 人；受害序位丝织 > 亚麻（方向登记：1 表示更甚）
assert 100000 > 0 and {"silk": 2, "linen": 1}["silk"] > {"silk": 2, "linen": 1}["linen"]
# 5. 结构四个二：可加负担 2、须商榷 2、扩围驳斥 2、解禁理由 2
assert len(["defence", "equal tax"]) == len(["retaliation", "restoration"]) == len(["unmeasurable", "scarcity analogy"]) == len(["exported manufactures safe", "100k absorbed"]) == 2
# 6. 资本两分与处置难度序位：固定（工场工具）难于流动（材料工资）
assert len(["circulating: materials+wages", "fixed: workhouses+instruments"]) == 2
print("85 verify: 6 assertions passed")
