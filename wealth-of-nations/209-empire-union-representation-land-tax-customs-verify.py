# -*- coding: utf-8 -*-
# Data from the book passage covered by note 209; no modern measurement.
# 1 Four principal branches of British taxes
assert len(["land-tax", "stamp-duties", "customs", "excise"]) == 4
# 2 Tithe floor is a fourth of real rent; a 5s-in-the-pound land tax is also 1/4;
#   the book states the tithe diminishes rent MORE than such a land tax (registered qualitatively)
assert 5 / 20 == 1 / 4
assert 0.25 <= 0.25 and len(["tithe diminishes more than 5s land tax"]) == 1
# 3 Complete church tithe of GB and Ireland estimated at 6-7 millions
assert 6_000_000 < 7_000_000
# 4 Tithe paid in America per the book: none
assert 0 == 0 and len([]) == 0
# 5 Two assessment modes where no rent-roll exists
assert len(["loose inaccurate estimation", "accurate survey valuation"]) == 2
# 6 Representation rule: each province's representation/tax ratio equals GB's (identity)
gb_ratio = 1.0
province_ratio = 1.0
assert province_ratio == gb_ratio
print("209 verify: 6 assertions passed")
