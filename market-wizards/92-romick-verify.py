# -*- coding: utf-8 -*-
"""92 Romick (FPA Crescent Fund FPACX) verification.
Source: FPA Crescent Fund Fact Sheet, September 30, 2026 (fpa.com PDF)
+ FPA official bio of Steven Romick (public-use extended version).
All performance figures are the fact sheet's printed FPACX rows
(FPACX = Institutional class per the fact sheet ticker block) unless noted.
"""
from datetime import date
from decimal import Decimal

ok = 0
def chk(name, cond, detail=""):
    global ok
    assert cond, f"FAIL {name}: {detail}"
    ok += 1
    print(f"PASS {name} {detail}")

# 1. Tenure: fund inception 1993-06-02 -> 2026-09-30; FPA control from 1996-03-01
tenure = (date(2026, 9, 30) - date(1993, 6, 2)).days
fpa = (date(2026, 9, 30) - date(1996, 3, 1)).days
chk("1 tenure", tenure == 12173 and fpa == 11170,
    f"fund life={tenure}d ({tenure/365.25:.2f}y) FPA-control={fpa}d share={fpa/tenure*100:.2f}% predecessor stub={tenure-fpa}d")

# 2. Growth of $10k: since-inception annualised (fund 10.20 / SP 10.91 / blend 8.48)
#    implied endpoints vs printed chart endpoints (254,742.48 / 315,213.07 / 150,916.41)
yrs = tenure / 365.25
imp = {n: 10000 * (1 + r) ** yrs for n, r in [("fund", .1020), ("sp", .1091), ("blend", .0848)]}
prt = {"fund": 254742.48, "sp": 315213.07, "blend": 150916.41}
chk("2 growth10k", all(abs(imp[k] / prt[k] - 1) < 0.002 for k in imp) and prt["sp"] > prt["fund"] > prt["blend"],
    "; ".join(f"{k} implied={imp[k]:,.0f} printed={prt[k]:,.2f} diff={(imp[k]/prt[k]-1)*100:+.2f}%" for k in imp))

# 3. Trailing annualised windows vs S&P 500 and vs 60/40 S&P blend (printed rows)
F = [10.20, 9.53, 8.45, 10.01, 10.00, 9.81, 15.56, 10.34]   # since,30,20,15,10,5,3,1
S = [10.91, 10.33, 11.21, 15.68, 15.33, 13.79, 22.89, 15.74]
B = [8.48, 8.10, 8.12, 10.15, 9.71, 8.01, 15.16, 8.56]
vs_sp = [round(f - s, 2) for f, s in zip(F, S)]
vs_bl = [round(f - b, 2) for f, b in zip(F, B)]
chk("3 trailing excess", vs_sp == [-0.71, -0.80, -2.76, -5.67, -5.33, -3.98, -7.33, -5.40]
    and vs_bl == [1.72, 1.43, 0.33, -0.14, 0.29, 1.80, 0.40, 1.78],
    f"vs SP all negative {vs_sp}; vs blend {vs_bl} (only 15Y negative)")

# 4. Market cycles (annualised): FPACX vs SP vs blend
cyc_f = [14.70, 7.65, 9.85]; cyc_s = [2.00, 10.43, 11.95]; cyc_b = [3.97, 8.14, 7.00]
chk("4 cycles", [round(f - s, 2) for f, s in zip(cyc_f, cyc_s)] == [12.70, -2.78, -2.10]
    and [round(f - b, 2) for f, b in zip(cyc_f, cyc_b)] == [10.73, -0.49, 2.85],
    "cycle1 (2000-03-25 to 2007-10-09) fund beats SP by 12.70pp/yr; cycle2 -2.78; current -2.10")

# Calendar rows 1994-2025 (printed Annual Performance)
FUND = {2025:17.65,2024:13.96,2023:20.27,2022:-9.20,2021:15.17,2020:12.11,2019:20.02,2018:-7.43,
        2017:10.39,2016:10.25,2015:-2.06,2014:6.64,2013:21.95,2012:10.33,2011:3.02,2010:12.04,
        2009:28.37,2008:-20.55,2007:6.84,2006:12.43,2005:10.83,2004:10.21,2003:26.15,2002:3.71,
        2001:36.14,2000:3.59,1999:-6.28,1998:2.79,1997:21.95,1996:22.88,1995:26.04,1994:4.22}
SPX = {2025:17.88,2024:25.02,2023:26.29,2022:-18.11,2021:28.71,2020:18.40,2019:31.49,2018:-4.38,
       2017:21.83,2016:11.96,2015:1.38,2014:13.69,2013:32.39,2012:16.00,2011:2.11,2010:15.06,
       2009:26.46,2008:-37.00,2007:5.49,2006:15.79,2005:4.91,2004:10.88,2003:28.68,2002:-22.10,
       2001:-11.89,2000:-9.10,1999:21.04,1998:28.58,1997:33.36,1996:22.96,1995:37.58,1994:1.32}
def prod(d, a, b):
    p = 1.0
    for y in range(a, b + 1): p *= 1 + d[y] / 100
    return p

# 5. Negative-year count and extremes, calendar 1994-2025 (32 years)
neg_f = sorted(y for y, v in FUND.items() if v < 0)
neg_s = sorted(y for y, v in SPX.items() if v < 0)
chk("5 negatives", neg_f == [1999, 2008, 2015, 2018, 2022] and neg_s == [2000, 2001, 2002, 2008, 2018, 2022]
    and max(FUND.values()) == 36.14 and min(FUND.values()) == -20.55,
    f"fund negatives {len(neg_f)} {neg_f}; SP negatives {len(neg_s)}; fund best 2001 +36.14 worst 2008 -20.55 range {36.14+20.55:.2f}pp")

# 6. Dot-com bust 2000-2002 compounding
pf, ps = prod(FUND, 2000, 2002), prod(SPX, 2000, 2002)
chk("6 bust 2000-02", abs((pf - 1) * 100 - 46.26) < 0.05 and abs((ps - 1) * 100 - (-37.61)) < 0.05,
    f"fund 2000-02 {(pf-1)*100:.2f}% vs SP {(ps-1)*100:.2f}%; ending-wealth ratio {pf/ps:.2f}x")

# 7. 2008 drawdown and 2009 recovery (two-year product)
chk("7 2008", abs((1 / 0.7945 - 1) * 100 - 25.87) < 0.05 and abs((1 / 0.63 - 1) * 100 - 58.73) < 0.05
    and abs((0.7945 * 1.2837 - 1) * 100 - 1.99) < 0.05 and abs((0.63 * 1.2646 - 1) * 100 - (-20.33)) < 0.05,
    "fund -20.55% needs +25.87%, 2009 +28.37% -> 2yr +1.99% (recovered); SP -37.00% needs +58.73%, 2yr -20.33%")

# 8. 2022 drawdown and 2023 recovery
chk("8 2022", abs((1 / 0.908 - 1) * 100 - 10.13) < 0.05 and abs((0.908 * 1.2027 - 1) * 100 - 9.21) < 0.05
    and abs((0.8189 * 1.2629 - 1) * 100 - 3.42) < 0.05 and abs((-9.20) - (-18.11) - 8.91) < 0.005,
    "fund -9.20% (8.91pp shallower than SP -18.11%), needs +10.13%, 2023 +20.27% -> 2yr +9.21% vs SP +3.42%")

# 9. Calendar decades compounding (annualised)
d = {}
for a, b in [(1996, 2005), (2006, 2015), (2016, 2025)]:
    d[(a, b)] = (prod(FUND, a, b) ** 0.1 - 1, prod(SPX, a, b) ** 0.1 - 1)
chk("9 decades", abs(d[(1996, 2005)][0] * 100 - 12.52) < 0.05 and abs(d[(1996, 2005)][1] * 100 - 9.07) < 0.05
    and abs(d[(2006, 2015)][0] * 100 - 7.11) < 0.05 and abs(d[(2016, 2025)][0] * 100 - 9.84) < 0.05
    and abs(d[(2016, 2025)][1] * 100 - 14.82) < 0.05,
    "; ".join(f"{a}-{b} fund {v[0]*100:.2f}% vs SP {v[1]*100:.2f}%" for (a, b), v in d.items()))

# 10. Since-inception risk stats: capture ratios tie to printed 94% / 73%
chk("10 risk", abs(10.20 / 10.91 * 100 - 93.49) < 0.05 and abs(10.79 / 14.85 * 100 - 72.66) < 0.05
    and abs(0.72 / 0.60 - 1.20) < 0.005,
    f"return capture {10.20/10.91*100:.2f}% ~ printed 94%; risk capture {10.79/14.85*100:.2f}% ~ printed 73%; "
    f"beta 0.59 corr 0.81 std 10.79 vs 14.85; Sharpe 0.72 vs 0.60 (+20.00% rel), Sortino 1.09 vs 0.90")

# 11. Top-10 holdings: rows sum 23.6 vs printed total 23.7 (rounding, per footnote 11)
top10 = [Decimal(x) for x in ("4.8", "3.3", "2.5", "2.2", "2.1", "1.9", "1.8", "1.8", "1.6", "1.6")]
chk("11 top10", sum(top10) == Decimal("23.6") and Decimal("4.8") + Decimal("3.3") + Decimal("2.5") == Decimal("10.6"),
    f"top10 rows sum={sum(top10)}% vs printed total 23.7% (rounding); top1 Alphabet 4.8 = {float(Decimal('4.8')/sum(top10))*100:.2f}% of top10; top3 sum=10.6%")

# 12. Allocation arithmetic: sector Of-Equity rows, geography, exposure gap (printed values)
sec = [Decimal(x) for x in ("18.2", "14.3", "13.6", "13.1", "10.9", "9.8", "9.2", "8.3", "1.5", "0.9", "0.1", "0.0")]
geo = Decimal("56.7") + Decimal("39.0") + Decimal("4.3")
chk("12 allocation", sum(sec) == Decimal("99.9") and geo == Decimal("100.0")
    and abs(67.5 - 62.2 - 5.3) < 1e-9 and abs(100 - 67.5 - 32.5) < 1e-9,
    f"sector Of-Equity rows sum={sum(sec)} (printed total 100.0, rounding); Of-Fund total 62.2 = net equity; "
    f"geography US 56.7 + IntlDev 39.0 + EM 4.3 = {geo}; net risk exposure 67.5 - equity 62.2 = 5.3pp (credit/other); "
    f"cash = 100 - 67.5 = 32.5 ties to asset-allocation chart cash row 32.5") 

print(f"ALL {ok} GROUPS PASSED")
