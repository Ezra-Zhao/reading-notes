#!/usr/bin/env python3
"""125 Gui Kai (Harvest Emerging Industries Equity, 000751) verification.
Source: 2026 Q3 report (cninfo PDF, sent 2026-10-27).
Contract effective 2014-09-17; Gui Kai appointed 2018-12-04, no departure
date; Chen Tao co-manager added 2025-12-23. Gui: 19 yrs experience.
Single share class.
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
# G1 life / tenure split
life=(date(2026,9,30)-date(2014,9,17)).days
chk(life==4396,"life 4396 days")
chk(r2(D(life)/D("365.25"))==D("12.04"),"life approx 12.04 years")
ten=(date(2026,9,30)-date(2018,12,4)).days
chk(ten==2857,"Gui tenure 2857 days")
chk(r2(D(ten)/D("365.25"))==D("7.82"),"Gui tenure approx 7.82 years")
pre=(date(2018,12,4)-date(2014,9,17)).days
chk(pre==1539,"pre-Gui 1539 days")
chk(pre+ten==life,"pre + tenure = life")
chk(r2(D(ten)/D(life)*100)==D("64.99"),"Gui tenure 64.99 pct of life")
solo=(date(2025,12,23)-date(2018,12,4)).days
co=(date(2026,9,30)-date(2025,12,23)).days
chk(solo==2576,"Gui solo period 2576 days")
chk(co==281,"co-managed period 281 days")
chk(solo+co==ten,"solo + co = tenure")
# G2 printed excess, eight windows - six positive, two negative
wins=[("3M",D("-23.99"),D("-25.78"),D("1.79")),("6M",D("14.52"),D("2.40"),D("12.12")),("1Y",D("15.47"),D("-5.32"),D("20.79")),("3Y",D("30.20"),D("38.28"),D("-8.08")),("5Y",D("-12.11"),D("-6.21"),D("-5.90")),("7Y",D("61.72"),D("53.65"),D("8.07")),("10Y",D("188.15"),D("40.27"),D("147.88")),("SI",D("344.90"),D("80.33"),D("264.57"))]
for n,f,b,e in wins: chk(f-b==e,f"excess {n}")
chk(sum(1 for _,f,b,_ in wins if f-b>0)==6,"six windows positive excess")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==2,"two windows negative excess (3Y,5Y)")
# G3 half-year split: Q2 implied
q2f=r2(((1+D("14.52")/100)/(1+D("-23.99")/100)-1)*100); q2b=r2(((1+D("2.40")/100)/(1+D("-25.78")/100)-1)*100)
chk(q2f==D("50.66"),"Q2 fund implied +50.66")
chk(q2b==D("37.97"),"Q2 bench implied +37.97")
chk(r2(q2f-q2b)==D("12.69"),"Q2 excess about +12.69")
# G4 one-year split: prior 9M implied
p9f=r2(((1+D("15.47")/100)/(1+D("-23.99")/100)-1)*100); p9b=r2(((1+D("-5.32")/100)/(1+D("-25.78")/100)-1)*100)
chk(p9f==D("51.91"),"prior 9M fund +51.91")
chk(p9b==D("27.57"),"prior 9M bench +27.57")
chk(r2(p9f-p9b)==D("24.34"),"prior 9M excess about +24.34")
# G5 recovery from Q3 drop
chk(r2(((1/(1+D("-23.99")/100))-1)*100)==D("31.56"),"recovery from Q3 needs +31.56")
# G6 NAV identity: SI factor vs unit NAV
chk(1+D("344.90")/100==D("4.4490"),"SI factor 4.4490 equals unit NAV 4.449")
# G7 segment splits: 10Y vs 7Y, 7Y vs 5Y, 5Y vs 3Y
sf=((1+D("188.15")/100))/((1+D("61.72")/100)); sb=((1+D("40.27")/100))/((1+D("53.65")/100))
chk(r2((sf-1)*100)==D("78.18"),"segment -10Y..-7Y fund +78.18")
chk(r2((sb-1)*100)==D("-8.71"),"segment -10Y..-7Y bench -8.71")
sf2=((1+D("61.72")/100))/((1+D("-12.11")/100)); sb2=((1+D("53.65")/100))/((1+D("-6.21")/100))
chk(r2((sf2-1)*100)==D("84.00"),"segment -7Y..-5Y fund +84.00")
chk(r2((sb2-1)*100)==D("63.82"),"segment -7Y..-5Y bench +63.82")
sf3=((1+D("-12.11")/100))/((1+D("30.20")/100)); sb3=((1+D("-6.21")/100))/((1+D("38.28")/100))
chk(r2((sf3-1)*100)==D("-32.50"),"segment -5Y..-3Y fund -32.50")
chk(r2((sb3-1)*100)==D("-32.17"),"segment -5Y..-3Y bench -32.17")
# G8 profit composition: realized positive, FV negative
real=D("434815027.20"); prof=D("-1211835581.69"); fv=prof-real
chk(fv==D("-1646650608.89"),"FV change -1,646,650,608.89")
chk(r2(-fv/-prof*100)==D("135.88"),"FV loss 135.88 pct of net loss")
# G9 NAV totals and loss vs ending NAV
nav=D("3710571811.85")
chk(r2(-prof/nav*100)==D("32.66"),"quarter loss about 32.66 pct of ending NAV")
chk(r2(D("-1.4261")/D("4.449")*100)==D("-32.05"),"weighted avg profit per share about -32.05 pct of NAV (info only)")
# G10 portfolio shape
tot=D("3719967953.24"); eq=D("3248934876.46")
chk(r2(eq/tot*100)==D("87.34"),"equity 87.34 pct of total assets")
chk(r2(eq/nav*100)==D("87.56"),"equity 87.56 pct of NAV")
chk(r2(D("2683039868.04")/eq*100)==D("82.58"),"manufacturing 82.58 pct of equity")
ind=D("39927914.10")+D("2683039868.04")+D("33151482.00")+D("317864571.04")+D("2145.52")+D("174948895.76")
chk(ind==eq,"industry amounts sum to equity total")
chk(r2(D("22893879.78")/nav*100)==D("0.62"),"bonds 0.62 pct of NAV")
chk(r2(D("444193796.05")/tot*100)==D("11.94"),"cash 11.94 pct of total assets")
# G11 top-10 holdings
top=[D(x) for x in ["8.26","6.70","6.50","5.96","5.25","4.71","4.15","3.66","2.83","2.67"]]
chk(sum(top)==D("50.69"),"top10 sum 50.69")
chk(max(top)==D("8.26"),"largest holding 8.26 (Jereh)")
# G12 share roll-forward
s0=D("900940768.55"); sub=D("21856533.27"); red=D("88762885.93"); s1=D("834034415.89")
chk(s0+sub-red==s1,"shares roll forward")
chk(r2((s1/s0-1)*100)==D("-7.43"),"total shares net -7.43 pct")
chk(r2(red/sub)==D("4.06"),"redemptions about 4.06x subscriptions")
print("ALL",ok,"ASSERTIONS PASSED")
