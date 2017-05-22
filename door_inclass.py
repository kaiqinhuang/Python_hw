"""
door.py

Name: Kaiqin Huang
Date: 1/18/2017

A module of class Door.
"""


class Door:

    def __init__(self):
        self.closed = True

    def open(self):
        self.closed = False

    def close(self):
        self.closed = True

    def knock(self):
        if self.closed:
            print("Knock knock!")
        else:
            print("Can't knock an open door.")

