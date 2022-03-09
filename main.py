from utils.house_generator import Generate3DHouse
from utils.locate_finder import LocateFinder


if __name__ == '__main__':
    input_address = input("Please enter your address in Flanders/Brussels:")
    lf = LocateFinder(input_address)
    lf.address_to_coordinates()
    gh = Generate3DHouse(lf.longitude,lf.latitude, size=40, geo_path="C:/Code/Geo Files/DSM_files/DHMVIIDSMRAS1m_k22")
    gh.generate3Dhouse()
    gh.plot3D()