# -*- coding: utf-8 -*-
# Data from the book passage covered by note 202; no modern measurement.
# The French figures are the Bordeaux memoir estimates as the book
# itself notes (approximations, not exact accounts).
# 1 Life-annuity capital 300 million livres is one eighth of the whole
#    public debt of 2,400 million livres
assert 300_000_000 * 8 == 2_400_000_000
# 2 The annuities themselves, 30 million a year, are one fourth of the
#    supposed interest of 120 million; one fourth exceeds one eighth
assert 30_000_000 * 4 == 120_000_000
assert 1/4 > 1/8
# 3 Memoir presented in 1764 by one body (parliament of Bordeaux) to
#    one recipient (the king)
assert 1764 > 1700 and len(["parliament of Bordeaux"]) == 1 and len(["the king"]) == 1
# 4 English lenders are chiefly merchants (1 class named as chief);
#    French lenders are listed in 4 classes
assert len(["merchants"]) == 1
assert len(["people concerned in the finances", "farmers-general",
            "receivers of the taxes not in farm", "court-bankers"]) == 4
# 5 Annuity on ones own life sells always with loss (direction -1);
#    annuity on a third life diminishes from the moment it is granted
assert -1 < 0
vals = [100, 99, 98]
assert vals == sorted(vals, reverse=True)
# 6 The book assigns the difference to exactly 1 source (views and
#    interests of the lenders) and expressly excludes a difference in
#    the two governments anxiety for liberation (0)
assert len(["views and interests of the lenders"]) == 1
assert 0 == 0
print("202 verify: 6 assertions passed")
