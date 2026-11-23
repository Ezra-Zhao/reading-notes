#!/usr/bin/env python3
"""119 Zhai Sen (PingAn Emerging Industries Hybrid LOF, 501099) verification.
Source: PingAn Emerging Industries Hybrid Fund (LOF) 2026 Q3 Report
(SSE official PDF, sent 2026-10-27, period-end 2026-09-30).
Manager Zhai Sen since 2020-12-29, sole listed, departure blank.
Fund inception 2020-04-10.
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
# G1 life / tenure
life=(date(2026,9,30)-date(2020,4,10)).days
ten=(date(2026,9,30)-date(2020,12,29)).days
chk(life==2364,"life 2364 days")
chk(r2(D(life)/D("365.25"))==D("6.47"),"life approx 6.47 years")
chk(ten==2101,"tenure 2101 days")
chk(r2(D(ten)/D("365.25"))==D("5.75"),"tenure approx 5.75 years")
chk(r2(D(ten)/D(life)*100)==D("88.87"),"tenure about 88.87% of life")
chk(life-ten==263,"pre-manager segment 263 days")
# G2 printed excess, six windows
wins=[("3M",D("-35.17"),D("-18.99"),D("-16.18")),("6M",D("18.03"),D("10.02"),D("8.01")),("1Y",D("17.33"),D("4.76"),D("12.57")),("3Y",D("127.16"),D("51.93"),D("75.23")),("5Y",D("61.76"),D("0.64"),D("61.12")),("SI",D("195.03"),D("34.75"),D("160.28"))]
for n,f,b,e in wins: chk(f-b==e,f"excess {n}")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==1,"only 3M window negative excess")
# G3 half-year split: Q2 implied
q2f=r2(((1+D("18.03")/100)/(1+D("-35.17")/100)-1)*100); q2b=r2(((1+D("10.02")/100)/(1+D("-18.99")/100)-1)*100)
chk(q2f==D("82.06"),"Q2 fund implied +82.06")
chk(q2b==D("35.81"),"Q2 bench implied +35.81")
chk(r2(q2f-q2b)==D("46.25"),"Q2 excess about +46.25")
# G4 one-year split: prior 9M
p9f=r2(((1+D("17.33")/100)/(1+D("-35.17")/100)-1)*100); p9b=r2(((1+D("4.76")/100)/(1+D("-18.99")/100)-1)*100)
chk(p9f==D("80.98"),"prior 9M fund +80.98")
chk(p9b==D("29.32"),"prior 9M bench +29.32")
chk(r2(p9f-p9b)==D("51.66"),"prior 9M excess about +51.66")
# G5 recovery price after Q3 drop
chk(r2(((1/(1+D("-35.17")/100))-1)*100)==D("54.25"),"recovery from Q3 needs +54.25")
chk(r2((D("2.9503")/(1+D("-35.17")/100)))==D("4.55"),"implied NAV at Q2-end about 4.55")
# G6 segment splits: -5Y..-3Y and inception..-5Y
s1f=r2(((1+D("61.76")/100)/(1+D("127.16")/100)-1)*100); s1b=r2(((1+D("0.64")/100)/(1+D("51.93")/100)-1)*100)
chk(s1f==D("-28.79"),"segment -5Y..-3Y fund -28.79")
chk(s1b==D("-33.76"),"segment -5Y..-3Y bench -33.76")
s2f=r2(((1+D("195.03")/100)/(1+D("61.76")/100)-1)*100); s2b=r2(((1+D("34.75")/100)/(1+D("0.64")/100)-1)*100)
chk(s2f==D("82.39"),"earliest segment fund +82.39")
chk(s2b==D("33.89"),"earliest segment bench +33.89")
# G7 NAV identity: SI factor equals unit NAV exactly
chk(D("2.9503")==1+D("195.03")/100,"NAV 2.9503 equals SI factor exactly")
# G8 profit composition
real=D("-13309128.62"); prof=D("-67764140.96"); fv=prof-real
chk(fv==D("-54455012.34"),"fair-value change -54,455,012.34")
chk(r2(abs(fv)/abs(prof)*100)==D("80.36"),"unrealized about 80.36% of loss")
chk(r2(abs(real)/abs(prof)*100)==D("19.64"),"realized about 19.64% of loss")
chk(r2(abs(prof)/D("99521037.71")*100)==D("68.09"),"quarter loss about 68.09% of end NAV")
# G9 asset mix
eq=D("77429340.28"); tot=D("105563234.45"); nav=D("99521037.71")
chk(r2(eq/tot*100)==D("73.35"),"equity 73.35% of total assets (printed)")
chk(r2(eq/nav*100)==D("77.80"),"equity 77.80% of NAV")
chk(r2(D("27311733.28")/nav*100)==D("27.44"),"cash about 27.44% of NAV")
chk(r2(D("400514.63")/nav*100)==D("0.40"),"bonds 0.40% of NAV (printed)")
# G10 industries
dom=D("61.76")+D("7.45")+D("5.56")+D("0.41")
chk(dom==D("75.18"),"domestic industries sum 75.18 (printed)")
chk(dom+D("2.62")==r2(eq/nav*100),"industries + HK = equity/NAV 77.80")
chk(r2(D("61.76")/D("77.80")*100)==D("79.38"),"manufacturing about 79.38% of equity")
# G11 top10 and optical cluster
top=[D(x) for x in ["6.89","5.43","5.09","4.39","3.85","3.69","3.48","3.32","2.56","2.49"]]
chk(sum(top)==D("41.19"),"top10 sum 41.19")
opt=D("6.89")+D("5.09")+D("4.39")+D("3.69")+D("3.32")
chk(opt==D("23.38"),"five optical-module names sum 23.38")
chk(r2(opt/sum(top)*100)==D("56.76"),"optical cluster about 56.76% of top10")
# G12 shares
s0=D("45817159.96"); sub=D("4664617.43"); red=D("16749042.88"); s1=D("33732734.51")
chk(s0+sub-red==s1,"share roll-forward exact")
chk(r2((s1/s0-1)*100)==D("-26.38"),"total shares net -26.38%")
chk(r2(red/s0*100)==D("36.56"),"redemptions about 36.56% of opening shares")
chk(r2(sub/s0*100)==D("10.18"),"subscriptions about 10.18% of opening shares")
print(f"ALL {ok} ASSERTIONS PASSED")
