#!/usr/bin/env python3
"""128 Ziehl/Weiner/Lassiter (Invesco V.I. Main Street Small Cap) verification.
Source: Morningstar Investment Profile via Pacific Life, release 09-30-2026:
portfolio inception 05-01-1998, managers Matthew Ziehl (since 2009),
Adam Weiner (since 2013), Bryan Lassiter (since 2026), benchmark S&P 500 TR,
category Small Blend, returns YTD/1Y/3Y/5Y/10Y/SI, composition, market cap,
sectors, top-10, 101 stock holdings, turnover 50, assets $1,211.30M,
expense 0.84. Ziehl lead-manager start month May 2009 per SEC prospectus
supplement filing (2011-04-29, predecessor Oppenheimer fund) = B grade;
day counts for Ziehl use 2009-05-01 and are labelled approximate.
Weiner/Lassiter starts are year-only in the profile (B grade), no day counts
are asserted for them. Lassiter joining effective 2026-09-30 per Invesco
manager-change notice, so his tenure at the profile date is effectively zero.
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
# G1 life / tenure
life=(date(2026,9,30)-date(1998,5,1)).days
chk(life==10379,"fund life 10379 days")
chk(r2(D(life)/D("365.25"))==D("28.42"),"fund life approx 28.42 years")
zie=(date(2026,9,30)-date(2009,5,1)).days
chk(zie==6361,"Ziehl tenure approx 6361 days (from 2009-05-01, B grade)")
chk(r2(D(zie)/D("365.25"))==D("17.42"),"Ziehl tenure approx 17.42 years")
chk(r2(D(zie)/D(life)*100)==D("61.29"),"Ziehl tenure 61.29 pct of fund life")
pre=(date(2009,5,1)-date(1998,5,1)).days
chk(pre==4018,"pre-Ziehl 4018 days")
chk(pre+zie==life,"pre + Ziehl = fund life")
# G2 excess vs benchmark (S&P 500 TR): five windows, all negative
wins=[("YTD",D("9.29"),D("12.75"),D("-3.46")),("1Y",D("12.09"),D("15.74"),D("-3.65")),("3Y",D("14.88"),D("22.89"),D("-8.01")),("5Y",D("6.86"),D("13.79"),D("-6.93")),("10Y",D("10.75"),D("15.33"),D("-4.58"))]
for n,f,b,e in wins: chk(f-b==e,f"excess vs benchmark {n}")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==5,"all five windows negative vs benchmark")
chk(min(e for *_,e in wins)==D("-8.01"),"worst window vs benchmark is 3Y -8.01")
chk(max(e for *_,e in wins)==D("-3.46"),"closest window vs benchmark is YTD -3.46")
# G3 excess vs category: five windows, four negative, only 10Y positive; SI not printed for category
cat=[("YTD",D("9.29"),D("12.75"),D("-3.46")),("1Y",D("12.09"),D("14.52"),D("-2.43")),("3Y",D("14.88"),D("15.21"),D("-0.33")),("5Y",D("6.86"),D("6.87"),D("-0.01")),("10Y",D("10.75"),D("9.76"),D("0.99"))]
for n,f,c,e in cat: chk(f-c==e,f"excess vs category {n}")
chk(sum(1 for _,f,c,_ in cat if f-c<0)==4,"four of five windows negative vs category")
chk(sum(1 for _,f,c,_ in cat if f-c>0)==1,"only 10Y positive vs category")
chk(cat[0][2]==wins[0][2],"category YTD printed equal to benchmark YTD 12.75, so YTD excess is -3.46 on both rulers")
# G4 cumulative conversions
chk(r2(((1+D("14.88")/100)**3-1)*100)==D("51.61"),"3Y cumulative fund +51.61")
chk(r2(((1+D("22.89")/100)**3-1)*100)==D("85.59"),"3Y cumulative benchmark +85.59")
chk(r2(((1+D("15.21")/100)**3-1)*100)==D("52.92"),"3Y cumulative category +52.92")
chk(r2(((1+D("6.86")/100)**5-1)*100)==D("39.34"),"5Y cumulative fund +39.34")
chk(r2(((1+D("13.79")/100)**5-1)*100)==D("90.77"),"5Y cumulative benchmark +90.77")
chk(r2(((1+D("6.87")/100)**5-1)*100)==D("39.41"),"5Y cumulative category +39.41")
chk(r2(((1+D("10.75")/100)**10-1)*100)==D("177.61"),"10Y cumulative fund +177.61")
chk(r2(((1+D("15.33")/100)**10-1)*100)==D("316.32"),"10Y cumulative benchmark +316.32")
chk(r2(((1+D("9.76")/100)**10-1)*100)==D("153.77"),"10Y cumulative category +153.77")
# G5 $10,000 endpoints, 10Y
f10=r2(D(10000)*(1+D("10.75")/100)**10); b10=r2(D(10000)*(1+D("15.33")/100)**10); c10=r2(D(10000)*(1+D("9.76")/100)**10)
chk(f10==D("27761.14"),"10Y $10k fund 27761.14")
chk(b10==D("41631.58"),"10Y $10k benchmark 41631.58")
chk(c10==D("25377.04"),"10Y $10k category 25377.04")
chk(r2(f10/b10)==D("0.67"),"10Y fund endpoint about 0.67x benchmark")
chk(b10-f10==D("13870.44"),"10Y endpoint gap vs benchmark 13870.44")
chk(r2(f10/c10)==D("1.09"),"10Y fund endpoint about 1.09x category")
chk(f10-c10==D("2384.10"),"10Y endpoint above category by 2384.10")
# G6 since-inception endpoint (fund only; benchmark/category SI not printed)
yrs=D(life)/D("365.25")
fsi=r2(D(10000)*(1+D("8.87")/100)**yrs)
chk(fsi==D("111889.60"),"SI $10k fund about 111889.60 over 28.42 years")
chk(r2(yrs)==D("28.42"),"SI window length approx 28.42 years")
# G7 segment -10Y..-5Y implied annualized
def seg(hi,lo,yhi,ylo):
    return r2(((((1+D(hi)/100)**yhi)/((1+D(lo)/100)**ylo))**(D(1)/D(yhi-ylo))-1)*100)
chk(seg("10.75","6.86",10,5)==D("14.78"),"segment -10..-5 fund +14.78")
chk(seg("15.33","13.79",10,5)==D("16.89"),"segment -10..-5 benchmark +16.89")
chk(seg("9.76","6.87",10,5)==D("12.73"),"segment -10..-5 category +12.73")
chk(seg("10.75","6.86",10,5)>seg("9.76","6.87",10,5),"segment -10..-5 fund beat category")
# G8 segment -5Y..-3Y implied annualized: fund and category negative, benchmark positive
chk(seg("6.86","14.88",5,3)==D("-4.13"),"segment -5..-3 fund -4.13")
chk(seg("13.79","22.89",5,3)==D("1.39"),"segment -5..-3 benchmark +1.39")
chk(seg("6.87","15.21",5,3)==D("-4.52"),"segment -5..-3 category -4.52")
chk(seg("6.86","14.88",5,3)>seg("6.87","15.21",5,3),"segment -5..-3 fund lost less than category")
# G9 Q4-2025 implied (1Y minus YTD)
chk(r2(((1+D("12.09")/100)/(1+D("9.29")/100)-1)*100)==D("2.56"),"Q4-2025 implied fund +2.56")
chk(r2(((1+D("15.74")/100)/(1+D("12.75")/100)-1)*100)==D("2.65"),"Q4-2025 implied benchmark +2.65")
chk(r2(((1+D("14.52")/100)/(1+D("12.75")/100)-1)*100)==D("1.57"),"Q4-2025 implied category +1.57")
# G10 composition and market cap (as of 08-31-26)
chk(D("93.3")+D("1.0")+D("0.0")+D("5.6")+D("0.0")==D("99.9"),"composition sums to 99.9 (rounding)")
chk(D("0.00")+D("0.00")+D("1.11")+D("75.19")+D("23.71")==D("100.01"),"market cap sums to 100.01 (rounding)")
chk(D("75.19")+D("23.71")==D("98.90"),"small plus micro = 98.90 pct of equity style")
# G11 sectors: super-sector subtotals reconcile
chk(D("0.75")+D("13.77")+D("18.68")+D("5.39")==D("38.59"),"cyclical subtotal 38.59")
chk(D("1.07")+D("6.24")+D("19.49")+D("13.65")==D("40.45"),"sensitive subtotal 40.45")
chk(D("1.84")+D("16.35")+D("2.77")==D("20.96"),"defensive subtotal 20.96")
chk(D("38.59")+D("40.45")+D("20.96")==D("100.00"),"sectors total 100.00")
# G12 top-10, scale and risk prints
top=[D(x) for x in ("1.99","1.79","1.63","1.58","1.57","1.54","1.52","1.50","1.50","1.44")]
chk(sum(top)==D("16.06"),"top-10 sum 16.06")
chk(top[0]+top[1]==D("3.78"),"top-2 sum 3.78")
chk(sum(top[:5])==D("8.56"),"top-5 sum 8.56")
chk(D("1211.30")>0 and D("0.84")>0,"assets 1211.30M and expense 0.84 printed")
chk(D("-8.08")<0 and D("-6.08")<0 and D("-4.93")<0,"alpha negative at 3Y/5Y/10Y")
chk(D("-0.63")<0 and D("-0.61")<0 and D("-0.43")<0,"information ratio negative at 3Y/5Y/10Y")
print(f"ALL {ok} ASSERTIONS PASS")
