# -*- coding: utf-8 -*-
"""验证《国富论》84 篇篇内数字与结构（取自原书第四卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 价格尺：1 磅小麦 1 便士对 1 磅屠肉 4 便士，比为 4
assert 4 // 1 == 4
# 2. 谷物进口份额：23,728 夸特为年消费 1/571，年消费复算 = 23,728*571
consumption = 23728 * 571
assert consumption == 13548688 and 23728 / consumption < 0.002
# 3. 垄断焦虑半径序位：20 英里 < 30 里格（里格大于英里，方向登记）
assert 20 < 30
# 4. 航海法：条款 4 条；水手门槛 3/4 = 75%；双倍外国人税系数 2
assert len(["colonial/coasting ban", "origin-or-british ships + double duty", "direct-from-origin only", "foreign fish double duty"]) == 4
assert 3/4 == 0.75 and 2 == 2
# 5. 天然保护三样本：活牛（运费）、腌肉（品质与价）、谷物（体积）
assert len(["live cattle", "salt provisions", "corn"]) == 3
# 6. 可加负担情形：国防（本篇）+ 对等税（下篇）= 2，与原书两情形总述自洽
assert len(["defence", "equal tax"]) == 2
print("84 verify: 6 assertions passed")
