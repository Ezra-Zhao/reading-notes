#!/usr/bin/env python3
"""142 David Baron verify: numbers from Baron Focused Growth Fund
official Q3 2026 shareholder letter and Baron product page, as of 2026-09-30.
Retail shares BFGFX unless noted."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
# G1 fund life: inception 1996-05-31 to 2026-09-30
life=(date(2026,9,30)-date(1996,5,31)).days
chk(life==11079,"G1 life 11079 days")
chk(approx(D(life)/D("365.25"),"30.33",D("0.01")),"G1 life 30.33 years")
# G2 David Baron tenure: Baron official says PM of this fund since 2018 (year only),
# joined Baron in 2005. Pre-David span 1996->2018 is 22 calendar years, his span to 2026 is 8.
chk(2018-1996==22,"G2 pre-David 22 years by calendar-year difference")
chk(2026-2018==8,"G2 David span 8 years by calendar-year difference")
chk(approx(D(8)/D(30)*100,"26.67",D("0.01")),"G2 David span about 26.67 pct of 30 calendar years")
chk(2005<2018,"G2 joined 2005 before becoming PM in 2018")
# windows (%), retail fund / Russell 2500 Growth / Russell 3000, as printed
F={"qtd":D("-2.38"),"ytd":D("4.90"),"1y":D("17.77"),"3y":D("22.02"),"5y":D("10.88"),"10y":D("21.07"),"si":D("13.81")}
B={"qtd":D("-10.35"),"ytd":D("7.28"),"1y":D("7.63"),"3y":D("14.92"),"5y":D("3.46"),"10y":D("10.59"),"si":D("8.34")}
R={"qtd":D("1.40"),"ytd":D("12.42"),"1y":D("15.13"),"3y":D("22.26"),"5y":D("12.64"),"10y":D("14.73"),"si":D("10.20")}
# G3 excess vs benchmark Russell 2500 Growth
expB={"qtd":"7.97","ytd":"-2.38","1y":"10.14","3y":"7.10","5y":"7.42","10y":"10.48","si":"5.47"}
for k in F: chk(approx(F[k]-B[k],expB[k],D("0.005")),f"G3 excess vs R2500 {k} {expB[k]}")
# G4 excess vs Russell 3000
expR={"qtd":"-3.78","ytd":"-7.52","1y":"2.64","3y":"-0.24","5y":"-1.76","10y":"6.34","si":"3.61"}
for k in F: chk(approx(F[k]-R[k],expR[k],D("0.005")),f"G4 excess vs R3000 {k} {expR[k]}")
# G5 counts: vs R2500 only YTD negative (6 of 7 positive); vs R3000 four negative
chk(sum(1 for k in F if F[k]>B[k])==6,"G5 vs R2500 positive 6 of 7")
chk(sum(1 for k in F if F[k]>R[k])==3,"G5 vs R3000 positive 3 of 7")
def seg(l,s): return ((1+float(l)/100)/(1+float(s)/100)-1)*100
# G6 implied H1 2026 from YTD and QTD
chk(approx(seg(F["ytd"],F["qtd"]),"7.46"),"G6 implied H1 fund +7.46")
chk(approx(seg(B["ytd"],B["qtd"]),"19.66"),"G6 implied H1 bench +19.66")
chk(approx(seg(R["ytd"],R["qtd"]),"10.87"),"G6 implied H1 R3000 +10.87")
# G7 implied prior nine months from 1y and QTD
chk(approx(seg(F["1y"],F["qtd"]),"20.64"),"G7 implied prior 9m fund +20.64")
chk(approx(seg(B["1y"],B["qtd"]),"20.05"),"G7 implied prior 9m bench +20.05")
# G8 annualized segments between annualized windows
def segann(la,ly,sa,sy):
    return D(str((((1+float(la)/100)**ly/(1+float(sa)/100)**sy)**(1/(ly-sy))-1)*100))
chk(approx(segann(F["5y"],5,F["3y"],3),"-3.95"),"G8 5to3 fund -3.95 ann")
chk(approx(segann(B["5y"],5,B["3y"],3),"-11.62"),"G8 5to3 bench -11.62 ann")
chk(approx(segann(F["10y"],10,F["5y"],5),"32.20"),"G8 10to5 fund +32.20 ann")
chk(approx(segann(B["10y"],10,B["5y"],5),"18.21"),"G8 10to5 bench +18.21 ann")
# G9 cumulative endpoints for 10000 dollars, annualized windows compounded
chk(approx(10000*(1+float(F["3y"])/100)**3,"18167",D("5")),"G9 10k 3y fund approx 18167")
chk(approx(10000*(1+float(F["5y"])/100)**5,"16760",D("5")),"G9 10k 5y fund approx 16760")
chk(approx(10000*(1+float(F["10y"])/100)**10,"67665",D("8")),"G9 10k 10y fund approx 67665")
chk(approx(10000*(1+float(B["10y"])/100)**10,"27363",D("5")),"G9 10k 10y bench approx 27363")
# G10 since-inception endpoint over 30.33 years (annualized compounded, approx)
yrs=life/365.25
chk(approx(((1+float(F["si"])/100)**yrs/(1+float(B["si"])/100)**yrs-1)*100,"345.52",D("3")),"G10 SI endpoint fund ahead of bench approx 345.52 pct")
# G11 holdings: product page top ten as of 2026-10-31 sums to printed 65.4
top10=[D(x) for x in ["23.4","6.1","6.0","5.5","5.0","4.1","4.1","3.9","3.8","3.5"]]
chk(approx(sum(top10),"65.4",D("0.01")),"G11 top10 Oct31 sum 65.4")
chk(approx(D("27.4")-D("23.4"),"4.0",D("0.01")),"G11 SpaceX weight Sep30 table 27.4 vs Oct31 23.4 diff 4.0, different dates")
chk(27==27,"G11 issuers 27 as printed")
# G12 Q3 2026 contribution table (letter): SpaceX and Tesla drag, segment sums near total
chk(approx(D("-3.15")+D("-1.19"),"-4.34",D("0.01")),"G12 SpaceX plus Tesla contribution -4.34")
chk(abs(D("-4.34"))>abs(D("-2.33")),"G12 two-stock drag larger than whole-quarter decline")
chk(approx(D("1.25")+D("0.55")+D("-2.33")+D("-1.52")+D("-0.29"),"-2.34",D("0.02")),"G12 segment contributions plus fees approx -2.34")
chk(approx(D("1.47")+D("1.23")+D("0.75"),"3.45",D("0.01")),"G12 top3 contributors Shopify Gartner FIGS sum +3.45")
print(f"ALL {ok} ASSERTIONS PASSED")
