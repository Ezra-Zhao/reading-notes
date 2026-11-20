# -*- coding: utf-8 -*-
"""91 Liu Shiqing (China Europe Value Discovery Mixed A, 166005) verification.
Source: 2026 Q3 report (period end 2026-09-30, sent 2026-10-27), cninfo PDF.
All performance windows are the report's printed A-class table unless noted.
"""
from datetime import date
from decimal import Decimal

ok = 0
def chk(name, cond, detail=""):
    global ok
    assert cond, f"FAIL {name}: {detail}"
    ok += 1
    print(f"PASS {name} {detail}")

# 1. Tenure: manager from 2025-03-21 to 2026-09-30; fund life 2009-07-24 -> 2026-09-30
tenure = (date(2026, 9, 30) - date(2025, 3, 21)).days
life = (date(2026, 9, 30) - date(2009, 7, 24)).days
chk("1 tenure", tenure == 558 and life == 6277,
    f"tenure={tenure}d ({tenure/365.25:.2f}y) life={life}d share={tenure/life*100:.2f}%")

# 2. Half-year split: 6M -0.30% and Q3 +3.13% imply Q2; benchmark 6M -1.09%, Q3 -9.84%
q2f = (1 - 0.0030) / (1 + 0.0313) - 1
q2b = (1 - 0.0109) / (1 - 0.0984) - 1
chk("2 q2 implied", abs(q2f * 100 - (-3.33)) < 0.05 and abs(q2b * 100 - 9.71) < 0.05,
    f"Q2 fund={q2f*100:.2f}% bench={q2b*100:.2f}% excess={100*(q2f-q2b):.2f}pp vs Q3 excess +12.97pp")

# 3. A-class printed excess (1-3) for all eight windows
rows = [  # (fund%, bench%, printed excess pp)
    (3.13, -9.84, 12.97), (-0.30, -1.09, 0.79), (10.97, -4.11, 15.08),
    (43.27, 17.98, 25.29), (43.27, -3.58, 46.85), (114.16, 19.79, 94.37),
    (161.79, 39.68, 122.11), (469.92, 39.90, 430.02)]
chk("3 excess all positive", all(abs((f - b) - e) < 0.005 for f, b, e in rows) and all(e > 0 for _, _, e in rows),
    "8 windows excess: " + "/".join(str(e) for _, _, e in rows))

# 4. Printed anomaly: A 3Y == 5Y == 43.27% -> implied segment (5Y ago to 3Y ago) = 0.00%
seg_a = 1.4327 / 1.4327 - 1
seg_e = 1.4326 / 1.4325 - 1
chk("4 3y=5y anomaly", seg_a == 0 and abs(seg_e * 100) < 0.02,
    f"A implied mid segment={seg_a*100:.2f}% ; E 3Y 43.25 vs 5Y 43.26 implied={seg_e*100:.2f}% (printed only)")

# 5. Long-window segment chain (A): inception->10Yago, 7Y->5Y, 3Y->1Y
s1 = 5.6992 / 2.6179 - 1
s2 = 2.1416 / 1.4327 - 1
s3 = 1.4327 / 1.1097 - 1
chk("5 segments", abs(s1 * 100 - 117.71) < 0.1 and abs(s2 * 100 - 49.48) < 0.1 and abs(s3 * 100 - 29.11) < 0.1,
    f"inception-to-10Yago={s1*100:.2f}% 7Y-to-5Y={s2*100:.2f}% 3Y-to-1Y={s3*100:.2f}%")

# 6. Q3 profit split: realised vs profit -> floating (yuan)
ra, pa = Decimal("1007411.46"), Decimal("50786156.48")
rc, pc = Decimal("-861494.14"), Decimal("20623854.58")
re_, pe = Decimal("35199.86"), Decimal("618174.42")
fa, fc, fe = pa - ra, pc - rc, pe - re_
tot_r, tot_p = ra + rc + re_, pa + pc + pe
chk("6 profit split", abs(fa - Decimal("49778745.02")) < Decimal("0.01") and tot_p == Decimal("72028185.48"),
    f"A float={fa} (~{float(fa/ra):.1f}x realised) total realised={tot_r} total profit={tot_p} float={tot_p-tot_r}")

# 7. Shares Q3: start/end per class, totals tie to section 2 total 977,270,429.93
a0, a1 = Decimal("591241220.37"), Decimal("636388003.60")
c0, c1 = Decimal("244121347.26"), Decimal("335444206.39")
e0, e1 = Decimal("5756511.99"), Decimal("5438219.94")
chk("7 shares", a1 + c1 + e1 == Decimal("977270429.93") and a0 + c0 + e0 == Decimal("841119079.62"),
    f"A {(float(a1/a0)-1)*100:.2f}% C {(float(c1/c0)-1)*100:.2f}% E {(float(e1/e0)-1)*100:.2f}% total {(float((a1+c1+e1)/(a0+c0+e0))-1)*100:.2f}%")

# 8. NAV: three classes sum; A shares x unit NAV vs stated NAV (rounding)
nav_sum = Decimal("2047627984.08") + Decimal("1007822200.65") + Decimal("19463532.88")
a_prod = a1 * Decimal("3.2176")
chk("8 nav", nav_sum == Decimal("3074913717.61") and abs(a_prod - Decimal("2047627984.08")) < Decimal("20000"),
    f"NAV sum={nav_sum} A shares*NAV={a_prod:.2f} diff={a_prod - Decimal('2047627984.08'):.2f}")

# 9. Asset mix: equity 76.62% of total assets / 76.79% of NAV; cash 23.29%; bonds zero
eq, tot_assets, cash = Decimal("2361212342.10"), Decimal("3081741811.46"), Decimal("717749489.15")
chk("9 asset mix", abs(float(eq / tot_assets) * 100 - 76.62) < 0.01 and abs(float(cash / tot_assets) * 100 - 23.29) < 0.01
    and abs(float(eq / nav_sum) * 100 - 76.79) < 0.01,
    f"equity/assets={float(eq/tot_assets)*100:.2f}% cash/assets={float(cash/tot_assets)*100:.2f}% equity/NAV={float(eq/nav_sum)*100:.2f}%")

# 10. Industry rows sum to 76.79; manufacturing share of equity
ind = [Decimal(x) for x in ("2.56", "3.55", "50.64", "0.02", "5.95", "3.27", "0.01", "7.13", "1.01", "2.66")]
chk("10 industry", sum(ind) == Decimal("76.80") or abs(sum(ind) - Decimal("76.79")) <= Decimal("0.01"),
    f"industry sum={sum(ind)} (printed total 76.79, rounding) manufacturing/equity={float(Decimal('50.64')/Decimal('76.79'))*100:.2f}%")

# 11. Top-10 sum; pharmacy pair equals wholesale/retail industry row 5.95
top10 = [Decimal(x) for x in ("3.28", "3.27", "3.18", "3.02", "2.98", "2.77", "2.77", "2.74", "2.67", "2.66")]
chk("11 top10", sum(top10) == Decimal("29.34") and Decimal("3.18") + Decimal("2.77") == Decimal("5.95"),
    f"top10 sum={sum(top10)}% top1 share of top10={float(Decimal('3.28')/sum(top10))*100:.2f}% pharmacy pair=5.95% == retail row 5.95%")

# 12. Inception factor vs unit NAV (dividend gap, register only); std-dev excess column A
ratio_a = 5.6992 / 3.2176
sd = [(1.11, 1.03, 0.08), (1.07, 1.03, 0.04), (1.05, 0.91, 0.14), (1.29, 0.91, 0.38),
      (1.22, 0.90, 0.32), (1.23, 0.94, 0.29), (1.19, 0.93, 0.26), (1.33, 1.11, 0.22)]
chk("12 factor & sd", abs(ratio_a - 1.7713) < 0.001 and all(abs((x - y) - d) < 0.005 for x, y, d in sd),
    f"A inception factor/unit NAV={ratio_a:.4f} (register only); sd excess column all ties")

print(f"ALL {ok} GROUPS PASSED")
