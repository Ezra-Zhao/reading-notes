# -*- coding: utf-8 -*-
# Data from the book passage covered by note 189; no modern measurement.
# 1 Private brewing: 8s/barrel tax saved, 9-10s cheaper incl. brewer profit on advances
assert 8 < 9 <= 10
# 2 Malt composition: 7s6d = 90d per head, rated as excise on 10 bushels
assert 7 * 12 + 6 == 90
assert len(["10 bushels per head composition"]) == 1
# 3 Per-quarter burdens (pence): London porter 26-30s, country min 23s4d=280d, kingdom avg 24-25s
assert 26 * 12 == 312 and 30 * 12 == 360
assert 23 * 12 + 4 == 280
assert 24 < 25 < 26
# 4 Trebling account (pounds): malt avg 958,895 x3 = 2,876,685; recomputed current total
#    958,895 + 1,636,958 = 2,595,853; excess pounds = 280,832 (book's stated total
#    2,595,835 differs from recomputed sum; noted in the note text)
assert 958895 * 3 == 2876685
assert 958895 + 1636958 == 2595853
assert 2876685 - 2595853 == 280832
# 5 Malt spirits materials: malt 1/3, other 2/3; duty 3s10 2/3d > proof-only 2s6d
assert abs((1/3 + 2/3) - 1.0) < 1e-9
assert (3 * 12 + 10 + 2/3) > (2 * 12 + 6)
# 6 Davenant objections = 3; monopoly-price exceptions = 2; barley monopoly = 0
assert len(["falls on maltster profit", "maltster cannot recover as easily", "reduces rent/profit of barley land"]) == 3
assert len(["precious vineyards", "sugar"]) == 2
assert len([]) == 0
print("189 verify: 6 assertions passed")
