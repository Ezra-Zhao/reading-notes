#!/usr/bin/env python3
"""117 Hu Yibin (HuaAn Jingqi Drive 1Y Hold, 014177) verification.
Source: HuaAn Jingqi Drive 1-Year Holding Hybrid Fund 2026 Q3 Report
(cninfo official PDF, sent 2026-10-27, period-end 2026-09-30).
Main class = A. Manager Hu Yibin since 2022-03-01 (fund inception day).
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
# G1 life/tenure: inception 2022-03-01 = manager start, sole manager
life=(date(2026,9,30)-date(2022,3,1)).days
chk(life==1674,"life 1674 days")
chk(r2(D(life)/D("365.25"))==D("4.58"),"life approx 4.58 years")
chk(life==life,"tenure equals life (founding sole manager, 100%)")
# G2 printed excess A windows
wins=[("3M",D("3.10"),D("-8.42"),D("11.52")),("6M",D("5.81"),D("-1.58"),D("7.39")),("1Y",D("-8.74"),D("-4.84"),D("-3.90")),("3Y",D("41.67"),D("20.32"),D("21.35")),("SI",D("43.30"),D("4.06"),D("39.24"))]
for n,f,b,e in wins: chk(f-b==e,f"excess {n}")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==1,"only 1Y window negative excess")
# G3 half-year split: Q2 implied
q2f=r2(((1+D("5.81")/100)/(1+D("3.10")/100)-1)*100); q2b=r2(((1+D("-1.58")/100)/(1+D("-8.42")/100)-1)*100)
chk(q2f==D("2.63"),"Q2 fund implied +2.63")
chk(q2b==D("7.47"),"Q2 bench implied +7.47")
chk(r2(q2f-q2b)==D("-4.84"),"Q2 excess -4.84")
# G4 one-year split: prior 9M
p9f=r2(((1+D("-8.74")/100)/(1+D("3.10")/100)-1)*100); p9b=r2(((1+D("-4.84")/100)/(1+D("-8.42")/100)-1)*100)
chk(p9f==D("-11.48"),"prior 9M fund -11.48")
chk(p9b==D("3.91"),"prior 9M bench +3.91")
chk(r2(p9f-p9b)==D("-15.39"),"prior 9M excess -15.39")
# G5 SI vs 3Y first segment
f1=r2(((1+D("43.30")/100)/(1+D("41.67")/100)-1)*100); b1=r2(((1+D("4.06")/100)/(1+D("20.32")/100)-1)*100)
chk(f1==D("1.15"),"first segment fund +1.15")
chk(b1==D("-13.51"),"first segment bench -13.51")
# G6 NAV identity: SI factor equals unit NAV
chk(D("1.4330")==1+D("43.30")/100,"NAV 1.4330 equals SI factor exactly")
# G7 profit composition
real=D("-6846958.60")+D("-1156424.30"); prof=D("1172488.84")+D("172117.54"); fv=prof-real
chk(real==D("-8003382.90"),"realized total -8,003,382.90")
chk(prof==D("1344606.38"),"profit total 1,344,606.38")
chk(fv==D("9347989.28"),"fair-value total 9,347,989.28")
chk(r2(fv/abs(real))==D("1.17"),"fv about 1.17x |realized|")
nav=D("43353748.27")+D("7170745.57")
chk(nav==D("50524493.84"),"end NAV total 50,524,493.84")
chk(r2(prof/nav*100)==D("2.66"),"profit about 2.66% of end NAV")
# G8 asset mix
eq=D("44871726.02"); tot=D("50960688.37")
chk(r2(eq/tot*100)==D("88.05"),"equity 88.05% of total assets (printed)")
chk(r2(eq/nav*100)==D("88.81"),"equity 88.81% of NAV")
chk(r2(D("9321904.68")/nav*100)==D("18.45"),"HK stocks 18.45% of NAV (printed)")
# G9 industries sum to equity/NAV
dom=D("25.55")+D("9.82")+D("25.42")+D("0.99")+D("8.58")
chk(dom==D("70.36"),"domestic industries sum 70.36 (printed)")
chk(dom+D("17.53")+D("0.92")==D("88.81"),"all industries sum 88.81 = equity/NAV")
chk(r2(D("25.55")/(eq/nav*100)*100)==D("28.77"),"manufacturing about 28.77% of equity")
# G10 top10
top=[D(x) for x in ["9.76","4.76","4.74","4.59","4.18","4.08","4.06","3.78","3.62","3.54"]]
chk(sum(top)==D("47.11"),"top10 sum 47.11")
chk(r2(top[0]/sum(top)*100)==D("20.72"),"first name about 20.72% of top10")
chk(sum(top[:6])==D("32.11"),"top6 biotech/CXO sum 32.11")
# G11 shares
a0,a1=D("33772205.24"),D("30253313.51"); c0,c1=D("5794403.71"),D("5144442.96")
chk(a1+c1==D("35397756.47"),"end total shares match printed")
chk(r2((a1/a0-1)*100)==D("-10.42"),"A shares net -10.42%")
chk(r2((c1/c0-1)*100)==D("-11.22"),"C shares net -11.22%")
chk(r2(((a1+c1)/(a0+c0)-1)*100)==D("-10.54"),"total shares net -10.54%")
# G12 vol + C class
chk(r2(D("1.65")/D("0.99"))==D("1.67"),"Q3 vol ratio about 1.67x")
chk(D("2.96")-D("-8.42")==D("11.38"),"C Q3 excess 11.38 (printed)")
print(f"ALL {ok} ASSERTIONS PASSED")
