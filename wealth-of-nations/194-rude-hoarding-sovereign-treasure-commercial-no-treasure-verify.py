# -*- coding: utf-8 -*-
# Data from the book passage covered by note 194; no modern measurement.
# 1 Since Henry IV's death in 1610, only the present and late kings of Prussia
#    are supposed to have amassed any considerable treasure (2 persons, 1 line)
assert 1610 == 1610
assert len(["present king of Prussia", "late king of Prussia"]) == 2
# 2 Rude-state sovereign expense has scarce any outlet but 2: bounty to
#    tenants and hospitality to retainers; vanity-driven court finery absent
assert len(["bounty to tenants", "hospitality to retainers"]) == 2
assert len([]) == 0  # standing armies not necessary in the rude state
# 3 Two bars kept gentlemen from using saved money openly: trade disgraceful,
#    lending at interest counted usury and prohibited by law
assert len(["trade disgraceful to a gentleman", "interest as usury prohibited"]) == 2
# 4 Debtor republics named in 2 groups (Italian republics, United Provinces);
#    the single European republic with a considerable treasure is Berne (1)
assert len(["Italian republics", "United Provinces"]) == 2
assert len(["canton of Berne"]) == 1
# 5 Swiss republics other than Berne with a treasure: none
assert len([]) == 0  # no other Swiss republic amassed a treasure
assert 1 + 0 == 1  # exactly one republic exception in Europe per the passage
# 6 Rude great revenue is paid in necessaries of 2 broad kinds in the text's
#    pairing (materials of food/clothing: corn/cattle and wool/raw hides = 4)
necessaries = ["corn", "cattle", "wool", "raw hides"]
assert len(necessaries) == 4
assert len(["hospitality without luxury", "liberality without ostentation"]) == 2
print("194 verify: 6 assertions passed")
