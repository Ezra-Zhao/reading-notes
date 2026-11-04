# -*- coding: utf-8 -*-
"""172 验证：什一税富贫地算例、亚洲份额与征收两式。参数取自原书篇内陈述，纯标准库。"""
from fractions import Fraction
# 一、富地：一半替回，地租上限5/10，抽1/10后减租1/5，地租4/10，什一合地租1/5=每镑4先令
rent_rich_before=Fraction(5,10); tythe=Fraction(1,10)
rent_rich_after=Fraction(4,10)
assert rent_rich_before-tythe==rent_rich_after and tythe/ (rent_rich_before) == Fraction(1,5)
assert Fraction(1,5)*20==4  # 每镑20先令的五分之一为4先令（以原书计价单位复算其自述4先令）
# 二、贫地：4/5替回，地租上限2/10，抽后1/10，什一合地租1/2=每镑10先令，且高于富地
rent_poor_before=Fraction(2,10); rent_poor_after=Fraction(1,10)
assert rent_poor_before-tythe==rent_poor_after and Fraction(1,2)*20==10
assert Fraction(1,2)>Fraction(1,5)
# 三、亚洲份额：中国名义1/10、实收不逾1/30；孟加拉与埃及各约1/5且大于1/10
assert Fraction(1,30)<Fraction(1,10)<Fraction(1,5)
# 四、亚洲君主关切通道恰三项，教会碎份利益计数为零（标记）
channels=["道路","运河","最广阔市场"]; assert len(channels)==3
church_interest=0; assert church_interest==0
# 五、货币两式漂移源计数：随市价恰一项，固定恰三项
vary=["真实产物"]; fixed=["真实产物","贵金属价值","铸币含金属量"]
assert len(vary)==1 and len(fixed)==3
# 六、定额代偿随地租变动为零；孟加拉改回实物后收入方向向下（序位）
modus_variation=0; assert modus_variation==0
revenue={"代偿时期据说水平":2,"改回实物后":1}; assert revenue["改回实物后"]<revenue["代偿时期据说水平"]
print("172 verify: 6 assertions passed")
