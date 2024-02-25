


from loggerFile.logger import logger
from src.PalmerArchipelagoPenguinClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.PalmerArchipelagoPenguinClassification.pipeline.stage_02_data_validation import DataValidationTrainingPipeline







STAGE_NAME = 'Data_Ingestion_Stage'


try:
    logger.info(f'---------------{STAGE_NAME} started------------------')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'--------------{STAGE_NAME} completed-----------------')
except:
    pass


STAGE_NAME = 'Data_Validation_Stage'

try:
    logger.info(f'---------------{STAGE_NAME} started----------------------')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'-----------------{STAGE_NAME} completed-------------------')
except:
    pass