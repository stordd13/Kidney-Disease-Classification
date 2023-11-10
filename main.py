from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline



STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx==========x")
except Exception as e:
    raise e