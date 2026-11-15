#!/usr/bin/env python3
"""Verification for Market Wizards 21: Cai Songsong. All arithmetic recomputed from public figures."""
from datetime import date

# 1. Tenure: 2019-02-20 (first appointment, Lion/Nuoan Growth) -> 2023-09-28 (last funds resigned)
d = (date(2023, 9, 28) - date(2019, 2, 20)).days
assert d == 1681, d
assert abs(d / 365.25 - 4.60) < 0.01
# co-management with Wang Chuanglian until 2020-05-14
d_co = (date(2020, 5, 14) - date(2019, 2, 20)).days
assert d_co == 449, d_co

# 2. Annual return chain of Nuoan Growth (calendar years, fund reports / reviews):
# 2019 +95.44%, 2020 +39.10%, 2021 +22.50%, 2022 -40.04%
cum = 1.9544 * 1.3910 * 1.2250 * 0.5996
assert abs(cum - 1.9968) < 0.001, cum  # ~2.00x over four calendar years despite the -40% year

# 3. A -40.04% year needs +66.78% just to break even
need = 1 / (1 - 0.4004) - 1
assert abs(need * 100 - 66.78) < 0.01, need * 100

# 4. Scale from the fund's own annual report (units: 100m CNY / yi):
# 2019YE owners' equity 6,696,818,318.64 CNY = 66.97 yi; 2020YE = 327.76 yi
assert abs(327.76 / 66.97 - 4.89) < 0.01
assert abs(327.76 - 66.97 - 260.79) < 0.01
# 2021YE scale 274.08 is 83.62% of 2020YE
assert abs(274.08 / 327.76 * 100 - 83.62) < 0.05

# 5. Manager-level AUM (iFinD via Beijing Business Today): 2021Q2 355.07 -> 2022Q2 306.16, -13.77%
assert abs((355.07 - 306.16) / 355.07 * 100 - 13.77) < 0.01

# 6. Tenure return at departure for Nuoan Growth +71.70% = 1.7170x (departure review table)
assert abs(1 + 71.70 / 100 - 1.7170) < 1e-9
# The other four departure returns: Hexin +79.98%, Positive Return -1.84%, Optimal +6.73%, Innovation -5.94%
vals = [71.70, 79.98, -1.84, 6.73, -5.94]
assert len(vals) == 5 and max(vals) == 79.98 and min(vals) == -5.94

# 7. Long-held top-10 counts at departure (2023 Q3 review): Shengbang 18 quarters, etc. - sanity ordering only
quarters = {"Shengbang": 18, "Maxscend": 17, "WillSemi": 17, "GigaDevice": 17, "NAURA": 16}
assert max(quarters.values()) == 18 and min(quarters.values()) == 16

print("21-cai-verify: all 7 assertion groups passed")
print(f" tenure {d}d/{d/365.25:.2f}y co-managed {d_co}d | 2019-2022 chain x={cum:.4f} | -40.04% needs +{need*100:.2f}% | scale 66.97->327.76 x={327.76/66.97:.2f}")
