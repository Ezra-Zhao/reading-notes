# -*- coding: utf-8 -*-
"""《金钱心理学》第9章「财富是你看不见的那些」数字与结构命题复核（clean-room 自写脚本）。
复核的是正文断言的算术恒等与结构计数，不引用原文；
运动研究的倍数只验证其算术含义，不作独立统计引用。"""
# 1 豪车恒等式：买下 10 万美元的车之后，能确定的只有财富总额减少 10 万
#    （付现）或负债增加 10 万（贷款）——车是消费凭证，不是财富凭证
car_price = 100_000
wealth_before = 500_000  # 自设情景本金，只为演示恒等式
assert wealth_before - car_price == 400_000
debt_after_loan = 0 + car_price
assert debt_after_loan == 100_000
# 2 人们判断「富有」时能用的外在信号共 3 类：车子、房子、社交网络照片
signals = ["车子", "房子", "社交网络照片"]
assert len(signals) == 3
# 3 本章点名的「没买」共 5 类：豪车、钻石、手表、服装、没升级的头等舱座位
not_bought = ["豪车", "钻石", "手表", "服装", "头等舱座位"]
assert len(not_bought) == 5
# 4 「百万富翁」的歧义：想花掉 100 万 vs 拥有 100 万——
#    花完之后净资产归零，拥有则净资产仍是 100 万，两者恰好相反
million = 1_000_000
assert million - million == 0 and million - 0 == million
# 5 运动研究倍数（书中转述）：能量消耗估值高估 4 倍，运动后摄入约为实际消耗的 2 倍
#    设实际消耗 100 千卡：自以为消耗 400，实际吃回 200，净摄入 +100——锻炼被大餐抵消
actual_burn = 100
estimated_burn = actual_burn * 4
intake_after = actual_burn * 2
assert estimated_burn == 400 and intake_after == 200
assert intake_after - actual_burn == 100
# 6 流量与存量：收入相同、储蓄率不同，10 年后存量差距 = 年收入 x 储蓄率差 x 年数
income, years = 100_000, 10
stock_a = income * 0.30 * years  # 存下三成
stock_b = income * 0.05 * years  # 存下半成
assert stock_a - stock_b == 250_000
print("all 6 assertions passed")
