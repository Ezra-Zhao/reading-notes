#!/usr/bin/env python3
"""Verify arithmetic for note 37 (Liu Yanchun). Inputs from public
sources cited in the note: China Securities Journal 2021-04-26
(Wind: AUM CNY 101.58bn at end of Q1 2021, second CNY-100bn active
equity manager after Zhang Kun); Sina Finance 2026-11-07 (Pengpai
report on co-manager additions + Sina fund data table: flagship
tenure return 95.33% vs peer 75.46% since 2015-04-09, holder P/L
-8.544bn and fees 3.076bn for 2015H2-2026H1, eight products total
-13.891bn / 6.111bn; CV: joined Invesco Great Wall Jan 2015, VP
2021-03-29 to 2025-09-18, 23 years experience); CLS 2026-11-07
(flagship AUM CNY 11.027bn = over half of total 21.881bn, solo AUM
1.651bn, only Jiyou Chengzhang left solo); 10jqka 2026-10-29
(11 share classes summing to 21.882bn at 2026-09-30, flagship A
10.947bn + C 0.080bn, all 11 classes negative YTD)."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Peak to now: AUM decline
peak, now = 1015.8, 218.81
assert close(peak - now, 796.99, 0.01) and close((peak - now) / peak * 100, 78.46, 0.01)
print("1 peak OK Q1-2021 AUM 1015.8 -> Q3-2026 218.81 = -796.99bn CNY, -78.46%; remaining is 21.54% of peak")

# 2. Flagship A + C equals the CLS fund total
assert close(109.47 + 0.80, 110.27, 0.001)
print("2 flagship OK A class 109.47 + C class 0.80 = 110.27, exactly the CLS figure for the whole fund -- the two reports differ by share-class scope, not by fact")

# 3. Sum of 11 share classes vs Wind main-product total
parts = [8.84, 0.42, 2.46, 0.01, 16.37, 48.90, 12.12, 0.80, 0.14, 109.47, 19.29]
assert close(sum(parts), 218.82, 0.01) and close(sum(parts) - now, 0.01, 0.001)
print(f"3 sum OK 11 share classes sum to {sum(parts):.2f} vs Wind 6-main-product total 218.81, diff 0.01 = rounding/class-count scope")

# 4. Shares of the total
assert close(109.47 / now * 100, 50.03, 0.01) and close(110.27 / now * 100, 50.39, 0.01) and close(16.51 / now * 100, 7.55, 0.01)
print("4 shares OK flagship A alone 50.03% of his total, A+C 50.39%; solo-managed 16.51 = only 7.55% of 218.81")

# 5. Flagship tenure: days and annualised tenure return
d = (date(2026, 9, 30) - date(2015, 4, 9)).days
years = d / 365.25
ann = (1 + 0.9533) ** (1 / years) - 1
assert d == 4192 and close(ann * 100, 6.00, 0.05)
print(f"5 tenure OK 2015-04-09 to 2026-09-30 = {d} days = {years:.2f} years; tenure return 95.33% = 1.9533x, mechanical annualised {ann*100:.2f}%; vs peer average 75.46% the gap is {95.33-75.46:.2f}pp")

# 6. Holder P/L vs fees (Sina fund data, 2015H2-2026H1 flagship)
assert close(30.76 / 85.44 * 100, 36.00, 0.01) and close(85.44 / 138.91 * 100, 61.51, 0.01) and close(30.76 / 61.11 * 100, 50.34, 0.01) and close(61.11 / 138.91 * 100, 43.99, 0.01)
print("6 pl OK flagship holders -85.44bn vs fees 30.76bn = fees are 36.00% of the loss; flagship is 61.51% of the 8-product total loss -138.91bn and 50.34% of total fees 61.11bn; total fees/loss = 43.99%")

# 7. Second fund: Dingyi tenure vs peer
assert close(89.61 - 62.17, 27.44, 0.001) and close(13.98 / 20.41 * 100, 68.50, 0.01)
print("7 dingyi OK tenure return 62.17% vs peer 89.61% = -27.44pp (flagship beat its peer, Dingyi lagged its own); holder loss -20.41bn, fees 13.98bn = 68.50% of that loss")

# 8. VP tenure vs the report's 'over five years' wording
dv = (date(2025, 9, 18) - date(2021, 3, 29)).days
assert dv == 1634 and dv / 365.25 < 5
print(f"8 vp OK VP from 2021-03-29 to 2025-09-18 = {dv} days = {dv/365.25:.2f} years, i.e. under 5 years -- the Sina/Pengpai wording 'over five years in the role' does not match its own dates; registered as a wording variant, not adopted")

# 9. Career and flagship founding arithmetic
assert 2026 - 23 == 2003 and close(109.47 / 59.21, 1.8487, 0.001)
print("9 career OK 23 years of experience in 2026 implies a start around 2003; flagship founded 2006-06-28 with 59.21bn, he took it over 2015-04-09, and at 2026-09-30 its A class alone is 109.47 = 1.8487x the founding size (+84.87%)")

# 10. Co-management wave and YTD spread
assert 3 + 1 + 1 == 5 and close(1 / 6 * 100, 16.67, 0.01) and close(86.53 / now * 100, 39.54, 0.01) and close(-4.89 - (-38.90), 34.01, 0.001)
print("10 wave OK May 2026 three funds + June one + 2026-11-07 flagship = 5 of 6 main products co-managed, solo products 1/6 = 16.67%; new flagship co-manager Nong Bingli runs 86.53bn = 39.54% of Liu's total; YTD 2026 across 11 classes ranges -38.90% to -4.89%, spread 34.01pp, all negative (10jqka, as of 2026-10-28/29)")

print("ALL PASS")
