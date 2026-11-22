#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""108 Hawkins / Longleaf Partners Fund 验算脚本（自写）
数据源：Longleaf Partners Fund Fact Sheet（Quarter ended September 30, 2026，
Southeastern Asset Management 官网，LLP001649）印刷行；
经理认人：Longleaf Partners Funds Prospectus（May 1, 2026）Partners Fund
Management 段——O. Mason Hawkins 自 1987 年任经理、Ross Glotzbach 自 2017 年任经理。
全部用 Decimal 机械验算，断言不过即报错。
"""
from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec = 28

ok = []
def chk(name, cond, detail=""):
    assert cond, f"FAIL {name} {detail}"
    ok.append(name)
    print(f"OK {name} {detail}")

def pct(x):  # 小数转百分比显示
    return (x * 100).quantize(D("0.01"))

# 印刷行（%）
F = {"qtd": D("-2.41"), "ytd": D("-3.15"), "y1": D("0.09"), "y3": D("5.41"),
     "y5": D("1.93"), "y10": D("4.62"), "si": D("8.93")}
S = {"qtd": D("2.30"), "ytd": D("12.75"), "y1": D("15.74"), "y3": D("22.89"),
     "y5": D("13.79"), "y10": D("15.33"), "si": D("10.93")}
R = {"qtd": D("2.61"), "ytd": D("19.27"), "y1": D("23.81"), "y3": D("20.07"),
     "y5": D("11.92"), "y10": D("11.43"), "si": D("10.19")}

# 1 任期与基金生命
inc = date(1987, 4, 8); end = date(2026, 9, 30)
days = (end - inc).days
chk("1-tenure-days", days == 14420, f"1987-04-08至2026-09-30共{days}天")
yrs = D(days) / D("365.25")
chk("1-tenure-years", D("39.47") < yrs < D("39.49"), f"约{yrs.quantize(D('0.01'))}年；Hawkins自1987年任经理，与基金同龄（招募书口径）")

# 2 Q3与YTD超额
chk("2-q3-excess-sp", F["qtd"] - S["qtd"] == D("-4.71"), "三季度输标普4.71个点")
chk("2-q3-excess-rv", F["qtd"] - R["qtd"] == D("-5.02"), "三季度输Russell价值5.02个点")
chk("2-ytd-excess-sp", F["ytd"] - S["ytd"] == D("-15.90"), "年初至今输标普15.90个点")
chk("2-ytd-excess-rv", F["ytd"] - R["ytd"] == D("-22.42"), "年初至今输Russell价值22.42个点")

# 3 2026年劈段：上半年 = (1+YTD)/(1+Q3)-1
def h1(tbl): return (1 + tbl["ytd"]/100) / (1 + tbl["qtd"]/100) - 1
chk("3-h1-fund", D("-0.77") < pct(h1(F)) < D("-0.75"), f"基金上半年约{pct(h1(F))}%")
chk("3-h1-sp", D("10.20") < pct(h1(S)) < D("10.23"), f"标普上半年约{pct(h1(S))}%")
chk("3-h1-rv", D("16.22") < pct(h1(R)) < D("16.26"), f"Russell价值上半年约{pct(h1(R))}%")
chk("3-h1-gap", pct(h1(S)) - pct(h1(F)) > D("10.9"), "上半年就已输标普约11个点，三季度不是全部差距的来源")

# 4 一年窗劈段：此前九个月 = (1+1yr)/(1+Q3)-1
def first9(tbl): return (1 + tbl["y1"]/100) / (1 + tbl["qtd"]/100) - 1
chk("4-first9-fund", D("2.55") < pct(first9(F)) < D("2.58"), f"基金此前九个月约{pct(first9(F))}%")
chk("4-first9-sp", D("13.12") < pct(first9(S)) < D("13.16"), f"标普此前九个月约{pct(first9(S))}%")
chk("4-1yr-excess", F["y1"] - S["y1"] == D("-15.65") and F["y1"] - R["y1"] == D("-23.72"),
    "一年窗输标普15.65个点、输Russell价值23.72个点；一年只涨0.09%近乎原地")

# 5 累计换算（年化连乘）
def cum(ann, n): return ((1 + ann/100) ** n - 1) * 100
chk("5-cum3", D("17.10") < cum(F["y3"], 3) < D("17.16") and D("85.4") < cum(S["y3"], 3) < D("85.7"),
    f"三年累计基金约{cum(F['y3'],3).quantize(D('0.01'))}%对标普约{cum(S['y3'],3).quantize(D('0.01'))}%")
chk("5-cum5", D("10.00") < cum(F["y5"], 5) < D("10.06") and D("90.7") < cum(S["y5"], 5) < D("91.2"),
    f"五年累计基金约{cum(F['y5'],5).quantize(D('0.01'))}%对标普约{cum(S['y5'],5).quantize(D('0.01'))}%")
chk("5-cum10", D("56.9") < cum(F["y10"], 10) < D("57.2") and D("315") < cum(S["y10"], 10) < D("319"),
    f"十年累计基金约{cum(F['y10'],10).quantize(D('0.01'))}%对标普约{cum(S['y10'],10).quantize(D('0.01'))}%")

# 6 十年拆段：五至十年前一段 = (1+10yr累计)/(1+5yr累计)-1
seg_f = (1 + cum(F["y10"], 10)/100) / (1 + cum(F["y5"], 5)/100) - 1
seg_s = (1 + cum(S["y10"], 10)/100) / (1 + cum(S["y5"], 5)/100) - 1
seg_r = (1 + cum(R["y10"], 10)/100) / (1 + cum(R["y5"], 5)/100) - 1
chk("6-seg-fund", D("42.5") < pct(seg_f) < D("43.0"), f"基金五至十年前一段约{pct(seg_f)}%")
chk("6-seg-sp", D("118") < pct(seg_s) < D("120"), f"标普同段约{pct(seg_s)}%")
chk("6-seg-rv", D("67") < pct(seg_r) < D("69"), f"Russell价值同段约{pct(seg_r)}%")
chk("6-seg-all-lose", seg_f < seg_r < seg_s, "拆段后更早五年基金同样落后，不是只有最近五年才输")

# 7 自成立终点（机械滚算，1万美元，年数=天数/365.25）
def terminal(ann): return D(10000) * (1 + ann/100) ** yrs
tf, ts, tr = terminal(F["si"]), terminal(S["si"]), terminal(R["si"])
chk("7-terminal-fund", D(285000) < tf < D(300000), f"基金一万美元机械终点约{int(tf)}美元")
chk("7-terminal-sp", D(590000) < ts < D(640000), f"标普约{int(ts)}美元")
chk("7-ratio", D("2.05") < ts/tf < D("2.20"), f"标普终点约基金的{(ts/tf).quantize(D('0.01'))}倍；每年只差2.00个点，39.5年差出一倍多")
chk("7-si-excess", F["si"] - S["si"] == D("-2.00") and F["si"] - R["si"] == D("-1.26"),
    "自成立年化输标普整2.00个点、输Russell价值1.26个点")

# 8 持仓合计与集中度
hold = [D("8.50"), D("7.73"), D("7.61"), D("6.94"), D("6.46"), D("6.40"),
        D("6.38"), D("6.19"), D("4.96"), D("4.86"), D("4.79"), D("4.77"),
        D("4.31"), D("3.31"), D("3.03"), D("2.98"), D("2.28"), D("2.10")]
chk("8-hold-count-sum", len(hold) == 18 and sum(hold) == D("93.60"), "18只持仓合计93.60%")
chk("8-plus-cash", sum(hold) + D("6.40") == D("100.00"), "加现金6.40%恰为100.00%，与印刷Total对齐")
chk("8-top5", sum(hold[:5]) == D("37.24"), "前五大合计37.24%")
chk("8-top10", sum(hold[:10]) == D("66.03"), "前十大合计66.03%，是股票仓位的约七成")
chk("8-rest8", sum(hold[10:]) == D("27.57"), "后八只合计27.57%")

# 9 行业合计与三个零
sec = [D("18.69"), D("14.40"), D("13.36"), D("12.79"), D("11.13"), D("9.89"),
       D("6.94"), D("6.40"), D("0.00"), D("0.00"), D("0.00")]
chk("9-sector-sum", sum(sec) + D("6.40") == D("100.00"), "十一行业合计93.60%，加现金6.40%恰100.00%")
chk("9-three-zeros", sec.count(D("0.00")) == 3, "材料、信息技术、公用事业三行业为0.00%——信息技术为零是与标普最大的结构差之一")
chk("9-triple-640", hold[5] == sec[7] == D("6.40"), "现金6.40%、能源行业6.40%、CNX单只6.40%，三个6.40互为印证（能源即CNX一只）")

# 10 费用与规模
chk("10-fee-waiver", D("0.93") - D("0.79") == D("0.14"), "费率总0.93%净0.79%，豁免差0.14个点，协议至少到2027-04-30")
chk("10-scale", D("1.0")/D("2.9") > D("0.34") and D("1.0")/D("2.9") < D("0.35"),
    "基金净资产约10亿美元约占公司总规模29亿美元的34%（均为印刷约数，只作量级）")

# 11 P/V 含义（mid-50s 只作区间登记）
chk("11-pv-midpoint", D("80") < (D(1)/D("0.55") - 1) * 100 < D("83"),
    "P/V若取55%中值，价格涨到估值需约+81.8%；印刷口径是mid-50s区间，不写死单点")
chk("11-pv-range", (D(1)/D("0.59") - 1) * 100 > D("69") and (D(1)/D("0.50") - 1) * 100 == D("100"),
    "P/V在50–59%区间对应涨到估值的空间约+69%至+100%，区间登记")

# 12 回本价
chk("12-ytd-recovery", D("3.25") < (D(1)/(1 + F["ytd"]/100) - 1) * 100 < D("3.26"),
    "年初至今-3.15%，回本需约+3.25%")
chk("12-q3-recovery", D("2.46") < (D(1)/(1 + F["qtd"]/100) - 1) * 100 < D("2.48"),
    "三季度-2.41%，单季回本需约+2.47%")

print(f"\nALL {len(ok)} assertions passed in 12 groups.")
print(f"days={days} years={yrs.quantize(D('0.01'))} terminal_fund={int(tf)} terminal_sp={int(ts)} terminal_rv={int(tr)}")
print(f"H1 fund={pct(h1(F))}% sp={pct(h1(S))}% rv={pct(h1(R))}% | first9 fund={pct(first9(F))}% sp={pct(first9(S))}%")
print(f"cum3 F={cum(F['y3'],3).quantize(D('0.01'))} S={cum(S['y3'],3).quantize(D('0.01'))} | cum5 F={cum(F['y5'],5).quantize(D('0.01'))} S={cum(S['y5'],5).quantize(D('0.01'))} | cum10 F={cum(F['y10'],10).quantize(D('0.01'))} S={cum(S['y10'],10).quantize(D('0.01'))}")
print(f"seg5-10 F={pct(seg_f)} S={pct(seg_s)} R={pct(seg_r)}")
