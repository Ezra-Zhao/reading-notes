#!/usr/bin/env python3
"""Verify arithmetic in note 59 (Hu Xinwei / China Universal
Consumer Industry Mixed Fund, 000083).

All inputs are figures printed in the fund's 2026 Q3 report (period
ending 2026-09-30, sent 2026-10-27, cninfo disclosure). This script
only checks internal arithmetic consistency and derived windows.
Clean-room, self-written.
"""

from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure: appointed 2016-04-08, departure column blank at
#    2026-09-30, so 3,827 days (about 10.48 years). The fund contract
#    took effect 2013-05-03, 1,071 days before he took over, so the
#    since-inception figures are not all his.
tenure = (date(2026, 9, 30) - date(2016, 4, 8)).days
check("1 tenure days 3827", tenure == 3827)
check("1 tenure years ~10.48", abs(tenure / 365.25 - 10.48) < 0.01)
check("1 head days before him 1071",
      (date(2016, 4, 8) - date(2013, 5, 3)).days == 1071)

# 2. Every reported excess (fund minus benchmark) in the 3.2.1 table
#    matches simple subtraction, for all eight windows.
rows = [(4.68, 1.08, 3.60), (-5.01, -10.54, 5.53),
        (-17.32, -19.46, 2.14), (-24.03, -14.35, -9.68),
        (-44.21, -26.32, -17.89), (-0.99, 3.27, -4.26),
        (91.94, 35.24, 56.70), (338.20, 107.18, 231.02)]
check("2 eight excess diffs match",
      all(abs(a - b - d) < 0.005 for a, b, d in rows))

# 3. Since-inception return 338.20% implies a factor of 4.382,
#    exactly the printed ending unit NAV 4.382 yuan.
check("3 1+338.20% == ending NAV 4.382", abs(1 + 3.3820 - 4.382) < 1e-9)

# 4. Window decomposition: inside the ten-year window, the earliest
#    five years gained about +244.04% (10y over 5y) while the last
#    five lost -44.21%; inside the seven-year window, the first two
#    years gained about +77.47% (7y over 5y); Q2 2026 alone lost
#    about -9.26% (6m over 3m); the two years before the last year
#    inside the three-year window lost about -8.12% (3y over 1y).
check("4 10y-over-5y earliest 5y ~+244.04%",
      abs((1.9194 / 0.5579 - 1) * 100 - 244.04) < 0.01)
check("4 7y-over-5y first 2y ~+77.47%",
      abs((0.9901 / 0.5579 - 1) * 100 - 77.47) < 0.01)
check("4 6m-over-3m Q2 2026 ~-9.26%",
      abs((0.9499 / 1.0468 - 1) * 100 + 9.26) < 0.01)
check("4 3y-over-1y prior 2y ~-8.12%",
      abs((0.7597 / 0.8268 - 1) * 100 + 8.12) < 0.01)

# 5. Q3 profit split: realised -40,022,999.73 with total profit
#    277,986,414.89 leaves unrealised +318,009,414.62, about 114.40%
#    of the quarter's profit: the quarter was won on paper gains
#    while realised results were negative.
check("5 unrealised +318,009,414.62",
      abs(277986414.89 - (-40022999.73) - 318009414.62) < 0.01)
check("5 unrealised share of profit ~114.40%",
      abs(318009414.62 / 277986414.89 * 100 - 114.40) < 0.01)

# 6. Ending shares times ending unit NAV reproduce ending net
#    assets within rounding of the four-decimal unit NAV.
check("6 shares x NAV ~ net assets (0.01%)",
      abs(1398337745.21 * 4.382 - 6127161619.84) / 6127161619.84 < 0.0001)

# 7. Share flows reconcile exactly; net redemption was about 1.66%
#    of opening shares in a quarter the fund rose 4.68%.
beg, sub, red, end = 1421926283.23, 58880130.53, 82468668.55, 1398337745.21
check("7 flow reconciles", abs(beg + sub - red - end) < 0.01)
check("7 net redemption ~1.66%", abs((red - sub) / beg * 100 - 1.66) < 0.01)
check("7 subscriptions only ~4.14% of opening",
      abs(sub / beg * 100 - 4.14) < 0.01)

# 8. Asset mix: equities 5,671,059,333.93 of total assets
#    6,139,374,322.89 are 92.37%; equities over net assets are
#    92.56%, the industry table total. Components sum exactly.
parts = [5671059333.93, 171724393.42, 252211020.59, 44379574.95]
check("8 components sum to total assets", abs(sum(parts) - 6139374322.89) < 0.01)
check("8 equity share ~92.37%", abs(5671059333.93 / 6139374322.89 * 100 - 92.37) < 0.01)
check("8 equity/NAV ~92.56%", abs(5671059333.93 / 6127161619.84 * 100 - 92.56) < 0.01)

# 9. Industry lines sum to the same 92.56% of net assets;
#    manufacturing 79.79% is about 86.20% of the whole equity book.
ind = [6.78, 2.58, 79.79, 0.50, 1.18, 0.23, 0.10, 1.40]
check("9 industry lines sum 92.56%", abs(sum(ind) - 92.56) < 0.01)
check("9 manufacturing share of equity ~86.20%",
      abs(79.79 / 92.56 * 100 - 86.20) < 0.01)

# 10. Top ten holdings sum to 55.48% of net assets, about 59.94% of
#     the equity book. Sub-groups: top three 25.44%; the three home
#     appliance names 23.47%; the two liquor names 11.05%; Muyuan
#     plus Haida exactly 10.00%.
tops = [8.89, 8.33, 8.22, 6.25, 5.54, 4.92, 4.46, 3.33, 2.83, 2.71]
check("10 top10 sum 55.48%", abs(sum(tops) - 55.48) < 0.01)
check("10 top10 share of equity ~59.94%", abs(sum(tops) / 92.56 * 100 - 59.94) < 0.01)
check("10 top3 sum 25.44%", abs(sum(tops[:3]) - 25.44) < 0.01)
check("10 appliances 8.89+6.25+8.33 = 23.47%",
      abs(tops[0] + tops[3] + tops[1] - 23.47) < 0.01)
check("10 liquor 8.22+2.83 = 11.05%", abs(tops[2] + tops[8] - 11.05) < 0.01)
check("10 Muyuan+Haida exactly 10.00%", abs(tops[4] + tops[6] - 10.00) < 1e-9)

# 11. Bond book: government 40,534,827.40 plus financial bonds
#     131,189,566.02 equal the printed total 171,724,393.42;
#     policy financial bonds are about 58.90% of the bond book and
#     1.65% of net assets as printed.
check("11 bond components sum", abs(40534827.40 + 131189566.02 - 171724393.42) < 0.01)
check("11 policy bonds share ~58.90%",
      abs(101151369.86 / 171724393.42 * 100 - 58.90) < 0.01)
check("11 bond total / NAV ~2.80%",
      abs(171724393.42 / 6127161619.84 * 100 - 2.80) < 0.01)

# 12. Mechanical annualised returns: ten years about 6.74% a year;
#     five years about -11.02% a year. A -44.21% five-year loss
#     needs +79.25% to break even.
check("12 10y ann ~6.74%", abs((1.9194 ** 0.1 - 1) * 100 - 6.74) < 0.01)
check("12 5y ann ~-11.02%", abs((0.5579 ** 0.2 - 1) * 100 + 11.02) < 0.01)
check("12 recovery from -44.21% needs ~+79.25%",
      abs((1 / 0.5579 - 1) * 100 - 79.25) < 0.01)

print("ALL PASSED" if ok else "SOME FAILED")
