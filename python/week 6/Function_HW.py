high_score_board = []
def get_score(item):
    return item[1]

def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    player: player name
    *scores: any number of scores
    bonus: extra points
    multiplier: multiply final score
    """

    global high_score_board

    if len(scores) == 0:
        return player, 0, 0, "no rounds played"

    for score in scores:
        if score < 0:
            return player, 0, 0, "negative score not allowed"

    total = int((sum(scores) + bonus) * multiplier)
    rounds = len(scores)

    high_score_board.append((player, total))

    sorted_board = sorted(high_score_board,
                          key=get_score,
                          reverse=True)

    rank = sorted_board.index((player, total)) + 1

    if rank == 1:
        status = "high score!"
    else:
        status = "rank " + str(rank)

    return player, rounds, total, status
print(record_game("Sara", 10, 20, 30))
print(record_game("Ali", 40, 50))
print(record_game("Nora", 25, 25, bonus=10))

print("\nLeaderboard:")
print(high_score_board)