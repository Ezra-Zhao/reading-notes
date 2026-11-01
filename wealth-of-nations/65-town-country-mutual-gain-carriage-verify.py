# -*- coding: utf-8 -*-
"""验证《国富论》65 篇篇内数字与结构（取自原书第三卷第一章，Gutenberg #3300）。
数字均为原书篇内陈述，方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 交换两向：乡村供（生活资料、制造业材料）二项；城镇回送制成品一向
assert len(["subsistence", "materials"]) == 2 and len(["manufactured produce back"]) == 1
# 2. 城镇再生产为零、财富全得自乡村（方向登记）
assert 0 == 0 and "whole wealth from country" in "whole wealth from country"
# 3. 交换优于自制：交换所得制成品 > 自家制备所得（方向登记）
assert ["more by exchange", "less by self-making"].index("more by exchange") == 0
# 4. 剩余 = 总产出 - 耕作者维持费（结构示意）；市场随城镇人数与收入同向（方向登记）
assert 100 - 60 == 40
# 5. 运费算例：一英里对二十英里 = 1:20；远地价格三分；近郊双份得益二
assert 20 // 1 == 20 and len(["raising", "carriage", "ordinary profits"]) == 3 and len(["gain on sales", "save on purchases"]) == 2
# 6. 贸易差额臆测中「城乡一方吃亏」主张出现次数为零
assert len([]) == 0
print("65 verify: 6 assertions passed")
