#!/usr/bin/env python3
"""Verify arithmetic for note 33 (Liu Gesong). Inputs from public
sources cited in the note: GF Shuangqing Upgrade 2019 annual report
(EY-audited, dfcfw reprint), 2022 annual report (Wind reprint),
2024 annual report (cninfo) via Sina full-table reprint, manager-change
announcements (2017-06-17 industry-leading; 2025-12-24 small-cap growth
resignation), China Securities Journal Wind tables (2019 top-3;
2021-08 scale ranking), Longbridge/Zhitong summary of GF Innovation
Upgrade 2026 Q3 report."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. 2019 triple crown (Wind via CS Journal 2020-01-18): all three above 100%
r = [121.69, 110.37, 106.58]
assert all(x > 100 for x in r)
assert close(r[0] - r[1], 11.32, 0.01)
assert close(r[1] - r[2], 3.79, 0.01)
print("1 triple OK 121.69 / 110.37 / 106.58 all >100%; gaps 11.32 / 3.79 pp")

# 2. Shuangqing 2019 self-consistency (2019 annual report)
assert close(0.9830 * (1 + 1.2169), 2.1792, 0.001)
assert close(121.69 - 28.29, 93.40, 0.01)
print("2 2019 OK 0.9830 x 2.2169 = 2.1792 unit NAV; excess over benchmark = 93.40 pp")

# 3. 2019 money flow (2019 annual report equity-change table)
sub, red = 8_546_015_780.96, 2_290_679_896.45
assert close(sub - red, 6_255_335_884.51, 0.01)
assert close(6_873_215_887.36 / 85_025_338.28, 80.84, 0.01)
print("3 flow OK subscriptions 85.46 - redemptions 22.91 = net inflow 62.55 (100M CNY); year-end assets 68.73 vs 0.85 = 80.84x")

# 4. Cumulative chain 2020-2021 (annual-report growth rates A class)
f19 = 0.9830 * (1 + 1.2169)
f20 = f19 * (1 + 0.6636)
f21 = f20 * (1 + 0.0441)
assert close((f20 - 1) * 100, 262.54, 0.02)   # reported 262.54%
assert close((f21 - 1) * 100, 278.53, 0.02)   # reported 278.53%
print("4 chain OK cum factor 2020 = 3.6254 (262.54%), 2021 = 3.7853 (278.53%), both match annual reports within rounding")

# 5. Drawdown chain 2022-2024 compounds to the reported past-3y figure
comp = (1 - 0.2390) * (1 - 0.3253) * (1 + 0.0356) - 1
assert close(comp * 100, -46.82, 0.02)        # 2024 annual report: past 3y -46.82%
f24 = f21 * (1 + comp)
assert close((f24 - 1) * 100, 101.28, 0.02)   # reported since-inception 101.28%
print("5 drawdown OK 2022 -23.90% x 2023 -32.53% x 2024 +3.56% = -46.82% (matches report); since-inception factor 2.0128 (101.28%)")

# 6. Recovery arithmetic from end-2024 back to end-2021 peak factor
assert close((f21 / f24 - 1) * 100, 88.07, 0.02)
f23 = f21 * (1 - 0.2390) * (1 - 0.3253)
assert close((f21 / f23 - 1) * 100, 94.76, 0.02)
print("6 recovery OK end-2024 factor needs +88.07% to regain end-2021 peak; end-2023 trough needed +94.76%")

# 7. 2024 balance sheet (2024 annual report via Sina reprint)
assert close(54.24 + 2.46, 56.70, 0.01)
assert close((56.70 / 68.7321588736 - 1) * 100, -17.51, 0.02)
print("7 2024 assets OK A 54.24 + C 2.46 = 56.70 (100M CNY), -17.51% vs 2019 year-end 68.73")

# 8. Tenure day counts (announcements / annual report)
assert (date(2025, 12, 24) - date(2017, 6, 19)).days == 3110
assert (date(2024, 12, 31) - date(2018, 11, 2)).days == 2251
assert (date(2014, 9, 1) - date(2013, 8, 23)).days == 374
print("8 tenure OK small-cap growth 2017-06-19 to 2025-12-24 = 3,110 days (~8.5y); Shuangqing inception to 2024-end = 2,251 days; first fund (Zhongyou Core Growth) = 374 days")

# 9. Scale context 2021 (Wind via CS Journal 2021-08-24)
assert 750 + 150 == 900
print("9 scale OK mid-2021 AUM >75.0bn CNY (No.4 active-equity); +15.0bn capped new fund = >90.0bn, No.3 behind Zhang Kun / Liu Yanchun")

# 10. 2026 Q3 Innovation Upgrade (Q3 report via Longbridge/Zhitong)
assert close(-34.15 - (-6.99), -27.16, 0.01)
print("10 2026Q3 OK Innovation Upgrade -34.15% vs benchmark -6.99% = -27.16 pp; equity position 93.32%")

print("ALL PASS")
