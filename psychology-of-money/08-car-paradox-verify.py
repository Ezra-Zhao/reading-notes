# -*- coding: utf-8 -*-
"""《金钱心理学》第8章「豪车悖论」结构命题复核（clean-room 自写脚本）。
本章几乎没有数字命题，复核的是正文断言的结构计数与注意力分配的算术演示，
不引用原文。演示数字为自设情景，只验证算术关系本身。"""
# 1 本章点名的豪车品牌共 3 个：法拉利、兰博基尼、劳斯莱斯
brands = ["法拉利", "兰博基尼", "劳斯莱斯"]
assert len(brands) == 3
# 2 悖论外推的领域共 3 类：豪车、豪宅、昂贵珠宝与华丽服饰（车之外再加 2 类）
domains = ["豪车", "豪宅", "珠宝服饰"]
assert len(domains) == 3 and len(domains) - 1 == 2
# 3 作者开出的替代路径是 3 种人格特质：谦虚、善良、同情心
traits = ["谦虚", "善良", "同情心"]
assert len(traits) == 3
# 4 注意力分配演示：100 名路人看车，设 90 人只想「换成我开」、
#    10 人注意到驾驶者本人——投向「人」的注意力只占一成
onlookers, self_imagining, noticing_driver = 100, 90, 10
assert self_imagining + noticing_driver == onlookers
assert noticing_driver / onlookers == 0.10
# 5 信号错位演示：车主预期收获的仰慕记 100 分，实际落到「人」身上的
#    按上条比例只有 10 分，错位 90 分——买的是车，漏的是人
expected, received = 100, 10
assert expected - received == 90 and received / expected == 0.10
print("all 5 assertions passed")
