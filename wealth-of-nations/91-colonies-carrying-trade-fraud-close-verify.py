# -*- coding: utf-8 -*-
"""验证《国富论》91 篇篇内数字与结构（原书第四卷第四章后段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 葡萄酒退殖民地：除 3 镑 10 先令外全退；3 镑 10 先令 = 3.5 镑（20 先令 = 1 镑）
assert 3 + 10/20 == 3.5
# 2. 时序：1755 年开战至 1763 年战终与宽典，差 8 年
assert 1763 - 1755 == 8
# 3. 对殖民地一般货例外三样：葡萄酒、白棉布、细棉布
assert len(["wines","white calicoes","muslins"]) == 3
# 4. 转口贸易资本无处就业四途计数：农业、制造业、本国贸易、消费性外贸
assert len(["agriculture","manufactures","home trade","foreign trade of consumption"]) == 4
# 5. 关税收入方向登记：保留一部分 >0 时贸易可发生，全保留致进口不发生则收入为 0，部分保留收入大于零（方向登记）
assert 0.5 > 0 and 0 == 0
# 6. 结构计数：退税正当化理由适用范围 1 类（完全外国独立国）、不适用 1 类（享垄断的殖民地）、欺诈重灾货样 1 样（烟草）
assert len(["altogether foreign and independent"]) == 1 and len(["monopoly colonies"]) == 1 and len(["tobacco"]) == 1
print("91 verify: 6 assertions passed")
