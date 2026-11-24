#!/usr/bin/env python3
"""131 Chen Heng (Huashang New Normal Mixed 001457) verification.
Source: Huashang Xin Changtai Flexible Allocation Mixed Fund 2026 Q3 report
(cninfo PDF, period end 2026-09-30, sent 2026-10-27), read page by page:
contract effective 2015-06-29 (S2); A-class windows S3.2.1; manager Chen Heng
appointed 2025-01-06, no departure, 18.2 years experience (S4.1); profits S3.1;
holdings S5; shares S6; manager own holding 9,446,878.24 shares = 9.18% (S7).
All derived values use Decimal division of printed factors (evidence C)."""
from decimal import Decimal as D
from datetime import date
ok = 0
def chk(c, l):
    global ok
    assert c, l
    ok += 1; print("PASS", l)
def r2(x): return x.quantize(D('0.01'))
# G1 life / tenure
life = (date(2026,9,30)-date(2015,6,29)).days
ten = (date(2026,9,30)-date(2025,1,6)).days
chk(life == 4111, "fund life 4111 days")
chk(r2(D(life)/D('365.25')) == D('11.26'), "life approx 11.26 years")
chk(ten == 632, "Chen tenure 632 days")
chk(r2(D(ten)/D(life)*100) == D('15.37'), "tenure 15.37% of fund life")
chk(life-ten == 3479, "pre-Chen period 3479 days not his")
# G2 windows A vs benchmark (printed)
rows = [("3M",D('-12.81'),D('-8.10')),("6M",D('-12.81'),D('-0.68')),("1Y",D('-18.59'),D('-2.97')),
        ("3Y",D('-1.30'),D('17.23')),("5Y",D('-35.45'),D('1.21')),("7Y",D('71.23'),D('22.99')),
        ("10Y",D('33.88'),D('42.47')),("SI",D('66.15'),D('22.92'))]
exc = {n: f-b for n,f,b in rows}
chk(exc == {"3M":D('-4.71'),"6M":D('-12.13'),"1Y":D('-15.62'),"3Y":D('-18.53'),
            "5Y":D('-36.66'),"7Y":D('48.24'),"10Y":D('-8.59'),"SI":D('43.23')}, "excess table")
# G3 win/loss
chk(sum(1 for v in exc.values() if v>0)==2, "only 2 of 8 windows positive excess (7Y, SI)")
chk(sum(1 for v in exc.values() if v<0)==6, "6 of 8 windows negative excess")
chk(exc["5Y"]==D('-36.66'), "worst excess 5Y -36.66pp")
# G4 Q2 2026 implied: 6M factor / 3M factor
chk(r2(((1+D('-12.81')/100)/(1+D('-12.81')/100)-1)*100)==D('0.00'), "Q2 fund implied 0.00%")
chk(r2(((1+D('-0.68')/100)/(1+D('-8.10')/100)-1)*100)==D('8.07'), "Q2 benchmark implied +8.07%")
# G5 prior 9 months of 1Y window
chk(r2(((1+D('-18.59')/100)/(1+D('-12.81')/100)-1)*100)==D('-6.63'), "prior 9M fund -6.63%")
chk(r2(((1+D('-2.97')/100)/(1+D('-8.10')/100)-1)*100)==D('5.58'), "prior 9M benchmark +5.58%")
# G6 segment 7Y-5Y
chk(r2(((1+D('71.23')/100)/(1+D('-35.45')/100)-1)*100)==D('165.27'), "seg 7-5 fund +165.27%")
chk(r2(((1+D('22.99')/100)/(1+D('1.21')/100)-1)*100)==D('21.52'), "seg 7-5 bench +21.52%")
# G7 segment 5Y-3Y
chk(r2(((1+D('-35.45')/100)/(1+D('-1.30')/100)-1)*100)==D('-34.60'), "seg 5-3 fund -34.60%")
chk(r2(((1+D('1.21')/100)/(1+D('17.23')/100)-1)*100)==D('-13.67'), "seg 5-3 bench -13.67%")
# G8 segment 3Y-1Y and 10Y-7Y
chk(r2(((1+D('-1.30')/100)/(1+D('-18.59')/100)-1)*100)==D('21.24'), "seg 3-1 fund +21.24%")
chk(r2(((1+D('17.23')/100)/(1+D('-2.97')/100)-1)*100)==D('20.82'), "seg 3-1 bench +20.82%")
chk(r2(((1+D('33.88')/100)/(1+D('71.23')/100)-1)*100)==D('-21.81'), "seg 10-7 fund -21.81%")
chk(r2(((1+D('42.47')/100)/(1+D('22.99')/100)-1)*100)==D('15.84'), "seg 10-7 bench +15.84%")
# G9 profit composition A+C
ra,rc = D('-3727329.87'), D('-16074.58'); pa,pc = D('-11492698.88'), D('-46039.86')
chk(ra+rc == D('-3743404.45'), "realized total -3,743,404.45")
chk(pa+pc == D('-11538738.74'), "profit total -11,538,738.74")
chk((pa-ra)+(pc-rc) == D('-7795334.29'), "unrealized total -7,795,334.29")
chk(r2(abs((pa-ra)+(pc-rc))/abs(pa+pc)*100)==D('67.56'), "unrealized 67.56% of loss")
# G10 shares / manager holding / loss vs net assets
net = D('78100214.45')+D('380045.83')
chk(net == D('78480260.28'), "net assets 78,480,260.28")
chk(r2(abs(pa+pc)/net*100)==D('14.70'), "Q3 loss 14.70% of ending net assets")
a0,a1 = D('104221437.70'), D('102446228.65'); c0,c1 = D('462575.10'), D('508538.82')
chk(r2((a1/a0-1)*100)==D('-1.70'), "A shares -1.70%")
chk(r2((c1/c0-1)*100)==D('9.94'), "C shares +9.94%")
chk(r2(((a1+c1)/(a0+c0)-1)*100)==D('-1.65'), "total shares -1.65%")
chk(r2(D('9446878.24')/D('102954767.47')*100)==D('9.18'), "manager own holding 9.18% matches printed")
# G11 holdings shape
tops = [D('5.40'),D('4.51'),D('4.16'),D('4.09'),D('4.07'),D('4.04'),D('4.03'),D('3.66'),D('3.56'),D('3.54')]
chk(sum(tops)==D('41.06'), "top-10 total 41.06%")
chk(r2(D('71534041.43')/net*100)==D('91.15'), "equity 91.15% of net assets (printed industry total)")
chk(r2(D('69957207.43')/D('71534041.43')*100)==D('97.80'), "manufacturing 97.80% of equity")
# G12 recovery math + NAV registration
chk(r2((1/(1+D('-12.81')/100)-1)*100)==D('14.69'), "Q3 -12.81% needs +14.69% to recover")
chk(r2((1/(1+D('-35.45')/100)-1)*100)==D('54.92'), "5Y -35.45% needs +54.92% to recover")
chk(D('1.744')-D('0.762')==D('0.982'), "cum NAV 1.744 minus unit NAV 0.762 = 0.982 (distributions, registered only)")
print("TOTAL PASS", ok)
