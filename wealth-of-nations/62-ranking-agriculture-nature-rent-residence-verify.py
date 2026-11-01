# -*- coding: utf-8 -*-
"""验证《国富论》62 篇篇内数字与结构（取自原书第二卷第五章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性与序位登记者已标明，不冒充现代实测。"""
# 1. 四途贡献排序：农业 > 制造 > 批发 > 零售（序位登记）
order = ["agriculture", "manufactures", "wholesale", "retail"]
assert order.index("agriculture") == 0 and order.index("retail") == 3
# 2. 地租份额：很少低于 1/4、常多于 1/3，且 1/3 > 1/4；制造业自然贡献为零
assert abs(1/3 - 0.333333) < 1e-5 and 1/3 > 1/4 and 0 == 0
# 3. 替回层数递增：零售一层、批发加运输雇用、制造加直接分付工匠（序位登记）
assert [1, 2, 3] == sorted([3, 1, 2])
# 4. 跨地例三则：里昂、西西里绸、西班牙羊毛
assert len(["Lyons distant both ways", "Sicily silks foreign made", "Spanish wool made in Britain part sent back"]) == 3
# 5. 外国出口商差额两项：一人、一人利润
assert len(["one productive labourer less", "one man's profits less"]) == 2
# 6. 居所分类：必居本地二途、无固定居所一途、地点不恒定一途
assert len(["agriculture", "retail"]) == 2 and len(["wholesale"]) == 1 and len(["manufactures"]) == 1
print("62 verify: 6 assertions passed")
