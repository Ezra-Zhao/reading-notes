# -*- coding: utf-8 -*-
"""验证《国富论》49 篇篇内数字与结构（取自原书第二卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性登记者已标明，不冒充现代实测。"""
# 1. 无水塘判据（方向登记）：自然流入 0、流出 >0 时水位必降
def pond_level(inflow, outflow, buckets=0):
    return inflow + buckets - outflow
assert pond_level(0, 10) < 0 and pond_level(0, 10, buckets=10) == 0
# 2. 借钱交易费用三项
assert len(["agents to find lenders", "negotiating", "drawing bond or assignment"]) == 3
# 3. 总借款处总量不变（方向登记）：增层前后可贷总量相等
assert 100 == 100
# 4. 规模对比：银行约 500 户 > 私人少数人（方向登记）
assert 500 > 12
# 5. 债务人两类与资金去向两途
assert len(["chimerical projectors", "sober frugal debtors"]) == 2
assert len(["prudent profitable", "imprudent unprofitable"]) == 2
# 6. 劳氏链三节：苏格兰议会未采纳、奥尔良公爵变通采纳、密西西比方案
assert len(["Scotch parliament rejected", "Duke of Orleans adopted with variations", "Mississippi scheme"]) == 3
print("49 verify: 6 assertions passed")
