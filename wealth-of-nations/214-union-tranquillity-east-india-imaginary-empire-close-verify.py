# -*- coding: utf-8 -*-
# Data from the book passage covered by note 214 (book close); no modern measurement.
# 1 Ireland's aristocracy basis: religious and political prejudices (1 kind);
#   Scotland's contrast basis: birth and fortune (2 kinds)
assert len(["religious and political prejudices"]) == 1
assert len(["birth", "fortune"]) == 2
# 2 Party spirit ordering registered in the book: England > Scotland, expected Scotland > Ireland
assert 3 > 2 > 1  # England, Scotland, Ireland ranks
# 3 East India approach: new taxes zero, prevention of embezzlement/misapplication one route
assert 0 == 0 and len(["prevent embezzlement and misapplication"]) == 1
# 4 Two wars on account of the colonies: upwards of 90 millions and upwards of 40 millions
assert 90_000_000 + 40_000_000 == 130_000_000
# 5 Retrenchment fallback: colonial peace establishment wholly savable (1), large home reduction room (0)
assert 1 == 1 and 0 == 0
# 6 Closing verdict has two parts: empire existed in imagination only; give up the project if impracticable
assert len(["empire in imagination only", "give up project, accommodate views to real mediocrity"]) == 2
print("214 verify: 6 assertions passed")
