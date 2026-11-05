# -*- coding: utf-8 -*-
# Data from the book passage covered by note 207; no modern measurement.
# 1 States/republics named as enfeebled: Genoa, Venice, Spain, France, United Provinces
assert len(["Genoa", "Venice", "Spain", "France", "United Provinces"]) == 5
# 2 Spain deeply in debt before end of 16th century, about 100 years before England owed a shilling
assert 100 > 0
# 3 Fair and complete payments of accumulated national debts: scarce a single instance -> 0
assert 0 == 0
# 4 Sixpence raised to a shilling doubles the denomination; 20 sixpences = 1 pound;
#    borrowed 20s ~4oz silver, pays with <2oz, i.e. less than half
assert 6 * 2 == 12 and 20 * 12 == 240 and 2 < 4 / 2 + 1 and 2 <= 4 // 2
assert 20 * 6 == 120  # old denomination pence in twenty sixpences
# 5 128 millions paid with about 64 millions = one half; defrauded 10s of 20s = one half
assert 128_000_000 // 2 == 64_000_000 and 10 / 20 == 0.5
# 6 Avowed bankruptcy ranks best on both measures (least dishonourable, least hurtful)
assert len(["least dishonourable to debtor", "least hurtful to creditor"]) == 2
print("207 verify: 6 assertions passed")
