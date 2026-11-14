"""Market Wizards 17 Zhu Shaoxing verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; inputs are public-source figures
from China Fund News reporting of the fund's 2026 Q3 report (via 21jingji, 2026-10-27),
a 2010 China Securities Journal manager profile, and a second provider's tally
(Securities Star via 10jqka, 2026-10-26) registered as a variant:
1) Tenure: fund inception 2005-11-16 to 2026-09-30 = 7,623 days = 20.87 years;
   to 2026-11-16 it completes 21 full years;
2) Tenure return 1537.37% = 16.3737x cumulative multiple;
3) Annualised check: 16.3737 ** (1/20.87) - 1 = 14.33%, within 0.1pt of the
   provider-reported 14.27% (difference is day-count / start-date convention);
4) Zhongji Innolight: 560k -> 950k shares = +69.6%, i.e. about +70% as reported;
5) CATL: 3.10m -> 1.65m shares = -46.8%, i.e. a cut of more than 40% as reported,
   leaving 53.2% of the previous position;
6) Changxin: RMB 548m / 10.00m shares = RMB 54.8 implied value per share;
   variant tally 1544.59% = 16.4459x, 0.44% above the main tally in multiple terms.
"""
from datetime import date

days = (date(2026, 9, 30) - date(2005, 11, 16)).days
assert days == 7623 and round(days / 365.25, 2) == 20.87
assert (date(2026, 11, 16) - date(2005, 11, 16)).days == 7670
print("1 ok: 2005-11-16 -> 2026-09-30 = 7623 days = 20.87 years; 21 years on 2026-11-16")
assert round(1 + 1537.37 / 100, 4) == 16.3737
print("2 ok: tenure return 1537.37% = 16.3737x")
ann = (16.3737 ** (1 / 20.87) - 1) * 100
assert round(ann, 2) == 14.33 and abs(ann - 14.27) < 0.1
print("3 ok: recomputed annualised 14.33%, within 0.1pt of reported 14.27%")
assert round((95 - 56) / 56 * 100, 1) == 69.6
print("4 ok: Zhongji Innolight 56 -> 95 (10k shares) = +69.6%, about +70%")
assert round((310 - 165) / 310 * 100, 1) == 46.8 and round(165 / 310 * 100, 1) == 53.2
print("5 ok: CATL 310 -> 165 (10k shares) = -46.8% cut, 53.2% remains")
assert 548_000_000 / 10_000_000 == 54.8
assert round(1 + 1544.59 / 100, 4) == 16.4459
print("6 ok: Changxin RMB 548m / 10m shares = RMB 54.8/share; variant 1544.59% = 16.4459x")
print("All six assertions passed")
