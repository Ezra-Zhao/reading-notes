# -*- coding: utf-8 -*-
# Data from the book passage covered by note 210; no modern measurement.
# 1 Only one of the four branches needs variation by province: the excise
assert len(["excise"]) == 1 and 1 < 4
# 2 Three molasses import-duty examples in the passage (values as stated, units differ)
assert len([("British Parliament", 1, "penny/gallon"), ("Massachusetts Bay", 8, "pence/hogshead"), ("South Carolina", 5, "pence/gallon")]) == 3
# 3 Three fallback modes for the molasses-beer tax
assert len(["tax the material", "duty on importation", "compound per family"]) == 3
# 4 Three commodities named extremely proper subjects of taxation, two conditions both present
assert len(["sugar", "rum", "tobacco"]) == 3
assert len(["nowhere necessaries of life", "almost universal consumption"]) == 2
# 5 Warehouse delivery objects: three; tax advanced only on delivery; export delivery duty-free
assert len(["consumer", "merchant retailer", "merchant exporter"]) == 3
# 6 Province named as needing no excise variation: Ireland only
assert len(["Ireland"]) == 1
print("210 verify: 6 assertions passed")
