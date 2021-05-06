from model.network import Network
from controller.settings import *
from tkinter import filedialog
import tkinter as tk


class GeoTale:
    def __init__(self):
        self.cache = dict()
        self.network = Network(HOST, PORT)
        if self.network.id is None:
            # todo handle no connection and let GuiState change to a state
            #  of warning
            pass

    def quit(self):
        self.network.quit()

    def add_story(self, zip_code: str, title: str, author: str, file_path: str,
                  description: str = "") -> None or ValueError:
        """
        Validate and add a story into database with information from user,
        Zip_code, title, author, file_path and optional description
        :param zip_code: Zip code of the story (len == 5)
        :param title: Title of the story (len < 45)
        :param author: Name of author of the story (len < 45)
        :param file_path: File path to the audio file
        :param description: Optional description of the story (len < 128)
        :return: None
        """
        # data validation
        # todo validate data
        if int(zip_code) < 00000 or int(zip_code) > 99999:
            raise ValueError("Invalid Zip Code")
        elif len(zip_code) != 5:
            raise ValueError("Invalid zip code")
        elif len(title) == 0:
            raise ValueError("Required title")
        elif len(title) >= 45:
            raise ValueError("Title too long")
        elif len(author) == 0:
            raise ValueError("Required author")
        elif len(author) >= 45:
            raise ValueError("Author name too long")
        elif len(description) >= 128:
            raise ValueError("description too long")
        # todo get length
        length = 0
        # todo check path validity

        # upload then insert data into database
        self.network.send_file(file_path)
        self.network.send(("I", (zip_code, title, author, description,
                                 length)))

    def query_story(self, zip_code) -> list:
        """
        Query story based on location and return a list of stories
        :param zip_code: zip code of user input
        :return: A list of stories
        """
        # query stories from database
        result = self.network.send(("Q", zip_code))

        # return a list of queried stories
        return result

    def download_story(self, song_id: int) -> None:
        # download story from database with story id
        download_path = ""
        self.network.request_file(song_id)
