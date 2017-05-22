"""
movies_object.py

Name: Kaiqin Huang
Date: 1/18/2017

Class Movie and a script using it.
"""


class Movie:

    def __init__(self, new_title, new_genre, new_year):  # __init__(): constructor
        '''Creates a new movie with properties title, genre, and year
            
        Args:
            new_title (str): movie name
            new_genre (str): movie genre
            new_year (int): movie year
            
        Returns:
            none
            
        '''
        
        self.title = new_title  # properties
        self.genre = new_genre
        self.year = new_year
        print("Movie made!")


    def describe(self):  # describe(): method
        '''Describes the movie title, year, and genre
            
        Args:
            none
            
        Returns:
            a string of movie description including title, year, and genre
            
        '''
        return ("%s (%d), a %s" % (self.title, self.year, self.genre))


my_movies = [Movie("Titanic", "Romantic Disaster", 1997),
             Movie("The Princess Bride", "Fantasy Adventure", 1987),
             Movie("Your Name", "Touching Anime", 2016)
            ]


for m in my_movies:
    print(m.describe())

