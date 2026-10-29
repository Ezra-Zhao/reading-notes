#!/usr/bin/env python3
"""10 四种运气篇验证：平行宇宙检验、尝试次数、识别率与机会份额（纯标准库，示意模型）。
验四件事：
1) 平行宇宙检验：靠盲运的路径只在约 5% 的宇宙成功，品格与技能的可重复路径约 99.9%——
   对应原书「999 个对 50 个」的表述结构；
2) 跑出来的运气：至少命中一次的概率随尝试次数严格递增；
3) 看出来的运气：机会同样多时，能接住多少由识别率决定；
4) 被吸来的运气：成为唯一被想起的人，机会份额从平分变独占。
参数为示意，只验证结构方向，不构成任何收益承诺。
"""

# 1) 平行宇宙检验
luck_path, skill_path = 50 / 1000, 999 / 1000
print(f"universes: luck={luck_path:.3f} skill={skill_path:.3f} ratio={skill_path/luck_path:.1f}")
assert luck_path == 0.05 and skill_path == 0.999, "盲运路径约 5% 成功，可重复路径约 99.9%"
assert skill_path / luck_path > 19, "两种路径的成功宇宙数相差约二十倍"

# 2) 尝试次数与至少命中一次
def at_least_once(p, n):
    return 1 - (1 - p) ** n

p1, p100 = at_least_once(0.02, 1), at_least_once(0.02, 100)
print(f"hustle: n=1 {p1:.3f}  n=100 {p100:.3f}")
assert abs(p1 - 0.02) < 1e-9 and 0.86 < p100 < 0.87, "单次 2%，一百次升到约 86.7%"
assert at_least_once(0.02, 50) < p100, "尝试越多，至少命中一次的概率严格越大"

# 3) 识别率决定接住多少
chances = 100
expert, novice = chances * 0.9, chances * 0.1
print(f"spotting: expert={expert:.0f} novice={novice:.0f}")
assert expert / novice == 9, "识别率 90% 对 10%，同样一百次机会接住数相差九倍"

# 4) 唯一被想起的人的机会份额
share_crowd, share_unique = 1 / 100, 1.0
print(f"inbound: crowd={share_crowd:.2f} unique={share_unique:.2f}")
assert share_unique / share_crowd == 100, "从一百人平分到唯一人选，机会份额放大一百倍"

print("ALL CHECKS PASSED")
