import numpy as np
from scipy.stats import binom
from scipy.special import comb
from math import factorial

def binomial_probability(n, k, p):
    q = 1 - p
    return comb(n, k) * (p ** k) * (q ** (n - k))

def joint_binomial_probability(n1, k1, p1, n2, k2, p2):
    prob1 = binomial_probability(n1, k1, p1)
    prob2 = binomial_probability(n2, k2, p2)
    return prob1 * prob2

def combined_binomial_probability(n1, p1, n2, p2, k_total):
    prob = 0.0
    for k1 in range(max(0, k_total - n2), min(n1, k_total) + 1):
        k2 = k_total - k1
        if 0 <= k2 <= n2:
            prob += joint_binomial_probability(n1, k1, p1, n2, k2, p2)
    return prob

"""
print(combined_binomial_probability(4, 0.5, 3, 0.25, 6))
print(combined_binomial_probability(5, 0.5, 4, 0.25, 6))
print(combined_binomial_probability(3, 0.5, 3, 0.25, 0))
print(combined_binomial_probability(4, 0.5, 4, 0.25, 2))
print(combined_binomial_probability(5, 0.5, 5, 0.25, 4))
print("-----")
print(combined_binomial_probability(4, 0.5, 3, 0.25, 6)+(combined_binomial_probability(5, 0.5, 4, 0.25, 6)))
print(combined_binomial_probability(3, 0.5, 3, 0.25, 0)+(combined_binomial_probability(4, 0.5, 4, 0.25, 2))+(combined_binomial_probability(5, 0.5, 5, 0.25, 4)))
print("-----")
print(combined_binomial_probability(4, 0.25, 3, 0.5, 6))
print(combined_binomial_probability(5, 0.25, 4, 0.5, 6))
print(combined_binomial_probability(3, 0.25, 3, 0.5, 0))
print(combined_binomial_probability(4, 0.25, 4, 0.5, 2))
print(combined_binomial_probability(5, 0.25, 5, 0.5, 4))
print ("-----")
print(combined_binomial_probability(4, 0.25, 3, 0.5, 6)+combined_binomial_probability(5, 0.25, 4, 0.5, 6))
print((combined_binomial_probability(3, 0.25, 3, 0.5, 0))+(combined_binomial_probability(4, 0.25, 4, 0.5, 2))+(combined_binomial_probability(5, 0.25, 5, 0.5, 4)))
print("-----")
print(binomial_probability(9, 5, combined_binomial_probability(4, 0.5, 3, 0.25, 6)+(combined_binomial_probability(5, 0.5, 4, 0.25, 6))))
print(binomial_probability(9, 5, (combined_binomial_probability(4, 0.25, 3, 0.5, 6)+combined_binomial_probability(5, 0.25, 4, 0.5, 6))))
print("-----")
print((binomial_probability(9, 5, combined_binomial_probability(4, 0.5, 3, 0.25, 6)+(combined_binomial_probability(5, 0.5, 4, 0.25, 6))))/(binomial_probability(9, 5, combined_binomial_probability(4, 0.5, 3, 0.25, 6)+(combined_binomial_probability(5, 0.5, 4, 0.25, 6)))+(binomial_probability(9, 5, (combined_binomial_probability(4, 0.25, 3, 0.5, 6)+combined_binomial_probability(5, 0.25, 4, 0.5, 6))))))
"""