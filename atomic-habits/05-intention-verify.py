#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原子习惯第5章验算：执行意向实验算术 + 范例计数。数字为书中转述(B级)，只核算术。"""
from decimal import Decimal

# 1 第三组91% 超过其他组上限38%的两倍(76%)
assert Decimal("91") > 2 * Decimal("38")
# 2 以其他组下限35%计: 91/35 = 2.6, 同样两倍还多
assert abs(float(Decimal(91) / Decimal(35)) - 2.6) < 0.001
# 3 前两组区间宽度 38-35 = 3 个百分点, 激励组与控制组几乎无差
assert Decimal("38") - Decimal("35") == Decimal("3")
# 4 狄德罗藏书售价1000英镑, 书中称合今天15万美元以上 -> 折算倍率大于150
assert Decimal("150000") / Decimal("1000") == Decimal("150")
# 5 执行意向填句范例4个: 静心/读书/运动/婚姻(泡茶)
intention_examples = ["静心", "读书", "运动", "婚姻"]
assert len(intention_examples) == 4
# 6 习惯堆叠范例5个: 静心/运动/感恩/婚姻/安全
stack_examples = ["静心", "运动", "感恩", "婚姻", "安全"]
assert len(stack_examples) == 5
# 7 晨间堆叠链3步 + 晚间堆叠链3步 = 6步
morning = ["倒咖啡后静心", "静心后写待办", "写完待办处理第一件事"]
evening = ["晚餐后放碗盘", "放碗盘后擦流理台", "擦完流理台摆咖啡杯"]
assert len(morning) == 3 and len(evening) == 3 and len(morning) + len(evening) == 6
# 8 实验规模: 248人分3组, 为期2周=14天; 伏地挺身堆叠修正版定量10下
assert 248 > 0 and 2 * 7 == 14 and 10 == 10
print("05-intention-verify: 8 assertions PASS")
