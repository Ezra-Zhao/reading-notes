#!/usr/bin/env python3
"""03 长期游戏验证（纯标准库，clean-room 自写，参数均为示意模型）。
1) 复利时间不对称：年投 1 万、年化 8%，连续 30 年 vs 每 10 年清零重来
2) 重复博弈简化模型：让利者 vs 计较者，机会按信任度分配，100 轮累计机会
"""
def fv(years, annual=10000, r=0.08):
    v = 0.0
    for _ in range(years):
        v = (v + annual) * (1 + r)
    return v
stay = fv(30)
restart = fv(10)  # 三次重来，只剩最后一个 10 年的成果（前两次清零）
print(f"stay30={stay:,.0f} restart_last10={restart:,.0f} ratio={stay/restart:.2f}")
assert stay > restart * 3

# 2) 信任博弈：信任分随让利行为增长；每轮机会数 = 基础1 + 信任分//10
import random
random.seed(7)
def run(generous):
    trust, opps = 0, 0
    for _ in range(100):
        opps += 1 + trust // 10
        trust += 3 if generous else 0   # 让利每轮 +3 信任；计较者不增长
        if not generous and random.random() < 0.05:
            trust = max(0, trust - 5)   # 计较者偶发信任损耗
    return opps
g, s = run(True), run(False)
print(f"generous_opps={g} stingy_opps={s}")
assert g > s * 2, "让利者经信任复利应拿到数倍机会（方向性验证）"
print("ALL CHECKS PASSED")
