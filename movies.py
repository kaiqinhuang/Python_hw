"""
    movies.py
    
    Name: Kaiqin Huang
    Date: 1/9/17
    
    Print the titles and years of three movies in a list.
    
    Inputs: a list of three movies including their titles and years
    Effects: use a for loop to iterate over every movie and print out the title of the movie and the year it came out in parentheses after
    Outputs: titles and years
    """

my_movies = [("Titanic", 1997), ("The Princess Bride", 1987), ("Your Name", 2016)]

for i in range(3):
    print(my_movies[i][0], "("+str(my_movies[i][1])+")")
