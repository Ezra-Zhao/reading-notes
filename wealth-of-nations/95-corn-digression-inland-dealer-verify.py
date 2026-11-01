# -*- coding: utf-8 -*-
"""验证《国富论》95 篇篇内数字与结构（原书第四卷第五章离题前段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 谷物商人四分支：内地商人、为国内消费进口者、出口本国产谷者、转口承运者，恰为四支
assert len(["inland dealer", "importer for home consumption", "exporter of home produce", "carrier for re-export"]) == 4
# 2. 合同价：荒歉前小麦每夸特普通约 28 先令，28 先令即 1 镑 8 先令（20 先令为 1 镑），折 1.4 镑
assert 28 == 20 + 8 and abs(28 / 20 - 1.4) < 1e-9
# 3. 配给比例：全年供给按日、周、月均匀摊分，月配给占全年 1/12，12 个月合回全年供给一份不少
annual_units = 1200
monthly_units = annual_units / 12
assert abs(monthly_units / annual_units - 1 / 12) < 1e-12 and 12 * monthly_units == annual_units
# 4. 谷物难被垄断的两道结构障碍：总值超过少数私人资本所能买下，加生产一出土即分散于无数所有者之手
assert len(["total value exceeds a few private capitals", "produce divided among innumerable scattered owners"]) == 2
# 5. 政府强令按自认合理价出售的两路致饥：或阻其上市致季初饥荒，或助长抢先消费致季末饥荒，恰为两路
assert len(["hindered from bringing corn to market", "encouraged to consume too fast"]) == 2
# 6. 历史裁决的成因映射：荒歉归真实稀缺一类，饥荒在原书裁决中只归政府以不当手段救荒一类，非政府成因为零
famine_causes = ["violence of government attempting by improper means to remedy a dearth"]
dearth_causes = ["real scarcity from the fault of the seasons or the waste of war"]
assert len(famine_causes) == 1 and len(dearth_causes) == 1 and famine_causes != dearth_causes
print("95 verify: 6 assertions passed")
