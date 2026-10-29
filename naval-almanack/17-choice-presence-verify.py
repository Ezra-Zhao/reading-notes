#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 17 (choice, presence, peace).
Illustrative parameters only; not empirical data."""
import math

# 1. Present share of a 16-hour waking day (960 minutes): a small 5%
# is only 48 minutes; raising it to 50% is 480 minutes, a 10x gain.
waking = 16 * 60
assert waking * 0.05 == 48 and waking * 0.50 == 480
assert (waking * 0.50) / (waking * 0.05) == 10

# 2. Space-between-thoughts model (illustrative): if a thought cycle
# is thought-time plus gap-time, the gap share rises as gaps lengthen.
def gap_share(thought_s, gap_s):
    return gap_s / (thought_s + gap_s)
assert gap_share(3, 1) == 0.25
assert gap_share(3, 3) > gap_share(3, 1)

# 3. Nexting chain (illustrative): each "next" adds one unit of
# background anxiety load; a chain of 10 loads 10x a single next.
def anxiety_load(nexts, per=1.0):
    return nexts * per
assert anxiety_load(10) == anxiety_load(1) * 10
assert anxiety_load(0) == 0

# 4. Thought-or-peace budget: attention is finite, so rumination and
# peace share 100 units; halving rumination frees exactly that much.
def peace_space(rumination):
    return 100 - rumination
assert peace_space(70) == 30
assert peace_space(35) - peace_space(70) == 35

# 5. "Should" elimination (illustrative count): removing should-driven
# items from a day leaves only want-driven ones, count strictly falls.
day = ["should"] * 6 + ["want"] * 4
cleaned = [x for x in day if x != "should"]
assert len(cleaned) == 4 and len(cleaned) < len(day)

# 6. Doing-nothing test: 30 silent minutes with a thought every
# 10 seconds produces 180 interruptions - noticing is the first step.
interruptions = 30 * 60 // 10
assert interruptions == 180

print("17-choice-presence-verify: all assertions passed")
print(f"  present 5% of waking day = {waking*0.05:.0f} min; gap share 3s+3s = {gap_share(3,3):.2f}")
