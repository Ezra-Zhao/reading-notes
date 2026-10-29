#!/usr/bin/env python3
"""06 杠杆篇验证：三种杠杆的放大方式不同（纯标准库，clean-room 自写，示意模型）。
验四件事：
1) 人力杠杆带协调成本：团队翻倍，净产出涨不到翻倍（次线性）；
2) 资本杠杆：同一个判断，部署的资本放大 10 倍，结果放大 10 倍、决策时间不变；
3) 代码/媒体杠杆：作者时间固定，边际复制成本近零，受众放大 1000 倍时总成本几乎不动；
4) 房产阶梯（原书自带数字）：体力工时薪 15 美元、总包一份合同 5 万美元、
   开发商一单利润 50 万美元起——同一项目里位置越高，单项目所得越高出两个量级；
5) 破产风险：每轮全押、单轮胜率六成，连押 10 轮的存活率跌破 1%。
参数为示意，只验证结构方向，不构成投资建议。
"""

# 1) 人力：毛产出 = 人数*8，协调成本随两两沟通线增长
def labor_net(n):
    return n * 8 - 0.25 * n * (n - 1)

net10, net20 = labor_net(10), labor_net(20)
print(f"labor: team10 net={net10:.0f} team20 net={net20:.0f} ratio={net20/net10:.2f} (<2x)")
assert net20 < 2 * net10, "人力翻倍但协调成本吃掉一部分，净产出次线性"

# 2) 资本：判断优势 2%，一次决策，资本 100 万对 1000 万
edge = 0.02
gain_small, gain_big = 1_000_000 * edge, 10_000_000 * edge
print(f"capital: 1M->{gain_small:,.0f} 10M->{gain_big:,.0f} (same 1 decision)")
assert gain_big == 10 * gain_small, "资本杠杆下同一判断的结果随资本线性放大"

# 3) 代码/媒体：创作 10 小时固定，服务成本每用户 0.001（近似零边际）
def media_cost(users):
    return 10 + users * 0.001  # 10 为创作小时折算的固定成本单位

c10, c10000 = media_cost(10), media_cost(10_000)
print(f"media/code: users 10 cost={c10:.1f} users 10000 cost={c10000:.1f} cost_ratio={c10000/c10:.1f} vs users_ratio=1000")
assert c10000 / c10 < 3, "受众放大 1000 倍，总成本只动一点——边际复制成本近零"
assert 10_000 / 10 == 1000

# 4) 房产阶梯：同一栋房子的维修/改造项目，四周工期
laborer_project = 15 * 40 * 4          # 时薪 15 美元、每周 40 小时、4 周
contractor_project = 50_000            # 原书：总包一份合同 5 万美元
developer_project = 500_000            # 原书：开发商一单利润 50 万至 100 万美元，取下限
print(f"ladder: laborer={laborer_project:,} contractor={contractor_project:,} developer={developer_project:,}")
assert laborer_project < contractor_project < developer_project
assert developer_project >= 10 * contractor_project, "阶梯每上一层，量级跳一档"

# 5) 破产风险：全押连押的存活率
survive = 0.6 ** 10
print(f"ruin: all-in 10 rounds at 60% win rate, survival={survive:.4f} (<1%)")
assert survive < 0.01, "再好的胜率，全押连押也会把存活率磨到近零——先避破产"

print("ALL CHECKS PASSED")
