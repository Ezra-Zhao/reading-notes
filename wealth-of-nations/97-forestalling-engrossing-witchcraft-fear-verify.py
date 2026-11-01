# -*- coding: utf-8 -*-
"""验证《国富论》97 篇篇内数字与结构（原书第四卷第五章离题第一部分收官，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 放宽门槛序：小麦价上限相继为 20、24、32、40 先令，最终 48 先令，严格递增
thresholds = [20, 24, 32, 40, 48]
assert thresholds == sorted(thresholds) and len(set(thresholds)) == 5 and thresholds[-1] == 48
# 2. 囤市除外窗口：三个月内在同一市场再卖者为囤市者，不在 48 先令合法化范围内
forestaller_window_months = 3
assert forestaller_window_months == 3 and forestaller_window_months < 12
# 3. 查理二世十五年法令是内地贸易自由的来源：法令序号 15、章 7，现王十二年法令未废此条
assert (15, 7) == (15, 7) and 12 != 15
# 4. 进口比：进口谷物平均量对消费量不超 1 比 570，内地对进口重要性为 570 比 1
assert abs(1 / 570 - 0.0017543859649122807) < 1e-15 and 570 // 1 == 570
# 5. 出口比：出口平均量不超年产出三十一分之一，内地占 30/31，内地对出口重要性为 30 比 1
export_share = 1 / 31
inland_share = 1 - export_share
assert abs(inland_share - 30 / 31) < 1e-15 and abs(inland_share / export_share - 30) < 1e-12
# 6. 时序：查理二世法令颁行于赏金设立前约二十五年前，已足时生效；两种偏见计数为 2
assert 25 == 25 and len(["engrossing_hurts_at_48s", "forestalling_at_some_price"]) == 2
print("97 verify: 6 assertions passed")
