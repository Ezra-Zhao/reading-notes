#!/usr/bin/env python3
"""124 Bobrinskoy / Ariel Focus Fund (Investor Class ARFFX) verification.
Source: Ariel Investments official Ariel Focus Fund fact sheet for the
quarter ended 2026-09-30 (fund inception 2005-06-30; the sheet lists
Charles K. Bobrinskoy as the sole Portfolio Manager). Primary return
series is the Investor Class. Manager start (June 2005) is Citywire
(B-grade) and is not printed on the sheet; it is not asserted here.
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
def cum(a,y): return r2(((1+a/100)**y-1)*100)
def grow(a,y): return r2(D(10000)*((1+a/100)**y))
# G1 life: 2005-06-30 to 2026-09-30
life=(date(2026,9,30)-date(2005,6,30)).days
chk(life==7762,"life 7762 days")
yrs=D(life)/D("365.25")
chk(r2(yrs)==D("21.25"),"life approx 21.25 years")
# G2 excess vs Russell 1000 Value, Investor Class, seven windows - all negative
wv=[("QTR",D("-1.26"),D("2.61"),D("-3.87")),("YTD",D("8.22"),D("19.27"),D("-11.05")),
("1Y",D("7.68"),D("23.81"),D("-16.13")),("3Y",D("18.16"),D("20.07"),D("-1.91")),
("5Y",D("8.65"),D("11.92"),D("-3.27")),("10Y",D("9.68"),D("11.43"),D("-1.75")),
("SI",D("7.09"),D("8.97"),D("-1.88"))]
for n,f,b,e in wv: chk(f-b==e,f"excess vs R1000V {n}")
chk(sum(1 for _,f,b,_ in wv if f-b<0)==7,"all seven windows negative vs R1000V")
# G3 excess vs S&P 500, seven windows - all negative
ws=[("QTR",D("-1.26"),D("2.30"),D("-3.56")),("YTD",D("8.22"),D("12.75"),D("-4.53")),
("1Y",D("7.68"),D("15.74"),D("-8.06")),("3Y",D("18.16"),D("22.88"),D("-4.72")),
("5Y",D("8.65"),D("13.79"),D("-5.14")),("10Y",D("9.68"),D("15.33"),D("-5.65")),
("SI",D("7.09"),D("11.24"),D("-4.15"))]
for n,f,b,e in ws: chk(f-b==e,f"excess vs SPX {n}")
chk(sum(1 for _,f,b,_ in ws if f-b<0)==7,"all seven windows negative vs SPX")
# G4 YTD split: H1 2026 implied (YTD through Q3 minus Q3)
h1f=r2(((1+D("8.22")/100)/(1+D("-1.26")/100)-1)*100); h1v=r2(((1+D("19.27")/100)/(1+D("2.61")/100)-1)*100)
h1s=r2(((1+D("12.75")/100)/(1+D("2.30")/100)-1)*100)
chk(h1f==D("9.60"),"H1 fund implied +9.60")
chk(h1v==D("16.24"),"H1 R1000V implied +16.24")
chk(h1s==D("10.22"),"H1 SPX implied +10.22")
chk(r2(h1f-h1v)==D("-6.64"),"H1 excess vs R1000V about -6.64")
# G5 1Y split: prior nine months implied
p9f=r2(((1+D("7.68")/100)/(1+D("-1.26")/100)-1)*100); p9v=r2(((1+D("23.81")/100)/(1+D("2.61")/100)-1)*100)
chk(p9f==D("9.05"),"prior 9M fund implied +9.05")
chk(p9v==D("20.66"),"prior 9M R1000V implied +20.66")
chk(r2(p9f-p9v)==D("-11.61"),"prior 9M excess about -11.61")
# G6 cumulative from annualized (mechanical)
chk(cum(D("18.16"),3)==D("64.97"),"3Y cum fund +64.97")
chk(cum(D("20.07"),3)==D("73.10"),"3Y cum R1000V +73.10")
chk(cum(D("8.65"),5)==D("51.41"),"5Y cum fund +51.41")
chk(cum(D("11.92"),5)==D("75.61"),"5Y cum R1000V +75.61")
chk(cum(D("9.68"),10)==D("151.93"),"10Y cum fund +151.93")
chk(cum(D("11.43"),10)==D("195.14"),"10Y cum R1000V +195.14")
# G7 growth of 10000 since inception (annualized over 21.25 years, mechanical)
gf=grow(D("7.09"),yrs); gv=grow(D("8.97"),yrs); gs=grow(D("11.24"),yrs)
print("SI growth fund/R1000V/SPX:",gf,gv,gs)
chk(r2(gf/gv)==D("0.69"),"SI endpoint about 0.69x R1000V")
chk(r2(gf/gs)==D("0.45"),"SI endpoint about 0.45x SPX")
# G8 segment annualized: inception..10Y ago implied from SI and 10Y
def seg(a_long,y_long,a_short,y_short):
    return r2((((1+a_long/100)**y_long/(1+a_short/100)**y_short)**(D(1)/(y_long-y_short))-1)*100)
y10=D(10); ypre=yrs-y10
chk(seg(D("7.09"),yrs,D("9.68"),y10)==D("4.84"),"segment inception..-10Y fund about +4.84")
chk(seg(D("8.97"),yrs,D("11.43"),y10)==D("6.83"),"segment inception..-10Y R1000V about +6.83")
chk(seg(D("11.24"),yrs,D("15.33"),y10)==D("7.73"),"segment inception..-10Y SPX about +7.73")
# G9 top-10 holdings sum to printed total 47.96
top=[D(x) for x in ("5.51","5.41","5.21","4.98","4.74","4.58","4.43","4.40","4.35","4.35")]
chk(sum(top)==D("47.96"),"top10 sums to printed 47.96")
chk(max(top)==D("5.51"),"largest holding 5.51")
energy_top=D("5.21")+D("4.98")+D("4.58")
chk(energy_top==D("14.77"),"three energy names in top10 sum 14.77")
fin_top=D("5.41")+D("4.74")+D("4.43")
chk(fin_top==D("14.58"),"three financial names in top10 sum 14.58")
# G10 characteristics gaps
chk(r2((1-D("11.50")/D("16.85"))*100)==D("31.75"),"forward P/E discount about 31.75 pct")
chk(r2(D("18.92")-D("23.77"))==D("-4.85"),"ROE gap -4.85")
chk(r2(D("6.38")-D("5.69"))==D("0.69"),"interest coverage gap +0.69")
chk(r2((1/(1-D("21.25")/100)-1)*100)==D("26.98"),"upside to private market value about +26.98")
chk(r2(D("14.78")-D("6.30"))==D("8.48"),"energy overweight +8.48")
chk(r2(D("2.99")-D("19.57"))==D("-16.58"),"technology underweight -16.58")
# G11 market-cap mix sums and small tilt
fund_mc=[D(x) for x in ("15.83","13.83","13.76","35.23","21.33")]
idx_mc=[D(x) for x in ("42.20","30.28","18.52","8.02","0.98")]
chk(sum(fund_mc)==D("99.98"),"fund market-cap mix sums 99.98 (rounding)")
chk(sum(idx_mc)==D("100.00"),"index market-cap mix sums 100.00")
chk(r2(D("35.23")+D("21.33"))==D("56.56"),"fund mid/small plus small 56.56")
chk(r2(D("8.02")+D("0.98"))==D("9.00"),"index mid/small plus small 9.00")
chk(r2(D("30")/D("869")*100)==D("3.45"),"30 holdings is 3.45 pct of index count")
# G12 contributors/detractors and class gap
contrib=[D(x) for x in ("0.93","0.77","0.58","0.47","0.46")]
detract=[D(x) for x in ("-1.39","-0.82","-0.72","-0.42","-0.35")]
chk(sum(contrib)==D("3.21"),"top5 contributors sum +3.21")
chk(sum(detract)==D("-3.70"),"bottom5 detractors sum -3.70")
chk(r2(sum(contrib)+sum(detract))==D("-0.49"),"named ten net -0.49")
chk(D("-1.39")<D("-1.26"),"PHINIA drag -1.39 exceeds whole-quarter fund return -1.26 in size")
gaps=[D("0.06"),D("0.18"),D("0.24"),D("0.32"),D("0.27"),D("0.28"),D("0.19")]
inst=[D("-1.20"),D("8.40"),D("7.92"),D("18.48"),D("8.92"),D("9.96"),D("7.28")]
inv=[D("-1.26"),D("8.22"),D("7.68"),D("18.16"),D("8.65"),D("9.68"),D("7.09")]
chk(all(r2(i-j)==g for i,j,g in zip(inst,inv,gaps)),"institutional minus investor gaps 0.06..0.32")
chk(r2(D("80.8")/D("15700")*100)==D("0.51"),"fund assets about 0.51 pct of firm AUM")
print("TOTAL PASS",ok)
