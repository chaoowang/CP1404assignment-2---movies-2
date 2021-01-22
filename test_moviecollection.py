"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    print("Test sorting - year:")
    movie_collection.sort("year")
    print(movie_collection)
    # Add more sorting tests
    print("Test sorting - category:")
    movie_collection.sort("category")
    print(movie_collection)

    # Test saving movies (check CSV file manually to see results)
    movie_collection.save_movies("movies.csv")
    # More tests, as appropriate, for each method
    movie_collection.watch_movie(1)
    movie_collection.watch_movie(4)
    print(movie_collection)
    unwatched_movie = movie_collection.get_number_of_unwatched_movie()
    watched_movie = movie_collection.get_number_of_watched_movie()
    print("{} movies watched, {} movies unwatched".format(watched_movie, unwatched_movie))
    total_number_of_movie = movie_collection.get_number_of_movie()
    print("Total {} movies.".format(total_number_of_movie))


run_tests()
