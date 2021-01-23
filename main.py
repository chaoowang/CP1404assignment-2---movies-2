"""
Name: Chao-Hsuan Wang
Date:
Brief Project Description:
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---movies-2-chaoowang
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection


class MoviesToWatchApp(App):
    """Main programme"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movies = MovieCollection()
        self.movies.load_movies('movies.csv')

    def build(self):
        self.title = "Movie to watch 2.0 By Chao-Hsuan Wang"
        self.root = Builder.load_file('app.kv')
        self.list_movie()
        return self.root

    def list_movie(self):
        for i, movie in enumerate(self.movies.movies):
            movie_button = Button()
            if movie.is_watched:
                is_watched = "watched"
                movie_button.background_color = (0.5, 0.5, 0.5, 1)
            else:
                is_watched = ""
                movie_button.background_color = (1, 0.5, 0.5, 1)
            movie_button.text = "{} ({} from {}){}".format(str(movie.title), str(movie.category), str(movie.year),
                                                           is_watched)
            movie_button.id = i
            movie_button.bind(on_press=self.watch_or_unwatch)
            self.root.ids.movie_list.add_widget(movie_button)
        number_of_unwatched_movie = self.movies.get_number_of_unwatched_movie()
        number_of_watched_movie = self.movies.get_number_of_watched_movie()
        self.root.ids.watch_status.text = "To watch: {}. Watched: {}".format(number_of_unwatched_movie,
                                                                             number_of_watched_movie)
        number_of_movie = self.movies.get_number_of_movie()
        self.root.ids.app_status.text = "{} movies loaded.".format(number_of_movie)

    def watch_or_unwatch(self, instance):
        movie_number = instance.id
        for i, movie in enumerate(self.movies.movies):
            if i == movie_number:
                if movie.is_watched:
                    movie.unwatch()
                    self.root.ids.movie_list.clear_widgets()
                    self.list_movie()
                    self.root.ids.app_status.text = "You have unwatched {}".format(str(movie.title))
                else:
                    movie.watch()
                    self.root.ids.movie_list.clear_widgets()
                    self.list_movie()
                    self.root.ids.app_status.text = "You have watched {}".format(str(movie.title))

    def add_movie(self, title, year, category):
        try:
            if title.strip() == "" or category.strip() == "" or year.strip() == "":
                self.root.ids.app_status.text = "All fields must be completed"
            else:
                year = int(year)
                if year < 0:
                    self.root.ids.app_status.text = "Please enter a valid number"
                else:
                    self.movies.add_movie(Movie(title, year, category))
                    self.root.ids.movie_list.clear_widgets()
                    self.list_movie()
                    self.clear()
                    self.root.ids.app_status.text = "{} ({} from {}) added to movie list".format(title, category, year)
        except ValueError:
            self.root.ids.app_status.text = "Please enter a valid number"

    def clear(self):
        self.root.ids.title.text = ""
        self.root.ids.year.text = ""
        self.root.ids.category.text = ""
        self.root.ids.app_status.text="Clear all fields"

    def sort(self, key):
        self.movies.sort(key)
        self.root.ids.movie_list.clear_widgets()
        self.list_movie()
        self.root.ids.app_status.text = "Sort by {}".format(key)

if __name__ == '__main__':
    MoviesToWatchApp().run()
