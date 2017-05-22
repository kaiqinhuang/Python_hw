"""
play_guessgame.py

Name: Kaiqin Huang
Date: 1/23/2017

A script to play the guess game.
"""


import guessgame

print("Hello!")
game = guess.GuessGame()

while game.getGuessesLeft() > 0 and not(game.hasWon()):
    inp = int(input("Guess a number? "))
    game.makeGuess(inp)

if game.hasWon():
    print("You won!")
else:
    print("You're a winner in your own way.  But not at this game.")

