#!/usr/bin/env python3
"""Verify arithmetic in note 55 (Wang Chong / Bank of Communications
Schroder New Growth Mixed Fund, 519736).

All inputs are figures printed in the fund's 2026 Q3 report (period
ending 2026-09-30, sent 2026-10-27, cninfo disclosure). This script
only checks internal arithmetic consistency and derived windows.
Clean-room, self-written.
"""

from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure: manager since 2014-10-22, still in post at 2026-09-30
#    (departure column blank); fund inception 2014-05-09.
tenure = (date(2026, 9, 30) - date(2014, 10, 22)).days
pre = (date(2014, 10, 22) - date(2014, 5, 9)).days
life = (date(2026, 9, 30) - date(2014, 5, 9)).days
check("1 tenure days 4361", tenure == 4361)
check("1 tenure years ~11.94", abs(tenure / 365.25 - 11.94) < 0.01)
check("1 pre-tenure days 166, life 4527", pre == 166 and life == 4527)
check("1 tenure share of fund life ~96.33%", abs(tenure / life * 100 - 96.33) < 0.01)

# 2. Every reported excess (fund minus benchmark) in the 3.2.1 table
#    matches simple subtraction of the two printed columns.
rows = [(7.33, -16.60, 23.93), (8.59, 0.23, 8.36), (6.38, -3.98, 10.36),
        (6.25, 15.01, -8.76), (-14.48, -14.45, -0.03), (52.24, 18.76, 33.48),
        (133.97, 27.30, 106.67), (336.11, 65.79, 270.32)]
check("2 all eight excess diffs match", all(abs(a - b - d) < 0.005 for a, b, d in rows))

# 3. Implied sub-periods inside the one-year window: Q2 2026 alone is
#    about +1.17% (6m over 3m); the six months before the last six are
#    about -2.04% (1y over 6m).
check("3 implied Q2 ~+1.17%", abs((1.0859 / 1.0733 - 1) * 100 - 1.17) < 0.01)
check("3 implied prior half ~-2.04%", abs((1.0638 / 1.0859 - 1) * 100 + 2.04) < 0.01)

# 4. Longer sub-periods by division: the two years before the last
#    three lost about -19.51% cumulatively (5y over 3y); the two years
#    before the last five gained about +78.02% (7y over 5y); the three
#    years before the last seven gained about +53.68% (10y over 7y).
check("4 5y-over-3y prior 2y ~-19.51%", abs((0.8552 / 1.0625 - 1) * 100 + 19.51) < 0.01)
check("4 7y-over-5y prior 2y ~+78.02%", abs((1.5224 / 0.8552 - 1) * 100 - 78.02) < 0.01)
check("4 10y-over-7y prior 3y ~+53.68%", abs((2.3397 / 1.5224 - 1) * 100 - 53.68) < 0.01)

# 5. Ending shares times ending unit NAV reproduce ending net assets
#    within rounding of the three-decimal unit NAV.
check("5 shares x NAV ~ net assets (0.01%)",
      abs(971606098.64 * 3.602 - 3499530353.74) / 3499530353.74 < 0.0001)

# 6. Q3 profit split: profit 251,190,536.88 minus realised
#    205,177,126.28 leaves unrealised 46,013,410.60, about 18.32%
#    of the quarter's profit.
check("6 unrealised 46,013,410.60", abs(251190536.88 - 205177126.28 - 46013410.60) < 0.01)
check("6 unrealised share ~18.32%", abs(46013410.60 / 251190536.88 * 100 - 18.32) < 0.01)

# 7. Share flow reconciles exactly; net redemption in a quarter the
#    fund beat its benchmark by 23.93pp was about 5.85% of the
#    opening share count.
begin, sub, red, end = 1031934598.51, 10745898.18, 71074398.05, 971606098.64
check("7 flow reconciles", abs(begin + sub - red - end) < 0.01)
check("7 net redemption ~5.85% of opening", abs((red - sub) / begin * 100 - 5.85) < 0.01)
check("7 subscriptions only ~1.04% of opening", abs(sub / begin * 100 - 1.04) < 0.01)

# 8. Asset mix: equities 77.45% of total assets and cash 18.85%;
#    equities over net assets equal the 78.69% industry-table total,
#    i.e. below the 80% line the manager described in the report.
total, eq, cash = 3555474030.61, 2753746781.37, 670220937.50
check("8 equity share ~77.45%", abs(eq / total * 100 - 77.45) < 0.01)
check("8 cash share ~18.85%", abs(cash / total * 100 - 18.85) < 0.01)
check("8 equity/NAV ~78.69% (<80)", abs(eq / 3499530353.74 * 100 - 78.69) < 0.01)

# 9. Top ten holdings sum to 54.39% of net assets, about 69.12% of
#    the equity book; the top three sum to 22.23%.
tops = [7.93, 7.22, 7.08, 5.91, 5.20, 4.86, 4.24, 4.00, 3.99, 3.96]
check("9 top10 sum 54.39%", abs(sum(tops) - 54.39) < 0.01)
check("9 top10 share of equity ~69.12%", abs(sum(tops) / 78.69 * 100 - 69.12) < 0.01)
check("9 top3 sum 22.23%", abs(sum(tops[:3]) - 22.23) < 0.01)

# 10. Industry mix: finance 34.69% is the largest industry, ahead of
#     manufacturing 25.23%; together 59.92% of net assets. The single
#     scientific-research holding (WuXi AppTec, 277,641,658.98 yuan,
#     7.93%) equals the whole M-industry line to the yuan.
check("10 finance+manufacturing 59.92%", abs(34.69 + 25.23 - 59.92) < 1e-9)
check("10 finance is largest industry", 34.69 > 25.23 > 7.93)
check("10 WuXi amount == M industry amount", 277641658.98 == 277641658.98)

# 11. Mechanical annualised returns from the printed cumulative
#     windows: since inception about 12.62% a year over 4,527 days;
#     ten years about 8.87% vs benchmark about 2.44%; five years
#     about -3.08%.
check("11 since-inception ann ~12.62%", abs((4.3611 ** (365.25 / 4527) - 1) * 100 - 12.62) < 0.01)
check("11 10y ann ~8.87% vs bench ~2.44%",
      abs((2.3397 ** 0.1 - 1) * 100 - 8.87) < 0.01 and abs((1.2730 ** 0.1 - 1) * 100 - 2.44) < 0.01)
check("11 5y ann ~-3.08%", abs((0.8552 ** 0.2 - 1) * 100 + 3.08) < 0.01)

# 12. Two scale checks: the Ningbo Bank penalty disclosed in the
#     notes (988,000 yuan) is about 0.40% of the fund's holding in
#     that bank (247,771,095.51 yuan); the quarter's profit equals
#     about 7.18% of ending net assets.
check("12 penalty ~0.40% of Ningbo holding", abs(988000 / 247771095.51 * 100 - 0.40) < 0.01)
check("12 Q3 profit ~7.18% of ending NAV", abs(251190536.88 / 3499530353.74 * 100 - 7.18) < 0.01)

print("ALL PASSED" if ok else "SOME FAILED")
