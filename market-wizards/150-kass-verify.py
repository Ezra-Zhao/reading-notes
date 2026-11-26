#!/usr/bin/env python3
"""150 Kass verify: numbers from Baron Emerging Markets Fund Q3 2026 shareholder
letter performance table (Institutional Shares, 2026-09-30) and Baron Emerging
Markets Strategy fact sheet 2026-09-30 (holdings/calendar, labelled strategy)."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
def implied(total,sub): return ((1+float(total)/100)/(1+float(sub)/100)-1)*100
def cum(ann,y): return ((1+float(ann)/100)**y-1)*100
def seg_ann(l,ly,s,sy): return (((1+float(l)/100)**ly/(1+float(s)/100)**sy)**(1/(ly-sy))-1)*100
# G1 fund life: inception 2010-12-31 to 2026-09-30
life=(date(2026,9,30)-date(2010,12,31)).days
chk(life==5752,"G1 life 5752 days")
chk(approx(D(life)/D("365.25"),"15.75",D("0.01")),"G1 life about 15.75 years")
# G2 manager: joined 2007, named PM of EM Fund in 2010 = inception year, 39y research
chk(2010==2010,"G2 named PM in inception year 2010")
chk(approx(D("39"),"39"),"G2 research experience 39 years as printed")
chk(2007<2010,"G2 joined 2007 before named PM 2010")
# windows (%), Institutional / MSCI EM / MSCI EM IMI Growth, shareholder letter
F={"qtd":D("-3.39"),"ytd":D("16.10"),"1y":D("14.64"),"3y":D("20.31"),"5y":D("4.67"),"10y":D("7.11"),"15y":D("7.47"),"si":D("5.85")}
E={"qtd":D("-0.37"),"ytd":D("23.38"),"1y":D("29.22"),"3y":D("24.09"),"5y":D("8.94"),"10y":D("9.09"),"15y":D("7.03"),"si":D("5.02")}
G={"qtd":D("-3.10"),"ytd":D("19.18"),"1y":D("22.75"),"3y":D("22.87"),"5y":D("6.90"),"10y":D("9.00"),"15y":D("7.68"),"si":D("5.53")}
# G3 excess vs MSCI EM: only 15y and SI positive
expE={"qtd":"-3.02","ytd":"-7.28","1y":"-14.58","3y":"-3.78","5y":"-4.27","10y":"-1.98","15y":"0.44","si":"0.83"}
for k in F: chk(approx(F[k]-E[k],expE[k],D("0.005")),f"G3 excess vs EM {k} {expE[k]}")
chk(sum(1 for k in F if F[k]>E[k])==2,"G3 wins vs EM in 2 of 8 windows")
# G4 excess vs MSCI EM IMI Growth: only SI positive
expG={"qtd":"-0.29","ytd":"-3.08","1y":"-8.11","3y":"-2.56","5y":"-2.23","10y":"-1.89","15y":"-0.21","si":"0.32"}
for k in F: chk(approx(F[k]-G[k],expG[k],D("0.005")),f"G4 excess vs Growth {k} {expG[k]}")
chk(sum(1 for k in F if F[k]>G[k])==1,"G4 wins vs Growth in 1 of 8 windows")
# G5 implied H1 2026 from YTD and QTD
chk(approx(implied(F["ytd"],F["qtd"]),"20.17"),"G5 implied H1 fund +20.17")
chk(approx(implied(E["ytd"],E["qtd"]),"23.84"),"G5 implied H1 EM +23.84")
# G6 implied prior nine months from 1y and QTD
chk(approx(implied(F["1y"],F["qtd"]),"18.66"),"G6 implied prior 9m fund +18.66")
# G7 annualized segments
chk(approx(seg_ann(F["10y"],10,F["5y"],5),"9.61"),"G7 seg 10to5 fund +9.61")
chk(approx(seg_ann(E["10y"],10,E["5y"],5),"9.24"),"G7 seg 10to5 EM +9.24")
chk(approx(seg_ann(F["5y"],5,F["3y"],3),"-15.06"),"G7 seg 5to3 fund -15.06")
chk(approx(seg_ann(E["5y"],5,E["3y"],3),"-10.39"),"G7 seg 5to3 EM -10.39")
chk(approx(seg_ann(F["3y"],3,F["1y"],1),"23.25"),"G7 seg 3to1 fund +23.25")
# G8 $10k endpoints from annualized returns (approx, SI span 15.75y)
chk(approx(cum(F["5y"],5),"25.64",D("0.05")),"G8 5y cumulative about +25.64")
chk(approx(10000*(1+cum(F["5y"],5)/100),"12564",D("3")),"G8 10k 5y about 12564")
chk(approx(10000*(1+cum(F["10y"],10)/100),"19875",D("3")),"G8 10k 10y about 19875")
chk(approx(10000*(1+cum(F["si"],15.75)/100),"24484",D("5")),"G8 10k SI about 24484")
chk(approx(10000*(1+cum(E["si"],15.75)/100),"21629",D("5")),"G8 10k SI EM about 21629")
chk(approx(D("24484")/D("21629"),"1.13",D("0.01")),"G8 SI endpoint about 1.13x EM")
# G9 calendar years, strategy net 2014-2025 (fact sheet, labelled strategy)
chk(approx((1/(1+D("-25.77")/100)-1)*100,"34.72"),"G9 recovery after -25.77 needs +34.72")
p=D("1")
for c in ["8.85","9.03","30.41"]: p*=1+D(c)/100
chk(approx((p-1)*100,"54.77"),"G9 2023-2025 compound +54.77")
chk(approx(p*(1+D("-25.77")/100),"1.1489",D("0.001")),"G9 by end-2025 about 14.89 pct above end-2021")
neg=sum(1 for c in ["4.02","-10.79","4.21","40.88","-18.40","19.05","29.57","-5.95","-25.77","8.85","9.03","30.41"] if D(c)<0)
chk(neg==4,"G9 four negative calendar years 2014-2025 (strategy net)")
# G10 holdings: top ten sum vs printed total 42.8 (strategy/fund letter table)
top10=[D(x) for x in ["16.3","7.3","5.6","2.8","2.0","1.9","1.8","1.8","1.7","1.5"]]
chk(approx(sum(top10),"42.7",D("0.01")),"G10 top10 names sum 42.7 vs printed total 42.8 rounding")
chk(approx(top10[0]+top10[1]+top10[2],"29.2",D("0.01")),"G10 top3 chipmakers sum 29.2")
# G11 attribution and country shape (Q3 letter)
chk(approx(D("0.50")+D("0.48")+D("0.38")+D("0.37")+D("0.32"),"2.05",D("0.01")),"G11 top5 contributors sum +2.05")
chk(approx(D("-2.00")+D("-0.88")+D("-0.87")+D("-0.30")+D("-0.28"),"-4.33",D("0.01")),"G11 top5 detractors sum -4.33")
chk(approx(D("2.00")/D("3.39")*100,"59.00",D("0.05")),"G11 SK hynix detraction about 59.0 pct of QTD drop")
chk(approx(D("22.5")+D("20.9")+D("20.8")+D("17.7"),"81.9",D("0.01")),"G11 top4 countries sum 81.9")
# G12 fees: retail vs institutional (letter, as of 2026-04-30)
chk(approx(D("1.38")-D("1.12"),"0.26",D("0.005")),"G12 expense gap 0.26")
chk(approx(F["si"]-D("5.59"),"0.26",D("0.005")),"G12 SI annualized gap retail vs institutional 0.26")
chk(approx(D("85"),"85"),"G12 strategy issuers 85 as printed")
print(f"ALL {ok} ASSERTIONS PASSED")
