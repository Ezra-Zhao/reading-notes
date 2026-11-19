#!/usr/bin/env python3
"""74 Nygren验算：Oakmark Fund（OAKMX）口径。
源数据：(1) Summary Prospectus（2026-01-28，2026-04-02 修订重述，SEC 497K）——
§Portfolio managers 认人、Average Annual Total Returns（截至 2025-12-31）、
自 2016 年以来最高／最低季度、费用表、Investor Class 历史溯至 1991-08-05 的脚注；
(2) Form N-CSRS 半年度财务报表（期间截至 2026-03-31，2026-05-22 申报）——
Schedule of Investments、Statement of Assets and Liabilities、Statement of
Operations、Statements of Changes in Net Assets、Notes 5、Financial Highlights。
金额凡注 (in thousands) 者单位为千美元。
"""
from datetime import date
from decimal import Decimal

def approx(a, b, tol=0.05):
    return abs(Decimal(str(a)) - Decimal(str(b))) <= Decimal(str(tol))

def f(p):  # percent -> factor
    return 1 + Decimal(str(p)) / 100

# 1: identity / tenure — Nygren has managed the Fund since 2000 (prospectus,
#    year only); joined the Adviser in 1983; co-managers Nicolas since 2020,
#    Bierig since 2022-08-01; Investor Class history traces to 1991-08-05,
#    so the fund was 12,651 days old at 2026-03-31 and Nygren's span covers
#    26 calendar-year steps of it, about 75% of the fund's life
assert 2026 - 2000 == 26
assert 2026 - 1983 == 43
assert 2020 - 2000 == 20 and 2022 - 2000 == 22
assert (date(2026, 3, 31) - date(1991, 8, 5)).days == 12657
assert approx(12657 / 365.25, 34.65, 0.01)
assert approx(26 / (12657 / 365.25) * 100, 75.03, 0.1)

# 2: per-share reconciliation, Investor Class — begin + NII + gain - dist = end,
#    and each period's begin equals the prior period's end
rows = [  # (begin, nii, gain, dist, end)
    ("72.67", "0.43", "42.53", "0.15", "115.48"),    # FY2021
    ("115.48", "0.91", "-21.04", "1.74", "93.61"),   # FY2022
    ("93.61", "1.20", "24.72", "0.94", "118.59"),    # FY2023
    ("118.59", "1.76", "31.72", "1.35", "150.72"),   # FY2024
    ("150.72", "1.70", "14.99", "1.70", "165.71"),   # FY2025
    ("165.71", "0.71", "3.00", "1.58", "167.84"),    # H1 FY2026
]
for b, n, g, d, e in rows:
    assert Decimal(b) + Decimal(n) + Decimal(g) - Decimal(d) == Decimal(e)
for i in range(1, len(rows)):
    assert rows[i][0] == rows[i - 1][4]

# 3: five fiscal years FY2021-FY2025 compound to about +138.87% (factor 2.3887),
#    CAGR about 19.01%; NAV alone went 72.67 -> 165.71, about +128.03%
rets = ["59.18", "-17.73", "27.84", "28.39", "11.13"]
fac = Decimal(1)
for r in rets:
    fac *= f(r)
assert approx((fac - 1) * 100, "138.87", 0.15)
assert approx(fac, "2.3887", 0.002)
assert approx((float(fac) ** 0.2 - 1) * 100, "19.01", 0.05)
assert approx((Decimal("165.71") / Decimal("72.67") - 1) * 100, "128.03")

# 4: only one negative fiscal year of the five — FY2022 -17.73% needs +21.55%
#    to break even; FY2022+FY2023 together are about +5.17%
assert approx((1 / f("-17.73") - 1) * 100, "21.55")
assert approx((f("-17.73") * f("27.84") - 1) * 100, "5.17")

# 5: benchmark flip (prospectus, periods ended 2025-12-31, Investor Class
#    before taxes): 10y fund 13.71 vs S&P 500 14.82 (-1.11pp) vs Russell 1000
#    Value 10.53 (+3.18pp); 5y 15.04 vs 14.42 / 11.33; 1y 14.11 vs 17.88 / 15.91;
#    10y cumulative factors about 3.61 / 3.98 / 2.72
assert Decimal("13.71") - Decimal("14.82") == Decimal("-1.11")
assert Decimal("13.71") - Decimal("10.53") == Decimal("3.18")
assert Decimal("15.04") - Decimal("14.42") == Decimal("0.62")
assert Decimal("15.04") - Decimal("11.33") == Decimal("3.71")
assert Decimal("14.11") - Decimal("17.88") == Decimal("-3.77")
assert Decimal("14.11") - Decimal("15.91") == Decimal("-1.80")
assert approx(1.1371 ** 10, 3.61, 0.01)
assert approx(1.1482 ** 10, 3.98, 0.01)
assert approx(1.1053 ** 10, 2.72, 0.01)

# 6: extremes since 2016 (prospectus): best quarter +24.2% (Q4 2020), worst
#    -30.4% (Q1 2020) — the same calendar year; -30.4% needs +43.68% to recover
assert approx((1 / f("-30.4") - 1) * 100, "43.68")

# 7: operations H1 FY2026 (in thousands) — income 216,740 = 193,432 + 22,760
#    + 548; expenses 93,822, of which the advisory fee 73,743 is about 78.60%;
#    net investment income 122,918
assert Decimal("193432") + Decimal("22760") + Decimal("548") == Decimal("216740")
assert Decimal("216740") - Decimal("93822") == Decimal("122918")
assert approx(Decimal("73743") / Decimal("93822") * 100, "78.60")

# 8: realized / unrealized split H1 FY2026 — realized 1,870,969, of which
#    in-kind transactions 1,454,087 are about 77.72%; unrealized change
#    -1,403,821 gives back about 75.03% of the realized gain; net gain 467,148;
#    operations total 590,066
real = (Decimal("400933") + Decimal("1454087") + Decimal("0")
        - Decimal("28369") + Decimal("44318"))
assert real == Decimal("1870969")
assert approx(Decimal("1454087") / Decimal("1870969") * 100, "77.72")
assert Decimal("-1412544") + Decimal("8723") == Decimal("-1403821")
assert approx(Decimal("1403821") / Decimal("1870969") * 100, "75.03")
assert Decimal("1870969") - Decimal("1403821") == Decimal("467148")
assert Decimal("122918") + Decimal("467148") == Decimal("590066")

# 9: changes in net assets — H1 distributions 270,003 are the sum of the four
#    classes; share transactions net -631,120; total change -311,057 ties
#    beginning 24,745,742 to end 24,434,685; FY2025 operations 2,530,894 and
#    total change +1,667,897 tie 23,077,845 to 24,745,742; the H1 outflow
#    alone exceeds the whole FY2025 outflow of 572,995
assert (Decimal("92489") + Decimal("44399") + Decimal("99092")
        + Decimal("34023")) == Decimal("270003")
sold = Decimal("413084") + Decimal("454484") + Decimal("881808") + Decimal("2988913")
rein = Decimal("89769") + Decimal("43504") + Decimal("85897") + Decimal("31030")
rede = Decimal("1082260") + Decimal("551118") + Decimal("914859") + Decimal("3071372")
assert sold == Decimal("4738289") and rein == Decimal("250200") and rede == Decimal("5619609")
assert sold + rein - rede == Decimal("-631120")
assert Decimal("590066") - Decimal("270003") - Decimal("631120") == Decimal("-311057")
assert Decimal("24745742") - Decimal("311057") == Decimal("24434685")
assert Decimal("290626") + Decimal("2223370") + Decimal("16898") == Decimal("2530894")
assert Decimal("2530894") - Decimal("290002") - Decimal("572995") == Decimal("1667897")
assert Decimal("23077845") + Decimal("1667897") == Decimal("24745742")
assert Decimal("631120") > Decimal("572995")

# 10: balance sheet at 2026-03-31 (in thousands) — assets 24,611,191 minus
#     liabilities 176,506 = net assets 24,434,685 = paid-in capital 19,642,664
#     + distributable earnings 4,792,021 = sum of the four classes' net assets;
#     shares outstanding total 145,554; Investor NAV 9,448,248 / 56,294 = 167.84
assert Decimal("24611191") - Decimal("176506") == Decimal("24434685")
assert Decimal("19642664") + Decimal("4792021") == Decimal("24434685")
assert (Decimal("9448248") + Decimal("3780626") + Decimal("8463066")
        + Decimal("2742745")) == Decimal("24434685")
assert Decimal("56294") + Decimal("22523") + Decimal("50407") + Decimal("16330") == Decimal("145554")
assert approx(Decimal("9448248") / Decimal("56294"), "167.84", 0.01)

# 11: holdings at 2026-03-31 — 59 common stocks; sector values sum to total
#     common stocks 23,582,633; financials 8,322,112 are about 34.06% of net
#     assets (stated 34.1%); largest holding Targa 822,896 is about 3.37%;
#     top ten sum to 6,644,285, about 27.19%; total investments less cost =
#     4,028,695 unrealized, all of it in the stock book
sectors = ["8322112", "2782466", "2623504", "2254492", "1856135",
           "1849297", "1770428", "981953", "961407", "180839"]
assert sum(Decimal(x) for x in sectors) == Decimal("23582633")
assert approx(Decimal("8322112") / Decimal("24434685") * 100, "34.06")
assert approx(Decimal("822896") / Decimal("24434685") * 100, "3.37")
top10 = ["822896", "808315", "666741", "657626", "647807",
         "641502", "622918", "593433", "592447", "590600"]
assert sum(Decimal(x) for x in top10) == Decimal("6644285")
assert approx(Decimal("6644285") / Decimal("24434685") * 100, "27.19")
assert Decimal("24577975") - Decimal("20549280") == Decimal("4028695")
assert Decimal("23582633") - Decimal("19553938") == Decimal("4028695")

# 12: written options, transactions, share counts — Alphabet calls: premiums
#     received 8,308 less value 66 = unrealized gain 8,242; Note 5 purchases
#     6,598,096 vs sales proceeds 4,490,423; in-kind sales 2,650,866 with
#     realized gain 1,454,087 (about 54.85% of proceeds); H1 net share change
#     -3,649 thousand = -3,421 - 299 + 338 - 267; Investor Class shares fell
#     about 5.73% while its net assets fell about 4.52% in a +2.19% half year
assert Decimal("8308") - Decimal("66") == Decimal("8242")
assert approx(Decimal("1454087") / Decimal("2650866") * 100, "54.85")
assert Decimal("-3421") - Decimal("299") + Decimal("338") - Decimal("267") == Decimal("-3649")
assert approx(Decimal("3421") / (Decimal("56294") + Decimal("3421")) * 100, "5.73")
assert approx((Decimal("9448.2") / Decimal("9895.1") - 1) * 100, "-4.52")

print("74-nygren-verify: all 12 assertion groups passed")
