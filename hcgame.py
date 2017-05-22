"""
hcgame.py

Name: Kaiqin Huang
Date: 1/23/2017

A module of class HotColdGame.
"""


import random
import math

class HotColdGame:

    def __init__(self):
        # Initialize state
        self._xTrue = random.randint(0, 20)
        self._yTrue = random.randint(0, 20)
        self._mysteryCoord = (self._xTrue, self._yTrue)
        self._distPrev = math.sqrt(self._xTrue ** 2 + self._yTrue ** 2)
        self._dist = 0
        self._guessesLeft = 10
        self._guessesMade = set()    # empty set
        self._hasWon = False

    # views
    def getGuessesLeft(self):
        # Users usually do not need to know the properties so use function .getGuessesLeft()
        # instead of calling property ._guessesLeft
        return self._guessesLeft

    def hasWon(self):
        return (self._mysteryCoord in self._guessesMade and self._guessesLeft > 0)

    # actions
    def makeGuess(self, xGuess, yGuess):
        
        self._dist = math.sqrt((xGuess - self._xTrue) ** 2 + (yGuess - self._yTrue) ** 2)
        
        if self._dist == 0:
            print("You win!")
        elif self._dist < self._distPrev:
            print("Hotter!")
        elif self._dist > self._distPrev:
            print("Colder!")
        else:
            print("No distance change.  Try again.")

        g = (xGuess, yGuess)
        if g in self._guessesMade:
            print("You guessed coordinate (%d, %d) twice." % (xGuess, yGuess))

        self._guessesLeft -= 1
        self._guessesMade.add(g)
        self._distPrev = self._dist

