#!/usr/bin/env python3
"""Verify arithmetic in note 47 (Feng Mingyuan / Cinda Aoyagi funds).
All inputs are figures stated in the note's cited sources; this script
only checks internal arithmetic consistency. Clean-room, self-written.
"""
from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Flagship tenure: started managing Xinao New Energy in Oct 2016;
#    co-manager added 2026-11-06 -> just over 10 full years.
check("1 flagship tenure reaches 10 years by Oct 2026", 2026 - 2016 == 10)
days = (date(2026, 11, 6) - date(2016, 10, 1)).days
check("1 days from 2016-10-01 to 2026-11-06 >= 3680", days >= 3680)

# 2. Tenure return >231% by 2020-10-09 means factor > 3.31.
check("2 +231% factor 3.31", abs((1 + 2.31) - 3.31) < 1e-9)

# 3. Zhiyuan A Q3 2026 gap: -32.32 vs benchmark -12.40 = -19.92pp.
check("3 Q3 gap -19.92pp", abs((-32.32 - (-12.40)) - (-19.92)) < 1e-9)

# 4. Zhiyuan A 6M/1Y/3Y gaps.
check("4 6M gap +28.04pp", abs((25.97 - (-2.07)) - 28.04) < 1e-9)
check("4 1Y gap +26.90pp", abs((22.22 - (-4.68)) - 26.90) < 1e-9)
check("4 3Y gap +58.69pp", abs((79.75 - 21.06) - 58.69) < 1e-9)

# 5. Implied Q2 2026 single quarter from 6M +25.97% and Q3 -32.32%.
q2 = 1.2597 / (1 - 0.3232) - 1
check("5 implied Q2 ~+86.14%", abs(q2 * 100 - 86.14) < 0.05)

# 6. Since inception A: +30.48% vs -3.81% = +34.29pp; NAV 1.3048 ~ 1.30.
check("6 inception gap +34.29pp", abs((30.48 - (-3.81)) - 34.29) < 1e-9)
check("6 NAV implied 1.3048 rounds to 1.30", round(1.3048, 2) == 1.30)
check("6 conflicting 'tenure 8.52%' != inception 30.48% (registered, unused)",
      abs(8.52 - 30.48) > 20)

# 7. Scale back-out: A 12.86 after -39.84% QoQ; C 2.21 after -41.66% QoQ.
a_q2 = 12.86 / (1 - 0.3984)
c_q2 = 2.21 / (1 - 0.4166)
check("7 A Q2 scale ~21.38", abs(a_q2 - 21.38) < 0.02)
check("7 C Q2 scale ~3.79", abs(c_q2 - 3.79) < 0.02)
check("7 A+C Q3 total 15.07", abs((12.86 + 2.21) - 15.07) < 1e-9)

# 8. Recovery from -32.32% needs +47.76%.
check("8 recovery +47.76%", abs((1 / (1 - 0.3232) - 1) * 100 - 47.76) < 0.01)

# 9. C class: Q3 -32.39 vs -12.40 = -19.99pp; A-C Q3 spread 0.07pp;
#    inception C +28.06 vs A +30.48 spread 2.42pp.
check("9 C Q3 gap -19.99pp", abs((-32.39 - (-12.40)) - (-19.99)) < 1e-9)
check("9 A-C Q3 spread 0.07pp", abs(abs(abs(-32.32) - abs(-32.39)) - 0.07) < 1e-9)
check("9 A-C inception spread 2.42pp", abs((30.48 - 28.06) - 2.42) < 1e-9)

# 10. 3Y annualised: A 1.7975^(1/3)-1 ~21.57%; benchmark ~6.59%.
check("10 A 3Y annualised ~21.57%", abs((1.7975 ** (1/3) - 1) * 100 - 21.57) < 0.05)
check("10 bench 3Y annualised ~6.59%", abs((1.2106 ** (1/3) - 1) * 100 - 6.59) < 0.05)

print("ALL PASSED" if ok else "SOME FAILED")
