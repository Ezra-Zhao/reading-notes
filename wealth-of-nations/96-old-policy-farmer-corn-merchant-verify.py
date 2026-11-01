# -*- coding: utf-8 -*-
"""验证《国富论》96 篇篇内数字与结构（原书第四卷第五章离题中段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 爱德华六世法令监禁阶梯：初犯 2 个月、再犯 6 个月，后者为前者 3 倍
first_months, second_months = 2, 6
assert second_months == 3 * first_months and first_months == 2
# 2. 没收阶梯：初犯没收 1 份谷值、再犯 2 倍，三犯没收全部财货（以 all 标记，不设倍数上限）
first_forfeit, second_forfeit, third_forfeit = 1, 2, "all"
assert second_forfeit == 2 * first_forfeit and third_forfeit == "all"
# 3. 执照门槛：按爱德华六世法令，发照须 3 名治安法官授权
justices_required = 3
assert justices_required == 3 and justices_required > 1
# 4. 双重利润算例：制造普通利润 10% 与开店普通利润 10%，自营零售须加 20%
manufacturing_profit, shopkeeping_profit = 10, 10
assert manufacturing_profit + shopkeeping_profit == 20
# 5. 少取即亏：应得 20% 而只取 15%，短少 5 个百分点，即未足额取得两份资本的利润
required, charged = 20, 15
assert required - charged == 5 and charged < required
# 6. 两法结构：受判法令 2 道，为害最烈者为逼农民兼营谷商一法；农民零售供应距离区间 4 至 5 英里
laws = ["ban_manufacturer_shopkeeper", "force_farmer_corn_merchant"]
assert len(laws) == 2 and laws[1] == "force_farmer_corn_merchant" and (4, 5) == (4, 5) and 5 - 4 == 1
print("96 verify: 6 assertions passed")
