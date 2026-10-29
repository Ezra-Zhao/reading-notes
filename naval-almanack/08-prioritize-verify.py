#!/usr/bin/env python3
"""08 优先级与专注篇验证：时薪线、大决定与零和/正和之分（纯标准库，clean-room 自写，示意模型）。
验三件事：
1) 时薪决策线：把自己的时间标了价之后，跨城一小时只为省小钱的动作在账面上直接是亏的；
   低于时薪线能外包的事，外包在账面上直接是赚的；
2) 大决定的支配性：住哪座城、做哪份工、和谁在一起这类轨迹级决定的 10% 轨迹差，
   10 年复利后放大到约 2.6 倍，量级远超日常小优化；
3) 地位零和、财富正和：五个人争排名，名次总和恒定，有人升必有人降；
   同样五个人做正和交易，蛋糕可以整体变大、人人所得同时上升。
参数为示意，只验证结构方向，不构成财务建议。
"""

# 1) 时薪线：时薪标价 100 美元（示意）
rate = 100
drive_cost = 1.0 * rate          # 跨城往返 1 小时的时间成本
drive_saving = 30                # 这一趟省下的钱
print(f"hourly: drive 1h cost={drive_cost:.0f} saving={drive_saving} net={drive_saving-drive_cost:.0f}")
assert drive_saving - drive_cost < 0, "按时薪线算账：为省 30 美元花掉价值 100 美元的一小时，是亏的"

outsource_cost, outsource_hours = 40, 1.0   # 花 40 美元请人做 1 小时的事
print(f"hourly: outsource cost={outsource_cost} frees value={outsource_hours*rate:.0f} net={outsource_hours*rate-outsource_cost:.0f}")
assert outsource_hours * rate - outsource_cost > 0, "外包价格低于时薪线时，外包是赚的"

# 2) 大决定：轨迹好 10% 的人生路径，10 年复利
good, base = 1.10 ** 10, 1.00 ** 10
print(f"big decision: 10y trajectory x{good:.2f} vs x{base:.2f} ratio={good/base:.2f}")
assert good / base > 2.5, "轨迹级决定的小差距经时间复利放大到数倍——值得花一两年去选"

# 3a) 地位零和：5 人名次 1..5，总和恒定
ranks_before = [1, 2, 3, 4, 5]
ranks_after = [2, 1, 3, 4, 5]    # 第 2 名升到第 1 名，第 1 名必须让位
print(f"status: rank sum before={sum(ranks_before)} after={sum(ranks_after)}")
assert sum(ranks_before) == sum(ranks_after), "地位是零和的：总和不变，一人上升必有一人下降"

# 3b) 财富正和：5 人各自创造，蛋糕整体变大、人人变多
wealth_before = [10, 10, 10, 10, 10]
wealth_after = [14, 13, 15, 12, 16]
print(f"wealth: total before={sum(wealth_before)} after={sum(wealth_after)} all_up={all(a>b for a,b in zip(wealth_after, wealth_before))}")
assert sum(wealth_after) > sum(wealth_before) and all(a > b for a, b in zip(wealth_after, wealth_before)), "财富可以是正和的：总量变大且人人同时变多"

print("ALL CHECKS PASSED")
