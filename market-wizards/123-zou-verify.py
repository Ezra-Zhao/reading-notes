#!/usr/bin/env python3
"""123 Zou Wei (Utrust Yongfeng Xingyan Flexible Allocation Mixed, 010064) verification.
Source: 2026 Q3 report (cninfo PDF, sent 2026-10-27).
Contract effective 2020-09-23; Zou Wei appointed 2020-09-23, no departure
date - founding manager, sole listed manager, 16 yrs experience.
Class A used for performance unless stated.
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
# G1 life / tenure (founding, tenure = life)
life=(date(2026,9,30)-date(2020,9,23)).days
chk(life==2198,"life 2198 days")
chk(r2(D(life)/D("365.25"))==D("6.02"),"life approx 6.02 years")
# G2 printed excess, six windows A - five positive, one negative
wins=[("3M",D("-5.15"),D("-7.82"),D("2.67")),("6M",D("0.48"),D("-0.39"),D("0.87")),("1Y",D("-2.82"),D("-2.68"),D("-0.14")),("3Y",D("30.47"),D("17.59"),D("12.88")),("5Y",D("14.26"),D("1.51"),D("12.75")),("SI",D("39.96"),D("6.50"),D("33.46"))]
for n,f,b,e in wins: chk(f-b==e,f"excess {n}")
chk(sum(1 for _,f,b,_ in wins if f-b>0)==5,"five windows positive excess")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==1,"one window negative excess (1Y)")
# G3 half-year split: Q2 implied
q2f=r2(((1+D("0.48")/100)/(1+D("-5.15")/100)-1)*100); q2b=r2(((1+D("-0.39")/100)/(1+D("-7.82")/100)-1)*100)
chk(q2f==D("5.94"),"Q2 fund implied +5.94")
chk(q2b==D("8.06"),"Q2 bench implied +8.06")
chk(r2(q2f-q2b)==D("-2.12"),"Q2 excess about -2.12")
# G4 one-year split: prior 9M implied
p9f=r2(((1+D("-2.82")/100)/(1+D("-5.15")/100)-1)*100); p9b=r2(((1+D("-2.68")/100)/(1+D("-7.82")/100)-1)*100)
chk(p9f==D("2.46"),"prior 9M fund +2.46")
chk(p9b==D("5.58"),"prior 9M bench +5.58")
chk(r2(p9f-p9b)==D("-3.12"),"prior 9M excess about -3.12")
# G5 recovery from Q3 drop
chk(r2(((1/(1+D("-5.15")/100))-1)*100)==D("5.43"),"recovery from Q3 needs +5.43")
# G6 NAV identity: SI factor vs unit NAV
chk(1+D("39.96")/100==D("1.3996"),"SI factor 1.3996 equals A unit NAV")
chk(1+D("36.37")/100==D("1.3637"),"C SI factor 1.3637 equals C unit NAV")
# G7 segment splits: 5Y vs 3Y and SI vs 5Y
sf=((1+D("14.26")/100))/((1+D("30.47")/100)); sb=((1+D("1.51")/100))/((1+D("17.59")/100))
chk(r2((sf-1)*100)==D("-12.42"),"segment -5Y..-3Y fund -12.42")
chk(r2((sb-1)*100)==D("-13.67"),"segment -5Y..-3Y bench -13.67")
sf2=((1+D("39.96")/100))/((1+D("14.26")/100)); sb2=((1+D("6.50")/100))/((1+D("1.51")/100))
chk(r2((sf2-1)*100)==D("22.49"),"segment SI..-5Y fund +22.49")
chk(r2((sb2-1)*100)==D("4.92"),"segment SI..-5Y bench +4.92")
# G8 profit composition (A+C combined): realized positive, FV negative
ra=D("13689352.35"); rc=D("710393.19"); pa=D("-24174862.35"); pc=D("-1346019.03")
real=ra+rc; prof=pa+pc; fv=prof-real
chk(real==D("14399745.54"),"combined realized +14,399,745.54")
chk(prof==D("-25520881.38"),"combined profit -25,520,881.38")
chk(fv==D("-39920626.92"),"combined FV change -39,920,626.92")
chk(r2(-fv/-prof*100)==D("156.42"),"FV loss 156.42 pct of net loss")
# G9 NAV totals and loss vs ending NAV
nav=D("439805069.05")+D("24419207.81")
chk(nav==D("464224276.86"),"combined ending NAV 464,224,276.86")
chk(r2(-prof/nav*100)==D("5.50"),"quarter loss about 5.50 pct of ending NAV")
# G10 portfolio shape
chk(r2(D("433293225.50")/D("465079794.37")*100)==D("93.17"),"equity 93.17 pct of total assets")
chk(r2(D("433293225.50")/nav*100)==D("93.34"),"equity 93.34 pct of NAV")
chk(r2(D("319192332.54")/D("433293225.50")*100)==D("73.67"),"manufacturing 73.67 pct of equity")
ind=D("23208410.00")+D("10474164.00")+D("319192332.54")+D("184705.60")+D("69671.36")+D("39901988.00")+D("40261954.00")
chk(ind==D("433293225.50"),"industry amounts sum to equity total")
chk(D("20980065.32")+D("5776212.90")==D("26756278.22"),"two gov bonds sum to bond total")
chk(r2(D("26756278.22")/nav*100)==D("5.76"),"bonds 5.76 pct of NAV")
# G11 top-10 holdings
top=[D(x) for x in ["6.25","5.99","5.59","4.86","4.70","4.50","3.47","3.43","3.39","3.16"]]
chk(sum(top)==D("45.34"),"top10 sum 45.34")
chk(max(top)==D("6.25"),"largest holding 6.25 (CATL)")
chk(r2(D("3.47")+D("3.39"))==D("6.86"),"two property names sum 6.86")
# G12 share roll-forward
a0=D("327816605.88"); a_sub=D("1321955.20"); a_red=D("14905000.22"); a1=D("314233560.86")
chk(a0+a_sub-a_red==a1,"A shares roll forward")
c0=D("17923460.04"); c_sub=D("65029.45"); c_red=D("81807.86"); c1=D("17906681.63")
chk(c0+c_sub-c_red==c1,"C shares roll forward")
chk(a1+c1==D("332140242.49"),"total ending shares match section 2")
tot0=a0+c0; tot1=a1+c1
chk(r2((tot1/tot0-1)*100)==D("-3.93"),"total shares net -3.93 pct")
chk(r2((a1/a0-1)*100)==D("-4.14"),"A shares net -4.14 pct")
chk(r2((c1/c0-1)*100)==D("-0.09"),"C shares net -0.09 pct")
print("ALL",ok,"ASSERTIONS PASSED")
