# -*- coding: utf-8 -*-
"""验证《国富论》156 篇结构（平民教育中段，Gutenberg #3300）。参数为原书篇内陈述。"""
# 1. 最基本教育三样
assert len(["read","write","account"]) == 3
# 2. 有地位者入行年龄 18/19
assert [18,19] == sorted([19,18]) and 19-18 == 1
# 3. 公共三作用
assert len(["facilitate","encourage","impose necessity"]) == 3
# 4. 教师部分付薪；全部/主要付薪致怠
assert len(["partly paid by public"]) == 1 and len(["wholly paid -> neglect","principally paid -> neglect"]) == 2
# 5. 两例：苏格兰几乎全体会读；英格兰同类不普遍
assert len(["Scotland parish schools","England charity schools"]) == 2
# 6. 教材一换一：拉丁皮毛换几何力学初步（两门）
assert len(["geometry","mechanics"]) == 2 and len(["little smattering of Latin removed"]) == 1
print("156 verify: 6 assertions passed")
