#!/usr/bin/env python3
"""143 Feng Mingyuan verify: numbers from Xinda Aoyin's XinAo New Energy
Industry Stock Fund (001410) official Q3 2026 quarterly report, as of 2026-09-30.
A shares unless noted."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
def seg(l,s): return ((1+float(l)/100)/(1+float(s)/100)-1)*100
# G1 fund life: inception 2015-07-31 to 2026-09-30
life=(date(2026,9,30)-date(2015,7,31)).days
chk(life==4079,"G1 life 4079 days")
chk(approx(D(life)/D("365.25"),"11.17",D("0.01")),"G1 life 11.17 years")
# G2 manager tenure: Feng Mingyuan from 2016-10-19 (report section 4.1)
ten=(date(2026,9,30)-date(2016,10,19)).days
pre=(date(2016,10,19)-date(2015,7,31)).days
chk(ten==3633,"G2 tenure 3633 days")
chk(pre==446,"G2 pre-manager 446 days")
chk(approx(D(ten)/D(life)*100,"89.07",D("0.01")),"G2 tenure 89.07 pct of fund life")
# windows (%), A fund / benchmark, as printed in report 3.2.1
F={"3m":D("-32.52"),"6m":D("24.74"),"1y":D("19.54"),"3y":D("89.95"),"5y":D("21.94"),"7y":D("230.69"),"10y":D("524.32"),"si":D("568.02")}
B={"3m":D("-10.50"),"6m":D("-1.33"),"1y":D("-4.60"),"3y":D("18.06"),"5y":D("-5.29"),"7y":D("18.49"),"10y":D("38.40"),"si":D("22.77")}
# G3 excess as printed
exp={"3m":"-22.02","6m":"26.07","1y":"24.14","3y":"71.89","5y":"27.23","7y":"212.20","10y":"485.92","si":"545.25"}
for k in F: chk(approx(F[k]-B[k],exp[k],D("0.005")),f"G3 excess {k} {exp[k]}")
# G4 counts: only 3m excess negative, 7 of 8 positive
chk(sum(1 for k in F if F[k]>B[k])==7,"G4 excess positive 7 of 8")
chk(sum(1 for k in F if F[k]<0)==1,"G4 fund negative only in 3m window")
# G5 implied Q2 2026 from 6m and 3m
chk(approx(seg(F["6m"],F["3m"]),"84.85"),"G5 implied Q2 fund +84.85")
chk(approx(seg(B["6m"],B["3m"]),"10.25"),"G5 implied Q2 bench +10.25")
# G6 implied prior nine months from 1y and 3m
chk(approx(seg(F["1y"],F["3m"]),"77.15"),"G6 implied prior 9m fund +77.15")
chk(approx(seg(B["1y"],B["3m"]),"6.59"),"G6 implied prior 9m bench +6.59")
# G7 recovery needed after -32.52 pct
chk(approx((1/(1+float(F["3m"])/100)-1)*100,"48.19"),"G7 recovery +48.19 after -32.52")
# G8 cumulative segments between windows
chk(approx(seg(F["5y"],F["3y"]),"-35.80"),"G8 seg 5to3 fund -35.80")
chk(approx(seg(B["5y"],B["3y"]),"-19.78"),"G8 seg 5to3 bench -19.78")
chk(approx(seg(F["7y"],F["5y"]),"171.19"),"G8 seg 7to5 fund +171.19")
chk(approx(seg(F["10y"],F["7y"]),"88.79"),"G8 seg 10to7 fund +88.79")
chk(approx(seg(F["si"],F["10y"]),"7.00"),"G8 seg SIto10 fund +7.00")
chk(approx(seg(B["si"],B["10y"]),"-11.29"),"G8 seg SIto10 bench -11.29")
# G9 realized vs profit, A plus C (yuan)
real=D("309767079.74")+D("16883907.91")
prof=D("-2736481207.46")+D("-154873026.35")
chk(approx(real,"326650987.65",D("0.01")),"G9 realized A+C 326650987.65")
chk(approx(prof,"-2891354233.81",D("0.01")),"G9 profit A+C -2891354233.81")
chk(approx(prof-real,"-3218005221.46",D("0.01")),"G9 unrealized -3218005221.46")
chk(approx(abs(prof-real)/real,"9.85",D("0.01")),"G9 unrealized loss about 9.85x realized gain")
# G10 holdings: top ten weights sum, first holding small
top10=[D(x) for x in ["2.48","2.29","2.06","2.05","1.96","1.93","1.89","1.83","1.77","1.70"]]
chk(approx(sum(top10),"19.96",D("0.01")),"G10 top10 sum 19.96")
chk(top10[0]==D("2.48"),"G10 first holding 2.48")
# G11 industry / asset mix
chk(approx(D("80.32")/D("91.31")*100,"87.96"),"G11 manufacturing 87.96 pct of stock book")
chk(approx(D("5138683823.59")/D("5627504610.94")*100,"91.31",D("0.02")),"G11 stocks 91.31 pct of NAV")
chk(approx(D("5367714391.57")+D("259790219.37"),"5627504610.94",D("0.01")),"G11 end NAV A+C 5627504610.94")
# G12 share changes in Q3
chk(approx((D("842847929.69")/D("912058223.77")-1)*100,"-7.59"),"G12 A shares -7.59 pct in Q3")
chk(approx((D("41071254.93")/D("49548671.30")-1)*100,"-17.11"),"G12 C shares -17.11 pct in Q3")
chk(approx((D("883919184.62")/D("961606895.07")-1)*100,"-8.08"),"G12 total shares -8.08 pct in Q3")
print(f"ALL {ok} ASSERTIONS PASSED")
