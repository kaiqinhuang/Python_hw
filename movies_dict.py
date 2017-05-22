"""
    movies_dict.py
    
    Name: Kaiqin Huang
    Date: 1/12/17
    
    Print the title, year, and a brief introduction of three movies in a list of dictionaries.
    
    Inputs: a list of dictionaries of three movies including their titles, years, and brief introductions
    Effects: use a for loop to iterate over every movie and print out the related information
    Outputs: titles, years, and brief introductions
"""

my_movies = [{ 'title': "Titanic",
               'year': 1997,
               'genre': "Romance Disaster"
             },
             { 'title': "The Princess Bride",
               'year': 1987,
               'genre': "Fantasy Adventure"
             },
             { 'title': "Your Name",
               'year': 2016,
               'genre': "Touching Anime"
             }
            ]

for movie in my_movies:
    print("%s (%d), a %s." % (movie['title'], movie['year'], movie['genre']))
