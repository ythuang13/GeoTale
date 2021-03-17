from geopy.geocoders import Nominatim


class GeoTale:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="GeoTale")

    def add_story(self):
        pass

    def hear_story(self, location):
        location = self.geolocator.geocode(location)
        print(location.latitude, location.longitude)


if __name__ == "__main__":
    # test for GeoTale
    gt = GeoTale()
    gt.hear_story("92780")
