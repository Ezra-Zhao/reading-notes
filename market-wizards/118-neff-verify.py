#!/usr/bin/env python3
"""118 Neff (Akre) verify: all numbers from Akre Focus ETF Q3 2026 Commentary
(performance table as of 09/30/2026, top-ten & sector tables) and the
2025-10-16 ETF Prospectus (manager identity). Decimal throughout."""
from decimal import Decimal as D
from datetime import date

ok = 0
def chk(cond, label):
    global ok
    assert cond, label
    ok += 1
    print("PASS", label)

def close(a, b, tol=D('0.02')):
    return abs(a - b) <= tol

# G1 identity / tenure (Prospectus 2025-10-16: John H. Neff PM since 2014;
# 2014 summary prospectus: since August 2014)
tenure_days = (date(2026, 9, 30) - date(2014, 8, 1)).days
chk(tenure_days == 4443, "G1 Neff tenure from Aug 2014 = 4443 days")
chk(close(D(tenure_days) / D('365.25'), D('12.16')), "G1 tenure ~12.16 years")
sole_days = (date(2026, 9, 30) - date(2023, 9, 27)).days
chk(sole_days == 1099, "G1 sole-manager span from 2023-09-27 = 1099 days (MFO)")

# G2 fund life
life = (date(2026, 9, 30) - date(2009, 8, 31)).days
chk(life == 6239, "G2 fund life 2009-08-31..2026-09-30 = 6239 days")
chk(close(D(tenure_days) / D(life) * 100, D('71.21')), "G2 Neff PM span ~71.21% of fund life")

# G3 quarter split: Jul +7.97, Aug +7.26, Sep -14.38 -> Q3 printed -0.84
jul_aug = (1 + D('7.97') / 100) * (1 + D('7.26') / 100)
chk(close((jul_aug - 1) * 100, D('15.81')), "G3 Jul+Aug compound ~+15.81%")
q3 = jul_aug * (1 + D('-14.38') / 100)
chk(close((q3 - 1) * 100, D('-0.84')), "G3 Jul*Aug*Sep compound ~-0.84% = printed Q3")
chk(close((1 / (1 + D('-14.38') / 100) - 1) * 100, D('16.80')), "G3 recovering September needs ~+16.80%")

# G4 YTD split: YTD -19.55 with Q3 -0.84 -> H1 reverse
h1 = D('0.8045') / q3
chk(close((h1 - 1) * 100, D('-18.86')), "G4 H1 2026 reverse ~-18.86%")
h1b = D('1.1275') / D('1.0230')
chk(close((h1b - 1) * 100, D('10.22')), "G4 benchmark H1 reverse ~+10.22%")

# G5 one-year split: 1Y -21.80 with Q3 -0.84 -> prior nine months
p9 = D('0.7820') / q3
chk(close((p9 - 1) * 100, D('-21.13')), "G5 prior nine months reverse ~-21.13%")
p9b = D('1.1574') / D('1.0230')
chk(close((p9b - 1) * 100, D('13.14')), "G5 benchmark prior nine months ~+13.14%")

# G6 excess table (NAV vs S&P 500 TR), all nine windows negative
rows = [('1M', D('-14.38'), D('-0.35'), D('-14.03')), ('3M', D('-0.84'), D('2.30'), D('-3.14')),
        ('YTD', D('-19.55'), D('12.75'), D('-32.30')), ('1Y', D('-21.80'), D('15.74'), D('-37.54')),
        ('3Y', D('3.98'), D('22.89'), D('-18.91')), ('5Y', D('0.50'), D('13.79'), D('-13.29')),
        ('10Y', D('10.44'), D('15.33'), D('-4.89')), ('15Y', D('12.82'), D('15.68'), D('-2.86')),
        ('SI', D('12.35'), D('14.61'), D('-2.26'))]
for name, f, b, ex in rows:
    chk(f - b == ex and ex < 0, f"G6 excess {name} = {ex}")

# G7 cumulative from annualized
chk(close((1 + D('10.44') / 100) ** 10, D('2.70'), D('0.01')), "G7 10y fund ~2.70x")
chk(close((1 + D('15.33') / 100) ** 10, D('4.16'), D('0.01')), "G7 10y benchmark ~4.16x")
chk(close((1 + D('12.82') / 100) ** 15, D('6.11'), D('0.01')), "G7 15y fund ~6.11x")
chk(close((1 + D('15.68') / 100) ** 15, D('8.89'), D('0.01')), "G7 15y benchmark ~8.89x")
yrs = D(life) / D('365.25')
chk(close((D('1.1235')) ** yrs, D('7.31'), D('0.02')), "G7 since-inception fund ~7.31x")
chk(close((D('1.1461')) ** yrs, D('10.27'), D('0.02')), "G7 since-inception benchmark ~10.27x")

# G8 market price vs NAV gaps
chk(D('-14.48') - D('-14.38') == D('-0.10'), "G8 1M market-minus-NAV = -0.10")
chk(D('-0.98') - D('-0.84') == D('-0.14'), "G8 3M market-minus-NAV = -0.14")
chk(D('-21.94') - D('-21.80') == D('-0.14'), "G8 1Y market-minus-NAV = -0.14")

# G9 top ten concentration
top10 = [D(x) for x in ['14.3', '12.6', '7.4', '7.1', '6.9', '6.8', '6.8', '6.6', '5.2', '4.2']]
chk(sum(top10) == D('77.9'), "G9 top ten sum = 77.9%")
chk(top10[0] + top10[1] == D('26.9'), "G9 top two (Mastercard+Constellation) = 26.9%")
groups = D('14.3') + D('7.4') + D('12.6') + D('7.1') + D('6.6') + D('6.8') + D('6.9')
chk(groups == D('61.7'), "G9 commentary-discussed groups = 61.7% (~60% as text says)")

# G10 sectors
sectors = [D(x) for x in ['50.1', '33.5', '5.2', '4.7', '3.7', '2.8']]
chk(sum(sectors) == D('100.0'), "G10 sector weights sum = 100.0%")
chk(sectors[0] + sectors[1] == D('83.6'), "G10 Financials+InfoTech = 83.6%")

# G11 valuation & balance-sheet stats from commentary text
chk(close((1 - D('16.3') / D('25')) * 100, D('34.80')), "G11 16.3x vs 10y avg 25x = 34.80% discount")
chk(close((1 - D('16.3') / D('22')) * 100, D('25.91')), "G11 16.3x vs since-inception avg 22x = 25.91% discount")
chk(close((1 - D('1.54') / D('2.13')) * 100, D('27.70')), "G11 debt/EBITDA 1.54 vs 2.13 = 27.70% lower")

# G12 cash move
chk(D('2.8') - D('1.7') == D('1.1'), "G12 cash 1.7% -> 2.8% = +1.1pp")
chk(close((D('2.8') / D('1.7') - 1) * 100, D('64.71')), "G12 cash relative rise ~+64.71%")

print(f"ALL {ok} ASSERTIONS PASSED (12 groups)")
