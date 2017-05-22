"""
    random_walk.py
    
    Name: Kaiqin Huang
    Date: 1/10/17
    
    Walk 250 random steps, and draw the rectangle of the area.
    
    Inputs:
    Effects:
    Outputs: 250 random steps, and the rectangle
    """

# %gui tk
import turtle
import random

scrn = turtle.Screen()
scrn.title("Look at Bob!")
bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(9)
x_history = []
y_history = []

for _ in range(250):
    angle = random.randrange(0,359)
    bob.right(angle)
    bob.forward(10)
    x = bob.xcor()
    y = bob.ycor()
    x_history.append(x)
    y_history.append(y)

x_min = min(x_history)
x_max = max(x_history)
y_min = min(y_history)
y_max = max(y_history)

bob.penup()
bob.setposition(x_min,y_min)
bob.pendown()
bob.setposition(x_min,y_max)
bob.setposition(x_max,y_max)
bob.setposition(x_max,y_min)
bob.setposition(x_min,y_min)

scrn.exitonclick()
