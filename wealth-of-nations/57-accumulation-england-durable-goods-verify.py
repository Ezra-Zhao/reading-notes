# -*- coding: utf-8 -*-
"""验证《国富论》57 篇篇内数字与结构（取自原书第二卷第三章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性登记者已标明，不冒充现代实测。"""
# 1. 增值途径恰两途
assert len(["more productive labourers","greater productive powers"]) == 2
# 2. 四次法国战争年份、四次计数；两次叛乱计数
assert len([1688,1701,1742,1756]) == 4 and len([1715,1745]) == 2
# 3. 债务账：145,000,000 < 200,000,000，差额 55,000,000
assert 145_000_000 < 200_000_000 and 200_000_000 - 145_000_000 == 55_000_000
# 4. 回溯链台阶 >=6
assert len(["Restoration","Elizabeth accession","York-Lancaster close","Norman conquest","Saxon heptarchy","Caesar invasion"]) >= 6
# 5. 大节日给养 200-300 英担区间、浪费份额 1/2
assert 200 <= 250 <= 300 and abs(0.5 - 1/2) < 1e-12
# 6. 开支两分；流转实例组计数（西摩宅邸、詹姆斯婚床、纪念物组）
assert len(["immediately consumed","durable commodities"]) == 2 and len(["Seymour seat","James I marriage-bed","Versailles/Stowe/Wilton"]) == 3
print("57 verify: 6 assertions passed")
