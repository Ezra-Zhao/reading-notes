#!/usr/bin/env python3
"""76 Danoff 验算脚本：数字取自 Fidelity Contrafund Class K 简要招募书（2026-02-28）
与 2025 年度股东报告（截至 2025-12-31）；任职起始日 1990-09-17 为 Morningstar 口径（B 级）。
运行：python3 76-danoff-verify.py —— 十二组断言全过才算数。
"""
from datetime import date

ok = []
def chk(name, cond, detail=""):
    ok.append(cond)
    print(("PASS" if cond else "FAIL"), name, detail)

def approx(a, b, tol=0.011):
    return abs(a - b) <= tol

# 1 任期：1990-09-17 任职（B 级日期，招募书 A 级只到年份 1990）至 2025-12-31 与至预计退休 2026-12-31
d1 = (date(2025, 12, 31) - date(1990, 9, 17)).days
d2 = (date(2026, 12, 31) - date(1990, 9, 17)).days
chk("1-tenure", d1 == 12889 and d2 == 13254 and approx(d1 / 365.25, 35.29, 0.01)
    and approx(d2 / 365.25, 36.29, 0.01), f"to2025={d1}d/{d1/365.25:.2f}y toRetire={d2}d/{d2/365.25:.2f}y")

# 2 基金生命与任期占比：1967-05-17 成立（Fidelity 官方产品页）至 2025-12-31
life = (date(2025, 12, 31) - date(1967, 5, 17)).days
chk("2-life", life == 21413 and approx(d1 / life * 100, 60.19, 0.02),
    f"life={life}d share={d1/life*100:.2f}%")

# 3 平均年化超额（Class K 对标普 500，截至 2025-12-31）
chk("3-excess", approx(21.92 - 17.88, 4.04, 0.005) and approx(15.62 - 14.42, 1.20, 0.005)
    and approx(16.95 - 14.82, 2.13, 0.005), "1y +4.04 / 5y +1.20 / 10y +2.13 pp")

# 4 十年终点：年报图 10,000 美元 -> Class K 47,861 对标普 39,827；与年化复利对照
chk("4-endpoint", approx(10000 * 1.1482 ** 10, 39827, 3) and approx(10000 * 1.1695 ** 10, 47861, 3)
    and 47861 - 39827 == 8034 and approx(47861 / 39827, 1.2017, 0.0005),
    f"K_from_rate={10000*1.1695**10:.0f} SP_from_rate={10000*1.1482**10:.0f} excess=8034 ratio={47861/39827:.4f}")

# 5 逐年回报连乘（Class K 2016-2025）对十年累计
yby = [3.48, 32.34, -2.07, 30.17, 32.68, 24.42, -28.22, 39.47, 36.05, 21.92]
f = 1.0
for r in yby:
    f *= 1 + r / 100
chk("5-yby10", approx((f - 1) * 100, 378.55, 0.05) and approx(f, 47861 / 10000, 0.001),
    f"compound={(f-1)*100:.2f}% factor={f:.4f} vs graph 4.7861")

# 6 五年段：2021-2025 连乘年化恰合表载 15.62%；2016-2020 一段
f5, f5a = 1.0, 1.0
for r in yby[5:]:
    f5 *= 1 + r / 100
for r in yby[:5]:
    f5a *= 1 + r / 100
chk("6-split5", approx((f5 ** 0.2 - 1) * 100, 15.62, 0.01) and approx((f5 - 1) * 100, 106.61, 0.05)
    and approx((f5a - 1) * 100, 131.62, 0.05) and approx((f5a ** 0.2 - 1) * 100, 18.29, 0.02),
    f"last5={(f5-1)*100:.2f}% ann={(f5**0.2-1)*100:.2f}% first5={(f5a-1)*100:.2f}% ann={(f5a**0.2-1)*100:.2f}%")

# 7 负年份计数与极值
chk("7-neg", sum(1 for r in yby if r < 0) == 2 and max(yby) == 39.47 and min(yby) == -28.22,
    "neg=2 (2018 -2.07, 2022 -28.22) best=39.47 worst=-28.22")

# 8 2022 回本：-28.22% 需 +39.31%；2023 年 +39.47%，两年连乘约 +0.11%
chk("8-rebound", approx((1 / 0.7178 - 1) * 100, 39.31, 0.02)
    and approx((0.7178 * 1.3947 - 1) * 100, 0.11, 0.02),
    f"need={(1/0.7178-1)*100:.2f}% two_year={(0.7178*1.3947-1)*100:.2f}%")

# 9 季度极值：最高 +26.91%（2020-06-30）最低 -20.35%（2022-06-30）
chk("9-quarter", approx(26.91 - (-20.35), 47.26, 0.005)
    and approx((1 / 0.7965 - 1) * 100, 25.55, 0.02),
    f"range=47.26pp lowest_q_rebound={(1/0.7965-1)*100:.2f}%")

# 10 前十大合计与发行人合并口径（2025-12-31 年报）
top = [12.5, 9.4, 6.1, 6.1, 4.3, 3.9, 2.5, 2.4, 2.3, 2.1]
chk("10-top10", approx(sum(top), 51.6, 0.005) and approx(top[0] + top[1], 21.9, 0.005)
    and approx(3.9 + 2.4, 6.3, 0.005) and 3.9 + 2.4 > 6.1,
    f"top10={sum(top):.1f}% top2={top[0]+top[1]:.1f}% Alphabet A+C=6.3% > 6.1%")

# 11 行业/资产/地域三表对平
sectors = [26.0, 22.1, 16.4, 10.1, 9.9, 7.5, 2.8, 1.7, 1.4, 0.9, 0.4]
geo = [92.2, 2.6, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.3, 1.5]
chk("11-tables", approx(sum(sectors), 99.2, 0.005) and approx(sum(sectors) + 0.8, 100.0, 0.005)
    and approx(95.7 + 3.5 + 0.0 + 0.8, 100.0, 0.005) and approx(sum(geo), 100.0, 0.005),
    f"sectors={sum(sectors):.1f}% +0.8=100.0 asset=100.0 geo={sum(geo):.1f}%")

# 12 规模与费用量级：顾问费/年末净资产约 0.6761%，对费用率 0.67%（平均资产口径不同，只登记量级）
chk("12-fees", approx(1192068056 / 176314376288 * 100, 0.6761, 0.0005)
    and approx(51.6 / 10, 5.16, 0.005) and approx((100 - 51.6) / (445 - 10), 0.111, 0.001),
    f"advisory/size={1192068056/176314376288*100:.4f}% top10avg=5.16% rest_avg={(100-51.6)/435:.3f}%")

print(f"\n{sum(ok)}/12 groups passed")
assert all(ok), "ASSERTION FAILED"
print("ALL PASS")
