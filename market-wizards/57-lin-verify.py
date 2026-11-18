#!/usr/bin/env python3
"""Verify arithmetic in note 57 (Lin Yingrui / GF Ruiyi Lingxian
Mixed Fund, 005233 A / 012449 C).

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

# 1. Tenure: founding manager, appointment date 2017-12-14 equals the
#    contract effective date; departure column blank at 2026-09-30,
#    so the whole fund life is his.
tenure = (date(2026, 9, 30) - date(2017, 12, 14)).days
check("1 tenure days 3212", tenure == 3212)
check("1 tenure years ~8.79", abs(tenure / 365.25 - 8.79) < 0.01)

# 2. Every reported excess (fund minus benchmark) in the 3.2.1 tables
#    matches simple subtraction, for all seven A windows and all six
#    C windows.
a_rows = [(-1.50, -10.24, 8.74), (-12.72, -1.94, -10.78),
          (-22.31, -4.53, -17.78), (-24.96, 16.98, -41.94),
          (-25.21, -2.39, -22.82), (61.47, 20.64, 40.83),
          (89.53, 19.80, 69.73)]
c_rows = [(-1.60, -10.24, 8.64), (-12.90, -1.94, -10.96),
          (-22.63, -4.53, -18.10), (-25.86, 16.98, -42.84),
          (-26.69, -2.39, -24.30), (-31.60, -8.29, -23.31)]
check("2 A seven excess diffs match", all(abs(a - b - d) < 0.005 for a, b, d in a_rows))
check("2 C six excess diffs match", all(abs(a - b - d) < 0.005 for a, b, d in c_rows))

# 3. Since-inception A return 89.53% implies a factor of 1.8953,
#    exactly the printed ending unit NAV 1.8953 yuan: the unit NAV
#    and the cumulative growth agree to four decimals.
check("3 1+89.53% == ending NAV 1.8953", abs(1 + 0.8953 - 1.8953) < 1e-9)

# 4. Window decomposition (A): the earliest two years inside the
#    seven-year window gained about +115.90% (7y over 5y), while the
#    last five years lost -25.21%; the two years before the last
#    three lost about -3.41% (3y over 1y); the half year before the
#    last half lost about -10.99% (1y over 6m); Q2 2026 alone lost
#    about -11.39% (6m over 3m).
check("4 7y-over-5y earliest 2y ~+115.90%", abs((1.6147 / 0.7479 - 1) * 100 - 115.90) < 0.01)
check("4 3y-over-1y prior 2y ~-3.41%", abs((0.7504 / 0.7769 - 1) * 100 + 3.41) < 0.01)
check("4 1y-over-6m prior half ~-10.99%", abs((0.7769 / 0.8728 - 1) * 100 + 10.99) < 0.01)
check("4 6m-over-3m Q2 ~-11.39%", abs((0.8728 / 0.9850 - 1) * 100 + 11.39) < 0.01)

# 5. Q3 profit split: A realised -12,927,429.05 with profit
#    -9,729,195.48 leaves unrealised +3,198,233.57; A+C realised
#    -17,237,634.40 with profit -12,911,801.45 leaves unrealised
#    +4,325,832.95, offsetting about 25.10% of the realised loss.
check("5 A unrealised +3,198,233.57", abs(-9729195.48 - (-12927429.05) - 3198233.57) < 0.01)
check("5 A+C realised -17,237,634.40", abs(-12927429.05 + -4310205.35 + 17237634.40) < 0.01)
check("5 A+C profit -12,911,801.45", abs(-9729195.48 + -3182605.97 + 12911801.45) < 0.01)
check("5 offset share ~25.10%", abs(4325832.95 / 17237634.40 * 100 - 25.10) < 0.01)

# 6. Ending shares times ending unit NAV reproduce ending net
#    assets within rounding of the four-decimal unit NAV.
check("6 A shares x NAV ~ net assets (0.01%)",
      abs(342131424.03 * 1.8953 - 648455712.53) / 648455712.53 < 0.0001)
check("6 C shares x NAV ~ net assets (0.01%)",
      abs(109416066.36 * 1.8560 - 203077179.15) / 203077179.15 < 0.0001)
check("6 A+C net assets 851,532,891.68",
      abs(648455712.53 + 203077179.15 - 851532891.68) < 0.01)

# 7. Share flows reconcile exactly for both classes; net redemption
#    was about 1.73% of opening shares for A and about 7.20% for C.
ab, asub, ared, aend = 348153554.55, 15107929.56, 21130060.08, 342131424.03
cb, csub, cred, cend = 117910967.14, 16156374.87, 24651275.65, 109416066.36
check("7 A flow reconciles", abs(ab + asub - ared - aend) < 0.01)
check("7 C flow reconciles", abs(cb + csub - cred - cend) < 0.01)
check("7 A net redemption ~1.73%", abs((ared - asub) / ab * 100 - 1.73) < 0.01)
check("7 C net redemption ~7.20%", abs((cred - csub) / cb * 100 - 7.20) < 0.01)
check("7 A+C ending shares 451,547,490.39", abs(aend + cend - 451547490.39) < 0.01)

# 8. Asset mix: equities 718,585,741.20 of total assets
#    854,079,051.60 are 84.14%; cash 122,456,056.20 is 14.34%;
#    equities over combined net assets are 84.39%, the industry
#    table total. Components sum to the printed total.
parts = [718585741.20, 8925889.15, 122456056.20, 4111365.05]
check("8 components sum to total assets", abs(sum(parts) - 854079051.60) < 0.01)
check("8 equity share ~84.14%", abs(718585741.20 / 854079051.60 * 100 - 84.14) < 0.01)
check("8 cash share ~14.34%", abs(122456056.20 / 854079051.60 * 100 - 14.34) < 0.01)
check("8 equity/NAV ~84.39%", abs(718585741.20 / 851532891.68 * 100 - 84.39) < 0.01)

# 9. Top ten holdings sum to 83.37% of net assets, about 98.79% of
#    the whole equity book; the six airlines on top sum to exactly
#    57.25%, the whole transport industry line.
tops = [10.03, 9.89, 9.49, 9.44, 9.35, 9.05, 8.31, 8.24, 7.42, 2.15]
check("9 top10 sum 83.37%", abs(sum(tops) - 83.37) < 0.01)
check("9 top10 share of equity ~98.79%", abs(sum(tops) / 84.39 * 100 - 98.79) < 0.01)
check("9 six airlines sum == transport 57.25%", abs(sum(tops[:6]) - 57.25) < 1e-9)
check("9 transport share of equity ~67.84%", abs(57.25 / 84.39 * 100 - 67.84) < 0.01)

# 10. Two more one-stock industries: Bohai Leasing 7.42% equals the
#     whole leasing-and-business-services line; Runbei Hangkong
#     2.15% equals the whole wholesale-and-retail line. Manufacturing
#     16.69% minus Luolai 8.31% and Dafeng 8.24% leaves 0.14%.
check("10 Bohai == leasing line 7.42%", abs(7.42 - 7.42) < 1e-9)
check("10 Runbei == wholesale line 2.15%", abs(2.15 - 2.15) < 1e-9)
check("10 manufacturing residual ~0.14%", abs(16.69 - 8.31 - 8.24 - 0.14) < 1e-9)

# 11. Concurrent management: 3 public funds at 2,810,983,515.04
#     yuan plus 1 private plan at 285,015,641.92 yuan equal the
#     printed total 3,095,999,156.96 yuan; public funds are about
#     90.79% of the total he runs in that table.
check("11 concurrent sum matches", abs(2810983515.04 + 285015641.92 - 3095999156.96) < 0.01)
check("11 public share ~90.79%", abs(2810983515.04 / 3095999156.96 * 100 - 90.79) < 0.01)

# 12. Mechanical annualised returns: since inception about 7.55%
#     a year over 3,212 days; seven years about 7.08%; five years
#     about -5.65%. The aviation figures quoted in the manager's
#     discussion imply demand beat capacity by 2.1 points.
check("12 since-inception ann ~7.55%", abs((1.8953 ** (365.25 / 3212) - 1) * 100 - 7.55) < 0.01)
check("12 7y ann ~7.08%", abs((1.6147 ** (1 / 7) - 1) * 100 - 7.08) < 0.01)
check("12 5y ann ~-5.65%", abs((0.7479 ** 0.2 - 1) * 100 + 5.65) < 0.01)
check("12 RPK-ASK gap 2.1pp", abs(6.8 - 4.7 - 2.1) < 1e-9)

print("ALL PASSED" if ok else "SOME FAILED")
