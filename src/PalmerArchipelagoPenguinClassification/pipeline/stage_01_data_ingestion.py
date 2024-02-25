

from src.PalmerArchipelagoPenguinClassification.config.configuration import ConfigurationManager
from src.PalmerArchipelagoPenguinClassification.entity.config_entity import DataIngestionConfig








STAGE_NAME = 'DataIngestionStage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestionConfig(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()