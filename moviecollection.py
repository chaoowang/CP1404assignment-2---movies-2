"""MovieCollection class"""

from movie import Movie
from operator import itemgetter


class MovieCollection:
    """represent a MovieCollection"""

    def __init__(self):
        """initialise a MovieCollection"""
        self.movies = []
        self.number_of_unwatched_movie = 0
        self.number_of_watched_movie = 0

    def __str__(self):
        """return a string representative of a MovieCollection"""
        movies = ""
        if self.movies == []:
            return "no movie collection yet"
        else:
            for i, movie in enumerate(self.movies):
                movies += ("{} - {}\n".format(i, movie))
            return movies

    def add_movie(self, movie=Movie):
        """add a movie to movie collection"""
        self.movies.append(movie)

    def get_number_of_unwatched_movie(self):
        """get the number of unwatched movies"""
        for movie in self.movies:
            if not movie.watch:
                self.number_of_unwatched_movie += 1
        return self.number_of_unwatched_movie

    def get_number_of_watched_movie(self):
        """get the number of watched movie"""
        for movie in self.movies:
            if movie.watch:
                self.number_of_watched_movie += 1
        return self.number_of_watched_movie

    def load_movies(self, movie_file):
        """load the movie file"""
        input_file = open(movie_file, "r")
        lines = input_file.readlines()
        for line in lines:
            movie = line.split(",")
            if movie[3] == "u":
                self.number_of_unwatched_movie += 1
            else:
                self.number_of_watched_movie += 1
            self.movies.append(Movie(movie[0], movie[1], movie[2], movie[3]))
        input_file.close()
        return self.movies, self.number_of_watched_movie, self.number_of_unwatched_movie



    def save_movies(self, movie_file):
        """save movie collection to the file"""
        output_file = open(movie_file, "w")
        movies = ""
        for movie in self.movies:
            movies += "{}\n".format(movie)
        print(movies, file=output_file)
        output_file.close()

    def sort(self):
        """sort the movies by year than by title"""
        self.movies.sort(key=itemgetter(1, 2))
        return self.movies
