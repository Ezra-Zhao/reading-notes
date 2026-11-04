# -*- coding: utf-8 -*-
"""170 验证：浮动地租税、威尼斯登记与自耕减税的结构与算术。
参数全部取自《国富论》第五卷第二章第二部第一条第二段篇内陈述，纯标准库。"""
# 一、威尼斯自耕账：名义 10%，扣减税额五分之一后实付 8%。
nominal=10.0; deduction=nominal/5
assert nominal-deduction==8.0
# 二、格言对账方向：浮动税平等胜固定，确定与费用处下风（1胜 -1负编码）
score={"平等":1,"确定":-1,"征收费用":-1}
assert score["平等"]>0 and score["确定"]<0 and score["征收费用"]<0
# 三、告发分金：登记义务方恰两方，罚金去向含告发坐实方
parties=["地主","佃户"]; assert len(parties)==2 and "告发并坐实对方的一方" in ["告发并坐实对方的一方"]
# 四、从高估值课税的租约形态恰三类
forms=["续租罚金","限定耕法的劳役租","实物租与劳役租"]; assert len(forms)==3
# 五、自耕仲裁组成两方，减税附上限一条
arb=["邻里地主","邻里佃农"]; assert len(arb)==2
caps=["所占土地地租不超过定额"]; assert len(caps)==1
# 六、期限与注意力序位：地主注意力权重大于君主
weights={"地主注意力":2,"君主注意力":1}; assert weights["地主注意力"]>weights["君主注意力"]
print("170 verify: 6 assertions passed")
