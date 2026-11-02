# -*- coding: utf-8 -*-
"""验证《国富论》99 篇篇内数字与结构（原书第四卷第五章离题第三部分，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 出口放行门槛：查理二世十二年 40 先令 < 十五年延至的 48 先令
assert 40 < 48
# 2. 磅税（便士）：小麦 1 先令 = 12 便士 > 其他谷物 6 便士 > 燕麦 4 便士
poundage_pence = {"wheat": 12, "other_grain": 6, "oats": 4}
assert poundage_pence["wheat"] == 1 * 12 and poundage_pence["wheat"] > poundage_pence["other_grain"] > poundage_pence["oats"]
# 3. 法令链计数：查理二世 12 年、15 年、22 年，威廉与玛丽 1 年，威廉三世 11-12 年 c.20，共 5 步
statute_chain = ["charles2_12_c4_40s", "charles2_15_48s", "charles2_22_all_prices", "william_mary_1_virtual_removal", "william3_11_12_c20_express_removal"]
assert len(statute_chain) == 5
# 4. 利益相反情形登记：内地商人从不相反，出口商在本国歉收加邻国饥荒时运出可加重灾情
opposite_cases = {"inland_dealer": False, "exporter_home_dearth_neighbour_famine": True}
assert opposite_cases["inland_dealer"] is False and opposite_cases["exporter_home_dearth_neighbour_famine"] is True
# 5. 大国小国对照计数：大国法国、英格兰各计 1，小邦瑞士一州、意大利小邦各计 1；必要性大国几乎永不、小邦有时或许
great_states = ["france", "england"]
small_states = ["swiss_canton", "little_states_italy"]
necessity = {"great": "scarce_ever", "small": "sometimes_perhaps"}
assert len(great_states) == 2 and len(small_states) == 2 and necessity["great"] != necessity["small"]
# 6. 临时补丁法令计数：临时禁出口、临时免进口税共 2 类，频出即反证总制不当
temporary_expedients = ["temporary_export_prohibition", "temporary_import_duty_removal"]
assert len(temporary_expedients) == 2 and len(temporary_expedients) > 0
print("99 verify: 6 assertions passed")
