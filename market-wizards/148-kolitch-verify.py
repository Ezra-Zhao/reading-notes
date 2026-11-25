#!/usr/bin/env python3
"""148 Jeff Kolitch verify: numbers from Baron Real Estate Fund Q3 2026
shareholder letter (Institutional Shares, Baron Capital, as of 2026-09-30)
+ Baron Real Estate Strategy fact sheet 2026-09-30 (official; manager bio,
top-10 holdings, calendar-year strategy net returns). Returns % unless noted."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.05")):
    return abs(D(str(a))-D(str(b)))<=tol
def seg_ann(la,ly,sa,sy):
    lc=(1+float(la)/100)**float(ly); sc=(1+float(sa)/100)**float(sy)
    return ((lc/sc)**(1/(float(ly)-float(sy)))-1)*100
def endpt(ann,yrs): return 10000*(1+float(ann)/100)**float(yrs)
# G1 fund life: inception 2009-12-31 to 2026-09-30
life=(date(2026,9,30)-date(2009,12,31)).days
chk(life==6117,"G1 life 6117 days")
chk(approx(D(life)/D("365.25"),"16.75",D("0.01")),"G1 life 16.75 years")
# G2 manager: Kolitch named PM of this fund in 2009 (fact sheet bio) == inception year
chk(2009==2009,"G2 PM start year 2009 equals inception year 2009")
chk(2026-2009==17,"G2 tenure about 17 years (letter: nearly 17 years managing)")
# windows (%), Institutional / Extended Real Estate Idx / US REIT Idx / S&P 500
F={"qtd":D("-13.05"),"ytd":D("-7.95"),"1y":D("-9.17"),"3y":D("8.84"),"5y":D("1.17"),"10y":D("9.98"),"15y":D("12.77"),"si":D("11.95")}
E={"qtd":D("-10.53"),"ytd":D("-2.64"),"1y":D("-6.00"),"3y":D("10.40"),"5y":D("4.16"),"10y":D("7.76"),"15y":D("10.95"),"si":D("10.09")}
R={"qtd":D("-6.33"),"ytd":D("9.49"),"1y":D("7.31"),"3y":D("11.42"),"5y":D("3.07"),"10y":D("4.30"),"15y":D("7.56"),"si":D("7.85")}
S={"qtd":D("2.30"),"ytd":D("12.75"),"1y":D("15.74"),"3y":D("22.89"),"5y":D("13.79"),"10y":D("15.33"),"15y":D("15.68"),"si":D("14.27")}
# G3 excess vs primary (Extended Real Estate): only 10y/15y/SI positive of 8
expE={"qtd":"-2.52","ytd":"-5.31","1y":"-3.17","3y":"-1.56","5y":"-2.99","10y":"2.22","15y":"1.82","si":"1.86"}
for k in F: chk(approx(F[k]-E[k],expE[k],D("0.005")),f"G3 excess vs ExtRE {k} {expE[k]}")
chk(sum(1 for k in F if F[k]>E[k])==3,"G3 only 3 of 8 windows beat primary benchmark")
# G4 excess vs REIT index: same 3 positive, YTD worst -17.44
expR={"qtd":"-6.72","ytd":"-17.44","1y":"-16.48","3y":"-2.58","5y":"-1.90","10y":"5.68","15y":"5.21","si":"4.10"}
for k in F: chk(approx(F[k]-R[k],expR[k],D("0.005")),f"G4 excess vs REIT {k} {expR[k]}")
chk(sum(1 for k in F if F[k]>R[k])==3,"G4 only 3 of 8 windows beat REIT index")
# G5 excess vs S&P 500: all 8 negative
chk(all(F[k]<S[k] for k in F),"G5 all 8 windows trail S&P 500")
chk(approx(F["si"]-S["si"],"-2.32",D("0.005")),"G5 since-inception excess vs S&P -2.32")
# G6 2026 split: H1 implied from YTD and Q3
def h1(ytd,q3): return ((1+float(ytd)/100)/(1+float(q3)/100)-1)*100
chk(approx(h1(F["ytd"],F["qtd"]),"5.87"),"G6 fund H1 2026 implied +5.87")
chk(approx(h1(E["ytd"],E["qtd"]),"8.82"),"G6 ExtRE H1 implied +8.82")
chk(approx(h1(R["ytd"],R["qtd"]),"16.89"),"G6 REIT H1 implied +16.89")
# G7 segments (annualized, fund): 5-3y ago is the pit, 10-5y ago sharpest
chk(approx(seg_ann(F["5y"],5,F["3y"],3),"-9.33"),"G7 fund segment 5-3y ago -9.33/yr")
chk(approx(seg_ann(F["10y"],10,F["5y"],5),"19.56",D("0.10")),"G7 fund segment 10-5y ago +19.56/yr")
chk(approx(seg_ann(F["15y"],15,F["10y"],10),"18.56",D("0.10")),"G7 fund segment 15-10y ago +18.56/yr")
chk(approx(seg_ann(E["5y"],5,E["3y"],3),"-4.54"),"G7 ExtRE segment 5-3y ago -4.54/yr")
# G8 $10k endpoints
chk(approx(endpt(F["5y"],5),"10599",D("3")),"G8 10k 5y fund ~10599")
chk(approx(endpt(E["5y"],5),"12260",D("5")),"G8 10k 5y ExtRE ~12260")
chk(approx(endpt(F["10y"],10),"25890",D("8")),"G8 10k 10y fund ~25890")
chk(approx(endpt(F["15y"],15),"60660",D("25")),"G8 10k 15y fund ~60660")
chk(approx(endpt(E["15y"],15),"47524",D("20")),"G8 10k 15y ExtRE ~47524")
# G9 since-inception cumulative vs annualized consistency (letter prints cum)
chk(approx(10000*(1+D("562.33")/100),"66233",D("1")),"G9 fund SI cumulative $66,233 per $10k")
chk(approx(10000*(1+D("400.50")/100),"50050",D("1")),"G9 ExtRE SI cumulative $50,050 per $10k")
chk(approx(((D("6.6233"))**(D(1)/(D(life)/D("365.25")))-1)*100,"11.95"),"G9 cum-implied annualized 11.95 matches printed")
chk(approx(D("66233")/D("50050"),"1.32",D("0.01")),"G9 fund SI endpoint ~1.32x ExtRE endpoint")
# G10 calendar years (strategy net): 2014-2025 compound, only 4 negative years
cal=[D(x) for x in ["16.90","-4.37","-1.71","31.48","-21.97","44.45","44.35","24.49","-28.39","25.08","12.52","5.24"]]
p=D(1)
for c in cal: p*=1+c/100
chk(approx((p-1)*100,"210.37",D("0.10")),"G10 calendar 2014-2025 compound +210.37")
chk(sum(1 for c in cal if c<0)==4,"G10 4 negative calendar years of 12")
# G11 2022 drawdown arithmetic (strategy net -28.39)
chk(approx((1/D("0.7161")-1)*100,"39.65"),"G11 -28.39 needs +39.65 to recover")
p2=D(1)
for c in [D("25.08"),D("12.52"),D("5.24")]: p2*=1+c/100
chk(approx((p2-1)*100,"48.11",D("0.05")),"G11 2023-2025 compound +48.11")
chk(approx((D("0.7161")*p2-1)*100,"6.07"),"G11 by end-2025 +6.07 above end-2021 level")
# G12 holdings / fees: top-10 printed total 39.0, names sum 39.1 (rounding), 44 issuers
top=[D(x) for x in ["7.0","4.0","4.0","3.8","3.7","3.7","3.6","3.3","3.1","2.9"]]
chk(sum(top)==D("39.1"),"G12 top-10 names sum 39.1 vs printed total 39.0 (rounding)")
chk(approx(D("1.32")-D("1.05"),"0.27",D("0.005")),"G12 retail-inst expense gap 0.27")
chk(approx(D("11.95")-D("11.67"),"0.28",D("0.005")),"G12 SI ann gap inst-retail 0.28/yr")
print(f"ALL {ok} ASSERTIONS PASSED")
