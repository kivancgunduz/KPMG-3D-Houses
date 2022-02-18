from geopy.geocoders import Nominatim

class LocateFinder:
    
    latitude:float = 0.0
    longitude: float = 0.0
    def __init__(self,address):
        self.address: str = address


    def address_to_locate(self) -> bool:
        try:

            geolocator = Nominatim(user_agent='my_req')
            location = geolocator.geocode(self.address)
            self.latitude = location.latitude
            self.longitude = location.longitude
        except:
            return False
        else:
            return True

    

    