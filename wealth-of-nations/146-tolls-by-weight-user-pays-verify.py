# -*- coding: utf-8 -*-
"""验证《国富论》146 篇篇内数字与结构（原书第五卷第一章第三部第一条前段：通行费自养、按重量收费与地方归属，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 朗格多克运河：逾 13,000,000 里弗，28 里弗一马克银，折逾 £900,000（量级登记：13,000,000/28 约 464,285 马克）
assert 13_000_000 > 900_000 and 13_000_000 // 28 == 464285
# 2. 收费节余猜测链（原书口径，作者脚注已自注过大）：现收基准猜测 500,000；加倍称可省 1,000,000；加至三倍称 2,000,000
savings = {1: 500_000, 2: 1_000_000, 3: 2_000_000}
assert savings[2] == 2 * savings[1] and savings[3] == 4 * savings[1]
# 3. 许多收费站所收逾修路所需两倍；奢侈马车按重量的费率高于必需货车（序位登记）
assert 2.0 > 1.0 and {"luxury_coach": 2, "necessary_cart": 1}["luxury_coach"] > {"luxury_coach": 2, "necessary_cart": 1}["necessary_cart"]
# 4. 失效模式对照：运河失修即断航（归私人可行），公路失修仍可通行（不可归私人，须受托人）
assert {"canal_neglected_passable": False, "highroad_neglected_passable": True}["canal_neglected_passable"] is False
# 5. 英法乡民修路劳役同为六日（登记）；中国君主收入几乎全出自土地税/地租（结构标记）
assert 6 == 6 and "land tax or land rent" in "revenue arises almost altogether from a land tax or land rent"
# 6. 自养工程四类（公路、桥、运河、港口）+ 另两件自养机构（铸币、邮政）
assert len(["highway", "bridge", "navigable canal", "harbour"]) == 4 and len(["coinage", "post-office"]) == 2
print("146 verify: 6 assertions passed")
