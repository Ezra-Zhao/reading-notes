#!/usr/bin/env python3
"""77 万民远 验算脚本：数字取自融通健康产业灵活配置混合型证券投资基金
2026 年第 3 季度报告（期末 2026-09-30，送出 2026-10-26）。
运行：python3 77-wan-verify.py —— 十二组断言全过才算数。
"""
from datetime import date

ok = []
def chk(name, cond, detail=""):
    ok.append(cond)
    print(("PASS" if cond else "FAIL"), name, detail)

def approx(a, b, tol=0.011):
    return abs(a - b) <= tol

# 1 任期与基金生命：2016-08-26 任职至 2026-09-30；基金 2014-12-25 生效
tenure = (date(2026, 9, 30) - date(2016, 8, 26)).days
life = (date(2026, 9, 30) - date(2014, 12, 25)).days
pre = (date(2016, 8, 26) - date(2014, 12, 25)).days
chk("1-tenure", tenure == 3687 and life == 4297 and pre == 610
    and approx(tenure / 365.25, 10.09, 0.01) and approx(tenure / life * 100, 85.80, 0.02),
    f"tenure={tenure}d/{tenure/365.25:.2f}y life={life}d pre={pre}d share={tenure/life*100:.2f}%")

# 2 A 类八个窗口超额逐项等于两列之差
A = [(13.30, 8.19, 5.11), (-3.53, 1.25, -4.78), (-10.79, -5.72, -5.07),
     (-15.59, 0.58, -16.17), (-10.44, -17.12, 6.68), (79.18, 12.95, 66.23),
     (124.10, 9.98, 114.12), (153.94, 43.50, 110.44)]
chk("2-excess-A", all(approx(a - b, c, 0.005) for a, b, c in A), "8 windows A excess all match")

# 3 半年劈成两季：六个月因子除以三季度因子反推二季度
q2 = (0.9647 / 1.1330 - 1) * 100
q2b = (1.0125 / 1.0819 - 1) * 100
chk("3-q2-reverse", approx(q2, -14.85, 0.01) and approx(q2b, -6.41, 0.01)
    and approx((1 / (1 + q2 / 100) - 1) * 100, 17.45, 0.02)
    and approx((1 / 0.9647 - 1) * 100, 3.66, 0.01),
    f"Q2 A={q2:.2f}% bench={q2b:.2f}% Q2-loss-recovery={(1/(1+q2/100)-1)*100:.2f}% half-recovery={(1/0.9647-1)*100:.2f}%")

# 4 长窗口拆段：十年最早五年与七年至三年一段
first5 = (2.2410 / 0.8956 - 1) * 100
seg = (1.7918 / 0.8441 - 1) * 100
chk("4-split", approx(first5, 150.22, 0.02) and approx(seg, 112.27, 0.02),
    f"first5of10y={first5:.2f}% seg7to3={seg:.2f}% last5=-10.44% last3=-15.59%")

# 5 自生效因子与期末净值：153.94% 对应因子 2.5394，A/B 期末净值 2.539 元
chk("5-nav", approx(2.539 / 2.5394 * 100, 99.98, 0.01),
    f"nav/factor={2.539/2.5394*100:.2f}% diff={abs(2.5394-2.539)/2.5394*100:.3f}%")

# 6 利润拆分：已实现为负、本期利润为正，差为公允价值变动
A_real, A_prof = -18416363.02, 140987674.85
C_real, C_prof = -3436308.40, 24185872.44
chk("6-profit", approx(A_prof - A_real, 159404037.87, 0.01)
    and approx((A_prof - A_real) / abs(A_real), 8.66, 0.01)
    and approx(C_prof - C_real, 27622180.84, 0.01)
    and approx((A_prof + C_prof) - (A_real + C_real), 187026218.71, 0.01),
    f"A fv={A_prof-A_real:.2f} x{(A_prof-A_real)/abs(A_real):.2f} combined fv={(A_prof+C_prof)-(A_real+C_real):.2f}")

# 7 加权平均份额反推落在期初与期末之间
wa = A_prof / 0.3027
wc = C_prof / 0.2896
chk("7-wavg", 409855496.21 < wa < 490990614.10 and 76581841.97 < wc < 96745894.84,
    f"A wavg={wa:,.0f} C wavg={wc:,.0f} both inside start-end range")

# 8 资产对平与仓位：权益+存款备付金+其他资产=总资产；权益占总资产 93.87%、占净值 94.10%
chk("8-assets", approx(1156413740.99 + 64869690.04 + 10699127.06, 1231982558.09, 0.01)
    and approx(1156413740.99 / 1231982558.09 * 100, 93.87, 0.01)
    and approx(1156413740.99 / 1228974238.38 * 100, 94.10, 0.01)
    and approx(1040610314.95 + 188363923.43, 1228974238.38, 0.01),
    f"sum=1231982558.09 eq/total=93.87% eq/nav={1156413740.99/1228974238.38*100:.2f}%")

# 9 行业表合计与前四行业
inds = [0.00, 53.95, 0.03, 11.99, 0.06, 20.05, 8.02]
chk("9-industry", approx(sum(inds), 94.10, 0.005) and approx(53.95 + 20.05 + 11.99 + 8.02, 94.01, 0.005),
    f"industry total={sum(inds):.2f}% top4={53.95+20.05+11.99+8.02:.2f}%")

# 10 前十大合计、前二合计、前十大占权益仓位
top = [7.58, 7.34, 6.74, 6.64, 6.64, 5.69, 5.67, 4.86, 4.81, 4.77]
chk("10-top10", approx(sum(top), 60.74, 0.005) and approx(top[0] + top[1], 14.92, 0.005)
    and approx(sum(top) / 94.10 * 100, 64.55, 0.02),
    f"top10={sum(top):.2f}% top2={top[0]+top[1]:.2f}% top10/equity={sum(top)/94.10*100:.2f}%")

# 11 份额对平与净变动：两类各自对平、合计等于 §2 总额
chk("11-shares", approx(490990614.10 + 15515862.21 - 96650980.10, 409855496.21, 0.01)
    and approx(96745894.84 + 7994643.15 - 28158696.02, 76581841.97, 0.01)
    and approx(409855496.21 + 76581841.97, 486437338.18, 0.01)
    and approx((409855496.21 - 490990614.10) / 490990614.10 * 100, -16.52, 0.01)
    and approx((76581841.97 - 96745894.84) / 96745894.84 * 100, -20.84, 0.01)
    and approx((486437338.18 - 587736508.94) / 587736508.94 * 100, -17.24, 0.01),
    "A -16.52% C -20.84% total -17.24% end total matches sec.2")

# 12 C 类六个窗口超额逐项等于两列之差（C 类自生效窗口起点为 2020-04-14 增设日口径）
C = [(13.16, 8.19, 4.97), (-3.76, 1.25, -5.01), (-11.22, -5.72, -5.50),
     (-16.84, 0.58, -17.42), (-12.64, -17.12, 4.48), (18.27, -3.78, 22.05)]
chk("12-excess-C", all(approx(a - b, c, 0.005) for a, b, c in C), "6 windows C excess all match")

print(f"\n{sum(ok)}/12 groups passed")
assert all(ok), "ASSERTION FAILED"
print("ALL PASS")
