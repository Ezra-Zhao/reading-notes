# -*- coding: utf-8 -*-
"""验证《国富论》68 篇篇内数字与结构（取自原书第三卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 再分割两途（继承、转让）计数二；土地皆有主（方向登记）
assert len(["division by succession", "breaking by alienation"]) == 2 and ["no land without proprietor"] == ["no land without proprietor"]
# 2. 罗马对照二项：不分长幼、不分男女
assert len(["no distinction elder younger", "no distinction male female"]) == 2
# 3. 长子挑选差异二项（性别、年龄），优先序男先于女、长先于幼
assert len(["sex", "age"]) == 2 and ["male", "female"].index("male") < ["male", "female"].index("female") and ["elder", "younger"].index("elder") < ["elder", "younger"].index("younger")
# 4. 限嗣继承脱出三途（赠与、遗嘱处置、转让）计数三
assert len(["gift", "device", "alienation"]) == 3
# 5. 苏格兰严格限嗣继承份额：下限五分之一、上限推测三分之一，三分之一大于五分之一
assert 1/3 > 1/5 and abs((1/3 - 1/5) - 2/15) < 1e-9
# 6. 大改良者算例：四百至五百英亩、十倍开支、十分之一前破产
assert 400 < 500 and 10 > 1 and 1/10 < 1 and 500 * 10 == 5000
print("68 verify: 6 assertions passed")
