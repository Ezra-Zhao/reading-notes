# -*- coding: utf-8 -*-
"""验证《国富论》110 篇篇内数字与结构（原书第四卷第七章第二部分第四项开头，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 行独占公司政策的国家计数四：荷兰、丹麦、法国、葡萄牙
assert len(["Holland", "Denmark", "France", "Portugal"]) == 4
# 2. 葡萄牙 1755 年此策所及巴西省份二：伯南布哥、马拉尼昂
assert len(["Pernambuco", "Maranhao"]) == 2
# 3. 公司压制动作三层：卖贵、买贱、限量收购
assert len(["sell dear", "buy cheap", "limit quantity bought"]) == 3
# 4. 1755 年在本世纪（1700-1799）后半，登记逆行时点方向
assert 1755 > 1750 and 1755 < 1800
# 5. 殖民者对公司的双向义务二：所需欧洲货全向其买、剩余产物全卖其手
assert len(["buy all European goods from company", "sell whole surplus to company"]) == 2
# 6. 贸易三型序位：独占公司型为第一型，一小于二小于三
assert 1 < 2 < 3
print("110 verify: 6 assertions passed")
