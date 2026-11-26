# -*- coding: utf-8 -*-
"""151 Lippert 验算脚本：数字全部取 Baron Opportunity Fund 官方事实表（BIOIX，2026-09-30）。
证据分级：A=官方披露原文数字；C=按 A 做四则运算/连乘反推的验算值。"""
from decimal import Decimal as D
from datetime import date

ok = 0
def chk(cond, label):
    global ok
    assert cond, label
    ok += 1
    print("PASS", label)

# 第1组 基金生命：2000-02-29 至 2026-09-30
days = (date(2026,9,30)-date(2000,2,29)).days
chk(days == 9710, f"基金生命 {days} 天")
chk(abs(D(days)/D(365) - D("26.60")) < D("0.01"), "约 26.60 年")

# 第2组 任期切分：Lippert 2006-03-03 起任（Schwab 报告口径）至 2026-09-30
tdays = (date(2026,9,30)-date(2006,3,3)).days
chk(tdays == 7516, f"任期 {tdays} 天")
share = D(tdays)/D(days)*100
chk(D("77.3") < share < D("77.5"), f"任期占基金生命约 {share:.2f}%")
pre = days - tdays
chk(pre == 2194, f"前任段 {pre} 天约 6.01 年")

# 官方年化表（证据 A）
fund = {"qtd":D("0.77"),"ytd":D("16.69"),"1y":D("22.09"),"3y":D("31.14"),"5y":D("11.62"),"10y":D("21.82"),"si":D("10.93")}
rg   = {"qtd":D("0.45"),"ytd":D("6.36"),"1y":D("7.58"),"3y":D("23.84"),"5y":D("13.11"),"10y":D("17.62"),"si":D("8.09")}
sp   = {"qtd":D("2.30"),"ytd":D("12.75"),"1y":D("15.74"),"3y":D("22.89"),"5y":D("13.79"),"10y":D("15.33"),"si":D("8.67")}

# 第3组 对 Russell 3000 Growth 超额：七窗赢六窗、只输五年
ex = {k: fund[k]-rg[k] for k in fund}
chk(ex["qtd"]==D("0.32") and ex["ytd"]==D("10.33") and ex["1y"]==D("14.51"), "对成长尺近窗超额")
chk(ex["3y"]==D("7.30") and ex["5y"]==D("-1.49") and ex["10y"]==D("4.20") and ex["si"]==D("2.84"), "对成长尺长窗超额")
chk(sum(1 for v in ex.values() if v>0)==6, "对成长尺七窗赢六窗")

# 第4组 对标普 500 超额：七窗赢五窗
exs = {k: fund[k]-sp[k] for k in fund}
chk(exs["qtd"]==D("-1.53") and exs["5y"]==D("-2.17"), "对标普输三季度与五年")
chk(sum(1 for v in exs.values() if v>0)==5, "对标普七窗赢五窗")

# 第5组 2026 上半年反推：YTD 拆 H1 与 Q3
h1 = ( (1+fund["ytd"]/100)/(1+fund["qtd"]/100) - 1 )*100
h1r = ( (1+rg["ytd"]/100)/(1+rg["qtd"]/100) - 1 )*100
chk(D("15.7") < h1 < D("15.9"), f"基金上半年反推约 {h1:.2f}%")
chk(D("5.8") < h1r < D("6.0"), f"成长尺上半年反推约 {h1r:.2f}%")

# 第6组 分段：十至五年前
def seg(ann_long, yrs_long, ann_short, yrs_short):
    total = (1+ann_long/100)**yrs_long
    short = (1+ann_short/100)**yrs_short
    return ((total/short) ** (D(1)/(yrs_long-yrs_short)) - 1)*100
s105 = seg(fund["10y"],10,fund["5y"],5)
s105r = seg(rg["10y"],10,rg["5y"],5)
chk(D("32.5") < s105 < D("33.5"), f"十至五年前基金约 {s105:.2f}%/年")
chk(D("22.0") < s105r < D("23.0"), f"十至五年前成长尺约 {s105r:.2f}%/年")

# 第7组 分段：五至三年前（坑）与三至一年前
s53 = seg(fund["5y"],5,fund["3y"],3)
s53r = seg(rg["5y"],5,rg["3y"],3)
chk(D("-12.5") < s53 < D("-11.0"), f"五至三年前基金约 {s53:.2f}%/年")
chk(D("-2.0") < s53r < D("-0.5"), f"五至三年前成长尺约 {s53r:.2f}%/年")
s31 = (( (1+fund["3y"]/100)**3/(1+fund["1y"]/100) ) ** D("0.5") - 1)*100
chk(D("35.0") < s31 < D("36.5"), f"三至一年前基金约 {s31:.2f}%/年")

# 第8组 一万美元终点
e5 = 10000*(1+fund["5y"]/100)**5
e10 = 10000*(1+fund["10y"]/100)**10
esi = 10000*(1+fund["si"]/100)**(D(days)/D(365))
esir = 10000*(1+rg["si"]/100)**(D(days)/D(365))
chk(D("17000") < e5 < D("17800"), f"五年终点约 {e5:.0f}")
chk(D("71000") < e10 < D("73000"), f"十年终点约 {e10:.0f}")
chk(D("155000") < esi < D("165000"), f"自成立终点约 {esi:.0f}")
chk(D("1.9") < esi/esir < D("2.1"), f"自成立终点约为主基准 {esi/esir:.2f} 倍")

# 第9组 2022 回本算术
need = (1/(1-D("42.83")/100)-1)*100
chk(D("74.8") < need < D("75.1"), f"2022 跌 42.83% 回本需约 {need:.2f}%")
rec = (1+D("49.98")/100)*(1+D("40.25")/100)*(1+D("19.73")/100)
net = (1-D("42.83")/100)*rec
chk(D("1.42") < net < D("1.46"), f"2022 跌后连涨三年至 2025 年末约过原点 {(net-1)*100:.2f}%")

# 第10组 日历年形状：2016-2025 十年只亏两年
cal = [D("-4.56"),D("40.88"),D("8.35"),D("40.60"),D("89.28"),D("12.29"),D("-42.83"),D("49.98"),D("40.25"),D("19.73")]
chk(sum(1 for v in cal if v<0)==2, "十年只亏 2016 与 2022 两年")
chk(max(cal)==D("89.28"), "最佳年 2020 +89.28%")

# 第11组 持仓：前十大逐名合计与印刷合计对位、前二集中
top = [D("16.4"),D("12.9"),D("4.7"),D("4.7"),D("4.2"),D("3.9"),D("3.5"),D("3.4"),D("3.2"),D("2.6")]
chk(sum(top)==D("59.5"), "前十大逐名合计 59.5 与印刷总计一致")
chk(top[0]+top[1]==D("29.3"), "前二 SpaceX+NVIDIA 合计 29.3%")

# 第12组 归因接缝：SpaceX 三季度拖累 -2.52 对全季 +0.77 的量级
chk(D("2.52") > fund["qtd"]*3, "SpaceX 单季拖累 2.52 约为全季涨幅 0.77 的三倍以上")
chk(D("1.70")/fund["qtd"] > 2, "NVIDIA 单季贡献 1.70 约为全季涨幅两倍以上")

print(f"ALL {ok} ASSERTIONS PASSED")
