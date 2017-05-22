"""
megaturtle.py

Name: Kaiqin Huang
Date: 1/21/2017

A module of class MegaTurtle.
"""


import turtle
import random


class MegaTurtle(turtle.Turtle):


    def __init__(self):
        # Calls all the properties that a normal turtle has
        turtle.Turtle.__init__(self)
        
        # Implements one more property to count the steps
        self._steps = 0
 
    def randomwalk(self, n):
        """ Causes the turtle to move n steps of distance 10 in random directions.  
            Basically exactly like in the *random_walk.py* script from lab 5
        """
        
        for _ in range(n):
            angle = random.randrange(0,359)
            self.right(angle)
            self.forward(10)

    def forwarddashed(self, n):
        """ Just like forward(n), except draws a dashed line instead of a solid line.  
            Each "dash" should be distance 10, and each "gap" should be distance 5.
            
            Should do nothing if the pen is up.
        """

        self._steps += n

        while n > 0:
            if n <= 10:
                self.forward(n)
                n -= 10
            else:
                self.forward(10)
                self.penup()
                n -= 10
                if n <= 5:
                    self.forward(n)
                    n -= 5
                else:
                    self.forward(5)
                    self.pendown()
                    n -= 5

    def dashdistance(self):
        """ Returns the total distance that the turtle has ever used "forwarddashed()" to move with.

            For example, with a new turtle bob:
        """

        # return self.distance(0,0)
        return self._steps

