#!/usr/bin/env python3
"""Verification for Market Wizards 20: Marty Schwartz. All arithmetic recomputed."""
from datetime import date

# 1. Futures account (interview self-report): $40,000 -> ~$20,000,000
mult = 20_000_000 / 40_000
assert mult == 500.0
assert abs((20_000_000 - 40_000) / 40_000 * 100 - 49900.0) < 1e-9

# 2. Four-month contests: average 210% nonannualized -> end value 3.10x stake
end_mult = 1 + 2.10
assert abs(end_mult - 3.10) < 1e-12
# on Schwager's typical $400,000 starting stake: profit $840,000, end $1,240,000
assert 400_000 * 2.10 == 840_000
assert 400_000 * end_mult == 1_240_000

# 3. One-year contest: 781% -> end value 8.81x; per $100,000 illustration: profit $781,000
assert abs(1 + 7.81 - 8.81) < 1e-12
assert 100_000 * 7.81 == 781_000

# 4. First two independent years (Publishers Weekly on Pit Bull): $600,000 then $1,200,000
assert 1_200_000 / 600_000 == 2.0
assert 600_000 + 1_200_000 == 1_800_000

# 5. Month-end drawdown cap 3%: on $400,000 stake = $12,000; on $1,000,000 = $30,000
assert 400_000 * 0.03 == 12_000
assert 1_000_000 * 0.03 == 30_000

# 6. Post-loss size cut: to 1/5 = 20% of normal, to 1/10 = 10% of normal
assert abs(1/5 * 100 - 20.0) < 1e-12
assert abs(1/10 * 100 - 10.0) < 1e-12

# 7. Timeline year gaps (birth year 1945; exact day single-source, so year arithmetic only)
assert 1967 - 1945 == 22   # Amherst graduation year minus birth year
assert 1970 - 1967 == 3    # Columbia MBA three years after Amherst
assert 1973 - 1968 == 5    # Marine Corps Reserve span in years
assert 1979 - 1970 == 9    # full-time trading nine years after the MBA (~ the losing decade)
assert 1984 - 1979 == 5    # championship year five years after going full-time
assert 1998 - 1989 == 9    # Pit Bull nine years after Market Wizards

print("20-schwartz-verify: all 7 assertion groups passed")
print(f"account x={mult:.0f} (+{(20_000_000-40_000)/40_000*100:,.0f}%) | 4m contest end x={end_mult:.2f} profit on 400k=${400_000*2.10:,.0f} | 1y contest end x={1+7.81:.2f} | first two years total=${600_000+1_200_000:,}")
