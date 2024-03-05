


from loggerFile.logger import logger
from src.PalmerArchipelagoPenguinClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.PalmerArchipelagoPenguinClassification.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.PalmerArchipelagoPenguinClassification.pipeline.stage_03_data_transformation import DataTransformationPipeline
from exceptionFile.exception import CustomException
import sys






STAGE_NAME = 'Data_Ingestion_Stage'


try:
    logger.info(f'---------------{STAGE_NAME} started------------------')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'--------------{STAGE_NAME} completed-----------------')
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = 'Data_Validation_Stage'

try:
    logger.info(f'---------------{STAGE_NAME} started----------------------')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'-----------------{STAGE_NAME} completed-------------------')
except Exception as e:
    raise CustomException(e, sys)



STAGE_NAME = 'Data_Transformation_Stage'

try:
    logger.info(f'-------------------------{STAGE_NAME} started ---------------------')
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f'-------------------------{STAGE_NAME} completed------------------')
except Exception as e:
    raise CustomException(e, sys)