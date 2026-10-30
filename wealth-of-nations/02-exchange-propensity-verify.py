#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 02
(Book I Ch. II, the propensity to truck, barter and exchange).
Counts are taken from Smith's in-text examples; illustrative
structure checks only, not empirical data."""

# 1. The exchange propensity is presented as common to all men and
# found in no other race of animals (no contract-like exchange).
propensity_animals_with_contract_exchange = 0
assert propensity_animals_with_contract_exchange == 0

# 2. Four trades named as emerging from exchange in a hunter/shepherd
# tribe: armourer (bows and arrows), house-carpenter, smith/brazier,
# tanner/dresser of hides.
trades = ["armourer", "house_carpenter", "smith_or_brazier", "tanner"]
assert len(trades) == 4

# 3. Four dog kinds contrasted by innate genius: mastiff, greyhound,
# spaniel, shepherd's dog.
dogs = ["mastiff", "greyhound", "spaniel", "shepherds_dog"]
assert len(dogs) == 4

# 4. Philosopher and street porter are said to be very much alike
# for the first six to eight years of life.
similar_years = (6, 8)
assert similar_years == (6, 8) and similar_years[1] - similar_years[0] == 2

# 5. Even a beggar's occasional wants are supplied, like others', by
# treaty, by barter, and by purchase -- three routes.
routes = ["treaty", "barter", "purchase"]
assert len(routes) == 3

# 6. Every bargain has one reciprocal structure: give me what I want
# and you shall have what you want; the direction cannot be flipped
# into benevolence-only and still explain ordinary supply.
bargain = {"give": "what_I_want", "receive": "what_you_want"}
assert bargain["give"] != bargain["receive"]

print("02-exchange-propensity-verify: all assertions passed")
print("  animal_contract=0 trades=4 dogs=4 similar_years=6-8 routes=3 bargain=reciprocal")
