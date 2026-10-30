#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 29 (free yourself).
Illustrative parameters only; not empirical data, not psychological
or medical advice."""

# 1. Two definitions of freedom: outward "freedom to" and inward
# "freedom from"; the from-list in the definition passage names
# four items.
definitions = ["freedom_to", "freedom_from"]
assert len(definitions) == 2
freedom_from = ["reaction", "anger", "sadness", "being_forced"]
assert len(freedom_from) == 4

# 2. Holding back stretches leaving from minutes to years; the
# year scale is strictly larger than the minute scale.
minutes, years_in_minutes = 10, 2 * 365 * 24 * 60
assert years_in_minutes > minutes * 1000

# 3. Expectations and agreements are two distinct classes, and
# responsibility attaches only to the agreement class.
classes = {"expectation": "their_problem", "agreement": "your_problem"}
assert len(classes) == 2
assert classes["agreement"] == "your_problem"
assert classes["expectation"] != "your_problem"

# 4. Time-waste test: a stretch of time counts as wasted only when
# all three are missing - doing what you want, earning, learning.
def is_waste(want, earning, learning):
    return not (want or earning or learning)

assert is_waste(False, False, False) is True
assert is_waste(True, False, False) is False
assert is_waste(False, True, False) is False
assert is_waste(False, False, True) is False

# 5. Street scene: one thousand people, each talking to themselves;
# uncontrolled thinking running 24/7 costs more than on-demand use
# in the illustrative model.
crowd = 1000
assert crowd == 1000
always_on_cost, on_demand_cost = 24 * 7, 2 * 7
assert always_on_cost > on_demand_cost

# 6. The modern struggle: five named weapons on one side (junk food,
# clickbait news, porn, endless games, addictive drugs) against
# three named practices on the other (fasting, meditating,
# exercising).
weapons = ["junk_food", "clickbait_news", "porn", "endless_games", "addictive_drugs"]
practices = ["fasting", "meditating", "exercising"]
assert len(weapons) == 5 and len(practices) == 3

print("29-free-yourself-verify: all assertions passed")
print("  freedom_from=4; waste needs all 3 missing; weapons=5 vs practices=3")
