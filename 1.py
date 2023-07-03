import random

def calculate_total_score(player_answers, levels_played):
    total_score = 0
    for level, answers in enumerate(player_answers[:levels_played], start=1):
        level_score = sum(answers)  # Summing up the scores for the current level
        total_score += level_score
    return total_score

# Generate random player answers
num_players = 25000
num_levels = 5
player_answers = [[random.randint(0, 1) for _ in range(num_levels)] for _ in range(num_players)]

# Generate random number of levels played for each player (between 1 and num_levels)
levels_played = [random.randint(1, num_levels) for _ in range(num_players)]

# Calculate total scores for each player based on levels played
player_scores = [calculate_total_score(answers, levels) for answers, levels in zip(player_answers, levels_played)]

# Print total scores for each player
for player_num, score in enumerate(player_scores, start=1):
    print(f"Player {player_num}: Total Score = {score}")
