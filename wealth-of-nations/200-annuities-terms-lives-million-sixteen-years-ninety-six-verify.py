# -*- coding: utf-8 -*-
# Data from the book passage covered by note 200; no modern measurement.
# 1 Middle borrowing methods are exactly 2: annuities for terms of years
#    and annuities for lives
assert len(["annuities for terms of years", "annuities for lives"]) == 2
# 2 1695 loan: 1,000,000 pounds at 140,000 a year = 14 per cent; over 16
#    years the total paid is 2,240,000, more than twice the principal
assert 140000 * 100 // 1000000 == 14
assert 140000 * 16 == 2240000 and 2240000 > 2 * 1000000
# 3 Fourteen per cent is a little more than seven years purchase
assert abs(100 / 14 - 7.142857) < 0.001 and 100 / 14 > 7
# 4 Exchange price: 63 pounds per hundred is 4.5 years purchase at 14
assert 63 / 14 == 4.5
# 5 Queen Anne term samples are exactly 4: 32, 89, 98, 99 years; the
#    longest exceeds the 1695 term of 16 years
terms = [32, 89, 98, 99]
assert len(terms) == 4 and max(terms) > 16
# 6 Long annuities fell from 666,821 pounds a year to a remainder of
#    136,453; the fall is 530,368 and the remainder is under one third
assert 666821 - 136453 == 530368
assert 136453 * 3 < 666821
print("200 verify: 6 assertions passed")
