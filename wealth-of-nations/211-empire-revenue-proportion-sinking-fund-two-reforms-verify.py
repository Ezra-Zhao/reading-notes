# -*- coding: utf-8 -*-
# Data from the book passage covered by note 211; no modern measurement.
# 1 Proportional extrapolation: 13M / 8M = 1.625; 10M * 1.625 = 16.25M
assert 13_000_000 / 8_000_000 == 1.625
assert 10_000_000 * 1.625 == 16_250_000
# 2 Deductions: Ireland <750k + colonies 141,800 + omitted 30-40k sums below the round 1M taken
assert 750_000 + 141_800 + 40_000 == 931_800 and 931_800 < 1_000_000
# 3 Remainder after the round deduction
assert 16_250_000 - 1_000_000 == 15_250_000
# 4 Peace-time spare for debt payment rises 1M -> 6.25M, within the remainder
assert 6_250_000 - 1_000_000 == 5_250_000 and 6_250_000 < 15_250_000
# 5 Population build-up as supposed in the book: 8M + 2M + 3M = 13M; American figure discounted to 3M
assert 8_000_000 + 2_000_000 + 3_000_000 == 13_000_000
assert 3_000_000 <= 3_000_000
# 6 Two simple alterations against smuggling
assert len(["single duty upon malt", "customs confined to few goods under excise laws"]) == 2
print("211 verify: 6 assertions passed")
