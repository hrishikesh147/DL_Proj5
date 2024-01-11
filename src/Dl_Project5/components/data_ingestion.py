import os
from pathlib import Path
from src.Dl_Project5 import logger
import urllib.request as request
import zipfile
from src.Dl_Project5.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info("File created successfully")
        else:
            logger.info("File already exist")

    
    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)