#!/usr/bin/env python3
"""09 像玩一样的工作篇验证：退休三条路、生活方式不升级与玩的时长账（纯标准库，示意模型）。
验三件事：
1) 退休第一条路（被动收入覆盖开支）：年开支 6 万美元、示意回报 5% 时需要本金 120 万美元；
   开支减半，所需本金也减半——压开支和攒本金是同一道题的两边；
2) 退休第二条路（开支压到近零）：开支趋近于零时，所需本金趋近于零；
3) 生活方式不升级：收入翻倍时生活固定，储蓄额涨数倍；生活同步升级，储蓄率原地不动；
4) 玩的时长账：当作玩的事一周能做 16 小时乘 7 天，当作苦工的事一周 8 小时乘 5 天，
   前者周投入是后者的 2.8 倍——不靠天赋，靠可持续时长就拉开距离。
参数为示意（回报率、开支、时薪均为演示数），只验证结构方向，不构成财务建议。
"""

# 1) 被动收入覆盖开支
burn, ret = 60_000, 0.05
need = burn / ret
need_half = (burn / 2) / ret
print(f"retire-1: burn={burn} need={need:,.0f}; burn halved need={need_half:,.0f}")
assert need == 1_200_000 and need_half == need / 2, "所需本金与年开支成正比：开支减半，本金门槛减半"

# 2) 开支趋零则门槛趋零
print(f"retire-2: burn->0 need={0 / ret:,.0f}")
assert 0 / ret == 0, "开支压到零，财务门槛同步归零——出家式退休在账面上成立"

# 3) 生活方式升级与否
income_1, income_2 = 80_000, 160_000
save_fixed = income_2 - 50_000          # 生活固定在 5 万美元开支
save_creep = income_2 - 100_000         # 生活随收入同步翻倍到 10 万美元
save_before = income_1 - 50_000
print(f"lifestyle: save before={save_before:,} fixed={save_fixed:,} creep={save_creep:,}")
assert save_fixed == 110_000 and save_fixed > 3 * save_before, "收入翻倍而生活固定，储蓄额涨到原来的三倍以上"
assert save_creep / income_2 == save_before / income_1, "生活同步升级时，储蓄率原地不动——涨薪被生活吃掉"

# 4) 玩的时长账
play_week, work_week = 16 * 7, 8 * 5
print(f"play: hours/week play={play_week} work={work_week} ratio={play_week/work_week:.1f}")
assert play_week / work_week == 2.8, "把工作过成玩的人，一周可持续投入是苦工模式的 2.8 倍"

print("ALL CHECKS PASSED")
