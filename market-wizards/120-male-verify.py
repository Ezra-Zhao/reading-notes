#!/usr/bin/env python3
"""120 Bob Male (Buffalo Small Cap Growth Fund, BUFSX) verification.
Source: Buffalo Small Cap Growth Fund Fact Sheet, September 30, 2026
(Buffalo Funds official PDF). Fund inception 1998-04-14.
Bob Male, CFA: Manager since Inception. Craig Richard, CFA: Manager since 2023.
Benchmark: Russell 2000 Growth Index. Investor Class BUFSX used throughout.
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
# G1 life / tenure (Male since inception, so tenure = life)
life=(date(2026,9,30)-date(1998,4,14)).days
chk(life==10396,"life 10396 days")
chk(r2(D(life)/D("365.25"))==D("28.46"),"life approx 28.46 years")
chk(life>10000,"life over ten thousand days")
# G2 printed excess, nine windows (annualized except 3M/YTD/1Y)
wins=[("3M",D("-7.58"),D("-9.39"),D("1.81")),("YTD",D("11.64"),D("10.71"),D("0.93")),("1Y",D("11.94"),D("12.05"),D("-0.11")),("3Y",D("8.19"),D("17.55"),D("-9.36")),("5Y",D("-3.46"),D("4.72"),D("-8.18")),("10Y",D("9.80"),D("9.90"),D("-0.10")),("15Y",D("11.23"),D("11.94"),D("-0.71")),("20Y",D("8.18"),D("9.09"),D("-0.91")),("SI",D("10.56"),D("6.87"),D("3.69"))]
for n,f,b,e in wins: chk(f-b==e,f"excess {n}")
chk(sum(1 for _,f,b,_ in wins if f-b>0)==3,"only 3M/YTD/SI windows positive excess")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==6,"six windows negative excess")
# G3 YTD split: H1 implied
h1f=r2(((1+D("11.64")/100)/(1+D("-7.58")/100)-1)*100); h1b=r2(((1+D("10.71")/100)/(1+D("-9.39")/100)-1)*100)
chk(h1f==D("20.80"),"H1 fund implied +20.80")
chk(h1b==D("22.18"),"H1 bench implied +22.18")
chk(r2(h1f-h1b)==D("-1.38"),"H1 excess about -1.38")
# G4 one-year split: prior 9M implied
p9f=r2(((1+D("11.94")/100)/(1+D("-7.58")/100)-1)*100); p9b=r2(((1+D("12.05")/100)/(1+D("-9.39")/100)-1)*100)
chk(p9f==D("21.12"),"prior 9M fund +21.12")
chk(p9b==D("23.66"),"prior 9M bench +23.66")
# G5 recovery after Q3 drop
chk(r2(((1/(1+D("-7.58")/100))-1)*100)==D("8.20"),"recovery from Q3 needs +8.20")
chk(r2(((1/(1+D("-9.39")/100))-1)*100)==D("10.36"),"bench recovery needs +10.36")
# G6 cumulative from annualized
chk(r2(((1+D("8.19")/100)**3-1)*100)==D("26.64"),"3Y fund cumulative +26.64")
chk(r2(((1+D("17.55")/100)**3-1)*100)==D("62.43"),"3Y bench cumulative +62.43")
chk(r2(((1+D("-3.46")/100)**5-1)*100)==D("-16.14"),"5Y fund cumulative -16.14")
chk(r2(((1+D("4.72")/100)**5-1)*100)==D("25.94"),"5Y bench cumulative +25.94")
chk(r2(((1+D("9.80")/100)**10-1)*100)==D("154.70"),"10Y fund cumulative +154.70")
chk(r2(((1+D("9.90")/100)**10-1)*100)==D("157.03"),"10Y bench cumulative +157.03")
# G7 segment -10Y..-5Y implied cumulative (the old winning segment)
sf=((1+D("9.80")/100)**10)/((1+D("-3.46")/100)**5); sb=((1+D("9.90")/100)**10)/((1+D("4.72")/100)**5)
chk(r2((sf-1)*100)==D("203.73"),"segment -10Y..-5Y fund +203.73")
chk(r2((sb-1)*100)==D("104.09"),"segment -10Y..-5Y bench +104.09")
# G8 segment -5Y..-3Y implied cumulative
sf2=((1+D("-3.46")/100)**5)/((1+D("8.19")/100)**3); sb2=((1+D("4.72")/100)**5)/((1+D("17.55")/100)**3)
chk(r2((sf2-1)*100)==D("-33.78"),"segment -5Y..-3Y fund -33.78")
chk(r2((sb2-1)*100)==D("-22.47"),"segment -5Y..-3Y bench -22.47")
# G9 growth of $10,000 identity
chk(D("174277")/10000==D("17.4277"),"fund growth multiple 17.4277x")
chk(D("66730")/10000==D("6.6730"),"bench growth multiple 6.6730x")
chk(r2(D("174277")/D("66730"))==D("2.61"),"fund terminal about 2.61x bench terminal")
chk(r2(D("174277")-D("66730"))==D("107547.00"),"terminal gap 107547")
# G10 calendar years 2016-2025: five wins, five losses
cal=[(2016,D("6.22"),D("11.32")),(2017,D("27.07"),D("22.17")),(2018,D("-5.78"),D("-9.31")),(2019,D("40.97"),D("28.48")),(2020,D("66.36"),D("34.63")),(2021,D("4.85"),D("2.83")),(2022,D("-30.01"),D("-26.36")),(2023,D("5.45"),D("18.66")),(2024,D("5.38"),D("15.15")),(2025,D("-0.13"),D("13.01"))]
chk(sum(1 for _,f,b in cal if f>b)==5,"calendar wins 5")
chk(sum(1 for _,f,b in cal if f<b)==5,"calendar losses 5")
chk(all(f>b for _,f,b in cal if 2017<= _ <=2021) if False else sum(1 for y,f,b in cal if 2017<=y<=2021 and f>b)==5,"2017-2021 five straight calendar wins")
chk(sum(1 for y,f,b in cal if 2022<=y<=2025 and f<b)==4,"2022-2025 four straight calendar losses")
# G11 top-10 holdings (as of 2026-06-30 per fact-sheet footnote)
top=[D(x) for x in ["3.02","3.02","2.84","2.74","2.43","2.34","2.32","2.14","2.10","2.06"]]
chk(sum(top)==D("25.01"),"top10 sum 25.01 (printed total)")
chk(max(top)==D("3.02"),"largest holding only 3.02")
# G12 portfolio shape
chk(D("5.53")+D("27.99")+D("65.52")+D("0.96")==D("100.00"),"market-cap buckets sum 100.00")
chk(D("65.52")+D("27.99")+D("5.53")==D("99.04"),"mid+small+micro 99.04, mid alone 65.52")
chk(D("0.99")-D("0.87")==D("0.12"),"class expense gap 0.12")
print(f"ALL {ok} ASSERTIONS PASSED")
