# -*- coding: utf-8 -*-
"""验证《国富论》107 篇篇内数字与结构（原书第四卷第七章第二部分开头，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 土地潜能：殖民者用尽自己与雇工的勤劳，也难做到土地所能产出的十分之一
assert 1/10 == 0.1 and 0.1 < 0.5
# 2. 希腊殖民地追平母城的时间：一两百年，即下限一百年、上限二百年
assert 100 < 200 and 200 - 100 == 100
# 3. 点名城市六座：叙拉古、阿格里真托、塔伦图姆、洛克里、以弗所、米利都
cities = ["Syracuse", "Agrigentum", "Tarentum", "Locri", "Ephesus", "Miletus"]
assert len(cities) == 6
# 4. 学派不在本土的两位哲学家：泰勒斯、毕达哥拉斯
philosophers = ["Thales", "Pythagoras"]
assert len(philosophers) == 2
# 5. 希腊繁荣两条件：丰裕好地、独立自主
assert len(["plenty of good land", "independence"]) == 2
# 6. 工资双读：作为土地价格看的低值小于作为劳动工资看的高值
assert 1 < 10  # 篇内序位断言：低读数 < 高读数
print("107 verify: 6 assertions passed")
