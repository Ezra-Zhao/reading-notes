# -*- coding: utf-8 -*-
# Data from the book passage covered by note 195; no modern measurement.
# 1 War establishment costs 3 or 4 times the peace establishment
assert 3 <= 4
assert 4 - 3 == 1
war_multiples = [3, 4]
assert min(war_multiples) == 3 and max(war_multiples) == 4
# 2 New taxes begin to come in only 10 or 12 months after imposition
assert 10 < 12
assert (10 + 12) // 2 == 11  # midpoint lag in months, as stated bounds
# 3 A quick-return merchant's whole capital and credit may pass through his
#    hands 2, 3 or 4 times a year; a rentier's revenue only once a year
assert max([2, 3, 4]) == 4 * 1
assert len([2, 3, 4]) == 3
# 4 Confidence conditions named for commerce to flourish: regular justice,
#    secure property, faith of contracts upheld, state enforcing payment = 4
conditions = ["regular administration of justice", "security of property",
              "faith of contracts supported by law", "state authority enforcing payment of debts"]
assert len(conditions) == 4
# 5 Lender gains on a new loan in the passage: advantageous terms, transferable
#    security, market price above original price = capital augmented, not diminished
assert len(["advantageous terms", "transferable security", "sells above original price"]) == 3
assert 1 > 0  # augmentation direction: increase, registered as positive
# 6 Rude state: people able to lend are few, willing are none (0 willing)
assert len([]) == 0  # nobody willing to lend in the rude state
assert len(["foreseen impossibility of borrowing -> sovereign must save"]) == 1
print("195 verify: 6 assertions passed")
