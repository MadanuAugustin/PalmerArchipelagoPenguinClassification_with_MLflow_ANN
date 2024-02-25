
from src.PalmerArchipelagoPenguinClassification.config.configuration import ConfigurationManager
from src.PalmerArchipelagoPenguinClassification.entity.config_entity import DataValidationConfig






STAGE_NAME = 'Data_Validation_Stage'


class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidationConfig(config = data_validation_config)
        data_validation.validate_all_columns()
