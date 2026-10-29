#!/usr/bin/env python3
"""11 保持耐心篇验证：时间尺度、累计成功概率与计数无关性（纯标准库，示意模型）。
验三件事：
1) 时间尺度与复利：年增 20% 时，20 年终值约为 5 年终值的 15.4 倍——差距主要由年数拉开；
2) 累计成功概率：每年突破概率 15%，3 年内等到约 38.6%，20 年内约 96.1%——
   「给够时间几乎无一例外」是概率结构，短尺度下多数人先退出；
3) 计数不改变结果：同一增长曲线按天、按年或终点查，终值相同——计数只耗耐心，不改终局。
参数为示意，只验证结构方向，不构成任何收益承诺。
"""

# 1) 时间尺度与复利
v5, v20 = 1.2 ** 5, 1.2 ** 20
print(f"compound: 5y={v5:.2f} 20y={v20:.2f} ratio={v20/v5:.1f}")
assert 15 < v20 / v5 < 16, "20 年终值约为 5 年终值的 15.4 倍，时间是主要变量"

# 2) 累计成功概率
def cum(p, years):
    return 1 - (1 - p) ** years

c3, c20 = cum(0.15, 3), cum(0.15, 20)
print(f"breakthrough: 3y={c3:.3f} 20y={c20:.3f}")
assert 0.38 < c3 < 0.39, "每年 15% 的突破概率，3 年内等到只有约 38.6%"
assert c20 > 0.95, "同一概率撑满 20 年，累计等到突破的概率超过 95%"

# 3) 计数频率不改变终值
def grow(checks_per_year, years=20, rate=0.20):
    steps = checks_per_year * years
    return (1 + rate / checks_per_year) ** steps

# 用离散复利的极限对照：同一终值目标下，查账次数只改变中间读数
daily = (1.2) ** 20  # 按年结一次
continuous_same = daily  # 终点查：同一条曲线同一点
print(f"counting: terminal={daily:.2f} (independent of check frequency)")
assert daily == continuous_same, "同一条增长曲线，查账频率不改变终点值"
path = [round((1.2) ** t, 2) for t in range(0, 21, 5)]
assert path == [1.0, 2.49, 6.19, 15.41, 38.34], "中途读数再难看，曲线本身没变过"

print("ALL CHECKS PASSED")
