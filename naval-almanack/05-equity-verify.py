#!/usr/bin/env python3
"""05 股权篇验证：工资线性对股权非线性（纯标准库，clean-room 自写，示意模型）。
情景：年薪 20 万、每年全额计入，十年累计；
对照：以十年工资的一小部分本金持有一门温和增长生意 10% 股权
（初始估值 100 万、年增 12%），比较终值与「停工一年」的收入差。
参数为假设值，只验证结构方向，不构成投资建议。
"""
SALARY = 200_000
YEARS = 10
wage_total = SALARY * YEARS

# 股权：初始投入 10 万买 10%（估值 100 万），生意年增 12%，十年后卖出对应份额
stake, growth = 0.10, 0.12
value = 1_000_000.0
for _ in range(YEARS):
    value *= 1 + growth
equity_final = value * stake

print(f"wage_10y_total={wage_total:,} (linear, stops when you stop)")
print(f"business_value_10y={value:,.0f} equity_10y={equity_final:,.0f} on initial 100,000")
assert wage_total == 2_000_000
assert equity_final > 100_000 * 2.5, "温和复利十年后股权应数倍于本金"

# 停工一年情景：工资收入归零；股权对应生意仍在增长（不依赖本人到岗）
wage_year_off = 0
equity_year_gain = value * growth * stake  # 第十一年生意增值中归属本人的部分
print(f"year_off: wage_income={wage_year_off} equity_value_gain={equity_year_gain:,.0f}")
assert wage_year_off == 0 and equity_year_gain > 0, "停工时工资停摆、股权仍增值"
print("ALL CHECKS PASSED")
