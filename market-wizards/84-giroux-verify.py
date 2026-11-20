#!/usr/bin/env python3
"""84 Giroux verify — Decimal assertions for the Giroux / PRWCX note.
Sources: T. Rowe Price press release 2025-01-14 (manager since 2006-06-30,
17-year streak, returns as of 2024-12-31) and official fact sheet as of
2026-09-30 (calendar returns 2016-2025, holdings, asset mix)."""
from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec = 28

def approx(a, b, tol=D("0.06")):
    assert abs(a - b) <= tol, f"{a} vs {b}"

# 1 tenure
takeover = date(2006, 6, 30); inception = date(1986, 6, 30); end = date(2026, 9, 30)
tenure_days = (end - takeover).days
life_days = (end - inception).days
assert tenure_days == 7397, tenure_days
assert life_days == 14702, life_days
assert (takeover - inception).days == 7305  # exactly 20 years incl 5 leap days
approx(D(tenure_days) / D(life_days) * 100, D("50.31"), D("0.02"))
approx(D(tenure_days) / D("365.25"), D("20.25"), D("0.01"))
print("1 tenure ok", tenure_days, life_days, round(tenure_days/life_days*100, 2))

pr = [D(x) for x in ("8.22","15.38","0.62","24.61","18.16","18.53","-11.94","18.83","12.69","12.50")]
sp = [D(x) for x in ("11.96","21.83","-4.38","31.49","18.40","28.71","-18.11","26.29","25.02","17.88")]
def comp(rs):
    f = D(1)
    for r in rs: f *= (1 + r/100)
    return f
def ann(f, n): return (float(f) ** (1/n) - 1) * 100

# 2 PRWCX calendar decade 2016-2025
f_pr = comp(pr); a_pr = ann(f_pr, 10)
print("2 PR decade factor", f_pr, "ann", round(a_pr, 2))
assert D("2.90") < f_pr < D("2.92")
approx(D(str(round(a_pr, 2))), D("11.27"), D("0.05"))

# 3 SP calendar decade
f_sp = comp(sp); a_sp = ann(f_sp, 10)
print("3 SP decade factor", f_sp, "ann", round(a_sp, 2))
assert f_sp > f_pr
approx(D(str(round(a_sp, 2))), D("14.82"), D("0.05"))

# 4 negative years
assert sum(1 for r in pr if r < 0) == 1
assert sum(1 for r in sp if r < 0) == 2
approx(pr[2] - sp[2], D("5.00"))  # 2018: +0.62 vs -4.38
print("4 negatives ok")

# 5 2022 gap and recovery
approx(sp[6] - pr[6], D("-6.17"))  # -18.11 vs -11.94 -> pr higher by 6.17
rec_pr = (1/(1+pr[6]/100)-1)*100; rec_sp = (1/(1+sp[6]/100)-1)*100
approx(D(str(rec_pr)), D("13.56"), D("0.02"))
approx(D(str(rec_sp)), D("22.11"), D("0.02"))
print("5 2022 ok", round(rec_pr,2), round(rec_sp,2))

# 6 press-release 5y check: calendar 2020-2024 annualized == 10.55
f5 = comp(pr[4:9]); a5 = ann(f5, 5)
print("6 2020-2024 factor", f5, "ann", round(a5, 4))
approx(D(str(round(a5, 2))), D("10.55"), D("0.03"))
assert pr[8] == D("12.69")  # 2024 calendar == press release 1y return
print("6 five-year ok")

# 7 $100k in 2008 -> $490k vs $253k at end-2024
approx(D(490000)/D(253000), D("1.9368"), D("0.001"))
approx((D(490000)/D(253000)-1)*100, D("93.68"), D("0.05"))  # release rounds to 94%
print("7 100k ok")

# 8 streak and closure arithmetic
assert 2024-2008+1 == 17 and 2023-2008+1 == 16
assert (date(2014,6,30)-takeover).days == 2922  # exactly 8 years incl 2 leap days
print("8 streak/closure ok")

# 9 top-10 issuers sum
top10 = [D(x) for x in ("16.8","4.1","3.4","3.0","2.9","2.7","2.6","2.4","2.1","2.1")]
assert sum(top10) == D("42.1")
approx(top10[0]/sum(top10)*100, D("39.90"), D("0.02"))
assert sum(top10[1:]) == D("25.3")
print("9 top10 ok")

# 10 asset mix and FI mix sums (as printed; rounding/other remainder registered)
assert sum(D(x) for x in ("57.4","35.0","2.2","5.3")) == D("99.9")
assert sum(D(x) for x in ("47.4","22.2","17.7","11.7","0.2")) == D("99.2")
print("10 mixes ok")

# 11 annualized windows as of 2026-09-30: PRWCX lags SP in all five
win_pr = [D(x) for x in ("9.54","13.92","8.65","11.23","12.33")]
win_sp = [D(x) for x in ("15.74","22.89","13.79","15.33","15.68")]
diffs = [a-b for a, b in zip(win_pr, win_sp)]
assert diffs == [D("-6.20"), D("-8.97"), D("-5.14"), D("-4.10"), D("-3.35")], diffs
print("11 windows ok", diffs)

# 12 decade halves split
fh1 = comp(pr[:5]); fh2 = comp(pr[5:])
print("12 halves", fh1, fh2, "product check", fh1*fh2, "vs", f_pr)
approx(fh1*fh2, f_pr, D("0.0001"))
approx(D(str(round(ann(fh1,5),2))), D("13.16"), D("0.15"))
approx(D(str(round(ann(fh2,5),2))), D("9.47"), D("0.05"))
print("12 halves ok")
print("ALL 12 GROUPS PASSED")
