#!/usr/bin/env python3
"""126 Ahlsten/Allen (Parnassus Core Equity Institutional, PRILX) verification.
Source: Morningstar Investment Profile, release date 09-30-2026 (one document):
fund inception (Institutional class) 04-28-06, managers Todd C. Ahlsten and
Benjamin E. Allen, annualized returns vs Morningstar US LM Cap Mkt TR USD and
category average, composition, style, sectors, top-10, 38 stock holdings,
turnover 28.45, total fund assets $21,522.63M, expense 0.61.
Manager start months (B grade, Morningstar manager data via Advyzon summary):
Ahlsten since 5/2001, Allen since 5/2012; day-level dates use the 1st of the
month and are labelled approximate. Strategy (Investor class) inception
8/31/1992 per Parnassus official materials.
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
# G1 life / tenure (day counts use month-precision starts, labelled approx)
strat=(date(2026,9,30)-date(1992,8,31)).days
chk(strat==12448,"strategy life 12448 days")
chk(r2(D(strat)/D("365.25"))==D("34.08"),"strategy life approx 34.08 years")
cls=(date(2026,9,30)-date(2006,4,28)).days
chk(cls==7460,"institutional class life 7460 days")
chk(r2(D(cls)/D("365.25"))==D("20.42"),"class life approx 20.42 years")
ahl=(date(2026,9,30)-date(2001,5,1)).days
chk(ahl==9283,"Ahlsten tenure approx 9283 days (from 2001-05-01)")
chk(r2(D(ahl)/D("365.25"))==D("25.42"),"Ahlsten tenure approx 25.42 years")
chk(r2(D(ahl)/D(strat)*100)==D("74.57"),"Ahlsten tenure 74.57 pct of strategy life")
pre=(date(2001,5,1)-date(1992,8,31)).days
chk(pre==3165,"pre-Ahlsten 3165 days")
chk(pre+ahl==strat,"pre + Ahlsten = strategy life")
alln=(date(2026,9,30)-date(2012,5,1)).days
chk(alln==5265,"Allen tenure approx 5265 days (from 2012-05-01)")
chk(ahl-alln==4018,"Ahlsten solo lead before Allen approx 4018 days")
# G2 excess vs benchmark: five windows, all negative
wins=[("YTD",D("9.23"),D("12.90"),D("-3.67")),("1Y",D("11.04"),D("15.59"),D("-4.55")),("3Y",D("17.52"),D("22.99"),D("-5.47")),("5Y",D("10.43"),D("13.27"),D("-2.84")),("10Y",D("13.67"),D("15.21"),D("-1.54"))]
for n,f,b,e in wins: chk(f-b==e,f"excess vs benchmark {n}")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==5,"all five windows negative vs benchmark")
chk(max(e for *_,e in wins)==D("-1.54"),"closest window vs benchmark is 10Y -1.54")
# G3 excess vs category: six windows, five negative, only SI positive
cat=[("YTD",D("9.23"),D("10.72"),D("-1.49")),("1Y",D("11.04"),D("13.17"),D("-2.13")),("3Y",D("17.52"),D("20.23"),D("-2.71")),("5Y",D("10.43"),D("11.77"),D("-1.34")),("10Y",D("13.67"),D("13.75"),D("-0.08")),("SI",D("11.68"),D("9.23"),D("2.45"))]
for n,f,c,e in cat: chk(f-c==e,f"excess vs category {n}")
chk(sum(1 for _,f,c,_ in cat if f-c<0)==5,"five of six windows negative vs category")
chk(sum(1 for _,f,c,_ in cat if f-c>0)==1,"only SI positive vs category")
# G4 cumulative conversions (annualized to cumulative)
chk(r2(((1+D("17.52")/100)**3-1)*100)==D("62.31"),"3Y cumulative fund +62.31")
chk(r2(((1+D("22.99")/100)**3-1)*100)==D("86.04"),"3Y cumulative benchmark +86.04")
chk(r2(((1+D("10.43")/100)**5-1)*100)==D("64.22"),"5Y cumulative fund +64.22")
chk(r2(((1+D("13.27")/100)**5-1)*100)==D("86.46"),"5Y cumulative benchmark +86.46")
chk(r2(((1+D("13.67")/100)**10-1)*100)==D("260.13"),"10Y cumulative fund +260.13")
chk(r2(((1+D("15.21")/100)**10-1)*100)==D("312.00"),"10Y cumulative benchmark +312.00")
# G5 $10,000 endpoints, 10Y
f10=r2(D(10000)*(1+D("13.67")/100)**10); b10=r2(D(10000)*(1+D("15.21")/100)**10); c10=r2(D(10000)*(1+D("13.75")/100)**10)
chk(f10==D("36012.94"),"10Y $10k fund 36012.94")
chk(b10==D("41200.43"),"10Y $10k benchmark 41200.43")
chk(c10==D("36267.20"),"10Y $10k category 36267.20")
chk(r2(f10/b10)==D("0.87"),"10Y fund endpoint about 0.87x benchmark")
chk(b10-f10==D("5187.49"),"10Y endpoint gap 5187.49")
chk(c10-f10==D("254.26"),"10Y endpoint also below category by 254.26")
# G6 $10,000 endpoints, since class inception (20.42 years, fractional power)
yrs=D(cls)/D("365.25")
fsi=r2(D(10000)*(1+D("11.68")/100)**yrs); csi=r2(D(10000)*(1+D("9.23")/100)**yrs)
chk(fsi==D("95470.08"),"SI $10k fund about 95470.08")
chk(csi==D("60688.96"),"SI $10k category about 60688.96")
chk(r2(fsi/csi)==D("1.57"),"SI fund endpoint about 1.57x category")
# G7 segment -10Y..-5Y (annualized, implied)
def seg(hi,lo,yhi,ylo):
    return r2(((((1+D(hi)/100)**yhi)/((1+D(lo)/100)**ylo))**(D(1)/D(yhi-ylo))-1)*100)
chk(seg("13.67","10.43",10,5)==D("17.01"),"segment -10..-5 fund +17.01")
chk(seg("15.21","13.27",10,5)==D("17.18"),"segment -10..-5 benchmark +17.18")
chk(seg("13.75","11.77",10,5)==D("15.77"),"segment -10..-5 category +15.77")
# G8 segment -5Y..-3Y (annualized, implied): nearly flat for all three
chk(seg("10.43","17.52",5,3)==D("0.59"),"segment -5..-3 fund +0.59")
chk(seg("13.27","22.99",5,3)==D("0.11"),"segment -5..-3 benchmark +0.11")
chk(seg("11.77","20.23",5,3)==D("0.18"),"segment -5..-3 category +0.18")
# G9 Q4-2025 implied (1Y window minus YTD)
chk(r2(((1+D("11.04")/100)/(1+D("9.23")/100)-1)*100)==D("1.66"),"Q4-2025 implied fund +1.66")
chk(r2(((1+D("15.59")/100)/(1+D("12.90")/100)-1)*100)==D("2.38"),"Q4-2025 implied benchmark +2.38")
chk(r2(((1+D("13.17")/100)/(1+D("10.72")/100)-1)*100)==D("2.21"),"Q4-2025 implied category +2.21")
# G10 composition and style box sum to 100
chk(D("96.5")+D("3.0")+D("0.5")==D("100.0"),"composition US 96.5 + non-US 3.0 + cash 0.5 = 100")
chk(D("43.24")+D("32.05")+D("24.71")+D("0.00")+D("0.00")==D("100.00"),"style box sums to 100.00")
chk(D("43.24")+D("32.05")==D("75.29"),"giant + large = 75.29")
# G11 sectors: three super-sectors reconcile; three sectors at zero vs S&P
chk(D("5.42")+D("14.33")+D("9.53")+D("0.00")==D("29.28"),"cyclical 29.28")
chk(D("7.61")+D("0.00")+D("16.32")+D("33.33")==D("57.26"),"sensitive 57.26")
chk(D("1.99")+D("11.48")+D("0.00")==D("13.47"),"defensive 13.47")
chk(D("29.28")+D("57.26")+D("13.47")==D("100.01"),"sector total 100.01 (rounding)")
chk(D("33.33")-D("40.45")==D("-7.12"),"technology -7.12 vs S&P 500")
chk(D("16.32")-D("7.54")==D("8.78"),"industrials +8.78 vs S&P 500")
chk(D("3.40")+D("1.70")+D("1.88")==D("6.98"),"S&P weight of the three zero sectors 6.98")
# G12 top-10 holdings
top=[D(x) for x in ["7.19","6.73","5.93","5.21","4.40","3.33","3.26","3.17","3.01","2.97"]]
chk(sum(top)==D("45.20"),"top10 sum 45.20")
chk(max(top)==D("7.19"),"largest holding 7.19 (Microsoft)")
chk(top[0]+top[1]==D("13.92"),"top two sum 13.92")
print("ALL",ok,"ASSERTIONS PASSED")
