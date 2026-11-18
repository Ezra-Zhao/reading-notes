#!/usr/bin/env python3
"""Verify arithmetic in note 63 (Zhang Qinghua / E Fund Xin Shouyi).

All inputs are figures printed in the 2026 Q3 report of
E Fund Xin Shouyi Flexible Allocation Mixed Fund (001216 A /
001217 C), period ended 2026-09-30, dispatched 2026-10-27:
identity in section 4.1, financials in 3.1, performance in
3.2.1, portfolio in 5, shares in 6, manager holdings in 7.
This script only checks internal arithmetic consistency and
derived windows. Clean-room, self-written.
"""
from datetime import date

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure: start 2018-12-25 to 2026-09-30; fund effective 2015-04-17.
d_start, d_end, d_eff = date(2018,12,25), date(2026,9,30), date(2015,4,17)
tenure = (d_end - d_start).days
pre = (d_start - d_eff).days
check("1 tenure days 2836 (~7.77y)", tenure == 2836 and abs(tenure/365.25-7.77)<0.01)
check("1 fund predates manager by 1348 days", pre == 1348)
print("   tenure", tenure, "pre", pre)

# 2. Excess arithmetic A: growth - benchmark = stated excess, all windows.
A = {"3m":(-31.68,-9.34,-22.34),"6m":(17.97,-1.15,19.12),"1y":(20.09,-4.12,24.21),
     "3y":(32.07,27.82,4.25),"5y":(4.28,36.61,-32.33),"7y":(125.64,45.41,80.23),
     "10y":(276.26,58.60,217.66),"since":(325.55,65.37,260.18)}
check("2 A excess all windows", all(abs(g-b-e)<0.005 for g,b,e in A.values()))

# 3. Q2 2026 implied: 6m factor / Q3 factor - 1.
q2 = 1.1797/0.6832 - 1
check("3 implied Q2 2026 ~+72.67%", abs(q2*100-72.67)<0.02)
print("   Q2 implied", round(q2*100,2))

# 4. Five-year split: earliest 2y = 5y factor / 3y factor - 1.
e2 = 1.0428/1.3207 - 1
check("4 earliest 2y of 5y ~-21.04%", abs(e2*100+21.04)<0.02)
# Ten-year split: earliest 5y = 10y factor / 5y factor - 1.
e5 = 3.7626/1.0428 - 1
check("4 earliest 5y of 10y ~+260.81%", abs(e5*100-260.81)<0.05)
print("   e2", round(e2*100,2), "e5", round(e5*100,2))

# 5. Prior half-year inside 1y: 1y factor / 6m factor - 1.
ph = 1.2009/1.1797 - 1
check("5 prior 6m inside 1y ~+1.80%", abs(ph*100-1.80)<0.02)
# Recovery needed after -31.68%.
rec = 1/0.6832 - 1
check("5 recovery from -31.68% ~+46.37%", abs(rec*100-46.37)<0.02)

# 6. Profit split combined A+C.
real = 334827468.85 + 83867792.10
prof = -723485474.55 - 181851724.51
unreal = prof - real
check("6 realized combined 418,695,260.95", abs(real-418695260.95)<0.01)
check("6 profit combined -905,337,199.06", abs(prof+905337199.06)<0.01)
check("6 unrealized ~-1,324,032,460.01, ~3.16x realized",
      abs(unreal+1324032460.01)<0.02 and abs(abs(unreal)/real-3.16)<0.01)
print("   unreal", round(unreal,2), "ratio", round(abs(unreal)/real,4))

# 7. Share reconciliation A and C exact.
check("7 A shares reconcile", abs(418271076.31+18366092.25-64339891.29-372297277.27)<0.01)
check("7 C shares reconcile", abs(106882213.55+14674520.80-22408248.45-99148485.90)<0.01)
tot_b, tot_e = 418271076.31+106882213.55, 372297277.27+99148485.90
net = tot_e - tot_b
check("7 total net redemption 53,707,526.69 = 10.23% of beginning",
      abs(-net-53707526.69)<0.01 and abs(-net/tot_b*100-10.23)<0.01)
a_net = 372297277.27-418271076.31
check("7 A net -10.99%, C net -7.24%",
      abs(a_net/418271076.31*100+10.99)<0.01 and abs((99148485.90-106882213.55)/106882213.55*100+7.24)<0.01)

# 8. NAV x shares vs net assets (rounding of NAV to 4 dp).
na = 372297277.27*3.9252; nc = 99148485.90*3.7870
check("8 A shares*NAV within 0.01% of net assets", abs(na-1461335653.09)/1461335653.09<0.0001)
check("8 C shares*NAV within 0.01% of net assets", abs(nc-375471782.85)/375471782.85<0.0001)
print("   A prod", round(na,2), "C prod", round(nc,2))

# 9. Asset composition sums to total; equity % of total assets 83.54%.
parts = [1539486700.97,116553785.38,137973167.53,8246856.85,40614702.24]
check("9 assets sum to 1,842,875,212.97", abs(sum(parts)-1842875212.97)<0.01)
check("9 equity/total ~83.54%", abs(parts[0]/1842875212.97*100-83.54)<0.01)
check("9 equity/NAV ~83.81%", abs(parts[0]/1836807435.94*100-83.81)<0.01)

# 10. Industry: manufacturing + IT share; rows sum to total equity.
ind = [39069.96,1357728823.50,549873.82,167473507.69,13695426.00]
check("10 industry rows sum to equity", abs(sum(ind)-1539486700.97)<0.01)
check("10 manufacturing 73.92% + IT 9.12% = 83.04pp of 83.81%",
      abs(73.92+9.12-83.04)<1e-9)

# 11. Top 10 concentration.
top = [8.68,7.95,6.76,6.33,6.29,5.09,4.83,4.74,3.87,3.63]
check("11 top10 sum 58.17% of NAV", abs(sum(top)-58.17)<0.01)
check("11 top2 optical modules 16.63%", abs(top[0]+top[1]-16.63)<1e-9)
check("11 top10 ~69.41% of equity (58.17/83.81)", abs(sum(top)/83.81*100-69.41)<0.02)

# 12. Weighted-avg implied shares lie between beginning and end; bonds check.
wa = 723485474.55/1.8798; wc = 181851724.51/1.7985
check("12 A implied avg shares between end and beginning", 372297277.27 < wa < 418271076.31)
check("12 C implied avg shares between end and beginning", 99148485.90 < wc < 106882213.55)
bonds = [86580252.60,10041235.62,8727043.74,6127800.00,5077453.42]
check("12 top5 bonds sum 116,553,785.38 = all bonds", abs(sum(bonds)-116553785.38)<0.01)
print("   wA", round(wa), "wC", round(wc))

print("ALL PASSED" if ok else "SOME FAILED")
