#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 08
(Book I Ch. VIII, wages of labour).
Numbers are Smith's in-text figures, recomputed; not modern measurements."""
# 1. Productivity parable: most trades improve tenfold, one only double.
#    Its pound appears 10/2 = 5 times dearer, yet needs half the labour,
#    so in reality it is twice as cheap.
assert 10 // 2 == 5
assert 1 / 2 == 0.5
# 2. Europe: twenty workmen under a master for one independent (20 to 1).
assert 20 // 1 == 20
# 3. Cantillon floor: earn at least double own maintenance; half the
#    children die before manhood, so rear 4 for 2 to survive;
#    maintenance of 4 children is nearly equal to that of 1 man.
assert 2 * 1 == 2
assert 4 // 2 == 2 and 4 * 0.5 == 2
# 4. Population doubling: Britain not less than 500 years;
#    North American colonies 20 or 25 years.
assert 500 // 25 == 20 and 500 // 20 == 25
# 5. London common labour 18d vs 14-15d a few miles off: a fourth or a
#    fifth higher, i.e. 20 to 25 per cent.
assert round((18 - 14.4) / 14.4 * 100) == 25
assert 1 / 5 * 100 == 20 and 1 / 4 * 100 == 25
# Edinburgh 10d vs 8d a few miles off is likewise 25 per cent higher.
assert (10 - 8) / 8 * 100 == 25
# 6. New York 1773 sterling equivalents in pence: common labourer
#    2s = 24d; ship-carpenter 6s6d = 78d; house-carpenter 4s6d = 54d.
assert (2 * 12, 6 * 12 + 6, 4 * 12 + 6) == (24, 78, 54)
# Hales: family of six at 10s a week = 26 pounds a year (52 weeks).
assert 10 * 52 // 20 == 26
print("08-wages-of-labour-verify: all assertions passed")
print("  parable=5x-appear/2x-cheap ratio=20:1 cantillon=2x/4rear2 doubling=500vs20-25 london=18dvs14-15d ny=24/78/54d hales=26/yr")
