


from loggerFile.logger import logger
from src.PalmerArchipelagoPenguinClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline








STAGE_NAME = 'Data_Ingestion_Stage'


try:
    logger.info(f'---------------{STAGE_NAME} started------------------')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'--------------{STAGE_NAME} completed-----------------')
except:
    pass