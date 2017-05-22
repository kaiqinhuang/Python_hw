"""
    guess.py
    
    Name: Kaiqin Huang
    Date: 1/8/17
    
    Guess a random integer between 1 and 100.
    
    Inputs: guess an integer between 1 and 100
    Effects: compare with the random integer
    Outputs: too high, too low, or correct
    """

import random
answer = random.randint(1,100)

guess = int(input("Please pick an integer between 1 and 100: "))

while guess != answer:
    if guess > answer:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Please try again.  Pick an integer between 1 and 100: "))

print("Congratulations!  The random integer is %d." % answer)
