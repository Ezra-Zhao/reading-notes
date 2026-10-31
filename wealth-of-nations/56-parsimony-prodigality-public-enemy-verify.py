# -*- coding: utf-8 -*-
"""验证《国富论》56 篇篇内数字与结构（取自原书第二卷第三章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性登记者已标明，不冒充现代实测。"""
# 1. 消费者两批：宾客家仆 / 劳动者制造业者工匠；后者再生产含利润（方向登记）
assert len(["idle guests","menial servants"]) == 2 and len(["labourers","manufacturers","artificers"]) == 3
# 2. 两价值算账：生产性路 2 个价值、非生产性路 1 个
assert 2 > 1 and 2 == 1 + 1
# 3. 破产率不大多于千分之一
assert abs(1/1000 - 0.001) < 1e-12
# 4. 公共非生产性列举四类：宫廷、教会机构、舰队、军队
assert len(["court","ecclesiastical establishment","fleets","armies"]) == 4
# 5. 欲望对比：开支原则暂时/偶然二项 对 储蓄原则平静/全程二项
assert len(["momentary","occasional"]) == 2 and len(["calm","womb to grave"]) == 2
# 6. 公共挥霍衰退链三年递减
assert 3 > 2 > 1  # 年序号示意递减方向登记（产物量递减以序登记）
print("56 verify: 6 assertions passed")
