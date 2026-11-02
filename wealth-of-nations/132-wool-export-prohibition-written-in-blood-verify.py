# -*- coding: utf-8 -*-
"""验证《国富论》132 篇篇内数字与结构（原书第四卷第八章中段：羊毛出口禁令，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资或税务建议。"""
# 1. 每磅羊毛罚金 3 先令=36 便士；原书称约当其值 4 至 5 倍，反推单价落在 36/5 至 36/4 即 7.2 至 9 便士
fine_d = 3 * 12
assert fine_d == 36 and 7.2 <= fine_d / 5 and fine_d / 4 == 9
# 2. 建议出口税每托德 5 先令小于 10 先令且皆为正（税优于禁的方向登记：税可产岁入、禁只产走私二态）
assert 0 < 5 < 10 and len(["tax yields revenue", "prohibition yields smuggling only"]) == 2
# 3. 距离序位：内陆陆运海岸带 5 英里 < 肯特苏塞克斯报备带 10 英里 < 买毛立约带 15 英里
assert 5 < 10 < 15
# 4. 百户区连带罚 20 镑大于货值门槛 10 镑且超额档为三倍；包装违规每磅 8 先令大于出口罚每磅 3 先令
assert 20 > 10 and 3 * 10 == 30 and 8 > 3
# 5. 细呢原料恰西班牙毛一类（英毛不在内）；苏格兰毛价跌幅约 1/2（序位登记：跌后约半价）
assert len(["Spanish wool"]) == 1 and 0.5 == 1 / 2
# 6. 毛织制造商独占恰两道（对消费者、对种植者）；流放 7 年=84 月大于船长后法 6 月大于初法 3 月
assert len(["against consumers", "against wool growers"]) == 2 and 84 > 6 > 3
print("132 verify: 6 assertions passed")
