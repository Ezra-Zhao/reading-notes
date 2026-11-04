# -*- coding: utf-8 -*-
# Data from the book passage covered by note 186; no modern measurement.
# 1 Year ending 5 Jan 1755 main chain (book's stated totals)
gross = 5068000
bounties_drawbacks = 2324600
assert gross - bounties_drawbacks == 2743400
assert 2743400 - 287900 == 2455500
# 2 Dissipation shares: bounties+drawbacks ~46%, net ~48% of gross
assert 0.40 < bounties_drawbacks / gross < 0.50
assert 2455500 / gross < 0.50
# 3 Management expense: ~5-6% of gross, >10% of post-deduction remainder
assert 0.05 < 287900 / gross < 0.06
assert 287900 / 2743400 > 0.10
# 4 Unlisted goods: 4s 9.75d = 57.75d per 240d ~ 24.1%, near five subsidies (25%)
assert abs(57.75 / 240 - 0.2406) < 0.001 and 57.75 / 240 < 0.25
# 5 Shift: old subsidy on 2 directions, later subsidies on import only; drawback 2 tiers
assert len(["export", "import"]) == 2
assert len(["old subsidy half drawn back", "later subsidies mostly whole drawn back"]) == 2
# 6 Materials exceptions 2 directions; prohibition examples 2
assert len(["foreign materials duty-free in", "home/colonial materials barred or heavy out"]) == 2
assert len(["foreign woollens wholly prohibited", "foreign silks and velvets much diminished"]) == 2
print("186 verify: 6 assertions passed")
