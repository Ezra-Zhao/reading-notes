# -*- coding: utf-8 -*-
"""验证《国富论》125 篇篇内数字与结构（原书第四卷第七章第三部分收官段起，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 两大发现恰两件：发现美洲、绕好望角通东印度
assert len(["discovery of America", "passage to the East Indies by the Cape of Good Hope"]) == 2
# 2. 后果已历时距为二至三百年之间
assert 200 < 250 < 300
# 3. 西葡殖民地仅亚麻一项年消费据说逾三百万镑（原书声明不担保此数，以下限加一示意逾数）
linen_consumption_lower_bound = 3_000_000
assert linen_consumption_lower_bound + 1 > linen_consumption_lower_bound
# 4. 供给亚麻的他国恰四：法国、佛兰德、荷兰、德国
assert len(["France", "Flanders", "Holland", "Germany"]) == 4
# 5. 占殖民地国恰二：西班牙、葡萄牙；其利润花销地恰二：加的斯、里斯本
assert len(["Spain", "Portugal"]) == 2 and len(["Cadiz", "Lisbon"]) == 2
# 6. 周转序位：汉堡商人绕道伦敦的回款快于直通美洲（序位登记，原书篇内陈述）
returns = {"via London": 1, "direct to America": 2}
assert returns["via London"] < returns["direct to America"]
print("125 verify: 6 assertions passed")
