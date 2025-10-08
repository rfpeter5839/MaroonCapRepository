import warnings
warnings.filterwarnings("error")
#Total games must be a positive odd number fitting (2n+1)"
def main(p, q, total_games):
    try:
        from BinomialProbsCalc import combined_binomial_probability
        from BinomialProbsCalc import binomial_probability
        from NumberSets import sets_needed_to_win
        #solves for the number of sets needed to win a best of n series
        if (p==1) and (q==0):
            return 1
        if (p==0) and (q==1):
            return 0
        if (p==0):
            return "impossible"
        if (p==1) and (q==1):
            return 0.5
        sets_to_win = sets_needed_to_win(total_games)
        #odds of A winning a best of 7 game if they have a p chance of winning each serve and q of each return serve assuming they serve first.
        probAServeAWin = (combined_binomial_probability(4, p, 3, q, 6))+(combined_binomial_probability(5, p, 4, q, 6))
        #odds of B winning a best of 7 game if they have a p chance of winning each serve and q of each return serve assuming they serve first.
        probBServeAWin = (combined_binomial_probability(4, q, 3, p, 6)+combined_binomial_probability(5, q, 4, p, 6))
        probAServeSet = (binomial_probability(total_games, sets_to_win, probAServeAWin))/(binomial_probability(total_games, sets_to_win, probAServeAWin)+(binomial_probability(total_games, sets_to_win, probBServeAWin)))
        return probAServeSet
    except RuntimeWarning as e:
        # Code to handle runtime warning if a high value of games is used or if a invalid value is encounter in scalar divide.
        # In short, more games than it can make a reasonable estimate for. This depends on the values p and q.
        print("The odds of this happening is near impossible",{e})
    except Exception as e:
        # Generic error handling for other exceptions
        print(f"An unexpected error occurred: {e}")
"""
Impossible example
print(main(0.9, 0.75, 2501))
"""

print(main(0.5, 0.25, 9))
print(main(0.5, 0.5, 9))
print(main(0.75, 0.25, 9))
print(main(1, 0.5, 9))
print(main(0, 0.75, 9))
print(main(1, 0, 9))
print(main(0, 1, 9))
print(main(0, 0, 9))
print(main(1, 1, 9))
print(main(1, 0.75, 9))
print(main(0.75, 1, 9))


