#!/usr/bin/env python3
"""136 Michael Lippert verify: all numbers from Baron Opportunity Fund fact sheet (BIOIX, 2026-09-30)."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
# G1 life and tenure range (PM year 2006 only)
life=(date(2026,9,30)-date(2000,2,29)).days
chk(life==9710,"G1 life 9710")
chk(approx(D(life)/D("365.25"),"26.58",D("0.01")),"G1 life years 26.58")
tmax=(date(2026,9,30)-date(2006,1,1)).days; tmin=(date(2026,9,30)-date(2006,12,31)).days
chk(tmax==7577 and tmin==7213,"G1 tenure range 7213-7577")
chk(approx(D(tmin)/D(life)*100,"74.28",D("0.01")),"G1 tenure share min 74.28")
chk(approx(D(tmax)/D(life)*100,"78.03",D("0.01")),"G1 tenure share max 78.03")
pre=life-tmax; chk(pre==2133,"G1 pre-Lippert at least 2133 days not his")
# G2 excess vs Russell 3000 Growth (annualized windows 1,3,5,10,SI)
fund=[D("22.09"),D("31.14"),D("11.62"),D("21.82"),D("10.93")]
r3g=[D("7.58"),D("23.84"),D("13.11"),D("17.62"),D("8.09")]
exp=["14.51","7.30","-1.49","4.20","2.84"]
for f,b,e in zip(fund,r3g,exp): chk(approx(f-b,e,D("0.005")),f"G2 excess R3G {e}")
chk(sum(1 for f,b in zip(fund,r3g) if f>b)==4,"G2 vs R3G 4 of 5 positive")
# G3 excess vs S&P 500
sp=[D("15.74"),D("22.89"),D("13.79"),D("15.33"),D("8.67")]
exp3=["6.35","8.25","-2.17","6.49","2.26"]
for f,b,e in zip(fund,sp,exp3): chk(approx(f-b,e,D("0.005")),f"G3 excess SP {e}")
chk(sum(1 for f,b in zip(fund,sp) if f>b)==4,"G3 vs SP 4 of 5 positive")
chk(fund[2]<r3g[2] and fund[2]<sp[2],"G3 5Y is the only window losing to both")
# G4 non-annualized QTD/YTD
chk(approx(D("0.77")-D("0.45"),"0.32",D("0.005")),"G4 QTD excess R3G +0.32")
chk(approx(D("16.69")-D("6.36"),"10.33",D("0.005")),"G4 YTD excess R3G +10.33")
chk(approx(D("0.77")-D("2.30"),"-1.53",D("0.005")),"G4 QTD excess SP -1.53")
chk(approx(D("16.69")-D("12.75"),"3.94",D("0.005")),"G4 YTD excess SP +3.94")
# G5 implied H1 2026
chk(approx((D("1.1669")/D("1.0077")-1)*100,"15.80"),"G5 H1 fund +15.80")
chk(approx((D("1.0636")/D("1.0045")-1)*100,"5.88"),"G5 H1 R3G +5.88")
chk(approx((D("1.1275")/D("1.0230")-1)*100,"10.22",D("0.02")),"G5 H1 SP +10.22")
chk(approx((D("1.2209")/D("1.0077")-1)*100,"21.16"),"G5 prior 9M of 1Y +21.16")
# G6 SI endpoints (mechanical, years=life/365.25)
yrs=D(life)/D("365.25")
def ep(r): return (D("10000")*( (D("1")+D(str(r))/100) ** yrs ))
# Decimal power with fractional exponent via float fallback check with tolerance 1%
import math
def epf(r): return 10000*(1+r/100)**(life/365.25)
chk(abs(epf(10.93)-157618.39)/157618.39<0.005,"G6 SI endpoint fund approx 157618")
chk(abs(epf(8.09)-79099.21)/79099.21<0.005,"G6 SI endpoint R3G approx 79099")
chk(abs(epf(8.67)-91192.38)/91192.38<0.005,"G6 SI endpoint SP approx 91192")
chk(approx(round(epf(10.93)/epf(8.09),2),"1.99",D("0.01")),"G6 fund/R3G 1.99x")
chk(approx(round(epf(10.93)/epf(8.67),2),"1.73",D("0.01")),"G6 fund/SP 1.73x")
# G7 segments 5-10 and 3-5
def seg(rl,yl,rs,ys):
    return round(((1+rl/100)**yl/(1+rs/100)**ys)**(1/(yl-ys))*100-100,2)
chk(seg(21.82,10,11.62,5)==32.95,"G7 seg 10-5 fund +32.95")
chk(seg(17.62,10,13.11,5)==22.31,"G7 seg 10-5 R3G +22.31")
chk(seg(11.62,5,31.14,3)==-12.35,"G7 seg 5-3 fund -12.35")
chk(seg(13.11,5,23.84,3)==-1.27,"G7 seg 5-3 R3G -1.27")
chk(seg(13.79,5,22.89,3)==1.39,"G7 seg 5-3 SP +1.39")
# G8 segment 1-3 and pre-10
chk(seg(31.14,3,22.09,1)==35.91,"G8 seg 3-1 fund +35.91")
chk(seg(23.84,3,7.58,1)==32.87,"G8 seg 3-1 R3G +32.87")
def pre10(rsi,r10):
    yrs2=life/365.25-10
    return round(((1+rsi/100)**(life/365.25)/(1+r10/100)**10)**(1/yrs2)*100-100,2)
chk(pre10(10.93,21.82)==4.84,"G8 pre10 fund +4.84")
chk(pre10(8.09,17.62)==2.72,"G8 pre10 R3G +2.72")
chk(pre10(8.67,15.33)==4.84,"G8 pre10 SP +4.84 same as fund")
# G9 calendar years 2016-2025
cal_f=[-4.56,40.88,8.35,40.60,89.28,12.29,-42.83,49.98,40.25,19.73]
cal_r=[7.39,29.59,-2.12,35.85,38.26,25.85,-28.97,41.21,32.46,18.15]
cal_s=[11.96,21.83,-4.38,31.49,18.40,28.71,-18.11,26.29,25.02,17.88]
chk(sum(1 for a,b in zip(cal_f,cal_r) if a>b)==7,"G9 cal vs R3G 7 wins 3 losses")
chk(sum(1 for a,b in zip(cal_f,cal_s) if a>b)==7,"G9 cal vs SP 7 wins 3 losses")
chk(sum(1 for a in cal_f if a<0)==2,"G9 only 2 negative calendar years")
chk(approx(D("89.28")-D("38.26"),"51.02",D("0.005")),"G9 2020 excess R3G +51.02")
chk(approx(D("-42.83")-D("-28.97"),"-13.86",D("0.005")),"G9 2022 excess R3G -13.86")
# G10 recovery and 2023-25 rebound
chk(approx((D("1")/D("0.5717")-1)*100,"74.92"),"G10 2022 recovery needs +74.92")
chk(approx(((D("1.4998")*D("1.4025")*D("1.1973"))-1)*100,"151.85",D("0.05")),"G10 2023-25 cum fund +151.85")
# G11 holdings shape
top=[D("16.4"),D("12.9"),D("4.7"),D("4.7"),D("4.2"),D("3.9"),D("3.5"),D("3.4"),D("3.2"),D("2.6")]
chk(sum(top)==D("59.5"),"G11 top10 sums to printed 59.5")
chk(approx((D("16.4")+D("12.9"))/D("59.5")*100,"49.24"),"G11 top2 is 49.24% of top10")
chk(approx(D("1740")/D("110.06"),"15.81"),"G11 wtd avg / median 15.81x")
chk(approx(D("100")/D("25.43"),"3.93"),"G11 turnover implies 3.93y holding")
# G12 Q3 attribution
chk(approx(D("1.70")+D("0.75")+D("0.57"),"3.02",D("0.005")),"G12 top3 contributors +3.02")
chk(approx(D("-2.52")+D("-0.89")+D("-0.53"),"-3.94",D("0.005")),"G12 top3 detractors -3.94")
chk(abs(D("-2.52"))>D("0.77"),"G12 SpaceX detraction larger than whole QTD gain")
print(f"ALL {ok} ASSERTIONS PASS")
