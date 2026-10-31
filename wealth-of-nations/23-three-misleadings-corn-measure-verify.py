# Verify Ch XI digression first-period errors: conversion price, assize transcription, 1270 extremes, Fleetwood count, cattle examples, two causes
from fractions import Fraction
# 1 conversion price 8s: in 1423 silver equal to 16s present (2x); in 1562 equal to 8s present (1x)
assert Fraction(16,8) == 2 and Fraction(8,8) == 1
# 2 assize transcription: copiers stopped at 12s of full 20s range = 3/5; mistaken middle 6s vs supposed middle 10s
assert Fraction(12,20) == Fraction(3,5) and Fraction(6,10) == Fraction(3,5)
# 3 1270 extremes converted at 3x to present: 4l16s=96s -> 288s=14l8s; 6l8s=128s -> 384s=19l4s
assert 96*3 == 288 and 288 == 14*20+8 and 128*3 == 384 and 384 == 19*20+4
# 4 Fleetwood: 80 years collected + 4 added by Smith from Eton = 84 = 7 divisions x 12 years
assert 80+4 == 84 and 7*12 == 84
# 5 cattle examples: Buenos Ayres ox 21.5d; Chili horse 16s=192d; horse/ox ratio
assert Fraction(192,1) / Fraction(43,2) == Fraction(384,43)
# 6 precious-metal quantity increase causes = 2 (mines abundance vs wealth increase); only first necessarily lowers value
assert len(["mines_abundance","wealth_increase"]) == 2
print("23 verify: 6 assertions passed")
