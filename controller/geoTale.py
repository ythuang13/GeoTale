from geopy.geocoders import Nominatim
from model.story import Story
import mysql.connector


class GeoTale:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="GeoTale")
        self.cache = dict()
        self.db = mysql.connector.connect(host="localhost", port="3306",
                                          user="root", password="root",
                                          database="geotale")
        self.my_cursor = self.db.cursor(dictionary=True)

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
        length = 0
        # validate data
        # todo invalid zip code (can only be number)
        if int(zip_code) < 00000 or int(zip_code) > 99999:
            raise ValueError("Invalid Zip Code")
        if len(title) >= 45:
            raise ValueError("Title too long")
        if len(author) >= 45:
            raise ValueError("Author name too long")
        # todo check path validity
        if len(description) >= 128:
            raise ValueError("description too long")

        # insert in database
        self.my_cursor.execute(
            "INSERT INTO story (zip_code, title, author, length, description)"
            " VALUES (%s, %s, %s, %s, %s)",
            (zip_code, title, author, length, description))
        self.db.commit()

        # upload file to server

    def query_story(self, zipcode) -> list[Story]:
        """
        Query story based on location and return a list of stories
        :param zipcode: zipcode of user input
        :return: A list of stories
        """
        # location = self.geolocator.geocode(location)
        # print(location.latitude, location.longitude)

        # query stories from database
        self.my_cursor.execute("SELECT * FROM story WHERE zip_code = %s",
                               (zipcode, ))
        result = self.my_cursor.fetchall()
        for x in result:
            print(x)

        # return a list of queried stories
        return result

    def download_story(self):
        # download story from database with story id
        pass

    def play_story(self):
        # play story in audio library
        pass


if __name__ == "__main__":
    # test for GeoTale
    gt = GeoTale()
    gt.add_story("92780", "Yeet", "Dan", "None", "LilSkeet")
    gt.query_story("92780")
