from pathlib import Path
from src.PalmerArchipelagoPenguinClassification.config.configuration import ConfigurationManager
from src.PalmerArchipelagoPenguinClassification.components.data_transformation import DataTransformation
from exceptionFile.exception import CustomException
import sys


STAGE_NAME = 'Data_Transformation_Stage'


class DataTransformationPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path('artifacts//data_validation//status.txt'), 'r') as f:
                status = f.read().split(" ")[-1]


            if status  == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.transformation_fun()

            else:
                print('your schema is not valid please check...!')

        except Exception as e:
            raise CustomException(e, sys)