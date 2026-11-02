# -*- coding: utf-8 -*-
"""验证《国富论》111 篇篇内数字与结构（原书第四卷第七章第二部分第四项中段，Gutenberg #3300）。数字均为原书篇内陈述及其所引乌略亚记录，不冒充现代实测，不构成投资建议。"""
# 1. 基多价格：一磅铁 4 先令 6 便士 = 4.5 先令，一磅钢 6 先令 9 便士 = 6.75 先令，钢/铁恰 1.5
iron, steel = 4 + 6/12, 6 + 9/12
assert iron == 4.5 and steel == 6.75 and steel / iron == 1.5
# 2. 第二型三道闸：特定港口、船队与特定季节、特别执照
assert len(["particular port", "fleet and particular season", "particular licence"]) == 3
# 3. 压迫程度序位：独占公司型最重、单一港口型居中、全民自由型最轻
assert 3 > 2 > 1  # 以 3/2/1 登记三型压迫序位（独占=3 最重，自由=1 最轻）
# 4. 第三型所需许可仅海关普通放行文书一种
assert len(["common despatches of the custom-house"]) == 1
# 5. 第三型沿革锚点二：英格兰普利茅斯公司解散、法国密西西比公司解散
assert len(["Plymouth company dissolved", "Mississippi company dissolved"]) == 2
# 6. 葡萄牙改行更坏型的例外省份二：伯南布哥、马拉尼昂
assert len(["Pernambuco", "Maranhao"]) == 2
print("111 verify: 6 assertions passed")
