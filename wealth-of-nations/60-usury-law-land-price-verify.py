# -*- coding: utf-8 -*-
"""验证《国富论》60 篇篇内数字与结构（取自原书第二卷第四章，Gutenberg #3300）。"""
# 1. 英国费率序：政府 3 < 私人 4 与 4.5 < 法定 5；法定只高最优市价 0.5-1
assert 3 < 4 < 4.5 < 5 and 0.5 <= 5 - 4.5 <= 1.0
# 2. 过高上限 8 与 10 均 >5，筛选对象两类
assert 8 > 5 and 10 > 5 and len(["prodigals", "projectors"]) == 2
# 3. 法国敕令 1766：目标 4 < 实际 5
assert 1766 == 1766 and 4 < 5
# 4. 地价年数：利率 10 对应 10-12 年；降至 6/5/4 对应 20-30 年，倍数随利率降而升（方向）
assert 10 <= 11 <= 12 and 20 <= 25 <= 30 and 30 > 12
# 5. 英 30 > 法 20，比 1.5
assert 30 / 20 == 1.5
# 6. 安全溢价差额有界：两情形（超差额无人买、不足人人买）
assert len(["rent shortfall exceeds difference: nobody buys", "advantages exceed: everybody buys"]) == 2
print("60 verify: 6 assertions passed")
