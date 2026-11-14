#!/usr/bin/env python3
"""Verification for Market Wizards 18: Michael Marcus. All arithmetic recomputed."""
from datetime import date

# 1. Plywood 1972: $7,000 -> $12,000
assert abs(12000/7000 - 1.7142857) < 1e-6
assert abs((12000-7000)/7000*100 - 71.4286) < 1e-3

# 2. 1973: $24,000 -> $64,000
assert abs(64000/24000 - 2.6666667) < 1e-6
assert abs((64000-24000)/24000*100 - 166.6667) < 1e-3

# 3. Commodities Corp account: $30,000 -> ~$80,000,000 nominal multiple
mult = 80_000_000/30_000
assert abs(mult - 2666.6667) < 1e-3
# book intro rounds to 2,500-fold; nominal multiple is within 6.7% of that rounding
assert abs(mult/2500 - 1) < 0.07
# mechanical 10y CAGR (illustrative only; flows make it not a true return)
cagr = mult**0.1 - 1
assert 1.19 < cagr < 1.21, cagr

# 4. Gold anecdote arithmetic: 200,000 oz x $10 move = $2,000,000
assert 200_000 * 10 == 2_000_000

# 5. Currency anecdote: 600m DEM ~ $300m implies ~0.50 USD per DEM (2 DEM per USD)
assert abs(300_000_000/600_000_000 - 0.5) < 1e-9

# 6. Age at death: 1947-08-02 -> 2023-03-25 = 75
age = 2023-1947 - ((3,25) < (8,2))
assert age == 75

# 7. Idea-risk rule illustration: three correlated positions at 2% each = 6% > 5% cap
assert 3*2 > 5

print("18-marcus-verify: all 7 assertions passed")
print(f"plywood x={12000/7000:.4f} +{(12000-7000)/7000*100:.2f}% | 1973 x={64000/24000:.4f} | CC nominal x={mult:.1f} mech CAGR={cagr*100:.1f}% | gold gain=${200_000*10:,}")
