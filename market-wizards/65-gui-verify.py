#!/usr/bin/env python3
"""Verify arithmetic in note 65 (Gui Kai / Harvest Emerging Industry).

All inputs are figures printed in the 2026 Q3 report of
Harvest Emerging Industry Stock Fund (000751), period ended
2026-09-30, dispatched 2026-10-27: identity in section 4.1,
financials in 3.1, performance in 3.2.1, portfolio in 5,
shares in 6, manager holdings in 7.
This script only checks internal arithmetic consistency and
derived windows. Clean-room, self-written.
"""
from datetime import date

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure: start 2018-12-04 to 2026-09-30; fund effective 2014-09-17.
d_start, d_end, d_eff = date(2018,12,4), date(2026,9,30), date(2014,9,17)
tenure = (d_end - d_start).days
pre = (d_start - d_eff).days
check("1 tenure days 2857 (~7.82y)", tenure == 2857 and abs(tenure/365.25-7.82)<0.01)
check("1 fund predates manager by 1539 days", pre == 1539)
print("   tenure", tenure, "pre", pre)

# 2. Excess arithmetic: growth - benchmark = stated excess, all windows.
W = {"3m":(-23.99,-25.78,1.79),"6m":(14.52,2.40,12.12),"1y":(15.47,-5.32,20.79),
     "3y":(30.20,38.28,-8.08),"5y":(-12.11,-6.21,-5.90),"7y":(61.72,53.65,8.07),
     "10y":(188.15,40.27,147.88),"since":(344.90,80.33,264.57)}
check("2 excess all windows", all(abs(g-b-e)<0.005 for g,b,e in W.values()))

# 3. Q2 2026 implied: 6m factor / Q3 factor - 1.
q2 = 1.1452/0.7601 - 1
check("3 implied Q2 2026 ~+50.65%", abs(q2*100-50.65)<0.02)
print("   Q2 implied", round(q2*100,2))

# 4. Window splits.
e2 = 0.8789/1.3020 - 1
check("4 earliest 2y of 5y ~-32.50%", abs(e2*100+32.50)<0.02)
e5 = 2.8815/0.8789 - 1
check("4 earliest 5y of 10y ~+227.87%", abs(e5*100-227.87)<0.05)
print("   e2", round(e2*100,2), "e5", round(e5*100,2))

# 5. Prior half-year inside 1y; recovery after -23.99%.
ph = 1.1547/1.1452 - 1
check("5 prior 6m inside 1y ~+0.83%", abs(ph*100-0.83)<0.02)
rec = 1/0.7601 - 1
check("5 recovery from -23.99% ~+31.56%", abs(rec*100-31.56)<0.02)
# Since-inception factor vs ending NAV (no distributions adjustment check: 1+344.90% = 4.4490)
check("5 since factor 4.4490 equals ending NAV 4.449", abs(4.4490-4.449)<0.0005)

# 6. Profit split.
real, prof = 434815027.20, -1211835581.69
unreal = prof - real
check("6 unrealized ~-1,646,650,608.89, ~3.79x realized",
      abs(unreal+1646650608.89)<0.02 and abs(abs(unreal)/real-3.79)<0.01)
print("   unreal", round(unreal,2), "ratio", round(abs(unreal)/real,4))

# 7. Share reconciliation exact; net redemption %.
check("7 shares reconcile", abs(900940768.55+21856533.27-88762885.93-834034415.89)<0.01)
net = 834034415.89-900940768.55
check("7 net redemption 66,906,352.66 = 7.43% of beginning",
      abs(-net-66906352.66)<0.01 and abs(-net/900940768.55*100-7.43)<0.01)

# 8. NAV x shares vs net assets (NAV rounded to 3 dp).
prod = 834034415.89*4.449
check("8 shares*NAV within 0.01% of net assets", abs(prod-3710571811.85)/3710571811.85<0.0001)
print("   prod", round(prod,2))

# 9. Asset composition sums; equity shares.
parts = [3248934876.46,22893879.78,444193796.05,3945400.95]
check("9 assets sum to 3,719,967,953.24", abs(sum(parts)-3719967953.24)<0.01)
check("9 equity/total ~87.34%", abs(parts[0]/3719967953.24*100-87.34)<0.01)
check("9 equity/NAV ~87.56%", abs(parts[0]/3710571811.85*100-87.56)<0.01)
check("9 bonds/NAV ~0.62%", abs(parts[1]/3710571811.85*100-0.62)<0.01)

# 10. Industry rows sum to equity; manufacturing + IT.
ind = [39927914.10,2683039868.04,33151482.00,317864571.04,2145.52,174948895.76]
check("10 industry rows sum to equity", abs(sum(ind)-3248934876.46)<0.01)
check("10 manufacturing 72.31% + IT 8.57% = 80.88pp of 87.56%",
      abs(72.31+8.57-80.88)<1e-9)

# 11. Top 10 concentration.
top = [8.26,6.70,6.50,5.96,5.25,4.71,4.15,3.66,2.83,2.67]
check("11 top10 sum 50.69% of NAV", abs(sum(top)-50.69)<0.01)
check("11 top3 sum 21.46%", abs(top[0]+top[1]+top[2]-21.46)<1e-9)
check("11 top10 ~57.89% of equity (50.69/87.56)", abs(sum(top)/87.56*100-57.89)<0.02)

# 12. Weighted-avg implied shares; single bond = all bonds; other assets sum.
wa = 1211835581.69/1.4261
check("12 implied avg shares between end and beginning", 834034415.89 < wa < 900940768.55)
check("12 only bond 22,893,879.78 = all fixed income", abs(22893879.78-22893879.78)<0.01)
oa = [957775.17,2476829.56,510796.22]
check("12 other assets sum 3,945,400.95", abs(sum(oa)-3945400.95)<0.01)
print("   wAvg", round(wa))

print("ALL PASSED" if ok else "SOME FAILED")
