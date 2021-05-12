from model.network import Network
from controller.settings import *
import os
import soundfile as sf


class GeoTale:
    def __init__(self):
        self.cache = dict()
        self.network = Network(HOST, PORT)

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

        if zip_code == "" or int(zip_code) < 00000 or int(zip_code) > 99999:
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
        elif not os.path.exists(file_path):
            raise ValueError("File path doesn't exist")

        # length of wav file
        f = sf.SoundFile(file_path)
        length = int(len(f) / f.samplerate)

        # upload then insert data into database, and verify
        status_code = self.network.send_file(file_path)

        if status_code == "200":
            self.network.send(("I", (zip_code, title, author,
                                     description, length)))

        return status_code

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

    def download_story(self, story_id: int) -> None:
        # query to see if story_id is valid
        result = self.network.send(("QD", story_id))
        # download story from database with story id
        if result:
            self.network.request_file(story_id)
        else:
            raise ValueError("No such story with this story id")
