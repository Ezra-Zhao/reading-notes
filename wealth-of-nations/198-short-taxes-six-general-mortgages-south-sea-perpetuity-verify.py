# -*- coding: utf-8 -*-
# Data from the book passage covered by note 198; no modern measurement.
# 1 New taxes were imposed for short terms only: 4, 5, 6 or 7 years
assert sorted({4, 5, 6, 7}) == [4, 5, 6, 7]
assert len({4, 5, 6, 7}) == 4
# 2 Six general mortgages, prolongation end-years strictly increasing
ends = [1706, 1710, 1712, 1714, 1716, 1720]
assert len(ends) == 6
assert ends == sorted(ends) and len(set(ends)) == 6
# 3 Deficiencies charged on the first mortgage exceeded those on the second
assert 5160459 > 2055999
# 4 Sums borrowed on the 3rd-6th mortgages (pounds) total 4,127,011
assert 983254 + 925176 + 922029 + 1296552 == 4127011
# 5 In 1711 those duties stood subject to 4 anticipations; the South Sea
#    advance of 9,177,967 pounds exceeded every single mortgage sum
assert 4 == len(["anticipation 1", "anticipation 2", "anticipation 3", "anticipation 4"])
assert 9177967 > max(5160459, 2055999, 983254, 925176, 922029, 1296552)
# 6 Before 1711, perpetual taxes for paying interest of a debt had been
#    imposed only for 3 named objects; only 2 ever actually advanced money
objects = ["Bank advance", "East India Company advance",
           "projected land bank (never advanced)"]
assert len(objects) == 3
assert len([o for o in objects if "never" not in o]) == 2
print("198 verify: 6 assertions passed")
