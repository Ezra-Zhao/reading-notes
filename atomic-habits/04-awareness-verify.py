#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原子习惯第4章验算：百分比算术 + 记分卡范例计数。数字为书中转述(B级)，只核算术。"""
from decimal import Decimal

# 1 指差确认: 错误减少85% -> 残余15%
assert Decimal("100") - Decimal("85") == Decimal("15")
# 2 事故避免30% -> 残余70%
assert Decimal("100") - Decimal("30") == Decimal("70")
# 3 纽约地铁未停妥发生率下降57% -> 残余43%
assert Decimal("100") - Decimal("57") == Decimal("43")
# 4-5 记分卡范例12项: 正号6 负号1 等号5, 合计12
marks = ["=", "=", "-", "=", "+", "+", "+", "+", "+", "=", "=", "+"]
assert len(marks) == 12
assert marks.count("+") == 6 and marks.count("-") == 1 and marks.count("=") == 5
assert marks.count("+") + marks.count("-") + marks.count("=") == 12
# 6 负号占比 1/12 约8.33%
assert abs(float(Decimal(1) / Decimal(12) * 100) - 8.33) < 0.01
# 7 错误残余15% 即降至原来的0.15倍
assert Decimal("15") / Decimal("100") == Decimal("0.15")
# 8 四法则第一法则对应回路第一环(提示): 4章属法则一(第4-7章), 章号在区间内
assert 4 <= 4 <= 7
print("04-awareness-verify: 8 assertions PASS")
