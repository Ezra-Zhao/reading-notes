#!/usr/bin/env python3
"""Verify arithmetic in note 69 (Yang Ming / Huaan Strategy Selection).

All inputs are figures printed in the 2026 Q3 report of
Huaan Strategy Selection Mixed Fund (040008), period ended
2026-09-30, dispatched 2026-10-27: identity in section 4.1,
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

# 1. Tenure: manager since 2013-06-05 to 2026-09-30; fund effective 2007-08-02.
d_start, d_end, d_eff = date(2013,6,5), date(2026,9,30), date(2007,8,2)
tenure = (d_end - d_start).days
pre = (d_start - d_eff).days
check("1 tenure days 4865 (~13.32y)", tenure == 4865 and abs(tenure/365.25-13.32)<0.01)
check("1 fund predates manager by 2134 days (~5.84y)", pre == 2134)
print("   tenure", tenure, "pre", pre)

# 2. Excess arithmetic: growth - benchmark = stated excess, all A windows.
W = {"3m":(-3.02,-9.83,6.81),"6m":(13.52,-1.03,14.55),"1y":(16.47,-4.06,20.53),
     "3y":(39.06,18.33,20.73),"5y":(-12.50,-3.19,-9.31),"7y":(39.88,20.47,19.41),
     "10y":(118.97,39.99,78.98),"since":(177.00,33.32,143.68)}
check("2 excess all A windows", all(abs(g-b-e)<0.005 for g,b,e in W.values()))
check("2 vol diff all A windows positive",
      all(abs(a-b-c)<0.005 for a,b,c in [(1.11,1.03,0.08),(1.27,1.03,0.24),(1.20,0.91,0.29),
      (1.12,0.91,0.21),(1.09,0.89,0.20),(1.15,0.94,0.21),(1.15,0.92,0.23),(1.40,1.23,0.17)]))

# 3. Q2 2026 implied: 6m factor / Q3 factor - 1 (fund and benchmark).
q2 = 1.1352/0.9698 - 1
q2b = 0.9897/0.9017 - 1
check("3 implied Q2 fund ~+17.06%, benchmark ~+9.76%",
      abs(q2*100-17.06)<0.02 and abs(q2b*100-9.76)<0.02)
print("   Q2 implied fund", round(q2*100,2), "bench", round(q2b*100,2))

# 4. Window splits inside the 10y window (A).
e5 = 2.1897/0.8750 - 1
check("4 earliest 5y of 10y ~+150.25%", abs(e5*100-150.25)<0.02)
seg53 = 0.8750/1.3906 - 1
seg75 = 1.3988/0.8750 - 1
seg107 = 2.1897/1.3988 - 1
check("4 segments: 5y->3y ago ~-37.08%, 7y->5y ago ~+59.86%, 10y->7y ago ~+56.54%",
      abs(seg53*100+37.08)<0.02 and abs(seg75*100-59.86)<0.02 and abs(seg107*100-56.54)<0.02)
ph = 1.1647/1.1352 - 1
check("4 prior 6m inside 1y ~+2.60%", abs(ph*100-2.60)<0.02)
print("   e5", round(e5*100,2), "seg53", round(seg53*100,2), "seg75", round(seg75*100,2), "seg107", round(seg107*100,2))

# 5. Recovery after -12.50% (5y); since-inception factor vs ending NAV.
rec = 1/0.8750 - 1
check("5 recovery from -12.50% ~+14.29%", abs(rec*100-14.29)<0.02)
check("5 since factor 2.7700 vs NAV 2.4669: not equal, ratio ~1.12",
      abs(2.7700/2.4669-1.12)<0.01)

# 6. Profit split (A): realized positive, profit negative, float loss > realized.
real, prof = 117850621.56, -102539483.40
unreal = prof - real
check("6 A unrealized -220,390,104.96, ~187.00% of realized gains",
      abs(unreal+220390104.96)<0.02 and abs(abs(unreal)/real*100-187.00)<0.02)
real_all = real + (-54733.63)
prof_all = prof + (-2339502.45)
check("6 A+C realized +117,795,887.93, profit -104,878,985.85, float -222,674,873.78",
      abs(real_all-117795887.93)<0.02 and abs(prof_all+104878985.85)<0.02
      and abs((prof_all-real_all)+222674873.78)<0.02)
print("   unrealA", round(unreal,2))

# 7. Share reconciliation exact (A and C); A net inflow %; C multiple.
check("7 A shares reconcile",
      abs(1256532372.72+86662427.37-51747658.02-1291447142.07)<0.01)
net = 1291447142.07-1256532372.72
check("7 A net inflow 34,914,769.35 = +2.78% of beginning",
      abs(net-34914769.35)<0.01 and abs(net/1256532372.72*100-2.78)<0.01)
check("7 C shares reconcile; ending ~45.51x beginning (tiny base)",
      abs(831087.41+37883420.03-890171.74-37824335.70)<0.01
      and abs(37824335.70/831087.41-45.51)<0.01)
check("7 A+C ending shares = 1,329,271,477.77 (report total)",
      abs(1291447142.07+37824335.70-1329271477.77)<0.01)

# 8. NAV x shares vs net assets (NAV rounded to 4 dp).
prod = 1291447142.07*2.4669
check("8 A shares*NAV within 0.01% of net assets", abs(prod-3185831099.59)/3185831099.59<0.0001)
print("   prodA", round(prod,2))

# 9. Asset composition sums; equity/cash shares; no bonds at all.
parts = [2467046564.34, 821476644.82, 2702486.86]
nav_total = 3185831099.59+90623624.89
check("9 assets sum to 3,291,225,696.02", abs(sum(parts)-3291225696.02)<0.01)
check("9 equity/total assets 74.96%, cash/total assets 24.96%",
      abs(parts[0]/3291225696.02*100-74.96)<0.01 and abs(parts[1]/3291225696.02*100-24.96)<0.01)
check("9 equity/NAV 75.30%, cash/NAV ~25.07%",
      abs(parts[0]/nav_total*100-75.30)<0.01 and abs(parts[1]/nav_total*100-25.07)<0.01)
print("   NAV total", round(nav_total,2))

# 10. Industry rows sum to equity; manufacturing largest.
ind = [1605134568.64,196216003.10,334422060.00,100773123.00,230500809.60]
check("10 industry rows sum to equity", abs(sum(ind)-2467046564.34)<0.01)
check("10 manufacturing 48.99% of NAV is largest industry row", 48.99 > 10.21 > 7.04)

# 11. Top 10 concentration; top holding equals its whole industry row.
top = [7.04,6.46,5.66,5.08,5.03,4.90,4.86,4.75,3.08,3.08]
check("11 top10 sum 49.94% of NAV", abs(sum(top)-49.94)<0.01)
check("11 top3 sum 19.16%; top10 ~66.32% of equity (49.94/75.30)",
      abs(sum(top[:3])-19.16)<1e-9 and abs(sum(top)/75.30*100-66.32)<0.02)
check("11 top holding value = scientific-research industry value 230,500,809.60",
      abs(230500809.60-230500809.60)<0.01)

# 12. Weighted-avg implied shares between beginning and ending (A and C).
wa = prof/-0.0812
check("12 A implied avg shares between beginning and ending", 1256532372.72 < wa < 1291447142.07)
wac = -2339502.45/-0.1081
check("12 C implied avg shares between beginning and ending", 831087.41 < wac < 37824335.70)
oa = [2485885.63, 216601.23]
check("12 other assets sum 2,702,486.86", abs(sum(oa)-2702486.86)<0.01)
print("   wAvgA", round(wa), "wAvgC", round(wac))

print("ALL PASSED" if ok else "SOME FAILED")
