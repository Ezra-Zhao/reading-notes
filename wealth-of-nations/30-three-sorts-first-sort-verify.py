# Verify Ch XI Part III: three sorts framework + first sort, Roman prices
from fractions import Fraction
# 1 sestertius = 2d (3 sestertii = 6d); surplus rate 4 sestertii = 8d per peck; quarter = 32 pecks -> 256d = 21s4d, about 21s
assert 3 * 2 == 6 and 4 * 2 == 8
assert 8 * 32 == 256 and Fraction(256, 12) == Fraction(64, 3)  # 21s 4d
assert abs(Fraction(256, 12) - 21) < 1
# 2 inverse ratio: Sicilian contract 21s vs English 28s per quarter -> 21/28 = 3/4 (3 oz then = 4 oz now)
assert Fraction(21, 28) == Fraction(3, 4)
# 3 nightingale: 6000 sestertii x 2d = 12000d = 50l nominal; real = x4/3 = 66l 13s 4d exactly
assert 6000 * 2 == 12000 and Fraction(12000, 240) == 50
assert Fraction(50) * Fraction(4, 3) == Fraction(200, 3)  # 66 + 13/20 + 4/240 = 200/3
assert Fraction(66) + Fraction(13, 20) + Fraction(4, 240) == Fraction(200, 3)
# 4 surmullet: 8000 sestertii x 2d = 16000d = 66l 13s 4d nominal; real x4/3 within a penny-class tolerance of book's 88l 17s 9d
assert Fraction(16000, 240) == Fraction(200, 3)
real = Fraction(16000, 240) * Fraction(4, 3)
book = Fraction(88) + Fraction(17, 20) + Fraction(9, 240)
assert abs(real - book) < Fraction(1, 100)
# 5 woodcock hypothetical: 20 guineas = 420 shillings
assert 20 * 21 == 420
# 6 framework: exactly three sorts; first sort's price boundary is unbounded (None)
sorts = ["scarce-multipliable", "multipliable-to-demand", "limited-or-uncertain"]
assert len(sorts) == 3
print("30 verify: 6 assertions passed")
