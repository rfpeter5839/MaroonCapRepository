def sets_needed_to_win(total_games):
    if total_games % 2 == 0 or total_games < 1:
        raise ValueError("Total games must be a positive odd number (2n+1)")
    return (total_games // 2) + 1