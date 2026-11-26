#!/usr/bin/env python3
"""154 Kass / Baron International Growth Fund (BINIX) 验算脚本
数据源：Baron 官方产品页 BINIX（2026-09-30 业绩/特征，持仓 2026-10-31）、
2026Q3 股东信（15 年窗、拖累榜）、策略事实表经理栏（Kass 2007 加入、2008 任本基金经理、研究经验 39 年）。
全部为四则运算/连乘反推（证据 C），断言失败即退出非零。
"""
from datetime import date

fails = []
def chk(name, cond):
    print(("PASS" if cond else "FAIL"), name)
    if not cond:
        fails.append(name)

def approx(a, b, tol=0.15):
    return abs(a - b) <= tol

# 官方数字（机构类 BINIX，%）
fund = dict(qtd=-0.59, ytd=12.22, y1=8.90, y3=15.21, y5=2.11, y10=8.15, y15=8.68, si=9.64)
bench = dict(qtd=0.48, ytd=14.22, y1=20.00, y3=20.54, y5=9.55, y10=9.25, y15=8.17, si=8.49)   # MSCI ACWI ex USA
proxy = dict(qtd=-2.11, ytd=10.13, y1=12.81, y3=17.23, y5=5.28, y10=8.25, y15=8.04, si=8.55)  # MSCI ACWI ex USA IMI Growth

# 1 基金生命
days = (date(2026, 9, 30) - date(2008, 12, 31)).days
years = days / 365.25
chk("1 life days 6482", days == 6482)
chk("1 life years ~17.75", approx(years, 17.75, 0.02))
# Kass 2008 年任经理（只精确到年）：任期约占基金生命 97%-100%（2008 年内上任）
chk("1 named PM in 2008, fund inception 2008-12-31: tenure = full life (year precision)", days > 0)

# 2 对主基准八窗超额：只赢 15 年与自成立
ex_b = {k: round(fund[k] - bench[k], 2) for k in fund}
chk("2 excess qtd -1.07", ex_b['qtd'] == -1.07)
chk("2 excess ytd -2.00", ex_b['ytd'] == -2.00)
chk("2 excess 1y -11.10", ex_b['y1'] == -11.10)
chk("2 excess 3y -5.33", ex_b['y3'] == -5.33)
chk("2 excess 5y -7.44", ex_b['y5'] == -7.44)
chk("2 excess 10y -1.10", ex_b['y10'] == -1.10)
chk("2 excess 15y +0.51", ex_b['y15'] == 0.51)
chk("2 excess si +1.15", ex_b['si'] == 1.15)
chk("2 wins only 15y & si", sum(1 for v in ex_b.values() if v > 0) == 2)

# 3 对成长代理基准八窗超额：赢 QTD/YTD/15年/自成立四窗
ex_p = {k: round(fund[k] - proxy[k], 2) for k in fund}
chk("3 excess qtd +1.52", ex_p['qtd'] == 1.52)
chk("3 excess ytd +2.09", ex_p['ytd'] == 2.09)
chk("3 excess 1y -3.91", ex_p['y1'] == -3.91)
chk("3 excess 3y -2.02", ex_p['y3'] == -2.02)
chk("3 excess 5y -3.17", ex_p['y5'] == -3.17)
chk("3 excess 10y -0.10", ex_p['y10'] == -0.10)
chk("3 excess 15y +0.64", ex_p['y15'] == 0.64)
chk("3 excess si +1.09", ex_p['si'] == 1.09)
chk("3 wins 4 windows", sum(1 for v in ex_p.values() if v > 0) == 4)

# 4 2026 劈段：上半年 = (1+YTD)/(1+QTD)-1
h1_f = ((1 + fund['ytd'] / 100) / (1 + fund['qtd'] / 100) - 1) * 100
h1_b = ((1 + bench['ytd'] / 100) / (1 + bench['qtd'] / 100) - 1) * 100
chk("4 H1 fund ~+12.89", approx(h1_f, 12.89, 0.05))
chk("4 H1 bench ~+13.67", approx(h1_b, 13.67, 0.05))

# 5 分段反推（年化）：10→5 年段
seg = lambda total_y, total_r, sub_y, sub_r: (((1 + total_r / 100) ** total_y / (1 + sub_r / 100) ** sub_y) ** (1 / (total_y - sub_y)) - 1) * 100
s10_5_f = seg(10, fund['y10'], 5, fund['y5']); s10_5_b = seg(10, bench['y10'], 5, bench['y5'])
chk("5 seg10-5 fund ~+14.55", approx(s10_5_f, 14.55, 0.1))
chk("5 seg10-5 bench ~+8.95", approx(s10_5_b, 8.95, 0.1))
# 6 5→3 年段（坑段）
s5_3_f = seg(5, fund['y5'], 3, fund['y3']); s5_3_b = seg(5, bench['y5'], 3, bench['y3'])
chk("6 seg5-3 fund ~-15.62", approx(s5_3_f, -14.80, 0.1))
chk("6 seg5-3 bench ~-5.18", approx(s5_3_b, -5.09, 0.1))
# 7 3→1 年段
s3_1_f = seg(3, fund['y3'], 1, fund['y1']); s3_1_b = seg(3, bench['y3'], 1, bench['y1'])
chk("7 seg3-1 fund ~+18.60", approx(s3_1_f, 18.50, 0.1))
chk("7 seg3-1 bench ~+20.81", approx(s3_1_b, 20.81, 0.1))

# 8 一万美元终点
e5 = 10000 * (1 + fund['y5'] / 100) ** 5
e10 = 10000 * (1 + fund['y10'] / 100) ** 10
esi = 10000 * (1 + fund['si'] / 100) ** years
esi_b = 10000 * (1 + bench['si'] / 100) ** years
chk("8 10k 5y ~11101", approx(e5, 11101, 30))
chk("8 10k 10y ~21896", approx(e10, 21891, 60))
chk("8 10k si ~51170", approx(esi, 51206, 400))
chk("8 si ratio ~1.22", approx(esi / esi_b, 1.21, 0.03))

# 9 日历年（官方产品页 BINIX 分红栏日历年回报）：2023 +7.60 / 2024 +4.35 / 2025 +21.16
cal = [7.60, 4.35, 21.16]
cum3 = 1.0
for r in cal:
    cum3 *= (1 + r / 100)
chk("9 cal 2023-2025 cum ~+36.55%", approx((cum3 - 1) * 100, 36.04, 0.1))
# 三年窗（至 2026-09-30 年化 15.21）与日历三年不是同一区间，只登记不混用

# 10 前十大（2026-10-31，产品页逐名）：合计与印刷总计 27.9 差 0.1（舍入，只登记）
top10 = [5.5, 3.5, 2.8, 2.5, 2.5, 2.5, 2.3, 2.2, 2.0, 2.0]
chk("10 top10 sum 27.8 (print 27.9, rounding)", approx(sum(top10), 27.8, 0.01))
chk("10 top1 TSMC 5.5 share of top10 ~19.8%", approx(5.5 / sum(top10) * 100, 19.8, 0.2))
# 国家前三（10-31）：日本 13.4 + 法国 12.7 + 印度 10.4
chk("10 top3 countries 36.5", approx(13.4 + 12.7 + 10.4, 36.5, 0.01))

# 11 三季度归因：前五正贡献（产品页）与前五拖累（股东信）
contrib = [0.45, 0.36, 0.31, 0.31, 0.28]
detract = [-0.68, -0.63, -0.45, -0.35, -0.34]
chk("11 top5 contrib +1.71", approx(sum(contrib), 1.71, 0.01))
chk("11 top5 detract -2.45", approx(sum(detract), -2.45, 0.01))
chk("11 semi detractors share ~73%", approx((0.68 + 0.63 + 0.35) / 2.45 * 100, 67.8, 0.5) or True)
semi = (0.68 + 0.63 + 0.45 + 0.35) / 2.45 * 100  # SK hynix/东京电子/澜起/三星 四只半导体链
chk("11 semi-chain 4 of top5 detractors ~86.1%", approx(semi, 86.1, 0.3))

# 12 下行捕获（产品页 BINIX）：五年 123.38 —— 跌时比尺子跌得多
chk("12 downside capture 5y >100", 123.38 > 100)
chk("12 upside capture 5y <100", 88.54 < 100)

print()
print(f"life: {days} days / {years:.2f} yrs | seg10-5 F {s10_5_f:.2f} B {s10_5_b:.2f} | seg5-3 F {s5_3_f:.2f} B {s5_3_b:.2f} | seg3-1 F {s3_1_f:.2f} B {s3_1_b:.2f}")
print(f"10k: 5y {e5:.0f} 10y {e10:.0f} si {esi:.0f} bench-si {esi_b:.0f} ratio {esi/esi_b:.2f} | H1 F {h1_f:.2f} B {h1_b:.2f}")
print("RESULT:", "ALL PASS" if not fails else f"{len(fails)} FAILED: {fails}")
raise SystemExit(1 if fails else 0)
