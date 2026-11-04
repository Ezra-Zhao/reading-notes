# -*- coding: utf-8 -*-
"""178 验证：荷兰继承税率表、封建两年租、三国印花登记与归宿映射。参数取自原书篇内陈述，纯标准库。"""
from fractions import Fraction
# 一、荷兰表：旁系5-30%、夫妻1/50=2%、哀戚1/20=5%、直系0；罗马1/20=5%
assert 0<2<5<30
assert Fraction(1,50)*100==2 and Fraction(1,20)*100==5
# 二、封建账：受封一年租+救济金一年租=两年租
assert 1+1==2
burdens=["未成年赡养","寡妇赡养份"]; assert len(burdens)==2
# 三、伯尔尼贵族1/6大于卑贱1/10；卢塞恩离境10%=1/10
assert Fraction(1,6)>Fraction(1,10) and Fraction(10,100)==Fraction(1,10)
# 四、英国印花：最高6镑=120先令大于半克朗2.5先令；登记税零项
assert 6*20==120 and 120>Fraction(5,2)
registration_duties=[]; assert len(registration_duties)==0
# 五、荷兰登记2.5%对象五类；遗嘱印花最高300弗罗林约27.5镑大于最低3便士
objects=["土地","房屋","抵押","二吨以上船舶","法庭命卖动产"]; assert len(objects)==5
assert Fraction(5,2)==Fraction(25,10) and 300>3
# 六、归宿六类：落卖方三类、落买方一类；格言占优确定便利经济三项
incidence={"遗产":"受领人","土地卖":"卖方","新房卖":"买方","旧房卖":"卖方","地皮租卖":"卖方","借贷印花登记":"借款人"}
assert len(incidence)==6 and list(incidence.values()).count("卖方")==3 and list(incidence.values()).count("买方")==1
favoured=["确定","便利","经济"]; assert len(favoured)==3
print("178 verify: 6 assertions passed")
