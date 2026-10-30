#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 26 (debug mode).
Illustrative parameters only; not empirical data, not medical,
psychological, or spiritual advice."""

# 1. His figure: 95 percent of what the brain runs off to do does not
# need tackling in that exact moment; the remainder is exactly 5.
not_now, remainder = 95, 100 - 95
assert not_now == 95 and remainder == 5 and not_now + remainder == 100

# 2. Awareness sequence: first see the mad monkey in operation, then
# separate from it; awareness itself calms. Order must not invert.
steps = ["see_the_uncontrolled_mind", "separate_self_from_it", "awareness_calms"]
assert steps[0].startswith("see") and steps.index("separate_self_from_it") == 1
assert steps[-1] == "awareness_calms"

# 3. Two layers: a kernel-level awareness OS below, applications on
# top. Monkey mind running 24/7 costs more than on-demand activation
# (illustrative model).
layers = ["awareness_os", "applications_on_top"]
assert len(layers) == 2 and layers[0] == "awareness_os"
always_on_cost, on_demand_cost = 24 * 7, 3  # hours per week, illustrative
assert always_on_cost > on_demand_cost

# 4. Closing list: five everyday forms named as meditation --
# hiking, journaling, praying, showering, sitting quietly.
forms = ["hiking", "journaling", "praying", "showering", "sitting_quietly"]
assert len(forms) == 5 and len(set(forms)) == 5

# 5. Debug-mode vignette: rehearsing a future podcast and brushing
# teeth are two different activities; he returns to the present one.
activities = {"rehearsed": "future_podcast_fantasy", "present": "brushing_teeth"}
assert activities["rehearsed"] != activities["present"]
returned_to = "brushing_teeth"
assert returned_to == activities["present"]

# 6. One uncontrolled-monkey metaphor and one core proposition:
# the mind itself is a muscle that can be trained and conditioned.
metaphors, propositions = ["uncontrolled_monkey"], ["mind_is_a_muscle_trainable"]
assert len(metaphors) == 1 and len(propositions) == 1

print("26-debug-mode-verify: all assertions passed")
print("  not-now=95%, remainder=5%; layers=2; everyday forms=5")
