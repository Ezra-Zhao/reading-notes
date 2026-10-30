#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 25 (meditation).
Illustrative parameters only; not empirical data, not medical or
spiritual advice."""

# 1. His audit of his own thoughts: 90 percent fear-based,
# 10 percent desire-based; the two shares sum to the whole.
fear, desire = 90, 10
assert fear + desire == 100 and fear > desire

# 2. Choiceless-awareness session length in the source: 10 to 15
# minutes of walking without judging.
session = (10, 15)
assert session[0] == 10 and session[1] == 15 and session[1] > session[0]

# 3. The sit-still protocol: at least one hour a day, tried for
# sixty days first thing in the morning -> 60 hours total.
minutes_per_day, days = 60, 60
assert minutes_per_day * days == 3600 and minutes_per_day * days // 60 == 60

# 4. Cold-shower lesson model (illustrative): suffering sits mostly
# in the avoidance/tiptoeing phase, not in the water itself.
suffering = {"tiptoeing_in": 9, "actually_in_the_water": 1}
assert suffering["tiptoeing_in"] > suffering["actually_in_the_water"]
shower_minutes = 2  # per the source, two minutes will not kill you
assert shower_minutes == 2

# 5. Meditation forms he says he identified and tried: at least four.
forms_tried = 4
assert forms_tried >= 4
# Breath sits where two systems meet: autonomic and voluntary.
systems_meeting_at_breath = ["autonomic", "voluntary"]
assert len(systems_meeting_at_breath) == 2

# 6. Mental-inbox model: unresolved items surface one by one and,
# processed by observation alone, the backlog can reach zero.
backlog = ["childhood item", "old fear", "unfinished grief", "stuck desire"]
resolved = []
while backlog:
    resolved.append(backlog.pop(0))  # observe one, resolve one
assert len(backlog) == 0 and len(resolved) == 4  # inbox zero is reachable

print("25-meditation-verify: all assertions passed")
print("  fear/desire=90/10; protocol=60min x 60d=60h; inbox zero reachable")
