# Verify Ch XI digression: East Indies market, gold/silver ratios, Birmingham consumption, Meggens and Raynal import accounts
from fractions import Fraction
# 1 tea imports 1,500,000l per year = 30x Birmingham annual consumption 50,000l
assert Fraction(1500000, 50000) == 30
# 2 ratios do not overlap: India 10-12 oz silver per oz gold, Europe 14-15; India max 12 < Europe min 14
assert 12 < 14 and 10 < 15
# 3 Birmingham 50,000 is 1/120 of annual importation 6,000,000
assert Fraction(50000, 6000000) == Fraction(1, 120)
# 4 Meggens: silver 1,101,107 lb x 62s; gold 49,940 lb x 44.5 guineas (guinea=21s); compare to book totals within tolerance
silver = Fraction(1101107 * 62, 20)
gold = Fraction(49940) * Fraction(89, 2) * Fraction(21, 20)
book_silver = Fraction(3413431) + Fraction(10, 20)
book_gold = Fraction(2333446) + Fraction(14, 20)
assert abs(silver - book_silver) < 1 and abs(gold - book_gold) < 1
assert abs((silver + gold) - (Fraction(5746878) + Fraction(4, 20))) < 2
# 5 Raynal: 17,000,000 piastres x 4s6d = 3,825,000l exactly; 2,250,000 + 3,825,000 = 6,075,000
assert Fraction(17000000) * Fraction(9, 40) == 3825000
assert 2250000 + 3825000 == 6075000
# 6 East India trade carrier nations named in this section: Portuguese, Dutch, English, French, Swedes, Danes, Muscovites = 7
assert len(["Portuguese", "Dutch", "English", "French", "Swedes", "Danes", "Muscovites"]) == 7
print("27 verify: 6 assertions passed")
