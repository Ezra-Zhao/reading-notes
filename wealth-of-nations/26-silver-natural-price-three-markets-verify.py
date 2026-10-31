# Verify Ch XI digression: silver tax sequence, 1504/1545/1636 timeline, Europe/America markets, Lima population
from fractions import Fraction
# 1 Spain silver tax sequence strictly decreasing: 1/2 -> 1/3 -> 1/5 -> 1/10
seq = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5), Fraction(1, 10)]
assert all(seq[i] > seq[i + 1] for i in range(3))
# 2 timeline: 1545-1504 = 41 years; 1545+90 = 1635, book rounds to 'before 1636' (difference 1, registered not forced)
assert 1545 - 1504 == 41 and 1545 + 90 == 1635 and 1636 - 1635 == 1
# 3 hypothetical further cut to 1/20 = 5%, exactly half of 1/10
assert Fraction(1, 20) == Fraction(1, 10) / 2 and Fraction(1, 20) == Fraction(5, 100)
# 4 Europe improving samples: England, Holland, France, Germany, Sweden, Denmark, Russia = 7, plus Italy not backwards = 8
assert len(["England", "Holland", "France", "Germany", "Sweden", "Denmark", "Russia"]) == 7
# 5 Lima: Ulloa >50,000 vs Frezier 25,000-28,000 -> vs upper 28,000 growth > 78%; vs lower 25,000 exactly 2x at 50,000 bound
assert Fraction(50000 - 28000, 28000) > Fraction(78, 100) and Fraction(50000, 25000) == 2
# 6 America samples: new-market colonies 4 (New Granada, Yucatan, Paraguay, Brazils) + older enlarged 2 (Mexico, Peru) = 6
assert len(["New Granada", "Yucatan", "Paraguay", "Brazils"]) + len(["Mexico", "Peru"]) == 6
print("26 verify: 6 assertions passed")
