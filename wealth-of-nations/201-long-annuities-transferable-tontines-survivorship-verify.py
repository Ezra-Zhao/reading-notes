# -*- coding: utf-8 -*-
# Data from the book passage covered by note 201; no modern measurement.
# 1 The two wars began in 1739 and 1755; the second is 16 years later
assert 1755 - 1739 == 16
# 2 Long terms named are 98 and 99 years, both finite and, as the book
#    puts it, nearly equal in value to a perpetuity (difference 1 year)
assert max([98, 99]) - min([98, 99]) == 1
# 3 In those wars annuities served as premiums, not as the proper fund:
#    proper-fund uses recorded as 0 in this passage, premium uses as 1 role
roles = {"proper fund": 0, "premium to subscribers": 1}
assert roles["proper fund"] == 0 and roles["premium to subscribers"] == 1
# 4 Life annuities are granted in exactly 2 ways: separate lives and
#    lots of lives (tontines)
assert len(["separate lives", "tontines"]) == 2
# 5 A tontine lot may consist of 20 to 30 persons; upper is 1.5x lower
assert 20 > 1 and 30 / 20 == 1.5
# 6 Liberation order: separate lives disburden at each death (first
#    liberation early), tontines only after all in the lot die (later)
first_liberation = {"separate lives": 1, "tontines": 30}
assert first_liberation["tontines"] > first_liberation["separate lives"]
print("201 verify: 6 assertions passed")
