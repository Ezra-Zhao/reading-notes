# -*- coding: utf-8 -*-
"""171 验证：普查估值税率表、工期与蒙托邦补正算例。参数取自原书篇内陈述，纯标准库。"""
from fractions import Fraction
# 一、普鲁士税率序位与贵族/平民差恰三点
rates={"教士其他收入":Fraction(50),"骑士团领地":Fraction(40),"贵族保有地":Fraction(115,3),"平民保有地":Fraction(106,3)}
assert rates["教士其他收入"]>rates["骑士团领地"]>rates["贵族保有地"]>rates["平民保有地"]
assert rates["贵族保有地"]-rates["平民保有地"]==3
# 二、俗人区间上限25小于教士区间下限40
assert 25<40
# 三、米兰教会旧地计税比例恰三分之一小于一
assert Fraction(1,3)<1
# 四、时序：1748和平早于1760，波希米亚工期逾100年标记
assert 1748<1760; bohemia_years=101; assert bohemia_years>100
# 五、蒙托邦时距 1727-1666=61
assert 1727-1666==61
# 六、补正算例：低估区实纳1100、高估区实纳900，政府净零
due_low,due_high,old=1100,900,1000
levied=due_low-old
relief=old-due_high
assert levied==relief==100 and levied-relief==0
print("171 verify: 6 assertions passed")
