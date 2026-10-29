#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 15 (love to read).
Illustrative parameters only; not empirical data."""

# 1. One hour of science/math/philosophy a day for seven years
hours = 1 * 365 * 7
assert hours == 2555

# 2. One to two hours a day vs one minute a day is a 60-120x gap
assert 60 // 1 == 60 and 120 // 1 == 120

# 3. Foundation chain: each layer retained at 95% leaves ~86% after 3
chain = 0.95 ** 3
assert 0.85 < chain < 0.87, chain
# a zero in the foundation zeroes everything built on it
assert 0.95 * 0.0 * 0.95 == 0.0

# 4. Lindy-style filter (illustrative): a book with a 1% annual chance
# of being forgotten survives 2000 years with tiny probability, so the
# few survivors are heavily filtered; a 0.1% annual loss rate does far better.
p_harsh = 0.99 ** 2000
p_gentle = 0.999 ** 2000
assert p_harsh < 1e-8 and p_gentle > 0.10 and p_gentle > p_harsh * 1e6

# 5. Finished-book vanity metric: skimming 20 books and finishing the
# 3 with predictive power can beat forcing 1 stuck book for months.
concepts_forced = 1 * 0.2       # one gist, poorly absorbed (illustrative)
concepts_skim_then_deep = 3 * 0.9
assert concepts_skim_then_deep > concepts_forced * 10 * 0.2

# 6. Teaching check: explaining halves the half-life of forgetting in
# this illustrative decay model; after 30 days more remains.
import math
plain = math.exp(-30 / 10)
taught = math.exp(-30 / 20)
assert taught > plain * 2

print("15-reading-verify: all assertions passed")
print(f"  7y x 1h/day = {hours}h; foundation chain 0.95^3 = {chain:.3f}")
