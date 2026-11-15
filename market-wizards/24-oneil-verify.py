#!/usr/bin/env python3
"""Verification for Market Wizards 24: William O'Neil. All arithmetic recomputed."""
from datetime import date

# 1. Schwager founding story: $5,000 -> $200,000 is 40.00x, a +3,900% gain
assert abs(200_000 / 5_000 - 40.00) < 1e-12
assert abs((200_000 - 5_000) / 5_000 * 100 - 3900.0) < 1e-9

# 2. Official-company variant: "20-fold increase in 26 months" does NOT reconcile
#    with $5,000 -> $200,000 (20x on $5,000 would be $100,000). Both registered, neither hidden.
assert 5_000 * 20 == 100_000
assert 200_000 / 100_000 == 2.0  # the two retellings differ by a factor of two

# 3. Ages: born 1933-03-25; founded firm in 1963 (after March birthday) = 30;
#    died 2023-05-28 = 90; launched Investor's Daily 1984 = 51; book 1988 = 55
assert 1963 - 1933 == 30
assert (date(2023, 5, 28) - date(1933, 3, 25)).days > 90 * 365  # past 90th birthday
assert 1984 - 1933 == 51
assert 1988 - 1933 == 55

# 4. O'Neil Fund: +116% in 1967 = 2.16x; later sold with $6M vs $49M peak = -87.76%
assert abs((1 + 1.16) - 2.16) < 1e-12
assert abs((49 - 6) / 49 * 100 - 87.7551) < 1e-3
assert abs(6 / 49 * 100 - 12.2449) < 1e-3

# 5. New USA Growth life-of-fund (Lipper, Mar 1997): +90.0% vs average growth fund +98.4%;
#    mechanical annualisation over an assumed 5 years: 13.70% vs 14.69%
ann_o = 1.900 ** 0.2 - 1
ann_a = 1.984 ** 0.2 - 1
assert abs(ann_o - 0.1370) < 1e-3
assert abs(ann_a - 0.1469) < 1e-3
assert abs(98.4 - 90.0 - 8.4) < 1e-9  # gap is 8.4 percentage points, not 8.4 percent

# 6. The 7-8% sell rule, account side: one 8% loss needs +8.70% to repair;
#    eight consecutive full-position 8% losses compound to -48.68%, needing +94.85%
assert abs(0.08 / 0.92 * 100 - 8.6957) < 1e-3
dd8 = 1 - 0.92 ** 8
assert abs(dd8 * 100 - 48.6781) < 1e-3
assert abs(dd8 / (1 - dd8) * 100 - 94.85) < 0.01

# 7. Position-size implication of an 8% stop: risk 2% of account -> position <= 25%;
#    risk 1% -> position <= 12.5% (my derivation, labelled as such in the note)
assert abs(2 / 8 * 100 - 25.0) < 1e-12
assert abs(1 / 8 * 100 - 12.5) < 1e-12

# 8. Timeline gaps: broker start 1958 -> founding 1963 = 5 years; Daily Graphs 1972 is
#    9 years after founding; Investor's Daily 1984 is 21 years after founding;
#    News Corp purchase 2021 is 37 years after the 1984 launch
assert 1963 - 1958 == 5
assert 1972 - 1963 == 9
assert 1984 - 1963 == 21
assert 2021 - 1984 == 37

print("24-oneil-verify: all 8 assertion groups passed")
print(f"schwager x=40.00 (+3900%) vs official 20x (factor-2 gap) | fund peak->sale -87.76% | New USA ann {ann_o*100:.2f}% vs avg {ann_a*100:.2f}% | 8x8% losses dd={dd8*100:.2f}% recovery=+{dd8/(1-dd8)*100:.2f}%")
