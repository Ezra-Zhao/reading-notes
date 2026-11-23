#!/usr/bin/env python3
"""122 Hoeft / Dodge & Cox Stock Fund (Class X, DOXGX) verification.
Source: Dodge & Cox official Stock Fund Class X fact sheet as of
2026-09-30 (fund inception 1965-01-04; managed by the U.S. Equity
Investment Committee, David Hoeft Chair and CIO, members' tenures at
the firm printed in years). Calendar-year returns and sector mix are
Class I (DODGX) from the Vanguard fact sheet dated 2026-09-30 and are
labelled Class I wherever used. Class X is the primary return series.
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
def seg(a_long,y_long,a_short,y_short):
    return r2((((1+a_long/100)**y_long/(1+a_short/100)**y_short)**(D(1)/(y_long-y_short))-1)*100)
# G1 life: 1965-01-04 to 2026-09-30
life=(date(2026,9,30)-date(1965,1,4)).days
chk(life==22549,"life 22549 days")
chk(r2(D(life)/D("365.25"))==D("61.74"),"life approx 61.74 years")
chk(life>22000,"life over 22000 days")
# G2 committee tenures printed (years at firm): 33,30,22,21,19,17
ten=[33,30,22,21,19,17]
chk(sum(ten)==142,"committee tenures sum 142 years")
chk(r2(D(sum(ten))/D(6))==D("23.67"),"committee mean tenure 23.67 (sheet prints average 23, registered)")
chk(max(ten)==33 and min(ten)==17,"tenure range 17 to 33")
# G3 excess vs S&P 500, seven windows, Class X - all negative
wins=[("3M",D("1.33"),D("2.30"),D("-0.97")),("YTD",D("5.25"),D("12.75"),D("-7.50")),
("1Y",D("7.91"),D("15.74"),D("-7.83")),("3Y",D("14.68"),D("22.89"),D("-8.21")),
("5Y",D("9.67"),D("13.79"),D("-4.12")),("10Y",D("12.39"),D("15.33"),D("-2.94")),
("20Y",D("8.90"),D("11.21"),D("-2.31"))]
for n,f,b,e in wins: chk(f-b==e,f"excess vs SPX {n}")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==7,"all seven windows negative vs SPX")
chk(sum(1 for _,f,b,_ in wins if f-b>0)==0,"zero windows positive vs SPX")
# G4 excess vs Russell 1000 Value - only 10Y/20Y positive
winsv=[("3M",D("1.33"),D("2.61"),D("-1.28")),("YTD",D("5.25"),D("19.27"),D("-14.02")),
("1Y",D("7.91"),D("23.81"),D("-15.90")),("3Y",D("14.68"),D("20.07"),D("-5.39")),
("5Y",D("9.67"),D("11.92"),D("-2.25")),("10Y",D("12.39"),D("11.43"),D("0.96")),
("20Y",D("8.90"),D("8.60"),D("0.30"))]
for n,f,b,e in winsv: chk(f-b==e,f"excess vs R1000V {n}")
chk(sum(1 for _,f,b,_ in winsv if f-b>0)==2,"only two windows positive vs R1000V")
# G5 YTD split: H1 2026 implied
h1f=r2(((1+D("5.25")/100)/(1+D("1.33")/100)-1)*100); h1b=r2(((1+D("12.75")/100)/(1+D("2.30")/100)-1)*100)
chk(h1f==D("3.87"),"H1 fund implied +3.87")
chk(h1b==D("10.22"),"H1 SPX implied +10.22")
chk(r2(h1f-h1b)==D("-6.35"),"H1 excess about -6.35")
# G6 cumulative from annualized (mechanical)
chk(cum(D("14.68"),3)==D("50.82"),"3Y cum fund +50.82")
chk(cum(D("22.89"),3)==D("85.59"),"3Y cum SPX +85.59")
chk(cum(D("9.67"),5)==D("58.65"),"5Y cum fund +58.65")
chk(cum(D("13.79"),5)==D("90.77"),"5Y cum SPX +90.77")
chk(cum(D("12.39"),10)==D("221.57"),"10Y cum fund +221.57")
chk(cum(D("15.33"),10)==D("316.32"),"10Y cum SPX +316.32")
# G7 growth of 10000 over 20 years (mechanical, matches sheet chart window 2006-09-30)
chk(grow(D("8.90"),20)==D("55024.69"),"20Y growth fund 55024.69")
chk(grow(D("11.21"),20)==D("83729.18"),"20Y growth SPX 83729.18")
chk(grow(D("8.60"),20)==D("52071.07"),"20Y growth R1000V 52071.07")
chk(r2(grow(D("8.90"),20)/grow(D("11.21"),20))==D("0.66"),"fund endpoint about 0.66x SPX")
chk(r2(grow(D("8.90"),20)/grow(D("8.60"),20))==D("1.06"),"fund endpoint about 1.06x R1000V")
# G8 segment annualized splits
chk(seg(D("12.39"),10,D("9.67"),5)==D("15.18"),"segment -10Y..-5Y fund 15.18")
chk(seg(D("15.33"),10,D("13.79"),5)==D("16.89"),"segment -10Y..-5Y SPX 16.89")
chk(seg(D("11.43"),10,D("11.92"),5)==D("10.94"),"segment -10Y..-5Y R1000V 10.94")
chk(seg(D("8.90"),20,D("12.39"),10)==D("5.52"),"segment -20Y..-10Y fund 5.52")
chk(seg(D("11.21"),20,D("15.33"),10)==D("7.24"),"segment -20Y..-10Y SPX 7.24")
chk(seg(D("8.60"),20,D("11.43"),10)==D("5.84"),"segment -20Y..-10Y R1000V 5.84")
# G9 calendar years 2016-2025, Class I vs S&P 500
f=[D(x) for x in ("21.28","18.33","-7.07","24.83","7.16","31.73","-7.22","17.48","14.51","13.65")]
b=[D(x) for x in ("11.96","21.83","-4.38","31.49","18.40","28.71","-18.11","26.29","25.02","17.88")]
chk(sum(1 for x,y in zip(f,b) if x>y)==3,"calendar wins 3 of 10")
chk(sum(1 for x,y in zip(f,b) if x<y)==7,"calendar losses 7 of 10")
chk(sum(1 for x in f if x<0)==2,"fund negative calendar years 2")
pf=D(1); pb=D(1)
for x in f: pf*=(1+x/100)
for x in b: pb*=(1+x/100)
chk(r2((pf-1)*100)==D("233.36"),"calendar 10Y compound fund +233.36")
chk(r2((pb-1)*100)==D("298.33"),"calendar 10Y compound SPX +298.33")
# G10 top ten weights, Class X sheet (% of fund)
w=[D(x) for x in ("4.2","3.9","3.7","3.6","3.5","3.2","3.2","2.8","2.3","2.2")]
chk(sum(w)==D("32.6"),"top ten X weights sum 32.6")
chk(w[0]==D("4.2"),"largest holding 4.2")
# G11 sectors, Class I / Vanguard mix sums to 100.0
s=[D(x) for x in ("25.9","17.9","17.8","11.0","10.8","5.0","4.1","3.0","2.0","1.5","1.0")]
chk(sum(s)==D("100.0"),"sectors sum 100.0")
chk(s[0]==D("25.9"),"healthcare largest sector 25.9")
# G12 valuation discount and class gap
chk(r2((1-D("13.4")/D("19.2"))*100)==D("30.21"),"forward PE discount vs SPX 30.21")
chk(r2((1-D("13.4")/D("17.2"))*100)==D("22.09"),"forward PE discount vs R1000V 22.09")
chk(D("7.91")-D("7.82")==D("0.09"),"Class X vs I one-year gap 0.09")
print(f"ALL {ok} CHECKS PASSED")
