# -*- coding: utf-8 -*-
"""谢治宇篇验算：兴全合润2026二季报/三季报口径连乘、份额与规模。"""
from datetime import date

def close(a, b, tol=0.15):
    return abs(a - b) <= tol

# 1 二季度+三季度连乘对三季报“过去六个月5.92%”
chain = 1.4118 * 0.7503
assert close((chain - 1) * 100, 5.92, 0.05), chain
print(f"1 Q2 +41.18% x Q3 -24.97% 连乘 {chain:.4f} -> {(chain-1)*100:.2f}% vs 三季报过去六个月 5.92% OK")

# 2 三季度基准反推：A/C两类跑输幅度指向同一基准
bench_a = -24.97 + 15.15
bench_c = -25.09 + 15.27
assert close(bench_a, -9.82, 0.01) and close(bench_c, -9.82, 0.01)
print(f"2 基准反推 A {bench_a:.2f}% / C {bench_c:.2f}% 两类一致 OK")

# 3 期末净资产与本期利润合计（利润分项和与报道合计差0.01为分项取舍）
assets = 177.43 + 4.74
profit = -59.80 + -1.53
assert close(assets, 182.17, 0.01) and close(profit, -61.34, 0.02)
print(f"3 净资产 A+C {assets:.2f}亿; 本期利润分项和 {profit:.2f}亿 vs 报道合计 -61.34亿(差0.01取舍) OK")

# 4 份额：期初合计、期末合计与净赎回
start = 81.61 + 1.96
end = 80.22 + 2.16
assert close(start, 83.57, 0.01) and close(end, 82.38, 0.01) and close(start - end, 1.19, 0.01)
assert close(80.22 - 81.61, -1.39, 0.01) and close(2.16 - 1.96, 0.20, 0.01)
print(f"4 份额 期初 {start:.2f} -> 期末 {end:.2f} 亿份, 净赎回 {start-end:.2f} (A -1.39 / C +0.20) OK")

# 5 跌24.97%回本所需涨幅
rec = (1 / 0.7503 - 1) * 100
assert close(rec, 33.28, 0.05)
print(f"5 Q3跌24.97%后回原点需涨 {rec:.2f}% OK")

# 6 三年/五年超额（百分点）与三年终值比
assert close(51.12 - 18.37, 32.75, 0.01) and close(13.97 - (-3.13), 17.10, 0.01)
ratio = 1.5112 / 1.1837
assert close(ratio, 1.2767, 0.001)
print(f"6 超额 三年 +32.75pp / 五年 +17.10pp; 三年终值比 {ratio:.4f} OK")

# 7 前五大重仓集中度
top5 = 8.55 + 7.36 + 6.30 + 5.86 + 5.17
assert close(top5, 33.24, 0.01)
print(f"7 前五大重仓合计占净值 {top5:.2f}% (晶合集成8.55/立讯精密7.36/晶晨股份6.30/泰格医药5.86/药明康德5.17) OK")

# 8 任期天数 2013-01-29 -> 2026-09-30
days = (date(2026, 9, 30) - date(2013, 1, 29)).days
yrs = days / 365.25
assert days == 4992, days
print(f"8 任合润 {days} 天, 约 {yrs:.2f} 年 OK")

# 9 二季度末净资产量级复核：期初份额(即Q2末份额) x Q2末净值
q2a = 81.61 * 2.9481
assert close(q2a, 240.58, 0.5), q2a
drop = (182.17 - (240.58 + 1.96 * 2.9274))
print(f"9 Q2末A净资产复算 {q2a:.2f}亿 vs 二季报 240.58亿 OK; Q3末总净资产较Q2末约 {drop:.2f}亿 (利润-61.34+净赎回约-2.8) OK")

# 10 兴全社会价值：三季度跑输与成立以来超额
assert close(-11.07 - (-6.31), -4.76, 0.01) and close(127.60 - 7.52, 120.08, 0.01)
print("10 社会价值 Q3 -11.07% vs 基准 -6.31% 差 -4.76pp; 成立以来 127.60% vs 7.52% 超额 120.08pp OK")

print("ALL PASS")
