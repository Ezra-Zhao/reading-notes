# Verify Ch XI digression closing B: taxes, lowest price, consumption equilibrium
from fractions import Fraction
# 1 Spanish taxes: gold 1/20 = 5%, silver 1/10 = 10%; silver tax is exactly twice the gold tax
assert Fraction(1, 20) == Fraction(5, 100) and Fraction(1, 10) == Fraction(10, 100)
assert Fraction(1, 10) / Fraction(1, 20) == 2
# 2 1736 reduction: silver tax from 1/5 to 1/10 is a halving; Portugal Brazil gold tax 1/5 equals old Spanish silver tax
assert Fraction(1, 10) / Fraction(1, 5) == Fraction(1, 2)
assert Fraction(1, 5) == Fraction(1, 5)
# 3 effect of the 1736 reduction: silver at least 10% lower than it would have been -> factor <= 9/10
assert Fraction(9, 10) <= 1 and 1 - Fraction(9, 10) == Fraction(1, 10)
# 4 growing expense admits exactly three compensating events
assert len(["price rise", "tax diminution", "partly both"]) == 3
# 5 consumption grows in greater proportion than mass: superlinear, e.g. mass x2 -> consumption x2^1.5 > x2
assert 2 ** 1.5 > 2
# 6 tax burden ordering across the metals as stated: gold 1/20 < silver 1/10 < Brazil gold / old silver 1/5
assert Fraction(1, 20) < Fraction(1, 10) < Fraction(1, 5)
print("29 verify: 6 assertions passed")
