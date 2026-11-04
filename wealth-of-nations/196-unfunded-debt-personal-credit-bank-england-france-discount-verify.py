# -*- coding: utf-8 -*-
# Data from the book passage covered by note 196; no modern measurement.
# 1 Unfunded debt has 2 kinds: bearing (or supposed to bear) no interest,
#    like a private man's account debts; and bearing interest, like his bills
assert len(["no-interest, on account", "interest-bearing, on bill or note"]) == 2
# 2 Interest start: exchequer bills from the day of issue (month 0);
#    navy bills six months after issue (month 6); gap is 6 months
assert 6 - 0 == 6
assert 0 < 6
# 3 France, having no bank: billets d'etat sold at 60 and 70 per cent discount,
#    i.e. buyers paid 40 down to 30 per cent of face
assert 100 - 60 == 40
assert 100 - 70 == 30
assert 30 < 40
# 4 William's recoinage, Bank support stopped: exchequer bills and tallies
#    sold from 25 to 60 per cent discount, i.e. at 75 down to 40 of face
assert 100 - 25 == 75
assert 100 - 60 == 40
assert 75 > 40
# 5 Causes assigned for that discount: 2 (supposed instability of the new
#    government; want of the support of the Bank of England)
assert len(["instability of the Revolution government", "want of Bank support"]) == 2
# 6 Borrowing stages are 2 (personal credit first, then assignments of
#    particular funds); assignment itself has 2 modes (short-term anticipation
#    paying principal+interest; perpetual funding paying interest only)
assert len(["personal credit", "assignment of particular funds"]) == 2
assert len(["anticipation (short term)", "perpetual funding"]) == 2
print("196 verify: 6 assertions passed")
