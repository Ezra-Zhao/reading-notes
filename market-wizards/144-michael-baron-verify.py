#!/usr/bin/env python3
"""144 Michael Baron verify: numbers from Baron Partners Fund fact sheet
(Institutional Shares BPTIX, Baron Capital official, as of 2026-09-30).
All returns % unless noted."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
def seg(long_cum,short_cum): return ((1+float(long_cum)/100)/(1+float(short_cum)/100)-1)*100
def cum(ann,years): return ((1+float(ann)/100)**float(years)-1)*100
def seg_ann(long_ann,long_yrs,short_ann,short_yrs):
    lc=(1+float(long_ann)/100)**float(long_yrs); sc=(1+float(short_ann)/100)**float(short_yrs)
    return ((lc/sc)**(1/(float(long_yrs)-float(short_yrs)))-1)*100
# G1 fund life: inception 1992-01-31 to 2026-09-30
life=(date(2026,9,30)-date(1992,1,31)).days
yrs=D(life)/D("365.25")
chk(life==12661,"G1 life 12661 days")
chk(approx(yrs,"34.66",D("0.01")),"G1 life 34.66 years")
# G2 managers: Ron since 1992 (year only, inception year); Michael since 2018 (year only)
tmax=(date(2026,9,30)-date(2018,1,1)).days
tmin=(date(2026,9,30)-date(2018,12,31)).days
chk(tmax==3194 and tmin==2830,"G2 Michael tenure 2830-3194 days")
chk(approx(D(tmin)/D(life)*100,"22.35",D("0.01")) and approx(D(tmax)/D(life)*100,"25.23",D("0.01")),"G2 Michael tenure 22.35-25.23 pct of life")
chk(life-tmax==9467,"G2 at least 9467 pre-Michael days are not co-managed by him")
# windows (%), fund / Russell Midcap Growth / Russell 3000, fact sheet performance table
F={"qtd":D("-4.36"),"ytd":D("5.59"),"1y":D("25.72"),"3y":D("23.89"),"5y":D("11.62"),"10y":D("24.53"),"si":D("15.74")}
M={"qtd":D("-5.84"),"ytd":D("1.01"),"1y":D("-2.73"),"3y":D("15.36"),"5y":D("4.92"),"10y":D("11.86"),"si":D("10.02")}
R={"qtd":D("1.40"),"ytd":D("12.42"),"1y":D("15.13"),"3y":D("22.26"),"5y":D("12.64"),"10y":D("14.73"),"si":D("10.81")}
# G3 excess vs Midcap Growth (annualized windows plus qtd/ytd)
expM={"qtd":"1.48","ytd":"4.58","1y":"28.45","3y":"8.53","5y":"6.70","10y":"12.67","si":"5.72"}
for k in F: chk(approx(F[k]-M[k],expM[k],D("0.005")),f"G3 excess vs RMG {k} {expM[k]}")
# G4 excess vs Russell 3000; only 5y annualized window negative among annualized, qtd/ytd also negative
expR={"qtd":"-5.76","ytd":"-6.83","1y":"10.59","3y":"1.63","5y":"-1.02","10y":"9.80","si":"4.93"}
for k in F: chk(approx(F[k]-R[k],expR[k],D("0.005")),f"G4 excess vs R3 {k} {expR[k]}")
chk(sum(1 for k in ["1y","3y","5y","10y","si"] if F[k]>M[k])==5,"G4 all 5 annualized windows beat RMG")
chk(sum(1 for k in ["1y","3y","5y","10y","si"] if F[k]>R[k])==4,"G4 4 of 5 annualized windows beat R3")
# G5 implied H1 2026 from YTD and Q3
chk(approx(seg(F["ytd"],F["qtd"]),"10.40"),"G5 implied H1 fund +10.40")
chk(approx(seg(M["ytd"],M["qtd"]),"7.27"),"G5 implied H1 RMG +7.27")
chk(approx(seg(R["ytd"],R["qtd"]),"10.87"),"G5 implied H1 R3 +10.87")
# G6 segment 10 to 5 years ago, annualized
chk(approx(seg_ann(F["10y"],10,F["5y"],5),"38.93"),"G6 seg 10to5 fund +38.93")
chk(approx(seg_ann(M["10y"],10,M["5y"],5),"19.26"),"G6 seg 10to5 RMG +19.26")
# G7 segment 5 to 3 years ago, annualized (2022 buried here)
chk(approx(seg_ann(F["5y"],5,F["3y"],3),"-4.54"),"G7 seg 5to3 fund -4.54")
chk(approx(seg_ann(M["5y"],5,M["3y"],3),"-9.00"),"G7 seg 5to3 RMG -9.00")
chk(approx(seg_ann(R["5y"],5,R["3y"],3),"-0.39"),"G7 seg 5to3 R3 -0.39")
# G8 segment since-inception to 10 years ago, annualized
chk(approx(seg_ann(F["si"],yrs,F["10y"],10),"12.36"),"G8 seg SIto10 fund +12.36")
chk(approx(seg_ann(M["si"],yrs,M["10y"],10),"9.28"),"G8 seg SIto10 RMG +9.28")
# G9 USD 10k endpoints, 10y and since inception
chk(approx(10000*(1+float(F["10y"])/100)**10,"89689",D("2")),"G9 10k 10y fund 89689")
chk(approx(10000*(1+float(M["10y"])/100)**10,"30672",D("2")),"G9 10k 10y RMG 30672")
chk(approx(10000*(1+float(F["si"])/100)**float(yrs),"1587036",D("300")),"G9 10k SI fund approx 1587036")
chk(approx(10000*(1+float(M["si"])/100)**float(yrs),"273886",D("300")),"G9 10k SI RMG approx 273886")
chk(approx(D("1587036")/D("273886"),"5.79",D("0.02")),"G9 SI endpoint fund about 5.79x RMG")
# G10 calendar years 2016-2025: compound, negatives, 2022 recovery
cal=[D(x) for x in ["4.29","31.91","-1.75","45.38","149.18","31.73","-42.41","43.47","33.08","24.86"]]
prod=1.0
for v in cal: prod*=1+float(v)/100
chk(approx((prod-1)*100,"785.52",D("0.05")),"G10 calendar 2016-2025 compound +785.52")
chk(sum(1 for v in cal if v<0)==2,"G10 only 2 negative calendar years in 2016-2025")
chk(approx((1/(1-0.4241)-1)*100,"73.64"),"G10 recovery after -42.41 is +73.64")
chk(approx(((1.4347*1.3308*1.2486)-1)*100,"138.40",D("0.05")),"G10 2023-2025 compound +138.40")
# G11 holdings and Q3 attribution
top=[D(x) for x in ["32.6","13.4","5.2","4.3","4.2","3.6","3.6","3.3","3.3","3.1"]]
chk(approx(sum(top),"76.6",D("0.01")),"G11 top10 sum 76.6 as printed")
chk(approx(D("32.6")/sum(top)*100,"42.56"),"G11 SpaceX 42.56 pct of top10 total")
chk(approx(D("-3.55")+D("-2.96"),"-6.51",D("0.01")),"G11 SpaceX plus Tesla Q3 contribution -6.51")
chk(approx(D("-4.36")-D("-6.51"),"2.15",D("0.01")),"G11 rest of book offset +2.15 vs Q3 -4.36")
chk(approx(D("1.41")+D("1.25")+D("0.96"),"3.62",D("0.01")),"G11 top3 contributors sum +3.62")
# G12 portfolio facts: leverage, cap ratio, turnover horizon
chk(approx(D("109.6")+D("-9.6"),"100.0",D("0.01")),"G12 long 109.6 plus cash -9.6 equals 100.0")
chk(approx(D("882.89")/D("13.40"),"65.89"),"G12 weighted avg cap 65.89x median cap")
chk(approx(D("100")/D("6.16"),"16.23"),"G12 turnover 6.16 pct implies 16.23y horizon")
print(f"ALL {ok} ASSERTIONS PASSED")
