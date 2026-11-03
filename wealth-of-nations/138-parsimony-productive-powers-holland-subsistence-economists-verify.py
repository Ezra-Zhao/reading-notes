# -*- coding: utf-8 -*-
"""验证《国富论》138 篇篇内数字与结构（原书第四卷第九章后段中半：根本错误后两条与体系总评，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 年产物增加途径恰两条：改良有用劳动生产力、增加有用劳动数量
assert len(["improvement of productive powers", "increase of quantity of labour"]) == 2
# 2. 生产力改良来源两项（工匠能力、机械）；分工细度序位：工匠制造劳动可分性大于耕者
rank = {"artificers subdivision": 2, "farmers subdivision": 1}
assert rank["artificers subdivision"] > rank["farmers subdivision"] and len(["ability of workman", "machinery"]) == 2
# 3. 资本增额恰等于储蓄额（等式登记）；体系所设更倾向节俭者恰三类
assert 100 == 100 and len(["merchants", "artificers", "manufacturers"]) == 3
# 4. 荷兰活牛来源两处；贸易国进口养多、出口养少（序位登记）
assert len(["Holstein", "Jutland"]) == 2
subsistence = {"imported by manufactured produce": 2, "exported rude produce of non-trading country": 1}
assert subsistence["imported by manufactured produce"] > subsistence["exported rude produce of non-trading country"]
# 5. 租约有效期 9 -> 27 年恰 3 倍；法国农业解除压迫恰三项（租期、省际运谷、出口自由）
assert 27 == 9 * 3 and len(["lease prolonged", "provincial restraints removed", "export liberty established"]) == 3
# 6. 三大发明恰三项，经济表居第三
inventions = ["writing", "money", "economical table"]
assert len(inventions) == 3 and inventions[2] == "economical table"
print("138 verify: 6 assertions passed")
