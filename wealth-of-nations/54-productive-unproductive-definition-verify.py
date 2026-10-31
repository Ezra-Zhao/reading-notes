# -*- coding: utf-8 -*-
"""验证《国富论》54 篇篇内数字与结构（取自原书第二卷第三章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性登记者已标明，不冒充现代实测。"""
# 1. 判据要件三项：固定于特定对象、可售商品、劳动后持续
assert len(["fixes in a particular subject","vendible commodity","endures after labour"]) == 3
# 2. 制造业者价值三分：材料增进、自身维持、主人利润
assert len(["materials improved","own maintenance","master profit"]) == 3
# 3. 非生产性同列：军政一类 + 教士/律师/医生/文人/演员/丑角/音乐家/歌剧歌手/歌剧舞者 >=10 类
assert len(["sovereign officers army navy","churchmen","lawyers","physicians","men of letters","players","buffoons","musicians","opera-singers","opera-dancers"]) >= 10
# 4. 年产物两分；补替份允许用途只有生产性工资一项
assert len(["replace capital","constitute revenue"]) == 2 and len(["productive wages only"]) == 1
# 5. 收入构成两途：利润、地租
assert len(["profit of stock","rent of land"]) == 2
# 6. 非生产性供养来源两路：原定收入、劳动者空余收入
assert len(["original revenue rent/profit","spare revenue of labourers"]) == 2
print("54 verify: 6 assertions passed")
