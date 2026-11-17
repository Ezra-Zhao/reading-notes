#!/usr/bin/env python3
"""Verify arithmetic in note 53 (Zhou Weiwen / China Europe New Blue Chip 166002).
All inputs are figures stated in the fund's 2026 Q2 report (reporting
period 2026-04-01 to 2026-06-30, sent 2026-07-21), read in full this
round. This script only checks internal arithmetic consistency.
Clean-room, self-written.
"""
from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure: appointed 2011-05-23, departure blank at 2026-06-30 ->
#    5,517 days = 15.11 years; joined the manager 2011-01-10, 133 days
#    before appointment; co-manager Feng Ludan since 2021-10-14.
check("1 tenure days 5517", (date(2026, 6, 30) - date(2011, 5, 23)).days == 5517)
check("1 tenure years ~15.11", abs(5517 / 365.25 - 15.11) < 0.01)
check("1 join-to-appoint 133 days", (date(2011, 5, 23) - date(2011, 1, 10)).days == 133)
check("1 feng days 1720", (date(2026, 6, 30) - date(2021, 10, 14)).days == 1720)

# 2. Fund contract effective 2008-07-25, 1,032 days (~2.83 years) before
#    he took over: the since-inception figure is not all his.
check("2 pre-tenure gap 1032 days", (date(2011, 5, 23) - date(2008, 7, 25)).days == 1032)
check("2 gap years ~2.83", abs(1032 / 365.25 - 2.83) < 0.01)

# 3. End-of-period NAV: A+C+E = 12,567,961,990.51 yuan (~125.68 yi);
#    A is 72.63% of it; NAV is 98.50% of total assets 12,759,686,270.31.
nav = 9127587392.28 + 2404958082.73 + 1035416515.50
check("3 total NAV 12,567,961,990.51", abs(nav - 12567961990.51) < 0.01)
check("3 A share 72.63%", abs(9127587392.28 / nav * 100 - 72.63) < 0.01)
check("3 NAV/assets 98.50%", abs(nav / 12759686270.31 * 100 - 98.50) < 0.01)

# 4. NAV per share = NAV / shares, within rounding for all classes.
check("4 A 3.6228", abs(9127587392.28 / 2519453956.46 - 3.6228) < 0.0001)
check("4 C 3.4195", abs(2404958082.73 / 703303023.96 - 3.4195) < 0.0001)
check("4 E 3.6387", abs(1035416515.50 / 284555730.26 - 3.6387) < 0.0001)

# 5. Q2 profit: total 2,361,892,745.66; realized 1,605,123,066.81;
#    unrealized share 32.04%.
profit = 1804541466.03 + 365453030.38 + 191898249.25
real = 1201752879.56 + 268434536.04 + 134935651.21
check("5 profit total", abs(profit - 2361892745.66) < 0.01)
check("5 realized total", abs(real - 1605123066.81) < 0.01)
check("5 unrealized share 32.04%", abs((profit - real) / profit * 100 - 32.04) < 0.01)

# 6. Class A windows: 3m +24.30 vs benchmark 7.49 -> excess 16.81 as
#    printed; 6m +22.33 with Q2 +24.30 implies Q1 = -1.58%.
check("6 excess 16.81", abs(24.30 - 7.49 - 16.81) < 1e-9)
check("6 implied Q1 -1.58%", abs((1.2233 / 1.2430 - 1) * 100 + 1.58) < 0.01)

# 7. 1y +95.17% vs 3y +95.66%: the two years before the last one added
#    only +0.25% in total.
check("7 prior two years +0.25%", abs((1.9566 / 1.9517 - 1) * 100 - 0.25) < 0.01)

# 8. 5y +63.70% vs 3y +95.66%: the earliest two of the five years were
#    -16.33%; annualised 5y ~10.36%, 3y ~25.07%.
check("8 earliest two years -16.33%", abs((1.6370 / 1.9566 - 1) * 100 + 16.33) < 0.01)
check("8 ann 5y 10.36 / 3y 25.07", abs((1.6370 ** 0.2 - 1) * 100 - 10.36) < 0.01 and abs((1.9566 ** (1 / 3) - 1) * 100 - 25.07) < 0.01)

# 9. Since inception A +1,116.25% = 12.1625x vs benchmark +98.68% =
#    1.9868x; terminal ratio 6.12x; printed excess 1,017.57pp checks.
check("9 inception excess", abs(1116.25 - 98.68 - 1017.57) < 1e-9)
check("9 terminal ratio 6.12x", abs(12.1625 / 1.9868 - 6.12) < 0.01)

# 10. Top-10 holdings: printed weights sum to 39.30%; fair values sum to
#     4,940,473,328.10 = 39.31% of NAV (0.01pp rounding gap, registered);
#     top-2 optical-module names 15.33%; top-4 tech names 24.27%.
w = [8.45, 6.88, 4.68, 4.26, 3.18, 2.72, 2.49, 2.38, 2.24, 2.02]
fv = [1061847000.00, 865091544.00, 587587724.10, 535894187.40, 399725034.39,
      342309894.40, 313173158.76, 298666494.85, 281709523.20, 254468767.00]
check("10 weights sum 39.30%", abs(sum(w) - 39.30) < 0.01)
check("10 fv sum / NAV 39.31%", abs(sum(fv) / nav * 100 - 39.31) < 0.01)
check("10 top2 15.33 / top4 24.27", abs(w[0] + w[1] - 15.33) < 1e-9 and abs(sum(w[:4]) - 24.27) < 0.01)

# 11. Asset mix: stocks 69.46% of total assets = 70.52% of NAV; cash
#     23.23% of assets = 23.59% of NAV; bonds 6.80% of assets.
check("11 stocks/NAV 70.52%", abs(8863324890.21 / nav * 100 - 70.52) < 0.01)
check("11 cash/NAV 23.59%", abs(2964494251.83 / nav * 100 - 23.59) < 0.01)
check("11 mix sums 100.00", abs(69.46 + 6.80 + 23.23 + 0.50 - 100.00) < 0.015)

# 12. Shares: end total A+C+E = 3,507,312,710.68 as printed in section 2;
#     A net redemption -66,555,160.96 (-2.57%) in a +24.30% quarter;
#     C net subscription +25.28%; total shares +2.77%.
end = 2519453956.46 + 703303023.96 + 284555730.26
beg = 2586009117.42 + 561384392.75 + 265260396.03
check("12 end total matches", abs(end - 3507312710.68) < 0.01)
check("12 A net -2.57%", abs((2519453956.46 / 2586009117.42 - 1) * 100 + 2.57) < 0.01)
check("12 C net +25.28%", abs((703303023.96 / 561384392.75 - 1) * 100 - 25.28) < 0.01)
check("12 total +2.77%", abs((end / beg - 1) * 100 - 2.77) < 0.01)
check("12 flow identity A", abs(2586009117.42 + 1016618124.72 - 1083173285.68 - 2519453956.46) < 0.01)

print("ALL PASSED" if ok else "SOME FAILED")
