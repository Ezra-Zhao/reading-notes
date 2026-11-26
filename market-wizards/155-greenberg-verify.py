#!/usr/bin/env python3
"""155 Greenberg / Baron Small Cap Fund (BSFIX) 验算脚本
数据源：Baron 官方产品页 BSFIX（2026-09-30 业绩/特征，持仓 2026-10-31）、
2026Q3 股东信（15 年窗、Cliff Greenberg 署名）、产品页分红栏日历年回报。
全部为四则运算/连乘反推（证据 C），断言失败即退出非零。
"""
from datetime import date
fails=[]
def chk(name,cond):
    print(("PASS" if cond else "FAIL"),name)
    if not cond: fails.append(name)
def approx(a,b,tol=0.15): return abs(a-b)<=tol
fund=dict(qtd=-7.69,ytd=-4.30,y1=-5.79,y3=6.75,y5=-0.17,y10=9.59,y15=11.07,si=9.46)
bench=dict(qtd=-9.39,ytd=10.71,y1=12.05,y3=17.55,y5=4.72,y10=9.90,y15=11.94,si=6.86)  # Russell 2000 Growth
r3=dict(qtd=1.40,ytd=12.42,y1=15.13,y3=22.26,y5=12.64,y10=14.73,y15=15.27,si=9.35)      # Russell 3000
# 1 基金生命：1997-09-30 至 2026-09-30 整 29 年
days=(date(2026,9,30)-date(1997,9,30)).days
chk("1 life days 10592",days==10592)
chk("1 life years 29.00",approx(days/365.25,29.00,0.01))
# 2 对主基准八窗超额：只赢 QTD 与自成立
ex={k:round(fund[k]-bench[k],2) for k in fund}
for k,v in dict(qtd=1.70,ytd=-15.01,y1=-17.84,y3=-10.80,y5=-4.89,y10=-0.31,y15=-0.87,si=2.60).items():
    chk(f"2 excess vs R2000G {k} {v}",ex[k]==v)
chk("2 wins only qtd+si vs bench",sum(1 for v in ex.values() if v>0)==2)
# 3 对 Russell 3000 八窗超额：只赢自成立 +0.11
ex3={k:round(fund[k]-r3[k],2) for k in fund}
for k,v in dict(qtd=-9.09,ytd=-16.72,y1=-20.92,y3=-15.51,y5=-12.81,y10=-5.14,y15=-4.20,si=0.11).items():
    chk(f"3 excess vs R3000 {k} {v}",ex3[k]==v)
chk("3 wins only si vs R3000",sum(1 for v in ex3.values() if v>0)==1)
# 4 2026 劈段：上半年基金 +3.67（与股东信自述一致）、尺子 +22.18
h1f=(1+fund['ytd']/100)/(1+fund['qtd']/100)-1
h1b=(1+bench['ytd']/100)/(1+bench['qtd']/100)-1
chk("4 H1 2026 fund +3.67",approx(h1f*100,3.67,0.02))
chk("4 H1 2026 bench +22.18",approx(h1b*100,22.18,0.02))
# 5 分段十至五年前
def seg(long,short,nl,ns): return (((1+long/100)**nl/(1+short/100)**ns)**(1/(nl-ns))-1)*100
chk("5 seg 10-5 fund +20.30",approx(seg(fund['y10'],fund['y5'],10,5),20.30,0.05))
chk("5 seg 10-5 bench +15.34",approx(seg(bench['y10'],bench['y5'],10,5),15.34,0.05))
# 6 分段五至三年前（坑段，基金跌得比尺子少）
chk("6 seg 5-3 fund -9.72",approx(seg(fund['y5'],fund['y3'],5,3),-9.72,0.05))
chk("6 seg 5-3 bench -11.95",approx(seg(bench['y5'],bench['y3'],5,3),-11.95,0.05))
# 7 分段三至一年前
chk("7 seg 3-1 fund +13.63",approx(seg(fund['y3'],fund['y1'],3,1),13.63,0.05))
chk("7 seg 3-1 bench +20.40",approx(seg(bench['y3'],bench['y1'],3,1),20.40,0.05))
# 8 一万美元终点
chk("8 10k 5y ~9915",approx(10000*(1+fund['y5']/100)**5,9915,5))
chk("8 10k 10y ~24987",approx(10000*(1+fund['y10']/100)**10,24987,15))
chk("8 10k si ~137533",approx(10000*(1+fund['si']/100)**29,137533,400))
chk("8 10k bench si ~68492",approx(10000*(1+bench['si']/100)**29,68492,300))
chk("8 si ratio ~2.01x",approx((1.0946**29)/(1.0686**29),2.01,0.02))
# 9 日历年：2022 大跌回本线与三年爬回原点下
cal=[-31.05,27.19,13.61,-0.66]; p=1.0
for v in cal: p*=1+v/100
chk("9 2022 recovery need +45.03",approx((1/0.6895-1)*100,45.03,0.02))
chk("9 thru 2024 ~0.9963 of origin",approx(0.6895*1.2719*1.1361,0.9963,0.001))
chk("9 thru 2025 ~0.9898 of origin",approx(p,0.9898,0.001))
# 10 前十大逐名合计 36.7 vs 印刷 36.6（差 0.1 舍入只登记）；第一大 Vertiv 5.5 占前十大 ~15.0%
top=[5.5,4.7,4.1,4.0,3.3,3.3,3.0,3.0,2.9,2.9]
chk("10 top10 named sum 36.7",approx(sum(top),36.7,0.01))
chk("10 vertiv share of top10 ~15.0%",approx(5.5/sum(top)*100,15.0,0.1))
# 11 三季度前五正贡献合计 +2.64
chk("11 contrib top5 sum +2.64",approx(0.67+0.57+0.48+0.47+0.45,2.64,0.01))
# 12 行业分布合计 100.0；五年捕获：上行 82.15 / 下行 96.70（只登记官方值自洽）
sectors=[30.3,22.4,13.9,13.8,7.8,7.0,1.7,1.2,1.1,0.8]
chk("12 sectors sum 100.0",approx(sum(sectors),100.0,0.01))
chk("12 5y downside<100 & upside<100 (defensive shape)",96.70<100 and 82.15<100)
print("TOTAL FAILS:",len(fails))
raise SystemExit(1 if fails else 0)
