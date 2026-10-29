#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 16 (happiness is learned).
Illustrative parameters only; not empirical data."""

# 1. Self-reported score moved from a 2-3/10 range (4 on best days)
# to 9/10: at least a doubling, and 3x from the low midpoint.
low_mid = 2.5
now = 9.0
assert now / low_mid > 3.0 and now > 4.0 * 2

# 2. Nothing-missing model (illustrative): contentment falls as the
# number of active "something is missing" desires rises; zero desires
# leaves the default state untouched.
def contentment(desires):
    return max(0, 100 - 12 * desires)
assert contentment(0) == 100
assert contentment(5) < contentment(2) < contentment(0)

# 3. Duality arithmetic: on a -5..+5 contrast scale, calling one side
# positive only has meaning relative to the opposite side below zero.
scale = list(range(-5, 6))
assert min(scale) < 0 < max(scale)
assert (5 + (-5)) == 0  # the pair is defined against each other

# 4. Mind-in-motion budget (illustrative): if rumination about past
# and future takes 80 of 100 attention units, 20 remain for the
# present; halving rumination triples the present share to 60.
def present_share(rumination):
    return 100 - rumination
assert present_share(80) == 20
assert present_share(40) == present_share(80) * 3

# 5. One-pound-weights analogy: practice capacity 1 unit against a
# 100-unit stressor covers only 1% - better than zero, never a shield.
assert 1 / 100 == 0.01 and 0.01 > 0.0

# 6. Slow baseline improvement (illustrative): 1% a week compounds
# to about 1.68x in a year, and stays under a 10/10 ceiling when capped.
baseline = 5.0
for _ in range(52):
    baseline = min(10.0, baseline * 1.01)
assert 8.0 < baseline < 8.5, baseline

print("16-happiness-learned-verify: all assertions passed")
print(f"  score 2.5 -> 9 is {now/low_mid:.1f}x; capped baseline after 52w = {baseline:.2f}")
