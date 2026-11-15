#!/usr/bin/env python3
"""Verification for Market Wizards 22: Jim Rogers. All arithmetic recomputed."""
from datetime import date

# 1. Quantum partnership claim: +4,200% -> 43.00x; S&P +47% -> 1.47x; ratio of end values
assert abs((1 + 42.00) - 43.00) < 1e-12
assert abs((1 + 0.47) - 1.47) < 1e-12
assert abs(43.00 / 1.47 - 29.2517) < 1e-3

# 2. Illustrative annualised over exactly 10 years (mechanical only, not an audited curve)
ann_q = 43.00 ** 0.1 - 1
ann_s = 1.47 ** 0.1 - 1
assert abs(ann_q - 0.4566) < 1e-3
assert abs(ann_s - 0.0393) < 1e-3

# 3. Retirement age: born 1942-10-19; leaving in 1980 before that birthday = 37
assert 1980 - 1942 - 1 == 37
assert 1973 - 1970 == 3  # joined Arnhold in 1970, co-founded Quantum three years later
assert 1980 - 1973 == 7  # seven calendar years at Quantum itself, partnership counted from 1970

# 4. Millennium Adventure: 1999-01-01 to 2002-01-05
delta = (date(2002, 1, 5) - date(1999, 1, 1)).days
assert delta == 1100
assert delta + 1 == 1101  # inclusive day count matches the 1,101-day source wording

# 5. Distance conversion: 245,000 km in miles
miles = 245_000 / 1.609344
assert abs(miles - 152_235.94) < 0.1

# 6. RICI sub-index starting weights sum to 100%
assert abs(34.90 + 44.00 + 21.10 - 100.00) < 1e-9

# 7. Timeline gaps
assert 1964 - 1942 == 22  # Yale graduation year minus birth year (graduated at 21, before Oct birthday)
assert 1966 - 1964 == 2   # Oxford second BA two years after Yale
assert 1998 - 1980 == 18  # first RICI-tracking fund 18 years after leaving Quantum
assert 2007 - 1980 == 27  # Singapore move 27 years after retirement

print("22-rogers-verify: all 7 assertion groups passed")
print(f"quantum x=43.00 vs S&P x=1.47 ratio={43/1.47:.2f} | ann(10y) quantum={ann_q*100:.1f}% S&P={ann_s*100:.1f}% | millennium days diff={delta} inclusive={delta+1} | 245000 km={miles:,.0f} miles")
