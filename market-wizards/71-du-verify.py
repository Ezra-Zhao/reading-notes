#!/usr/bin/env python3
"""71 杜猛验算：摩根新兴动力混合（377240）2026 年三季报口径。
源数据全部取自季报原文：§2 份额总额、§3.1 财务、§3.2.1 A 类窗口、
§5.1/§5.2.1/§5.3.1 组合、§6 份额变动、§7.1 管理人自持、§4.1 任职日期。
"""
from datetime import date
from decimal import Decimal

def approx(a, b, tol=0.05):
    return abs(Decimal(str(a)) - Decimal(str(b))) <= Decimal(str(tol))

def f(p):  # percent -> factor
    return 1 + Decimal(str(p)) / 100

# 1: founding manager — appointment date == contract effective date; tenure
assert (date(2026, 9, 30) - date(2011, 7, 13)).days == 5558
assert approx(5558 / 365.25, 15.22, 0.01)

# 2: since-inception factor equals end NAV exactly (A class)
assert f("885.34") == Decimal("9.8534")

# 3: excess column is fund minus benchmark, every A window
rows = [("-27.70", "-25.00", "-2.70"), ("3.56", "12.51", "-8.95"),
        ("10.99", "7.41", "3.58"), ("112.57", "59.30", "53.27"),
        ("31.26", "-4.27", "35.53"), ("259.09", "62.34", "196.75"),
        ("346.26", "88.08", "258.18"), ("885.34", "106.17", "779.17")]
assert all(Decimal(a) - Decimal(b) == Decimal(c) for a, b, c in rows)

# 4: Q2 2026 implied by 6M / Q3 — fund +43.24%, benchmark +50.01%
assert approx((f("3.56") / f("-27.70") - 1) * 100, "43.24")
assert approx((f("12.51") / f("-25.00") - 1) * 100, "50.01")

# 5: recovery from the Q3 drop
assert approx((1 / f("-27.70") - 1) * 100, "38.31", 0.01)

# 6: ten-year split — earliest five years +239.98%, latest five +31.26%
assert approx((f("346.26") / f("31.26") - 1) * 100, "239.98")
assert approx((f("346.26") / f("259.09") - 1) * 100, "24.28")   # yrs 10->7
assert approx((f("259.09") / f("31.26") - 1) * 100, "173.57")   # yrs 7->5
assert approx((f("31.26") / f("112.57") - 1) * 100, "-38.25")   # yrs 5->3
assert approx((f("112.57") / f("10.99") - 1) * 100, "91.52")    # yrs 3->1

# 7: A-class profit split — realized +1.93亿, profit -33.58亿, float -35.51亿
rA, pA = Decimal("192537617.78"), Decimal("-3358341440.07")
assert approx(pA - rA, "-3550879057.85", 0.01)
assert approx(abs(pA - rA) / rA, "18.44", 0.01)

# 8: all-class totals — realized +2.61亿, profit -46.17亿, float -48.78亿
rT = rA + Decimal("64146161.52") + Decimal("4230410.73")
pT = pA + Decimal("-1180438619.50") + Decimal("-78535650.25")
assert approx(rT, "260914190.03", 0.01) and approx(pT, "-4617315709.82", 0.01)
assert approx(pT - rT, "-4878229899.85", 0.01)

# 9: equity is 90.00% of NAV; bonds zero; NAV total = sum of three classes
navT = Decimal("8386192111.87") + Decimal("2812123808.21") + Decimal("206757153.53")
assert approx(Decimal("10264272188.02") / navT * 100, "90.00")
assert approx(Decimal("10264272188.02") / Decimal("11489630930.93") * 100, "89.34")

# 10: manufacturing is 84.70% of NAV = 94.11% of the equity book
assert approx(Decimal("84.70") / Decimal("90.00") * 100, "94.11")

# 11: top-10 = 52.01% of NAV = 57.79% of equity; top-3 = 22.29%
top = [Decimal(x) for x in ("8.94", "7.18", "6.17", "5.72", "4.71",
                            "4.42", "4.37", "3.57", "3.52", "3.41")]
assert sum(top) == Decimal("52.01") and sum(top[:3]) == Decimal("22.29")
assert approx(sum(top) / Decimal("90.00") * 100, "57.79")

# 12: share flows reconcile to the §2 total; manager holding = 0.21%
a = (Decimal("851100103.94") - Decimal("908778779.63")) / Decimal("908778779.63") * 100
c = (Decimal("292207187.34") - Decimal("309475264.60")) / Decimal("309475264.60") * 100
assert approx(a, "-6.35") and approx(c, "-5.58")
tot = Decimal("851100103.94") + Decimal("292207187.34") + Decimal("20969652.56")
assert tot == Decimal("1164276943.84")
assert approx(Decimal("2401612.60") / tot * 100, "0.21", 0.01)

print("ALL 12 ASSERTION GROUPS PASS")
print("tenure 5558d/15.22y  Q2 +43.24% -> Q3 -27.70%  float A -35.51亿 = 18.44x realized")
