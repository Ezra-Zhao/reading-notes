"""Market Wizards 15 Feng Liu verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; inputs are public-source figures
from Hikvision 2026 Q3 report coverage by China Securities Journal / Sina Finance /
10jqka and Choice data summaries (checked 2026-11-14):
1) 2026 Q3 cut: 113m -> 77m shares = -36m = -31.9%, more than 30%;
2) Peak to now: 435m (2023 Q3) -> 77m = 17.7% left, -82.3%, -358m shares;
3) From 412m at the start of the cutting run (2024 Q4) -> 77m = -81.3%;
4) Hikvision 2026 first-three-quarters minus Q3 alone gives H1:
   revenue 740.44 - 272.22 = 468.22; net profit 129.11 - 50.16 = 78.95 (CNY 100m);
5) Visible holdings: Hikvision 24.99 / total 55.21 = 45.3%; other six = 30.22 (CNY 100m);
6) Longbai: prior 53.00 - 25.50 = 27.50m, +92.7%; Angel Yeast cut 4.50 / 31.50 = 14.3%.
"""
assert round((113-77)/113*100, 1) == 31.9 and 113-77 == 36
print("1 ok: 2026 Q3 cut 36m shares = 31.9%")
assert round(77/435*100, 1) == 17.7 and round((435-77)/435*100, 1) == 82.3 and 435-77 == 358
print("2 ok: peak 435m -> 77m = 17.7% left, -82.3%, -358m shares")
assert round((412-77)/412*100, 1) == 81.3
print("3 ok: 412m -> 77m = -81.3%")
assert round(740.44-272.22, 2) == 468.22 and round(129.11-50.16, 2) == 78.95
print("4 ok: H1 revenue 468.22, H1 net profit 78.95 (CNY 100m, derived)")
assert round(24.99/55.21*100, 1) == 45.3 and round(55.21-24.99, 2) == 30.22
print("5 ok: Hikvision 24.99 / 55.21 = 45.3%; other visible holdings 30.22")
assert round(25.50/(53.00-25.50)*100, 1) == 92.7 and round(4.50/(27.00+4.50)*100, 1) == 14.3
print("6 ok: Longbai +92.7% vs prior quarter; Angel Yeast cut 14.3%")
print("All six assertions passed")
