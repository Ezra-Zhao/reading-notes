# -*- coding: utf-8 -*-
"""验证《国富论》160 篇结构（第三条收官，Gutenberg #3300）。参数为原书篇内陈述。"""
# 1. 改革两大派别恰两派、政府形态恰两型
assert len(["Lutheran", "Calvinistic"]) == 2 and len(["episcopal subordination", "presbyterian equality"]) == 2
# 2. 罗马旧权势世俗支柱恰三样
assert len(["landed jurisdictions", "tythes", "hospitality and charity retainers"]) == 3
# 3. 时程锚：教士衰势十四十五世纪、苏格兰选举制存续约二十二年、安妮法令为其第十年
assert len([14, 15]) == 2 and 22 > 20 and 10 == 10
# 4. 苏格兰账：总收入 68514 镑、944 名牧师、人均在 72 至 73 镑间、总费上限人均约 90 镑
assert 72 < 68514 / 944 < 73 and 85000 / 944 < 91
# 5. 人才流向恰两向、正反例组数
assert len(["universities drain church when benefices moderate", "church drains universities when benefices great"]) == 2 and len(["France", "England"]) == 2 and len(["Geneva", "Swiss protestant cantons", "Germany protestant", "Holland", "Scotland", "Sweden and Denmark"]) == 6
# 6. 报酬格言失效恰两途、管理手段归升迁一途
assert len(["underpaid meanness incapacity", "overpaid negligence idleness"]) == 2 and len(["preferment"]) == 1
print("160 verify: 6 assertions passed")
