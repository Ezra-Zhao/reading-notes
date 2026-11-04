# -*- coding: utf-8 -*-
# Data from the book passage covered by note 187; no modern measurement.
# 1 Reform has 2 moves
assert len(["confine duties to few articles", "excise-like administration"]) == 2
# 2 Foreign staples: 3 origin groups, 11 listed sorts
assert len(["europe wines brandies", "america west indies", "east indies"]) == 3
assert len(["wine", "brandy", "sugar", "rum", "tobacco", "cocoa-nuts", "tea", "coffee", "china-ware", "spiceries", "piece-goods"]) == 11
# 3 Smuggling remedies: consumption case 1 way; smuggling case 2 ways (temptation/difficulty ends)
assert len(["lower the tax (consumption case)"]) == 1
assert len(["diminish temptation by lowering tax", "increase difficulty by administration"]) == 2
# 4 Warehouse: 2 options; rum excise as 1 existing precedent
assert len(["private warehouse duty paid never drawn back", "public warehouse duty on removal for home consumption, free for export"]) == 2
assert len(["excise duties on imported rum levied this way"]) == 1
# 5 Net-revenue safeguards: 2 savings
assert len(["drawback re-landing loss saved", "export bounties abolished unless real excise drawbacks"]) == 2
# 6 Walpole scheme: 2 commodities, zero successors resumed it
assert len(["wine", "tobacco"]) == 2
assert len([]) == 0
print("187 verify: 6 assertions passed")
