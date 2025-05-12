import random

# Probability that done() will return True (25% chance)
DONE_LIKELIHOOD = 0.25

def chaotic_counting():
    """
    Counts from 1 to 10, but may stop early if done() returns True.
    At each number, checks if we should stop before printing.
    """
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Exit function early if done() returns True
        print(curr_num, end=' ')  # Print numbers with spaces between them

def done():
    """Returns True with a probability of DONE_LIKELIHOOD (25% chance by default)"""
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done")

if __name__ == "__main__":
    main()