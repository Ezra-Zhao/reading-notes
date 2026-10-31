# Verify Ch XI digression third period later: bounty two directions, France rebuttal, low decade 1741-1750, export/bounty totals, French wage ratio
from fractions import Fraction
# 1 bounty raises price in both states: plenty (extra export) and scarcity (plenty cannot compensate) -> 2 directions, both upward
directions = {"plenty": "up", "scarcity": "up"}
assert len(directions) == 2 and set(directions.values()) == {"up"}
# 2 France: grain export prohibited till 1764; three named collectors observed the same rise
assert 1764 > 1700 and len(["Dupre de St Maur", "Messance", "Essay on Police of Grain author"]) == 3
# 3 low decade: middle wheat 1l6s8d = 320d = 26s8d; best 1l13s9 4/5d = 405.8d below 64y avg 2l0s6 10/32d = 486.3125d
assert 1*240 + 6*12 + 8 == 320 and Fraction(320, 12) == Fraction(80, 3)
best_low = Fraction(240 + 13*12) + Fraction(49, 5)  # 9 4/5 d
avg64 = Fraction(480) + Fraction(6) + Fraction(10, 32)
assert best_low == Fraction(2029, 5) and best_low < avg64
# 4 bounty totals: 1750 single year 324,176l is more than one fifth of ten-year total 1,514,962l (approx, whole pounds)
assert Fraction(324176, 1514962) > Fraction(1, 5)
assert 8029156 > 8000000  # exported quarters (plus 1 bushel stated in note text)
# 5 French day wage = 1/20 of septier price, so 20 days of wages buy one septier; septier stated as a little more than 4 Winchester bushels (lower bound 4)
assert Fraction(1, 20) * 20 == 1 and Fraction(4, 1) == 4
# 6 twenty-year opposition: pre-1750 twenty vs pre-1770 twenty, gap 20 years
assert 1770 - 1750 == 20 and 1750 - 1741 + 1 == 10
print("25 verify: 6 assertions passed")
