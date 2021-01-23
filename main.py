"""
Name: Chao-Hsuan Wang
Date: 20.01.2021
Brief Project Description: A Python project with GUI and Console programs that use classes to manage a list of Movies
to Watch.

GitHub URL: https://github.com/JCUS-CP1404/assignment-2---movies-2-chaoowang
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection

FILE = 'movies.csv'
KIVY_FILE = 'app.kv'


class MoviesToWatchApp(App):
    """Main programme"""

    def __init__(self, **kwargs):
        """initialise the app"""
        super().__init__(**kwargs)
        self.movies = MovieCollection()
        self.movies.load_movies(FILE)

    def build(self):
        """build kivy app from the kivy file"""
        self.title = "Movie to watch 2.0 By Chao-Hsuan Wang"
        self.root = Builder.load_file(KIVY_FILE)
        self.list_movie()
        return self.root

    def list_movie(self):
        """display the movie collection"""
        for i, movie in enumerate(self.movies.movies):
            # create dynamic movie button
            movie_button = Button()
            if movie.is_watched:
                # indicate watch status with two different color
                is_watched = "watched"
                movie_button.background_color = (0.5, 0.5, 0.5, 1)
            else:
                is_watched = ""
                movie_button.background_color = (1, 0.5, 0.5, 1)
            # format the text on button
            movie_button.text = "{} ({} from {}){}".format(str(movie.title), str(movie.category), str(movie.year),
                                                           is_watched)
            movie_button.id = i
            movie_button.bind(on_press=self.watch_or_unwatch)
            self.root.ids.movie_list.add_widget(movie_button)
        # display how many movies unwatched/to watched
        number_of_unwatched_movie = self.movies.get_number_of_unwatched_movie()
        number_of_watched_movie = self.movies.get_number_of_watched_movie()
        self.root.ids.watch_status.text = "To watch: {}. Watched: {}".format(number_of_unwatched_movie,
                                                                             number_of_watched_movie)
        # display how many movies loaded
        number_of_movie = self.movies.get_number_of_movie()
        self.root.ids.app_status.text = "{} movies loaded.".format(number_of_movie)

    def watch_or_unwatch(self, instance):
        """mark a movie as watch or unwatch by pressing the movie button"""
        movie_number = instance.id
        for i, movie in enumerate(self.movies.movies):
            if i == movie_number:
                if movie.is_watched:
                    # unwatched a movie and update the movie list and the app status
                    movie.unwatch()
                    self.root.ids.movie_list.clear_widgets()
                    self.list_movie()
                    self.root.ids.app_status.text = "You have unwatched {}".format(str(movie.title))
                else:
                    # watched a movie and update the movie list and the app status
                    movie.watch()
                    self.root.ids.movie_list.clear_widgets()
                    self.list_movie()
                    self.root.ids.app_status.text = "You have watched {}".format(str(movie.title))

    def add_movie(self, title, year, category):
        """add new movie to movie collection"""
        try:
            # check if input year is number
            if title.strip() == "" or category.strip() == "" or year.strip() == "":
                # check if any field is not completed
                self.root.ids.app_status.text = "All fields must be completed"
            else:
                year = int(year)
                if year < 0:
                    # check if input year is valid year
                    self.root.ids.app_status.text = "Please enter a valid number"
                else:
                    # add the new movie if all fields are completed and year is valid
                    self.movies.add_movie(Movie(title, year, category))
                    self.root.ids.movie_list.clear_widgets()
                    self.list_movie()
                    self.clear()
                    self.root.ids.app_status.text = "{} ({} from {}) added to movie list".format(title, category, year)
        except ValueError:
            self.root.ids.app_status.text = "Please enter a valid number"

    def clear(self):
        """clear the input fields"""
        self.root.ids.title.text = ""
        self.root.ids.year.text = ""
        self.root.ids.category.text = ""
        self.root.ids.app_status.text = "Clear all fields"

    def sort(self, key):
        """sort the movies by key"""
        self.movies.sort(key)
        self.root.ids.movie_list.clear_widgets()
        self.list_movie()
        self.root.ids.app_status.text = "Sort by {}".format(key)

    def on_stop(self):
        """save movie collection to file when stop the app"""
        self.movies.save_movies(FILE)


if __name__ == '__main__':
    MoviesToWatchApp().run()
