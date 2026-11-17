#!/usr/bin/env python3
"""Verify arithmetic in note 46 (Peter Lynch / Fidelity Magellan).
All inputs are figures stated in the note's cited sources; this script
only checks internal arithmetic consistency. Clean-room, self-written.
"""
from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure and ages: born 1944-01-19; took over May 1977; retired 1990-05-31.
tenure_years = 1990 - 1977
check("1 tenure 13 years", tenure_years == 13)
age_takeover = (date(1977, 5, 1) - date(1944, 1, 19)).days / 365.25
age_retire = (date(1990, 5, 31) - date(1944, 1, 19)).days / 365.25
check("1 age 33 at takeover", 33.0 < age_takeover < 34.0)
check("1 age 46 at retirement", 46.0 < age_retire < 47.0)

# 2. Compounding at 29.2% for 13 years.
factor = 1.292 ** 13
check("2 factor ~27.95x", abs(factor - 27.952) < 0.01)
check("2 $10,000 -> $279,519.86 (independent published figure)",
      abs(10000 * factor - 279519.86) < 1.0)

# 3. S&P 500 comparison at the secondary-compilation figure of 15.8%/yr.
sp_factor = 1.158 ** 13
check("3 S&P factor ~6.73x", abs(sp_factor - 6.733) < 0.01)
check("3 annual gap 13.40pp", abs((29.2 - 15.8) - 13.40) < 1e-9)
check("3 terminal ratio ~4.15x", abs(factor / sp_factor - 4.15) < 0.01)

# 4. Beat rate: outperformed in 11 of 13 years.
check("4 beat share 84.62%", abs(11 / 13 * 100 - 84.62) < 0.01)
check("4 losing years = 2", 13 - 11 == 2)

# 5. AUM growth: $18m -> $14,000m.
check("5 AUM multiple 777.78x", abs(14000 / 18 - 777.78) < 0.01)
check("5 '660x' version inconsistent (18*660 != 14,000)",
      18 * 660 != 14000)

# 6. Performance alone cannot explain terminal AUM (inflows did the rest).
perf_only = 18 * factor
check("6 performance-only AUM ~$503.14m", abs(perf_only - 503.14) < 0.5)
check("6 performance share of $14bn ~3.59%",
      abs(perf_only / 14000 * 100 - 3.59) < 0.01)

# 7. Holdings expansion: ~60 stocks at takeover, advised 25-30, 1,400 in 1989.
check("7 1400/60 = 23.33x", abs(1400 / 60 - 23.33) < 0.01)
check("7 1400/25 = 56.00x the advised floor", abs(1400 / 25 - 56.0) < 1e-9)

# 8. Selected yearly gaps from the fund performance table (percentage points).
rows = [(1977, 14.46, -7.16, 21.62), (1979, 51.73, 18.61, 33.12),
        (1980, 69.94, 32.50, 37.44), (1985, 43.11, 31.73, 11.38),
        (1989, 34.58, 31.69, 2.89)]
check("8 yearly gaps", all(abs((m - s) - d) < 0.011 for _, m, s, d in rows))

# 9. PEG rule-of-thumb arithmetic from his own framework.
check("9 PEG fair: PE 20 / growth 20 = 1.0", abs(20 / 20 - 1.0) < 1e-9)
check("9 PEG rich: PE 40 / growth 20 = 2.0", abs(40 / 20 - 2.0) < 1e-9)
check("9 PEG cheap: PE 10 / growth 20 = 0.5", abs(10 / 20 - 0.5) < 1e-9)

# 10. Career timeline gaps: research director 1974-1977, books 1989/1993/1997.
check("10 research director 3 years", 1977 - 1974 == 3)
check("10 first book 1989 is 1 year before retirement", 1990 - 1989 == 1)
check("10 book gaps 4 and 4 years", (1993 - 1989) == 4 and (1997 - 1993) == 4)

print("ALL PASSED" if ok else "SOME FAILED")
raise SystemExit(0 if ok else 1)
