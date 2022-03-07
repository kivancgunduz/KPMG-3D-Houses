from geopy.geocoders import Nominatim
import pyproj
import requests
from pyproj import Proj, transform

class LocateFinder:
    
    def __init__(self,address):
        self.address: str = address
        self.latitude: float = 0.00
        self.longitude: float = 0.00


    def address_to_coordinates(self) -> bool:
        try:
            geolocator = Nominatim(user_agent='my_req')
            location = geolocator.geocode(self.address)
            # Convert Lambert 72
            proj = pyproj.Transformer.from_crs(4326, 31370 , always_xy=True)
            x2, y2 = proj.transform(location.longitude, location.latitude)
            self.latitude = x2
            self.longitude = y2
            return True
        except:
            return False
        else:
            pass
            
    
    def address_to_lambert72(self):
        req = requests.get(f"http://loc.geopunt.be/geolocation/location?q={self.address}&c=1")
        x_lambert = req.json()["LocationResult"][0]["Location"]["X_Lambert72"]
        y_lambert = req.json()["LocationResult"][0]["Location"]["Y_Lambert72"]
        return (x_lambert,y_lambert)
    

lf = LocateFinder('Cataloniëstraat, 9000 Gent')
lf.address_to_coordinates()
print(f'x={lf.latitude} y={lf.longitude}')
lambert72 = lf.address_to_lambert72()
print(f'x_lambert={lambert72[0]} - y_lambert={lambert72[1]}')

    



    

    