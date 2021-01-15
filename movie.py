"""Movie class"""


class Movie:
    """represent a Movie object"""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """initialise a Movie"""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """return a string representative of a Movie"""
        return "{}, {}, {}, {}".format(self.title, self.year, self.category, self.is_watched)

    def watch(self):
        self.is_watched = True
        return self.is_watched

    def unwatch(self):
        self.is_watched = False
        return self.is_watched
