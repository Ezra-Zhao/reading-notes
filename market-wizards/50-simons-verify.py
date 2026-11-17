#!/usr/bin/env python3
"""Verify arithmetic in note 50 (James Simons / Renaissance / Medallion).
All inputs are figures stated in the note's cited sources (Simons
Foundation obituary 2024-05-10; Zuckerman's yearly table as analysed in
Bradford Cornell's 2019 paper; Bloomberg/FT/Reuters reporting of the
66.1% gross / 39.1% net arithmetic averages for 1988-2018; Ziemba's
postscript monthly sample). This script only checks internal
arithmetic consistency. Clean-room, self-written.
"""
from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Life dates: born 1938-04-25, died 2024-05-10 at 86 (31,427 days);
#    MIT BS 1958 at age 20; Berkeley PhD 1961 at age 23.
check("1 lifespan days 31427", (date(2024, 5, 10) - date(1938, 4, 25)).days == 31427)
check("1 died aged 86", 2024 - 1938 == 86)
check("1 MIT 1958 at 20", 1958 - 1938 == 20)
check("1 PhD 1961 at 23", 1961 - 1938 == 23)

# 2. Career timeline: IDA code work 1964-1968 (4y); Stony Brook math
#    chair 1968-1978 (10y); founded firm (as Monemetrics) 1978, renamed
#    Renaissance 1982 (4y later); Medallion launched 1988, when he was
#    50; CEO until 2010 (28y from 1982), chairman until 2021 (39y).
check("2 IDA 4y", 1968 - 1964 == 4)
check("2 Stony Brook chair 10y", 1978 - 1968 == 10)
check("2 founding to rename 4y", 1982 - 1978 == 4)
check("2 Medallion at age 50", 1988 - 1938 == 50)
check("2 CEO span 28y / chair span 39y", (2010 - 1982 == 28) and (2021 - 1982 == 39))

# 3. The headline averages (Zuckerman table via Bloomberg/FT/Reuters):
#    1988-2018 arithmetic average 66.1% gross, 39.1% net; the fee wedge
#    is 27.0pp, i.e. fees consumed about 40.85% of the gross average.
check("3 fee wedge 27.0pp", abs((66.1 - 39.1) - 27.0) < 1e-9)
check("3 fees took ~40.85% of gross average", abs(27.0 / 66.1 * 100 - 40.85) < 0.01)

# 4. Cornell's compounding of the yearly gross table: USD 100 at the
#    start of 1988 becomes USD 398,723,873 by end-2018; over 31 years
#    that is a CAGR of about 63.3% -- below the 66.1% arithmetic
#    average, as it must be when yearly returns vary.
check("4 Cornell terminal multiple 3,987,238.73x",
      abs(398723873 / 100 - 3987238.73) < 0.01)
check("4 implied CAGR ~63.3%", abs(((398723873 / 100) ** (1 / 31) - 1) * 100 - 63.28) < 0.05)

# 5. Why the average is not a CAGR: compounding the 66.1% average flat
#    for 31 years would give about 6.78 million x, about 1.70x the
#    actual compounded table value; compounding the 39.1% net average
#    flat gives about 27,742x (USD 100 to about USD 2.77m) -- a
#    hypothetical only, since the fund capped size and returned
#    profits, so no dollar actually rode untouched for 31 years.
check("5 flat-gross hypothetical ~6,783,575x", abs(1.661 ** 31 - 6783575) < 1)
check("5 flat-gross / actual ~1.70x", abs((1.661 ** 31) / 3987238.73 - 1.70) < 0.01)
check("5 flat-net hypothetical ~27,742x", abs(1.391 ** 31 - 27742) < 1)

# 6. Reported trading profits: over USD 100bn by 2018 (Bloomberg via
#    Zuckerman); the appendix figure often cited is USD 104.5bn,
#    4.5% above the round floor; against the reported ~USD 10bn size
#    cap, cumulative profits are about 10.45x the cap itself.
check("6 appendix vs floor +4.5%", abs((104.5 / 100 - 1) * 100 - 4.5) < 1e-9)
check("6 profits ~10.45x the 10bn cap", abs(104.5 / 10 - 10.45) < 1e-9)

# 7. Fees against the industry standard 2-and-20: management 5% is
#    2.5x the standard 2%; performance rose 20% (to 2000) -> 36%
#    (2001) -> 44% (from 2002), i.e. the final performance fee is
#    2.2x both its own starting level and the standard 20%.
check("7 management 5 vs 2 = 2.5x", abs(5 / 2 - 2.5) < 1e-9)
check("7 performance 44 vs 20 = 2.2x", abs(44 / 20 - 2.2) < 1e-9)

# 8. The one losing year: in the 31 calendar years 1988-2018 the
#    yearly table shows a single negative net year (1989, about
#    -4.1% as republished); 30 of 31 years positive = 96.77%.
check("8 window is 31 years", 2018 - 1988 + 1 == 31)
check("8 positive years 30/31 = 96.77%", abs(30 / 31 * 100 - 96.77) < 0.01)
check("8 rebound from -4.1% needs +4.28%", abs((1 / 0.959 - 1) * 100 - 4.28) < 0.01)

# 9. Ziemba postscript monthly sample (net, Jan 1993-Apr 2005):
#    148 months with 17 monthly losses -> 131 non-losing months
#    (88.51%); 46 quarters with 3 quarterly losses (93.48% non-loss)
#    and no losing year inside that sample window.
check("9 sample months 148", (2005 - 1993) * 12 + 4 == 148)
check("9 non-losing months 131 = 88.51%", abs(131 / 148 * 100 - 88.51) < 0.01)
check("9 non-losing quarters 43/46 = 93.48%", abs(43 / 46 * 100 - 93.48) < 0.01)

# 10. Philanthropy scale: Simons Foundation founded 1994, 30 years
#     before his death; the 2023 Stony Brook gift was USD 500m;
#     lifetime giving reported above USD 6bn equals at least 19.11%
#     of the USD 31.4bn net worth Forbes estimated at his death.
check("10 foundation span 30y", 2024 - 1994 == 30)
check("10 giving >= 19.11% of final net worth", abs(6 / 31.4 * 100 - 19.11) < 0.01)

print("ALL PASSED" if ok else "SOME FAILED")
