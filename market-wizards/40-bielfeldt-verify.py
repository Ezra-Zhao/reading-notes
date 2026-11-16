#!/usr/bin/env python3
"""Verify arithmetic for note 40 (Gary Bielfeldt). Inputs from public
sources cited in the note: Schwager, Market Wizards (1989), chapter
"Gary Bielfeldt: Yes, They Do Trade T-Bonds in Peoria" (narrative:
started with USD 1,000, built it to USD 10,000 by 1965, bought 20
soybean contracts in an all-or-nothing play where a 10-cent decline
would have wiped out the account, exited with more than double his
equity; soybean speculative limit 600 contracts vs the later T-bond
limit of 10,000 contracts; T-bond futures 1 point = USD 1,000 per
contract; bottom-picking in the 63-66 area in 1983-84, bonds fell
into the 50s; turned really bullish in May 1984 when five-year notes
auctioned at a 13.93% yield while local banks could not find
qualified borrowers for three-year loans at 13%; traded heavily long
from then through April 1986, his best trade and longest trend;
banking involvement since 1974; foundation set up in 1985, planned
since the early 1970s; fundamentals give about 80% of the pieces,
self-built trend system used mainly as an exit backup);
Bielfeldt v. Commissioner, 231 F.3d 1035 (7th Cir. 2000, Posner,
C.J.) (some USD 85 million in refunds at stake; capital losses
offset ordinary income only up to USD 3,000 a year; he bought huge
quantities from primary dealers and resold in smaller batches a few
weeks later on an auction-glut theory; he took part in as few as 6%
and never more than 15% of auctions, out of the market as much as
200 days a year; NY Fed called his activity outright speculation on
interest-rate movements; judgment affirmed); DOJ Solicitor General
brief in opposition, No. 00-1545 (refund claims USD 3,202,380 for
1984, 19,781,480 for 1985, 39,160,798 for 1986, 16,232,812 for 1987,
6,658,075 for 1988; trading through Bielfeldt & Co. 1985-1989;
7th Cir. judgment entered 2000-11-08, rehearing denied 2001-01-08,
cert petition filed 2001-04-06)."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. The shoestring start
assert close(10_000 / 1_000, 10.0, 0.001) and close((10_000 / 1_000 - 1) * 100, 900.0, 0.01)
print("1 start OK USD 1,000 grew to USD 10,000 by 1965: exactly 10.00x, a +900% build -- painstaking, in Schwager's word, and still only seed money")

# 2. The 1965 all-or-nothing soybean trade
per_contract = 10_000 / 20
assert close(per_contract, 500.0, 0.001) and 20 * per_contract == 10_000
print("2 soybean OK Schwager: a 10-cent decline would have wiped out the USD 10,000 account across 20 contracts, i.e. USD 500 of loss per contract per 10 cents; he exited with more than double his equity, so the single trade returned over +100% and left him with over USD 20,000")

# 3. Why he had to leave soybeans: the position-limit ceiling
assert close(10_000 / 600, 16.67, 0.01) and 10_000 - 600 == 9_400
print("3 limits OK the T-bond market's eventual 10,000-contract limit was 16.67x the 600-contract soybean limit (a 9,400-contract difference) -- the market he left capped him, the market he entered did not, at first")

# 4. The refund claims add up to the Seventh Circuit's own round number
claims = [3_202_380, 19_781_480, 39_160_798, 16_232_812, 6_658_075]
total = sum(claims)
assert total == 85_035_545 and close((total / 85_000_000 - 1) * 100, 0.04, 0.01)
print(f"4 refunds OK the five yearly refund claims in the Solicitor General's brief sum to USD {total:,}, within 0.04% of the 'some $85 million' the Seventh Circuit prints -- the brief's parts and the opinion's total are the same account")

# 5. The claims are concentrated in two years
assert close(claims[2] / total * 100, 46.05, 0.01) and close((claims[1] + claims[2]) / total * 100, 69.31, 0.01)
print(f"5 concentration OK 1986 alone is USD 39,160,798 = {claims[2]/total*100:.2f}% of all claims; 1985 plus 1986 are {(claims[1]+claims[2])/total*100:.2f}% -- the fight was mostly about two years of losses, not five equal years")

# 6. What losing the case meant at USD 3,000 a year
assert close(total / 3_000, 28345.18, 0.01)
print(f"6 limit OK as capital losses, the amount behind the claims could offset ordinary income at only USD 3,000 a year (26 U.S.C. 1211(b) as quoted by the court): USD 85,035,545 / 3,000 = {total/3000:,.2f} years of allowance -- that ratio, not pride, is why a trader/dealer label was worth litigating to the Supreme Court door")

# 7. How part-time the alleged 'dealer' was, in the court's own numbers
assert close(200 / 365 * 100, 54.79, 0.01) and 365 - 200 == 165 and 15 - 6 == 9
print("7 presence OK the opinion: he joined as few as 6% and never more than 15% of auctions (a 9-point range) and was out of the market as much as 200 days a year = 54.79% of the year, leaving at most 165 days in -- a market maker who is absent most of the year is the contradiction the court seized on")

# 8. The best trade: its length and its yield signal
months = (1986 - 1984) * 12 + (4 - 5)
assert months == 23 and close(13.93 - 13.00, 0.93, 0.001)
print("8 best-trade OK heavily long from May 1984 through April 1986 is 23 months; the trigger he cites is arithmetic a banker could check: five-year Treasury notes auctioned at 13.93% while his bank could not find qualified borrowers for three-year loans at 13% -- a 0.93-point gap, 'nearly a full percentage point' in his words")

# 9. The slow prerequisites behind the fast-looking trade
assert 1984 - 1974 == 10 and 1985 - 1970 >= 12 and 1985 - 1973 <= 15
print("9 patience OK he had been involved in banking since 1974, ten years before the May-1984 call; the foundation he set up in 1985 had been planned since the early 1970s, a 12-to-15-year lag between intention and act -- the same patience profile as the trading")

# 10. The litigation tail
d_decide = (date(2000, 11, 8) - date(2000, 9, 27)).days
d_rehear = (date(2001, 1, 8) - date(2000, 11, 8)).days
d_cert = (date(2001, 4, 6) - date(2001, 1, 8)).days
assert d_decide == 42 and d_rehear == 61 and d_cert == 88
print(f"10 tail OK argued 2000-09-27, decided 42 days later on 2000-11-08 (affirmed); rehearing denied 61 days after judgment; cert petition filed 88 days after that, on 2001-04-06 -- the 1985-1989 partnership trading years produced a tax tail still running in 2001")

print("ALL PASS")
