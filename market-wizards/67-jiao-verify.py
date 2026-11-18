#!/usr/bin/env python3
"""Verify arithmetic in note 67 (Jiao Wei / Yinhua Affluence Theme).

All inputs are figures printed in the 2026 Q3 report of
Yinhua Affluence Theme Mixed Fund (180012), period ended
2026-09-30, dispatched 2026-10-26: identity in section 4.1,
financials in 3.1, performance in 3.2.1, portfolio in 5,
shares in 6, manager own-funds in 7.
This script only checks internal arithmetic consistency and
derived windows. Clean-room, self-written.
"""
from datetime import date

ok = True
def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure: start 2018-12-27 to 2026-09-30; fund effective 2006-11-16.
d_start, d_end, d_eff = date(2018,12,27), date(2026,9,30), date(2006,11,16)
tenure = (d_end - d_start).days
pre = (d_start - d_eff).days
check("1 tenure days 2834 (~7.76y)", tenure == 2834 and abs(tenure/365.25-7.76)<0.01)
check("1 fund predates manager by 4424 days", pre == 4424)
print("   tenure", tenure, "pre", pre)

# 2. Excess arithmetic: growth - benchmark = stated excess, all A windows.
W = {"3m":(17.74,-9.87,27.61),"6m":(3.19,-1.09,4.28),"1y":(4.73,-4.05,8.78),
     "3y":(6.47,18.06,-11.59),"5y":(-35.90,-3.43,-32.47),"7y":(29.54,20.20,9.34),
     "10y":(147.24,40.05,107.19),"since":(810.80,176.49,634.31)}
check("2 excess all windows", all(abs(g-b-e)<0.005 for g,b,e in W.values()))

# 3. Q2 2026 implied: 6m factor / Q3 factor - 1.
q2 = 1.0319/1.1774 - 1
check("3 implied Q2 2026 ~-12.36%", abs(q2*100+12.36)<0.02)
print("   Q2 implied", round(q2*100,2))

# 4. Window splits: earliest 5y of 10y; earliest 3y of 10y (10y/7y);
#    prior 6m inside 1y.
e5 = 2.4724/0.6410 - 1
check("4 earliest 5y of 10y ~+285.71%", abs(e5*100-285.71)<0.02)
e3 = 2.4724/1.2954 - 1
check("4 earliest 3y of 10y ~+90.86%", abs(e3*100-90.86)<0.02)
ph = 1.0473/1.0319 - 1
check("4 prior 6m inside 1y ~+1.49%", abs(ph*100-1.49)<0.02)
print("   e5", round(e5*100,2), "e3", round(e3*100,2), "prior6m", round(ph*100,2))

# 5. Recovery after -35.90%; since-inception factor vs ending NAV.
rec = 1/0.6410 - 1
check("5 recovery from -35.90% ~+56.01%", abs(rec*100-56.01)<0.02)
check("5 since factor 9.1080 vs NAV 4.4459: not equal (distributions etc.)",
      abs(9.1080/4.4459-2.05)<0.01)

# 6. Profit split (A): realized negative, profit positive, float > profit.
real, prof = -87756208.81, 1035185012.36
unreal = prof - real
check("6 A unrealized ~+1,122,941,221.17, ~108.48% of profit",
      abs(unreal-1122941221.17)<0.02 and abs(unreal/prof*100-108.48)<0.01)
real_all = real + (-147049.71)
prof_all = prof + 1060478.24
check("6 A+C realized -87,903,258.52, profit +1,036,245,490.60, float +1,124,148,749.12",
      abs(real_all+87903258.52)<0.02 and abs(prof_all-1036245490.60)<0.02
      and abs((prof_all-real_all)-1124148749.12)<0.02)
print("   unrealA", round(unreal,2))

# 7. Share reconciliation exact (A and C); A net redemption %; C growth %.
check("7 A shares reconcile",
      abs(1571103901.78+18527613.19-80828702.68-1508802812.29)<0.01)
net = 1571103901.78-1508802812.29
check("7 A net redemption 62,301,089.49 = 3.97% of beginning",
      abs(net-62301089.49)<0.01 and abs(net/1571103901.78*100-3.97)<0.01)
check("7 C shares reconcile and grow ~+231.10%",
      abs(864786.70+5903620.62-3905062.67-2863344.65)<0.01
      and abs((2863344.65-864786.70)/864786.70*100-231.10)<0.02)
check("7 A+C ending shares = 1,511,666,156.94 (report total)",
      abs(1508802812.29+2863344.65-1511666156.94)<0.01)

# 8. NAV x shares vs net assets (NAV rounded to 4 dp).
prod = 1508802812.29*4.4459
check("8 A shares*NAV within 0.01% of net assets", abs(prod-6708021448.56)/6708021448.56<0.0001)
print("   prodA", round(prod,2))

# 9. Asset composition sums; equity shares of total assets and of NAV.
parts = [6286649033.43,16138511.78,431430747.06,2149720.38]
nav_total = 6708021448.56+12486405.53
check("9 assets sum to 6,736,368,012.65", abs(sum(parts)-6736368012.65)<0.01)
check("9 equity/total assets ~93.32%", abs(parts[0]/6736368012.65*100-93.32)<0.01)
check("9 equity/NAV ~93.54%", abs(parts[0]/nav_total*100-93.54)<0.01)
check("9 bonds/NAV ~0.24% and single bond = all bonds",
      abs(parts[1]/nav_total*100-0.24)<0.01 and abs(16138511.78-parts[1])<0.01)

# 10. Industry rows sum to equity; finance + mining.
ind = [1202417067.74,405536250.30,33391800.00,152751700.14,377918354.40,4114633860.85]
check("10 industry rows sum to equity", abs(sum(ind)-6286649033.43)<0.01)
check("10 finance 61.23% + mining 17.89% = 79.12pp of NAV",
      abs(61.23+17.89-79.12)<1e-9)

# 11. Top 10 concentration.
top = [10.02,9.67,9.58,8.18,6.91,6.08,5.96,5.81,5.78,5.62]
check("11 top10 sum 73.61% of NAV", abs(sum(top)-73.61)<0.01)
banks5 = top[0]+top[2]+top[1]+top[4]+top[5]
check("11 five banks sum 42.26%", abs(banks5-42.26)<1e-9)
check("11 banks + leasing 48.04%", abs(banks5+top[8]-48.04)<1e-9)
check("11 top10 ~78.69% of equity (73.61/93.54)", abs(sum(top)/93.54*100-78.69)<0.02)

# 12. Weighted-avg implied shares between beginning and ending (A and C).
wa = prof/0.6746
check("12 A implied avg shares between end and beginning", 1508802812.29 < wa < 1571103901.78)
wac = 1060478.24/0.4215
check("12 C implied avg shares between beginning and end", 864786.70 < wac < 2863344.65)
oa = [1512151.95,637568.43]
check("12 other assets sum 2,149,720.38", abs(sum(oa)-2149720.38)<0.01)
print("   wAvgA", round(wa), "wAvgC", round(wac))

print("ALL PASSED" if ok else "SOME FAILED")
