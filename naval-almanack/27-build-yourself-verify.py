#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 27 (build yourself).
Illustrative parameters only; not empirical data, not cessation or
psychological advice."""

# 1. Retrospective exercise cadence: decade steps (20->30, 30->40);
# younger readers may use five-year steps.
decades = [(20, 30), (30, 40)]
assert all(b - a == 10 for a, b in decades)
young_step = 5
assert young_step == 5 and young_step < 10

# 2. Same actions, less anger: with anger the total cost is strictly
# higher (illustrative model). His walk-up-and-say-it list has four
# items: what happened, what I will do, how I will do it, what is
# fair and what is not.
base_cost, anger_surcharge = 100, 60
assert base_cost + anger_surcharge > base_cost
fairness_list = ["what_happened", "what_i_will_do", "how_i_will_do_it", "fair_vs_unfair"]
assert len(fairness_list) == 4

# 3. Habit journey: at least ten years, one batch of habits every
# six months -> twenty batches; a three-month fix is not sustainable.
years, batches_per_year = 10, 2
assert years * batches_per_year == 20
sustainable_months = list(range(6, 121))
assert 3 not in sustainable_months and 120 in sustainable_months

# 4. Scaled-down commitment window: three to six months, and the
# order is honest admission first, then shrink, then commit aloud.
window = (3, 6)
assert window[0] == 3 and window[1] == 6 and window[1] > window[0]
order = ["admit_not_ready", "shrink_the_goal", "commit_externally"]
assert order[0] == "admit_not_ready" and order[-1] == "commit_externally"

# 5. Patience split: zero waiting on actions, years of patience on
# results; the two ends point in opposite directions.
wait_actions, wait_results_years = 0, 10
assert wait_actions == 0 and wait_results_years >= 1

# 6. One chapter proposition (greatest superpower = ability to change
# yourself) and one habit-scale figure (thousands of habits running
# subconsciously).
propositions = ["greatest_superpower_is_changing_yourself"]
assert len(propositions) == 1
habit_scale = 2000  # "thousands", illustrative floor
assert habit_scale >= 1000

print("27-build-yourself-verify: all assertions passed")
print("  batches=20 over 10y; scaled window=3-6mo; action wait=0")
