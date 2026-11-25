#!/usr/bin/env python3
"""145 Tong Li verify: numbers from Huashang New Trend Preferred Flexible
Allocation Hybrid Fund (166301) official Q3 2026 quarterly report, as of 2026-09-30."""
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
# G1 fund life: inception (transformation) 2015-05-14 to 2026-09-30
life=(date(2026,9,30)-date(2015,5,14)).days
chk(life==4157,"G1 life 4157 days")
chk(approx(D(life)/D("365.25"),"11.38",D("0.01")),"G1 life 11.38 years")
# G2 manager tenure: Tong Li from 2025-03-12 (report section 4.1)
ten=(date(2026,9,30)-date(2025,3,12)).days
pre=(date(2025,3,12)-date(2015,5,14)).days
chk(ten==567,"G2 tenure 567 days")
chk(pre==3590,"G2 pre-manager 3590 days")
chk(approx(D(ten)/D(life)*100,"13.64",D("0.01")),"G2 tenure 13.64 pct of fund life")
chk(approx(D(ten)/D("365.25"),"1.55",D("0.01")),"G2 tenure 1.55 years")
# windows (%), fund / benchmark, as printed in report 3.2.1
F={"3m":D("-27.93"),"6m":D("-4.24"),"1y":D("4.29"),"3y":D("56.24"),"5y":D("71.49"),"7y":D("372.73"),"10y":D("576.34"),"si":D("542.18")}
B={"3m":D("-11.78"),"6m":D("-3.03"),"1y":D("-5.26"),"3y":D("14.47"),"5y":D("-1.18"),"7y":D("20.08"),"10y":D("39.10"),"si":D("14.11")}
# G3 excess as printed
exp={"3m":"-16.15","6m":"-1.21","1y":"9.55","3y":"41.77","5y":"72.67","7y":"352.65","10y":"537.24","si":"528.07"}
for k in F: chk(approx(F[k]-B[k],exp[k],D("0.005")),f"G3 excess {k} {exp[k]}")
# G4 counts: excess positive 6 of 8; negatives only 3m and 6m
chk(sum(1 for k in F if F[k]>B[k])==6,"G4 excess positive 6 of 8")
chk(sum(1 for k in F if F[k]<0)==2,"G4 fund negative in 3m and 6m only")
# G5 implied Q2 2026 from 6m and 3m
chk(approx(seg(F["6m"],F["3m"]),"32.87"),"G5 implied Q2 fund +32.87")
chk(approx(seg(B["6m"],B["3m"]),"9.92"),"G5 implied Q2 bench +9.92")
# G6 implied prior nine months from 1y and 3m
chk(approx(seg(F["1y"],F["3m"]),"44.72"),"G6 implied prior 9m fund +44.72")
chk(approx(seg(B["1y"],B["3m"]),"7.39"),"G6 implied prior 9m bench +7.39")
# G7 recovery needed after -27.93 pct
chk(approx((1/(1+float(F["3m"])/100)-1)*100,"38.76"),"G7 recovery +38.76 after -27.93")
# G8 cumulative segments between windows
chk(approx(seg(F["5y"],F["3y"]),"9.76"),"G8 seg 5to3 fund +9.76")
chk(approx(seg(B["5y"],B["3y"]),"-13.67"),"G8 seg 5to3 bench -13.67")
chk(approx(seg(F["7y"],F["5y"]),"175.66"),"G8 seg 7to5 fund +175.66")
chk(approx(seg(F["10y"],F["7y"]),"43.07"),"G8 seg 10to7 fund +43.07")
chk(approx(seg(F["si"],F["10y"]),"-5.05"),"G8 seg SIto10 fund -5.05")
chk(approx(seg(B["si"],B["10y"]),"-17.97"),"G8 seg SIto10 bench -17.97")
# G9 realized vs profit (yuan, single class fund)
real=D("-371587068.12"); prof=D("-1732787615.35")
chk(approx(prof-real,"-1361200547.23",D("0.01")),"G9 unrealized -1361200547.23")
chk(approx(abs(prof-real)/abs(real),"3.66",D("0.01")),"G9 unrealized loss about 3.66x realized loss")
chk(approx(abs(prof)/D("4127386416.97")*100,"41.98"),"G9 quarterly loss about 41.98 pct of end NAV")
# G10 holdings: top ten weights sum
top10=[D(x) for x in ["5.25","4.62","3.86","3.67","3.50","3.43","3.41","3.16","2.93","2.52"]]
chk(approx(sum(top10),"36.35",D("0.01")),"G10 top10 sum 36.35")
chk(top10[0]==D("5.25"),"G10 first holding 5.25")
# G11 industry / asset mix
chk(approx(D("70.11")/D("86.02")*100,"81.52"),"G11 manufacturing 81.52 pct of stock book")
chk(approx(D("3550444664.67")/D("4127386416.97")*100,"86.02",D("0.02")),"G11 stocks 86.02 pct of NAV")
chk(approx(D("3550444664.67")/D("4147835305.89")*100,"85.60",D("0.02")),"G11 stocks 85.60 pct of total assets")
# G12 share changes in Q3 and NAV cross-check
chk(approx(D("40549888.68")-D("73250408.42"),"-32700519.74",D("0.01")),"G12 net share flow -32700519.74")
chk(approx(D("317459666.85")-D("32700519.74"),"284759147.11",D("0.01")),"G12 end shares 284759147.11")
chk(approx((D("284759147.11")/D("317459666.85")-1)*100,"-10.30"),"G12 total shares -10.30 pct in Q3")
chk(approx(D("284759147.11")*D("14.494"),"4127386416.97",D("150000")),"G12 shares x NAV approx end net assets")
print(f"ALL {ok} ASSERTIONS PASSED")
