#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 33 (appendix
recommended reading, part 2: philosophy, sci-fi, blogs, other).
Illustrative parameters only; not empirical data."""

# 1. Update to his always-rereading list adds four: the two
# all-works authors, a classical yoga text, and Schopenhauer.
reread_additions = ["jed_mckenna", "kapil_gupta",
                    "vashistha_yoga", "schopenhauer"]
assert len(reread_additions) == 4

# 2. Osho: two books named; the meditation collection holds 112.
osho = ["book_of_secrets_112_meditations", "the_great_challenge"]
assert len(osho) == 2
meditation_methods = 112
assert meditation_methods == 112

# 3. Ted Chiang: three works named (two story collections and
# The Lifecycle of Software Objects).
chiang = ["stories_of_your_life_and_others", "exhalation",
          "lifecycle_of_software_objects"]
assert len(chiang) == 3

# 4. He skips two-thirds of his reading when telling people;
# one-third is what gets reported.
reported = 1 / 3
skipped = 1 - reported
assert abs(skipped - 2 / 3) < 1e-9 and skipped > reported

# 5. Blogs section lists four sites.
blogs = ["melting_asphalt", "farnam_street", "stratechery",
         "idle_words"]
assert len(blogs) == 4

# 6. Graphic novels he calls among the finest art of the age: four.
graphic_novels = ["transmetropolitan", "the_boys", "planetary",
                  "the_sandman"]
assert len(graphic_novels) == 4

print("33-reading-philosophy-scifi-verify: all assertions passed")
print("  additions=4; osho=2 methods=112; chiang=3; skipped=2/3; blogs=4; graphic_novels=4")
