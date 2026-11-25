#!/usr/bin/env python3
"""140 Alex Umansky verify: numbers from Baron Durable Advantage Fund (BDAIX)
official Q3 2026 shareholder letter and Baron product page, as of 2026-09-30."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
# G1 fund life: inception 2017-12-29 to 2026-09-30
life=(date(2026,9,30)-date(2017,12,29)).days
chk(life==3197,"G1 life 3197 days")
chk(approx(D(life)/D("365.25"),"8.75",D("0.01")),"G1 life 8.75 years")
# G2 tenure: strategy fact sheet says Umansky named PM of this fund in 2017;
# fund inception 2017-12-29 and Q3 2026 letter signed by him as Portfolio Manager.
# Tenure therefore covers essentially the whole fund life; start only precise to year.
chk(date(2017,12,29).year==2017,"G2 fund inception year equals his named-PM year 2017")
# annualized/total windows (%), BDAIX institutional / S&P 500, as printed
F={"qtd":D("2.23"),"ytd":D("5.70"),"1y":D("8.49"),"3y":D("21.30"),"5y":D("13.74"),"si":D("15.64")}
B={"qtd":D("2.30"),"ytd":D("12.75"),"1y":D("15.74"),"3y":D("22.89"),"5y":D("13.79"),"si":D("14.59")}
# G3 excess: only since-inception positive; 5y misses by 0.05
exp={"qtd":"-0.07","ytd":"-7.05","1y":"-7.25","3y":"-1.59","5y":"-0.05","si":"1.05"}
for k in F: chk(approx(F[k]-B[k],exp[k],D("0.005")),f"G3 excess {k} {exp[k]}")
chk(sum(1 for k in F if F[k]>B[k])==1 and F["si"]>B["si"],"G3 only since-inception window positive, 1 of 6")
# G4 retail vs institutional gap (fee gap, printed in letter)
chk(approx(D("15.64")-D("15.36"),"0.28",D("0.005")),"G4 retail SI trails institutional by 0.28")
chk(approx(D("13.74")-D("13.45"),"0.29",D("0.005")),"G4 retail 5y trails institutional by 0.29")
def seg(l,s): return ((1+float(l)/100)/(1+float(s)/100)-1)*100
# G5 implied H1 2026 from YTD and Q3: the lag sits in H1, Q3 was a near tie
chk(approx(seg(F["ytd"],F["qtd"]),"3.39"),"G5 implied H1 2026 fund +3.39")
chk(approx(seg(B["ytd"],B["qtd"]),"10.22"),"G5 implied H1 2026 bench +10.22")
chk(approx(seg(F["ytd"],F["qtd"])-seg(B["ytd"],B["qtd"]),"-6.82"),"G5 H1 gap approx -6.82 pts (return diff)")
# G6 implied Q4 2025 from 1y and YTD: essentially tied
chk(approx(seg(F["1y"],F["ytd"]),"2.64"),"G6 implied Q4 2025 fund +2.64")
chk(approx(seg(B["1y"],B["ytd"]),"2.65"),"G6 implied Q4 2025 bench +2.65")
chk(approx(seg(F["1y"],F["ytd"])-seg(B["1y"],B["ytd"]),"-0.01"),"G6 Q4 2025 gap approx -0.01, a tie")
def segann(la,ly,sa,sy):
    return D(str((((1+float(la)/100)**ly/(1+float(sa)/100)**sy)**(1/(ly-sy))-1)*100))
# G7 segment 5y-ago to 3y-ago (annualized): fund won the older segment
chk(approx(segann(F["5y"],5,F["3y"],3),"3.27"),"G7 5to3 fund +3.27 ann")
chk(approx(segann(B["5y"],5,B["3y"],3),"1.39"),"G7 5to3 bench +1.39 ann")
# G8 segment 3y-ago to 1y-ago (annualized): fund also won this segment;
# the 3y deficit is created by the most recent year alone
chk(approx(segann(F["3y"],3,F["1y"],1),"28.26"),"G8 3to1 fund +28.26 ann")
chk(approx(segann(B["3y"],3,B["1y"],1),"26.63"),"G8 3to1 bench +26.63 ann")
# G9 cumulative endpoints: 3y and 5y (annualized windows compounded)
chk(approx(10000*(1+float(F["3y"])/100)**3,"17848",D("3")),"G9 10k 3y fund approx 17848")
chk(approx(10000*(1+float(B["3y"])/100)**3,"18559",D("3")),"G9 10k 3y bench approx 18559")
chk(approx(10000*(1+float(F["5y"])/100)**5,"19036",D("3")),"G9 10k 5y fund approx 19036")
chk(approx(10000*(1+float(B["5y"])/100)**5,"19077",D("3")),"G9 10k 5y bench approx 19077")
# G10 since-inception endpoint over 8.75 years: fund ahead by about 8.31%
yrs=life/365.25
chk(approx(10000*(1+float(F["si"])/100)**yrs,"35676",D("30")),"G10 10k SI fund approx 35676")
chk(approx(10000*(1+float(B["si"])/100)**yrs,"32939",D("30")),"G10 10k SI bench approx 32939")
chk(approx(((1+float(F["si"])/100)**yrs/(1+float(B["si"])/100)**yrs-1)*100,"8.31"),"G10 SI endpoint fund ahead approx 8.31 pct")
# G11 portfolio shape (letter, 2026-09-30): top10 sum, top20, sector split, count
top10=[D(x) for x in ["10.0","9.7","7.2","7.0","6.2","6.0","5.2","5.2","4.5","3.5"]]
chk(approx(sum(top10),"64.5",D("0.01")),"G11 top10 sum 64.5 pct of net assets")
chk(approx(D("87.6")-D("64.5"),"23.1",D("0.01")),"G11 holdings 11-20 sum 23.1 pct")
chk(approx(D("64.8")+D("33.1")+D("2.1"),"100.0",D("0.01")),"G11 sector split sums to 100.0")
# G12 Q3 contributors (letter): top3 contributed more than the whole quarter's gain;
# 13 contributors vs 16 detractors out of 29 investments
chk(approx(D("1.74")+D("1.30")+D("1.15"),"4.19",D("0.01")),"G12 top3 contributors sum +4.19")
chk(approx(D("1.74")+D("1.30")+D("1.15")+D("0.38")+D("0.36"),"4.93",D("0.01")),"G12 top5 contributors sum +4.93")
chk(13+16==29,"G12 13 contributors + 16 detractors = 29 investments")
print(f"ALL {ok} ASSERTIONS PASSED")
