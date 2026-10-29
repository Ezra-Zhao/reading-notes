#!/usr/bin/env python3
"""12 判断力与清晰思考篇验证：方向对速度、基础链条与拖延真相的代价（纯标准库，示意模型）。
验三件事：
1) 方向压过速度：日速只有 1、方向全对的人，一百天向目标走 100；
   日速 3 倍、方向偏 80 度的人，一百天只向目标走约 52.1——杠杆时代先选方向再谈快慢；
2) 基础链条：高级概念的掌握是基础环节的连乘，一环为零则全链为零，全环 0.95 也只剩约 0.857；
   死记的事实按遗忘曲线三十天只剩约 5.0%，能从基础重新推导则不靠单点记忆存活；
3) 拖延真相的代价：一摊每月缩水 5% 的生意，装看不见拖满十二个月只剩约 54.0，
   第一个月就承认并止损能保住 95.0——痛苦时刻来得越晚，账越贵。
参数为示意，只验证结构方向，不构成任何经营或投资建议。
"""
import math

# 1) 方向压过速度（向目标方向的投影才是有效进度）
right = 1 * math.cos(math.radians(0)) * 100
fast_wrong = 3 * math.cos(math.radians(80)) * 100
print(f"direction: right={right:.1f} fast_wrong={fast_wrong:.1f}")
assert right == 100.0, "方向全对、日速 1，一百天有效进度 100"
assert 52 < fast_wrong < 53, "三倍速度、方向偏 80 度，有效进度只剩约 52.1"
assert fast_wrong < right, "方向错时，三倍努力也追不上对方向的一倍努力"

# 2) 基础链条：连乘与遗忘
chain_full = 0.95 * 0.95 * 0.95
chain_broken = 0.95 * 0.0 * 0.95
memorized = math.exp(-0.1 * 30)
print(f"chain: full={chain_full:.3f} broken={chain_broken:.3f} memorized30d={memorized:.3f}")
assert abs(chain_full - 0.857) < 0.001, "三环各 0.95，连乘后高级概念只剩约 0.857"
assert chain_broken == 0.0, "基础有一环为零，再高级的概念也立不住"
assert memorized < 0.05 + 0.001, "只靠死记的事实，三十天后按示意遗忘曲线只剩约 5.0%"

# 3) 拖延真相的代价
ignored = 100 * 0.95 ** 12
faced_early = 100 * 0.95
print(f"reality: ignored={ignored:.1f} faced_early={faced_early:.1f}")
assert 54 < ignored < 55, "每月缩水 5% 拖满一年，100 只剩约 54.0"
assert faced_early == 95.0 and faced_early - ignored > 40, "第一个月就面对并止损，保住的比拖一年多 40 以上"

print("ALL CHECKS PASSED")
