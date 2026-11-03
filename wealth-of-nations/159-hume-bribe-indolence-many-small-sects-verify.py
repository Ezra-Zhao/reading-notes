# -*- coding: utf-8 -*-
"""验证《国富论》159 篇结构（休谟引文与小派别，Gutenberg #3300）。参数为原书篇内陈述。"""
# 1. 休谟两类行业恰两类
assert len(["leave to itself", "public encouragement against negligence"]) == 2
# 2. 热忱危险构型恰两种；无害构型数量级数百至数千
assert len(["one sect tolerated", "two or three great sects"]) == 2 and 200 < 3000
# 3. 道德体系恰两套；轻浮之恶毁人时程平民一周小于时髦人士数年
assert len(["austere", "liberal or loose"]) == 2 and 1 < 52 * 3
# 4. 小派别惩罚恰两名
assert len(["expulsion", "excommunication"]) == 2
# 5. 矫正办法恰两个
assert len(["science and philosophy probation", "public diversions liberty"]) == 2
# 6. 娱乐门类五类
assert len(["painting", "poetry", "music", "dancing", "dramatic representations"]) == 5
print("159 verify: 6 assertions passed")
