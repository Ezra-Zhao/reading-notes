# -*- coding: utf-8 -*-
"""93 Fu Beijia (Zhong Ou Potential Value Flexible Allocation Mixed 001810) verification.
Source: Zhong Ou Potential Value Flexible Allocation Mixed Fund 2026 Q3 Report
(report period 2026-07-01 to 2026-09-30, sent 2026-10-27, cninfo PDF).
All performance figures are the report's printed Class A rows unless noted.
"""
from datetime import date
from decimal import Decimal as D

ok = 0
def chk(name, cond, detail=""):
    global ok
    assert cond, f"FAIL {name}: {detail}"
    ok += 1
    print(f"PASS {name} {detail}")

# 1. Tenure: Fu Beijia sole manager from 2025-03-27 to 2026-09-30; fund inception 2015-09-30
ten = (date(2026, 9, 30) - date(2025, 3, 27)).days
life = (date(2026, 9, 30) - date(2015, 9, 30)).days
chk("1 tenure", ten == 552 and life == 4018 and abs(ten / life * 100 - 13.74) < 0.01,
    f"tenure={ten}d ({ten/365.25:.2f}y) fund life={life}d ({life/365.25:.2f}y, exactly 11 calendar years) "
    f"share={ten/life*100:.2f}% predecessor stub={life-ten}d")

# 2. Half-year split (Class A): 6M -14.22% and Q3 -4.97% imply Q2; benchmark 6M -0.54%, Q3 -10.59%
q2f = (1 - 0.1422) / (1 - 0.0497) - 1
q2b = (1 - 0.0054) / (1 - 0.1059) - 1
chk("2 half-year split", abs(q2f * 100 - (-9.73)) < 0.02 and abs(q2b * 100 - 11.24) < 0.02
    and abs((q2f - q2b) * 100 - (-20.97)) < 0.03 and abs((1 / 0.8578 - 1) * 100 - 16.58) < 0.02,
    f"Q2 implied fund {q2f*100:.2f}% vs benchmark {q2b*100:.2f}% excess {(q2f-q2b)*100:.2f}pp; "
    f"Q3 printed excess +5.62pp; 6M -14.22% needs +16.58% to recover, Q3 -4.97% needs +5.23%")

# 3. Class A window excess self-consistency (printed 1-3 = fund - benchmark, all eight windows)
F = [D(x) for x in ("-4.97", "-14.22", "-5.38", "13.88", "17.04", "86.30", "124.91", "157.75")]
B = [D(x) for x in ("-10.59", "-0.54", "1.54", "22.67", "9.21", "38.41", "21.02", "26.65")]
E = [D(x) for x in ("5.62", "-13.68", "-6.92", "-8.79", "7.83", "47.89", "103.89", "131.10")]
chk("3 window excess", all(f - b == e for f, b, e in zip(F, B, E)),
    "A 3M/6M/1Y/3Y/5Y/7Y/10Y/since excess = fund-benchmark exactly as printed; "
    "only windows fully inside her tenure are 3M, 6M and 1Y (1Y -5.38%, excess -6.92pp)")

# 4. Long-window decomposition (Class A): earliest 5Y inside 10Y; 5-to-7Y-ago segment; inception stub
chk("4 decomposition", abs(((1 + 1.2491) / (1 + 0.1704) - 1) * 100 - 92.17) < 0.05
    and abs(((1 + 0.8630) / (1 + 0.1704) - 1) * 100 - 59.18) < 0.05
    and abs(((1 + 1.5775) / (1 + 1.2491) - 1) * 100 - 14.60) < 0.05
    and abs(((1 + 0.1388) / (1 - 0.0538) - 1) * 100 - 20.36) < 0.05,
    "10Y +124.91% = earliest 5Y +92.17% x latest 5Y +17.04%; 7Y vs 5Y segment +59.18%; "
    "inception-to-10Y-start stub (first ~1Y) +14.60%; 3Y vs 1Y middle ~2Y +20.36% (all pre-/mostly pre-tenure, registered only)")

# 5. Q3 profit split: realised and profit both negative in both classes; unrealised = profit - realised
ra, pa = D("-24307406.27"), D("-45707402.88")
rc, pc = D("-14732448.52"), D("-22978677.98")
ua, uc = pa - ra, pc - rc
chk("5 profit split", ua == D("-21399996.61") and uc == D("-8246229.46")
    and ra + rc == D("-39039854.79") and pa + pc == D("-68686080.86") and ua + uc == D("-29646226.07")
    and abs(abs(ua + uc) / abs(ra + rc) - D("0.7594")) < D("0.001"),
    f"A unrealised {ua} C unrealised {uc}; combined realised {ra+rc} profit {pa+pc} unrealised {ua+uc} "
    f"= 75.94% of realised loss (both legs negative: sold at a loss, holdings also down)")

# 6. Futures offset: index-futures realised gain in Q3 vs combined loss; no position at quarter end
chk("6 futures", abs(D("8560110.85") / abs(pa + pc) * 100 - D("12.46")) < D("0.01"),
    "index futures Q3 gain 8,560,110.85 = 12.46% of combined profit loss magnitude; quarter-end futures position nil (printed)")

# 7. NAV arithmetic: class assets sum to total NAV; unit NAV vs since-inception factor (A and C registered)
na, nc = D("823834958.64"), D("424524444.55")
chk("7 nav", na + nc == D("1248359403.19")
    and abs(D("2.5775") / D("2.2225") - D("1.1597")) < D("0.0002")
    and abs(D("2.0739") / D("1.6384") - D("1.2658")) < D("0.0002"),
    f"total NAV {na+nc}; A since-inception factor 2.5775 vs unit NAV 2.2225 ratio 1.1597 (cash-distribution basis, registered); "
    f"C factor 1.6384 vs unit NAV 2.0739 ratio 1.2658 (C started 2018-03-14 off the then A NAV, registered)")

# 8. Asset allocation: equity share of total assets and of NAV; cash; bonds nil vs benchmark bond leg
eq, tot = D("1107540803.55"), D("1251301224.92")
chk("8 allocation", abs(eq / tot * 100 - D("88.51")) < D("0.01")
    and abs(eq / (na + nc) * 100 - D("88.72")) < D("0.01")
    and abs(D("142295366.53") / (na + nc) * 100 - D("11.40")) < D("0.01"),
    "equity 88.51% of total assets, 88.72% of NAV (ties to industry-table total); cash 11.40% of NAV; bonds nil "
    "while benchmark carries a bond leg (40% old / 15% new after 2026-09-21 mid-quarter change, seam registered)")

# 9. Industry table: rows sum to 88.72; manufacturing share of equity; finance vs two insurers
ind = [D("0.00"), D("67.08"), D("0.04"), D("4.02"), D("1.14"), D("16.44"), D("0.00")]
chk("9 industries", sum(ind) == D("88.72") and abs(D("67.08") / D("88.72") * 100 - D("75.61")) < D("0.01")
    and D("8.73") + D("7.70") == D("16.43"),
    "industry rows (mining 0.00 + manufacturing 67.08 + utilities 0.04 + transport 4.02 + IT 1.14 + finance 16.44 + sci-tech 0.00) "
    "= 88.72 exactly; manufacturing = 75.61% of equity book; finance 16.44 vs Ping An 8.73 + CPIC 7.70 = 16.43 (0.01 rounding, registered)")

# 10. Top-10 holdings: rows sum, top-1 share, machinery trio, chemical pair, top-10 share of equity
top = [D(x) for x in ("8.73", "8.59", "7.83", "7.70", "7.18", "5.71", "4.80", "3.62", "3.35", "3.18")]
chk("10 top10", sum(top) == D("60.69") and abs(D("8.73") / sum(top) * 100 - D("14.38")) < D("0.01")
    and D("5.71") + D("4.80") + D("3.62") == D("14.13") and D("8.59") + D("3.35") == D("11.94")
    and abs(sum(top) / D("88.72") * 100 - D("68.41")) < D("0.01"),
    f"top10 rows sum {sum(top)}% of NAV = 68.41% of equity book; top1 Ping An 8.73 = 14.38% of top10; "
    "machinery trio (Weichai 5.71 + CIMC Vehicles 4.80 + XCMG 3.62) = 14.13; chemical pair (Rongsheng 8.59 + Tongkun 3.35) = 11.94")

# 11. Share changes: end = start + subscriptions - redemptions in both classes; net outflow rates
sa, ea = D("415362000.37"), D("370676759.42")
sc, ec = D("248919504.37"), D("204702878.82")
chk("11 shares", sa + D("8191730.22") - D("52876971.17") == ea and sc + D("6668996.69") - D("50885622.24") == ec
    and ea + ec == D("575379638.24") and abs((ea - sa) / sa * 100 - D("-10.76")) < D("0.01")
    and abs((ec - sc) / sc * 100 - D("-17.76")) < D("0.01")
    and abs((ea + ec - sa - sc) / (sa + sc) * 100 - D("-13.38")) < D("0.01"),
    "A net -10.76%, C net -17.76%, total shares 664,281,504.74 -> 575,379,638.24 net -13.38% in a quarter the fund beat its benchmark by 5.62pp")

# 12. Two anchor institutions: combined holding, zero trades all quarter; manager own holding nil
h = D("119731171.61") + D("150629612.12")
chk("12 anchors", h == D("270360783.73") and abs(h / (ea + ec) * 100 - D("46.99")) < D("0.01"),
    "two institutions hold 119,731,171.61 (20.81%) + 150,629,612.12 (26.18%) = 270,360,783.73 = 46.99% of all shares, "
    "both with zero subscriptions and zero redemptions in Q3 (printed); manager's own holding nil, no trades in Q3 (printed S7)")

print(f"ALL {ok} GROUPS PASSED")
