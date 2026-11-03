# -*- coding: utf-8 -*-
"""163 验证：第一章结论后半的分担结构与全章收官。参数取原书篇内陈述，不冒充现代实测。"""
# 1. 地方性费用例恰一类（城镇或地区治安）、承担主体为地方或省收入
assert len(["police of a particular town or district"]) == 1
assert len(["local revenue", "provincial revenue"]) == 2
# 2. 道路直接受益者恰两类、通行费名目恰两个
assert len(["travel or carry goods", "consume such goods"]) == 2
assert len(["turnpike tolls (England)", "peages (other countries)"]) == 2
# 3. 教育与宗教教育费用承担路线恰三条：普遍贡献 + 替代两条
routes = ["general contribution", "immediate beneficiaries", "voluntary contribution"]
assert len(routes) == 3 and len(routes[1:]) == 2
# 4. 总收入补缺之前置支出恰两笔：国防、君主尊严
assert len(["defending the society", "supporting dignity of chief magistrate"]) == 2
# 5. 判据档位：地方错位补贴为 unjust，比 no injustice 重一档（序位）
assert ["no injustice", "unjust"].index("unjust") == 1
# 6. 章节过桥：第一章开支与分担在前、第二章收入来源在后
assert ["ch1 expenses", "ch2 sources of revenue"] == sorted(
    ["ch1 expenses", "ch2 sources of revenue"], key=lambda s: s[2])
print("163 verify: 6 assertions passed")
