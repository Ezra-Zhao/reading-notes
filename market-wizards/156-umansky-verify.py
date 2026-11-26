#!/usr/bin/env python3
"""156 Umansky / Baron Global Opportunity Fund (BGAIX, 原 Global Advantage) 验算脚本
数据源：Baron 官方 2026Q3 股东信（Alex Umansky 署名，业绩截至 2026-09-30）、
Baron 官网产品页（2026-09-30 组合特征）、官方事实表（经理栏、日历年回报）。
全部为四则运算/连乘反推（证据 C），断言失败即退出非零。
"""
from datetime import date
fails=[]
def chk(name,cond):
    print(("PASS" if cond else "FAIL"),name)
    if not cond: fails.append(name)
def approx(a,b,tol=0.15): return abs(a-b)<=tol
fund=dict(qtd=3.32,ytd=24.61,y1=32.74,y3=32.12,y5=3.36,y10=15.73,si=13.83)
acwi=dict(qtd=1.60,ytd=13.03,y1=16.75,y3=21.73,y5=11.57,y10=12.38,si=10.98)  # MSCI ACWI
grow=dict(qtd=-0.46,ytd=10.08,y1=13.20,y3=23.59,y5=11.24,y10=14.45,si=12.65)   # MSCI ACWI Growth
# 1 基金生命：2012-04-30 至 2026-09-30 共 5,266 天、约 14.42 年；Umansky 2012 年被任命、自成立任至今
days=(date(2026,9,30)-date(2012,4,30)).days
chk("1 life days 5266",days==5266)
chk("1 life years 14.42",approx(days/365.25,14.42,0.01))
# 2 对 MSCI ACWI 七窗超额：只输五年窗
ex={k:round(fund[k]-acwi[k],2) for k in fund}
for k,v in dict(qtd=1.72,ytd=11.58,y1=15.99,y3=10.39,y5=-8.21,y10=3.35,si=2.85).items():
    chk(f"2 excess vs ACWI {k} {v}",ex[k]==v)
chk("2 wins 6 of 7 vs ACWI, only 5y negative",sum(1 for v in ex.values() if v>0)==6 and ex['y5']<0)
# 3 对 MSCI ACWI Growth 七窗超额：同样只输五年窗
exg={k:round(fund[k]-grow[k],2) for k in fund}
for k,v in dict(qtd=3.78,ytd=14.53,y1=19.54,y3=8.53,y5=-7.88,y10=1.28,si=1.18).items():
    chk(f"3 excess vs Growth {k} {v}",exg[k]==v)
chk("3 wins 6 of 7 vs Growth, only 5y negative",sum(1 for v in exg.values() if v>0)==6 and exg['y5']<0)
# 4 2026 劈段：上半年基金约 +20.61%、尺子约 +11.25%
h1f=(1+fund['ytd']/100)/(1+fund['qtd']/100)-1
h1b=(1+acwi['ytd']/100)/(1+acwi['qtd']/100)-1
chk("4 H1 2026 fund +20.61",approx(h1f*100,20.61,0.02))
chk("4 H1 2026 acwi +11.25",approx(h1b*100,11.25,0.02))
# 5 分段十至五年前
def seg(long,short,nl,ns): return (((1+long/100)**nl/(1+short/100)**ns)**(1/(nl-ns))-1)*100
chk("5 seg 10-5 fund +29.58",approx(seg(fund['y10'],fund['y5'],10,5),29.58,0.05))
chk("5 seg 10-5 acwi +13.20",approx(seg(acwi['y10'],acwi['y5'],10,5),13.20,0.05))
# 6 分段五至三年前（大坑段）
chk("6 seg 5-3 fund -28.48",approx(seg(fund['y5'],fund['y3'],5,3),-28.48,0.05))
chk("6 seg 5-3 acwi -2.10",approx(seg(acwi['y5'],acwi['y3'],5,3),-2.10,0.05))
# 7 分段三至一年前
chk("7 seg 3-1 fund +31.81",approx(seg(fund['y3'],fund['y1'],3,1),31.81,0.05))
chk("7 seg 3-1 acwi +24.30",approx(seg(acwi['y3'],acwi['y1'],3,1),24.30,0.05))
# 8 一万美元终点
chk("8 10k 5y fund ~11797",approx(10000*(1+fund['y5']/100)**5,11797,10))
chk("8 10k 5y acwi ~17288",approx(10000*(1+acwi['y5']/100)**5,17288,10))
chk("8 10k 10y fund ~43098",approx(10000*(1+fund['y10']/100)**10,43098,20))
chk("8 10k 10y acwi ~32128",approx(10000*(1+acwi['y10']/100)**10,32128,15))
yrs=days/365.25
chk("8 10k si fund ~64727",approx(10000*(1+fund['si']/100)**yrs,64727,300))
chk("8 10k si acwi ~44907",approx(10000*(1+acwi['si']/100)**yrs,44907,250))
chk("8 si ratio ~1.44x",approx(((1+fund['si']/100)/(1+acwi['si']/100))**yrs,1.44,0.02))
# 9 日历年：2022 年 -51.57% 回本线与连涨三年仍未回原点
cal=[-51.57,25.56,26.42,27.53]; p=1.0
for v in cal: p*=1+v/100
chk("9 2022 recovery need +106.48",approx((1/0.4843-1)*100,106.48,0.02))
chk("9 thru 2024 ~0.7687 of origin",approx(0.4843*1.2556*1.2642,0.7687,0.001))
chk("9 thru 2025 ~0.9804 of origin",approx(p,0.9804,0.001))
# 10 前十大逐名合计 58.0 与印刷总计一致；第一大 SpaceX 16.8 约占前十大 29.0%
top=[16.8,7.5,6.6,5.4,4.8,3.8,3.6,3.2,3.2,3.1]
chk("10 top10 named sum 58.0 = printed",approx(sum(top),58.0,0.01))
chk("10 spacex share of top10 ~29.0%",approx(16.8/sum(top)*100,29.0,0.1))
# 11 三季度前五大正贡献合计 +6.14；SpaceX 单只拖累 -2.69
chk("11 contrib top5 sum +6.14",approx(1.65+1.41+1.26+0.99+0.83,6.14,0.01))
chk("11 spacex detraction -2.69 offsets ~43.8% of top5 gains",approx(2.69/6.14*100,43.8,0.2))
# 12 国家分布逐项合计 99.9（印刷 100.0，差 0.1 舍入只登记）；非美合计 38.8 与股东信自述一致
countries=[59.0,8.0,6.6,5.4,5.0,3.8,3.2,2.9,2.4,0.9,0.5,2.2]
chk("12 countries named sum 99.9 (printed 100.0, rounding)",approx(sum(countries),99.9,0.01))
chk("12 non-US ex-cash 38.8 matches letter",approx(100-59.0-2.2,38.8,0.01))
chk("12 sectors 80.6+17.1+2.2=99.9 (rounding)",approx(80.6+17.1+2.2,99.9,0.01))
print("TOTAL FAILS:",len(fails))
raise SystemExit(1 if fails else 0)
