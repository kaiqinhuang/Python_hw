"""
    coin.py
    
    Name: Kaiqin Huang
    Date: 1/5/17
    
    A coin flip game to guess Head or Tail.
    
    Inputs: guess
    Effects: flip the coin and compare the result with the guess
    Outputs: guess is right or wrong
    """

guess = input("Hello, please type in either \"H\" for Head or \"T\" for Tail: ")

while guess != "H" and guess != "T":
    guess = input("Please retry and type in either \"H\" for Head or \"T\" for Tail: ")

if guess == "H":
    print("Your guess is Head.")
else:
    print("Your guess is Tail.")

import random
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
