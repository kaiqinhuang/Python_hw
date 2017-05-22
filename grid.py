"""
grid.py

Name: Kaiqin Huang
Date: 1/13/2017

A module of function draw_grid().
"""


import turtle

def draw_grid(row, column):
    """Draws an n x m grid of squares
        
    Arguments:
        row (int): Number of rows
        column (int): Number of columns
        
    Returns:
        Draw an n x m grid of squares
    """
    
    scrn = turtle.Screen()
    scrn.title("Look at Bob!")
    bob = turtle.Turtle()
    bob.shape("turtle")
    
    for i in range(row + 1):
        bob.forward(30 * column)
        bob.penup()
        bob.setposition(0, -30 * (i + 1))
        bob.pendown()
    
    bob.penup()
    bob.home()
    bob.right(90)
    bob.pendown()

    for i in range(column + 1):
        bob.forward(30 * row)
        bob.penup()
        bob.setposition(30 * (i + 1), 0)
        bob.pendown()

    scrn.exitonclick()
