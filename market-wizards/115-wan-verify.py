#!/usr/bin/env python3
# 115 Wan Jianjun (Huaan Reverse Strategy 040035) verify script
# Source: Huaan Reverse Strategy Q3 2026 report (cninfo PDF)
from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec = 28
ok = 0
def chk(cond, label):
    global ok
    assert cond, f"FAIL: {label}"
    ok += 1
    print(f"  ok {label}")
def seg(total_pct, later_pct):
    return ((D(str(total_pct)) / 100 + 1) / (D(str(later_pct)) / 100 + 1) - 1) * 100

print("G1 identity and tenure")
fund_start, mgr_start, end = date(2012, 8, 16), date(2022, 1, 26), date(2026, 9, 30)
life = (end - fund_start).days; tenure = (end - mgr_start).days; pre = life - tenure
chk(life == 5158, f"life {life} days")
chk(tenure == 1708, f"tenure {tenure} days")
chk(pre == 3450, f"pre {pre} days")
chk(abs(D(tenure) / D(life) * 100 - D("33.11")) < D("0.01"), f"tenure share {D(tenure)/D(life)*100:.2f}%")
chk(abs(D(life) / D("365.25") - D("14.12")) < D("0.01"), "life ~14.12y")
chk(abs(D(tenure) / D("365.25") - D("4.68")) < D("0.01"), "tenure ~4.68y")

print("G2 Q3 and half split (A)")
q3, bench_q3 = D("-29.64"), D("-9.97")
chk(q3 - bench_q3 == D("-19.67"), "Q3 excess -19.67 matches print")
half, bench_half = D("10.58"), D("-1.33")
q2 = seg(half, q3); bench_q2 = seg(bench_half, bench_q3)
chk(abs(q2 - D("57.16")) < D("0.01"), f"Q2 implied {q2:.2f}%")
chk(abs(bench_q2 - D("9.60")) < D("0.01"), f"bench Q2 implied {bench_q2:.2f}%")
chk(abs((q2 - bench_q2) - D("47.57")) < D("0.02"), f"Q2 excess ~{q2-bench_q2:.2f}pp")

print("G3 full table excess (A, 8 windows)")
rows = [("3M", "-29.64", "-9.97", "-19.67"), ("6M", "10.58", "-1.33", "11.91"),
        ("1Y", "3.47", "-4.50", "7.97"), ("3Y", "15.99", "16.27", "-0.28"),
        ("5Y", "-13.96", "-6.05", "-7.91"), ("7Y", "107.04", "15.46", "91.58"),
        ("10Y", "142.62", "31.96", "110.66"), ("SI", "798.37", "78.46", "719.91")]
for name, f, b, ex in rows:
    chk(D(f) - D(b) == D(ex), f"{name} excess {ex} matches print")
neg = [r for r in rows if D(r[3]) < 0]
chk(len(neg) == 3, "8 windows: exactly 3 negative excess (3M, 3Y, 5Y)")

print("G4 1Y split")
prior9 = seg(D("3.47"), q3); bench_prior9 = seg(D("-4.50"), bench_q3)
chk(abs(prior9 - D("47.06")) < D("0.01"), f"prior 9M implied {prior9:.2f}%")
chk(abs(bench_prior9 - D("6.08")) < D("0.01"), f"bench prior 9M {bench_prior9:.2f}%")
chk(abs((prior9 - bench_prior9) - D("40.98")) < D("0.02"), "prior 9M lead ~40.98pp")

print("G5 long splits")
s5_10 = seg(D("142.62"), D("-13.96")); b5_10 = seg(D("31.96"), D("-6.05"))
chk(abs(s5_10 - D("181.98")) < D("0.02"), f"5-10y ago segment {s5_10:.2f}%")
chk(abs(b5_10 - D("40.46")) < D("0.02"), f"bench same {b5_10:.2f}%")
s3_5 = seg(D("-13.96"), D("15.99")); b3_5 = seg(D("-6.05"), D("16.27"))
chk(abs(s3_5 - D("-25.82")) < D("0.02"), f"3-5y ago segment {s3_5:.2f}%")
chk(abs(b3_5 - D("-19.20")) < D("0.02"), f"bench same {b3_5:.2f}%")
s5_7 = seg(D("107.04"), D("-13.96")); b5_7 = seg(D("15.46"), D("-6.05"))
chk(abs(s5_7 - D("140.63")) < D("0.02"), f"5-7y ago segment {s5_7:.2f}%")
chk(abs(b5_7 - D("22.89")) < D("0.02"), f"bench same {b5_7:.2f}%")
s_pre10 = seg(D("798.37"), D("142.62")); b_pre10 = seg(D("78.46"), D("31.96"))
chk(abs(s_pre10 - D("270.28")) < D("0.02"), f"pre-10y segment {s_pre10:.2f}%")
chk(abs(b_pre10 - D("35.24")) < D("0.02"), f"bench same {b_pre10:.2f}%")

print("G6 recovery price")
need = (1 / (1 + q3 / 100) - 1) * 100
chk(abs(need - D("42.13")) < D("0.01"), f"drop 29.64% recovery needs {need:.2f}%")
need5 = (1 / (1 + D("-13.96") / 100) - 1) * 100
chk(abs(need5 - D("16.23")) < D("0.01"), f"5Y drop 13.96% recovery needs {need5:.2f}%")

print("G7 profit composition (A+C)")
realized = D("-11482679.41") + D("-122918.92")
profit = D("-698934967.41") + D("-3893322.81")
fv = profit - realized
chk(realized == D("-11605598.33"), f"realized total {realized} (~-0.12 yi)")
chk(profit == D("-702828290.22"), f"profit total {profit} (~-70.28 yi x0.1 = -7.03 yi)")
chk(abs(fv - D("-691222691.89")) < D("0.01"), f"FV change {fv} (~-6.91 yi)")
chk(abs(abs(fv) / abs(realized) - D("59.56")) < D("0.01"), f"FV loss ~{abs(fv)/abs(realized):.2f}x realized loss")
nav_total = D("1616564332.14") + D("5725300.47")
chk(nav_total == D("1622289632.61"), f"NAV total {nav_total} (~16.22 yi)")
chk(abs(profit / nav_total * 100 - D("-43.32")) < D("0.01"), f"profit ~{profit/nav_total*100:.2f}% of end NAV")

print("G8 asset mix")
total_assets = D("1640995188.47")
equity = D("1167669551.19")
chk(abs(equity / total_assets * 100 - D("71.16")) < D("0.01"), "equity 71.16% of total assets matches print")
chk(abs(equity / nav_total * 100 - D("71.98")) < D("0.01"), f"equity {equity/nav_total*100:.2f}% of NAV")
cash = D("471964485.09")
chk(abs(cash / total_assets * 100 - D("28.76")) < D("0.01"), "cash 28.76% of total assets matches print")

print("G9 industry and top10")
ind = [D("7.66"), D("32.32"), D("0.51"), D("0.96"), D("4.58"), D("3.78"), D("14.48"), D("7.70")]
chk(sum(ind) == D("71.99"), f"industry rows sum {sum(ind)} vs equity/NAV 71.98 diff 0.01 register only")
# recompute from amounts
mfg = D("524275067.34")
chk(abs(mfg / equity * 100 - D("44.90")) < D("0.01"), f"manufacturing {mfg/equity*100:.2f}% of equity")
fin = D("234832843.50")
chk(abs(fin / equity * 100 - D("20.11")) < D("0.01"), f"finance {fin/equity*100:.2f}% of equity")
top10 = [D("4.67"), D("4.15"), D("3.72"), D("3.47"), D("3.12"), D("2.99"), D("2.88"), D("2.65"), D("2.50"), D("2.49")]
chk(sum(top10) == D("32.64"), f"top10 sum {sum(top10)}%")
chk(abs(D("4.67") / sum(top10) * 100 - D("14.31")) < D("0.01"), "top1 ~14.31% of top10")

print("G10 shares")
a0, a1 = D("270150207.64"), D("255581093.21")
c0, c1 = D("1364917.49"), D("932384.24")
chk(a1 - a0 == D("-14569114.43"), "A net -14,569,114.43 shares")
chk(abs((a1 - a0) / a0 * 100 - D("-5.39")) < D("0.01"), f"A net {(a1-a0)/a0*100:.2f}%")
chk(c1 - c0 == D("-432533.25"), "C net -432,533.25 shares")
chk(abs((c1 - c0) / c0 * 100 - D("-31.69")) < D("0.01"), f"C net {(c1-c0)/c0*100:.2f}%")
chk(a1 + c1 == D("256513477.45"), "end total matches section 2 print")
chk(abs(((a1 + c1) - (a0 + c0)) / (a0 + c0) * 100 - D("-5.53")) < D("0.01"), "total net ~-5.53%")

print("G11 volatility")
chk(abs(D("2.70") / D("1.03") - D("2.62")) < D("0.01"), "Q3 vol 2.70 ~2.62x bench 1.03")
vols = [(D("2.70"), D("1.03")), (D("2.65"), D("1.03")), (D("2.21"), D("0.91")), (D("1.58"), D("0.91")), (D("1.48"), D("0.89")), (D("1.48"), D("0.94")), (D("1.39"), D("0.92")), (D("1.51"), D("1.07"))]
chk(all(f > b for f, b in vols), "all 8 windows vol above bench")

print("G12 NAV registration")
chk(abs((D("798.37") / 100 + 1) - D("8.9837")) < D("0.0001"), "since-inception factor 8.9837")
chk(D("6.325") != D("8.9837"), "unit NAV 6.325 vs factor 8.9837 differ, register only")

print(f"ALL {ok} ASSERTIONS PASSED")
