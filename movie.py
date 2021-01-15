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
