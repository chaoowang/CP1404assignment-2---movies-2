"""Movie class"""


class Movie:
    """represent a Movie object"""

    def __init__(self, title="", year=0, category="", is_watched="u"):
        """initialise a Movie"""
        self.title = title
        self.year = int(year)
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """return a string representative of a Movie"""
        return "{}, {}, {}, {}".format(self.title, self.year, self.category, self.is_watched)

    def watch(self):
        """mark movie as watched"""
        self.is_watched = "w"
        return self.is_watched

    def unwatch(self):
        """mark movie as unwatch"""
        self.is_watched = "u"
        return self.is_watched
