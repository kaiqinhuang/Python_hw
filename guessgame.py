"""
guessgame.py

Name: Kaiqin Huang
Date: 1/23/2017

A module of class GuessGame.
"""


import random

class GuessGame:

    def __init__(self):
        # Initialize state
        self._mysteryNumber = random.randint(1, 100)
        self._guessesLeft = 7
        self._guessesMade = set()    # empty set
        self._hasWon = False
    
    def __len__(self):
        return 10
    
    def __repr__(self):
        return("I am a game with %d guesses left" % self._guessesLeft)

    # views
    def getGuessesLeft(self):
        return self._guessesLeft

    def hasWon(self):
        return (self._mysteryNumber in self._guessesMade and self._guessesLeft > 0)

    # actions
    def makeGuess(self, g):
        
        if g < self._mysteryNumber:
            print("Too low.")
        elif g > self._mysteryNumber:
            print("Too high.")
        else:
            print("You guessed it.")

        if g in self._guessesMade:
            print("Why you did this.  You guessed %d twice." % g)

        self._guessesLeft -= 1
        self._guessesMade.add(g)


