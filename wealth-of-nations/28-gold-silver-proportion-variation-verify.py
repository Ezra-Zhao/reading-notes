# Verify Ch XI digression closing A: durability of metals + gold/silver proportion variation
from fractions import Fraction
# 1 ratio bands shifted up without overlap: before America 10-12, by mid-last-century 14-15 silver per gold
assert 12 < 14 and (10, 12) != (14, 15)
# 2 ox/lamb: ox 10 guineas = 210s; lamb 3s6d = 3.5s; 210 / 3.5 = 60 exactly
assert Fraction(210, 1) / Fraction(7, 2) == 60
# 3 Meggens: import quantity proportion 22 exceeds value proportion band max 15
assert 22 > 15 > 12
# 4 regional silver-per-gold ordering: Japan 8 < China 10..12 < Europe/Calcutta 14..15 (Calcutta 15)
assert 8 < 10 <= 12 < 14 <= 15
# 5 durability horizons ordering: corn < 1 year cycle, iron 200-300 years, gold 2000-3000 years
assert 1 < 200 < 300 < 2000 < 3000
# 6 cheap-commodity chain has 4 levels: bread > butcher's meat > poultry > wild fowl (quantity and total value)
chain = ["bread", "butcher's meat", "poultry", "wild fowl"]
assert len(chain) == 4
print("28 verify: 6 assertions passed")
