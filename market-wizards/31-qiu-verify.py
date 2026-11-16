#!/usr/bin/env python3
"""Verify arithmetic for note 31 (Qiu Dongrong). Inputs from public
sources cited in the note: Zhonggeng Value Pilot 2024 annual report
(fund inception, manager tenure and bio, NAV table, AUM table,
shareholder list, company AUM), Zhonggeng fund-manager change
announcements Jul-2024, Wind figures carried by multiple secondary
reports for the HSBC Jinxin period and for his five-fund AUM in
2024 Q1/Q2, and secondary reports of Zhonggeng company AUM peaks."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Tenure on Value Pilot: 2018-12-19 (inception, first manager) to 2024-07-19
d0, d1 = date(2018, 12, 19), date(2024, 7, 19)
assert (d1 - d0).days == 2039, (d1 - d0).days
assert d1.year - d0.year == 6 and (d1.month - d0.month) == -5  # 5 years 7 months net
print("1 tenure OK 2018-12-19 to 2024-07-19 = 2039 days = 5y7m")

# 2. Cumulative return vs NAV: no distributions since inception, NAV 2.2107
assert close(1 + 121.07 / 100, 2.2107, 0.0001)
print("2 cumulative OK 1+121.07% = 2.2107 = end-2024 NAV (no distributions)")

# 3. Three calendar years chain vs reported past-3y figure
chain = 1.0485 * (1 - 0.0384) * 1.0114 - 1
assert close(chain * 100, 1.98, 0.02), chain
nav21 = 2.2729 / 1.0485
assert close((2.2107 / nav21 - 1) * 100, 1.98, 0.02)
print("3 3y chain OK 2022 +4.85% / 2023 -3.84% / 2024 +1.14% compounds to +1.97% vs reported past-3y +1.98%")

# 4. Value Pilot AUM path (annual report, RMB bn): 2022 11.6631, 2023 8.5289, 2024 2.7419 (x10bn units below in yi)
aum22, aum23, aum24 = 116.6307503692, 85.2892258017, 27.4189491360
assert close((aum23 / aum22 - 1) * 100, -26.87, 0.02)
assert close((aum24 / aum23 - 1) * 100, -67.85, 0.02)
assert close((aum24 / aum22 - 1) * 100, -76.49, 0.02)
print("4 AUM OK 116.63 -> 85.29 (-26.87%) -> 27.42 (-67.85%); two-year -76.49%")

# 5. 2024 shrinkage is redemption, not NAV loss: shares 39.0219 -> 12.4029 (yi shares), NAV +1.14%
sh23, sh24 = 39.0218911833, 12.4029173703
drop_sh = sh24 / sh23 - 1
assert close(drop_sh * 100, -68.22, 0.02), drop_sh
recon = (1 + drop_sh) * 1.0114 - 1
assert close(recon * 100, -67.85, 0.03), recon
print("5 redemption OK shares -68.22% in 2024; (1-68.22%)*(1+1.14%)-1 = -67.86% vs AUM -67.85%")

# 6. HSBC Jinxin Large-Cap tenure return (Wind via secondary reports): +193.86%, Sep-2014 to Apr-2018
fac = 1 + 193.86 / 100
assert close(fac, 2.9386, 0.0001)
years = 43 / 12
ann = fac ** (1 / years) - 1
assert close(ann * 100, 34.73, 0.6), ann
print("6 HSBC OK +193.86% = 2.9386x over ~43 months, mechanical ann ~", round(ann * 100, 2), "% vs reported 34.69/34.73% (date-precision gap)")

# 7. His five funds at departure window (secondary, Wind): Q1-2024 198.54 -> Q2-2024 147.08 (yi RMB)
assert close((147.08 / 198.54 - 1) * 100, -25.92, 0.02)
assert close(198.54 - 147.08, 51.46, 0.001)
assert close(147.08 / 189.72 * 100, 77.52, 0.01)
print("7 five-fund OK 198.54 -> 147.08 = -51.46 (-25.92%) in Q2-2024; 147.08/189.72 company = 77.52%")

# 8. Company AUM: end-2024 136.45 (annual report) vs Q2-2024 189.72; mid-2026 98.03 vs two peak claims
assert close((136.45 / 189.72 - 1) * 100, -28.08, 0.02)
assert close((98.03 / 413.55 - 1) * 100, -76.30, 0.02)
assert close((98.03 / 371.0 - 1) * 100, -73.58, 0.02)
assert close(27.4189491360 / 136.45 * 100, 20.09, 0.02)
print("8 company OK end-2024 136.45 vs Q2 189.72 = -28.08%; mid-2026 98.03 vs peak 413.55 = -76.30%, vs peak 371 = -73.58% (parallel); Value Pilot = 20.09% of company end-2024")

# 9. Performance gaps from the annual-report table
assert close(1.14 - 13.52, -12.38, 0.001)
assert close(-9.28 - (-0.25), -9.03, 0.001)
assert close(70.45 - 9.08, 61.37, 0.001)
ann5 = 1.7045 ** 0.2 - 1
assert close(ann5 * 100, 11.25, 0.05), ann5
print("9 gaps OK 2024 +1.14% vs bench +13.52% = -12.38pp; Q4 -9.28% vs -0.25% = -9.03pp; 5y +70.45% vs +9.08% = +61.37pp, 5y ann ~11.25%")

# 10. Inception-to-2024 annualized (mechanical, 2204 days)
days = (date(2024, 12, 31) - d0).days
assert days == 2204, days
ann_inc = 2.2107 ** (365.25 / days) - 1
assert close(ann_inc * 100, 14.06, 0.1), ann_inc
print("10 inception ann OK 2204 days, NAV 2.2107 -> mechanical ann ~", round(ann_inc * 100, 2), "%")

# 11. Shareholder list in the annual report sums to 100%; Qiu holds 9.73%
total = 33.25 + 23.75 + 18.05 + 9.73 + 4.74 + 3.80 + 2.39 + 2.39 + 1.90
assert close(total, 100.00, 0.001), total
print("11 shareholders OK nine holders sum to 100.00%; Qiu Dongrong 9.73% (4th largest)")

# 12. Career span at departure: securities work from 2008, 16 years per 2024 annual report
assert 2024 - 2008 == 16
print("12 career OK 2008 start -> 16 years at 2024 report, matches bio line")

print("ALL PASS")
