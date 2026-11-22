#!/usr/bin/env python3
"""Verify arithmetic for reading-notes 114: Thornburg Global Opportunities / McMahon.
All inputs are printed figures from the fund's Portfolio Manager Commentary
dated 30 September 2026 (Thornburg). Decimal throughout."""
from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec = 28
ok = 0
def chk(name, got, exp, tol=D("0.06")):
    global ok
    assert abs(got - exp) <= tol, f"{name}: got {got} exp {exp}"
    ok += 1
    print(f"OK {name}: {got} ~ {exp}")

# G1 life / tenure frame: inception 2006-07-28 to 2026-09-30
life = (date(2026,9,30) - date(2006,7,28)).days
chk("life days", D(life), D(7369), D(0))
chk("life years", D(life)/D("365.25"), D("20.18"))
# 21st year statement: 2026-07-28 starts year 21
chk("anniversary days to 2026-07-28", D((date(2026,7,28)-date(2006,7,28)).days), D(7305), D(0))

# G2 Q3 NAV vs total return: 52.14 -> 53.47
chk("Q3 NAV pct", (D("53.47")/D("52.14")-1)*100, D("2.55"))
chk("Q3 NAV dollar", D("53.47")-D("52.14"), D("1.33"), D(0))

# G3 12m NAV price-only vs total return, dividends 0.61+2.45=3.06
chk("12m NAV price pct", (D("53.47")/D("47.92")-1)*100, D("11.58"))
chk("dividends sum", D("0.61")+D("2.45"), D("3.06"), D(0))
chk("12m total minus price", D("19.25")-D("11.58"), D("7.67"))

# G4 YTD split: H1 = (1+YTD)/(1+Q3)-1 for fund and index
chk("fund H1 pct", ((D("1.1198")/D("1.0255"))-1)*100, D("9.20"))
chk("index H1 pct", ((D("1.1303")/D("1.0160"))-1)*100, D("11.25"))
chk("fund H1 excess", D("9.20")-D("11.25"), D("-2.05"))

# G5 annualized excess table (I shares minus MSCI ACWI)
for nm, f, i, e in [("QTR","2.55","1.60","0.95"),("YTD","11.98","13.03","-1.05"),
                    ("1YR","19.25","16.75","2.50"),("3YR","24.99","21.73","3.26"),
                    ("5YR","14.09","11.57","2.52"),("10YR","13.23","12.38","0.85"),
                    ("ITD","11.43","8.41","3.02")]:
    chk(f"excess {nm}", D(f)-D(i), D(e), D("0.005"))

# G6 cumulative since inception: printed 788% vs 410%; $10k endpoints and ratio
chk("fund 10k endpoint", D(10000)*(1+D("7.88")), D(88800), D(0))
chk("index 10k endpoint", D(10000)*(1+D("4.10")), D(51000), D(0))
chk("endpoint ratio", D(88800)/D(51000), D("1.7412"))

# G7 ITD annualized consistency: (1+cum)^(1/years)-1 approx printed ann (rounding/cashflow caveat, tol 0.35)
yrs = D(life)/D("365.25")
chk("fund ann from cum", ((D("8.88")) ** (D(1)/yrs) - 1)*100, D("11.43"), D("0.35"))
chk("index ann from cum", ((D("5.10")) ** (D(1)/yrs) - 1)*100, D("8.41"), D("0.35"))

# G8 cumulative from annualized windows: 3/5/10 yr
for nm, f, i in [("3YR","24.99","21.73"),("5YR","14.09","11.57"),("10YR","13.23","12.38")]:
    n = int(nm[0]) if nm != "10YR" else 10
    chk(f"cum fund {nm}", ((1+D(f)/100)**n - 1)*100, {"3YR":D("95.28"),"5YR":D("93.29"),"10YR":D("246.42")}[nm], D("0.6"))
    chk(f"cum index {nm}", ((1+D(i)/100)**n - 1)*100, {"3YR":D("80.44"),"5YR":D("72.93"),"10YR":D("221.13")}[nm], D("0.6"))

# G9 10yr split: earlier 5yr segment ann from 10yr and recent 5yr factors
def seg_ann(cum_factor_long, cum_factor_short, years):
    return ((cum_factor_long/cum_factor_short) ** (D(1)/D(years)) - 1)*100
f10 = (1+D("13.23")/100)**10; f5 = (1+D("14.09")/100)**5
i10 = (1+D("12.38")/100)**10; i5 = (1+D("11.57")/100)**5
chk("fund 5-10yr ago ann", seg_ann(f10, f5, 5), D("12.38"))
chk("index 5-10yr ago ann", seg_ann(i10, i5, 5), D("13.20"))

# G10 holdings shape: 77 + 5 + 18 = 100; counts 25 + 14 = 39
chk("holdings pct sum", D("77")+D("5")+D("18"), D(100), D(0))
chk("holdings count", D(25)+D(14), D(39), D(0))
chk("top25 avg pct", D("77")/D(25), D("3.08"))

# G11 valuation discount and revenue growth ratios
chk("PE discount pct", (1-D("12.1")/D("17.8"))*100, D("32.02"))
chk("rev 5yr ratio", D("13.7")/D("5.0"), D("2.74"))
chk("rev 1yr gap", D("23.9")-D("5.6"), D("18.30"), D("0.005"))
chk("rev 1yr ex-Zegona gap", D("17.6")-D("5.6"), D("12.00"), D("0.005"))

# G12 A vs I: expense gap and QTR/ITD return gaps; sales-charge A QTR check approx
chk("expense gross gap", D("1.33")-D("1.07"), D("0.26"), D("0.005"))
chk("QTR I minus A", D("2.55")-D("2.47"), D("0.08"), D("0.005"))
chk("ITD I minus A", D("11.43")-D("11.00"), D("0.43"), D("0.005"))
# A with 4.50% sales charge: (1.0247)*(0.955)-1 = -2.14%
chk("A with load QTR", ((D("1.0247")*D("0.955"))-1)*100, D("-2.14"))

print(f"ALL {ok} ASSERTIONS PASSED")
