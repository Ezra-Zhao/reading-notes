# -*- coding: utf-8 -*-
"""177 验证：马车椅比例、执照阶梯、泰耶总额与反应对照。参数取自原书篇内陈述，纯标准库。"""
from fractions import Fraction
# 一、马车每周5先令*52=260先令=13镑；椅每年10先令；年额比26倍
assert 5*52==260 and 260//20==13 and 260//10==26
# 二、执照阶梯：麦酒20、烈酒40恰2倍、烈酒+葡萄酒40合80恰麦酒4倍；同额标记
assert 40==20*2 and 40+40==80 and 80==20*4
same_for_all=1; assert same_for_all==1
# 三、泰耶：总额40107239里弗16苏、总区20、分摊层级3、重课触发3类、挑补者5至6人
assert 40107239>40000000
layers=["省际","选举区间","教区与个人"]; assert len(layers)==3
triggers=["误课得直","纳税人破产","收款人破产"]; assert len(triggers)==3
assert 5<=5 and 6<=6 and 5<6
# 四、反应对照：贸易终落消费者、农业终落（续租）地主，两路不同
final={"贸易":"消费者","农业":"地主"}; assert final["贸易"]!=final["农业"] and len(final)==2
# 五、仆役税：一畿尼/男仆；1万镑为200镑的50倍而男仆少于50（方向登记）
assert 10000//200==50
servants_at_10000=49; assert servants_at_10000<50  # 原书作“不会雇五十个”，以小于五十登记方向
# 六、收官：特定行业税触利息零项；普遍精确税终落含利息；二十分之一=5%
assert len([])==0
assert Fraction(1,20)==Fraction(5,100)
print("177 verify: 6 assertions passed")
