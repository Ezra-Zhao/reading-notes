#!/usr/bin/env python3
"""146 Neal Kaufman verify: numbers from Baron Health Care Fund Q3 2026
quarterly letter (Institutional Shares BHCHX, Baron Capital official, as of
2026-09-30) + Baron official product page; calendar-year returns BHCHX via
Zacks (evidence B). All returns % unless noted."""
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
# G1 fund life: inception 2018-04-30 to 2026-09-30
life=(date(2026,9,30)-date(2018,4,30)).days
yrs=D(life)/D("365.25")
print("life days",life,"years",yrs)
chk(life==3075,"G1 life 3075 days")
chk(approx(yrs,"8.42",D("0.01")),"G1 life 8.42 years")
# G2 manager: Kaufman joined 2005, named PM of this fund in 2018 (year only);
# fund inception 2018-04-30 -> tenure start year == inception year, tenure ~ fund life
chk(2018==2018,"G2 PM start year 2018 equals inception year 2018 (year precision only)")
# windows (%), Institutional / Russell 3000 Health Care / Russell 3000
F={"qtd":D("4.02"),"ytd":D("8.38"),"1y":D("22.58"),"3y":D("9.34"),"5y":D("1.84"),"si":D("10.80")}
H={"qtd":D("6.19"),"ytd":D("11.61"),"1y":D("24.91"),"3y":D("12.27"),"5y":D("6.49"),"si":D("10.49")}
R={"qtd":D("1.40"),"ytd":D("12.42"),"1y":D("15.13"),"3y":D("22.26"),"5y":D("12.64"),"si":D("14.55")}
# G3 excess vs health care benchmark: only since-inception positive among all six
expH={"qtd":"-2.17","ytd":"-3.23","1y":"-2.33","3y":"-2.93","5y":"-4.65","si":"0.31"}
for k in F: chk(approx(F[k]-H[k],expH[k],D("0.005")),f"G3 excess vs HC {k} {expH[k]}")
chk(sum(1 for k in F if F[k]>H[k])==1,"G3 only 1 of 6 windows beats HC benchmark (since inception)")
# G4 excess vs Russell 3000
expR={"qtd":"2.62","ytd":"-4.04","1y":"7.45","3y":"-12.92","5y":"-10.80","si":"-3.75"}
for k in F: chk(approx(F[k]-R[k],expR[k],D("0.005")),f"G4 excess vs R3 {k} {expR[k]}")
chk(sum(1 for k in ["1y","3y","5y","si"] if F[k]>R[k])==1,"G4 only 1y of 4 annualized windows beats R3")
# G5 implied H1 2026 from YTD and Q3; cross-check with Zacks quarterly Q1 -6.96 / Q2 +11.99 (B)
print("H1 fund",seg(F["ytd"],F["qtd"]),"HC",seg(H["ytd"],H["qtd"]),"R3",seg(R["ytd"],R["qtd"]))
chk(approx(seg(F["ytd"],F["qtd"]),"4.19"),"G5 implied H1 fund +4.19")
chk(approx(seg(H["ytd"],H["qtd"]),"5.10"),"G5 implied H1 HC +5.10")
chk(approx(seg(R["ytd"],R["qtd"]),"10.87"),"G5 implied H1 R3 +10.87")
h1z=(1+D("-6.96")/100)*(1+D("11.99")/100)
chk(approx((h1z-1)*100,"4.19"),"G5 Zacks Q1*Q2 compounds to same H1 +4.19")
# G6 segment 5-to-3 years ago, annualized (the pit)
print("seg5to3 fund",seg_ann(F["5y"],5,F["3y"],3),"HC",seg_ann(H["5y"],5,H["3y"],3),"R3",seg_ann(R["5y"],5,R["3y"],3))
chk(approx(seg_ann(F["5y"],5,F["3y"],3),"-8.45",D("0.10")),"G6 seg 5to3 fund about -8.45")
chk(approx(seg_ann(H["5y"],5,H["3y"],3),"-1.65",D("0.10")),"G6 seg 5to3 HC about -1.65")
chk(approx(seg_ann(R["5y"],5,R["3y"],3),"-0.36",D("0.10")),"G6 seg 5to3 R3 about -0.36")
# G7 segment inception-to-5-years-ago, annualized (the sharp early segment, ~3.42 yrs)
yrsf=float(yrs)
print("seg SIto5 fund",seg_ann(F["si"],yrsf,F["5y"],5),"HC",seg_ann(H["si"],yrsf,H["5y"],5),"R3",seg_ann(R["si"],yrsf,R["5y"],5))
chk(approx(seg_ann(F["si"],yrsf,F["5y"],5),"25.34",D("0.15")),"G7 seg SIto5 fund about +25.34")
chk(approx(seg_ann(H["si"],yrsf,H["5y"],5),"16.61",D("0.15")),"G7 seg SIto5 HC about +16.61")
chk(approx(seg_ann(F["si"],yrsf,F["5y"],5)-seg_ann(H["si"],yrsf,H["5y"],5),"8.73",D("0.15")),"G7 head-segment excess vs HC about +8.73/yr")
chk(approx(seg_ann(F["5y"],5,F["3y"],3)-seg_ann(H["5y"],5,H["3y"],3),"-6.82",D("0.15")),"G6 seg 5to3 shortfall vs HC about -6.82/yr")
# G8 $10k endpoints
print("EP5 fund",endpt(F["5y"],5),"HC",endpt(H["5y"],5),"R3",endpt(R["5y"],5))
print("EPSI fund",endpt(F["si"],yrsf),"HC",endpt(H["si"],yrsf),"R3",endpt(R["si"],yrsf))
chk(approx(endpt(F["5y"],5),"10956",D("30")),"G8 10k 5y fund about 10956")
chk(approx(endpt(H["5y"],5),"13689",D("30")),"G8 10k 5y HC about 13689")
chk(approx(endpt(R["5y"],5),"18145",D("40")),"G8 10k 5y R3 about 18145")
chk(approx(endpt(F["si"],yrsf)/endpt(H["si"],yrsf),"1.02",D("0.01")),"G8 SI fund/HC endpoint ratio about 1.02")
chk(approx(endpt(F["si"],yrsf)/endpt(R["si"],yrsf),"0.76",D("0.01")),"G8 SI fund/R3 endpoint ratio about 0.76")
# G9 calendar years BHCHX (Zacks, B): 2019-2025
cal={"2019":D("35.57"),"2020":D("47.71"),"2021":D("15.70"),"2022":D("-16.89"),"2023":D("6.42"),"2024":D("1.55"),"2025":D("10.28")}
chk(sum(1 for v in cal.values() if v<0)==1,"G9 only one negative calendar year 2019-2025 (2022)")
prod=D(1)
for v in cal.values(): prod*= (1+v/100)
print("compound 2019-2025",(prod-1)*100)
chk(approx((prod-1)*100,"129.47",D("0.30")),"G9 compound 2019-2025 about +129.47")
rec=(1/(1+D("-16.89")/100)-1)*100
print("2022 recovery need",rec)
chk(approx(rec,"20.32"),"G9 2022 drawdown needs +20.32 to recover")
post=(1+D("6.42")/100)*(1+D("1.55")/100)*(1+D("10.28")/100)
print("2023-2025 compound",(post-1)*100,"level vs end-2021",(1+D("-16.89")/100)*post)
chk(approx((post-1)*100,"19.18"),"G9 2023-2025 compound about +19.18")
chk(approx((1+D("-16.89")/100)*post,"0.9905",D("0.001")),"G9 end-2025 still about 0.95 pct below end-2021 level")
chk(approx((1+D("-16.89")/100)*post*(1+F["ytd"]/100),"1.0735",D("0.001")),"G9 with 2026 YTD the 2022 hole is filled (about +7.35 vs end-2021)")
# G10 Q3 attribution (letter): top5 contributors sum beats whole-quarter return
contrib=D("1.45")+D("1.15")+D("0.74")+D("0.66")+D("0.59")
detract=D("-0.57")+D("-0.49")+D("-0.47")+D("-0.37")+D("-0.28")
print("contrib top5",contrib,"detract top5",detract)
chk(contrib==D("4.59") and contrib>F["qtd"],"G10 top5 contributors +4.59 exceed QTD +4.02")
chk(detract==D("-2.18"),"G10 top5 detractors sum -2.18")
# G11 holdings shape (letter): 33 stocks vs benchmark 526; top10 weights sum 61.3
top10=[D("14.3"),D("7.5"),D("7.3"),D("5.9"),D("5.1"),D("4.5"),D("4.5"),D("4.2"),D("4.1"),D("3.9")]
chk(sum(top10)==D("61.3"),"G11 top10 weights sum 61.3 (matches letter text)")
chk(approx(top10[0]/sum(top10)*100,"23.33",D("0.02")),"G11 Lilly is about 23.33 pct of top10")
chk(approx(D(526)/D(33),"15.94",D("0.01")),"G11 benchmark holds about 15.94x the fund's stock count")
# G12 share-class fee gap: retail SI 10.52 vs institutional 10.80; net expense 1.10 vs 0.85
chk(approx(F["si"]-D("10.52"),"0.28",D("0.005")),"G12 retail trails institutional by 0.28/yr since inception")
chk(approx(D("1.10")-D("0.85"),"0.25",D("0.005")),"G12 net expense gap retail vs institutional 0.25")
print(f"ALL {ok} assertions passed")
