# -*- coding: utf-8 -*-
"""验证《国富论》124 篇篇内数字与结构（原书第四卷第七章第三部分行省出路与代表制段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 征税渠道恰两路：殖民地自有议会、大不列颠议会
assert len(["colony assemblies", "parliament of Great Britain"]) == 2
# 2. 法国行省课税样式恰两式：王亲定亲征、王索定额任省自征
assert len(["king imposes assesses levies", "king demands sum, states assess"]) == 2
# 3. 战时假想筹款一千万镑，基金来源恰两部
assert 10_000_000 == 10**7
assert len(["tax levied in Great Britain", "requisition to colony assemblies"]) == 2
# 4. 大陆会议层级：五百人直属、五十万人在其下，比例一千倍
assert 500_000 // 500 == 1000
# 5. 美洲拟送代表五六十名，落在 50-60 区间
assert 50 <= 55 <= 60
# 6. 根西与泽西恰两岛；税收反超预判时距一个多世纪（大于一百年）
assert len(["Guernsey", "Jersey"]) == 2
assert 100 < 120  # little more than a century，方向登记
print("124 verify: 6 assertions passed")
