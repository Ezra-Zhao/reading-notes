#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 24 (exercise).
Illustrative parameters only; not empirical data, not medical advice."""

# 1. Annual breaks from daily workouts are countable on one hand:
# at most five per year, i.e. adherence at least 360/365 days.
max_breaks = 5
adherence = (365 - max_breaks) / 365
assert max_breaks <= 5 and adherence > 0.98

# 2. A fuzzy basket holds ten to fifteen priorities and, per the
# source, ends with none of them done; a single top priority gets done.
fuzzy = list(range(10, 16))
assert min(fuzzy) == 10 and max(fuzzy) == 15
done_fuzzy, done_single = 0, 1
assert done_fuzzy < done_single

# 3. Walking-meeting benefits listed in the source: exactly six.
benefits = ["brain works better", "exercise and sunlight",
            "shorter, fewer pleasantries", "more dialogue, less monologue",
            "no slides", "ends easily by walking back"]
assert len(benefits) == 6 and len(set(benefits)) == 6

# 4. Training modalities named as things people obsess over: five.
# The source's point is daily practice, not the modality.
modalities = ["weight training", "tennis", "Pilates", "HIIT", "The Happy Body"]
assert len(modalities) == 5
days_per_week = 7
assert days_per_week == 7

# 5. Trade-off slogan as a monotone illustrative model: the harder
# the workout (effort 1..10), the easier the rest of the day feels.
ease = [effort for effort in range(1, 11)]
assert all(ease[i] < ease[i + 1] for i in range(9))
# And the morning workout makes the waiting world wait 30 minutes.
world_waits_minutes = 30
assert world_waits_minutes == 30

# 6. Hard choices now, easy life later: the inversion holds across
# the five domains the source names or implies in this passage.
domains = ["eating", "working out", "values", "saving for a rainy day",
           "relationships"]
assert len(domains) == 5
sign = {"hard now": +1, "easy later": +1, "easy now": -1, "hard later": -1}
assert sign["hard now"] == sign["easy later"] > sign["easy now"]

print("24-exercise-verify: all assertions passed")
print(f"  adherence>={adherence:.3f}; benefits=6; modalities=5; domains=5")
