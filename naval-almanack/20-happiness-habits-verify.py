#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 20 (happiness habits).
Illustrative parameters only; not empirical data."""

# 1. Positive-reframe speed: a few seconds at first (~3s) down to
# sub-second (~0.5s) after practice is a 6x speedup.
before, after = 3.0, 0.5
assert before / after == 6.0 and after < 1.0

# 2. Desire check: of 20 desires caught in a week, most fail the
# "important enough to be unhappy over" test; here 18 of 20 fail,
# i.e. 90 percent were not worth unhappiness.
desires, important = 20, 2
assert (desires - important) / desires == 0.9

# 3. Obligation metric: in a 16-hour waking day, 12 hours of
# obligation is 75 percent; cutting it to 8 hours is 50 percent,
# strictly lower.
waking = 16
assert 12 / waking == 0.75 and 8 / waking == 0.5 and 8 / waking < 12 / waking

# 4. Changing-habits sequence in the source has nine steps.
steps = ["pick one", "cultivate desire", "visualize", "plan path",
         "needs-triggers-substitutes", "tell friends", "track",
         "self-discipline bridge", "bake in self-image"]
assert len(steps) == 9

# 5. Drug-free serotonin list in the source names four inputs.
serotonin = ["sunlight", "exercise", "positive thinking", "tryptophan"]
assert len(serotonin) == 4

# 6. Hedonic adaptation contrast (illustrative decay): if man-made
# pleasures halve each period and natural ones halve every three
# periods, after three periods man-made is at 1/8 and natural at 1/2.
man_made = 0.5 ** 3
natural = 0.5 ** 1
assert man_made == 0.125 and natural == 0.5 and man_made < natural

print("20-happiness-habits-verify: all assertions passed")
print(f"  reframe {before:.1f}s -> {after:.1f}s (6x); desires not worth it 90%")
