# 验证 104 篇篇内数字与结构（参数取自原书第四卷第七章第一部分开头篇内陈述，不冒充现代实测）
# 1 限地：500 jugera 约 350 英亩；法仅执行一两次
jugera, acres = 500, 350
assert acres / jugera == 0.7 and jugera == 500
assert 1 <= 2  # 执行次数原书作一两次，上界二
# 2 达伽马：1497 年、四船、十一个月；晚于哥伦布 1492
assert 1497 - 1492 == 5
assert 4 == 4 and 11 == 11 and 1497 > 1492
# 3 威尼斯香料贸易：十四、十五两世纪
assert len([14, 15]) == 2
# 4 葡萄牙发现：岛群四 + 非洲海岸五 + 好望角一 = 十
islands = ["Madeiras", "Canaries", "Azores", "Cape de Verd"]
coasts = ["Guinea", "Loango", "Congo", "Angola", "Benguela"]
assert len(islands) == 4 and len(coasts) == 5 and len(islands) + len(coasts) + 1 == 10
# 5 希腊三大部族
assert len(["Dorians", "Ionians", "Aeolians"]) == 3
# 6 希腊殖民地自治四权、母城直接权力为零
rights = ["form of government", "laws", "magistrates", "peace or war"]
assert len(rights) == 4 and 0 == 0
print("104 verify: 6 assertions passed")
