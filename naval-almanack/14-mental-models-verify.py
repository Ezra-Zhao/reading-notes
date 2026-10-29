#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 14 (mental models).
Illustrative parameters only; not empirical data, not investment advice."""
import math

# 1. Compound interest examples from the book: 10% on $1
v = 1.0
seq = []
for _ in range(3):
    v *= 1.10
    seq.append(round(v, 3))
assert seq == [1.1, 1.21, 1.331], seq

# 2. 30% compounded for 30 years ends in thousands, not 10-20x
final = 1.30 ** 30
assert 2000 < final < 3000, final
assert final > 100 * (1 + 0.30 * 30) / 10  # far above simple-interest intuition

# 3. 100 users growing 20% per month reaches millions in about 51 months
months = math.log(1_000_000 / 100) / math.log(1.20)
assert 50 < months < 52, months
assert 100 * 1.20 ** 51 >= 1_000_000

# 4. Principal-agent: tying pay to value created raises the share of
# effort aimed at the principal's outcome (illustrative linear model).
def principal_value(tie_fraction, base_care=0.3):
    return base_care + (1 - base_care) * tie_fraction
assert principal_value(0.0) < principal_value(0.5) < principal_value(1.0)
assert abs(principal_value(1.0) - 1.0) < 1e-9

# 5. Run uphill: a path whose payoff compounds at 10% for 20 years
# beats a one-off short-term gain with no compounding.
pain_path = 100 * (1.10 ** 20)   # effort-equivalent payoff, grows
easy_path = 110.0                # one-off short gain, no compounding
assert pain_path > easy_path * 5

# 6. Options explosion: modern connected pool vs a 150-person tribe
assert 7_000_000_000 / 150 > 40_000_000

print("14-mental-models-verify: all assertions passed")
print(f"  30% x 30y multiple = {final:.1f}x; months 100 users -> 1M at 20%/mo = {months:.1f}")
