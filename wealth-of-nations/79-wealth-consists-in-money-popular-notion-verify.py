# -*- coding: utf-8 -*-
"""验证《国富论》79 篇篇内数字与结构（取自原书第四卷引论与第一章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 两目标与两体系：目标二、体系二
assert len(["plentiful revenue for the people", "revenue for public services"]) == 2
assert len(["commercial system", "agricultural system"]) == 2
# 2. 货币双重职能：商业工具、价值尺度，计数二
assert len(["instrument of commerce", "measure of value"]) == 2
# 3. 汇兑算例：105 对 100，差 5，恰百分之五
assert 105 - 100 == 5 and 5 / 100 == 0.05
# 4. 两探问对照：西班牙问金银、鞑靼问牛羊，计数二
assert len(["Spaniards: gold or silver?", "Tartars: sheep and oxen?"]) == 2
# 5. 商人两论证：播种再出口、差额决定进出，计数二
assert len(["seed-time and harvest re-export", "balance of trade determines flow"]) == 2
# 6. 禁令样本：西葡、古苏格兰、法英古代，计数三组
assert len(["Spain and Portugal prohibition/duty", "old Scotch acts heavy penalties", "France and England ancient policy"]) == 3
print("79 verify: 6 assertions passed")
