#!/usr/bin/env python3
"""04 担责篇验证：公开可问责记录如何放大可达杠杆（纯标准库，clean-room 自写，示意模型）。
规则：信任分按每期成败更新（成 +0.06，败 -0.10，下限 0、上限 1）；
可达杠杆上限 = 1 + 99 * 信任分（无记录基线恒为 1，即只能动用自己的资源）。
同一串成败序列下，对比「记在名下」与「匿名不累积」两条轨迹。
参数为示意，只验证方向，不冒充实证。
"""
import random

SEQ_SEED = 42
PERIODS = 40
rng = random.Random(SEQ_SEED)
# 固定一串成败：胜率 65%，体现「大体靠谱、偶有失败」的真实记录
outcomes = [rng.random() < 0.65 for _ in range(PERIODS)]

trust = 0.10
named_leverage = []
for ok in outcomes:
    trust = min(1.0, max(0.0, trust + (0.06 if ok else -0.10)))
    named_leverage.append(1 + 99 * trust)

anon_leverage = [1.0] * PERIODS  # 匿名参与：记录不累积，杠杆上限不变

print(f"periods={PERIODS} wins={sum(outcomes)}")
print(f"named_final_trust={trust:.2f} named_final_leverage={named_leverage[-1]:.1f}x")
print(f"anon_final_leverage={anon_leverage[-1]:.1f}x")
print(f"named_peak_leverage={max(named_leverage):.1f}x")

assert named_leverage[-1] > anon_leverage[-1] * 5, "可问责记录应带来杠杆上限的系统性差距"
assert max(named_leverage) > 50, "长期靠谱记录应解锁数量级更大的杠杆"
# 失败确实扣信任（双刃剑的另一面）：找到一次失败后信任应低于失败前
first_fail = outcomes.index(False)
t_before = 0.10
tr = 0.10
for ok in outcomes[: first_fail + 1]:
    tr = min(1.0, max(0.0, tr + (0.06 if ok else -0.10)))
assert tr < 0.10 + 0.06 * first_fail, "失败期信任应被扣减"
print("ALL CHECKS PASSED")
