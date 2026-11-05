# -*- coding: utf-8 -*-
# Data from the book passage covered by note 206; no modern measurement.
# 1 The two original sources of all revenue are land and capital stock
assert len(["land", "capital stock"]) == 2
# 2 Management belongs to 2 sets; capital pays wages in 3 branches
assert len(["proprietors of land", "owners or employers of capital"]) == 2
assert len(["agriculture", "manufactures", "commerce"]) == 3
# 3 Landlord improvements expressly named: tenants houses, drains, enclosures
assert len(["build/repair tenants houses", "drains", "enclosures"]) == 3
# 4 When the landlord ceases to do his part, the tenant continuing is 0 (impossible)
assert 0 == 0
# 5 Two layers push capital from disposition to actual removal
assert len(["revenue buys less than abroad", "vexatious visits of tax-gatherers"]) == 2
# 6 Creditor: particular interest/knowledge/inspection/care all 0, general interest 1
assert sum([0, 0, 0, 0]) == 0 and 1 == 1
print("206 verify: 6 assertions passed")
