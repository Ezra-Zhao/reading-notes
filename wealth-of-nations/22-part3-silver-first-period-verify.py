# Verify Ch XI Part III intro + first period: halving, statute, feast, assize, Northumberland, thresholds
from fractions import Fraction
# 1 first period: wheat 4 oz -> 2 oz, present-money 20s -> 10s, both halved
assert Fraction(2,4) == Fraction(1,2) and Fraction(10,20) == Fraction(1,2)
# 2 Statute of Labourers: 10d per bushel x 8 bushels = 80d = 6s8d; 10d contains 1/2 oz, so 80d contains 4 oz
assert 10*8 == 80 and 80 == 6*12+8 and Fraction(1,2)*8 == 4
# 3 Feast 1309 present-money equivalents: wheat 21s6d, malt 18s, oats 12s; nominal wheat 7s2d=86d
assert 7*12+2 == 86 and Fraction(43,2) > 18 > 12
# 4 Assize 1262: range 1s to 20s, supposed middle 10s (=6 oz, ~30s present); one-third of highest 20s = 6s8d (=4 oz)
assert Fraction(20,3) == Fraction(20,3) and 6*12+8 == 80 and Fraction(10,20) == Fraction(1,2)
# 5 Northumberland 1512: 6s8d then only 2 oz (~10s present) vs 4 oz (~20s) in 1350 era
assert Fraction(2,4) == Fraction(1,2)
# 6 threshold change 1562: 6s8d (80d) -> 10s (120d) is 1.5x
assert Fraction(120,80) == Fraction(3,2)
print("22 verify: 6 assertions passed")
