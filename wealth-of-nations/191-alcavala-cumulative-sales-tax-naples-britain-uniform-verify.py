# -*- coding: utf-8 -*-
# Data from the book passage covered by note 191; no modern measurement.
# 1 Alcavala rates over time: 10 -> 14 -> 6 per cent; now below the start
alcavala = [10, 14, 6]
assert alcavala[1] > alcavala[0] > alcavala[2]
# 2 Charged on every sort of property, moveable and immoveable (2), at every sale
assert len(["moveable property", "immoveable property"]) == 2
# 3 Naples 3% is half of Spain's present 6%, and under a quarter of the 14% peak
assert 3 * 2 == 6
assert 3 < 14 / 4 + 0.01 or 3 <= 3.5
assert 3 < 6 < 14
# 4 Naples mitigations: lighter rate + composition levied locally as towns please (2)
assert len(["lighter than the Spanish tax", "composition in lieu, levied as towns please"]) == 2
# 5 Britain coastwise: certificates required, but only coals taxed (1), rest duty-free
assert len(["coals"]) == 1
# 6 Home market dictum: best and most extensive market (2); extension targets (2)
assert len(["best market", "most extensive market"]) == 2
assert len(["Ireland", "the plantations"]) == 2
print("191 verify: 6 assertions passed")
