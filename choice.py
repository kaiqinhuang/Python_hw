"""
    choice.py
    
    Name: Kaiqin Huang
    Date: 1/9/17
    
    Make a list of items that you might want to buy and get a random item to buy.
    
    Inputs: items might need to buy
    Effects: make a list of the items entered and get one of them randomly
    Outputs: the item should buy
    """

import random

item = input("Enter something you might want to buy: ")
options = []

while item != "":
    options.append(item)
    print("If you are done with shopping please enter nothing.")
    item = input("Enter something you might want to buy: ")

purchase = random.choice(options)

print("Out of all those options, you should probably buy %s." % purchase)
