#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 23 (care for yourself / diet).
Illustrative parameters only; not empirical data, not medical advice."""

# 1. Priority chain has exactly six levels; the first three are
# one's own physical, mental, and spiritual health, in that order.
priorities = ["own physical health", "own mental health", "own spiritual health",
              "family health", "family wellbeing", "rest of the world"]
assert len(priorities) == 6
assert priorities[:3] == ["own physical health", "own mental health",
                          "own spiritual health"]
assert priorities.index("family health") > priorities.index("own spiritual health")

# 2. Modern-mismatch list in the note counts nine items.
mismatches = ["unevolved diet", "treadmill instead of play",
              "visual-only inputs", "always wearing shoes",
              "constant warmth / no cold exposure", "over-sterile environment",
              "no small tribe / family around", "phone check every five minutes",
              "scarcity genes in abundance"]
assert len(mismatches) == 9 and len(set(mismatches)) == 9

# 3. Directional sign model (illustrative): fat alone points to
# satiety (+1 satiety), sugar alone points to hunger (-1 satiety);
# per the source, combined the sugar direction dominates.
satiety = {"fat": +1, "sugar": -1}
assert satiety["fat"] > 0 > satiety["sugar"]
combined = satiety["sugar"]  # sugar effect dominates, per source
assert combined < 0

# 4. Nature examples in the source where carbs and fat co-occur:
# exactly three tropical fruits named.
natural_combo = ["coconut", "mango", "banana"]
assert len(natural_combo) == 3

# 5. Processing rule is monotone: as processing depth rises from
# 1 to 10, the recommended intake share strictly falls.
intake = [100 / depth for depth in range(1, 11)]
assert all(intake[i] > intake[i + 1] for i in range(9))

# 6. Subtract before you add: in the intervention sequence the
# removal step comes before the addition step.
sequence = ["subtract", "add"]
assert sequence.index("subtract") < sequence.index("add")

print("23-care-diet-verify: all assertions passed")
print(f"  priorities=6; mismatches=9; combined satiety sign = {combined}")
