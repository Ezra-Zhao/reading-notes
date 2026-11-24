#!/usr/bin/env python3
"""130 Bob Male (Buffalo Small Cap Growth BUFSX) verification.
Source: Buffalo Small Cap Growth Fund Fact Sheet, September 30, 2026
(buffalofunds.com official PDF, read page by page in browser):
Inception 4/14/98 (Investor Class), performance table (annualized, Investor
Class vs Russell 2000 Growth Index), Growth of $10,000 chart values,
calendar year returns 2016-2025, portfolio characteristics (77 holdings),
top-10 holdings (as of 6/30/2026 per footnote, total 25.01%),
Fund Management: Bob Male, CFA - Manager since Inception, 37 years
experience; Craig Richard, CFA - Manager since 2023, 24 years experience.
Annualized figures are converted to cumulative with float powers; all
derived values are approximations from the printed (rounded) annual rates.
"""
from datetime import date
ok = 0
def chk(c, l):
    global ok
    assert c, l
    ok += 1; print("PASS", l)
def r2(x): return round(x + 0.0, 2)
# G1 life / tenure: manager since inception
life = (date(2026, 9, 30) - date(1998, 4, 14)).days
chk(life == 10396, "fund life 10396 days")
yrs = life / 365.25
chk(r2(yrs) == 28.46, "fund life approx 28.46 years")
chk(life == 10396, "Male tenure = full fund life (manager since inception)")
# G2 annualized table (Investor Class vs Russell 2000 Growth)
ann = [("1Y", 11.94, 12.05), ("3Y", 8.19, 17.55), ("5Y", -3.46, 4.72),
       ("10Y", 9.80, 9.90), ("15Y", 11.23, 11.94), ("20Y", 8.18, 9.09),
       ("SI", 10.56, 6.87)]
for n, f, b in ann:
    pass
exc = {n: r2(f - b) for n, f, b in ann}
chk(exc == {"1Y": -0.11, "3Y": -9.36, "5Y": -8.18, "10Y": -0.10,
            "15Y": -0.71, "20Y": -0.91, "SI": 3.69}, "annualized excess table")
# G3 win/loss count on annualized excess
chk(sum(1 for v in exc.values() if v < 0) == 6, "six windows negative excess")
chk(sum(1 for v in exc.values() if v > 0) == 1, "only SI positive excess")
chk(exc["10Y"] == -0.10, "closest window 10Y only -0.10 per year")
chk(exc["3Y"] == -9.36, "worst window 3Y -9.36 per year")
# G4 cumulative conversions
def cum(a, y): return (1 + a / 100) ** y - 1
win_y = {"1Y": 1, "3Y": 3, "5Y": 5, "10Y": 10, "15Y": 15, "20Y": 20, "SI": yrs}
exp_cum = {"1Y": (11.94, 12.05), "3Y": (26.64, 62.43), "5Y": (-16.14, 25.94),
           "10Y": (154.70, 157.03), "15Y": (393.55, 442.97),
           "20Y": (381.88, 469.77), "SI": (1641.48, 562.70)}
for n, f, b in ann:
    chk(r2(cum(f, win_y[n]) * 100) == exp_cum[n][0], f"cumulative fund {n}")
    chk(r2(cum(b, win_y[n]) * 100) == exp_cum[n][1], f"cumulative index {n}")
# G5 $10,000 endpoints (recomputed approx vs printed chart 174,277 / 66,730)
chk(r2(10000 * (1 + cum(9.80, 10))) == 25469.67, "10k 10Y fund approx 25469.67")
chk(r2(10000 * (1 + cum(9.90, 10))) == 25702.59, "10k 10Y index approx 25702.59")
chk(r2(10000 * (1 + cum(8.18, 20))) == 48188.07, "10k 20Y fund approx 48188.07")
chk(r2(10000 * (1 + cum(9.09, 20))) == 56976.90, "10k 20Y index approx 56976.90")
chk(abs(10000 * (1 + cum(10.56, yrs)) - 174277) / 174277 < 0.001, "10k SI fund recomputed within 0.1 pct of printed 174277")
chk(abs(10000 * (1 + cum(6.87, yrs)) - 66730) / 66730 < 0.01, "10k SI index recomputed within 1 pct of printed 66730")
# G6 segment SI minus 20Y (first approx 8.46 years)
def seg(long_a, long_y, short_a, short_y):
    return ((1 + long_a / 100) ** long_y / (1 + short_a / 100) ** short_y - 1) * 100
chk(r2(seg(10.56, yrs, 8.18, 20)) == 261.39, "first segment fund +261.39")
chk(r2(seg(6.87, yrs, 9.09, 20)) == 16.31, "first segment index +16.31")
# G7 middle segments
chk(r2(seg(8.18, 20, 11.23, 15)) == -2.36, "20Y-minus-15Y fund -2.36")
chk(r2(seg(9.09, 20, 11.94, 15)) == 4.93, "20Y-minus-15Y index +4.93")
chk(r2(seg(11.23, 15, 9.80, 10)) == 93.78, "15Y-minus-10Y fund +93.78")
chk(r2(seg(11.94, 15, 9.90, 10)) == 111.25, "15Y-minus-10Y index +111.25")
chk(r2(seg(9.80, 10, -3.46, 5)) == 203.73, "10Y-minus-5Y fund +203.73")
chk(r2(seg(9.90, 10, 4.72, 5)) == 104.09, "10Y-minus-5Y index +104.09")
# G8 recent segments
chk(r2(seg(-3.46, 5, 8.19, 3)) == -33.78, "5Y-minus-3Y fund -33.78")
chk(r2(seg(4.72, 5, 17.55, 3)) == -22.47, "5Y-minus-3Y index -22.47")
chk(r2(seg(8.19, 3, 11.94, 1)) == 13.13, "3Y-minus-1Y fund +13.13")
chk(r2(seg(17.55, 3, 12.05, 1)) == 44.96, "3Y-minus-1Y index +44.96")
# G9 2026 split: YTD cumulative split by Q3 (3 Mo)
h1f = (1 + 11.64 / 100) / (1 - 7.58 / 100) - 1
h1b = (1 + 10.71 / 100) / (1 - 9.39 / 100) - 1
chk(r2(h1f * 100) == 20.80, "implied H1 2026 fund +20.80")
chk(r2(h1b * 100) == 22.18, "implied H1 2026 index +22.18")
chk(r2((-7.58) - (-9.39)) == 1.81, "Q3 2026 fund fell 1.81 pp less than index")
# G10 calendar years 2016-2025
fcal = [6.22, 27.07, -5.78, 40.97, 66.36, 4.85, -30.01, 5.45, 5.38, -0.13]
ical = [11.32, 22.17, -9.31, 28.48, 34.63, 2.83, -26.36, 18.66, 15.15, 13.01]
chk(sum(1 for a, b in zip(fcal, ical) if a > b) == 5, "calendar wins 5 of 10")
chk(sum(1 for a, b in zip(fcal, ical) if a < b) == 5, "calendar losses 5 of 10")
chk(sum(1 for a in fcal if a < 0) == 3, "fund negative calendar years 3")
chk(sum(1 for a in ical if a < 0) == 2, "index negative calendar years 2")
chk(r2(fcal[4] - ical[4]) == 31.73, "best calendar gap 2020 +31.73")
# G11 holdings shape (top-10 as of 6/30/2026 per fact sheet footnote)
top10 = [3.02, 3.02, 2.84, 2.74, 2.43, 2.34, 2.32, 2.14, 2.10, 2.06]
chk(r2(sum(top10)) == 25.01, "top10 sum 25.01 pct")
chk(max(top10) == 3.02, "largest holding 3.02 pct (two names tied)")
# G12 recovery math
chk(r2((1 / (1 - 7.58 / 100) - 1) * 100) == 8.20, "Q3 -7.58 needs +8.20 to recover")
chk(r2((1 / (1 + cum(-3.46, 5)) - 1) * 100) == 19.25, "5Y cumulative -16.14 needs +19.25 to recover")
print("TOTAL", ok, "assertions passed")
