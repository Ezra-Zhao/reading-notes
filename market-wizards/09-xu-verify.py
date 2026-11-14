"""Market Wizards 09 Xu Xiang verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; all inputs are public-report figures, not audited accounts:
1) An increase of about 3000% means the ending value is about 31x the start;
2) Fine 11 billion yuan / registered capital 30 million yuan = about 366.67x;
3) Fine 11 billion / reported AUM 20 billion = 55%;
4) Xu fine 11 billion is 11x Wang Wei fine 1 billion;
5) Arrest 2015-11-01 to formal arrest 2016-04-29 is 180 days; arrest to release 2021-07-09 is 2077 days;
6) A 40% market fall needs a 66.7% rise to recover.
"""
from datetime import date
assert 1 + 3000 / 100 == 31
print("1 ok: +3000% = 31x")
assert round(110 / 0.3, 2) == 366.67
print("2 ok: 11bn / 30m = 366.67x")
assert 110 / 200 == 0.55
print("3 ok: fine / AUM = 55%")
assert 110 / 10 == 11
print("4 ok: Xu fine = 11x Wang fine")
assert (date(2016, 4, 29) - date(2015, 11, 1)).days == 180 and (date(2021, 7, 9) - date(2015, 11, 1)).days == 2077
print("5 ok: 180 days to formal arrest; 2077 days arrest to release")
assert round((1 / 0.6 - 1) * 100, 1) == 66.7
print("6 ok: -40% needs +66.7% to recover")
print("All six assertions passed")
