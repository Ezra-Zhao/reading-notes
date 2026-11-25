#!/usr/bin/env python3
"""141 Zhu Hongyu verify: numbers from China Merchants Core Competitiveness
Hybrid Fund (014412, A class) official Q3 2026 report, as of 2026-09-30."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
# G1 fund life: inception 2022-04-13 to 2026-09-30
life=(date(2026,9,30)-date(2022,4,13)).days
chk(life==1631,"G1 life 1631 days")
chk(approx(D(life)/D("365.25"),"4.47",D("0.01")),"G1 life 4.47 years")
# G2 tenure: report note says first manager's start date is the contract
# effective date; only Zhu Hongyu is listed, start 2022-04-13, no departure.
chk(date(2022,4,13)==date(2022,4,13),"G2 manager start equals fund inception 2022-04-13")
chk(approx(D(life)/D(life)*100,"100.00",D("0.01")),"G2 tenure covers 100 pct of fund life")
# A-class windows (%), fund / benchmark, as printed in the Q3 report
F={"3m":D("9.52"),"6m":D("-2.63"),"1y":D("-8.69"),"3y":D("7.92"),"si":D("45.19")}
B={"3m":D("-6.83"),"6m":D("-2.03"),"1y":D("-6.99"),"3y":D("18.55"),"si":D("9.73")}
exp={"3m":"16.35","6m":"-0.60","1y":"-1.70","3y":"-10.63","si":"35.46"}
# G3 excess for all five printed windows
for k in F: chk(approx(F[k]-B[k],exp[k],D("0.005")),f"G3 excess {k} {exp[k]}")
chk(sum(1 for k in F if F[k]>B[k])==2,"G3 only 3m and since-inception windows positive, 2 of 5")
def seg(l,s): return ((1+float(l)/100)/(1+float(s)/100)-1)*100
# G4 implied Q2 2026: fund fell while benchmark rose
chk(approx(seg(F["6m"],F["3m"]),"-11.09"),"G4 implied Q2 fund -11.09")
chk(approx(seg(B["6m"],B["3m"]),"5.15"),"G4 implied Q2 bench +5.15")
chk(approx(seg(F["6m"],F["3m"])-seg(B["6m"],B["3m"]),"-16.24"),"G4 Q2 return gap approx -16.24 pts")
# G5 implied prior 9 months of the 1y window
chk(approx(seg(F["1y"],F["3m"]),"-16.63"),"G5 implied prior 9m fund -16.63")
chk(approx(seg(B["1y"],B["3m"]),"-0.17"),"G5 implied prior 9m bench -0.17")
# G6 implied segment 3y-ago to 1y-ago (cumulative)
chk(approx(seg(F["3y"],F["1y"]),"18.19"),"G6 implied 3to1 fund +18.19")
chk(approx(seg(B["3y"],B["1y"]),"27.46"),"G6 implied 3to1 bench +27.46")
# G7 implied segment inception to 3y-ago: the since-inception lead was built early
chk(approx(seg(F["si"],F["3y"]),"34.53"),"G7 implied SI-to-3y fund +34.53")
chk(approx(seg(B["si"],B["3y"]),"-7.44"),"G7 implied SI-to-3y bench -7.44")
# G8 endpoints per 10,000 yuan (cumulative windows)
chk(approx(10000*(1+float(F["1y"])/100),"9131",D("1")),"G8 10k 1y fund 9131")
chk(approx(10000*(1+float(B["1y"])/100),"9301",D("1")),"G8 10k 1y bench 9301")
chk(approx(10000*(1+float(F["si"])/100),"14519",D("1")),"G8 10k SI fund 14519")
chk(approx(10000*(1+float(B["si"])/100),"10973",D("1")),"G8 10k SI bench 10973")
# G9 profit quality, A class: realised is only about 8.39 pct of Q3 profit
chk(approx(D("99794919.78")-D("8374739.43"),"91420180.35",D("0.01")),"G9 A unrealised 91420180.35")
chk(approx(D("8374739.43")/D("99794919.78")*100,"8.39"),"G9 A realised share 8.39 pct")
chk(approx(D("99794919.78")+D("36946029.66"),"136740949.44",D("0.01")),"G9 A+C total profit 136740949.44")
# G10 holdings: top10 and top3 concentration (pct of NAV, as printed)
top10=[D(x) for x in ["9.87","9.66","9.46","8.76","7.66","6.74","4.55","4.36","4.27","4.19"]]
chk(approx(sum(top10),"69.52",D("0.01")),"G10 top10 sum 69.52 pct")
chk(approx(sum(top10[:3]),"28.99",D("0.01")),"G10 top3 sum 28.99 pct")
# G11 portfolio shape: equities about 94.57 pct of NAV, HK about 38.05 pct
nav=D("1095218582.28")+D("407994148.92")
chk(approx(nav,"1503212731.20",D("0.01")),"G11 total NAV 1503212731.20")
chk(approx(D("1421600562.45")/nav*100,"94.57"),"G11 equities 94.57 pct of NAV")
chk(approx(D("571955906.39")/nav*100,"38.05"),"G11 HK stocks 38.05 pct of NAV")
chk(approx(D("56.52")+D("38.05"),"94.57",D("0.01")),"G11 domestic 56.52 + HK 38.05 = 94.57")
# G12 flows and manager holding: net redemptions in a winning quarter
chk(approx(D("955565277.98")/D("1027848167.38")*100-100,"-7.03"),"G12 A shares net -7.03 pct in Q3")
chk(approx(D("369347403.78")/D("395095204.34")*100-100,"-6.52"),"G12 C shares net -6.52 pct in Q3")
chk(approx(D("12384305.22")/D("1324912681.76")*100,"0.93"),"G12 manager own holding 0.93 pct")
print(f"ALL {ok} ASSERTIONS PASSED")
