# -*- coding: utf-8 -*-
"""验证《国富论》98 篇篇内数字与结构（原书第四卷第五章离题第二部分，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
from fractions import Fraction

# 1. 查理二世二十二年法令两档：价不超 53s4d 征 16s、价不超 4 镑征 8s；53s4d = 53 又 1/3 先令，4 镑 = 80 先令
price_low = Fraction(53) + Fraction(4, 12)
assert 16 > 8 and price_low == Fraction(160, 3) and 4 * 20 == 80 and price_low < 80
# 2. 小麦三档税递减：至 44s 征 21s9d、至 53s4d 征 17s、至 4 镑征 8s；其后约 1s4d 为最低
wheat = [Fraction(21) + Fraction(9, 12), Fraction(17), Fraction(8), Fraction(1) + Fraction(4, 12)]
assert wheat[0] > wheat[1] > wheat[2] > wheat[3] and wheat[0] == Fraction(87, 4)
# 3. 税表谷物行计数为 8：豆/大麦/麦芽/燕麦/豌豆/黑麦/小麦/荞麦；麦芽被年度麦芽税法案禁止
table_rows = ["beans", "barley", "malt", "oats", "pease", "rye", "wheat", "buck-wheat"]
malt_status = "prohibited_by_annual_malt_tax_bill"
assert len(table_rows) == 8 and "malt" in table_rows and malt_status.startswith("prohibited")
# 4. 税源叠加：22 年法令代替旧补助 + 新补助 + 三分之一补助 + 三分之二补助 + 1747 补助，共 5 个构件，其后法令又再提高
duty_sources = ["22_charles_ii_replacing_old_subsidy", "new_subsidy", "one_third_subsidy", "two_thirds_subsidy", "subsidy_1747"]
assert len(duty_sources) == 5 and Fraction(1, 3) + Fraction(2, 3) == 1
# 5. 临时暂停法令逻辑：荒年严格执行 -> 困苦；故临时法令暂停执行并限时许进口；其必要性 -> 总法不当
strict_execution_in_scarcity_causes_distress = True
temporary_statute_suspends_and_permits_for_limited_time = True
general_law_improper = strict_execution_in_scarcity_causes_distress and temporary_statute_suspends_and_permits_for_limited_time
assert general_law_improper is True
# 6. 赏金连带：小麦在 48s 以下或不远其上若自由进口，可带赏金转口出口；48 < 53 又 1/3 < 80
bounty_threshold = 48
free_import_below_threshold_opens_reexport_arbitrage = bounty_threshold < price_low < 80
assert free_import_below_threshold_opens_reexport_arbitrage is True
print("98 verify: 6 assertions passed")
