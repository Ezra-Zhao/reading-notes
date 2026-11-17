#!/usr/bin/env python3
"""Verify arithmetic in note 52 (Charlie Munger / Wheeler, Munger & Co.).
All inputs are figures stated in the note's cited sources (Buffett's
1984 'Superinvestors of Graham-and-Doddsville' Table 5 yearly results,
as republished in The Intelligent Investor appendix and The Warren
Buffett Portfolio ch.3; Berkshire Hathaway 2023 shareholder letter;
Buffett's See's Candies figures from the 1991/2007 Berkshire letters as
transcribed in secondary sources). This script only checks internal
arithmetic consistency. Clean-room, self-written.
"""
from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

overall = [30.1, 71.7, 49.7, 8.4, 12.4, 56.2, 40.4, 28.3, -0.1, 25.4, 8.3, -31.9, -31.5, 73.2]
limited = [20.1, 47.8, 33.1, 6.0, 8.3, 37.5, 27.0, 21.3, -0.1, 20.6, 7.3, -31.9, -31.5, 73.2]
dow     = [-7.6, 20.6, 18.7, 14.2, -15.7, 19.0, 7.7, -11.6, 8.7, 9.8, 18.2, -23.1, -13.1, 44.4]

def prod(xs):
    p = 1.0
    for x in xs:
        p *= 1 + x / 100
    return p

# 1. Life dates: born 1924-01-01, died 2023-11-28 at 99; 100th birthday
#    would have been 2024-01-01, 34 days later (Berkshire's 2023 letter
#    phrases it as 'just 33 days before' by exclusive counting).
check("1 age at death 99", date(2023, 11, 28).year - 1924 - ((11, 28) < (1, 1)) == 99)
check("1 days to 100th birthday = 34", (date(2024, 1, 1) - date(2023, 11, 28)).days == 34)
check("1 met Buffett 1959 at 35", 1959 - 1924 == 35)
check("1 partnership start 1962 at 38", 1962 - 1924 == 38)

# 2. Overall partnership 1962-1975 (14 years): yearly product must
#    reproduce Table 5's compound gain 1156.7% (factor 12.567) and the
#    stated compound annual rate 19.8%.
po = prod(overall)
check("2 overall factor ~12.567 (gain 1156.7%)", abs(po - 12.567) < 0.01)
check("2 overall CAGR ~19.8%", abs(po ** (1 / 14) * 100 - 119.8) < 0.15)

# 3. Limited partners: product = gain 500.1% (factor 6.001), CAGR 13.7%;
#    fee wedge vs overall = 6.1pp; LP terminal is 47.75% of overall.
pl = prod(limited)
check("3 LP factor ~6.001 (gain 500.1%)", abs(pl - 6.001) < 0.01)
check("3 LP CAGR ~13.7%", abs(pl ** (1 / 14) * 100 - 113.7) < 0.15)
check("3 wedge 6.1pp", abs(19.8 - 13.7 - 6.1) < 1e-9)
check("3 LP terminal 47.75% of overall", abs(pl / po * 100 - 47.75) < 0.1)

# 4. Dow column in Table 5: compound gain 96.8% (factor 1.968), CAGR
#    5.0%; overall terminal / Dow terminal = 6.39x.
pd_ = prod(dow)
check("4 Dow factor ~1.968 (gain 96.8%)", abs(pd_ - 1.968) < 0.01)
check("4 Dow CAGR ~5.0%", abs(pd_ ** (1 / 14) * 100 - 105.0) < 0.15)
check("4 overall/Dow terminal ~6.39x", abs(po / pd_ - 6.39) < 0.02)

# 5. USD 10,000 terminals: overall 125,670; LP 60,010; Dow 19,680.
check("5 terminals", abs(po * 10000 - 125670) < 100 and abs(pl * 10000 - 60010) < 100 and abs(pd_ * 10000 - 19680) < 100)

# 6. Arithmetic mean of overall yearly results = 24.3% (as printed in
#    The Warren Buffett Portfolio table), 4.53pp above the 19.8%
#    compound rate: the volatility drag of a concentrated book.
check("6 arithmetic mean ~24.33%", abs(sum(overall) / 14 - 24.33) < 0.01)
check("6 mean minus CAGR ~4.5pp", abs(sum(overall) / 14 - 19.8 - 4.53) < 0.05)

# 7. Negative years: overall has 3 of 14 (1970 -0.1, 1973 -31.9,
#    1974 -31.5) = 21.43%; the other 11 are positive.
neg = [x for x in overall if x < 0]
check("7 three negative years", len(neg) == 3 and neg == [-0.1, -31.9, -31.5])
check("7 negative share 21.43%", abs(len(neg) / 14 * 100 - 21.43) < 0.01)

# 8. The 1973-74 hole: 0.681 x 0.685 - 1 = -53.35%; recovery to the
#    end-1972 level needs +114.37%.
hole = 0.681 * 0.685
check("8 two-year hole -53.35%", abs((hole - 1) * 100 + 53.35) < 0.01)
check("8 recovery needs +114.37%", abs((1 / hole - 1) * 100 - 114.37) < 0.05)

# 9. Path check vs Table 5 compound rows: through 1972 gain 1455.5%
#    (factor 15.555); through 1974 gain 625.6% (factor 7.256); the
#    +73.2% year of 1975 still leaves the fund 19.21% below its
#    end-1972 peak.
p72, p74 = prod(overall[:11]), prod(overall[:13])
check("9 through-1972 factor ~15.555", abs(p72 - 15.555) < 0.01)
check("9 through-1974 factor ~7.256", abs(p74 - 7.256) < 0.01)
check("9 after 1975 still -19.21% vs 1972 peak", abs((po / p72 - 1) * 100 + 19.21) < 0.05)

# 10. See's Candies (Blue Chip, early 1972): paid USD 25m; sellers had
#     asked USD 30m (16.67% less paid); net tangible assets USD 8m, so
#     price = 3.125x tangible assets; pre-tax earnings about USD 4m, so
#     price = 6.25x pre-tax; after-tax about USD 2m, so about 12.5x.
check("10 discount vs ask 16.67%", abs((1 - 25 / 30) * 100 - 16.67) < 0.01)
check("10 price/tangible 3.125x", abs(25 / 8 - 3.125) < 1e-9)
check("10 price/pretax 6.25x", abs(25 / 4 - 6.25) < 1e-9)
check("10 price/after-tax ~12.5x", abs(25 / 2 - 12.5) < 1e-9)

# 11. See's by 2007 (Buffett 2007 letter figures): sales USD 383m,
#     pre-tax USD 82m, capital required USD 40m = 5.00x the 1972
#     USD 8m; incremental capital 32m; cumulative pre-tax earnings
#     USD 1.35bn = 54.0x the USD 25m purchase price.
check("11 capital 5.00x, increment 32m", abs(40 / 8 - 5.0) < 1e-9 and 40 - 8 == 32)
check("11 cumulative pretax 54.0x price", abs(1350 / 25 - 54.0) < 1e-9)
check("11 2007 pretax margin 21.41%", abs(82 / 383 * 100 - 21.41) < 0.01)

# 12. Berkshire-era tenures: vice chairman 1978-2023 = 45 years;
#     Daily Journal chairman 1977-2023 = 46 years; Wesco chairman
#     1984-2011 = 27 years; partnership 1962-1975 inclusive = 14 years.
check("12 tenures 45/46/27/14", (2023 - 1978, 2023 - 1977, 2011 - 1984, 1975 - 1962 + 1) == (45, 46, 27, 14))

print("ALL PASSED" if ok else "SOME FAILED")
