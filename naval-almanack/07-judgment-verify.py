#!/usr/bin/env python3
"""07 判断力篇验证：小幅判断优势经杠杆复利放大（纯标准库，clean-room 自写，示意模型）。
验三件事：
1) 判断正确率 85% 对 75%：单次决策的期望收益差只有 0.4 个百分点，
   但在一笔大资本上连做 50 次决策后，终值差距拉开到 20% 以上；
2) 这段差距折算成钱，远大于原书所说「为 10 个百分点的判断优势付 5000 万美元也值」的量级；
3) 按判断收费与按工时收费的脱钩：判断者的收入不随工时变，工时者的收入随工时线性变。
参数为示意，只验证结构方向，不构成投资建议。
"""

BASE = 1_000_000_000  # 十亿美元量级的「船」（原书口径为千亿美元级航母，此处缩小示意）
DECISIONS = 50
STAKE = 0.02  # 每次决策对/错带来 +2% / -2%

def final_value(p):
    per_decision = (2 * p - 1) * STAKE  # 期望单次收益：85%->+1.4%，75%->+1.0%
    return BASE * (1 + per_decision) ** DECISIONS

v85, v75 = final_value(0.85), final_value(0.75)
print(f"judgment: p85 final={v85:,.0f} p75 final={v75:,.0f} ratio={v85/v75:.3f}")
assert v85 / v75 > 1.20, "10 个百分点的判断优势经 50 次决策复利后终值差超 20%"

gap = v85 - v75
print(f"value gap={gap:,.0f} vs a 50,000,000 judgment fee -> gap/fee={gap/50_000_000:.1f}x")
assert gap > 50_000_000 * 3, "判断优势创造的价值差数倍于为它支付的高额报酬，付费仍划算"

# 按判断收费 vs 按工时收费：同样一周，5 小时与 40 小时
judgment_fee = 200_000  # 按成果/判断计价，与投入工时无关（示意）
hourly = lambda h: 100 * h
print(f"decoupled: judgment pay 5h={judgment_fee:,} 40h={judgment_fee:,}; hourly pay 5h={hourly(5):,} 40h={hourly(40):,}")
assert hourly(40) == 8 * hourly(5), "工时收入随工时线性变"
# 判断计价在两种工时下不变——脱钩本身即断言对象，用常量对照表达
assert judgment_fee > hourly(40), "示意量级下，单个关键判断的定价高于整周工时收入"

print("ALL CHECKS PASSED")
