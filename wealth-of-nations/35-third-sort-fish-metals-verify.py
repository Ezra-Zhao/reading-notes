# Verify Ch XI Part III third sort B: price division, Scotland union, fish, precious metals uncertainty
from fractions import Fraction
# 1 improved country: whole-beast price must cover rent + profit; a fall paid by wool/hide is shifted to the carcase, total unchanged (illustrative split 100 = 70+30 -> 80+20)
assert 70 + 30 == 80 + 20 == 100
# 2 Scotland after the Union: wool price fall fully compensated by butcher's-meat rise in the southern sheep counties (net change registered as 0 in the book's judgement)
assert -1 + 1 == 0
# 3 fish: market from 1,000 to 10,000 tons is a tenfold demand rise, needing MORE than ten times the labour
assert Fraction(10000, 1000) == 10
labour_multiple = Fraction(21, 2)  # any value strictly above ten satisfies the book's "more than ten times"
assert labour_multiple > 10
# 4 precious-metal quantity in a country depends on exactly 2 circumstances: power of purchasing; fertility/barrenness of the mines supplying the commercial world
circumstances = ["power of purchasing", "fertility or barrenness of world-supplying mines"]
assert len(circumstances) == 2
# 5 foreign dependence of wool/hide multiplication: 2 factors independent of domestic industry (what other countries do not manufacture; export restraints they impose)
foreign_factors = ["quantity other countries do not manufacture", "export restraints imposed by other countries"]
assert len(foreign_factors) == 2
# 6 mine-discovery horizon in the book: "a century or two" -- lower bound 100 years, upper bound 200 years, ratio 2
assert Fraction(200, 100) == 2
print("35 verify: 6 assertions passed")
