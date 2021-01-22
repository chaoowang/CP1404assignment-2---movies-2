"""MovieCollection class"""

from movie import Movie
from operator import attrgetter


class MovieCollection:
    """represent a MovieCollection"""

    def __init__(self):
        """initialise a MovieCollection"""
        self.movies = []
        self.number_of_unwatched_movie = 0
        self.number_of_watched_movie = 0
        self.number_of_movie = 0

    def __str__(self):
        """return a string representative of a MovieCollection"""
        movies = ""
        if not self.movies:
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
        number_of_unwatched_movie = 0
        for movie in self.movies:
            if not movie.is_watched:
                number_of_unwatched_movie += 1
        self.number_of_unwatched_movie = number_of_unwatched_movie
        return self.number_of_unwatched_movie

    def get_number_of_watched_movie(self):
        """get the number of watched movie"""
        number_of_watched_movie = 0
        for movie in self.movies:
            if movie.is_watched:
                number_of_watched_movie += 1
        self.number_of_watched_movie = number_of_watched_movie
        return self.number_of_watched_movie

    def get_number_of_movie(self):
        number_of_watched_movie = self.get_number_of_watched_movie()
        number_of_unwatched_movie = self.get_number_of_unwatched_movie()
        number_of_movie = number_of_watched_movie + number_of_unwatched_movie
        self.number_of_movie = number_of_movie
        return self.number_of_movie

    def load_movies(self, movie_file):
        """load the movie file"""
        input_file = open(movie_file, "r")
        lines = input_file.readlines()
        for line in lines:
            movie = line.split(",")
            self.movies.append(Movie(movie[0], movie[1], movie[2], movie[3]))
        input_file.close()
        return self.movies

    def save_movies(self, movie_file):
        """save movie collection to the file"""
        output_file = open(movie_file, "w")
        movies = ""
        for movie in self.movies:
            movies += "{}\n".format(movie)
        print(movies, file=output_file)
        output_file.close()

    def sort(self, key):
        """sort the movies by key than by title"""
        self.movies.sort(key=attrgetter(key, "title"))
        return self.movies

    def watch_movie(self, number_of_movie):
        """mark a movie as watched"""
        for i, movie in enumerate(self.movies):
            if i == number_of_movie:
                movie.watch()
        return self.movies

    def unwatch_movie(self, number_of_movie):
        """mark a movie as unwatched"""
        for i, movie in enumerate(self.movies):
            if i == number_of_movie:
                movie.unwatch()
        return self.movies
