#!/usr/bin/env python3
"""73 陈皓验算：易方达科翔混合（110013）2026 年三季报口径。
源数据全部取自季报原文：§2 合同生效日与期末份额、§3.1 财务、§3.2.1 窗口、
§4.1 任职日期、§5.1/§5.2.1/§5.3.1 组合、§6 份额变动、§7.1/§7.2 管理人固有资金。
"""
from datetime import date
from decimal import Decimal

def approx(a, b, tol=0.05):
    return abs(Decimal(str(a)) - Decimal(str(b))) <= Decimal(str(tol))

def f(p):  # percent -> factor
    return 1 + Decimal(str(p)) / 100

# 1: tenure — appointed 2014-05-10, still in post at 2026-09-30; fund began 2008-11-13
assert (date(2026, 9, 30) - date(2014, 5, 10)).days == 4526
assert approx(4526 / 365.25, 12.39, 0.01)
assert (date(2014, 5, 10) - date(2008, 11, 13)).days == 2004
assert approx(2004 / 365.25, 5.49, 0.01)

# 2: excess column is fund minus benchmark, every window
rows = [("-15.68", "7.58", "-23.26"), ("20.75", "-3.02", "23.77"),
        ("25.46", "0.81", "24.65"), ("101.12", "6.75", "94.37"),
        ("53.35", "6.24", "47.11"), ("230.80", "28.34", "202.46"),
        ("333.37", "35.98", "297.39"), ("1512.09", "177.41", "1334.68")]
assert all(Decimal(a) - Decimal(b) == Decimal(c) for a, b, c in rows)

# 3: Q2 2026 implied by 6M / Q3 — fund +43.20%, benchmark -9.85%, excess +53.05pp
assert approx((f("20.75") / f("-15.68") - 1) * 100, "43.20")
assert approx((f("-3.02") / f("7.58") - 1) * 100, "-9.85")
q2e = (f("20.75") / f("-15.68") - 1) * 100 - (f("-3.02") / f("7.58") - 1) * 100
assert approx(q2e, "53.05", 0.06)

# 4: after Q3 -15.68%, break-even needs +18.60%
assert approx((1 / f("-15.68") - 1) * 100, "18.60")

# 5: long-window splits — earliest 5 of 10y +182.61%; years 7->3 ago +64.47%
assert approx((f("333.37") / f("53.35") - 1) * 100, "182.61")
assert approx((f("230.80") / f("101.12") - 1) * 100, "64.47")

# 6: profit split — realised +479,626,111.22, profit -836,059,955.30,
#    fair-value change -1,315,686,066.52, about 2.74x the realised gain
fv = Decimal("-836059955.30") - Decimal("479626111.22")
assert fv == Decimal("-1315686066.52")
assert approx(abs(fv) / Decimal("479626111.22"), "2.74", 0.01)

# 7: asset mix — equity 81.43% of total assets, 81.77% of NAV; cash 15.38%; bonds zero
assert approx(Decimal("3751151434.18") / Decimal("4606559439.49") * 100, "81.43")
assert approx(Decimal("3751151434.18") / Decimal("4587580473.33") * 100, "81.77")
assert approx(Decimal("708416491.11") / Decimal("4606559439.49") * 100, "15.38")
tot = Decimal("3751151434.18") + Decimal("708416491.11") + Decimal("146991514.20")
assert tot == Decimal("4606559439.49")

# 8: manufacturing 67.70% of NAV, about 82.79% of the equity book
assert approx(Decimal("3105787815.58") / Decimal("3751151434.18") * 100, "82.79")

# 9: top-10 concentration — sum 51.08% of NAV, top-2 17.19%, top-3 23.07%
top10 = ["8.71", "8.48", "5.88", "5.23", "4.33", "4.17", "4.12", "3.60", "3.43", "3.13"]
assert sum(Decimal(x) for x in top10) == Decimal("51.08")
assert Decimal(top10[0]) + Decimal(top10[1]) == Decimal("17.19")
assert sum(Decimal(x) for x in top10[:3]) == Decimal("23.07")
assert approx(Decimal("51.08") / Decimal("81.77") * 100, "62.47")

# 10: shares reconcile exactly; net inflow about +7.64% of opening shares
s0, sub, red = Decimal("602177443.27"), Decimal("108973988.72"), Decimal("62956709.31")
assert s0 + sub - red == Decimal("648194722.68")
assert approx((sub - red) / s0 * 100, "7.64")

# 11: manager's own money — 15,704,580.38 shares = 2.4228% of total, no trades;
#     cash dividend 4,711,374.11 on 2026-07-24 is exactly 0.30 per share held
assert approx(Decimal("15704580.38") / Decimal("648194722.68") * 100, "2.4228", 0.001)
assert approx(Decimal("4711374.11") / Decimal("15704580.38"), "0.30", 0.001)

# 12: since-inception factor 16.1209 vs end NAV 7.077 — NAV alone is about 43.90%
#     of the cumulative factor (distributions over the fund's life); weighted
#     average shares implied by -1.3350 per-share profit is about 626.30m
assert f("1512.09") == Decimal("16.1209")
assert approx(Decimal("7.077") / Decimal("16.1209") * 100, "43.90")
assert approx(Decimal("836059955.30") / Decimal("1.3350") / Decimal(1000000), "626.30", 0.5)

print("73-chen-verify: all 12 assertion groups passed")
