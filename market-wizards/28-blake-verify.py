# -*- coding: utf-8 -*-
"""Gil Blake 篇验算：Schwager《The New Market Wizards》Blake 章口径复算。"""
from datetime import date
from math import comb

def close(a, b, tol=0.15):
    return abs(a - b) <= tol

def binom_majority(n, p):
    return sum(comb(n, k) * p**k * (1 - p) ** (n - k) for k in range(n // 2 + 1, n + 1))

# 1 月度一致性：134/139、亏损月数、胜负比与原书结尾 25 倍之差
pct = 134 / 139 * 100
assert close(pct, 96.40, 0.01) and 139 - 134 == 5
ratio = 134 / 5
assert close(ratio, 26.80, 0.01) and close(ratio - 25, 1.80, 0.01)
print(f"1 月度 134/139 = {pct:.2f}%, 亏损 5 个月, 不亏/亏损比 {ratio:.1f} vs 原书结尾约 25 倍差 1.8 OK")

# 2 十二年年均 45% 的机械连乘（只作量级，不是实际终值：45% 为平均口径）
c45 = 1.45 ** 12
c35 = 1.35 ** 12
c55 = 1.55 ** 12
assert close(c45, 86.38, 0.05) and close(c35, 36.64, 0.05) and close(c55, 192.30, 0.05)
print(f"2 机械连乘 45%^12 = {c45:.2f} 倍; 35%^12 = {c35:.2f}; 55%^12 = {c55:.2f} (平均不等于逐年同率) OK")

# 3 市政债基金 NAV 10.50 -> 5.65 的跌幅
drop = (5.65 - 10.50) / 10.50 * 100
assert close(drop, -46.19, 0.01)
print(f"3 NAV 10.50 -> 5.65 跌幅 {drop:.2f}% (原书作 nearly 50%) OK")

# 4 二项分布硬币类比：9 枚对得上原书 62%，99 枚对不上原书约 75%
p9 = binom_majority(9, 0.55) * 100
p99 = binom_majority(99, 0.55) * 100
assert close(p9, 62.14, 0.05) and close(p99, 84.13, 0.05) and close(p99 - 75, 9.13, 0.05)
print(f"4 硬币类比 9 枚多数正面 {p9:.2f}% vs 原书 62% OK; 99 枚 {p99:.2f}% vs 原书约 75% 差 {p99-75:.2f}pp (原书低估) OK")

# 5 原书脚注：250 日、平均日变动 1%、涨 20% 对应 135 涨日/115 跌日
assert close(135 / 250 * 100, 54.0, 0.01) and (135 - 115) * 1 == 20 and 135 + 115 == 250
print("5 脚注 135/250 = 54.00% 涨日, 简单加减 (135-115)*1% = +20% (非连乘口径) OK")

# 6 板块波动对已萎缩的市政债基金波动的倍数
assert close(0.8 / 0.2, 4.0, 0.01) and close(0.8 / 0.1, 8.0, 0.01)
assert close(1.2 / 0.2, 6.0, 0.01) and close(1.2 / 0.1, 12.0, 0.01)
print("6 波动倍数 生物科技 0.8% 对 0.1-0.2% 为 4-8 倍; 黄金 1.2% 为 6-12 倍 (原书作 more than five times) OK")

# 7 能源服务基金小时限额：原限额为资产 1% 约 50 万美元，反推资产与降幅
assets = 500000 / 0.01
cut = (100000 - 500000) / 500000 * 100
assert close(assets, 50000000, 1) and close(cut, -80.0, 0.01)
print(f"7 限额反推 1% = 500,000 美元对应资产约 {assets:,.0f} 美元; 新限额 100,000 美元降 {cut:.1f}% OK")

# 8 紧张客户账户与两笔医疗板块亏损的量级
acct = (67000 - 70000) / 70000 * 100
assert close(acct, -4.29, 0.01) and 70000 - 67000 == 3000
two3 = (0.97 * 0.97 - 1) * 100
two2 = (0.98 * 0.98 - 1) * 100
assert close(two3, -5.91, 0.01) and close(two2, -3.96, 0.01)
print(f"8 客户 70,000 -> 67,000 = {acct:.2f}% 亏 3,000 美元; 两笔各亏 2-3% 若连乘为 {two2:.2f}% 至 {two3:.2f}% OK")

# 9 切换频率对指引的倍数、二押借款与收益的利差
assert close(20 / 4, 5.0, 0.01) and close(30 / 4, 7.5, 0.01)
assert close(35 - 15, 20, 0.01) and close(40 - 15, 25, 0.01)
print("9 切换 20-30 次/年是指引 4 次的 5.0-7.5 倍; 二押成本 15% 对收益 35-40% 利差 20-25pp OK")

# 10 日期与年数：出生、开始交易年龄、139 个月折年、锦标赛与连胜月差
age_days = (date(1980, 3, 1) - date(1945, 7, 14)).days
assert 12600 < age_days < 12700  # 1980 年春开始交易时 34 岁
assert 139 // 12 == 11 and 139 % 12 == 7 and 144 - 139 == 5
assert 1993 - 1989 + 1 == 5 and 65 - 56 == 9
print(f"10 1980年春开始交易时 34 岁 (距出生 {age_days} 天); 139 个月 = 11 年 7 个月, 距整 12 年差 5 个月; 1989-1993 连冠 5 年; 65 月连胜比 DiMaggio 56 场多 9 OK")

print("ALL PASS")
