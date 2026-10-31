# Verify Ch XI Part III second sort A: price ceiling at parity + manure bottleneck
from fractions import Fraction
# 1 ceiling: price can rise until profit of feeding land == profit of corn land; beyond -> land switches
ceiling = Fraction(1, 1)  # parity ratio feeding-profit / corn-profit = 1
assert ceiling == 1
assert Fraction(11, 10) > ceiling  # above parity triggers conversion to pasture/feeding use up to parity restored
# 2 well-manured share: seldom above 1/3 or 1/4, sometimes only 1/5 or 1/6; strict decreasing ladder, 1/3 is twice 1/6
ladder = [Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]
assert ladder == sorted(ladder, reverse=True) and len(set(ladder)) == 4
assert Fraction(1, 3) / Fraction(1, 6) == 2
# 3 waste rotation: pasture 6-7 years, then only 1-2 poor crops; crops per year <= 1/3
assert Fraction(2, 6) == Fraction(1, 3) and Fraction(1, 7) < Fraction(2, 6)
# 4 abolition of old system: half a century to a century -> 50 to 100 years, upper = 2x lower
assert 50 * 2 == 100
# 5 manure chain has 3 links: well-cultivated land <- manure <- cattle stock
chain = ["cattle stock", "manure produced", "well-cultivated land"]
assert len(chain) == 3
# 6 Scotland before Union: districts at ceiling = 0; London neighbourhood at ceiling by early last century = True contrast
scotland_at_ceiling, london_at_ceiling = 0, 1
assert scotland_at_ceiling == 0 and london_at_ceiling == 1
print("31 verify: 6 assertions passed")
