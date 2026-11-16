#!/usr/bin/env python3
"""Verify arithmetic for note 36 (Brian Gelber). Inputs from public
sources cited in the note: Gelber Group official leadership page
(CEO; Hamilton College class of 1976, honors BA in economics;
managed Salomon Brothers and Citigroup accounts), Brian Gelber's
sworn declaration dated 2004-08-03 in TD Ameritrade v. Trading
Technologies, PTAB CBM2014-00136 Exhibit 2024 (Chairman, Gelber
Group LLC, 141 W. Jackson 21st Floor Chicago; Full Clearing Member
of CBOT and CME since 1989; about 5-10% of total electronic volume
on CBOT and CME; broker from 1977 on the T-bond floor, own account
from 1979, one of the largest brokers/locals 1979-1985, left the
floor 1986; first interactive computer trading 1998; Patsystems
chosen 1999), Schwager interview excerpt reprinted by TurtleTrader
(graduated 1976, Salt Lake City ad, boiler-room licence then quit,
Thomson McKinnon USD 800/month cold-calling, Ginnie Mae desk,
opened almost every mortgage banker account in Salt Lake City),
MarketsWiki / SEC comment letter 2023-06-02 (Gelber Group founded
1982 by Brian and Frank Gelber; 200+ employees as of 2024), and
CFTC Order dated 2013-02-08 (USD 750,000 penalty,
two incidents, no admission or denial; docket number is redacted
in the copy opened this run, so no docket number is cited)."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Thomson McKinnon pay: USD 800 per month
assert 800 * 12 == 9600
print("1 pay OK Schwager interview salary USD 800/month = USD 9,600/year at Thomson McKinnon, cold-calling, accounts he opened were his")

# 2. Entry timeline: graduation to broker start to own account
assert 1977 - 1976 == 1 and 1979 - 1977 == 2
print("2 entry OK Hamilton class of 1976 (official leadership page) -> broker on CBOT T-bond floor in 1977 = 1 year later (declaration); broker-only phase 1977->1979 = 2 years before trading for his own account in 1979")

# 3. Largest broker/local period 1979-1985
assert 1985 - 1979 == 6
print("3 largest OK declaration: one of the largest T-bond brokers/locals 1979-1985 = 6-year difference, 7 calendar years inclusive")

# 4. Floor span and the two different 'leaving the floor' dates
assert 1986 - 1977 == 9 and 1997 - 1986 == 11
print("4 floor OK personal floor span 1977->1986 = 9 years (declaration: 'In 1986, I left the floor'); MarketsWiki firm-level screen/prop shift in 1997 is a different subject, 11 years later -- registered separately, never merged")

# 5. Founding and clearing membership
assert 1982 - 1977 == 5 and 1986 - 1982 == 4 and 1989 - 1982 == 7
print("5 founding OK Gelber Group founded 1982 (MarketsWiki + SEC 2023 letter) = 5 years after his 1977 start and 4 years before he personally left the floor, so founding overlaps the floor era; Full Clearing Member of CBOT/CME since 1989 = 7 years after founding (declaration)")

# 6. Declaration experience check, 2004-08-03
assert 2004 - 1977 == 27 and 2004 - 1989 == 15
print("6 declaration OK sworn 2004-08-03: 'over 25 years experience' vs 2004-1977 = 27 years, consistent with a 2-year margin; clearing-member tenure by then 2004-1989 = 15 years")

# 7. Screen transition lag
assert 1998 - 1986 == 12 and 1999 - 1998 == 1
print("7 screen OK left floor 1986 -> first interactive computer trading 1998 = 12-year gap; Patsystems chosen as primary vendor in 1999 = 1 year later, on cost (declaration); later switch to Trading Technologies MD Trader despite higher cost, on trader preference")

# 8. Electronic volume share in the declaration
assert close((5 + 10) / 2, 7.5, 0.001) and close(10 / 5, 2.0, 0.001) and 10 - 5 == 5
print("8 volume OK declaration: Gelber Group about 5-10% of total electronic volume on CBOT and CME -- midpoint 7.5%, range width 5pp, upper bound is 2.00x the lower bound; a share range, not a single figure")

# 9. CFTC order arithmetic: incident span and penalty
d = (date(2010, 2, 16) - date(2009, 8, 20)).days
assert d == 180
assert 750000 == 750 * 1000
print(f"9 cftc OK CFTC Order dated 2013-02-08: first incident at least 2009-08-20 to 2010-02-16 = {d} days (NASDAQ E-mini pre-open non-bona-fide orders), second incident Mar-Aug 2010 (Russell wash trades for ICE rebates); civil penalty USD 750,000, firm consented without admitting or denying -- firm-level record, the order does not name Brian Gelber as the trader in either incident")

# 10. Long-run scale and book timing
assert 2024 - 1982 == 42 and 2010 - 2004 == 6 and 1989 - 1976 == 13
print("10 scale OK founded 1982 -> 200+ employees as of 2024 (MarketsWiki) = 42 years; algorithmic division founded 2010 by Carl Mahler who joined in 2004 = 6 years after joining (official leadership page: Mahler leads algo, joined 2004 after MIT); Schwager Market Wizards published 1989 = 13 years after Gelber's 1976 graduation")

print("ALL PASS")
