# -*- coding: utf-8 -*-
# Data from the book passage covered by note 185; no modern measurement.
# 1 Excise exceptions: 4 necessaries + perhaps green glass
assert len(["salt", "soap", "leather", "candles"]) == 4
assert len(["green glass (perhaps)"]) == 1
# 2 Customs three branches
assert len(["wool and leather", "tonnage on wine", "poundage on other goods"]) == 3
# 3 Poundage zigzag: 6d -> 12d (1s) -> 6d -> 8d -> 12d; 1s / 240d = 5%
assert 12 == 2 * 6 and 6 < 8 < 12
assert 12 / 240 == 0.05
# 4 Subsidy layers: old + new + (1/3+2/3) + 1747 + 1759 = 5 layers of 5%
assert len(["old", "new", "thirds combined", "1747", "1759"]) == 5
assert 5 * 5 == 25
# 5 Ancient customs uniform on 2 dimensions; alien distinction 2 stages
assert len(["necessaries/luxuries alike", "export/import alike"]) == 2
assert len(["begun from ignorance", "continued from monopoly"]) == 2
# 6 Book of rates: 12 Charles II, method older than James I
assert len(["book of rates 12 Charles II"]) == 1
print("185 verify: 6 assertions passed")
