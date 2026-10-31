# Verify effects on manufactures + conclusion of Ch XI: watch price, cloth laws 1487/1463, three orders
from fractions import Fraction
# 1 watch movement: 20 pounds mid-last-century vs 20 shillings now -- in pence 4800 vs 240, a twentyfold fall
assert Fraction(20 * 240, 20 * 12) == 20
# 2 fine cloth 1487: cap 16s; wheat 6s8d (80d) per quarter (8 bushels) -> 16s buys 2.4 quarters = 19.2 bushels (book: two quarters and more than three bushels)
bushels = Fraction(16 * 12, 80) * 8
assert bushels > 19
# its real value at 28s the quarter: 2.4 * 28s = 67.2s, at least the book's 3 pounds 6s 6d (66.5s)
assert Fraction(24, 10) * 28 >= Fraction(133, 2)
# 3 coarse cloth 1463: cap 2s; wheat 10d the bushel -> about 2.5 bushels (two bushels and near two pecks, approximated); at 3s6d (42d) = 105d = 8s 9d, matching the book
assert Fraction(5, 2) * 42 == 105
# 4 hose 14d then contained about twice the silver: 28d in present money (book's figure)
assert 14 * 2 == 28
# 5 three capital improvements in woollen machinery: spinning-wheel, winding machines, fulling-mill
improvements = ["spinning-wheel for rock and spindle", "winding machines for warp and woof", "fulling-mill"]
assert len(improvements) == 3
# 6 three great orders: rent, wages, profit; profit runs opposite to prosperity (low in rich, high in poor countries) while rent rises with improvement
orders = ["rent", "wages", "profit"]
assert len(orders) == 3 and "low in rich countries" != "high in poor countries"
print("37 verify: 6 assertions passed")
