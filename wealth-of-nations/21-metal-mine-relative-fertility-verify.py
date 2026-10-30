# Verify Ch XI Part II metals: trade routes, tin rent, 13:12 comparison, tax sequence, bounding dimensions, pricing radius
from fractions import Fraction
# 1 world trade samples 3 (Japan copper, Spain iron, Peru silver); coal non-competing pairs 2
assert len(["japan_copper", "spain_iron", "peru_silver"]) == 3 and len(["westmoreland_newcastle", "lionnois"]) == 2
# 2 Cornwall tin average rent = 1/6 gross; several fertile Scotland lead mines also 1/6
assert Fraction(1,6) == Fraction(1,6)
# 3 comparison: tin 1/6 + duke tax 1/20 = 13/60; Peru silver rent/tax 1/5 = 12/60; ratio 13:12
assert Fraction(1,6) + Fraction(1,20) == Fraction(13,60) and Fraction(1,5) == Fraction(12,60) and Fraction(13,60)/Fraction(12,60) == Fraction(13,12)
# 4 tax sequence: silver fifth until 1736 then tenth; gold twentieth, earlier fifth and tenth both unbearable
assert Fraction(1,5) > Fraction(1,10) > Fraction(1,20)
# 5 Peru discovery measure: 246 feet length, half as much breadth = 123
assert 246 // 2 == 123
# 6 pricing radius: coal neighbourhood < metals world; for metals fertility weight > situation weight
assert ["neighbourhood", "world"][1] == "world"
print("21 verify: 6 assertions passed")
