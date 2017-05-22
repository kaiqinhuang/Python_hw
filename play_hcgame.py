"""
play_hcgame.py

Name: Kaiqin Huang
Date: 1/23/2017

A script to play the HotColdGame.
"""


import hcgame

print("Hello!")
hcgame = hcgame.HotColdGame()

while hcgame.getGuessesLeft() > 0 and not(hcgame.hasWon()):
    inputX = int(input("Guess a value for x? "))
    inputY = int(input("Guess a value for y? "))
    hcgame.makeGuess(inputX, inputY)

if hcgame.hasWon():
    print("You won!")
else:
    print("You're a winner in your own way.  But not at this game.")

