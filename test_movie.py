"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    # tests show this initialise works
    print(initial_movie)
    assert initial_movie.title == "Thor: Ragnarok"
    assert initial_movie.year == 2017
    assert initial_movie.category == "Comedy"
    assert initial_movie.is_watched

    # more tests, as appropriate, for each method
    movie_test = Movie("Star Wars: Episode IV - A New Hope", 1997, "action", "u")
    print(movie_test)
    movie_test.unwatch()
    print(movie_test)
    movie_test.watch()
    print(movie_test)


run_tests()
