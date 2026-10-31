# Verify Ch XI Part III third sort A: wool and raw hides -- appendage limit, market extent, English wool fall
from fractions import Fraction
# 1 Saxon fleece estimated at two-fifths of the whole sheep (Hume, as cited in the book)
assert Fraction(2, 5) == Fraction(4, 10) and Fraction(2, 5) > Fraction(1, 3)
# 2 tod of wool = 28 lb; Edward III money price 10s then contained 6 oz silver ~ 30s present; good price now 21s; money ratio 30:21 = 10:7
assert Fraction(30, 21) == Fraction(10, 7)
# 3 real price: 10s at 6s8d/quarter (8 bushels) buys 12 bushels; 21s at 28s/quarter buys 6 bushels; real ratio 2:1
assert Fraction(10 * 12, 80) * 8 == 12 and Fraction(21 * 12, 28 * 12) * 8 == 6 and Fraction(12, 6) == 2
# 4 artificial degradation of English wool: exactly 3 regulations (export ban from England; Spanish wool duty-free in; Irish wool forced to England only)
regs = ["export of wool from England prohibited", "Spanish wool imported duty free", "Irish wool exportable only to England"]
assert len(regs) == 3
# 5 salt-provision exporters of butcher's meat named as the only ones believed: Ireland and part of British America = 2
exporters = ["Ireland", "part of British America"]
assert len(exporters) == 2
# 6 Fleetwood 1425 account: 5 ox hides 12s + 5 cow hides 7s3d + 36 sheep skins 9s + 16 calf skins 2s = 62 skins, 363 pence in all
skins = 5 + 5 + 36 + 16
pence = 12 * 12 + (7 * 12 + 3) + 9 * 12 + 2 * 12
assert skins == 62 and pence == 363
print("34 verify: 6 assertions passed")
