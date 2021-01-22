"""
assignment 1 - movies
Name: Chao-Hsuan Wang
"""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class

from movie import Movie
from operator import itemgetter

MENU = "Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"


def main():
    print("Movies To Watch 1.0 - by Chao-Hsuan Wang")

    read_movie_file = open("movies.csv", "r")  # open movie to read
    movie_index, movie_list, number_of_line = load_file(read_movie_file)  # load file
    read_movie_file.close()
    print("{} movies loaded".format(number_of_line))

    movie_to_watch, num_movie_watched = count_movies_watch(movie_list)  # count how many movies watched/unwatched

    print(MENU)
    menu_choice = input("").lower()

    while menu_choice != "q":
        while menu_choice not in ["l", "a", "w", "q"]:  # error checking for menu choice
            print("Invalid menu choice")
            print(MENU)
            menu_choice = input("").lower()
        if menu_choice == "l":  # list movies
            list_movie(movie_list, movie_to_watch, num_movie_watched)
            print(MENU)
            menu_choice = input("").lower()

        elif menu_choice == "a":  # add new movie including: title, year, category
            add_movie(movie_index, movie_list)
            resort_movies(movie_list)
            print(MENU)
            menu_choice = input("").lower()

        elif menu_choice == "w":  # watch a movie
            watch_a_movie(movie_list, movie_to_watch)
            print(MENU)
            menu_choice = input("").lower()
        elif menu_choice == "q":
            pass
        movie_to_watch, num_movie_watched = count_movies_watch(movie_list)

    output_movie_file = open("movies.csv", "w")
    save_to_file(output_movie_file, movie_list)
    output_movie_file.close()

    print("{} movies saved to movies.csv".format(len(movie_list)))
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


def watch_a_movie(movie_list, movie_to_watch):
    if movie_to_watch == 0:
        print("No more movies to watch!")
    else:
        print("Enter the number of movie to mark as watched")
        movie_watched = input()
        watched_check = False
        while watched_check == False:  # error checking for movie number watched
            try:
                movie_watched = int(movie_watched)
                if movie_watched >= len(movie_list):
                    print("Invalid movie number")
                    movie_watched = input()
                elif movie_watched < 0:
                    print("Number must be >= 0")
                    movie_watched = input()
                else:
                    watched_check = True
            except ValueError:
                print("Invalid input; enter a valid number")
                movie_watched = input()

        for movie in movie_list:  # watch a movie
            if int(movie_watched) == movie[0]:
                if movie[4] == " ":
                    print("You have already watched {}".format(movie[1]))
                else:
                    print("{} from {} watched".format(movie[1], movie[2]))
                    movie[4] = " "


def resort_movies(movie_list):
    for movie in movie_list:  # reorder movies after new movie added
        movie.pop(0)  # remove old movie number
    movie_list.sort(key=itemgetter(1, 2))  # resort movies
    new_index = 0
    for movie in movie_list:  # add new new movie number
        movie.insert(0, new_index)
        new_index += 1


def add_movie(movie_index, movie_list):
    movie_title = input("Title:")
    while movie_title.strip() == "":  # error checking for title
        print("Input can not be blank")
        movie_title = input("Title:")
    movie_year = input("Year:")
    year_check = False
    while year_check == False:  # error checking for year
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
    movie_list.append(
        [movie_index, movie_title, movie_year, movie_category, "*"])  # add new movie to movie list
    print("{} ({} from {}) added to movie list".format(movie_title, movie_category, movie_year))
    movie_index += 1


def list_movie(movie_list, movie_to_watch, num_movie_watched):
    for line in movie_list:
        print(" {}. {} {:<35} - {:>4} ({})".format(line[0], line[4], line[1], line[2], line[3]))
    print("{} movies watched, {} movies still to watch".format(num_movie_watched, movie_to_watch))


def count_movies_watch(movie_list):
    movie_to_watch = 0
    num_movie_watched = 0
    for line in movie_list:
        if line[4] == "*":  # count how many movies watched and how many to watch
            movie_to_watch += 1
        else:
            num_movie_watched += 1
    return movie_to_watch, num_movie_watched


def load_file(movie_file):
    movie_list = []
    number_of_line = 0
    movie_index = 0
    lines = movie_file.readlines()  # read all lines in movie file
    for line in lines:
        movie = line.split(",")
        movie[1] = int(movie[1])  # convert year into int
        if movie[3] == "u\n" or movie[3] == "u":
            movie[3] = "*"  # "*"=unwatch; " "=watched
        else:
            movie[3] = " "
        movie_list.append(movie)
        number_of_line += 1  # count how many movies loaded
    movie_list.sort(key=itemgetter(1, 2)) #sort movie by year then by title
    for movie in movie_list:  # add movie number
        movie.insert(0, movie_index)
        movie_index += 1
    return movie_index, movie_list, number_of_line


if __name__ == '__main__':
    main()
