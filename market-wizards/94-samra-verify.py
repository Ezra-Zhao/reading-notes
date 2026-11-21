# -*- coding: utf-8 -*-
"""94 Samra (Artisan International Value Fund, Investor Class ARTKX) verification.
Source: Artisan International Value Fund Quarterly Fact Sheet as of 2026-09-30
(Artisan Partners official PDF). All performance figures are the sheet's printed
Investor Class rows unless noted. Identity: Artisan bio text (Samra lead PM since
inception Sep 2002) reproduced verbatim by TWST and The Market.
"""
from datetime import date
from decimal import Decimal as D

ok = 0
def chk(name, cond, detail=""):
    global ok
    assert cond, f"FAIL {name}: {detail}"
    ok += 1
    print(f"PASS {name} {detail}")

# 1. Tenure: Samra lead PM since inception 2002-09-23; fact sheet date 2026-09-30
ten = (date(2026, 9, 30) - date(2002, 9, 23)).days
chk("1 tenure", ten == 8773 and abs(ten / 365.25 - 24.02) < 0.01,
    f"tenure={ten}d ({ten/365.25:.2f}y); fund inception is his start, so tenure = 100% of fund life, no predecessor stub")

# 2. Calendar decade ARTKX 2016-2025 compound, negatives, best-worst spread
cal = [D(x) for x in ("5.50", "23.82", "-15.65", "23.96", "8.52", "16.69", "-7.00", "22.65", "6.39", "22.50")]
prod = D(1)
for r in cal:
    prod *= (1 + r / 100)
ann = float(prod) ** (1 / 10) - 1
neg = sum(1 for r in cal if r < 0)
chk("2 calendar compound", abs((float(prod) - 1) * 100 - 157.12) < 0.05 and abs(ann * 100 - 9.90) < 0.02
    and neg == 2 and max(cal) - min(cal) == D("39.61"),
    f"2016-2025 compound {(float(prod)-1)*100:.2f}% annualised {ann*100:.2f}%; only {neg} negative years (2018 -15.65, 2022 -7.00); best 2019 +23.96 vs worst 2018 -15.65 spread 39.61pp")

# 3. Calendar two halves
def compound(rs):
    p = D(1)
    for r in rs:
        p *= (1 + r / 100)
    return float(p)
h1, h2 = compound(cal[:5]), compound(cal[5:])
chk("3 halves", abs((h1 - 1) * 100 - 48.22) < 0.05 and abs((h2 - 1) * 100 - 73.47) < 0.05
    and abs((h1 ** 0.2 - 1) * 100 - 8.19) < 0.02 and abs((h2 ** 0.2 - 1) * 100 - 11.65) < 0.02,
    f"2016-2020 {(h1-1)*100:.2f}% ann {(h1**0.2-1)*100:.2f}%; 2021-2025 {(h2-1)*100:.2f}% ann {(h2**0.2-1)*100:.2f}%; second half faster by ~3.46pp/yr")

# 4. Calendar per-year excess: ARTKX vs EAFE and vs ACWI ex USA, win counts
eafe_cal = [D(x) for x in ("1.00", "25.03", "-13.79", "22.01", "7.82", "11.26", "-14.45", "18.24", "3.82", "31.22")]
acwi_cal = [D(x) for x in ("4.50", "27.19", "-14.20", "21.51", "10.65", "7.82", "-16.00", "15.62", "5.53", "32.39")]
ex_e = [a - b for a, b in zip(cal, eafe_cal)]
ex_a = [a - b for a, b in zip(cal, acwi_cal)]
chk("4 calendar excess", sum(1 for e in ex_e if e > 0) == 7 and sum(1 for e in ex_a if e > 0) == 6
    and ex_e[9] == D("-8.72") and ex_a[9] == D("-9.89") and ex_e[6] == D("7.45"),
    f"vs EAFE wins 7/10 (worst 2025 -8.72pp, best 2022 +7.45pp); vs ACWI ex USA wins 6/10 (worst 2025 -9.89pp)")

# 5. Trailing excess as of 2026-09-30 (printed annualised): fund vs both indexes
F = [D(x) for x in ("13.60", "16.23", "11.08", "10.23", "11.80")]   # 1Y 3Y 5Y 10Y inception
E = [D(x) for x in ("15.69", "18.40", "9.32", "9.07", "8.17")]
A = [D(x) for x in ("20.00", "20.54", "9.55", "9.25", "8.60")]
chk("5 trailing excess", [f - e for f, e in zip(F, E)] == [D("-2.09"), D("-2.17"), D("1.76"), D("1.16"), D("3.63")]
    and [f - a for f, a in zip(F, A)] == [D("-6.40"), D("-4.31"), D("1.53"), D("0.98"), D("3.20")],
    "vs EAFE: 1Y -2.09, 3Y -2.17, 5Y +1.76, 10Y +1.16, inception +3.63 pp/yr; vs ACWI ex USA: -6.40, -4.31, +1.53, +0.98, +3.20; short windows lose, long windows win on both rulers")

# 6. Window decomposition: inception vs last 10Y; 10Y vs 5Y; 5Y vs 3Y
yrs = ten / 365.25
first14 = ((1.1180 ** yrs) / (1.1023 ** 10)) ** (1 / (yrs - 10)) - 1
first5of10 = ((1.1023 ** 10) / (1.1108 ** 5)) ** (1 / 5) - 1
first2of5 = ((1.1108 ** 5) / (1.1623 ** 3)) ** (1 / 2) - 1
chk("6 decomposition", abs(first14 * 100 - 12.93) < 0.03 and abs(first5of10 * 100 - 9.39) < 0.03 and abs(first2of5 * 100 - 3.78) < 0.03,
    f"implied first ~14.02y {first14*100:.2f}%/yr vs last 10Y 10.23; implied first 5 of last 10 {first5of10*100:.2f} vs last 5Y 11.08; implied first 2 of last 5 {first2of5*100:.2f} vs last 3Y 16.23 (arithmetic decomposition, not printed)")

# 7. Growth of $10,000 since inception at printed annualised rates
g_f = 10000 * 1.1180 ** yrs
g_e = 10000 * 1.0817 ** yrs
g_a = 10000 * 1.0860 ** yrs
chk("7 growth", abs(g_f - 145700) < 1500 and abs(g_e - 65900) < 900 and abs(g_f / g_e - 2.21) < 0.03,
    f"$10k at 11.80% for {yrs:.2f}y ~ ${g_f:,.0f}; EAFE at 8.17% ~ ${g_e:,.0f}; ACWI ex USA at 8.60% ~ ${g_a:,.0f}; fund/EAFE ratio ~{g_f/g_e:.2f}x (annualised-rate approximation)")

# 8. Drawdown recovery: 2018 and 2022 calendar losses
chk("8 recovery", abs((1 / 0.8435 - 1) * 100 - 18.55) < 0.02 and abs((0.8435 * 1.2396 - 1) * 100 - 4.56) < 0.02
    and abs((1 / 0.93 - 1) * 100 - 7.53) < 0.02 and abs((0.93 * 1.2265 - 1) * 100 - 14.06) < 0.02,
    "2018 -15.65% needs +18.55%; 2019 +23.96% compounds to +4.56% above pre-drop level (recovered in one year); 2022 -7.00% needs +7.53%, 2023 +22.65% overshoots to +14.06%")

# 9. 2026 split: YTD and Q3 printed imply H1
h1f = 1.0898 / 0.9703 - 1
h1e = 1.1033 / 1.0081 - 1
chk("9 2026 split", abs(h1f * 100 - 12.31) < 0.02 and abs(h1e * 100 - 9.45) < 0.02
    and abs((D("-2.97") - D("0.81"))) == D("3.78") and abs((D("8.98") - D("10.33"))) == D("1.35"),
    f"implied H1 2026 fund {h1f*100:.2f}% vs EAFE {h1e*100:.2f}% (fund ahead ~2.87pp); Q3 fund -2.97 vs EAFE +0.81 (behind 3.78pp); YTD ends 1.35pp behind")

# 10. Share-class spreads on the shared 10Y window vs prospectus expense gaps
chk("10 class spreads", D("10.39") - D("10.23") == D("0.16") and D("10.49") - D("10.23") == D("0.26")
    and D("1.20") - D("1.07") == D("0.13") and D("1.20") - D("0.97") == D("0.23"),
    "10Y annualised: ARTKX 10.23, APDKX 10.39 (+0.16), APHKX 10.49 (+0.26); prospectus expense 1.20/1.07/0.97 gaps 0.13/0.23; return spreads exceed fee gaps by only 0.03pp each (same portfolio, cheaper classes keep more)")

# 11. Top 10 holdings sum vs printed total
top10 = [D(x) for x in ("4.4", "4.3", "3.9", "3.9", "3.9", "3.5", "3.4", "3.4", "3.1", "3.0")]
chk("11 top10", sum(top10) == D("36.8") and abs(float(top10[0] / sum(top10)) * 100 - 11.96) < 0.02,
    "rows sum 36.8% vs printed total 36.7% (0.1pp rounding, registered only); largest Unilever 4.4% = 11.96% of the top-10 block; 51 securities in total")

# 12. Sector and country sums, construction limits
sec_f = [D(x) for x in ("1.6", "18.4", "17.7", "1.4", "13.5", "13.3", "16.9", "7.2", "9.8", "0", "0")]
sec_e = [D(x) for x in ("3.9", "8.1", "6.5", "3.9", "26.3", "10.0", "18.9", "11.2", "6.0", "1.5", "3.7")]
eur = [D(x) for x in ("18.1", "17.4", "12.4", "10.9", "6.6", "5.2", "1.3")]
chk("12 allocations", sum(sec_f) == D("99.8") and sum(sec_e) == D("100.0") and sum(eur) == D("71.9")
    and D("12.1") + D("3.0") == D("15.1") and D("72.0") + D("15.1") + D("10.3") + D("2.6") == D("100.0")
    and D("18.1") < D("35") and D("10.3") < D("30") and D("4.4") < D("5") and D("11.9") < D("15"),
    "fund sectors sum 99.8 vs printed 100.0 (rounding, registered); EAFE sectors sum exactly 100.0; Europe components 71.9 vs printed 72.0 (rounding, registered); Americas exact 15.1; regions total exactly 100.0; Switzerland 18.1% < 35% country cap, EM 10.3% < 30% cap, largest holding 4.4% < 5% guide, cash 11.9% < 15% typical (caps apply at purchase)")

print(f"ALL {ok} GROUPS PASS")
