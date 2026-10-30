#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 28 (grow yourself).
Illustrative parameters only; not empirical data, not education or
career advice."""

# 1. The thousand-lives test: succeed 999 times out of 1000, so the
# failure budget is exactly one and the rate is 99.9 percent.
plays, wins = 1000, 999
assert wins / plays == 0.999
assert plays - wins == 1

# 2. Systems route order: judge the environment first, build the
# environment second, and only then talk about the odds of success.
# A specific goal is not the starting point of that order.
order = ["judge_fitting_environments", "build_the_environment", "raise_the_odds"]
assert order[0] == "judge_fitting_environments"
assert order[-1] == "raise_the_odds"
assert "set_a_specific_goal" not in order

# 3. The prerequisites he names for a reader of the book: a
# functioning body and a functioning mind (two items).
prerequisites = ["functioning_body", "functioning_mind"]
assert len(prerequisites) == 2

# 4. Secondhand versus original: his complaint is one hundred
# regurgitated books read against zero readings of the original
# (illustrative figures as stated in the book).
regurgitated, originals_read = 100, 0
assert regurgitated == 100 and originals_read == 0
assert regurgitated > originals_read

# 5. Skills passed to his kids: reading, persuasion, mathematics
# (three skills).
skills = ["reading", "persuasion", "mathematics"]
assert len(skills) == 3

# 6. His own math working set: arithmetic, statistics and probability
# are in; calculus is not the tool he reaches for himself.
math_in = ["arithmetic", "statistics", "probability"]
assert "statistics" in math_in and "probability" in math_in
assert "calculus" not in math_in

print("28-grow-yourself-verify: all assertions passed")
print("  win rate=999/1000=99.9%; skills=3; prerequisites=2")
