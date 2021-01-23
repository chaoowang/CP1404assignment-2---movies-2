"""
assignment 1 - movies
Name: Chao-Hsuan Wang
"""

from movie import Movie
from moviecollection import MovieCollection

MENU = "Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"
FILE = 'movies.csv'


def main():
    print("Movies To Watch 2.0 - by Chao-Hsuan Wang")

    movies = MovieCollection()
    movies.load_movies(FILE)
    movies.sort("year")
    movies.get_number_of_movie()
    print("{} movies loaded".format(movies.number_of_movie))

    print(MENU)
    menu_choice = input(">>> ").lower()

    while menu_choice != "q":
        while menu_choice not in ["l", "a", "w", "q"]:  # error checking for menu choice
            print("Invalid menu choice")
            print(MENU)
            menu_choice = input(">>> ").lower()
        if menu_choice == "l":  # list movies
            list_movie(movies)
            print(MENU)
            menu_choice = input(">>> ").lower()

        elif menu_choice == "a":  # add new movie including: title, year, category
            add_movie(movies)
            print(MENU)
            menu_choice = input(">>> ").lower()

        elif menu_choice == "w":  # watch a movie
            watch_a_movie(movies)
            print(MENU)
            menu_choice = input(">>> ").lower()
        elif menu_choice == "q":
            pass

    movies.save_movies(FILE)

    print("{} movies saved to {}".format(movies.get_number_of_movie(), FILE))
    print("Have a nice day :)")


def watch_a_movie(movies):
    """mark a movie as watched"""
    if movies.get_number_of_unwatched_movie() == 0:
        print("No more movies to watch!")
    else:
        print("Enter the number of movie to mark as watched")
        movie = input(">>> ")
        has_watched = False
        while not has_watched:  # error checking for movie number watched
            try:
                # check if input number is number
                movie = int(movie)
                if movie >= movies.get_number_of_movie():
                    # check if input number is valid
                    print("Invalid movie number")
                    movie = input(">>> ")
                elif movie < 0:
                    # check if input number is positive number
                    print("Number must be >= 0")
                    movie = input(">>> ")
                else:
                    has_watched = True
            except ValueError:
                print("Invalid input; enter a valid number")
                movie = input(">>> ")
        movies.watch_movie(movie)


def add_movie(movies):
    """add a movie to movie list"""
    movie_title = input("Title: ")
    while movie_title.strip() == "":  # error checking for title
        print("Input can not be blank")
        movie_title = input("Title: ")
    movie_year = input("Year: ")
    year_check = False
    while not year_check:  # error checking for year
        try:
            # check if input year is number
            movie_year = int(movie_year)
            if movie_year < 0:
                # check if input is positive number
                print("Number must be >= 0")
                movie_year = input("Year: ")
            else:
                year_check = True
        except ValueError:
            print("Invalid input; enter a valid number")
            movie_year = input("Year: ")
    movie_category = input("Category: ")
    while movie_category.strip() == "":  # error checking for category
        print("Input can not be blank")
        movie_category = input("Category: ")
    movies.add_movie(Movie(movie_title, movie_year, movie_category, False))
    movies.sort("year")
    print("{} ({} from {}) added to movie list".format(movie_title, movie_category, movie_year))


def list_movie(movies):
    """display the movie list"""
    # count how many movies unwatched/to watched
    num_of_watched_movies = movies.get_number_of_watched_movie()
    num_of_unwatched_movies = movies.get_number_of_unwatched_movie()
    print(
        "{}{} movies watched, {} movies still to watch".format(movies, num_of_watched_movies, num_of_unwatched_movies))


if __name__ == '__main__':
    main()
