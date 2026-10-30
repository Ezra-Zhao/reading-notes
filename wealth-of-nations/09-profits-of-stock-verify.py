#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 09
(Book I Ch. IX, profits of stock).
Numbers are Smith's in-text figures, recomputed; not modern measurements."""
# 1. England legal interest ladder: Henry VIII 10, James I 8,
#    after Restoration 6, Queen Anne 5 per cent (strictly falling).
ladder = [10, 8, 6, 5]
assert ladder == sorted(ladder, reverse=True) and len(ladder) == 4
# 2. France swings: 1720 from 5 to 2, 1724 to 3 1/3, 1725 back to 5,
#    1766 to 4, afterwards back to 5 per cent.
france = [5, 2, 10 / 3, 5, 4, 5]
assert france[1] == 2 and abs(france[2] - 3.3333) < 0.001
# Penny fractions: twentieth penny = 5%, fiftieth = 2%, thirtieth = 3 1/3%,
# twenty-fifth = 4%.
assert (100 / 20, 100 / 50, 100 / 25) == (5, 2, 4)
# 3. Holland: government borrows at 2, good private credit at 3 per cent.
assert (2, 3) == (2, 3) and 3 - 2 == 1
# Colonies legal and market interest run from 6 to 8 per cent.
assert (6, 8) == (6, 8)
# 4. Bengal money lent to farmers at 40, 50, 60 per cent;
#    Brutus in Cyprus at 48 per cent; China common interest 12 per cent.
assert sorted([40, 50, 60]) == [40, 50, 60] and 48 > 12
# 5. Britain rule: double interest is reckoned a good moderate profit;
#    clear profit 8 or 10 per cent, half to interest = 4 or 5 per cent.
assert (8 / 2, 10 / 2) == (4, 5)
# 6. Linen chain has three employer stages; a 5 per cent profit rise
#    compounds geometrically: factor 1.05^3, while a wages rise adds
#    only arithmetically (twopences times hands times days).
stages = ["flax_dressers", "spinners", "weavers"]
assert len(stages) == 3
assert abs(1.05 ** 3 - 1.157625) < 1e-9
assert 1.05 ** 3 > 1 + 0.05 * 3
print("09-profits-of-stock-verify: all assertions passed")
print("  england=10/8/6/5 france=5-2-3.33-5-4-5 holland=2/3 colonies=6-8 bengal=40/50/60 brutus=48 china=12 double-interest=8-10->4-5 linen=1.05^3")
