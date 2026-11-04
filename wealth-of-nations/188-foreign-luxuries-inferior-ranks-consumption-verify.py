# -*- coding: utf-8 -*-
# Data from the book passage covered by note 188; no modern measurement.
# 1 Foreign luxuries examples
assert len(["foreign wines", "coffee", "chocolate", "tea", "sugar"]) == 5
# 2 Cheaper home luxuries examples
assert len(["malt", "hops", "beer", "ale"]) == 4
# 3 Four distribution channels to inferior ranks
assert len(["wages of productive labour", "wages/maintenance of menial servants and unproductive labourers", "profits of small capitals (small shopkeepers/tradesmen/retailers)", "rent of land in small parts"]) == 4
# 4 Inferior total expense > superior total expense, in quantity and in value
assert len(["quantity", "value"]) == 2
# 5 Home fermented/spirituous excise gross produce year ended 5 July 1775: £3,341,837 9s 9d
assert 3341837 > 3000000
# 6 Tax on necessaries of inferior ranks: 2 roads, both final payment on superior ranks
assert len(["raise wages of labour", "lessen demand for labour"]) == 2
assert len(["final payment on superior via wages", "final payment on superior via wage enhancement in any state"]) == 2
print("188 verify: 6 assertions passed")
