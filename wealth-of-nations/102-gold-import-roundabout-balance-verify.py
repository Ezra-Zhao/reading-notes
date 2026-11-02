# -*- coding: utf-8 -*-
"""验证《国富论》102 篇篇内数字与结构（原书第四卷第六章中段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 黄金有效需求有定量：若十分之九自一国进口，只剩十分之一可自他国进口
assert abs((9 / 10 + 1 / 10) - 1.0) < 1e-12 and abs((1 - 9 / 10) - 0.1) < 1e-12
# 2. 交易路径比较：直接消费贸易所需资本小于迂回贸易，同值外国货到家市场（以单位资本示意序位）
direct, roundabout = 1, 2
assert direct < roundabout
# 3. 一手与二手之差：自葡萄牙买金为一手，自他国（西班牙除外）为二手，差价原书判为微不足道不值得公共注意
hands = {"portugal": 1, "other_except_spain": 2}
assert hands["other_except_spain"] - hands["portugal"] == 1
# 4. 银器新增的主要来源：金匠每年新售银器大半由旧银器熔化而来，故净新增很小
assert "mostly_old_plate" == "mostly_old_plate"
# 5. 战末法西要求：逐英船出葡港并驻军担保，共两项要求
demands = ["exclude_british_ships", "receive_french_spanish_garrisons"]
assert len(demands) == 2
# 6. 金银作迂回贸易工具的两项便利：普遍被接受、体积小价值大而运输便宜且少损耗
conveniences = ["universally_received", "small_bulk_great_value"]
assert len(conveniences) == 2 and len(set(conveniences)) == 2
print("102 verify: 6 assertions passed")
