"""Market Wizards 13 Wang Fuji verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; inputs are public-source figures
from Pientzehuang (600436) periodic reports / allotment announcement and press reports:
1) 2009 H1 first appearance: 2,755,100 shares on 140,000,000 total = 1.97%;
   2010 H1: 6,300,000 shares on the same 140,000,000 total = 4.50%;
2) 2013 allotment: total 140,000,000 + 20,884,589 = 160,884,589;
   his 7,268,000 shares = 4.52%;
3) Share-count growth 2009->2026Q3: 27,228,500 / 2,755,100 = 9.88x, decomposed as
   total-capital expansion 603,317,210 / 140,000,000 = 4.31x times stake rise about 2.29x;
4) Holding value: FY2021 report 118.19 yi CNY vs 2026Q3 32.13 yi CNY:
   difference 86.06 yi, drop 72.8%; implied prices 437.13 and 118.00 CNY;
   share count actually rose 191,000 shares (+0.71%) between the two dates;
5) Cross-check 2026-11-04: close 132.17 CNY x 603,317,210 shares = about 797 yi market cap;
6) Musk/bovine bezoar price in his 2024 speech transcript: 100k -> 1,800k CNY/kg = 18x;
   holding span 2026 - 2009 = 17 years.
"""
assert round(275.51 / 14000 * 100, 2) == 1.97
assert round(630 / 14000 * 100, 2) == 4.50
print("1 ok: 2009 H1 275.51/14000 = 1.97%; 2010 H1 630/14000 = 4.50%")
assert 14000 + 2088.4589 == 16088.4589
assert round(726.8 / 16088.4589 * 100, 2) == 4.52
print("2 ok: 2013 allotment total 16088.4589 wan shares; 726.8 wan = 4.52%")
assert round(2722.85 / 275.51, 2) == 9.88
assert round(60331.721 / 14000, 2) == 4.31
assert round(4.51 / 1.97, 2) == 2.29
print("3 ok: shares 9.88x = capital expansion 4.31x x stake rise about 2.29x")
assert round(118.19 - 32.13, 2) == 86.06
assert round((1 - 32.13 / 118.19) * 100, 1) == 72.8
assert round(118.19 * 10000 / 2703.75, 1) == 437.1
assert round(32.13 * 10000 / 2722.85, 1) == 118.0
assert round(2722.85 - 2703.75, 2) == 19.10 and round(19.10 / 2703.75 * 100, 2) == 0.71
print("4 ok: value 118.19 -> 32.13 yi, -86.06 yi (-72.8%); implied 437.1 vs 118.0 CNY; shares +0.71%")
assert round(132.17 * 6.0331721, 0) == 797
print("5 ok: 2026-11-04 close 132.17 x 6.0331721 yi shares = about 797 yi market cap")
assert 180 / 10 == 18 and 2026 - 2009 == 17
print("6 ok: bezoar 10 -> 180 wan/kg = 18x; 2009 to 2026 = 17 years")
print("All six assertions passed")
