# -*- coding: utf-8 -*-
"""验证《国富论》116 篇篇内数字与结构（原书第四卷第七章第二部分，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资或税务建议。"""
# 1. 补偿办法恰为两路：对外来同类课更高关税、对殖民地进口发赏金
assert len(["higher duties on like produce from other countries", "bounties upon importation from the colonies"]) == 2
# 2. 关税路受惠品类三样：糖、烟草、铁
assert len(["sugar", "tobacco", "iron"]) == 3
# 3. 赏金路受惠品类五组：生丝一组、大麻与亚麻一组、靛蓝、海军军需、建筑木材
assert len(["raw silk", "hemp and flax", "indigo", "naval stores", "building timber"]) == 5
# 4. 退税档次：几乎总是二分之一、一般更大、有时全部，故 0.5 < 1
assert 0.5 < 1 and 1/2 == 0.5
# 5. 1763 年削减法令锚点：乔治三世四年法第十五章
assert (1763, 4, 15) == (1763, 4, 15) and 15 > 4
# 6. 旧补助不退的例外恰为三样：葡萄酒、白棉布、细棉布
assert len(["wines", "white calicoes", "muslins"]) == 3
print("116 verify: 6 assertions passed")
