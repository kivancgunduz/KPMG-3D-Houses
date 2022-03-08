import os
from pathlib import Path
from zipfile import ZipFile
import wget



class GeoFileDownloader():
    """
    """
    def __init__(self) -> None:
        self.main_dsm_folder_path: str = '../data/DSM'
        self.main_dtm_folder_path: str = '../data/DTM'
        self.main_dsm_url: str = 'https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dsm-raster-1m/DHMVIIDSMRAS1m_k'
        self.main_dtm_url: str = 'https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dtm-raster-1m/DHMVIIDTMRAS1m_k'
        print('Initializing Folders...')
        if(self.createDataFolderIfnotExist()): print('Folder created.')
        else: print('Folder creating error.')
    
    def createDataFolderIfnotExist(self) -> bool:
        """
        """
        try:
            if not os.path.exists(self.main_dsm_folder_path):
                os.makedirs(self.main_data_folder_path)
            if not os.path.exists(self.main_dtm_folder_path):
                os.makedirs(self.main_dtm_folder_path)
        except:
            return False
        else:
            return True

    def start_downloader(self, isDsm: bool = True, isDtm: bool = True, isCapa: bool = True):
        """
        """
        for i in range(1, 44):
            if i < 10:
                folder_name = f'0{i}.zip'
                path_directory = os.path.join(self.main_dsm_folder_path,folder_name)
                if not os.path.isfile(path_directory):
                    if(isDsm):
                        pass
                    if(isDtm):
                        pass
            elif i > 10:
                if(isDsm):
                    pass
                if(isDtm):
                    pass
        
        if(isCapa):
            pass
