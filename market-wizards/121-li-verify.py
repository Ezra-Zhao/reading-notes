#!/usr/bin/env python3
"""121 Li Shuai (China Europe Industry Foresight Mixed, 012390) verification.
Source: 2026 Q3 report (cninfo PDF, sent 2026-10-27).
Contract effective 2021-06-16; Li Shuai appointed 2021-06-16, no departure
date (note in report: if appointed from contract date, that date is the
appointment date) - founding manager, sole listed manager, 17 yrs experience.
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
life=(date(2026,9,30)-date(2021,6,16)).days
chk(life==1932,"life 1932 days")
chk(r2(D(life)/D("365.25"))==D("5.29"),"life approx 5.29 years")
chk(life>1900,"life over 1900 days")
# G2 printed excess, six windows A - all negative
wins=[("3M",D("-40.26"),D("-6.61"),D("-33.65")),("6M",D("-33.45"),D("-1.76"),D("-31.69")),("1Y",D("-36.91"),D("-6.56"),D("-30.35")),("3Y",D("-22.03"),D("19.00"),D("-41.03")),("5Y",D("-47.31"),D("-2.68"),D("-44.63")),("SI",D("-51.94"),D("-8.30"),D("-43.64"))]
for n,f,b,e in wins: chk(f-b==e,f"excess {n}")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==6,"all six windows negative excess")
chk(sum(1 for _,f,b,_ in wins if f-b>0)==0,"zero windows positive excess")
# G3 half-year split: Q2 implied
q2f=r2(((1+D("-33.45")/100)/(1+D("-40.26")/100)-1)*100); q2b=r2(((1+D("-1.76")/100)/(1+D("-6.61")/100)-1)*100)
chk(q2f==D("11.40"),"Q2 fund implied +11.40")
chk(q2b==D("5.19"),"Q2 bench implied +5.19")
chk(r2(q2f-q2b)==D("6.21"),"Q2 excess about +6.21")
# G4 one-year split: prior 9M implied
p9f=r2(((1+D("-36.91")/100)/(1+D("-40.26")/100)-1)*100); p9b=r2(((1+D("-6.56")/100)/(1+D("-6.61")/100)-1)*100)
chk(p9f==D("5.61"),"prior 9M fund +5.61")
chk(p9b==D("0.05"),"prior 9M bench +0.05")
# G5 recovery
chk(r2(((1/(1+D("-40.26")/100))-1)*100)==D("67.39"),"recovery from Q3 needs +67.39")
chk(r2(((1/(1+D("-51.94")/100))-1)*100)==D("108.07"),"recovery to inception par needs +108.07")
# G6 NAV identity: SI factor vs unit NAV
chk(1+D("-51.94")/100==D("0.4806"),"SI factor 0.4806 equals A unit NAV")
chk(1+D("-53.94")/100==D("0.4606"),"C SI factor 0.4606 equals C unit NAV")
# G7 segment splits: 5Y vs 3Y (segment -5Y..-3Y)
sf=((1+D("-47.31")/100))/((1+D("-22.03")/100)); sb=((1+D("-2.68")/100))/((1+D("19.00")/100))
chk(r2((sf-1)*100)==D("-32.42"),"segment -5Y..-3Y fund -32.42")
chk(r2((sb-1)*100)==D("-18.22"),"segment -5Y..-3Y bench -18.22")
# segment inception..-5Y (first ~0.29y)
sf2=((1+D("-51.94")/100))/((1+D("-47.31")/100)); sb2=((1+D("-8.30")/100))/((1+D("-2.68")/100))
chk(r2((sf2-1)*100)==D("-8.79"),"segment SI..-5Y fund -8.79")
chk(r2((sb2-1)*100)==D("-5.77"),"segment SI..-5Y bench -5.77")
# G8 profit composition (A+C combined)
ra=D("-302934873.28"); rc=D("-9012256.03"); pa=D("-409457139.26"); pc=D("-11733659.22")
real=ra+rc; prof=pa+pc; fv=prof-real
chk(real==D("-311947129.31"),"combined realized -311,947,129.31")
chk(prof==D("-421190798.48"),"combined profit -421,190,798.48")
chk(fv==D("-109243669.17"),"combined FV change -109,243,669.17")
chk(r2(-real/-prof*100)==D("74.06"),"realized share of loss 74.06 pct")
chk(r2(-fv/-prof*100)==D("25.94"),"FV share of loss 25.94 pct")
# G9 NAV totals and loss vs ending NAV
nav=D("602165708.24")+D("19690591.56")
chk(nav==D("621856299.80"),"combined ending NAV 621,856,299.80")
chk(r2(-prof/nav*100)==D("67.73"),"quarter loss about 67.73 pct of ending NAV")
# G10 portfolio shape
chk(r2(D("567385493.83")/D("643999744.94")*100)==D("88.10"),"equity 88.10 pct of total assets")
chk(r2(D("567385493.83")/nav*100)==D("91.24"),"equity 91.24 pct of NAV")
chk(r2(D("566957364.44")/D("567385493.83")*100)==D("99.92"),"manufacturing 99.92 pct of equity")
chk(D("91.17")+D("0.05")+D("0.01")+D("0.01")==D("91.24"),"industry rows sum to 91.24")
# G11 top-10 holdings
top=[D(x) for x in ["5.45","5.40","5.29","5.27","5.19","5.09","5.06","5.04","4.97","4.79"]]
chk(sum(top)==D("51.55"),"top10 sum 51.55")
chk(max(top)==D("5.45"),"largest holding 5.45")
chk(min(top)==D("4.79"),"smallest top10 4.79")
chk(r2(max(top)-min(top))==D("0.66"),"top10 spread only 0.66 pp")
# G12 share roll-forward
a0=D("1272647084.43"); a_sub=D("12138098.01"); a_red=D("31769800.47"); a1=D("1253015381.97")
chk(a0+a_sub-a_red==a1,"A shares roll forward")
c0=D("37119880.94"); c_sub=D("12508138.53"); c_red=D("6876731.78"); c1=D("42751287.69")
chk(c0+c_sub-c_red==c1,"C shares roll forward")
chk(a1+c1==D("1295766669.66"),"total ending shares match section 2")
tot0=a0+c0; tot1=a1+c1
chk(r2((tot1/tot0-1)*100)==D("-1.07"),"total shares net -1.07 pct in crash quarter")
chk(r2((a1/a0-1)*100)==D("-1.54"),"A shares net -1.54 pct")
chk(r2((c1/c0-1)*100)==D("15.17"),"C shares net +15.17 pct")
print(f"ALL {ok} ASSERTIONS PASSED")
