#!/usr/bin/env python3
"""137 Wang Mingxu verify: numbers from GF Domestic Demand Growth Q3 2026 report data as republished by Sina Finance (2026-10-29, table to 2026-09-30)."""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(cond,label):
    global ok
    assert cond, f"FAIL {label}"
    ok+=1; print(f"PASS {label}")
def approx(a,b,tol=D("0.02")):
    return abs(D(str(a))-D(str(b)))<=tol
# G1 life
life=(date(2026,9,30)-date(2010,4,19)).days
chk(life==6008,"G1 life 6008 days")
chk(approx(D(life)/D("365.25"),"16.45",D("0.01")),"G1 life 16.45 years")
# G2 tenure
ten=(date(2026,9,30)-date(2018,10,17)).days
chk(ten==2905,"G2 tenure 2905 days")
chk(approx(D(ten)/D("365.25"),"7.95",D("0.01")),"G2 tenure 7.95 years")
chk(approx(D(ten)/D(life)*100,"48.35",D("0.01")),"G2 tenure share 48.35")
chk(life-ten==3103,"G2 pre-tenure 3103 days not his")
# windows: fund, bench (cumulative, non-annualized)
F={"3m":D("-7.09"),"6m":D("13.14"),"1y":D("17.46"),"3y":D("11.49"),"5y":D("-12.16"),"si":D("92.68")}
B={"3m":D("-7.97"),"6m":D("-1.41"),"1y":D("-2.90"),"3y":D("16.16"),"5y":D("4.38"),"si":D("72.33")}
# G3 excess
exp={"3m":"0.88","6m":"14.55","1y":"20.36","3y":"-4.67","5y":"-16.54","si":"20.35"}
for k in F: chk(approx(F[k]-B[k],exp[k],D("0.005")),f"G3 excess {k} {exp[k]}")
# G4 sign pattern: 4 positive, 2 negative; negatives are 3y and 5y
chk(sum(1 for k in F if F[k]>B[k])==4,"G4 four windows beat bench")
chk(F["3y"]<B["3y"] and F["5y"]<B["5y"],"G4 only 3y and 5y lose")
def seg(long,short): return ((1+long/100)/(1+short/100)-1)*100
# G5 implied Q2 2026 from 6m and 3m
chk(approx(seg(F["6m"],F["3m"]),"21.77"),"G5 Q2 fund +21.77")
chk(approx(seg(B["6m"],B["3m"]),"7.13"),"G5 Q2 bench +7.13")
chk(approx(seg(F["6m"],F["3m"])-seg(B["6m"],B["3m"]),"14.65",D("0.03")),"G5 Q2 excess +14.65")
# G6 prior 9 months of 1y window
chk(approx(seg(F["1y"],F["3m"]),"26.43"),"G6 prior9m fund +26.43")
chk(approx(seg(B["1y"],B["3m"]),"5.51"),"G6 prior9m bench +5.51")
# G7 segment 5y-ago to 3y-ago
chk(approx(seg(F["5y"],F["3y"]),"-21.21"),"G7 5to3y fund -21.21")
chk(approx(seg(B["5y"],B["3y"]),"-10.14"),"G7 5to3y bench -10.14")
# G8 segment 3y-ago to 1y-ago
chk(approx(seg(F["3y"],F["1y"]),"-5.08"),"G8 3to1y fund -5.08")
chk(approx(seg(B["3y"],B["1y"]),"19.63"),"G8 3to1y bench +19.63")
chk(approx(seg(B["3y"],B["1y"])-seg(F["3y"],F["1y"]),"24.71",D("0.03")),"G8 gap 24.71 pts")
# G9 recovery prices
chk(approx((1/(1+F["3m"]/100)-1)*100,"7.63"),"G9 recover Q3 +7.63")
chk(approx((1/(1+F["5y"]/100)-1)*100,"13.84"),"G9 recover 5y +13.84")
# G10 10k endpoints since inception
chk(approx(10000*(1+F["si"]/100),"19268",D("1")),"G10 10k fund 19268")
chk(approx(10000*(1+B["si"]/100),"17233",D("1")),"G10 10k bench 17233")
# G11 annualized since inception
yrs=life/365.25
chk(approx(((1+float(F["si"])/100)**(1/yrs)-1)*100,"4.07",D("0.02")),"G11 ann fund 4.07")
chk(approx(((1+float(B["si"])/100)**(1/yrs)-1)*100,"3.36",D("0.02")),"G11 ann bench 3.36")
# G12 scale: end 2.90 yi, -10.26% QoQ -> Q2 end
chk(approx(D("2.90")/(1-D("10.26")/100),"3.23",D("0.01")),"G12 Q2 scale 3.23 yi")
print(f"ALL {ok} assertions passed")
