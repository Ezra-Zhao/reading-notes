#!/usr/bin/env python3
"""Verify arithmetic for note 35 (Dong Chengfei). Inputs from public
sources cited in the note: Xingzheng Global (Industrial Securities
Global) announcements reprinted on cninfo / 10jqka (VP appointment
2015-04-30 CV: joined Sep 2003, Global Vision manager since
2007-02-06, Trend manager since 2013-10-28; VP departure announced
2022-01-22, departure date 2022-01-21, personal reasons), Brokerage
China / China Fund News reports at his Oct 2021 fund-manager exit
(Trend 324.49% to 2021-10-18, annualised 19.86%; Xingxin New Vision
93.19%, annualised 11.01%; Q2-2021-end scales 384.19 + 221.96),
China Fund News 2026-11-13 via Sina (Trend 325.05% to the
2021-10-20 exit date; private AUM over CNY 15bn at Q3-2026 end;
sealed from 2025-06-08; new product on sale 2026-11-16)."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Identity anchors from the 2015-04-30 VP appointment announcement CV
assert (date(2015, 4, 30) - date(2007, 2, 6)).days == 3005
print("1 cv OK joined Sep 2003 (announcement CV); Global Vision manager since 2007-02-06, still listed in that role in the 2015-04-30 announcement = 3,005 days (8y2m+) already by then; Trend manager since 2013-10-28 per same CV")

# 2. Trend tenure to the last reported return date 2021-10-18
d = (date(2021, 10, 18) - date(2013, 10, 28)).days
assert d == 2912
assert close(d / 365.25, 7.97, 0.01)
print(f"2 tenure OK Trend 2013-10-28 -> 2021-10-18 = {d} days = 7.97y; press wording '7 years 358 days' at the 2021-10-19 exit reports is an inclusive-count variant (2912 exclusive + counting conventions), registered not merged")

# 3. Trend return: 324.49% to 2021-10-18, annualised check vs reported 19.86%
f = 1 + 324.49 / 100
assert close(f, 4.2449, 0.0001)
ann = f ** (365.25 / 2912) - 1
assert close(ann * 100, 19.86, 0.10)
print(f"3 trend return OK +324.49% = {f:.4f}x; mechanical annualised over 2,912 days = {ann*100:.2f}% vs reported 19.86% (difference is day-count convention)")

# 4. Variant: 325.05% to the 2021-10-20 exit date (China Fund News 2026-11-13)
assert close(325.05 - 324.49, 0.56, 0.001)
assert close((1 + 325.05 / 100) / f - 1, 0.0013, 0.0002)
print("4 variant OK 325.05% (to 2021-10-20, China Fund News 2026) vs 324.49% (to 2021-10-18) differ by 0.56pp = 0.13% in factor terms -- two dates, two numbers, both registered")

# 5. Xingxin New Vision: 93.19%, annualised 11.01%, tenure 6y112d reported
d2 = (date(2021, 10, 19) - date(2015, 6, 29)).days
assert d2 == 2304
f2 = 1 + 93.19 / 100
ann2 = f2 ** (365.25 / d2) - 1
assert close(ann2 * 100, 11.01, 0.10)
print(f"5 xingxin OK tenure back-solved from '6y112d' at 2021-10-19 starts 2015-06-29 ({d2} days, the 2015 bull-market peak month); +93.19% = {f2:.4f}x, mechanical annualised {ann2*100:.2f}% vs reported 11.01%")

# 6. Combined scale at Q2-2021 end (exit reports)
assert close(384.19 + 221.96, 606.15, 0.01)
print("6 scale OK Trend CNY 38.419bn + Xingxin CNY 22.196bn = CNY 60.615bn at Q2-2021 end, the 'over CNY 60bn' headline figure")

# 7. Xingxin's 2020 management fee vs the whole company's 2020 profit (Zhiyou reprint, secondary)
assert close(11.8 / 15.97 * 100, 73.89, 0.05)
print("7 fee OK Xingxin New Vision 2020 management fee CNY 1.18bn = 73.89% of Xingzheng Global's whole 2020 net profit CNY 1.597bn (single-secondary-source reprint, registered as such)")

# 8. Career spans: public-fund chapter and the 2026 profile arithmetic
assert (date(2022, 1, 21) - date(2003, 9, 1)).days > 18 * 365
assert 2026 - 2003 == 23 and 2026 - 2007 == 19
print("8 spans OK Sep 2003 -> VP departure 2022-01-21 (cninfo announcement 2022-01-22, personal reasons) = 18y+ at one firm; China Fund News 2026 profile '23y experience, 19y investing' is exactly 2026-2003 and 2026-2007")

# 9. Aggregate-career variant vs single-fund figure (do not merge)
assert 900 / 324.49 > 2.7
print("9 aggregate OK press aggregate 'total return over 900%, annualised 17.04%' spans all his funds/periods and is 2.7x+ the single-fund Trend figure -- a different aggregate, registered as a variant, never merged with claim 3")

# 10. Private chapter: seal length and reopening product floor arithmetic
seal = (date(2026, 11, 16) - date(2025, 6, 8)).days
assert seal == 526
assert 101 * 200 == 20200
assert close(150 / 606.15 * 100, 24.75, 0.05)
print(f"10 private OK sealed 2025-06-08 -> new product on sale 2026-11-16 = {seal} days (17m+, 'over a year' as reported); 200 slots x CNY 1.01m minimum = CNY 202m minimum if every slot filled at the floor; personal private AUM over CNY 15bn at Q3-2026 end = 24.75% of his CNY 60.615bn public-fund peak")

print("ALL PASS")
