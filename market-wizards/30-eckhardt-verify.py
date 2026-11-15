#!/usr/bin/env python3
"""Verify arithmetic for note 30 (William Eckhardt). Inputs from public
sources cited in the note: AbeBooks/Springer author bio, Top Traders
Unplugged podcast transcript (his own words, 2024), ETC official site
Alternatives Watch reprint (2023), Autumn Gold CTA database Evolution
Strategy report Aug-1991 to Sep-2025, New Trader U / PaxForex secondary
summaries of the older 20-year record."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Education timeline: BA 1969 -> MS 1970 (1y), doctoral research 1970-1974 (4y)
assert 1970 - 1969 == 1 and 1974 - 1970 == 4
print("1 education timeline OK BA1969 MS1970 doctoral 4y trading 1974")

# 2. Birth-year check: 1955 claim makes BA at 14 (impossible); 1949 makes BA at 20
assert 1969 - 1955 == 14 and 1969 - 1949 == 20 and 1974 - 1949 == 25
print("2 birth-year OK 1955->BA at 14 impossible; 1949->BA 20, trading at 25")

# 3. Pre-ETC years and ETC age: 1974->1991 = 17y; Aug1991->Sep2025 = 410 months
assert 1991 - 1974 == 17
months = (2025 - 1991) * 12 + (9 - 8) + 1
assert months == 410 and 224 + 186 == 410
assert close(224 / 410 * 100, 54.63, 0.01)
print("3 spans OK 17y before ETC; 410 months Aug1991-Sep2025, gain months 224/410 = 54.63%")

# 4. Cumulative vs VAMI vs annualized (Autumn Gold stats table)
vami = 1000 * (1 + 2023.06 / 100)
assert close(vami, 21231, 1), vami
ann = (vami / 1000) ** (12 / 410) - 1
assert close(ann * 100, 9.35, 0.05), ann
print("4 cumulative OK VAMI 21231, annualized from 410 months =", round(ann * 100, 2), "% vs reported 9.35%")

# 5. Older 20-year record: 17.35% compound factor and 2010 discrepancy
f20 = 1.1735 ** 20
assert close(f20, 24.53, 0.15), f20
assert close(21.09 - 20.61, 0.48, 0.001)
print("5 old-record OK 17.35%^20 =", round(f20, 2), "x; 2010 secondary 21.09% vs AutumnGold table 20.61% diff 0.48pp")

# 6. Drawdown recovery math: -27.11% peak-to-valley, worst month -18.30%
rec = 1 / (1 - 0.2711) - 1
assert close(rec * 100, 37.19, 0.02), rec
rec2 = 1 / (1 - 0.1877) - 1
assert close(rec2 * 100, 23.11, 0.02), rec2
print("6 drawdown OK -27.11% needs +37.19%; current streak -18.77% needs +23.11%")

# 7. AUM scopes: 94.2m (Evolution Sep-2025) vs ~200m (firm, 2023) vs >1bn (old bio)
assert close(94.2 / 200 * 100, 47.10, 0.01)
assert close(94.2 / 1000 * 100, 9.42, 0.01)
assert close(20 / 94.2 * 100, 21.23, 0.01)
print("7 AUM scopes OK 94.2m = 47.10% of 200m, 9.42% of 1bn; min ticket 20m = 21.23% of program AUM")

# 8. 2022: AutumnGold annual 12.53% vs Alternatives Watch 'almost 13%' and UCITS >14%
assert close(13 - 12.53, 0.47, 0.01) and 14 - 12.53 > 1.4
print("8 2022 OK table 12.53% vs 'almost 13%' diff 0.47pp; UCITS >14% is a different vehicle")

# 9. Turtle totals reused from note 04: 175m over 23 trainees
assert close(175 / 23, 7.61, 0.01)
f = 1.8 ** 4
assert close(f, 10.50, 0.02)
print("9 turtle OK 175m/23 = 7.61m per head (scale only); 80%^4 = 10.50x")

# 10. Monthly-average vs compound gap (volatility drag, illustrative)
assert close(0.87 * 12, 10.44, 0.001) and close(10.44 - 9.35, 1.09, 0.001)
print("10 monthly avg OK 0.87%*12 = 10.44% simple vs 9.35% compound, gap 1.09pp")

# 11. Academic lag: Mind paper 1993, Paradoxes book 2013
assert 1993 - 1974 == 19 and 2013 - 1991 == 22 and 2013 - 1974 == 39
assert 2024 - 1974 == 50
print("11 academic lag OK Mind 1993 = trading+19y; Paradoxes 2013 = ETC+22y / trading+39y; 2024 podcast = trading+50y")

# 12. Annual table spot checks (Autumn Gold): 1997, 1993, 2011, 2025YTD signs
assert close(57.95 - 45.18, 12.77, 0.001)  # 1993 vs 1997
assert close(-15.64 - (-12.43), -3.21, 0.001)  # 2011 vs 2025 YTD diff
print("12 annual spot OK 1993 +57.95% vs 1997 +45.18% diff 12.77pp; 2011 -15.64% vs 2025YTD -12.43%")

print("ALL PASS")
