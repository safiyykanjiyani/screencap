"""Provides seeding for random generation and allows generation of a value within a range"""
import random
from datetime import date

class Movie:
    """This is a movie class to store values of movies, such as title, year, country ,and genre"""
    def __init__(self, title, year, country, genre, runtime, director):
        self.title = title
        self.director = director
        self.year = year
        self.country = country
        self.runtime = runtime
        self.genre = genre
        


today = date.today()
today = today.strftime("%m%d%y")

random.seed(int(today))
movie_number = random.randrange(1, 1001)

movie_list = open("data/movies.csv", encoding="utf-8")
movie_info = movie_list.readlines()[movie_number]
movie_list.close()

today_movie = Movie(movie_info[1], movie_info[2], movie_info[3], movie_info[4], movie_info[5], movie_info[6])