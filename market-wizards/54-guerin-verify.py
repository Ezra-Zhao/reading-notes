#!/usr/bin/env python3
"""Verify arithmetic in note 54 (Rick Guerin / Pacific Partners, Ltd.).
All inputs are the yearly figures in Table 6 of Warren Buffett's 1984
essay "The Superinvestors of Graham-and-Doddsville" (Columbia Business
School, Hermes, Fall 1984), read in full this round from Columbia's own
republication. This script only checks internal arithmetic consistency.
Clean-room, self-written.
"""

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

def comp(rs):
    p = 1.0
    for r in rs:
        p *= 1 + r / 100
    return p

overall = [32.0, 36.7, 180.1, 171.9, 97.1, -7.2, 16.4, 17.1, -42.1, -34.4,
           31.2, 127.8, 27.1, 37.9, 48.2, 24.1, 8.0, 32.0, 24.8]
lp = [21.2, 24.5, 120.1, 114.6, 64.7, -7.2, 10.9, 12.8, -42.1, -34.4,
      23.4, 127.8, 20.3, 28.4, 36.1, 18.1, 6.0, 24.0, 18.6]
sp = [12.4, -10.1, 23.9, 11.0, -8.4, 3.9, 14.6, 18.9, -14.8, -26.4,
      37.2, 23.6, -7.4, 6.4, 18.2, 32.3, -5.0, 21.4, 22.4]

# 1. Stated totals vs stated CAGRs (19 years): overall +22,200.0% at
#    32.9%, LP +5,530.2% at 23.6%, S&P +316.4% at 7.8%.
check("1 overall CAGR from stated total ~32.9", abs((223.0 ** (1/19) - 1) * 100 - 32.9) < 0.05)
check("1 LP CAGR from stated total ~23.6", abs((56.302 ** (1/19) - 1) * 100 - 23.6) < 0.05)
check("1 SP CAGR from stated total ~7.8", abs((4.164 ** (1/19) - 1) * 100 - 7.8) < 0.05)

# 2. Compounding the printed yearly rows reproduces the stated totals
#    within rounding of the one-decimal yearly inputs.
check("2 overall yearly compound ~22206%", abs((comp(overall) - 1) * 100 - 22206.0) < 1.0)
check("2 LP yearly compound ~5531%", abs((comp(lp) - 1) * 100 - 5531.3) < 1.0)
check("2 SP yearly compound ~317%", abs((comp(sp) - 1) * 100 - 316.8) < 1.0)

# 3. Terminal values per USD 10,000 and terminal ratios.
check("3 10k overall 2,230,000", abs(10000 * 223.0 - 2230000) < 1e-6)
check("3 10k LP 563,020", abs(10000 * 56.302 - 563020) < 1e-6)
check("3 10k SP 41,640", abs(10000 * 4.164 - 41640) < 1e-6)
check("3 overall/LP terminal ratio ~3.96", abs(223.0 / 56.302 - 3.96) < 0.01)
check("3 overall/SP terminal ratio ~53.55", abs(223.0 / 4.164 - 53.55) < 0.01)

# 4. Fee wedge: CAGR gap 32.9 - 23.6 = 9.3pp; LP keeps only about a
#    quarter of the overall terminal multiple (56.302/223 = 25.25%).
check("4 CAGR wedge 9.3pp", abs(32.9 - 23.6 - 9.3) < 1e-9)
check("4 LP share of terminal ~25.25%", abs(56.302 / 223.0 * 100 - 25.25) < 0.01)

# 5. First five years (1965-1969): overall compounds to about 27.09x,
#    LP to about 11.74x.
check("5 1965-69 overall ~27.09x", abs(comp(overall[:5]) - 27.09) < 0.01)
check("5 1965-69 LP ~11.74x", abs(comp(lp[:5]) - 11.74) < 0.01)

# 6. Peak before the crash: through 1972 overall is about 34.26x.
check("6 through-1972 overall ~34.26x", abs(comp(overall[:8]) - 34.26) < 0.01)

# 7. 1973-1974: overall -42.1% then -34.4% compounds to -62.02%;
#    recovery to the old peak needs +163.28%. S&P same two years -37.29%.
check("7 1973-74 overall -62.02%", abs((0.579 * 0.656 - 1) * 100 + 62.02) < 0.01)
check("7 recovery needed +163.28%", abs((1 / (0.579 * 0.656) - 1) * 100 - 163.28) < 0.01)
check("7 1973-74 SP -37.29%", abs((0.852 * 0.736 - 1) * 100 + 37.29) < 0.01)

# 8. The climb back: 1975-1976 overall compounds to about 2.9887x
#    (+198.87%); measured from end-1972, the fund only exceeds its old
#    peak in 1976 (factor about 1.1352), not in 1975 (about 0.4983).
check("8 1975-76 overall ~2.9887x", abs(comp(overall[10:12]) - 2.9887) < 0.001)
check("8 vs 1972 peak: 1975 ~0.4983, 1976 ~1.1352",
      abs(comp(overall[8:11]) - 0.4983) < 0.001 and abs(comp(overall[8:12]) - 1.1352) < 0.001)

# 9. Negative years: overall and LP each have exactly 3 losing years in
#    19 (1970, 1973, 1974) = 15.79%; the S&P has 6 = 31.58%.
check("9 neg years overall 3 / LP 3 / SP 6",
      sum(1 for x in overall if x < 0) == 3 and sum(1 for x in lp if x < 0) == 3
      and sum(1 for x in sp if x < 0) == 6)
check("9 neg share 15.79% vs 31.58%", abs(3/19*100 - 15.79) < 0.01 and abs(6/19*100 - 31.58) < 0.01)

# 10. Arithmetic means vs CAGRs (volatility drag): overall mean about
#     43.62% vs CAGR 32.9% (gap about 10.7pp); LP mean about 30.94% vs
#     23.6%; S&P mean about 9.16% vs 7.8%.
check("10 overall mean ~43.62", abs(sum(overall)/19 - 43.62) < 0.01)
check("10 LP mean ~30.94", abs(sum(lp)/19 - 30.94) < 0.01)
check("10 SP mean ~9.16", abs(sum(sp)/19 - 9.16) < 0.01)

# 11. The 1976 anomaly: overall and LP print the same +127.8% that year,
#     a zero fee gap, unlike every other positive year in the table.
check("11 1976 overall == LP == 127.8", overall[11] == lp[11] == 127.8)
check("11 other positive years LP < overall",
      all(lp[i] < overall[i] for i in range(19) if overall[i] > 0 and i != 11))

# 12. Single-year extremes: best overall year 1967 +180.1%, worst 1973
#     -42.1%; best-vs-worst S&P spread in table is 37.2 vs -26.4.
check("12 best overall 180.1 / worst -42.1", max(overall) == 180.1 and min(overall) == -42.1)
check("12 SP best 37.2 / worst -26.4", max(sp) == 37.2 and min(sp) == -26.4)

print("ALL PASSED" if ok else "SOME FAILED")
