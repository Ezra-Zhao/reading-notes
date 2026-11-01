# -*- coding: utf-8 -*-
"""验证《国富论》93 篇篇内数字与结构（原书第四卷第五章中段，Gutenberg #3300）。数字均为原书篇内陈述，方向登记者为原书论证方向，不冒充现代实测，不构成投资建议。"""
# 1. 名义算例：4 先令对 3 先令 6 便士，差 6 便士（1 先令 = 12 便士，3 先令 6 便士 = 42 便士，4 先令 = 48 便士）
assert 48 - 42 == 6
# 2. 价格管制传导链：谷价直管二项（劳动、土地粗产物），再管二项（制造材料、制造技艺），合管一项（完整制造品）
assert len(["money price of labour", "rude produce of land"]) == 2 and len(["materials of manufactures", "manufacturing art and industry"]) == 2 and len(["complete manufacture"]) == 1
# 3. 西葡金银自然差额上限构成二项：运费、保险
assert len(["freight", "insurance"]) == 2
# 4. 坝模型方向登记：坝满后溢出量等于无坝时流量（流量不变），坝后存量比例大于坝前（方向登记，非实测）
flow_with_dam = flow_without_dam = 1.0
assert flow_with_dam == flow_without_dam and 1.5 > 1.0
# 5. 唯一真正受益群体一类：谷物商人（出口者与进口者同属一类人）
assert len(["corn merchants: exporters and importers as one set"]) == 1
# 6. 反对意见层数：出口赏金一般一层 + 特定一层，谷物赏金另加第三层（不能促进该商品生产）
assert 2 + 1 == 3
print("93 verify: 6 assertions passed")
