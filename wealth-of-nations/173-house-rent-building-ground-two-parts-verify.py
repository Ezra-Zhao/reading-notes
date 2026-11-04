# -*- coding: utf-8 -*-
"""173 验证：建筑租双锚、房租税六十镑算例与最终分担。参数取自原书篇内陈述，纯标准库。"""
from fractions import Fraction
# 一、建筑租双锚：利率4%时6–6.5%、5%时7–7.5%，替回余量两锚同为2–2.5点
for rate, lo, hi in [(Fraction(4), Fraction(6), Fraction(13,2)), (Fraction(5), Fraction(7), Fraction(15,2))]:
    assert lo-rate==2 and hi-rate==Fraction(5,2)
# 二、税率换算：每镑四先令（每镑20先令）合五分之一
assert Fraction(4,20)==Fraction(1,5)
# 三、六十镑算例：60房加税合72、超12；50房加10税恰60，放弃档差10
assert 60+60//5==72 and 72-60==12 and 50+50//5==60 and 60-50==10
# 四、竞争方向：各档减弱、唯最低档一时增强（方向登记）
competition={"六十镑档":-1,"五十镑档":-1,"其余各档":-1,"最低档":1}
assert competition["最低档"]>0 and competition["六十镑档"]<0
# 五、长期归宿：租金削减落建筑租份为0、全归地皮租
building_share=Fraction(0); ground_share=Fraction(1)
assert building_share==0 and ground_share==1
# 六、最终分担方恰两方，建筑租不在其内
payers=["住户","地面所有者"]; assert len(payers)==2 and "建筑租" not in payers
print("173 verify: 6 assertions passed")
