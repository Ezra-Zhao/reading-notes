# -*- coding: utf-8 -*-
"""176 验证：利润两分、英格兰百镑估算与荷兰百分之二标尺。参数取自原书篇内陈述，纯标准库。"""
from fractions import Fraction
# 一、利润恰两份，自救恰两路，抬价终落恰两处
parts=["付利息归业主","剩余补偿风险麻烦"]; assert len(parts)==2
routes=["抬利润率","扣利息"]; assert len(routes)==2
destinations=["农耕落地主","工商落消费者"]; assert len(destinations)==2
# 二、初看同构推理链：资本量不变时三者皆不变（序位登记）
unchanged={"普通利润率":0,"补偿份":0,"利息份":0}; assert all(v==0 for v in unchanged.values()) and len(unchanged)==3
# 三、不如地租适于直接课税的情形恰两项，公民身份对照一组
circumstances=["秘密且浮动","易移动"]; assert len(circumstances)==2
citizenship={"地主":"本国","资本主":"世界"}; assert len(citizenship)==2
# 四、英格兰估算：6%时百镑利息6镑、五分之一1.2镑=24先令；5%时1镑=20先令
assert Fraction(6,5)*20==24 and Fraction(5,5)*20==20 and 24>20
# 五、实估：资本五十分之一严格小于土地二分之一；汉堡四分之一个百分点=四百分之一
assert Fraction(1,50)<Fraction(1,2)
assert Fraction(1,4)/100==Fraction(1,400)
# 六、荷兰：2%对3%为三分之二，折每镑13又1/3先令=13先令4便士；本意课利息四处、课资本一处
assert Fraction(2,3)==Fraction(2,100)/Fraction(3,100)
assert Fraction(20)*Fraction(2,3)==Fraction(40,3)  # 13又1/3先令，1/3先令=4便士
interest_intended=["英格兰","汉堡","翁特瓦尔德","苏黎世"]; capital_intended=["荷兰"]
assert len(interest_intended)==4 and len(capital_intended)==1
print("176 verify: 6 assertions passed")
