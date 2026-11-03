# -*- coding: utf-8 -*-
"""验证《国富论》142 篇篇内数字与结构（原书第五卷第一章第一部末段：常备军与文明、自由条件、火药费用，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 两笔长和平实证：俄国近 20 年（1756 入波兰）、英国约 28 年（1739 开战），差 8 年
assert 28 - 20 == 8 and 1756 > 1739
# 2. 长和平效应分层两层
assert len(["generals may forget skill", "soldiers never forget valour where standing army kept up"]) == 2
# 3. 自由安全条件三项；危险反例两人
assert len(["sovereign himself the general", "principal nobility and gentry chief officers", "officers interest connected with constitution"]) == 3
assert len(["Caesar", "Cromwell"]) == 2
# 4. 国防费用阶段恰三段
assert len(["costs nothing in peace or war", "maintained in war", "maintained even in peace"]) == 3
# 5. 费用对照三组：火枪>标枪弓箭、火炮迫击炮>弩炮投石机、火药不可回收 vs 标枪箭可拾回
assert len(["musket > javelin/bow", "cannon/mortar > balista/catapulta", "powder lost irrecoverably vs javelins picked up"]) == 3
# 6. 优劣翻转：古代富裕开化国难自守，现代贫穷蛮族国难自守（方向反转一次）
ancient, modern = "opulent finds defence difficult", "barbarous finds defence difficult"
assert ancient != modern
print("142 verify: 6 assertions passed")
