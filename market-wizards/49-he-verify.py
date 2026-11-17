#!/usr/bin/env python3
"""Verify arithmetic in note 49 (He Shuai / BOCOM Schroder funds).
All inputs are figures stated in the note's cited sources (the funds'
2026 Q3 reports on CNINFO, report date 2026-10-27, and Sina Finance
reprints of the same reports on 2026-10-29). This script only checks
internal arithmetic consistency. Clean-room, self-written.
"""
from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure: flagship from 2015-07-09, still in post at 2026-09-30
#    (4101 days, about 11.23 years); growth fund from 2018-01-12
#    (3183 days, about 8.71 years). Joined the firm in 2012.
check("1 flagship tenure days 4101", (date(2026, 9, 30) - date(2015, 7, 9)).days == 4101)
check("1 flagship tenure ~11.23y", abs(4101 / 365.25 - 11.23) < 0.01)
check("1 growth tenure days 3183", (date(2026, 9, 30) - date(2018, 1, 12)).days == 3183)
check("1 research-to-manager 2012->2015 = 3y", 2015 - 2012 == 3)

# 2. Manager tenure return (Sina/Wind window to 2026-10-29):
#    flagship 285.67% = 3.8567x over 4130 days (~11.31y) -> ~12.68%/yr.
#    This is NOT the fund's since-transformation 664.60% (2012-02-03),
#    which includes three years before he took over.
check("2 tenure factor 3.8567x", abs((1 + 2.8567) - 3.8567) < 1e-9)
check("2 days to 2026-10-29 = 4130", (date(2026, 10, 29) - date(2015, 7, 9)).days == 4130)
check("2 tenure annualised ~12.68%", abs((3.8567 ** (365.25 / 4130) - 1) * 100 - 12.68) < 0.05)
check("2 fund since-transform 664.60% is a different window",
      abs((664.60 - 285.67) - 378.93) < 0.01)

# 3. Flagship excess-return column self-checks (fund minus benchmark):
#    3m -5.19/-7.17, 6m 26.35/-0.10, 1y 16.71/-1.93, 3y 40.23/17.65,
#    5y 13.93/3.57, 7y 81.71/25.03, 10y 181.44/44.81, since 664.60/94.20.
pairs = [(-5.19, -7.17, 1.98), (26.35, -0.10, 26.45), (16.71, -1.93, 18.64),
         (40.23, 17.65, 22.58), (13.93, 3.57, 10.36), (81.71, 25.03, 56.68),
         (181.44, 44.81, 136.63), (664.60, 94.20, 570.40)]
check("3 all eight excess figures reconcile",
      all(abs((a - b) - c) < 0.011 for a, b, c in pairs))

# 4. Window split: six months +26.35% with Q3 -5.19% implies Q2 alone
#    about +33.27%. Growth fund: six months +33.79% with Q3 +0.82%
#    implies Q2 alone about +32.70%. Same manager, same Q2 shape.
check("4 flagship implied Q2 ~+33.27%", abs((1.2635 / 0.9481 - 1) * 100 - 33.27) < 0.05)
check("4 growth implied Q2 ~+32.70%", abs((1.3379 / 1.0082 - 1) * 100 - 32.70) < 0.05)
check("4 Q3 drop rebound needs +5.47%", abs((1 / 0.9481 - 1) * 100 - 5.47) < 0.01)

# 5. Long-window split: past 5y +13.93% vs past 3y +40.23% implies the
#    two years before that were about -18.75% combined; past 10y
#    +181.44% vs past 5y implies the first five years were +147.03%.
check("5 earlier two years ~-18.75%", abs((1.1393 / 1.4023 - 1) * 100 - (-18.75)) < 0.05)
check("5 first five of ten ~+147.03%", abs((2.8144 / 1.1393 - 1) * 100 - 147.03) < 0.05)

# 6. The cash quarter: flagship asset mix at 2026-09-30 (share of total
#    assets) stocks 31.08 + bonds 5.25 + deposits 63.35 + other 0.32
#    = 100.00. Growth fund stocks 59.37, deposits 40.22: the flagship
#    held 28.29pp less equity than his own other fund.
check("6 flagship mix sums 100.00", abs((31.08 + 5.25 + 63.35 + 0.32) - 100.00) < 1e-9)
check("6 growth mix sums 100.00", abs((59.37 + 40.22 + 0.41) - 100.00) < 1e-9)
check("6 equity gap between his two funds 28.29pp", abs((59.37 - 31.08) - 28.29) < 1e-9)
check("6 cash is 2.04x the equity book", abs(63.35 / 31.08 - 2.04) < 0.01)

# 7. What was left was concentrated: top-10 weights (share of NAV)
#    sum to 29.83% against total equity of 31.22% of NAV, i.e. the
#    top ten are 95.55% of the equity book; top stock alone 31.65%;
#    top four 24.30% of NAV = 77.83% of the equity book.
top10 = [9.88, 5.86, 4.49, 4.07, 1.62, 1.47, 0.86, 0.65, 0.47, 0.46]
check("7 top10 sums 29.83", abs(sum(top10) - 29.83) < 0.01)
check("7 top10 = 95.55% of equity", abs(sum(top10) / 31.22 * 100 - 95.55) < 0.05)
check("7 top1 = 31.65% of equity", abs(9.88 / 31.22 * 100 - 31.65) < 0.05)
check("7 top4 = 77.83% of equity", abs(sum(top10[:4]) / 31.22 * 100 - 77.83) < 0.05)

# 8. Q3 profit split: realised -93,255,490.18 and total profit
#    -142,861,167.36, so the unrealised (mark-to-market) part is
#    -49,605,677.18. Shares x NAV reproduces reported net assets
#    within rounding of the 3-decimal NAV.
check("8 unrealised part -49,605,677.18",
      abs((-142861167.36 - (-93255490.18)) - (-49605677.18)) < 0.01)
check("8 shares x NAV within 0.01% of net assets",
      abs(446649285.70 * 5.586 - 2494929004.73) / 2494929004.73 < 0.0001)

# 9. Share flows: 471,995,473.97 + 14,835,645.32 - 40,181,833.59
#    = 446,649,285.70; net -5.37%; redemptions were 2.71x subscriptions.
check("9 share identity holds",
      abs((471995473.97 + 14835645.32 - 40181833.59) - 446649285.70) < 0.01)
check("9 net share change -5.37%",
      abs((446649285.70 / 471995473.97 - 1) * 100 - (-5.37)) < 0.01)
check("9 redemptions 2.71x subscriptions", abs(40181833.59 / 14835645.32 - 2.71) < 0.01)

# 10. Second fund cross-checks: Q3 excess A 0.82-(-7.93)=8.75 and
#     C 0.67-(-7.93)=8.60; A NAV 647,597,114.67 + C 10,654,449.94
#     = 658,251,564.61 total, A is 98.38%; HK stocks 118,859,675.17
#     are 18.06% of net assets as the report states; A tenure return
#     178.95% (to 2026-10-29) vs fund since-inception 186.00%
#     (to 2026-09-30) are different windows, 7.05pp apart.
check("10 growth A excess 8.75", abs((0.82 - (-7.93)) - 8.75) < 1e-9)
check("10 growth C excess 8.60", abs((0.67 - (-7.93)) - 8.60) < 1e-9)
check("10 A+C net assets 658,251,564.61",
      abs((647597114.67 + 10654449.94) - 658251564.61) < 0.01)
check("10 A is 98.38% of the fund", abs(647597114.67 / 658251564.61 * 100 - 98.38) < 0.01)
check("10 HK weight 18.06%", abs(118859675.17 / 658251564.61 * 100 - 18.06) < 0.01)
check("10 tenure vs inception gap 7.05pp", abs((186.00 - 178.95) - 7.05) < 0.01)

print("ALL PASSED" if ok else "SOME FAILED")
