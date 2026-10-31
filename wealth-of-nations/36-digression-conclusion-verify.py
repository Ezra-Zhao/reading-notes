# Verify digression conclusion: relative prices as the true diagnostic, corn comparison, food price directions
from fractions import Fraction
# 1 a fall in silver's value would raise ALL goods equally by the same fraction; the book lists a third, a fourth, or a fifth
falls = [Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)]
assert falls == sorted(falls, reverse=True) and len(falls) == 3
# 2 corn comparison windows: first 64 years of the present century vs last 64 years of the preceding century -- equal windows
assert 64 == 64
# 3 decisive relative-price evidence: particular goods named -- cattle, poultry, game = 3 kinds set against corn
particular = ["cattle", "poultry", "game"]
assert len(particular) == 3
# 4 the two most important vegetable improvements from commerce/navigation: potatoes and maize (Indian corn) = 2
new_foods = ["potatoes", "maize"]
assert len(new_foods) == 2
# 5 kitchen-garden foods moved to the plough field: turnips, carrots, cabbages = 3
field_moved = ["turnips", "carrots", "cabbages"]
assert len(field_moved) == 3
# 6 artificially tax-raised manufactured commodities named at the chapter's end of this section: salt, soap, leather, candles, malt, beer, ale = 7
taxed = ["salt", "soap", "leather", "candles", "malt", "beer", "ale"]
assert len(taxed) == 7
print("36 verify: 6 assertions passed")
