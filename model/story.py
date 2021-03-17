class Story:
    def __init__(self, username, title, file_path):
        self._username = username
        self._title = title
        self._file_path = file_path
        self._server_path = None
        self._length = None

    @property
    def username(self):
        return self._username

    @property
    def title(self):
        return self._title

    @property
    def length(self):
        return self._length

    @property
    def server_path(self):
        return self._server_path

    def __repr__(self):
        return f"Story({self._username}, {self._title}, {self._file_path})"

    def __str__(self):
        return f"Story:{self._title} by {self._username} @ {self._file_path}"
