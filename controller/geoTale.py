from geopy.geocoders import Nominatim
from model.story import Story


class GeoTale:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="GeoTale")
        self.cache = dict()

    def add_story(self, story: Story) -> None:
        """
        Add story from user into database
        :param story: Object of type Story that have necessary information
        :return: None
        """
        pass

    def query_story(self, location) -> list[Story]:
        """
        Query story based on location and return a list of stories
        :param location: location of user input
        :return: A list of stories
        """
        location = self.geolocator.geocode(location)
        print(location.latitude, location.longitude)


if __name__ == "__main__":
    # test for GeoTale
    gt = GeoTale()
    gt.query_story("92780")
