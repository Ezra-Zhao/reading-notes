#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 21 (acceptance).
Illustrative parameters only; not empirical data."""

# 1. In any situation the source gives exactly three options:
# change it, accept it, or leave it. Wishing without acting is
# not a fourth option in the list.
options = ["change", "accept", "leave"]
assert len(options) == 3 and "wish-and-stay-stuck" not in options

# 2. One big desire keeps full attention; splitting across two
# halves the attention each receives.
total = 100
assert total / 1 == 100 and total / 2 == 50 and total / 2 < total / 1

# 3. Photo-inbox example: picking 5 favorites out of 100 photos
# uses 5 percent of the pile as the positive selection.
assert 5 / 100 == 0.05

# 4. Timescale contrast used for the death hack: an 80-year life
# against the source's 20-billion-year universe span (10 billion
# past + 10 billion future) is 4e-9 of the span.
ratio = 80 / 20_000_000_000
assert abs(ratio - 4e-9) < 1e-12 and ratio < 1e-8

# 5. Positive-reframe practice effect (illustrative seconds):
# from a couple of seconds (~2s) to near-instant (~0.2s) is 10x.
assert 2.0 / 0.2 == 10.0

# 6. Acceptance timing: adapting only starts after acceptance,
# so accepting at day 1 leaves more adaptive days in a fixed
# 30-day window than accepting at day 20 (29 vs 10 days).
window = 30
assert window - 1 > window - 20 and (window - 1) - (window - 20) == 19

print("21-acceptance-verify: all assertions passed")
print(f"  options=3; photo pick 5%; life/universe ratio = {ratio:.1e}")
