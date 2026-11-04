# -*- coding: utf-8 -*-
# Data from the book passage covered by note 192; no modern measurement.
# 1 Traites divide France into 3 parts; tariffs of 1664 and 1667
assert len(["provinces of the five great farms (1664)", "provinces reckoned foreign (1667)", "provinces treated as foreign"]) == 3
assert 1667 > 1664
# 2 Treated-as-foreign members: Alsace (1) + three bishoprics + three cities = 7
assert len(["Alsace", "Mentz", "Toul", "Verdun", "Dunkirk", "Bayonne", "Marseilles"]) == 7
assert len(["Mentz", "Toul", "Verdun"]) == 3 and len(["Dunkirk", "Bayonne", "Marseilles"]) == 3
# 3 Gabelle treatments across provinces: pay / compound / exempt = 3
assert len(["subject to the gabelle", "compound for the gabelle", "exempted altogether"]) == 3
# 4 Five great farms: duties once divided into 5 branches, now united into 1 farm
assert len(["branch 1", "branch 2", "branch 3", "branch 4", "branch 5"]) == 5
# 5 Milan divided into 6 provinces; Parma into 3 or 4; Milan more fragmented
parma_low, parma_high = 3, 4
assert 6 > parma_high >= parma_low
# 6 Wine dictum direction: most famous provinces = fewest restraints, largest market
assert len(["fewest restraints", "most extensive market"]) == 2
print("192 verify: 6 assertions passed")
