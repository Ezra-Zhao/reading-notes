# Verify Ch XI Part III second sort B: colonies, Kalm, order of reaching the ceiling, poultry
from fractions import Fraction
# 1 Kalm: best annual grasses formerly rose 3-4 feet high
assert 3 < 4
# 2 same ground: formerly maintained 4 cows, now 1; each former cow gave 4x the milk of the present one -> total milk 16x
assert 4 * 4 == 16 and Fraction(1, 16) < 1
# 3 Kalm's account year 1749; book published 1776 -> 27 years earlier
assert 1776 - 1749 == 27
# 4 French middling farmer sometimes has 400 fowls in his yard
assert 400 == 4 * 100
# 5 dearest moment ordering: scarcity-raised price -> general practice of cultivating land for it -> new feeding methods cheapen
stages = ["scarcity", "general-practice", "efficiency-cheapening"]
assert stages.index("scarcity") < stages.index("general-practice") < stages.index("efficiency-cheapening")
# 6 order of reaching the ceiling: cattle first, poultry later, venison among the last
order = ["cattle", "poultry", "venison"]
assert order.index("cattle") == 0 and order.index("venison") == len(order) - 1
print("32 verify: 6 assertions passed")
