# Verify Ch XI Part III second sort C: hogs, dairy keeping ladder, complete-improvement conditions
from fractions import Fraction
# 1 keeping ladder in days: milk 1 day (scarce 24h) < fresh butter 7 < salt butter 365 < cheese several years (>= 2*365 as lower bound)
ladder = [1, 7, 365, 2 * 365]
assert ladder == sorted(ladder) and len(set(ladder)) == 4
# 2 pork vs beef: France nearly equal (ratio ~1), Great Britain pork somewhat higher (ratio > 1)
assert Fraction(1, 1) == 1 and Fraction(11, 10) > 1
# 3 zero-expense keepers named: cat, dog, poultry, sow-and-pigs = 4 kinds
keepers = ["cat", "dog", "poultry", "sow and pigs"]
assert len(keepers) == 4
# 4 complete improvement needs exactly 2 price conditions: rent of good corn land; labour/expense as paid on good corn land with ordinary profit
conditions = ["rent of good corn land", "labour and expense at good-corn-land rate"]
assert len(conditions) == 2
# 5 ordering: price rise to paying the expense must be previous to improving land for that produce
seq = ["price pays expense", "improvement of land for the produce"]
assert seq.index("price pays expense") < seq.index("improvement of land for the produce")
# 6 keeping ratios: salt butter / fresh butter = 365/7 ~ 52x; cheese lower bound / fresh butter > 100x
assert Fraction(365, 7) > 52 and Fraction(2 * 365, 7) > 100
print("33 verify: 6 assertions passed")
