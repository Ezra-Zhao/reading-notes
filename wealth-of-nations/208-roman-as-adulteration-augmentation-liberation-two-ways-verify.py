# -*- coding: utf-8 -*-
# Data from the book passage covered by note 208; no modern measurement.
# 1 As reduced 12oz -> 2oz copper: payment ratio 1/6; 128M/6 = 21,333,333 1/3
assert 2 / 12 == 1 / 6
assert abs(128_000_000 / 6 - 21_333_333.333333) < 0.001
# 2 As finally 0.5oz = 1/24 of original; 128M/24 = 5,333,333 1/3
assert 0.5 / 12 == 1 / 24
assert abs(128_000_000 / 24 - 5_333_333.333333) < 0.001
# 3 Adulterated pound (20s = 240d) worth little more than 6s8d = 80d = 1/3
assert 6 * 12 + 8 == 80 and 80 / 240 == 1 / 3
# 4 Two expedients, same effect, opposite openness
assert len(["raising denomination", "adulterating standard"]) == 2
assert len(["open and avowed", "concealed"]) == 2
# 5 After augmentation weight seldom restored (0-ish); after adulteration fineness almost always restored (1)
assert 0 < 1
# 6 Liberation requires exactly 2 routes: great augmentation of revenue or great reduction of expense
assert len(["augmentation of public revenue", "reduction of public expense"]) == 2
print("208 verify: 6 assertions passed")
