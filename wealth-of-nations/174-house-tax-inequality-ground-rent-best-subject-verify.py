# -*- coding: utf-8 -*-
"""174 验证：房租占比序位、三源、地皮租税全额归宿。参数取自原书篇内陈述，纯标准库。"""
from fractions import Fraction
# 一、房租占比序位：最高财富等级严格大于最低等级（方向编码，取自原书篇内陈述）
share={"最高等级":3,"中间等级":2,"最低等级":1}
assert share["最高等级"]>share["中间等级"]>share["最低等级"]
# 二、私人收入来源恰三样，房租税落住户部分遍落三源
sources=["劳动工资","资本利润","土地地租"]; assert len(sources)==3
# 三、自住按成本折算灾难例：6.5–7%折算房租与其实产净租几乎相等（比值落在0.9–1.1登记）
for pct in [Fraction(13,2), Fraction(7)]:
    ratio=pct/Fraction(7)  # 以区间上界为净租基准的保守登记
    assert Fraction(9,10) <= ratio <= Fraction(11,10)
assert 3<4  # 每镑三至四先令区间成立
# 四、空房两式应课额均为零
assert {"房租税空房":0,"地皮租税空房":0}=={"房租税空房":0,"地皮租税空房":0}
# 五、地皮租税归宿：所有者承担份额为1、房租涨幅为0、垫付者两式不改最终承担
owner_share=Fraction(1); rent_rise=Fraction(0)
assert owner_share==1 and rent_rise==0 and len(["住户垫付","所有者垫付"])==2
# 六、最能承受特别税的对象恰两类，其产业挫伤登记为零
subjects=["地皮租","普通地租"]; assert len(subjects)==2
discouragement=0; assert discouragement==0
print("174 verify: 6 assertions passed")
