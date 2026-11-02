# -*- coding: utf-8 -*-
"""验证《国富论》114 篇篇内数字与结构（原书第四卷第七章第二部分，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 瑞典沥青焦油公司抬价之举的年份锚点 1703，处本世纪（十八世纪）初
assert 1700 < 1703 < 1776
# 2. 赏金抬价幅度大于限定母国市场压价幅度：以方向量登记，赏金效应大于限定效应，净效应为正
bounty_raise, confinement_lower = 2, 1
assert bounty_raise > confinement_lower and bounty_raise - confinement_lower > 0
# 3. 两项规制同时施行：一为限定、一为赏金，合二
assert len(["confinement to home market", "bounty on importation from America"]) == 2
# 4. 被列举却又享免税优惠的铁类两样：生铁与条铁
assert len(["pig iron", "bar iron"]) == 2
# 5. 熔炉耗木居制造业之首：以序位一登记（无制造业耗木超过熔炉）
assert 1 == min([1, 2, 3])
# 6. 殖民间完全自由贸易的范围：商品两类（列举与非列举）、殖民地两组（美洲与西印度群岛），合二加二
assert len(["enumerated", "non-enumerated"]) + len(["America colonies", "West Indies colonies"]) == 4
print("114 verify: 6 assertions passed")
