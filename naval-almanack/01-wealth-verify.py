#!/usr/bin/env python3
"""01 财富篇验证：三件可算的事（纯标准库，clean-room 自写）。
1) 出租时间=线性收入 vs 持有资产=复利增长，十年尺度数量级对比
2) 免许可杠杆边际成本：多服务一个客户，劳动力 vs 代码/媒体的增量成本
3) 个人时薪决策表：省钱<时薪*耗时->忽略；外包价<时薪*耗时->外包；否则自己做
"""
# 1) 线性 vs 复利：年投 1000 小时、时薪 50 -> 每年 5 万，十年 50 万（不增长）
linear_10y = 50 * 1000 * 10
# 资产：初始投入等值 5 万，此后每年追加 5 万、年化 10% 复利
asset = 0.0
for _ in range(10):
    asset = (asset + 50000) * 1.10
print(f"linear_10y={linear_10y} asset_10y={asset:,.0f} ratio={asset/linear_10y:.2f}")
assert linear_10y == 500000
assert asset > linear_10y * 1.5, "复利十年应显著高于纯线性累计"

# 2) 边际复制成本：服务第 N 个客户的增量成本
def marginal_labor(n):   # 劳动力杠杆：每客户都要人时
    return 30.0
def marginal_code(n):    # 代码/媒体杠杆：增量趋近服务器分摊
    return 0.01
tot_lab = sum(marginal_labor(i) for i in range(10000))
tot_code = sum(marginal_code(i) for i in range(10000))
print(f"10k customers: labor_total={tot_lab:,.0f} code_total={tot_code:,.0f}")
assert tot_lab / tot_code > 1000

# 3) 个人时薪决策表（时薪 100）
RATE = 100
def decide(hours, saving, outsource_cost=None):
    value = RATE * hours
    if saving < value and (outsource_cost is None or outsource_cost >= value):
        # 省下的钱不值自己的时间、且外包也不划算 -> 忽略（书中规则）
        if saving < value:
            return "ignore" if outsource_cost is None else "ignore"
    if outsource_cost is not None and outsource_cost < value:
        return "outsource"
    return "do_it"
cases = [
    # (耗时, 自己修可省, 外包报价, 预期)
    (2, 50, None, "ignore"),       # 省50 < 2h*100 -> 忽略
    (2, 50, 80, "outsource"),      # 外包80 < 200 -> 外包
    (1, 500, 300, "do_it"),        # 省500 > 100，且外包300>100 -> 自己做最划算? 见下注
]
# 注：第三例按严格规则 outsource_cost(300) > value(100) 故不外包；saving(500)>value 故自己做
for h, s, o, exp in cases:
    got = decide(h, s, o)
    print(f"hours={h} saving={s} outsource={o} -> {got} (expect {exp})")
    assert got == exp, (h, s, o, got, exp)
print("ALL CHECKS PASSED")
