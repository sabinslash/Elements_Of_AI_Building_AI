import random
import math

def accept_prob(S_old, S_new, T):
    # Calculate the acceptance probability for simulated annealing
    if S_new > S_old:
        return 1.0
    else:
        return math.exp((S_new - S_old) / T)

# Test the accept function using accept_prob
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

# Example usage
S_old = 10
S_new = 12
T = 1.0
accept(S_old, S_new, T)
