#!/usr/bin/env python3
"""13 卸下身份与决策技能篇验证：决策的杠杆计价、成套信念的概率与启发法的适用边界（纯标准库，示意模型）。
验三件事：
1) 决策计价：管十亿美元的人，正确率只多十个百分点，一次判断的价值差就是一亿美元——
   对应原书「80% 对 70%、多对 10% 值一亿」的账，决策被杠杆计价、不按工时计价；
2) 成套信念可疑：十个本应独立判断的立场若全靠各自掷硬币，对齐成整齐一包的概率只有约 0.098%——
   信念整齐成套，更像是整包接收、不是逐条想过；
3) 启发法边界：偏见类捷径省下的时间是固定的（示意 100 美元），出错代价却随事情大小涨——
   一千美元的事多错 5% 只多亏 50、值得用捷径，一百万美元的事多亏 50,000、必须弃捷径慢慢想。
参数为示意，只验证结构方向，不构成任何经营或投资建议。
"""

# 1) 决策的杠杆计价
value_gap = 1_000_000_000 * (0.80 - 0.70)
print(f"decision value gap: {value_gap:,.0f}")
assert abs(value_gap - 100_000_000) < 1, "十亿美元盘子上多对十个百分点，价值差恰是一亿美元"

# 2) 成套信念的概率
bundle = 0.5 ** 10
print(f"bundle probability: {bundle:.4%}")
assert abs(bundle - 0.0009765625) < 1e-12, "十个独立立场全部同向对齐的概率只有约 0.098%"
assert bundle < 0.001, "整齐成套在独立判断下是千分之一级的小概率事件，值得高度怀疑"

# 3) 启发法的适用边界：省时固定、代价随规模涨
time_saved = 100
small_loss = 1_000 * 0.05
big_loss = 1_000_000 * 0.05
print(f"heuristic: saved={time_saved} small_extra_loss={small_loss:.0f} big_extra_loss={big_loss:.0f}")
assert small_loss == 50 and small_loss < time_saved, "小事上捷径多亏 50、省时 100，用捷径划算"
assert big_loss == 50_000 and big_loss > time_saved * 100, "大事上同一捷径多亏 50,000，是省时价值的五百倍，必须弃用"

print("ALL CHECKS PASSED")
