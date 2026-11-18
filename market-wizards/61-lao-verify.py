#!/usr/bin/env python3
"""Verify arithmetic in note 61 (Lao Jienan / China Universal Value
Selected Mixed Fund, 519069).

All inputs are figures printed in the fund's 2026 Q3 report
(disclosed via CNINFO / SSE, report end 2026-09-30, sent
2026-10-27): identity from section 4.1, performance windows from
section 3.2.1, financials from section 3.1, portfolio from
sections 5.1-5.3, share changes from section 6, manager's own
holding from section 7.1. This script only checks internal
arithmetic consistency and derived windows. Clean-room,
self-written.
"""

from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# Performance windows: (fund %, benchmark %, stated excess pp)
win = [
    (-11.53, -9.84, -1.69), (1.43, -1.09, 2.52),
    (0.68, -4.11, 4.79), (29.20, 17.98, 11.22),
    (-14.55, -3.58, -10.97), (29.54, 19.79, 9.75),
    (80.80, 39.68, 41.12), (650.32, 123.46, 526.86),
]

# 1. Tenure: appointed 2015-11-18, still in post at 2026-09-30:
#    3,969 days, about 10.87 years; the fund contract took effect
#    2009-01-23, 2,490 days before his appointment, so the
#    since-inception figure includes almost seven years that are
#    not his.
d = (date(2026, 9, 30) - date(2015, 11, 18)).days
check("1 tenure 3969 days ~10.87y", d == 3969 and abs(d / 365.25 - 10.87) < 0.01)
check("1 contract predates tenure by 2490 days",
      (date(2015, 11, 18) - date(2009, 1, 23)).days == 2490)

# 2. All eight stated excess figures equal fund minus benchmark.
check("2 eight excess figures self-consistent",
      all(abs((f - b) - e) < 0.005 for f, b, e in win))

# 3. End shares times unit NAV 3.124 reproduce end net assets
#    6,496,974,700.56 within four-decimal NAV rounding (<0.01%).
shares_end = 2079564382.69
nav_total = 6496974700.56
check("3 shares*NAV within rounding of net assets",
      abs(shares_end * 3.124 - nav_total) / nav_total < 0.0001)

# 4. Window splits: earliest five years of the ten-year window,
#    first two years of the seven-year window, first two years
#    of the three-year window.
check("4 earliest 5y of 10y ~+111.59%",
      abs((1.8080 / 0.8545 - 1) * 100 - 111.59) < 0.01)
check("4 first 2y of 7y ~+51.60%",
      abs((1.2954 / 0.8545 - 1) * 100 - 51.60) < 0.01)
check("4 first 2y of 3y ~+28.33%",
      abs((1.2920 / 1.0068 - 1) * 100 - 28.33) < 0.01)

# 5. Q2 2026 implied by six-month minus Q3: about +14.65%; the
#    half year is a strong quarter followed by a weak one.
check("5 implied Q2 ~+14.65%",
      abs((1.0143 / 0.8847 - 1) * 100 - 14.65) < 0.01)

# 6. Profit split: realised +276,009,950.21 against total profit
#    -856,630,058.93 gives an unrealised loss of about
#    -1,132,640,009.14, about 4.10x the realised gain.
realised = 276009950.21
profit = -856630058.93
unreal = profit - realised
check("6 unrealised ~-1,132,640,009.14",
      abs(unreal - (-1132640009.14)) < 0.01)
check("6 unrealised loss ~4.10x realised gain",
      abs(abs(unreal) / realised - 4.10) < 0.01)

# 7. Share reconciliation: start + subscriptions - redemptions
#    equals end exactly; net redemption 90,306,304.96 shares is
#    about 4.16% of the opening balance, subscriptions only
#    about 1.29%.
s0, sub, red = 2169870687.65, 28031623.03, 118337927.99
check("7 share reconciliation exact", abs(s0 + sub - red - shares_end) < 0.01)
check("7 net redemption ~4.16% of opening",
      abs((s0 - shares_end) / s0 * 100 - 4.16) < 0.01)
check("7 subscriptions ~1.29% of opening", abs(sub / s0 * 100 - 1.29) < 0.01)

# 8. Asset mix: the four asset lines sum exactly to total assets
#    6,510,983,245.82; equity is 85.56% of total assets and about
#    85.75% of net assets.
parts = [5570929760.34, 99978904.11, 836007131.43, 4067449.94]
check("8 asset lines sum exactly", abs(sum(parts) - 6510983245.82) < 0.01)
check("8 equity ~85.75% of net assets",
      abs(5570929760.34 / nav_total * 100 - 85.75) < 0.01)
check("8 cash ~12.84% of total assets",
      abs(836007131.43 / 6510983245.82 * 100 - 12.84) < 0.01)

# 9. Industry lines sum to 85.74% against a stated total of
#    85.75% (0.01 rounding); manufacturing 54.44% plus finance
#    18.17% is 72.61%, about 84.66% of the equity book.
ind = [8.18, 54.44, 4.52, 0.43, 18.17]
check("9 industry sum 85.74 vs stated 85.75 rounding",
      abs(sum(ind) - 85.74) < 0.005)
check("9 manufacturing+finance 72.61, ~84.66% of equity",
      abs((54.44 + 18.17) - 72.61) < 0.005
      and abs(72.61 / 85.75 * 100 - 84.66) < 0.02)

# 10. Top ten sum to 54.44% of net assets (a numerical coincidence
#     with the manufacturing share, different bases); top three
#     20.17%; three banks 15.13%; two drug makers 9.80%; top ten
#     are about 63.49% of the equity book.
top = [7.45, 6.65, 6.07, 5.63, 5.02, 4.96, 4.78, 4.70, 4.64, 4.54]
check("10 top10 sum 54.44", abs(sum(top) - 54.44) < 0.005)
check("10 top3 20.17, banks 15.13, pharma 9.80",
      abs(sum(top[:3]) - 20.17) < 0.005
      and abs((5.63 + 4.96 + 4.54) - 15.13) < 0.005
      and abs((5.02 + 4.78) - 9.80) < 0.005)
check("10 top10 ~63.49% of equity book",
      abs(sum(top) / 85.75 * 100 - 63.49) < 0.01)

# 11. Annualised and recovery: ten years +80.80% annualises to
#     about +6.10%; five years -14.55% to about -3.10%; the
#     five-year hole needs about +17.03% to fill.
check("11 10y annualised ~+6.10%", abs(1.8080 ** 0.1 - 1 - 0.0610) < 0.001)
check("11 5y annualised ~-3.10%", abs(0.8545 ** 0.2 - 1 - (-0.0310)) < 0.001)
check("11 -14.55% needs ~+17.03% to recover",
      abs((1 / 0.8545 - 1) * 100 - 17.03) < 0.01)

# 12. Manager's own holding: 4,161,089.75 shares is about 0.20%
#     of the fund, unchanged over the quarter; weighted-average
#     profit per share -0.4052 implies an average share base of
#     about 2.114 billion, between opening and closing balances.
check("12 manager holding ~0.20%",
      abs(4161089.75 / shares_end * 100 - 0.20) < 0.005)
check("12 implied average shares ~2.114bn between open and close",
      abs(profit / -0.4052 / 1e9 - 2.114) < 0.002
      and shares_end < profit / -0.4052 < s0)

print("ALL PASS" if ok else "SOME FAILED")
