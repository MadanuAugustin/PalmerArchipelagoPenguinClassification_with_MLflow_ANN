
from src.PalmerArchipelagoPenguinClassification.entity.config_entity import DataIngestionConfig
import os
import urllib.request as request
from loggerFile.logger import logger
from src.PalmerArchipelagoPenguinClassification.utils.common import get_size
from pathlib import Path
import zipfile

class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config



    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )

            logger.info(f'{filename} downloaded successfully and saved at : {self.config.local_data_file}')


        else:
            logger.info(f'{filename} already exists with the size of : {get_size(Path(self.config.local_data_file))}')
            pass


    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(unzip_path)