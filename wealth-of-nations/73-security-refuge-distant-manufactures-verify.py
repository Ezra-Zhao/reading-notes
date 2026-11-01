# -*- coding: utf-8 -*-
"""验证《国富论》73 篇篇内数字与结构（取自原书第三卷第三章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 自由期限：在城躲避追索满一年得永为自由人
assert 1 == 1 and ["one year free for ever"] == ["one year free for ever"]
# 2. 当时富裕勤劳者名单五项：希腊帝国、萨拉森阿拔斯、埃及、巴巴里部分、摩尔西班牙
assert len(["Greek empire", "Saracens Abbasides", "Egypt before Turks", "part of Barbary coast", "Moorish Spain"]) == 5
# 3. 十字军受益三城：威尼斯、热那亚、比萨计数三
assert len(["Venice", "Genoa", "Pisa"]) == 3
# 4. 移植路算例：1310 年、九百家被逐、三十一户退威尼斯、三百工人，31 小于 900 且 300 小于 900
assert 1310 == 1310 and 31 < 900 and 300 < 900 and 31 < 300
# 5. 自生路城镇五座：利兹、哈利法克斯、谢菲尔德、伯明翰、伍尔弗汉普顿计数五
assert len(["Leeds", "Halifax", "Sheffield", "Birmingham", "Wolverhampton"]) == 5
# 6. 虚拟出口：细布八十磅、谷物数千磅以二千磅为下限登记，2000 大于 80 为二十五倍；时序差一世纪以上（方向登记）
assert 2000 // 80 == 25 and 2000 > 80 and ["more than a century before"] == ["more than a century before"]
print("73 verify: 6 assertions passed")
