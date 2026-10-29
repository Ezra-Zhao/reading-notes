#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 19 (envy, habits).
Illustrative parameters only; not empirical data."""

# 1. Envy is pure loss (illustrative): the envier drops, the envied
# person is unchanged, so the combined total strictly falls.
before = {"envier": 50, "envied": 80}
after = {"envier": 50 - 3, "envied": 80}
assert after["envied"] == before["envied"]
assert sum(after.values()) < sum(before.values())

# 2. Wholesale swap test: picking 1 of 3 aspects is a partial swap,
# which is not equal to the only valid swap (the whole person).
aspects = ["body", "money", "personality"]
partial = aspects[:1]
assert partial != aspects and len(partial) == 1

# 3. Should-elimination (illustrative count): of 10 items, 6 are
# should-driven; removing them leaves 4 and strictly fewer total.
day = ["should"] * 6 + ["want"] * 4
cleaned = [x for x in day if x != "should"]
assert len(cleaned) == 4 and len(cleaned) < len(day)

# 4. Five-companions average: scores 9,8,8,9,4 average 7.6;
# replacing the 4 with a 9 lifts the average to 8.6, exactly +1.0.
group = [9, 8, 8, 9, 4]
avg = sum(group) / len(group)
assert avg == 7.6
group2 = [9, 8, 8, 9, 9]
avg2 = sum(group2) / len(group2)
assert avg2 == 8.6 and avg2 - avg == 1.0

# 5. Habit compounding (illustrative): improving 1% a day for
# 100 days multiplies the starting level by about 2.70.
level = 1.01 ** 100
assert abs(level - 2.7048) < 0.001 and level > 2

# 6. Inner vs outer scorecard can fully diverge: outer can be at
# maximum while inner is low, so the gap is positive and large.
outer, inner = 100, 20
assert outer - inner == 80 and outer - inner > 0

print("19-envy-habits-verify: all assertions passed")
print(f"  five-companion avg {avg:.1f} -> {avg2:.1f}; 1.01^100 = {level:.4f}")
