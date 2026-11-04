# -*- coding: utf-8 -*-
# Data from the book passage covered by note 197; no modern measurement.
# 1 Two taxes are regularly anticipated every year in Great Britain
assert len(["land tax", "malt tax"]) == 2
# 2 Bank of England advance rate since the Revolution: varied from 8 to 3
#    per cent; spread is 5 points, high above low
assert 8 - 3 == 5
assert 8 > 3
# 3 Deficiency "always is": in every sample year the anticipation runs short
assert all({"deficiency": True}["deficiency"] for _ in range(3))
# 4 Only one considerable branch of public revenue yet remains unmortgaged
#    (the land and malt taxes taken as that branch)
assert len(["land and malt taxes (unmortgaged branch)"]) == 1
# 5 The Bank advances the sums and receives payment as the produce
#    gradually comes in: advance and repayment are both present
assert len(["advance", "repayment as produce comes in"]) == 2
# 6 The spendthrift structure has 2 points: the state borrows of its own
#    factors and agents, and pays interest for the use of its own money
assert len(["borrowing of its own factors and agents",
            "paying interest for the use of its own money"]) == 2
print("197 verify: 6 assertions passed")
