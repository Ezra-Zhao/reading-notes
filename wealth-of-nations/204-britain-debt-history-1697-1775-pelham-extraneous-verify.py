# -*- coding: utf-8 -*-
# Data from the book passage covered by note 204; pounds only, the
# shillings/pence in the source are noted in the note itself.
# 1 1697 debt minus the reduction before 1701 leaves the stated remainder
assert 21_515_742 - 5_121_041 == 16_394_701
# 2 A war of less than 9 years added over 3x what 17 years of profound
#    peace had paid off
assert 31_338_689 > 8_328_554 * 3
# 3 Funded plus unfunded at the 1763 peace is below the 1764 total
assert 122_603_336 + 13_927_589 == 136_530_925
assert 136_530_925 < 139_561_807
# 4 The three war-derived extraneous items sum to the stated total
assert 690_449 + 670_000 + 95_500 == 1_455_949
# 5 Eleven-year repayment minus the extraneous floor of five millions,
#    averaged, is under half a million a year from ordinary savings
assert (10_415_476 - 5_000_000) / 11 < 500_000
# 6 War borrowing above 75 millions exceeds 12x the 6 millions of old
#    debt a prudent peace administration could not clear in like time
assert 75_000_000 > 6_000_000 * 12
print("204 verify: 6 assertions passed")
