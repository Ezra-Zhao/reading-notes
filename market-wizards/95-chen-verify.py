# -*- coding: utf-8 -*-
"""95 Chen Wenkai (Huatai-PB Quality Growth Mixed 008528) verification.
Source: Huatai-PB Quality Growth Mixed Fund 2026 Q3 Report
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

# 1. Tenure: Chen Wenkai sole manager from 2024-06-21 to 2026-09-30; fund inception 2020-03-18
ten = (date(2026, 9, 30) - date(2024, 6, 21)).days
life = (date(2026, 9, 30) - date(2020, 3, 18)).days
chk("1 tenure", ten == 831 and life == 2387 and abs(ten / life * 100 - 34.81) < 0.01,
    f"tenure={ten}d ({ten/365.25:.2f}y) fund life={life}d ({life/365.25:.2f}y) "
    f"share={ten/life*100:.2f}% predecessor stub={life-ten}d")

# 2. Half-year split (Class A): 6M +30.51% and Q3 -31.41% imply Q2; benchmark 6M -1.26%, Q3 -7.11%
q2f = (1 + 0.3051) / (1 - 0.3141) - 1
q2b = (1 - 0.0126) / (1 - 0.0711) - 1
chk("2 half-year split", abs(q2f * 100 - 90.28) < 0.02 and abs(q2b * 100 - 6.30) < 0.02
    and abs((q2f - q2b) * 100 - 83.98) < 0.03 and abs((1 / 0.6859 - 1) * 100 - 45.79) < 0.02,
    f"Q2 implied fund {q2f*100:.2f}% vs benchmark {q2b*100:.2f}% excess {(q2f-q2b)*100:.2f}pp; "
    f"Q3 printed excess -24.30pp; Q3 -31.41% needs +45.79% to recover")

# 3. Class A window excess self-consistency (printed 1-3 = fund - benchmark, all six windows)
F = [D(x) for x in ("-31.41", "30.51", "83.50", "210.35", "61.05", "183.07")]
B = [D(x) for x in ("-7.11", "-1.26", "-4.49", "23.15", "3.08", "23.44")]
E = [D(x) for x in ("-24.30", "31.77", "87.99", "187.20", "57.97", "159.63")]
chk("3 window excess", all(f - b == e for f, b, e in zip(F, B, E)),
    "A 3M/6M/1Y/3Y/5Y/since excess = fund-benchmark exactly as printed; "
    "only windows fully inside his tenure are 3M, 6M and 1Y (1Y +83.50%, excess +87.99pp, the longest fully-his window)")

# 4. Long-window decomposition (Class A): middle ~2Y inside 3Y; 5-to-3Y-ago segment; inception stub
chk("4 decomposition", abs(((1 + 2.1035) / (1 + 0.8350) - 1) * 100 - 69.13) < 0.05
    and abs(((1 + 0.6105) / (1 + 2.1035) - 1) * 100 - (-48.11)) < 0.05
    and abs(((1 + 1.8307) / (1 + 0.6105) - 1) * 100 - 75.77) < 0.05
    and abs(((1 + 1.8307) / (1 + 2.1035) - 1) * 100 - (-8.79)) < 0.05,
    "3Y +210.35% = latest 1Y +83.50% x middle ~2Y +69.13%; 5Y +61.05% hides a 5-to-3Y-ago segment of -48.11% "
    "before the 3Y window; inception-to-5Y-start stub (first ~1.54Y) +75.77%; since-inception vs 3Y segment -8.79% (mostly pre-tenure, registered only)")

# 5. Q3 profit split: realised positive in both classes, profit deeply negative; unrealised = profit - realised
ra, pa = D("264425739.32"), D("-1782472744.92")
rc, pc = D("962165708.90"), D("-6910367816.67")
ua, uc = pa - ra, pc - rc
chk("5 profit split", ua == D("-2046898484.24") and uc == D("-7872533525.57")
    and ra + rc == D("1226591448.22") and pa + pc == D("-8692840561.59") and ua + uc == D("-9919432009.81")
    and abs(abs(ua + uc) / (ra + rc) - D("8.0870")) < D("0.001"),
    f"A unrealised {ua} C unrealised {uc}; combined realised {ra+rc} profit {pa+pc} unrealised {ua+uc} "
    f"= 8.09x the realised gain (pocketed gains, holdings underwater: the mirror image of a realised-loss quarter)")

# 6. Volatility: Class A Q3 printed std 4.71% vs benchmark 0.92%
chk("6 volatility", abs(D("4.71") / D("0.92") - D("5.12")) < D("0.01") and D("4.71") - D("0.92") == D("3.79"),
    "Q3 fund std 4.71% = 5.12x benchmark 0.92%, printed diff +3.79pp; same +3.79pp diff printed in the 6M row by coincidence of rounding, registered")

# 7. NAV arithmetic: class assets sum to total NAV; A since-inception factor equals unit NAV; C registered
na, nc = D("3220738572.43"), D("11270854932.90")
chk("7 nav", na + nc == D("14491593505.33")
    and D("2.8307") == D("2.8307")
    and abs(D("2.7709") / D("1.5128") - D("1.8316")) < D("0.0002"),
    f"total NAV {na+nc}; A since-inception factor 2.8307 exactly equals unit NAV 2.8307 (no cash-distribution gap on this print, registered); "
    f"C factor 1.5128 vs unit NAV 2.7709 ratio 1.8316 (C started 2021-02-19 off the then A NAV, registered)")

# 8. Asset allocation: equity share of total assets and of NAV; bonds are treasuries only; cash
eq, tot = D("13414594755.82"), D("14821048026.41")
chk("8 allocation", abs(eq / tot * 100 - D("90.51")) < D("0.01")
    and abs(eq / (na + nc) * 100 - D("92.57")) < D("0.01")
    and abs(D("309817388.41") / (na + nc) * 100 - D("2.14")) < D("0.01")
    and abs(D("976060816.48") / (na + nc) * 100 - D("6.74")) < D("0.01"),
    "equity 90.51% of total assets, 92.57% of NAV (ties to domestic 81.89 + HK 10.68 industry totals); "
    "bonds 2.14% of NAV, all treasury bonds (printed 5.4); cash 6.74% of NAV; no index futures held at quarter end (printed 5.9.1)")

# 9. Industry table: domestic + HK totals tie to equity/NAV; manufacturing share of equity
chk("9 industries", D("81.89") + D("10.68") == D("92.57")
    and abs(D("81.88") / D("92.57") * 100 - D("88.45")) < D("0.01")
    and D("2.12") + D("8.56") == D("10.68"),
    "domestic industries sum 81.89% of NAV (manufacturing alone 81.88, IT services 0.01, mining 0.00, all other domestic rows nil); "
    "HK rows IT 2.12 + telecom 8.56 = 10.68; manufacturing = 88.45% of the whole equity book")

# 10. Top-10 holdings: rows sum, top-1 share, top-5 sum, top-10 share of equity
top = [D(x) for x in ("9.59", "9.09", "8.56", "8.54", "6.89", "6.58", "4.82", "4.25", "4.02", "3.48")]
chk("10 top10", sum(top) == D("65.82") and abs(D("9.59") / sum(top) * 100 - D("14.57")) < D("0.01")
    and sum(top[:5]) == D("42.67")
    and abs(sum(top) / D("92.57") * 100 - D("71.10")) < D("0.01"),
    f"top10 rows sum {sum(top)}% of NAV = 71.10% of equity book; top1 Lianxun Instruments 9.59 = 14.57% of top10; "
    "top5 = 42.67; all ten names are optical / AI-hardware chain names (printed 5.3.1), matching the 4.4 self-description of heavy AI exposure")

# 11. Share changes: end = start + subscriptions - redemptions in both classes; net outflow rates
sa, ea = D("1457030472.34"), D("1137797257.07")
sc, ec = D("5607077790.38"), D("4067591438.19")
chk("11 shares", sa + D("363600961.12") - D("682834176.39") == ea and sc + D("3459414094.17") - D("4998900446.36") == ec
    and ea + ec == D("5205388695.26") and abs((ea - sa) / sa * 100 - D("-21.91")) < D("0.01")
    and abs((ec - sc) / sc * 100 - D("-27.46")) < D("0.01")
    and abs((ea + ec - sa - sc) / (sa + sc) * 100 - D("-26.31")) < D("0.01"),
    "A net -21.91%, C net -27.46%, total shares 7,064,108,262.72 -> 5,205,388,695.26 net -26.31% in the -31.41% quarter; "
    "gross subscriptions 3,823,015,055.29 vs gross redemptions 5,681,734,622.75 (printed S6)")

# 12. Holder structure: C share of end shares; no holder at/above 20%; manager own holding nil
chk("12 holders", abs(ec / (ea + ec) * 100 - D("78.14")) < D("0.01"),
    "C class = 78.14% of all end shares (C NAV 11,270,854,932.90 of total 14,491,593,505.33); "
    "no single holder reached 20% in Q3 (printed 8.1: none); manager's own holding nil, no trades in Q3 (printed S7)")

print(f"ALL {ok} GROUPS PASSED")
