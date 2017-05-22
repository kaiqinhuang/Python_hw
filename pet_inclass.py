"""
pet.py

Name: Kaiqin Huang
Date: 1/18/2017

A module of class Pet.
"""


class Pet:

    def __init__(self, new_name, new_age):
        print("I'm alive!")
        self.name = new_name
        self.age = new_age
        self.location = "couch"
        print("Also my name is %s." % self.name)

    def locate(self):
        print("I am at the %s." % self.location)
        
    def report(self):
        print("I am %s, and %d years old." % (self.name, self.age))

