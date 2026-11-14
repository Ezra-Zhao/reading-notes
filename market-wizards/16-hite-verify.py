"""Market Wizards 16 Larry Hite verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; inputs are public-source figures
from publisher bios (McGraw Hill / Meb Faber episode notes), Wikipedia timeline and
Schwager-reported Mint figures as summarised in secondary profiles (checked 2026-11-14):
1) Tenure: co-founded Mint 1981, stepped back from hands-on role 1994 = 13 years;
2) >30% compounded for 13 years = at least 1.30**13 = 30.29x before fees;
3) AUM scale: USD 2m at Apr 1981 inception to over USD 800m by mid-1988 = 400x,
   and to USD 1bn by 1990 = 500x (asset growth, not investment return);
4) 1% rule losing streaks: 0.99**10 leaves 90.4% (-9.6%), 0.99**20 leaves 81.8%;
5) Contrast at 5% risk: 0.95**10 leaves 59.9% (-40.1%);
6) Sizing example and year spread: USD 50,000 x 1% = USD 500, / USD 4 stop = 125 units;
   best year +60% (1987) minus worst year +13% (to 1988) = 47 points, worst still positive.
"""
assert 1994 - 1981 == 13
print("1 ok: 1981 -> 1994 = 13-year tenure")
assert round(1.30 ** 13, 2) == 30.29
print("2 ok: 1.30**13 = 30.29x minimum for >30% over 13 years")
assert 800 / 2 == 400 and 1000 / 2 == 500
print("3 ok: AUM 2m -> 800m = 400x; 2m -> 1bn = 500x (scale, not return)")
assert round((1 - 0.99 ** 10) * 100, 1) == 9.6 and round(0.99 ** 20 * 100, 1) == 81.8
print("4 ok: ten 1% losses = -9.6%; twenty leaves 81.8%")
assert round((1 - 0.95 ** 10) * 100, 1) == 40.1
print("5 ok: ten 5% losses = -40.1%")
assert 50000 * 0.01 == 500 and 500 / 4 == 125 and 60 - 13 == 47
print("6 ok: sizing 500 / 4 = 125 units; best-worst spread 47 points")
print("All six assertions passed")
