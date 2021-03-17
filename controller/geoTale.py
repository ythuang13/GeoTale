from geopy.geocoders import Nominatim
from model.story import Story


class GeoTale:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="GeoTale")
        self.cache = dict()

    def add_story(self, username, title, file_path) -> None:
        """
        Add a story of type Story into database with information from user,
        username, title and file path
        :param username: Username that upload to the database
        :param title: Title of the story
        :param file_path: A file path to the audio file
        :return: None
        """
        story = Story(username, title, file_path)

        # todo check validity before insert in database, maybe check validity in Story class
        # insert in database
        # upload file to server

    def query_story(self, location) -> list[Story]:
        """
        Query story based on location and return a list of stories
        :param location: location of user input
        :return: A list of stories
        """
        location = self.geolocator.geocode(location)
        print(location.latitude, location.longitude)
        # query stories from database
        # return a list of queried stories

    def download_story(self):
        # download story from database with story id
        pass

    def play_story(self):
        # play story in audio library
        pass


if __name__ == "__main__":
    # test for GeoTale
    gt = GeoTale()
    gt.query_story("92780")
