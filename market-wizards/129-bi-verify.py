#!/usr/bin/env python3
"""129 毕天宇 (富国天博创新主题混合 519035) verification.
Source: 富国天博创新主题混合型证券投资基金 2026 年第 3 季度报告
(上交所披露原文 PDF, 报告期末 2026-09-30, 送出 2026-10-27):
§2 合同生效 2007-04-27, §3.1 财务指标, §3.2.1 八窗净值表现,
§4.1 毕天宇 2007-04-27 起任未离任/证券从业 26 年/注1首任任职日为合同生效日,
§5.1-5.3 组合与前十大, §6 份额变动, §7 管理人固有资金无持有无交易.
All derived figures recomputed with Decimal / datetime.
"""
from decimal import Decimal as D
from datetime import date
ok=0
def chk(c,l):
    global ok
    assert c,l
    ok+=1; print("PASS",l)
def r2(x): return x.quantize(D("0.01"))
# G1 life / tenure: first manager, start = inception
life=(date(2026,9,30)-date(2007,4,27)).days
chk(life==7096,"fund life 7096 days")
chk(r2(D(life)/D("365.25"))==D("19.43"),"fund life approx 19.43 years")
ten=(date(2026,9,30)-date(2007,4,27)).days
chk(ten==life,"Bi Tianyu tenure = full fund life 7096 days")
chk(r2(D(ten)/D(life)*100)==D("100.00"),"tenure 100.00 pct of fund life")
# G2 eight windows vs benchmark (printed excess check)
wins=[("3M",D("-19.98"),D("-9.97"),D("-10.01")),("6M",D("6.58"),D("-1.33"),D("7.91")),
("1Y",D("8.25"),D("-4.45"),D("12.70")),("3Y",D("23.49"),D("16.16"),D("7.33")),
("5Y",D("-3.12"),D("-6.12"),D("3.00")),("7Y",D("91.88"),D("15.26"),D("76.62")),
("10Y",D("147.32"),D("31.95"),D("115.37")),("SI",D("361.50"),D("45.00"),D("316.50"))]
for n,f,b,e in wins: chk(f-b==e,f"excess {n}")
# G3 win/loss count
chk(sum(1 for _,f,b,_ in wins if f-b>0)==7,"seven windows positive excess")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==1,"one window negative excess")
chk(min(e for *_,e in wins)==D("-10.01"),"worst excess 3M -10.01")
chk(max(e for *_,e in wins)==D("316.50"),"largest excess SI +316.50")
# G4 implied Q2 2026 (6M split by 3M)
q2f=(1+D("6.58")/100)/(1+D("-19.98")/100)-1
chk(r2(q2f*100)==D("33.19"),"implied Q2 fund +33.19")
q2b=(1+D("-1.33")/100)/(1+D("-9.97")/100)-1
chk(r2(q2b*100)==D("9.60"),"implied Q2 benchmark +9.60")
chk(r2((q2f-q2b)*100)==D("23.59"),"implied Q2 excess approx +23.59 pp")
# G5 prior nine months of 1Y window
p9f=(1+D("8.25")/100)/(1+D("-19.98")/100)-1
chk(r2(p9f*100)==D("35.28"),"prior 9M of 1Y fund +35.28")
p9b=(1+D("-4.45")/100)/(1+D("-9.97")/100)-1
chk(r2(p9b*100)==D("6.13"),"prior 9M of 1Y benchmark +6.13")
# G6 segment 7Y minus 5Y (2019-10-01 to 2021-09-30)
s1f=(1+D("91.88")/100)/(1+D("-3.12")/100)-1
chk(r2(s1f*100)==D("98.06"),"7Y-minus-5Y segment fund +98.06")
s1b=(1+D("15.26")/100)/(1+D("-6.12")/100)-1
chk(r2(s1b*100)==D("22.77"),"7Y-minus-5Y segment benchmark +22.77")
# G7 segments 10Y-7Y and SI-10Y
s2f=(1+D("147.32")/100)/(1+D("91.88")/100)-1
chk(r2(s2f*100)==D("28.89"),"10Y-minus-7Y segment fund +28.89")
s2b=(1+D("31.95")/100)/(1+D("15.26")/100)-1
chk(r2(s2b*100)==D("14.48"),"10Y-minus-7Y segment benchmark +14.48")
s3f=(1+D("361.50")/100)/(1+D("147.32")/100)-1
chk(r2(s3f*100)==D("86.60"),"SI-minus-10Y segment fund +86.60")
s3b=(1+D("45.00")/100)/(1+D("31.95")/100)-1
chk(r2(s3b*100)==D("9.89"),"SI-minus-10Y segment benchmark +9.89")
# G8 segment 5Y-3Y and 3Y-1Y
s4f=(1+D("-3.12")/100)/(1+D("23.49")/100)-1
chk(r2(s4f*100)==D("-21.55"),"5Y-minus-3Y segment fund -21.55")
s4b=(1+D("-6.12")/100)/(1+D("16.16")/100)-1
chk(r2(s4b*100)==D("-19.18"),"5Y-minus-3Y segment benchmark -19.18")
s5f=(1+D("23.49")/100)/(1+D("8.25")/100)-1
chk(r2(s5f*100)==D("14.08"),"3Y-minus-1Y segment fund +14.08")
s5b=(1+D("16.16")/100)/(1+D("-4.45")/100)-1
chk(r2(s5b*100)==D("21.57"),"3Y-minus-1Y segment benchmark +21.57")
# G9 profit split (yuan, single class)
real=D("89253242.88"); prof=D("-367637778.22")
unreal=prof-real
chk(unreal==D("-456891021.10"),"unrealized -456,891,021.10")
chk(r2(-unreal/real)==D("5.12"),"unrealized loss approx 5.12x realized gain")
chk(r2(-prof/D("1467733887.45")*100)==D("25.05"),"quarter loss approx 25.05 pct of ending NAV")
# G10 NAV arithmetic
chk(D("648281471.27")+D("17544757.20")-D("28035436.08")==D("637790792.39"),"share flow reconciles to ending shares")
prod=D("637790792.39")*D("2.3013")
chk(abs(prod-D("1467733887.45"))<D("20000"),"shares x unit NAV within rounding of ending NAV")
chk(r2((D("637790792.39")-D("648281471.27"))/D("648281471.27")*100)==D("-1.62"),"total shares net -1.62 pct")
# G11 holdings shape
top10=[D("8.35"),D("7.67"),D("7.02"),D("6.44"),D("5.48"),D("4.19"),D("4.11"),D("3.45"),D("3.39"),D("3.36")]
chk(sum(top10)==D("53.46"),"top10 sum 53.46 pct of NAV")
chk(r2(D("1153905715.64")/D("1343861755.68")*100)==D("85.86"),"manufacturing 85.86 pct of equity")
chk(r2(D("1343861755.68")/D("1467733887.45")*100)==D("91.56"),"equity 91.56 pct of NAV")
chk(r2(D("125297369.07")/D("1470920651.23")*100)==D("8.52"),"cash 8.52 pct of total assets")
# G12 recovery prices and SI factor
chk(r2((1/(1+D("-19.98")/100)-1)*100)==D("24.97"),"Q3 recovery needs +24.97")
chk(r2((1/(1+D("-3.12")/100)-1)*100)==D("3.22"),"5Y recovery needs +3.22")
chk(1+D("361.50")/100==D("4.6150"),"SI factor 4.6150")
print("TOTAL", ok, "assertions passed")
