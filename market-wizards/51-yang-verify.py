#!/usr/bin/env python3
"""Verify arithmetic in note 51 (Yang Ruiwen / Invesco Great Wall Select 260101).
All inputs are figures stated in the note's cited sources (the fund's
2026 Q2 report; Eastmoney manager profile snapshot ~2026-07-24; Sina
2026-10-28 piece carrying the 2026 Q3 top-10 and the 2026-10-27 NAV
snapshot). This script only checks internal arithmetic consistency.
Clean-room, self-written.
"""
from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure: appointed 2014-10-25 (Q2 report sec.4.1). To 2026-09-30
#    is 4,358 days (11 years + 340 days); 2026-10-25 completes 12
#    years = 4,383 days = 12*365 + 3 leap days (2016/2020/2024).
check("1 days to 2026-09-30 = 4358", (date(2026, 9, 30) - date(2014, 10, 25)).days == 4358)
check("1 11y + 340d", (date(2025, 10, 25) - date(2014, 10, 25)).days + 340 == 4358)
check("1 12y span 4383d", (date(2026, 10, 25) - date(2014, 10, 25)).days == 12 * 365 + 3)

# 2. Q2-end identity: NAV per share 5.5944 x shares 584,566,945.09
#    reproduces net assets 3,270,314,122.93 within NAV rounding
#    (4-decimal NAV; residual 12,805.32 on 3.27bn).
prod = 5.5944 * 584566945.09
check("2 NAV x shares within rounding", abs(prod - 3270314122.93) < 20000 and abs(prod / 3270314122.93 - 1) < 1e-5)

# 3. Q2 report performance table: excess (fund minus benchmark) must
#    equal the report's own (1)-(3) column in all eight windows.
rows = [(22.94, 11.18, 11.76), (23.29, 9.38, 13.91), (38.47, 26.39, 12.08),
        (52.34, 31.41, 20.93), (26.55, 8.88, 17.67), (171.20, 43.10, 128.10),
        (245.12, 49.59, 195.53), (2612.19, 275.76, 2336.43)]
check("3 eight excess windows match report", all(abs(g - b - e) < 0.005 for g, b, e in rows))
check("3 since-inception factor 27.1219x", abs((1 + 26.1219) - 27.1219) < 1e-9)

# 4. Q2 profit split: total profit 651,291,225.22 minus realised
#    321,725,710.88 leaves unrealised 329,565,514.34 = 50.60%.
unreal = 651291225.22 - 321725710.88
check("4 unrealised 329,565,514.34", abs(unreal - 329565514.34) < 0.01)
check("4 unrealised share 50.60%", abs(unreal / 651291225.22 * 100 - 50.60) < 0.01)

# 5. Q2 share flows: 650,903,563.73 + 26,119,344.23 - 92,455,962.87
#    = 584,566,945.09; net redemption 66,336,618.64 = 10.19% of start.
check("5 flow identity", abs(650903563.73 + 26119344.23 - 92455962.87 - 584566945.09) < 0.01)
check("5 net redemption 10.19% of start", abs((92455962.87 - 26119344.23) / 650903563.73 * 100 - 10.19) < 0.01)

# 6. Q2-end mix: stocks 2,494,079,082.35 = 75.80% of total assets and
#    76.26% of NAV (contract band 70-80%); bonds 666,871,577.32 all
#    treasury = 20.39% of NAV; manufacturing 68.15% of NAV.
check("6 stocks/total 75.80%", abs(2494079082.35 / 3290280309.06 * 100 - 75.80) < 0.01)
check("6 stocks/NAV 76.26%", abs(2494079082.35 / 3270314122.93 * 100 - 76.26) < 0.01)
check("6 bonds/NAV 20.39%", abs(666871577.32 / 3270314122.93 * 100 - 20.39) < 0.01)
check("6 manufacturing/NAV 68.15%", abs(2228671643.56 / 3270314122.93 * 100 - 68.15) < 0.01)

# 7. Q2 top-10 weights sum to 48.17% of NAV = 63.17% of the stock book.
q2 = [8.09, 7.03, 6.60, 4.92, 4.12, 4.11, 3.86, 3.46, 3.20, 2.78]
check("7 Q2 top10 sum 48.17", abs(sum(q2) - 48.17) < 1e-9)
check("7 top10 = 63.17% of stocks", abs(sum(q2) / 76.26 * 100 - 63.17) < 0.01)

# 8. Q3 top-10 (per latest periodic report via Sina) sums to 43.32%,
#    4.85pp below Q2; six continuing names by share count: five cuts,
#    one add (Aiko Solar +8.81%; GCL Gas -12.47% shown as Guanggang).
q3 = [6.28, 5.22, 4.83, 4.76, 4.51, 3.80, 3.80, 3.59, 3.30, 3.23]
check("8 Q3 top10 sum 43.32", abs(sum(q3) - 43.32) < 1e-9)
check("8 concentration -4.85pp", abs(sum(q3) - sum(q2) + 4.85) < 1e-9)
chg = [("segway-ninebot", 6023812, 4789651, -20.49), ("guanggang-gas", 5078961, 4445634, -12.47),
       ("shennan", 471300, 342200, -27.39), ("sankeshu", 5595086, 4743606, -15.22),
       ("mgi", 2215042, 1494654, -32.52), ("aiko", 11743884, 12778384, 8.81)]
check("8 six continuing share changes", all(abs((b / a - 1) * 100 - e) < 0.01 for _, a, b, e in chg))

# 9. Q3-end net assets implied two ways from top-10 value/weight
#    (Wangsu 93,531,800 / 3.30%; Terruide 91,334,100 / 3.23%) both land
#    near RMB 2.83bn, about 13.3% below Q2-end 3.270bn (estimate only,
#    weights are 2-decimal rounded).
imp1, imp2 = 93531800 / 0.0330, 91334100 / 0.0323
check("9 two implied NAVs agree within 0.3%", abs(imp1 / imp2 - 1) < 0.003)
check("9 implied NAV ~ -13.3% vs Q2", abs(((imp1 + imp2) / 2 / 3270314122.93 - 1) * 100 + 13.33) < 0.15)

# 10. Tenure-return snapshots: Eastmoney ~2026-07-24 +353.04% (factor
#     4.5304, 11.75y, mechanical CAGR ~13.73%); Sina 2026-10-27
#     +307.03% (factor 4.0703); snapshot-to-snapshot move ~ -10.16%.
yrs_jul = (date(2026, 7, 24) - date(2014, 10, 25)).days / 365.25
check("10 Jul factor 4.5304, CAGR ~13.73%", abs(4.5304 ** (1 / yrs_jul) * 100 - 113.73) < 0.05)
check("10 snapshot move -10.16%", abs((4.0703 / 4.5304 - 1) * 100 + 10.16) < 0.01)

# 11. Current-fund scale: the 13 share classes on the profile page sum
#     to RMB 19.394bn vs the page's stated total 19.395bn (0.01 rounding).
funds = [1.74, 0.56, 16.58, 23.38, 16.08, 1.99, 12.38, 18.29, 6.40, 8.92, 21.89, 33.03, 32.70]
check("11 classes sum 193.94 vs stated 193.95", abs(sum(funds) - 193.94) < 1e-9 and abs(193.95 - sum(funds) - 0.01) < 1e-9)

# 12. Second long fund: Environmental Advantage since 2016-03-15,
#     +344.60% at the Jul snapshot = factor 4.4460 over 3,783 days
#     (~10.36y), mechanical CAGR ~15.49%.
yrs_env = (date(2026, 7, 24) - date(2016, 3, 15)).days / 365.25
check("12 env span 3783d", (date(2026, 7, 24) - date(2016, 3, 15)).days == 3783)
check("12 env CAGR ~15.49%", abs(4.4460 ** (1 / yrs_env) * 100 - 115.49) < 0.05)

print("ALL PASSED" if ok else "SOME FAILED")
