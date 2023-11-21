ranked = [100, 90, 90, 80]
player = [70, 80, 105]

def climbingLeaderboard(ranked, player):
    scores = sorted(set(ranked), reverse=True)
    player_ranks = []
    for score in player:
        scores.append(score)
        scores = sorted(set(scores), reverse=True)
        player_ranks.append(scores.index(score) + 1)

    return player_ranks


# faster solution
def climbingLeaderboard(ranked, player):
    unique_leaderboard = sorted(set(ranked), reverse=True)
    player_ranks = []

    # Start from the end of the leaderboard.
    current_rank_index = len(unique_leaderboard)

    for score in player:
        # Move up the leaderboard until the current score is less than or equal to the leaderboard score.
        while current_rank_index > 0 and score >= unique_leaderboard[current_rank_index - 1]:
            current_rank_index -= 1
        # The rank is the index + 1 because rank is 1-based and index is 0-based.
        player_ranks.append(current_rank_index + 1)

    return player_ranks
