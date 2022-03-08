import os
from pyproj import Proj, Transformer
import rasterio
import rasterio.plot
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import geopandas as gpd




class Generate3DHouse():
    """
    """
    def __init__(self,longitude:float, latitude:float, size:int = 25, geo_path:str = '') -> None:

        self.longitude: float = longitude
        self.latitude: float = latitude
        self.size: int = size
        self.top: float = longitude + size
        self.bottom: float = longitude - size
        self.left: float = latitude - size
        self.right: float = latitude + size
        self.main_dsm_directory: str = '../data/DSM'
        self.main_dtm_directory: str = '../data/DTM'
        self.correct_tiff_path: str = None
        self.x_max: int = None
        self.x_min: int = None
        self.y_max: int = None
        self.y_min: int = None



    def check_geofile_path(self) -> bool:
        """
        """
        for gtif in os.listdir(self.main_dsm_directory):
            path = os.path.join(self.main_dsm_directory,'/GeoTiff',gtif)
            dsm = rasterio.open(path)
            if ((dsm.bounds.left < self.coord[0] < dsm.bounds.right) and (dsm.bounds.bottom < self.coord[1]< dsm.bounds.top)):
                self.correct_tiff_path = path
                return True
            else:
                return False
        

    def create_chm(self, dsm_path:str, dtm_path:str):
        """
        """
        try:
            
            dsm =  rasterio.open(dsm_path)
            window_block = rasterio.windows.from_bounds(self.x_min, self.y_min, self.x_max, self.y_max, transform=dsm.window_transform)
            block_dsm = dsm.read(1, window=window_block)
            dtm =  rasterio.open(dtm_path)
            block_dtm = dtm.read(1, window=window_block)
            cols, row = np.meshgrid(np.arange(block_dsm.shape[1]), np.arange(block_dtm.shape[0]))
        except:
            pass
        else:
            pass
    
    def create_building_polygon(self):
        """
        """
        try:
            for path in os.listdir('data/CaPa-CaBu/'):
                df = gpd.read_file(path,bbox=(self.longitude,self.latitude,self.longitude,self.latitude))
                if(df.size > 0):
                    self.x_max = df.geometry.bounds.iloc[0]['maxx']
                    self.x_min = df.geometry.bounds.iloc[0]['minx']
                    self.y_max = df.geometry.bounds.iloc[0]['maxy']
                    self.y_min = df.geometry.bounds.iloc[0]['miny']
                    break
        except FileNotFoundError:
            print("CaPa/CaBu file not found.")
        except:
            print("Dataframe couldn't readed.")
            
    
    def plot3D(self,column:np.ndarray, row:np.ndarray, dsm:np.ndarray, dtm:np.ndarray):
        """
        A function 
        """
        try:
            building = go.Figure(data=[go.Surface(y=column, x=row, z=(dsm-dtm))])
        except:
            pass
        else:
            building.show()

    def generate3Dhouse(self):
        """
        A function
        """
        if(self.check_geofile_path()):
            chm_file_path = self.create_chm(path=self.correct_tiff_path)
        else:
            print('GeoTiFF file not found.')
    
    

        





    
    