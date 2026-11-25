#!/usr/bin/env python3
"""138 Andrew Peck verify: numbers from Baron Asset Fund (BARIX) official fact sheet 2026-09-30."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
# G1 life: inception 1987-06-12 to 2026-09-30
life=(date(2026,9,30)-date(1987,6,12)).days
chk(life==14355,"G1 life 14355 days")
chk(approx(D(life)/D("365.25"),"39.30",D("0.01")),"G1 life 39.30 years")
# G2 tenure: fact sheet says only "named portfolio manager in 2003" -> range
ten_max=(date(2026,9,30)-date(2003,1,1)).days
ten_min=(date(2026,9,30)-date(2003,12,31)).days
chk(ten_max==8673 and ten_min==8309,"G2 tenure range 8309-8673 days")
chk(approx(D(ten_min)/D(life)*100,"57.88",D("0.01")) and approx(D(ten_max)/D(life)*100,"60.42",D("0.01")),"G2 tenure share 57.88-60.42 pct")
chk(life-ten_max==5682,"G2 at least 5682 pre-tenure days not his")
# annualized windows (%), BARIX / Russell Midcap Growth / Russell 3000
F={"1y":D("10.97"),"3y":D("11.50"),"5y":D("2.41"),"10y":D("11.06"),"si":D("11.12")}
G={"1y":D("-2.73"),"3y":D("15.36"),"5y":D("4.92"),"10y":D("11.86"),"si":D("10.27")}
R={"1y":D("15.13"),"3y":D("22.26"),"5y":D("12.64"),"10y":D("14.73"),"si":D("10.76")}
# G3 excess vs Midcap Growth
expG={"1y":"13.70","3y":"-3.86","5y":"-2.51","10y":"-0.80","si":"0.85"}
for k in F: chk(approx(F[k]-G[k],expG[k],D("0.005")),f"G3 excess vs RMG {k} {expG[k]}")
# G4 excess vs Russell 3000 + sign patterns
expR={"1y":"-4.16","3y":"-10.76","5y":"-10.23","10y":"-3.67","si":"0.36"}
for k in F: chk(approx(F[k]-R[k],expR[k],D("0.005")),f"G4 excess vs R3000 {k} {expR[k]}")
chk(sum(1 for k in F if F[k]>G[k])==2,"G4 vs RMG only 2 of 5 windows positive")
chk(sum(1 for k in F if F[k]>R[k])==1 and F["si"]>R["si"],"G4 vs R3000 only since-inception positive")
def seg(l,s): return ((1+l/100)/(1+s/100)-1)*100
# G5 implied H1 2026 from YTD and Q3 (non-annualized)
chk(approx(seg(D("2.86"),D("-6.22")),"9.68"),"G5 H1 fund +9.68")
chk(approx(seg(D("1.01"),D("-5.84")),"7.27"),"G5 H1 RMG +7.27")
chk(approx(seg(D("12.42"),D("1.40")),"10.87"),"G5 H1 R3000 +10.87")
def segann(la,ly,sa,sy):
    return D(str((((1+float(la)/100)**ly/(1+float(sa)/100)**sy)**(1/(ly-sy))-1)*100))
# G6 segment 10y-ago to 5y-ago (annualized)
chk(approx(segann(F["10y"],10,F["5y"],5),"20.44"),"G6 10to5 fund +20.44")
chk(approx(segann(G["10y"],10,G["5y"],5),"19.26"),"G6 10to5 RMG +19.26")
chk(approx(segann(R["10y"],10,R["5y"],5),"16.86"),"G6 10to5 R3000 +16.86")
# G7 segment 5y-ago to 3y-ago: both fund and RMG negative
chk(approx(segann(F["5y"],5,F["3y"],3),"-9.85"),"G7 5to3 fund -9.85")
chk(approx(segann(G["5y"],5,G["3y"],3),"-9.00"),"G7 5to3 RMG -9.00")
chk(approx(segann(R["5y"],5,R["3y"],3),"-0.39"),"G7 5to3 R3000 -0.39")
# G8 segment 3y-ago to 1y-ago
chk(approx(segann(F["3y"],3,F["1y"],1),"11.77"),"G8 3to1 fund +11.77")
chk(approx(segann(G["3y"],3,G["1y"],1),"25.63"),"G8 3to1 RMG +25.63")
# G9 10k endpoints, 10 years
chk(approx(10000*(1+float(F["10y"])/100)**10,"28548",D("2")),"G9 10k 10y fund 28548")
chk(approx(10000*(1+float(G["10y"])/100)**10,"30672",D("2")),"G9 10k 10y RMG 30672")
chk(approx(10000*(1+float(R["10y"])/100)**10,"39516",D("2")),"G9 10k 10y R3000 39516")
# G10 10k endpoints, since inception (39.30y; index inception date noted as 1987-06-30 in fact sheet)
yrs=life/365.25
chk(approx(10000*(1+float(F["si"])/100)**yrs,"630550",D("300")),"G10 10k SI fund approx 630550")
chk(approx(10000*(1+float(G["si"])/100)**yrs,"466287",D("300")),"G10 10k SI RMG approx 466287")
chk(approx(10000*(1+float(R["si"])/100)**yrs,"555050",D("300")),"G10 10k SI R3000 approx 555050")
# G11 calendar years 2016-2025: only one negative year (2022)
cal=[D("8.20"),D("10.77"),D("17.35"),D("-25.87"),D("14.22"),D("33.33"),D("37.96"),D("0.14"),D("26.49"),D("6.51")]
chk(sum(1 for c in cal if c<0)==1,"G11 only one negative calendar year 2022")
chk(approx((1/(1+D("-25.87")/100)-1)*100,"34.90"),"G11 2022 recovery price +34.90")
chk(approx(((1+D("-25.87")/100)*(1+D("17.35")/100)-1)*100,"-13.01"),"G11 2022-2023 compound -13.01")
# G12 holdings / structure
top=[D("30.5"),D("4.9"),D("3.8"),D("3.8"),D("3.7"),D("3.6"),D("3.4"),D("3.2"),D("2.8"),D("2.4")]
chk(approx(sum(top),"62.1",D("0.05")),"G12 top10 rows sum 62.1 (fact sheet prints 62.0, rounding)")
chk(approx(D("30.5")/D("62.0")*100,"49.19"),"G12 SpaceX 49.19 pct of printed top10 total")
chk(approx(D("100")/D("5.11"),"19.57"),"G12 turnover 5.11 pct implies approx 19.57y holding")
chk(approx(D("4.01")/D("6.22")*100,"64.47"),"G12 SpaceX Q3 detractor 64.47 pct of Q3 loss")
chk(approx(D("673.22")/D("23.20"),"29.02"),"G12 weighted avg cap 29.02x median")
print(f"ALL {ok} assertions passed")
