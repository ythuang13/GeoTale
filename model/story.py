class Story:
    def __init__(self, zip_code: str, author: str, title: str,
                 description: str):
        self._zip_code = zip_code
        self._author = author
        self._title = title
        self._description = description
        self._length = None

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @property
    def length(self):
        return self._length

    @property
    def description(self):
        return self._description

    @property
    def zip_code(self):
        return self._zip_code

    def __repr__(self):
        return f"Story({self._author}, {self._title}, {self._description})"

    def __str__(self):
        return f"Story:{self._title} by {self._author}"
