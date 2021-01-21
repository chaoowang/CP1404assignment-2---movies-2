"""Movie class"""


class Movie:
    """represent a Movie object"""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """initialise a Movie"""
        self.title = title
        self.year = int(year)
        self.category = category
        if is_watched==False or is_watched==True:
            pass
        elif is_watched=="w":
            is_watched=True
        else:
            is_watched=False
        self.is_watched = is_watched

    def __str__(self):
        """return a string representative of a Movie"""
        return "{}, {}, {}, {}".format(self.title, self.year, self.category, self.is_watched)

    def watch(self):
        """mark movie as watched"""
        self.is_watched = True
        return self.is_watched

    def unwatch(self):
        """mark movie as unwatch"""
        self.is_watched = False
        return self.is_watched
