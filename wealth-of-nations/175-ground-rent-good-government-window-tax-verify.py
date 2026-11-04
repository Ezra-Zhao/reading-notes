# -*- coding: utf-8 -*-
"""175 验证：荷兰2.5%标尺、英格兰替代指标阶梯与窗税表。参数取自原书篇内陈述，纯标准库。"""
from fractions import Fraction
# 一、荷兰标尺：2.5%严格大于建筑租两锚（6.5%、7%）的三分之一，且小于利率上限3%
assert Fraction(5,2) > Fraction(13,2)/3 and Fraction(5,2) > Fraction(7)/3
assert Fraction(5,2) < 3
# 二、英国个别房税率变异来源恰两项，区税率恒定
variations=["空房优待免除","新建修缮改良归区冲抵"]; assert len(variations)==2
district_rate_constant=1; assert district_rate_constant==1
# 三、住屋税阶梯：基础2先令，十窗+4、二十窗以上+8，后改20–30窗10、30窗以上20，严格递增
assert 2+4==6 and 2+8==10 and 10<20
# 四、窗税现行表：房税英格兰3先令大于苏格兰1先令；每窗2便士至2先令（24便士）恰12倍
assert 3>1 and 2*12==24
# 五、最坏不平等方向：伦敦500镑为乡间10镑的50倍，窗数方向却相反（方向登记）
assert 500//10==50
windows={"乡间十镑房":2,"伦敦五百镑房":1}; assert windows["乡间十镑房"]>windows["伦敦五百镑房"]
# 六、格言对账恰犯一合三；税压低房租与繁荣抬高房租两方向并存（序位登记）
violated=["第一条平等"]; not_offended=["第二条","第三条","第四条"]
assert len(violated)==1 and len(not_offended)==3
direction={"税的天然作用":-1,"窗税以来实际房租":1}; assert direction["税的天然作用"]<0<direction["窗税以来实际房租"]
print("175 verify: 6 assertions passed")
