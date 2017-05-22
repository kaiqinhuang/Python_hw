"""
polyturtle.py

Name: Kaiqin Huang
Date: 1/19/2017

A module of a subclass of Turtle, PolyTurtle.
"""


import turtle

class PolyTurtle(turtle.Turtle):

    def __init__(self, num_sides):
        # Calls all the properties that a normal turtle has
        turtle.Turtle.__init__(self)
        # Adds one more property for how many sides the polygon has
        self.sides = num_sides

    def polygon(self, side_length):
        # Draws the polygon using the given number of sides and side length
        for _ in range(self.sides):
            self.forward(side_length)
            self.right(360/self.sides)

