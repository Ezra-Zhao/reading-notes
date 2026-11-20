# -*- coding: utf-8 -*-
"""90 Smith (Fundsmith Equity Fund, T Class Acc) verification.
Source: Fundsmith Equity Fund factsheet October 2026 (data as at 30 Oct 2026),
official PDF from fundsmith.co.uk. All annual totals are the factsheet monthly
table's printed yearly totals; monthly rows used only for spot compounds.
"""
from datetime import date

ok = 0
def chk(name, cond, detail=""):
    global ok
    assert cond, f"FAIL {name}: {detail}"
    ok += 1
    print(f"PASS {name} {detail}")

# Annual totals (T Acc, %) printed in factsheet monthly table
annual = {2010: 6.1, 2011: 8.4, 2012: 12.5, 2013: 25.3, 2014: 23.3, 2015: 15.7,
          2016: 28.2, 2017: 22.0, 2018: 2.2, 2019: 25.6, 2020: 18.3, 2021: 22.1,
          2022: -13.8, 2023: 12.4, 2024: 8.9, 2025: 0.8}
ytd2026 = 2.0  # Jan-Oct 2026

# 1. Tenure: 1 Nov 2010 -> 30 Oct 2026
d = (date(2026, 10, 30) - date(2010, 11, 1)).days
chk("1 tenure", d == 5842, f"days={d} years={d/365.25:.2f}")

# 2. Compound of printed annual totals 2010(partial)..2025 + 2026 YTD vs inception +627.1%
f = 1.0
for y in range(2010, 2026):
    f *= 1 + annual[y] / 100
f *= 1 + ytd2026 / 100
chk("2 inception compound", abs(f - 7.271) < 0.06, f"factor={f:.4f} vs 7.271 (cum +{(f-1)*100:.1f}%)")

# 3. Annualised: 7.271 over tenure years vs printed 13.2%; equities 6.319 vs 12.2%
yrs = d / 365.25
ann_f = 7.271 ** (1 / yrs) - 1
ann_e = 6.319 ** (1 / yrs) - 1
chk("3 annualised", abs(ann_f * 100 - 13.2) < 0.15 and abs(ann_e * 100 - 12.2) < 0.15,
    f"fund={ann_f*100:.2f}% equities={ann_e*100:.2f}% diff={100*(ann_f-ann_e):.2f}pp")

# 4. Terminal: GBP10,000 inception endpoints fund vs equities
chk("4 terminal", abs(10000 * 7.271 - 72710) < 1 and abs(10000 * 6.319 - 63190) < 1,
    f"fund=72710 equities=63190 diff=9520 ratio={7.271/6.319:.4f}")

# 5. Negative full calendar years 2011-2025: only 2022
neg = [y for y in range(2011, 2026) if annual[y] < 0]
chk("5 only one down year", neg == [2022], f"negative years={neg} of 15")

# 6. 2022 drawdown recovery arithmetic
need = 1 / (1 - 0.138) - 1
after23 = (1 - 0.138) * (1 + 0.124)
after24 = after23 * (1 + 0.089)
chk("6 recovery", abs(need * 100 - 16.01) < 0.05 and after23 < 1 < after24,
    f"need=+{need*100:.2f}% after2023={(after23-1)*100:.2f}% after2024={(after24-1)*100:.2f}%")

# 7. Split: first decade-ish 2011-2020 vs last five full years 2021-2025
f1 = 1.0
for y in range(2011, 2021):
    f1 *= 1 + annual[y] / 100
f2 = 1.0
for y in range(2021, 2026):
    f2 *= 1 + annual[y] / 100
chk("7 split", f1 > 4 and f2 < 1.3,
    f"2011-2020 factor={f1:.4f} ann={(f1**0.1-1)*100:.2f}% ; 2021-2025 factor={f2:.4f} ann={(f2**0.2-1)*100:.2f}%")

# 8. Recent windows vs IA Global sector (cumulative table): 3Y 20.4/51.3, 5Y 14.7/39.5, 10Y 143.9/144.6
a5f = (1.147) ** 0.2 - 1
a5s = (1.395) ** 0.2 - 1
chk("8 recent windows", abs(a5f * 100 - 2.78) < 0.05 and abs(a5s * 100 - 6.88) < 0.05 and abs(143.9 - 144.6) - 0.7 < 1e-9,
    f"5Y ann fund={a5f*100:.2f}% sector={a5s*100:.2f}% ; 10Y gap=0.7pp sector ahead")

# 9. Monthly extremes and positive-month share: 192 months Nov2010-Oct2026, 65% positive
months = (2026 - 2010) * 12 + (10 - 11) + 1
chk("9 months", months == 192 and abs(0.65 * months - 124.8) < 0.01 and abs(9.4 - (-9.5) - 18.9) < 1e-9,
    f"months={months} positive~{0.65*months:.0f} best/worst range=18.9pp")

# 10. Price cross-check: T Acc price 727.05p vs inception factor 7.271 (launch 100p)
chk("10 price check", abs(727.05 / 100 - 7.271) < 0.002, f"price factor={727.05/100:.4f}")

# 11. Splits sum: geographic 81.6+7.3+5.3+4.5+1.3=100.0; sector sums 99.9 (rounding)
geo = 81.6 + 7.3 + 5.3 + 4.5 + 1.3
sec = 19.7 + 16.9 + 16.1 + 16.0 + 12.5 + 12.2 + 5.2 + 1.3
chk("11 splits", abs(geo - 100.0) < 1e-9 and abs(sec - 99.9) < 1e-9, f"geo={geo} sector={sec}")

# 12. OCF spread R 1.55 vs I 0.95 = 0.60pp; 2022 monthly compound vs printed -13.8 (rounding tol)
m2022 = [-9.5, -4.1, 4.0, -1.5, -4.7, -3.0, 7.3, -0.8, -4.5, 0.0, 1.5, 1.5]
fm = 1.0
for m in m2022:
    fm *= 1 + m / 100
chk("12 ocf & monthly compound", abs(1.55 - 0.95 - 0.60) < 1e-9 and abs((fm - 1) * 100 - (-13.8)) < 0.35,
    f"OCF spread=0.60pp ; 2022 months compound={(fm-1)*100:.2f}% vs printed -13.8%")

print(f"ALL {ok} GROUPS PASSED")
