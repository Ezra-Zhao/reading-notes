# -*- coding: utf-8 -*-
"""96 Bill Smead (Smead Value Fund, I1 class SVFFX) verification.
Source: Smead Value Fund 3rd Quarter 2026 Fact Sheet (as of 2026-09-30,
Smead Capital Management official PDF). All performance figures are the
fact sheet's printed I1 Share Class (SVFFX) rows unless noted.
"""
from datetime import date
from decimal import Decimal as D

ok = 0
def chk(name, cond, detail=""):
    global ok
    assert cond, f"FAIL {name}: {detail}"
    ok += 1
    print(f"PASS {name} {detail}")

# 1. Fund life: inception 2008-01-02 to 2026-09-30; Bill Smead lead PM / founder / CIO
life = (date(2026, 9, 30) - date(2008, 1, 2)).days
chk("1 fund life", life == 6846 and abs(life / 365.25 - 18.74) < 0.01,
    f"fund life={life}d ({life/365.25:.2f}y) from inception 2008-01-02 to 2026-09-30; "
    "fact sheet lists Bill Smead as Lead Portfolio Manager, founder/chairman, creator of the firm's "
    "investment discipline and, as CIO, final decision maker for domestic equity portfolios; "
    "Cole Smead is Co-Portfolio Manager, so the claim is lead-manager, not sole-manager")

# 2. Calendar table 2017-2025 (I1): only two negative years; win counts vs both rulers
cal = [D(x) for x in ("25.30", "-4.51", "26.60", "1.94", "42.89", "-2.53", "17.15", "5.09", "5.38")]
rus = [D(x) for x in ("13.66", "-8.27", "26.54", "2.80", "25.16", "-7.54", "11.46", "14.37", "15.91")]
spx = [D(x) for x in ("21.83", "-4.38", "31.49", "18.40", "28.71", "-18.11", "26.29", "25.02", "17.88")]
neg = sum(1 for x in cal if x < 0)
wr = sum(1 for a, b in zip(cal, rus) if a > b)
ws = sum(1 for a, b in zip(cal, spx) if a > b)
chk("2 calendar shape", neg == 2 and wr == 6 and ws == 3 and max(cal) == D("42.89") and min(cal) == D("-4.51"),
    f"2017-2025 nine calendar years: only 2 negative (2018 -4.51, 2022 -2.53); best 2021 +42.89, worst 2018 -4.51; "
    f"beat Russell 1000 Value in {wr}/9 years, beat S&P 500 in only {ws}/9 years (2017, 2021, 2022)")

# 3. Calendar compounding 2017-2025: fund vs both rulers; last-3-years (2023-2025) split
def prod(xs):
    p = D(1)
    for x in xs:
        p *= 1 + x / 100
    return p
chk("3 calendar compounding", abs((prod(cal) - 1) * 100 - D("179.01")) < D("0.05")
    and abs((prod(rus) - 1) * 100 - D("131.91")) < D("0.05")
    and abs((prod(spx) - 1) * 100 - D("255.78")) < D("0.05")
    and abs((prod(cal[-3:]) - 1) * 100 - D("29.74")) < D("0.05")
    and abs((prod(spx[-3:]) - 1) * 100 - D("86.12")) < D("0.05"),
    "2017-2025 nine years compounded: fund +179.01%, Russell +131.91%, S&P +255.78%; "
    "but the last three calendar years (2023-2025) compounded fund +29.74% vs S&P +86.12% - the recent lag in one line")

# 4. 2022 defence and its price: fund -2.53 vs S&P -18.11; recovery prices; 2021-2022 two-year compound
chk("4 2022 defence", D("-2.53") - D("-18.11") == D("15.58") and D("-2.53") - D("-7.54") == D("5.01")
    and abs((1 / (1 - D("0.0253")) - 1) * 100 - D("2.60")) < D("0.01")
    and abs((1 / (1 - D("0.1811")) - 1) * 100 - D("22.12")) < D("0.01")
    and abs((prod([D("42.89"), D("-2.53")]) - 1) * 100 - D("39.27")) < D("0.05"),
    "2022: fund -2.53% beat S&P 500 by 15.58pp and Russell Value by 5.01pp; recovery price +2.60% vs S&P +22.12%; "
    "2021-2022 two years compounded fund +39.27% vs S&P about +5.40% - the defence was real, and it was bought in 2021-2022, not 2023-2025")

# 5. Annualized windows (I1) excess vs both rulers, all printed rows
W = ["1M", "QTR", "YTD", "1Y", "3Y", "5Y", "10Y", "15Y", "Since"]
F = [D(x) for x in ("-4.73", "1.61", "18.46", "18.93", "14.52", "10.18", "13.16", "14.94", "10.30")]
R = [D(x) for x in ("-3.13", "2.61", "19.27", "23.81", "20.07", "11.92", "11.43", "12.98", "8.85")]
S = [D(x) for x in ("-0.35", "2.30", "12.75", "15.74", "22.89", "13.79", "15.33", "15.68", "11.39")]
er = [f - r for f, r in zip(F, R)]
es = [f - s for f, s in zip(F, S)]
chk("5 window excess", er == [D(x) for x in ("-1.60", "-1.00", "-0.81", "-4.88", "-5.55", "-1.74", "1.73", "1.96", "1.45")]
    and es == [D(x) for x in ("-4.38", "-0.69", "5.71", "3.19", "-8.37", "-3.61", "-2.17", "-0.74", "-1.09")],
    "vs Russell Value: wins only the 10Y (+1.73pp), 15Y (+1.96) and since-inception (+1.45) windows; "
    "vs S&P 500: wins only YTD (+5.71) and 1Y (+3.19), loses since-inception by -1.09pp/yr - same fund, opposite verdicts by ruler")

# 6. Since-inception endpoints at printed annualized rates over the fund's 18.74-year life
yrs = life / 365.25
ef = 10000 * (1 + 0.1030) ** yrs
er_ = 10000 * (1 + 0.0885) ** yrs
es_ = 10000 * (1 + 0.1139) ** yrs
chk("6 endpoints", abs(ef - 62807) < 30 and abs(er_ - 49010) < 30 and abs(es_ - 75519) < 40
    and abs(ef / er_ - 1.2815) < 0.002 and abs(ef / es_ - 0.8317) < 0.002,
    f"$10,000 at printed since-inception annualized rates over {yrs:.2f}y: fund about ${ef:,.0f}, "
    f"Russell about ${er_:,.0f} (fund = 1.28x), S&P about ${es_:,.0f} (fund = 0.83x); annualized approximation, registered as such")

# 7. Decomposition of the since-inception rate: crisis-era opening segment vs the 15Y window
def seg(total_ann, total_y, sub_ann, sub_y):
    return ((1 + total_ann) ** total_y / (1 + sub_ann) ** sub_y) ** (1 / (total_y - sub_y)) - 1
chk("7 decomposition", abs(seg(0.1030, yrs, 0.1494, 15) * 100 - (-6.49)) < 0.05
    and abs(seg(0.0885, yrs, 0.1298, 15) * 100 - (-6.24)) < 0.05
    and abs(seg(0.1139, yrs, 0.1568, 15) * 100 - (-4.26)) < 0.05
    and abs(seg(0.1494, 15, 0.1316, 10) * 100 - 18.58) < 0.05,
    "opening segment (Jan 2008 to about Sep 2011, 3.74y) implied annualized: fund -6.49%, Russell -6.24%, S&P -4.26% - "
    "the fund opened on 2008-01-02, on the eve of the crisis year; the middle segment inside the 15Y window "
    "(about 2011-2016) implied +18.58%/yr is the fastest stretch of the whole record")

# 8. 2026 intra-year split: H1 implied from YTD and Q3; Jul-Aug implied from Q3 and September
h1f = (1 + D("0.1846")) / (1 + D("0.0161")) - 1
h1r = (1 + D("0.1927")) / (1 + D("0.0261")) - 1
h1s = (1 + D("0.1275")) / (1 + D("0.0230")) - 1
jaf = (1 + D("0.0161")) / (1 - D("0.0473")) - 1
chk("8 2026 split", abs(h1f * 100 - D("16.58")) < D("0.02") and abs(h1r * 100 - D("16.24")) < D("0.02")
    and abs(h1s * 100 - D("10.22")) < D("0.02") and abs(jaf * 100 - D("6.65")) < D("0.02"),
    f"2026 H1 implied: fund +{h1f*100:.2f}%, Russell +{h1r*100:.2f}%, S&P +{h1s*100:.2f}%; Q3 fund +1.61% lost to both rulers; "
    f"inside Q3, Jul-Aug implied +{jaf*100:.2f}% and September alone -4.73% (Russell -3.13, S&P -0.35) gave most of the quarter back")

# 9. Top ten lines: nine stocks plus cash sum to exactly 54.00; ex-cash stocks 48.44
top = [D(x) for x in ("7.40", "6.92", "6.64", "5.56", "5.21", "5.20", "5.11", "4.03", "3.99", "3.94")]
chk("9 top10", sum(top) == D("54.00") and sum(top) - D("5.56") == D("48.44")
    and abs(D("7.40") / (sum(top) - D("5.56")) * 100 - D("15.28")) < D("0.01"),
    "top-ten table rows sum to exactly 54.00% - but the fourth row is Cash 5.56%, so the nine stocks sum to 48.44%; "
    "largest stock Cenovus 7.40% is 15.28% of the nine-stock total; the cash row inside a top-ten table is itself a position")

# 10. Sectors and asset allocation: top-5 sectors 93.46 vs common stock 94.44; energy names inside top ten
chk("10 sectors", D("26.56") + D("19.25") + D("18.87") + D("17.75") + D("11.03") == D("93.46")
    and D("94.44") + D("5.56") == D("100.00")
    and D("7.40") + D("6.64") + D("4.03") == D("18.07")
    and D("5.21") + D("5.20") == D("10.41") and D("6.92") + D("5.11") == D("12.03"),
    "top-5 sectors (Energy 26.56, Financials 19.25, Cons. Disc. 18.87, Healthcare 17.75, Real Estate 11.03) sum to 93.46% "
    "against common stock 94.44% of assets - the 0.98pp remainder sits in unlisted sectors, registered; "
    "common stock 94.44 + cash 5.56 = 100.00 exactly; three energy names inside the top ten already sum to 18.07%")

# 11. Concentration and turnover: 27 holdings, $3.97bn assets, 16.25% turnover implies about 6.15 years
chk("11 turnover", abs(1 / D("0.1625") - D("6.15")) < D("0.01"),
    "27 holdings and $3.97bn total net assets (printed key facts); turnover 16.25% inverts to an implied average "
    "holding period of about 6.15 years - the low-turnover claim in the fund's own 'play the long game' text, in numbers")

# 12. Fee ladder vs 10Y returns across classes: return gaps track fee gaps, not exactly
chk("12 fees", D("13.28") - D("13.16") == D("0.12") and D("0.96") - D("0.81") == D("0.15")
    and D("13.16") - D("12.88") == D("0.28") and D("1.23") - D("0.96") == D("0.27")
    and D("13.16") - D("12.47") == D("0.69") and D("1.82") - D("0.96") == D("0.86"),
    "10Y annualized: Y 13.28 (fee 0.81), I1 13.16 (0.96), A w/o load 12.88 (1.23), C 12.47 (1.82); "
    "return gaps vs I1 are +0.12 / -0.28 / -0.69 against fee gaps of -0.15 / +0.27 / +0.86 - same portfolio, "
    "the class you buy moves the 10Y result by up to 0.81pp/yr, roughly but not exactly the fee ladder")

print(f"ALL {ok} GROUPS PASSED")
