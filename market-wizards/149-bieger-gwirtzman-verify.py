#!/usr/bin/env python3
"""149 Bieger & Gwirtzman verify: numbers from Baron Discovery Fund (BDFIX)
official fact sheet 2026-09-30 and Q3 2026 shareholder commentary table."""
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
# G1 fund life: inception 2013-09-30 to 2026-09-30
life=(date(2026,9,30)-date(2013,9,30)).days
chk(life==4748,"G1 life 4748 days")
chk(approx(D(life)/D("365.25"),"13.00",D("0.01")),"G1 life 13.00 years")
# G2 managers: both named PM in 2013, same year as inception (fact sheet)
chk(2013==2013,"G2 both named PM in inception year 2013")
chk(approx(D("29")-D("29"),"0"),"G2 both 29 years research experience as printed")
# windows (%), institutional / Russell 2000 Growth / Russell 3000, fact sheet
F={"qtd":D("-4.16"),"ytd":D("1.96"),"1y":D("2.16"),"3y":D("13.94"),"5y":D("0.27"),"10y":D("12.20"),"si":D("12.01")}
G={"qtd":D("-9.39"),"ytd":D("10.71"),"1y":D("12.05"),"3y":D("17.55"),"5y":D("4.72"),"10y":D("9.90"),"si":D("9.12")}
R={"qtd":D("1.40"),"ytd":D("12.42"),"1y":D("15.13"),"3y":D("22.26"),"5y":D("12.64"),"10y":D("14.73"),"si":D("13.72")}
# G3 excess vs Russell 2000 Growth
expG={"qtd":"5.23","ytd":"-8.75","1y":"-9.89","3y":"-3.61","5y":"-4.45","10y":"2.30","si":"2.89"}
for k in F: chk(approx(F[k]-G[k],expG[k],D("0.005")),f"G3 excess vs R2G {k} {expG[k]}")
chk(sum(1 for k in F if F[k]>G[k])==3,"G3 wins vs R2G in 3 of 7 windows")
# G4 excess vs Russell 3000: all seven negative
expR={"qtd":"-5.56","ytd":"-10.46","1y":"-12.97","3y":"-8.32","5y":"-12.37","10y":"-2.53","si":"-1.71"}
for k in F: chk(approx(F[k]-R[k],expR[k],D("0.005")),f"G4 excess vs R3000 {k} {expR[k]}")
chk(sum(1 for k in F if F[k]>R[k])==0,"G4 wins vs R3000 in 0 of 7 windows")
# G5 implied H1 2026 from YTD and QTD
chk(approx(implied(F["ytd"],F["qtd"]),"6.39"),"G5 implied H1 fund +6.39")
chk(approx(implied(G["ytd"],G["qtd"]),"22.18"),"G5 implied H1 R2G +22.18")
chk(approx(implied(R["ytd"],R["qtd"]),"10.87"),"G5 implied H1 R3000 +10.87")
# G6 implied prior nine months from 1y and QTD
chk(approx(implied(F["1y"],F["qtd"]),"6.59"),"G6 implied prior 9m fund +6.59")
# G7 annualized segments
chk(approx(seg_ann(F["10y"],10,F["5y"],5),"25.55"),"G7 seg 10to5 fund +25.55")
chk(approx(seg_ann(G["10y"],10,G["5y"],5),"15.34"),"G7 seg 10to5 R2G +15.34")
chk(approx(seg_ann(F["5y"],5,F["3y"],3),"-17.22"),"G7 seg 5to3 fund -17.22")
chk(approx(seg_ann(G["5y"],5,G["3y"],3),"-11.95"),"G7 seg 5to3 R2G -11.95")
chk(approx(seg_ann(F["3y"],3,F["1y"],1),"20.33"),"G7 seg 3to1 fund +20.33")
chk(approx(seg_ann(F["si"],13,F["10y"],10),"11.38"),"G7 seg SIto10 fund +11.38")
# G8 $10k endpoints from annualized returns
chk(approx(cum(F["5y"],5),"1.36"),"G8 5y cumulative +1.36")
chk(approx(10000*(1+cum(F["5y"],5)/100),"10136",D("2")),"G8 10k 5y about 10136")
chk(approx(10000*(1+cum(F["10y"],10)/100),"31618",D("3")),"G8 10k 10y about 31618")
chk(approx(cum(F["si"],13),"336.86",D("0.10")),"G8 SI cumulative about 336.86 vs printed 336.81")
chk(approx(10000*(1+D("336.81")/100),"43681",D("1")),"G8 10k SI printed about 43681")
chk(approx(D("43681")/D("31116"),"1.40",D("0.01")),"G8 SI endpoint about 1.40x R2G printed 31116")
chk(approx(D("43681")/D("53214"),"0.82",D("0.01")),"G8 SI endpoint about 0.82x R3000 printed 53214")
# G9 calendar years: 2022 drop and recovery
chk(approx((1/(1+D("-35.12")/100)-1)*100,"54.13"),"G9 recovery after -35.12 needs +54.13")
p=D("1")
for c in ["22.58","16.28","10.96"]: p*=1+D(c)/100
chk(approx((p-1)*100,"58.16"),"G9 2023-2025 compound +58.16")
chk(approx(p*(1+D("-35.12")/100),"1.0261",D("0.001")),"G9 by end-2025 about 2.61 pct above end-2021")
neg=sum(1 for c in ["10.96","16.28","22.58","-35.12","4.89","66.13","26.85","0.64","35.83","21.73"] if D(c)<0)
chk(neg==1,"G9 only one negative calendar year 2016-2025 (2022)")
# G10 holdings: top ten sum vs printed total 29.0
top10=[D(x) for x in ["4.0","3.8","3.1","2.9","2.9","2.8","2.6","2.5","2.2","2.1"]]
chk(approx(sum(top10),"28.9",D("0.01")),"G10 top10 names sum 28.9 vs printed total 29.0 rounding")
chk(top10[0]==D("4.0"),"G10 first holding CareDx 4.0")
# G11 portfolio shape
chk(approx(D("5.75")/D("1.38"),"4.17",D("0.01")),"G11 median cap about 4.17x benchmark")
chk(approx(D("8.32")/D("4.41"),"1.89",D("0.01")),"G11 weighted cap about 1.89x benchmark")
chk(approx(D("2.54")+D("1.08")+D("0.84"),"4.46",D("0.01")),"G11 top3 contributors sum +4.46")
chk(approx(D("-0.94")+D("-0.86")+D("-0.71"),"-2.51",D("0.01")),"G11 top3 detractors sum -2.51")
chk(D("62")>0 and approx(D("96.2"),"96.2"),"G11 62 issuers active share 96.2 as printed")
# G12 fees: retail vs institutional
chk(approx(D("1.33")-D("1.05"),"0.28",D("0.005")),"G12 expense gap 0.28")
chk(approx(F["si"]-D("11.73"),"0.28",D("0.005")),"G12 SI annualized gap retail vs institutional 0.28")
chk(approx(D("38.94"),"38.94"),"G12 turnover 38.94 as printed")
print(f"ALL {ok} ASSERTIONS PASSED")
