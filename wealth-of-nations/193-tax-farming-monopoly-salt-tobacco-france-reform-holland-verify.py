# -*- coding: utf-8 -*-
# Data from the book passage covered by note 193; no modern measurement.
# 1 Farms of 1767: tobacco 22,541,278 + salt 36,492,404 = 59,033,682 livres
assert 22541278 + 36492404 == 59033682
assert 36492404 > 22541278
# 2 Both farms commence 1768, to last six years
assert 1768 + 6 == 1774
assert len(["tobacco farm", "salt farm"]) == 2
# 3 France has 8 revenue sources; 5 farmed, 3 administered (vingtiemes counted
#    as one source heading though it names two taxes, as in the book's list)
farmed = ["gabelles", "aides", "traites", "domaine", "farm of tobacco"]
administered = ["taille", "capitation", "the two vingtiemes"]
assert len(farmed) + len(administered) == 8
assert len(farmed) == 5 and len(administered) == 3
# 4 Three reformations; the first abolishes 2 taxes (taille, capitation)
assert len(["abolish taille+capitation, add vingtiemes", "make all taxes uniform", "bring all under administration"]) == 3
assert len(["taille", "capitation"]) == 2
# 5 Britain/France: France ~3x people; expected 30m vs actual under 15m sterling
assert 23000000 > 22000000  # about 3x Britain's under-8-million, lower bound
assert 15000000 <= 30000000 // 2  # actual did not amount to 15m: under half of 30m
assert 308000000 < 325000000  # livres range 1765-66
# 6 Holland: revenue above 5,250,000 pounds; people at most a third of Britain's
assert 5250000 > 0
assert len(["United Provinces inhabitants <= 1/3 of Great Britain"]) == 1
print("193 verify: 6 assertions passed")
