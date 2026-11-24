#!/usr/bin/env python3
"""127 陆彬 (汇丰晋信低碳先锋股票 540008) verification.
Source: 汇丰晋信低碳先锋股票型证券投资基金 2026 年第 3 季度报告
(报告期末 2026-09-30, 送出 2026-10-27, 巨潮资讯原文 PDF):
§2 合同生效 2010-06-08, §3.1 财务指标, §3.2.1 A 类八窗净值表现,
§4.1 陆彬 2019-08-17 起任未离任/证券从业 11.5 年, §5.1-5.3 组合与前十大,
§6 份额变动, §7 管理人固有资金无持有无交易.
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
# G1 life / tenure
life=(date(2026,9,30)-date(2010,6,8)).days
chk(life==5958,"fund life 5958 days")
chk(r2(D(life)/D("365.25"))==D("16.31"),"fund life approx 16.31 years")
ten=(date(2026,9,30)-date(2019,8,17)).days
chk(ten==2601,"Lu Bin tenure 2601 days")
chk(r2(D(ten)/D("365.25"))==D("7.12"),"tenure approx 7.12 years")
chk(r2(D(ten)/D(life)*100)==D("43.66"),"tenure 43.66 pct of fund life")
pre=(date(2019,8,17)-date(2010,6,8)).days
chk(pre==3357,"pre-tenure 3357 days")
chk(pre+ten==life,"pre + tenure = life")
# G2 A-class windows vs benchmark (printed excess check)
wins=[("3M",D("-15.55"),D("-18.06"),D("2.51")),("6M",D("-26.69"),D("-18.13"),D("-8.56")),
("1Y",D("-32.11"),D("-16.29"),D("-15.82")),("3Y",D("-25.07"),D("-3.00"),D("-22.07")),
("5Y",D("-53.81"),D("-39.96"),D("-13.85")),("7Y",D("81.88"),D("29.85"),D("52.03")),
("10Y",D("20.51"),D("-10.50"),D("31.01")),("SI",D("117.90"),D("12.69"),D("105.21"))]
for n,f,b,e in wins: chk(f-b==e,f"A excess {n}")
# G3 win/loss count
chk(sum(1 for _,f,b,_ in wins if f-b>0)==4,"four windows positive excess")
chk(sum(1 for _,f,b,_ in wins if f-b<0)==4,"four windows negative excess")
chk(max(e for *_,e in wins)==D("105.21"),"largest excess SI +105.21")
chk(min(e for *_,e in wins)==D("-22.07"),"worst excess 3Y -22.07")
# G4 implied Q2 2026 (6M split by 3M)
q2f=(1+D("-26.69")/100)/(1+D("-15.55")/100)-1
chk(r2(q2f*100)==D("-13.19"),"implied Q2 fund -13.19")
q2b=(1+D("-18.13")/100)/(1+D("-18.06")/100)-1
chk(r2(q2b*100)==D("-0.09"),"implied Q2 benchmark -0.09")
chk(r2((q2f-q2b)*100)==D("-13.11"),"implied Q2 excess approx -13.11 pp")
# G5 segment inside 7Y: first two years (2019-10-01 to 2021-09-30) = 7Y / 5Y
s1f=(1+D("81.88")/100)/(1+D("-53.81")/100)-1
chk(r2(s1f*100)==D("293.76"),"7Y-minus-5Y segment fund +293.76")
s1b=(1+D("29.85")/100)/(1+D("-39.96")/100)-1
chk(r2(s1b*100)==D("116.27"),"7Y-minus-5Y segment benchmark +116.27")
# G6 segment 10Y minus 7Y (2016-10-01 to 2019-09-30, pre-tenure mostly)
s2f=(1+D("20.51")/100)/(1+D("81.88")/100)-1
chk(r2(s2f*100)==D("-33.74"),"10Y-minus-7Y segment fund -33.74")
s2b=(1+D("-10.50")/100)/(1+D("29.85")/100)-1
chk(r2(s2b*100)==D("-31.07"),"10Y-minus-7Y segment benchmark -31.07")
# G7 segment 5Y minus 3Y (2021-10-01 to 2023-09-30) and prior 9M of 1Y
s3f=(1+D("-53.81")/100)/(1+D("-25.07")/100)-1
chk(r2(s3f*100)==D("-38.36"),"5Y-minus-3Y segment fund -38.36")
s3b=(1+D("-39.96")/100)/(1+D("-3.00")/100)-1
chk(r2(s3b*100)==D("-38.10"),"5Y-minus-3Y segment benchmark -38.10")
p9f=(1+D("-32.11")/100)/(1+D("-15.55")/100)-1
chk(r2(p9f*100)==D("-19.61"),"prior 9M of 1Y fund -19.61")
p9b=(1+D("-16.29")/100)/(1+D("-18.06")/100)-1
chk(r2(p9b*100)==D("2.16"),"prior 9M of 1Y benchmark +2.16")
# G8 profit split A+C (yuan)
real=D("-74793097.26")+D("-8361465.33")
prof=D("-308877408.02")+D("-33008495.01")
chk(real==D("-83154562.59"),"A+C realized -83,154,562.59")
chk(prof==D("-341885903.03"),"A+C profit -341,885,903.03")
unreal=prof-real
chk(unreal==D("-258731340.44"),"unrealized -258,731,340.44")
chk(r2(unreal/real)==D("3.11"),"unrealized approx 3.11x realized loss")
chk(r2(-prof/D("1838631568.44")*100)==D("18.59"),"quarter loss approx 18.59 pct of ending NAV")
# G9 NAV arithmetic
navA=D("1671826596.89"); navC=D("166804971.55")
tot=navA+navC
chk(tot==D("1838631568.44"),"total ending NAV 1,838,631,568.44")
chk(r2(navA/D("836450439.94"))==D("2.00"),"A unit NAV rounds 2.00 (printed 1.9987)")
chk(abs(navA/D("836450439.94")-D("1.9987"))<D("0.0001"),"A unit NAV matches printed 1.9987")
chk(abs(navC/D("85561118.43")-D("1.9495"))<D("0.0001"),"C unit NAV matches printed 1.9495")
chk(r2(D("1724932929.46")/tot*100)==D("93.82"),"equity 93.82 pct of NAV (printed industry total)")
chk(r2(D("1724932929.46")/D("1843863588.55")*100)==D("93.55"),"equity 93.55 pct of total assets")
# G10 holdings shape
top10=[D("9.36"),D("9.28"),D("9.17"),D("9.13"),D("9.09"),D("8.94"),D("8.63"),D("6.85"),D("6.54"),D("6.16")]
chk(sum(top10)==D("83.15"),"top10 sum 83.15 pct of NAV")
chk(r2(D("1704594059.06")/D("1724932929.46")*100)==D("98.82"),"manufacturing 98.82 pct of equity")
chk(r2(top10[0]/sum(top10)*100)==D("11.26"),"top1 approx 11.26 pct of top10")
# G11 share changes
a0,a1=D("852509288.58"),D("836450439.94")
c0,c1=D("99212023.17"),D("85561118.43")
chk(r2((a1-a0)/a0*100)==D("-1.88"),"A shares net -1.88 pct")
chk(r2((c1-c0)/c0*100)==D("-13.76"),"C shares net -13.76 pct")
chk(r2(((a1+c1)-(a0+c0))/(a0+c0)*100)==D("-3.12"),"total shares net -3.12 pct")
chk(a1+c1==D("922011558.37"),"ending total shares match §2")
# G12 recovery prices
chk(r2((1/(1+D("-53.81")/100)-1)*100)==D("116.50"),"5Y recovery needs +116.50")
chk(r2((1/(1+D("-32.11")/100)-1)*100)==D("47.30"),"1Y recovery needs +47.30")
chk(r2((1/(1+D("-15.55")/100)-1)*100)==D("18.41"),"Q3 recovery needs +18.41")
print("TOTAL", ok, "assertions passed")
