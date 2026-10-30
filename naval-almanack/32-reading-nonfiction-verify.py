#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 32 (appendix
recommended reading, part 1: bonus pages and nonfiction).
Illustrative parameters only; not empirical data."""

# 1. Bonus pages: two aphorisms, one tech-optimism, one alien joke.
bonus = ["tech_democratization_optimism", "alien_civilizations_joke"]
assert len(bonus) == 2

# 2. Reading motive: curiosity and interest, explicitly not
# self-improvement; best-book test is devourability.
motive = {"primary": "curiosity_and_interest", "not": "self_improvement",
          "best_book_test": "will_devour"}
assert motive["not"] == "self_improvement"
assert motive["best_book_test"] == "will_devour"

# 3. Feynman cluster names four items: Six Easy Pieces,
# Six Not-So-Easy Pieces, his letters volume, and his biography.
feynman = ["six_easy_pieces", "six_not_so_easy_pieces",
           "letters_volume", "feynman_biography"]
assert len(feynman) == 4

# 4. Ridley: besides The Rational Optimist, four more are named;
# Rovelli: two are named.
ridley_more = ["genome", "red_queen", "origins_of_virtue",
               "evolution_of_everything"]
rovelli = ["reality_is_not_what_it_seems", "seven_brief_lessons"]
assert len(ridley_more) == 4 and len(rovelli) == 2

# 5. Taleb: two featured plus three more named as worth reading.
taleb_featured = ["skin_in_the_game", "bed_of_procrustes"]
taleb_more = ["black_swan", "antifragile", "fooled_by_randomness"]
assert len(taleb_featured) == 2 and len(taleb_more) == 3

# 6. Game theory pair: one strategy primer, one cooperation study.
game_theory = ["compleat_strategyst", "evolution_of_cooperation"]
assert len(game_theory) == 2

print("32-reading-nonfiction-verify: all assertions passed")
print("  bonus=2; motive=curiosity; feynman=4; ridley_more=4; rovelli=2; taleb=2+3; game_theory=2")
