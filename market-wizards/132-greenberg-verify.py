#!/usr/bin/env python3
"""132 Greenberg (Baron Small Cap Fund, Institutional BSFIX) verification.
Sources (Baron official, read page by page in browser):
- Q3 2026 quarterly letter (signed Cliff Greenberg, Portfolio Manager):
  Institutional annualized performance as of 2026-09-30, inception 1997-09-30;
  QTD -7.69, YTD -4.30, 1Y -5.79, 3Y 6.75, 5Y -0.17, 10Y 9.59, 15Y 11.07,
  SI 9.46; Russell 2000 Growth and Russell 3000 same table; letter states
  first-half 2026 fund return +3.67%; expense ratios Retail 1.32 / Inst 1.06
  as of 2026-01-28.
- Baron Small Cap Strategy fact sheet 2026-09-30: "Cliff Greenberg joined
  Baron Capital in 1997 as the portfolio manager for Baron Small Cap Fund",
  42 years of research experience.
- Baron product page (characteristics as of 2026-09-30): net assets $2.36B,
  51 issuers / 98.9% of net assets, turnover (3Y avg) 11.08%, active share
  95.3%, median market cap $5.20B vs index $1.38B, weighted avg $14.32B vs
  $4.41B; Retail (BSCFX) performance table on same page; holdings and top-10
  total 36.6% are as of 2026-10-31 (registered with that date); Q3 top
  contributors as of 2026-09-30: Neogen 0.67, Intapp 0.57, Baldwin 0.48,
  Gartner 0.47, Everforth 0.45.
All derived values use Decimal arithmetic on printed values (evidence C)."""
from decimal import Decimal as D
from datetime import date
ok = 0
def chk(c, l):
    global ok
    assert c, l
    ok += 1; print("PASS", l)
def r2(x): return x.quantize(D('0.01'))
# G1 life / tenure (manager joined in inception year 1997 as this fund's PM)
life = (date(2026,9,30)-date(1997,9,30)).days
chk(life == 10592, "fund life 10592 days")
chk(r2(D(life)/D('365.25')) == D('29.00'), "life approx 29.00 years")
chk(life == 29*365 + 7, "29 years incl 7 leap days (2000..2024)")
# G2 excess vs Russell 2000 Growth (annualized windows, pp)
F = {"1Y":D('-5.79'),"3Y":D('6.75'),"5Y":D('-0.17'),"10Y":D('9.59'),"15Y":D('11.07'),"SI":D('9.46')}
G = {"1Y":D('12.05'),"3Y":D('17.55'),"5Y":D('4.72'),"10Y":D('9.90'),"15Y":D('11.94'),"SI":D('6.86')}
exc = {k: F[k]-G[k] for k in F}
chk(exc == {"1Y":D('-17.84'),"3Y":D('-10.80'),"5Y":D('-4.89'),"10Y":D('-0.31'),"15Y":D('-0.87'),"SI":D('2.60')}, "excess vs R2000G table")
chk(sum(1 for v in exc.values() if v>0)==1, "only 1 of 6 annualized windows positive vs R2000G (SI)")
chk(exc["10Y"]==D('-0.31'), "closest window 10Y only -0.31/yr")
# G3 excess vs Russell 3000
R = {"1Y":D('15.13'),"3Y":D('22.26'),"5Y":D('12.64'),"10Y":D('14.73'),"15Y":D('15.27'),"SI":D('9.35')}
exc3 = {k: F[k]-R[k] for k in F}
chk(exc3 == {"1Y":D('-20.92'),"3Y":D('-15.51'),"5Y":D('-12.81'),"10Y":D('-5.14'),"15Y":D('-4.20'),"SI":D('0.11')}, "excess vs R3000 table")
chk(sum(1 for v in exc3.values() if v>0)==1, "only SI positive vs R3000 too (+0.11)")
# G4 non-annualized windows
chk(D('-7.69')-D('-9.39')==D('1.70'), "QTD excess vs R2000G +1.70pp")
chk(D('-7.69')-D('1.40')==D('-9.09'), "QTD excess vs R3000 -9.09pp")
chk(D('-4.30')-D('10.71')==D('-15.01'), "YTD excess vs R2000G -15.01pp")
# G5 H1 x Q3 = YTD consistency (letter H1 +3.67%)
chk(r2(((1+D('3.67')/100)*(1+D('-7.69')/100)-1)*100)==D('-4.30'), "H1 +3.67 x Q3 -7.69 = YTD -4.30")
# G6 cumulative endpoints $10k, SI 29 years
def cum(rate, yrs): return (1+rate/100)**yrs
chk(r2(cum(D('9.46'),29)*10000)==D('137533.30'), "SI fund $10k approx 137,533.30")
chk(r2(cum(D('6.86'),29)*10000)==D('68492.01'), "SI R2000G $10k approx 68,492.01")
chk(r2(cum(D('9.35'),29)*10000)==D('133581.04'), "SI R3000 $10k approx 133,581.04")
chk(r2(cum(D('9.46'),29)/cum(D('9.35'),29))==D('1.03'), "SI fund only 1.03x R3000 endpoint")
chk(r2(cum(D('9.46'),29)/cum(D('6.86'),29))==D('2.01'), "SI fund 2.01x R2000G endpoint")
# G7 cumulative windows
chk(r2((cum(F['10Y'],10)-1)*100)==D('149.87'), "10Y cumulative fund +149.87%")
chk(r2((cum(G['10Y'],10)-1)*100)==D('157.03'), "10Y cumulative R2000G +157.03%")
chk(r2((cum(F['5Y'],5)-1)*100)==D('-0.85'), "5Y cumulative fund -0.85%")
chk(r2((cum(F['3Y'],3)-1)*100)==D('21.65'), "3Y cumulative fund +21.65%")
chk(r2((cum(G['3Y'],3)-1)*100)==D('62.43'), "3Y cumulative R2000G +62.43%")
# G8 segments (annualized -> segment total return)
seg_29_10_f = cum(F['SI'],29)/cum(F['10Y'],10)-1
seg_29_10_g = cum(G['SI'],29)/cum(G['10Y'],10)-1
chk(r2(seg_29_10_f*100)==D('450.43'), "seg first-19Y fund +450.43%")
chk(r2(seg_29_10_g*100)==D('166.48'), "seg first-19Y R2000G +166.48%")
seg_10_5_f = cum(F['10Y'],10)/cum(F['5Y'],5)-1
seg_10_5_g = cum(G['10Y'],10)/cum(G['5Y'],5)-1
chk(r2(seg_10_5_f*100)==D('152.00'), "seg 10-5Y fund +152.00%")
chk(r2(seg_10_5_g*100)==D('104.09'), "seg 10-5Y R2000G +104.09%")
seg_5_3_f = cum(F['5Y'],5)/cum(F['3Y'],3)-1
chk(r2(seg_5_3_f*100)==D('-18.49'), "seg 5-3Y fund -18.49%")
# G9 recovery prices
chk(r2((1/(1+D('-5.79')/100)-1)*100)==D('6.15'), "1Y -5.79 needs +6.15% to recover")
chk(r2((1/(1+D('-4.30')/100)-1)*100)==D('4.49'), "YTD -4.30 needs +4.49% to recover")
chk(r2((1/cum(F['5Y'],5)-1)*100)==D('0.85'), "5Y cumulative -0.85 needs +0.85% to recover")
# G10 share-class gap
chk(D('1.32')-D('1.06')==D('0.26'), "expense gap retail-inst 0.26pp")
chk(r2(D('9.46')-D('9.29'))==D('0.17'), "SI gap inst-retail +0.17/yr")
chk(D('-7.69')-D('-7.77')==D('0.08'), "QTD gap inst-retail +0.08pp")
# G11 portfolio shape
chk(r2(D('5.20')/D('1.38'))==D('3.77'), "median cap 3.77x index")
chk(r2(D('14.32')/D('4.41'))==D('3.25'), "weighted avg cap 3.25x index")
chk(r2(D('100')/D('11.08'))==D('9.03'), "turnover 11.08% implies approx 9.03y avg holding")
chk(D('0.67')+D('0.57')+D('0.48')+D('0.47')+D('0.45')==D('2.64'), "top5 Q3 contributors sum +2.64pp")
# G12 YTD path vs index: fund down while both indices up double digits (printed)
chk(F['5Y']<0 and G['5Y']>0, "5Y fund negative while index positive")
print(f"ALL {ok} ASSERTIONS PASS")
