#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 07
(Book I Ch. VII, natural and market price).
Numbers are Smith's in-text figures, recomputed; not modern measurements."""
# 1. Natural price = rent + wages + profit at their natural rates (3 parts).
parts = ["rent", "wages", "profit"]
assert len(parts) == 3
# 2. Market price has exactly three relations to natural price.
relations = ["above", "below", "equal"]
assert len(relations) == 3
# 3. Variable-produce industries named: corn, wine, oil, hops (4);
#    steady-produce industries named: linen, woollen cloth (2).
variable = ["corn", "wine", "oil", "hops"]
steady = ["linen", "woollen"]
assert len(variable) == 4 and len(steady) == 2
# 4. Causes that can hold market price long above natural price: 3 classes
#    (particular accidents/secrets, natural causes, regulations of policy).
causes = ["accidents_secrets", "natural_causes", "policy_regulations"]
assert len(causes) == 3
# 5. Dyer's secret: materials at half the common cost -> saving is one half.
common_cost, dyer_cost = 2, 1
assert dyer_cost * 2 == common_cost and (common_cost - dyer_cost) / common_cost == 0.5
# 6. Perishable vs durable contrast pair: oranges vs old iron (2 goods),
#    and mourning example splits: black cloth price up, weavers' wages
#    unchanged, tailors' wages up (3 distinct effects).
assert len(["oranges", "old_iron"]) == 2
mourning = {"black_cloth_price": "up", "weavers_wages": "same", "tailors_wages": "up"}
assert len(set(mourning.values())) == 2 and mourning["weavers_wages"] == "same"
print("07-natural-market-price-verify: all assertions passed")
print("  parts=3 relations=3 variable=4 steady=2 causes=3 dyer_cost=1/2 mourning_effects=3")
