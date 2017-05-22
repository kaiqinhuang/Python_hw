"""
movies_object_inclass.py

Name: Kaiqin Huang
Date: 1/18/2017

A module of object Movie.
"""


class Movie:

def __init__(self, new_title, new_year, new_genre):  # __init__: constructor
        self.title = new_title
        self.year = new_year
        self.genre = new_genre
        print("Movie made!")

    def display(self):
        return ("%s (%d), a %s" % (self.title,self.year,self.genre))

    def time_travel(self):
        self.year -= 10

    def shout(self):
        self.title = self.title.upper()

