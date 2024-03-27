import random

def main():
    # Define the words and their corresponding probabilities
    words = ['dogs', 'cats', 'bats']
    probabilities = [0.8, 0.1, 0.1]
    
    # Select a word based on the specified probabilities
    favourite = random.choices(words, weights=probabilities)[0]
    
    print("I love " + favourite) 

main()
