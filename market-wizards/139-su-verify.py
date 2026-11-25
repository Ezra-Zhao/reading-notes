#!/usr/bin/env python3
"""139 Su Wenjie verify: numbers from GF Growth Power 3Y Holding (014725) official Q3 2026 report (2026-09-30)."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
# G1 fund life: inception 2022-07-26 to 2026-09-30
life=(date(2026,9,30)-date(2022,7,26)).days
chk(life==1527,"G1 life 1527 days")
chk(approx(D(life)/D("365.25"),"4.18",D("0.01")),"G1 life 4.18 years")
# G2 tenure: Su from 2025-07-02 to 2026-09-30; pre-tenure share
ten=(date(2026,9,30)-date(2025,7,2)).days
chk(ten==455,"G2 tenure 455 days")
chk(approx(D(ten)/D(life)*100,"29.80",D("0.01")),"G2 tenure share 29.80 pct of fund life")
chk(life-ten==1072,"G2 pre-tenure 1072 days not his")
# A-class windows (%), fund / benchmark printed in report
F={"3m":D("-6.68"),"6m":D("-11.95"),"1y":D("-13.06"),"3y":D("-16.16"),"si":D("-49.69")}
B={"3m":D("-5.96"),"6m":D("-1.51"),"1y":D("-6.33"),"3y":D("21.83"),"si":D("11.60")}
# G3 excess all negative, counts
exp={"3m":"-0.72","6m":"-10.44","1y":"-6.73","3y":"-37.99","si":"-61.29"}
for k in F: chk(approx(F[k]-B[k],exp[k],D("0.005")),f"G3 excess {k} {exp[k]}")
chk(all(F[k]<B[k] for k in F),"G3 all five windows behind benchmark")
# G4 windows fully inside tenure: 3m/6m/1y start after 2025-07-02; 3y and SI mostly pre-tenure
chk(date(2025,10,1)>date(2025,7,2),"G4 1y window starts 2025-10-01, inside tenure")
chk(date(2023,10,1)<date(2025,7,2)<date(2025,9,30),"G4 3y window spans tenure start near its end")
def seg(l,s): return ((1+l/100)/(1+s/100)-1)*100
# G5 implied Q2 2026 from 6m and Q3
chk(approx(seg(F["6m"],F["3m"]),"-5.65"),"G5 implied Q2 2026 fund -5.65")
chk(approx(seg(B["6m"],B["3m"]),"4.73"),"G5 implied Q2 2026 bench +4.73")
chk(approx(seg(F["6m"],F["3m"])-seg(B["6m"],B["3m"]),"-10.38"),"G5 Q2 gap -10.38 pts")
# G6 implied prior half (2025Q4-2026Q1) from 1y and 6m: fund fell less than bench
chk(approx(seg(F["1y"],F["6m"]),"-1.26"),"G6 prior half fund -1.26")
chk(approx(seg(B["1y"],B["6m"]),"-4.89"),"G6 prior half bench -4.89")
# G7 segment 3y-ago to 1y-ago (cumulative 2y): fund slightly down, bench up 30
chk(approx(seg(F["3y"],F["1y"]),"-3.57"),"G7 3to1 segment fund -3.57")
chk(approx(seg(B["3y"],B["1y"]),"30.07"),"G7 3to1 segment bench +30.07")
# G8 first segment inception to 3y-ago: entirely pre-tenure
chk(approx(seg(F["si"],F["3y"]),"-40.00",D("0.03")),"G8 first segment fund approx -40.00")
chk(approx(seg(B["si"],B["3y"]),"-8.40"),"G8 first segment bench -8.40")
# G9 NAV check: SI factor equals printed NAV 0.5031; recovery price
chk(approx((1+F["si"]/100)*10000,"5031",D("1")),"G9 10k since inception becomes 5031")
chk(approx(D("0.5031"),1+F["si"]/100,D("0.0001")),"G9 NAV 0.5031 equals SI factor")
chk(approx((1/D("0.5031")-1)*100,"98.77"),"G9 recovery needs +98.77")
# G10 Q3 financials: combined realized / profit / implied unrealized (yuan)
ra,pa=D("-25596283.84"),D("-54132573.49")
rc,pc=D("-3823241.70"),D("-7890299.88")
chk(approx(ra+rc,"-29419525.54",D("0.01")),"G10 combined realized -29419525.54")
chk(approx(pa+pc,"-62022873.37",D("0.01")),"G10 combined profit -62022873.37")
chk(approx((pa-ra)+(pc-rc),"-32603347.83",D("0.01")),"G10 combined unrealized -32603347.83")
chk(approx(abs(pa+pc)/D("838548447.92")*100,"7.40"),"G10 Q3 loss approx 7.40 pct of end net assets")
# G11 shares: A and C net change in Q3
a0,a1=D("1545647486.23"),D("1456873085.03")
c0,c1=D("225473674.58"),D("214273600.04")
chk(approx((a1-a0)/a0*100,"-5.74"),"G11 A shares -5.74 pct in Q3")
chk(approx((c1-c0)/c0*100,"-4.97"),"G11 C shares -4.97 pct in Q3")
chk(approx(a1+c1,"1671146685.07",D("0.01")),"G11 total end shares match report")
# G12 portfolio shape: top10 sum, petrochemical cluster in top10, equity weight, manager holding
top10=[D(x) for x in ["7.88","5.84","4.64","4.54","4.08","4.04","3.83","3.28","3.20","3.08"]]
chk(approx(sum(top10),"44.41",D("0.01")),"G12 top10 sum 44.41 pct of NAV")
petro=D("7.88")+D("5.84")+D("4.54")+D("4.04")+D("3.28")
chk(approx(petro,"25.58",D("0.01")),"G12 top10 petrochemical five sum 25.58 pct")
chk(approx(D("784059113.04")/D("838548447.92")*100,"93.50"),"G12 equity approx 93.50 pct of net assets")
chk(approx(D("12194962.54")/D("1671146685.07")*100,"0.73"),"G12 manager own holding 0.73 pct")
print(f"ALL {ok} ASSERTIONS PASSED")
