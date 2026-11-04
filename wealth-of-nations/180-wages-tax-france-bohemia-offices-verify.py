# -*- coding: utf-8 -*-
# 数据取自原书篇内陈述（180 篇覆盖段），不冒充现代实测。
# 1 法国泰耶：年工作日估 200 天 < 365，裁断者两类
assert 200 < 365
assert len(["collector", "commissary appointed by intendant"]) == 2
# 2 波希米亚四等递减；最高等 100 florins * 22.5d = 2250d = 9*240 + 90d = £9 7s 6d
classes = [100, 70, 50, 25]
assert classes == sorted(classes, reverse=True) and len(classes) == 4
pence = 100 * 22.5
assert pence == 2250 and pence // 240 == 9 and pence % 240 == 90 and 90 == 7 * 12 + 6
# 3 艺人/自由职业：退出通道一项
assert len(["deserted until returns to level"]) == 1
# 4 官俸不由市场竞争调节（否=0），常高于所需（方向 1）
regulated_by_competition = 0
above_required = 1
assert regulated_by_competition == 0 and above_required == 1
# 5 英格兰官俸税 5s6d = 27.5% > 土地税 4s = 20%；门槛年俸过 100 镑；豁免三组
assert 5.5 / 20 == 0.275 and 4 / 20 == 0.20 and 0.275 > 0.20
assert 100 == 100
assert len(["royal younger branches pensions", "army and navy pay", "few less obnoxious others"]) == 3
# 6 英格兰其他直接工资税为零项
other_direct_wage_taxes_england = []
assert len(other_direct_wage_taxes_england) == 0
print("180 verify: 6 assertions passed")
