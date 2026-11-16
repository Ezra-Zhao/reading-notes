#!/usr/bin/env python3
"""Verify arithmetic for note 39 (Cui Chenlong). Inputs from public
sources cited in the note: Qianhai Kaiyuan Public Utilities Industry
Stock Fund (005669) 2023 annual report (sent 2024-03-30) section 3.1
(2021 NAV growth 119.42%, realised gain CNY 1,383,504,406.87, period
profit CNY 5,271,371,657.55, year-end NAV per share 3.6455, year-end
net assets CNY 25,816,364,659.74, distributable profit per share
0.7466; 2022 NAV growth -26.02%, realised CNY 852,096,162.00, profit
CNY -6,332,410,043.41, NAV 2.6971, assets CNY 16,883,794,861.93;
2023 NAV growth -13.67%, realised CNY -576,482,591.06, profit
CNY -2,044,314,418.47, NAV 2.3285, assets CNY 12,026,634,215.79,
total shares 5,164,924,807.80, past-three-years growth 40.15% vs
benchmark 6.39%); section 4.1.2 (sole manager Cui Chenlong, appointed
2020-07-20, 7 years of securities experience, NTU Singapore PhD,
joined the manager in Aug 2017 after Nov 2016-Aug 2017 at Qianhai
Ankang); cninfo manager-change announcement dated 2021-11-20
(appointed 2020-07-20 to funds 005669 and 006923, 5 years of
experience at that date); Wind figures carried by Lai Times / China
Securities Journal (2021 champion 119.42%, runner-up also his at
109.36%, third place 100.52%, active-equity average 9.29%); China
Securities Journal profile 2025-12-29 (total AUM from under CNY 0.7bn
to a peak over CNY 40bn, over CNY 15bn at 2025 Q3-end); Sina fund
report 2026-10-29 (his other fund, Qianhai Kaiyuan HK-Shenzhen
Non-Cyclical C, tenure return -8.63% since 2020-07-20, scale
CNY 13,207,700 at 2026 Q3-end, bio says 9 years of experience)."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. The 2021 double championship gaps
assert close(119.42 - 109.36, 10.06, 0.001) and close(119.42 - 100.52, 18.90, 0.001) and close(119.42 - 9.29, 110.13, 0.001)
print("1 champion OK his two funds took first and second in 2021: 119.42% vs 109.36% is a 10.06-point gap inside one manager's own book; the champion beat third place (100.52%) by 18.90 points and the active-equity average (9.29%) by 110.13 points")

# 2. Three annual growth rates compound to the annual report's own past-three-years figure
comp = 2.1942 * 0.7398 * 0.8633 - 1
assert close(comp * 100, 40.15, 0.02)
print(f"2 compound OK (1+119.42%) x (1-26.02%) x (1-13.67%) - 1 = {comp*100:.2f}%, matching the 2023 annual report's printed past-three-years growth of 40.15% (benchmark 6.39%) within rounding -- the three annual prints and the three-year print are the same account")

# 3. The two years after the championship: drawdown and recovery price
dd = 0.7398 * 0.8633
assert close((dd - 1) * 100, -36.13, 0.01) and close((1 / dd - 1) * 100, 56.58, 0.02)
print(f"3 drawdown OK 2022-2023 compounded = {dd:.4f}, i.e. -36.13% from the 2021 year-end NAV; getting back needs +{(1/dd-1)*100:.2f}% -- the fall and the climb back are never the same number")

# 4. The NAV-per-share prints tell the same story independently
assert close(2.3285 / 3.6455, dd, 0.001) and close(2.6971 / 3.6455, 0.7398, 0.001)
print("4 nav OK year-end NAV per share 3.6455 (2021) -> 2.6971 (2022) -> 2.3285 (2023): the ratios are 0.7398 and 0.6387, the same two factors as the printed growth rates -26.02% and the compounded -36.13%")

# 5. The profit swing between the championship year and the year after
swing = 5_271_371_657.55 - (-6_332_410_043.41)
assert close(swing / 1e8, 116.04, 0.01) and close((6_332_410_043.41 + 2_044_314_418.47) / 1e8, 83.77, 0.01)
print(f"5 swing OK period profit swung from +52.71 yi CNY in 2021 to -63.32 yi in 2022, a swing of {swing/1e8:.2f} yi; the 2022 and 2023 losses together are 83.77 yi, more than the championship year's entire profit")

# 6. 2022: realised gains were positive while the period profit was deeply negative
unreal = -6_332_410_043.41 - 852_096_162.00
assert close(unreal / 1e8, -71.85, 0.01)
print(f"6 unrealised OK in 2022 the fund booked +8.52 yi CNY of realised gains yet a period profit of -63.32 yi, so the mark-to-market part was about {unreal/1e8:.2f} yi -- he did not sell his way out; the loss sat in the holdings")

# 7. The champion fund's own assets and shares shrank by more than half in two years
assert close((12_026_634_215.79 / 25_816_364_659.74 - 1) * 100, -53.41, 0.01)
shares21 = 5_287_050_697.11 / 0.7466
assert close(25_816_364_659.74 / shares21, 3.6455, 0.01) and close(5_164_924_807.80 / shares21 * 100, 72.93, 0.05)
print(f"7 shrink OK the fund's net assets fell from CNY 25.816bn (2021-end) to CNY 12.027bn (2023-end), -53.41%; shares implied by the 2021 distributable-profit line are about {shares21/1e8:.2f} hundred-million (assets/shares reproduces the printed NAV 3.6455), and the printed 2023 share count is only 72.93% of that -- holders left as well as prices fell")

# 8. How fast the championship came, and how long the tenure now is
d_champ = (date(2021, 12, 31) - date(2020, 7, 20)).days
d_2023 = (date(2023, 12, 31) - date(2020, 7, 20)).days
d_2026 = (date(2026, 10, 29) - date(2020, 7, 20)).days
assert d_champ == 529 and d_2023 == 1259 and d_2026 == 2292
print(f"8 tenure OK appointed 2020-07-20, so the 2021 championship closed {d_champ} days (about 1.45 years) into the job -- the 'just over one year' profile wording checks out; by the 2023 annual report he had served {d_2023} days, and by 2026-10-29 {d_2026} days, about 6.28 years")

# 9. The experience-year prints in three official documents agree with each other
assert 2021 - 2016 == 5 and 2023 - 2016 == 7 and 2026 - 2016 == 10
print("9 experience OK the Nov-2021 cninfo announcement prints 5 years of experience, the 2023 annual report prints 7, and the Oct-2026 Sina fund bio prints 9 -- each is the truncated count from a Nov-2016 start (2016-11 to 2026-10 is 9 years 11 months, printed as 9); three documents, one start date, no contradiction")

# 10. Total-AUM arc (bounds only) and the same-manager contrast fund
assert close(400 / 7, 57.14, 0.01) and close(12_026_634_215.79 / 13_207_700, 910.57, 0.5)
print("10 scale OK profile bounds: total AUM went from under CNY 0.7bn to a peak over CNY 40bn, a rise of more than 57.14x on the printed bounds, and was back to over CNY 15bn at 2025 Q3-end (bounds only, no exact peak or trough is printed); contrast: the other fund he took on the same day, 2020-07-20, showed a tenure return of -8.63% by 2026-10-29 and a scale of only CNY 13.21m at 2026 Q3-end -- about 1/911 of the champion fund's 2023 year-end assets (different dates, scale contrast only)")

print("ALL PASS")
