#!/usr/bin/env python3
"""Verify arithmetic for note 38 (Monroe Trout). Inputs from public
sources cited in the note: Schwager The New Market Wizards (1992)
interview as summarised by Macro Ops 2023-07-07 (five-year average
return 67%, maximum drawdown just over 8%, risk rules 1.5% per trade /
4% per day / 10% per month, 1991-01-09 loss about USD 9.5m, about 700
S&P contracts); Alchetron/Wikipedia profile (born 1962-01-22, Harvard
1984 magna cum laude, NCZ Sep 1984 to Jun 1986, founded Trout Trading
Jul 1986, 69 profitable months out of 79, summer job in 1978 said to be
at age 17); Sports-Reference college stats via Wikipedia (87 games,
8.5 points, 5.1 rebounds, 58.2% shooting, height 6 ft 9 in); MAR Hedge
summary carried by Elite Trader 2002-01-17 (fund almost USD 3bn,
average annual net return 21.5% over its 14-year life, closed to new
investors since 1995, Tewksbury joined 1992, CEO 1999, takeover
2002-04-01); NYT 2002-01-19 founder-leaving report; reported net
worth in excess of USD 900m at retirement."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Early five-year average vs long-run fund record
early = 1.67 ** 5
longrun = 1.215 ** 14
assert close(early, 12.99, 0.01) and close(longrun, 15.28, 0.01) and close(1.67 ** 14, 1312.29, 0.5)
print(f"1 record OK if the early 67% average were compounded it gives {early:.2f}x in 5 years; the fund's later 14-year net record at 21.5% gives {longrun:.2f}x -- and 67% compounded for 14 years would be {1.67**14:.0f}x, so the 67% figure cannot describe the fund's whole life; the two figures cover different windows and bases (early/gross vs 14-year/net)")

# 2. Profitable-months: the 69-of-79 count vs the 87% summary vs the 87-of-90 blog version
assert close(69 / 79 * 100, 87.34, 0.01) and 79 - 69 == 10 and close(87 / 90 * 100, 96.67, 0.01)
print("2 months OK 69 profitable out of 79 months = 87.34%, which is exactly the widely quoted '87% of months' -- the count and the percentage reconcile; a later blog version '87 profitable months out of 90' would be 96.67% and does not reconcile with either, registered as an amplified variant, not adopted")

# 3. Last-ten-years variant: only 6 negative months (single secondary thread)
assert close(6 / 120 * 100, 5.00, 0.001) and close(114 / 120 * 100, 95.00, 0.001)
print("3 tenyear OK '6 negative months in the last ten years' = 6/120 = 5.00% negative, 95.00% non-negative -- a different window from group 2, registered side by side, not merged")

# 4. Risk ladder ratios
assert close(4 / 1.5, 2.67, 0.01) and close(10 / 4, 2.50, 0.001) and close(10 / 1.5, 6.67, 0.01)
print("4 ladder OK per-trade 1.5% -> per-day 4% is 2.67x the single-trade limit; per-month 10% is 2.50x the daily limit and 6.67x the single-trade limit")

# 5. Return over drawdown, and recovery from that drawdown
assert close(67 / 8, 8.38, 0.01) and close((1 / (1 - 0.08) - 1) * 100, 8.70, 0.01)
print("5 ratio OK early average return 67% over a drawdown of just over 8% is a return/drawdown ratio of about 8.38 using 8% exactly (an upper bound, since the drawdown is 'just over' 8%); recovering from -8% needs +8.70%")

# 6. 1991-01-09 loss arithmetic (S&P futures multiplier USD 500/point in 1991)
per_contract = 9_500_000 / 700
points = per_contract / 500
assert close(per_contract, 13571.43, 0.01) and close(points, 27.14, 0.01)
print(f"6 jan1991 OK USD 9.5m over about 700 contracts = USD {per_contract:,.0f} per contract; at the 1991 big-contract multiplier of USD 500 per point that is about {points:.2f} points per contract -- so the retold 'lost 1,200 points' cannot be a per-contract index move; it only makes sense as an aggregate or a loose retelling, registered as such")

# 7. The 4% daily rule and the implied equity scale
assert close(9_500_000 / 0.04, 237_500_000, 1)
print("7 trigger OK he reports realising the book was down over 4% that day and liquidating everything by the close; if USD 9.5m were exactly 4% the equity would be USD 237.5m -- since the loss was over 4%, USD 237.5m is an upper-bound scale marker for the equity then at risk, not a reported AUM figure")

# 8. Career timeline
months_ncz = (1986 - 1984) * 12 + (6 - 9)
months_firm = (2002 - 1986) * 12 + (4 - 7)
assert months_ncz == 21 and months_firm == 189 and 2002 - 14 == 1988
print("8 career OK NCZ Sep 1984 to Jun 1986 = 21 months; he left and founded Trout Trading in Jul 1986, the next month; Jul 1986 to the 2002-04-01 handover = 189 months = 15 years 9 months; the MAR '14-year life' of the fund points to about 1988, two years after the company was founded -- fund life and company age are different scopes, registered side by side")

# 9. Age checks: the 1978 summer job and the 2002 retirement
assert 1978 - 1962 == 16 and (date(2002, 1, 22) - date(2002, 1, 19)).days == 3
age_handover = (date(2002, 4, 1) - date(1962, 1, 22)).days / 365.25
assert close(age_handover, 40.19, 0.01)
print(f"9 age OK born 1962-01-22, so in summer 1978 he was 16, not 17 as the profile wording says -- a one-year wording error, registered, the 1978 start itself is not disputed; the NYT founder-leaving report is dated 2002-01-19, three days before his 40th birthday, while the actual handover on 2002-04-01 was at age {age_handover:.2f} -- 'retired at 40' fits the handover date, not the announcement date")

# 10. Harvard basketball totals, height, scale at exit, closed period
assert close(87 * 8.5, 739.5, 0.01) and close(87 * 5.1, 443.7, 0.01) and close(81 * 2.54, 205.74, 0.01)
assert close(900 / 3000 * 100, 30.00, 0.001) and 2002 - 1995 == 7 and 2002 - 1992 == 10
print("10 scale OK 87 college games at the rounded averages of 8.5 points and 5.1 rebounds imply about 740 points and about 444 rebounds in total (derived from rounded averages, scale only); 6 ft 9 in = 205.74 cm; reported net worth over USD 900m is over 30.00% of the fund's almost USD 3bn at handover (a wealth-to-AUM ratio, not a return); the fund had been closed to new investors since 1995, seven years by 2002; Tewksbury joined in 1992, ten years before taking over")

print("ALL PASS")
