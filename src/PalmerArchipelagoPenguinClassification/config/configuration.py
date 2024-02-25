from src.PalmerArchipelagoPenguinClassification.constants import *
from src.PalmerArchipelagoPenguinClassification.utils.common import read_yaml, create_directories
from src.PalmerArchipelagoPenguinClassification.entity.config_entity import DataIngestionConfig



class ConfigurationManager:
    def __init__(self, config_filepath = ConfigFilePath, schema_filepath = SchemaFilePath, params_filepath = ParamsFilePath):
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        self.params = read_yaml(params_filepath)


        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.DataIngestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
