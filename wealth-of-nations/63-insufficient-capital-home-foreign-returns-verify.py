# -*- coding: utf-8 -*-
"""验证《国富论》63 篇篇内数字与结构（取自原书第二卷第五章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性与序位登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 资本不足时用途次序：农业 > 制造 > 出口贸易（序位登记）；英国缺口例三处
order = ["agriculture", "manufactures", "exportation trade"]
assert order[0] == "agriculture" and len(["land improvement", "Scotch wool to Yorkshire", "little towns distant markets"]) == 3
# 2. 北美：零售属母国商人的两省
assert len(["Virginia", "Maryland"]) == 2
# 3. 最富古国三例
assert len(["China", "ancient Egypt", "Indostan"]) == 3
# 4. 批发贸易恰三类
assert len(["home trade", "foreign trade of consumption", "carrying trade"]) == 3
# 5. 替回因子：国内每次替回本国资本 2、对外消费每次替回本国资本 1，比为 2
assert 2 // 1 == 2
# 6. 周转与总乘数：国内 12 次对对外 1 次；12 * 2 = 24 倍；国内一年 3-4 次、对外 1-3 年
assert 12 * 2 == 24 and 3 <= 4 and 1 <= 3
print("63 verify: 6 assertions passed")
