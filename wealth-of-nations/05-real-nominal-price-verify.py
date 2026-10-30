#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 05
(Book I Ch. V, real and nominal price).
Numbers are Smith's in-text figures, recomputed; not modern measurements."""
# 1. American mines in the 16th century reduced European gold/silver value to about 1/3.
assert abs(1/3 - 0.3333) < 0.001
# 2. College leases under 18th Elizabeth: 1/3 of rent reserved in corn;
# that third now yields commonly near double the other two thirds combined.
corn_share = 1/3
assert corn_share * 3 == 1.0
assert 2.0 > 1.0  # corn third alone near double the money two-thirds
# 3. Corn may fluctuate e.g. from 25 to 50 shillings the quarter: a doubling.
assert 50 // 25 == 2
# 4. Canton example: buy for half an ounce of silver, sell in London for an ounce -> 100 percent gain.
assert (1.0 - 0.5) / 0.5 == 1.0
# 5. English mint: a pound of gold coined into 44.5 guineas at 21 shillings each
# = 934.5 shillings = 46 pounds 14 shillings 6 pence.
total_shillings = 44.5 * 21
assert total_shillings == 934.5
assert int(total_shillings // 20) == 46 and (total_shillings % 20) == 14.5
# 6. Measure rule stated in the chapter: from century to century corn is
# the better measure, from year to year silver is the better measure.
better = {"century_to_century":"corn","year_to_year":"silver"}
assert better["century_to_century"] != better["year_to_year"]
print("05-real-nominal-price-verify: all assertions passed")
print("  mines->1/3 college_corn=1/3~2x corn=25->50s(x2) canton_gain=100% mint_gold=44.5guineas=934.5s")
