"""
    polygon.py
    
    Name: Kaiqin Huang
    Date: 1/10/17
    
    Draw equilateral polygons.
    
    Inputs: an integer no smaller than 3
    Effects: launch a turtle screen and spawn a turtle, and draw the polygon
    Outputs: polygon
    """

# %gui tk
import turtle

number = int(input("Please enter an integer not smaller than 3: "))

scrn = turtle.Screen()
scrn.title("Look at Bob!")
bob = turtle.Turtle()
bob.shape("turtle")
for _ in range(number):
    bob.forward(50)
    bob.right(360/number)

scrn.exitonclick()
