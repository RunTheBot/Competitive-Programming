# Mock CCC '24 Contest 1 J2 - Simple Elo Rating System
# DMOJ: https://dmoj.ca/problem/mccc6j2

def calculate_expected_score(rating_diff):
    return 1 / (1 + 10 ** (rating_diff / 400))

def update_ratings(rating_a, rating_b, outcome, k_factor):
    expected_score_a = calculate_expected_score(rating_b - rating_a)
    actual_score_a = 1 if outcome == 'W' else 0.5 if outcome == 'T' else 0
    delta = k_factor * (actual_score_a - expected_score_a)
    return rating_a + delta, rating_b - delta

# Input
initial_games, initial_rating_a, initial_rating_b, k_factor = map(int, input().split())
outcomes = input()

# Initial ratings
current_rating_a, current_rating_b = initial_rating_a, initial_rating_b

# Update ratings based on outcomes
for outcome in outcomes:
    current_rating_a, current_rating_b = update_ratings(current_rating_a, current_rating_b, outcome, k_factor)
    # Output
    print(f"{current_rating_a:.1f} {current_rating_b:.1f}")

