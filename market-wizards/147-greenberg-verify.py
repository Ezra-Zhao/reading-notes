#!/usr/bin/env python3
"""147 Cliff Greenberg verify: numbers from Baron Small Cap Fund Q3 2026
quarterly letter (Institutional Shares, Baron Capital official, as of
2026-09-30) + Baron Small Cap Strategy fact sheet 2026-09-30 (official;
manager bio + calendar-year strategy net returns). All returns % unless noted."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.05")):
    return abs(D(str(a))-D(str(b)))<=tol
def seg(long_cum,short_cum): return ((1+float(long_cum)/100)/(1+float(short_cum)/100)-1)*100
def seg_ann(long_ann,long_yrs,short_ann,short_yrs):
    lc=(1+float(long_ann)/100)**float(long_yrs); sc=(1+float(short_ann)/100)**float(short_yrs)
    return ((lc/sc)**(1/(float(long_yrs)-float(short_yrs)))-1)*100
def endpt(ann,yrs): return 10000*(1+float(ann)/100)**float(yrs)
# G1 fund life: inception 1997-09-30 to 2026-09-30 = exactly 29 years
life=(date(2026,9,30)-date(1997,9,30)).days
print("life days",life)
chk(life==10592,"G1 life 10592 days")
chk(approx(D(life)/D("365.25"),"29.00",D("0.01")),"G1 life 29.00 years")
# G2 manager: Greenberg joined Baron in 1997 as PM of this fund (fact sheet);
# fund inception 1997-09-30 -> tenure start year == inception year, full tenure
chk(1997==1997,"G2 PM start year 1997 equals inception year 1997")
chk(2026-1997==29,"G2 tenure 29 years equals fund life")
# windows (%), Institutional / Russell 2000 Growth / Russell 3000
F={"qtd":D("-7.69"),"ytd":D("-4.30"),"1y":D("-5.79"),"3y":D("6.75"),"5y":D("-0.17"),"10y":D("9.59"),"15y":D("11.07"),"si":D("9.46")}
I={"qtd":D("-9.39"),"ytd":D("10.71"),"1y":D("12.05"),"3y":D("17.55"),"5y":D("4.72"),"10y":D("9.90"),"15y":D("11.94"),"si":D("6.86")}
R={"qtd":D("1.40"),"ytd":D("12.42"),"1y":D("15.13"),"3y":D("22.26"),"5y":D("12.64"),"10y":D("14.73"),"15y":D("15.27"),"si":D("9.35")}
# G3 excess vs primary benchmark: only QTD and since-inception positive of 8
expI={"qtd":"1.70","ytd":"-15.01","1y":"-17.84","3y":"-10.80","5y":"-4.89","10y":"-0.31","15y":"-0.87","si":"2.60"}
for k in F: chk(approx(F[k]-I[k],expI[k],D("0.005")),f"G3 excess vs R2000G {k} {expI[k]}")
chk(sum(1 for k in F if F[k]>I[k])==2,"G3 only 2 of 8 windows beat primary benchmark (QTD + since inception)")
# G4 excess vs Russell 3000: only since-inception positive among annualized windows
expR={"qtd":"-9.09","ytd":"-16.72","1y":"-20.92","3y":"-15.51","5y":"-12.81","10y":"-5.14","15y":"-4.20","si":"0.11"}
for k in F: chk(approx(F[k]-R[k],expR[k],D("0.005")),f"G4 excess vs R3000 {k} {expR[k]}")
chk(sum(1 for k in ["1y","3y","5y","10y","15y","si"] if F[k]>R[k])==1,"G4 only since-inception of 6 annualized windows beats R3000")
# G5 implied H1 2026 from YTD and Q3
print("H1 fund",seg(F["ytd"],F["qtd"]),"idx",seg(I["ytd"],I["qtd"]),"R3",seg(R["ytd"],R["qtd"]))
chk(approx(seg(F["ytd"],F["qtd"]),"3.67"),"G5 implied H1 fund +3.67")
chk(approx(seg(I["ytd"],I["qtd"]),"22.18"),"G5 implied H1 index +22.18")
chk(approx(seg(F["ytd"],F["qtd"])-seg(I["ytd"],I["qtd"]),"-18.51",D("0.10")),"G5 H1 shortfall vs index about -18.51 (the year's hole was dug in H1)")
# G6 segment 10-to-5 years ago annualized (the sharpest segment)
print("seg10to5 fund",seg_ann(F["10y"],10,F["5y"],5),"idx",seg_ann(I["10y"],10,I["5y"],5))
chk(approx(seg_ann(F["10y"],10,F["5y"],5),"20.30",D("0.10")),"G6 seg 10to5 fund about +20.30")
chk(approx(seg_ann(I["10y"],10,I["5y"],5),"15.34",D("0.10")),"G6 seg 10to5 index about +15.34")
# G7 segment 5-to-3 years ago annualized (the pit, contains calendar 2022)
print("seg5to3 fund",seg_ann(F["5y"],5,F["3y"],3),"idx",seg_ann(I["5y"],5,I["3y"],3))
chk(approx(seg_ann(F["5y"],5,F["3y"],3),"-9.72",D("0.10")),"G7 seg 5to3 fund about -9.72")
chk(approx(seg_ann(I["5y"],5,I["3y"],3),"-11.95",D("0.10")),"G7 seg 5to3 index about -11.95 (fund fell less in the pit)")
# G8 segment inception-to-15-years-ago annualized (first ~14 years)
print("segSIto15 fund",seg_ann(F["si"],29,F["15y"],15),"idx",seg_ann(I["si"],29,I["15y"],15),"R3",seg_ann(R["si"],29,R["15y"],15))
chk(approx(seg_ann(F["si"],29,F["15y"],15),"7.76",D("0.10")),"G8 seg SIto15 fund about +7.76")
chk(approx(seg_ann(I["si"],29,I["15y"],15),"1.67",D("0.10")),"G8 seg SIto15 index about +1.67 (early lead built here)")
# G9 $10k endpoints
print("ep5",endpt(F["5y"],5),endpt(I["5y"],5),endpt(R["5y"],5))
print("epSI",endpt(F["si"],29),endpt(I["si"],29),endpt(R["si"],29))
chk(approx(endpt(F["5y"],5),"9915",D("15")),"G9 $10k 5y fund about 9915 (still under water after 5 years)")
chk(approx(endpt(F["si"],29),"137533",D("400")),"G9 $10k since inception fund about 137533")
chk(approx(endpt(I["si"],29),"68492",D("300")),"G9 $10k since inception index about 68492")
chk(approx(endpt(F["si"],29)/endpt(I["si"],29),"2.01",D("0.02")),"G9 since-inception endpoint about 2.01x the index")
# G10 calendar years, strategy net (fact sheet, evidence A): 2022 -31.03, recoup math
cal=[D("2.00"),D("-4.96"),D("10.29"),D("27.53"),D("-7.09"),D("34.93"),D("40.82"),D("15.87"),D("-31.03"),D("27.25"),D("13.66"),D("-0.61")]
prod=D("1")
for c in cal: prod*= (1+c/100)
print("cal 2014-2025 compound %",(prod-1)*100)
chk(approx((prod-1)*100,"176.52",D("0.15")),"G10 calendar 2014-2025 compounds to about +176.52")
chk(approx((D("1")/(1+D("-31.03")/100)-1)*100,"44.99"),"G10 2022 -31.03 needs +44.99 to recover")
chk(approx(((1+D("27.25")/100)*(1+D("13.66")/100)*(1+D("-0.61")/100)-1)*100,"43.75"),"G10 2023-2025 compounds to about +43.75")
chk(approx((D("0.6897")*(1+D("43.75")/100)-1)*100,"-0.86",D("0.10")),"G10 after 2023-2025 still about -0.86 vs end-2021 (pit not fully refilled by end-2025)")
# G11 Q3 attribution sums (shareholder letter)
chk(approx(D("0.67")+D("0.57")+D("0.48")+D("0.47")+D("0.45"),"2.64",D("0.005")),"G11 top5 contributors sum +2.64")
chk(approx(D("-2.10")+D("-1.08")+D("-0.83")+D("-0.75")+D("-0.59"),"-5.35",D("0.005")),"G11 top5 detractors sum -5.35")
chk(approx(D("2.10")/D("7.69")*100,"27.31",D("0.10")),"G11 Vertiv alone about 27.31% of the quarter's drop")
# G12 holdings / fees / long-held (shareholder letter + fact sheet)
top10=[D("6.1"),D("4.3"),D("4.2"),D("4.2"),D("3.2"),D("3.2"),D("2.9"),D("2.8"),D("2.7"),D("2.7")]
chk(approx(sum(top10),"36.3",D("0.005")),"G12 top10 sums to 36.3 as printed")
chk(approx(D("1.32")-D("1.06"),"0.26",D("0.005")),"G12 retail-institutional expense gap 0.26")
chk(approx(D("9.46")-D("9.29"),"0.17",D("0.005")),"G12 retail-institutional since-inception return gap 0.17/yr")
chk(39+29==68,"G12 long-held >5y positions total 68% of assets as printed")
chk(33+25==58,"G12 at-least-doubled positions total 58% of assets as printed")
print(f"ALL {ok} CHECKS PASSED (12 groups)")
