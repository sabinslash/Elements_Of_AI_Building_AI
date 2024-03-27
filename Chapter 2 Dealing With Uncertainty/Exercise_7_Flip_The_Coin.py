import numpy as np

def generate(p1):
    # Generates 10000 random zeros and ones where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    # Returns the number of occurrences of 11111 in the sequence
    return sum((seq[i:i+5] == 1).all() for i in range(len(seq) - 4))

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
