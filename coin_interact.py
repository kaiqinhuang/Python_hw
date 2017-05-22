"""
    coin_interact.py
    
    Name: Kaiqin Huang
    Date: 1/11/2017
    
    A coin flip game to guess Head or Tail.
    
    Inputs: guess
    Effects: flip the coin and compare the result with the guess
    Outputs: guess is right or wrong
"""

import random
from interact import get_option

print("What do you guess, Head (H) or Tail (T)?")
guess = get_option(["H","T"])

flip = random.randint(0,1)
if flip == 0:
    print("The coin flip result is Head.")
else:
    print("The coin flip result is Tail.")

if guess == "H" and flip == 0:
    print("Congratulations!  Your guess Head is correct!")
elif guess == "T" and flip == 1:
    print("Congratulations!  Your guess Tail is correct!")
else:
    print("Sorry, wrong guess.")
