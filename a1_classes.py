"""
assignment 1 - movies
Name: Chao-Hsuan Wang
"""

from movie import Movie
from moviecollection import MovieCollection

MENU = "Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"


def main():
    print("Movies To Watch 2.0 - by Chao-Hsuan Wang")

    movies = MovieCollection()
    movies.load_movies('movies.csv')
    movies.sort("year")
    movies.get_number_of_movie()
    print("{} movies loaded".format(movies.number_of_movie))

    print(MENU)
    menu_choice = input("").lower()

    while menu_choice != "q":
        while menu_choice not in ["l", "a", "w", "q"]:  # error checking for menu choice
            print("Invalid menu choice")
            print(MENU)
            menu_choice = input("").lower()
        if menu_choice == "l":  # list movies
            list_movie(movies)
            print(MENU)
            menu_choice = input("").lower()

        elif menu_choice == "a":  # add new movie including: title, year, category
            add_movie(movies)
            print(MENU)
            menu_choice = input("").lower()

        elif menu_choice == "w":  # watch a movie
            watch_a_movie(movies)
            print(MENU)
            menu_choice = input("").lower()
        elif menu_choice == "q":
            pass

    movies.save_movies("movies.csv")

    print("{} movies saved to movies.csv".format(
        movies.get_number_of_watched_movie() + movies.get_number_of_unwatched_movie()))
    print("Have a nice day :)")


def save_to_file(output_movie_file, movie_list):
    for movie in movie_list:
        movie.pop(0)
        if movie[3] == "*":  # "*"=unwatch; " "=watched
            movie[3] = "u"
        else:
            movie[3] = "w"
        movie_info = movie[0] + "," + str(movie[1]) + "," + movie[2] + "," + movie[3]
        print(movie_info, file=output_movie_file)


def watch_a_movie(movies):
    if movies.get_number_of_unwatched_movie() == 0:
        print("No more movies to watch!")
    else:
        print("Enter the number of movie to mark as watched")
        movie = input()
        has_watched = False
        while not has_watched:  # error checking for movie number watched
            try:
                movie = int(movie)
                if movie >= movies.get_number_of_movie():
                    print("Invalid movie number")
                    movie = input()
                elif movie < 0:
                    print("Number must be >= 0")
                    movie = input()
                else:
                    has_watched = True
            except ValueError:
                print("Invalid input; enter a valid number")
                movie = input()
        movies.watch_movie(movie)


def add_movie(movies):
    movie_title = input("Title:")
    while movie_title.strip() == "":  # error checking for title
        print("Input can not be blank")
        movie_title = input("Title:")
    movie_year = input("Year:")
    year_check = False
    while not year_check:  # error checking for year
        try:
            movie_year = int(movie_year)
            if movie_year < 0:
                print("Number must be >= 0")
                movie_year = input("Year:")
            else:
                year_check = True
        except ValueError:
            print("Invalid input; enter a valid number")
            movie_year = input("Year:")
    movie_category = input("Category:")
    while movie_category.strip() == "":  # error checking for category
        print("Input can not be blank")
        movie_category = input("Category:")
    movies.add_movie(Movie(movie_title, movie_year, movie_category, False))
    movies.sort("year")
    print("{} ({} from {}) added to movie list".format(movie_title, movie_category, movie_year))


def list_movie(movies):
    print(movies)
    num_of_watched_movies = movies.get_number_of_watched_movie()
    num_of_unwatched_movies = movies.get_number_of_unwatched_movie()
    print("{} movies watched, {} movies still to watch".format(num_of_watched_movies, num_of_unwatched_movies))


if __name__ == '__main__':
    main()
