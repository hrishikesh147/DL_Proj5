from src.Dl_Project5 import logger
from src.Dl_Project5.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.Dl_Project5.pipeline.stage02_prepare_pipeline import PrepareBaseModel_Training_Pipeline
from src.Dl_Project5.pipeline.stage03_training import ModelTrainingPipeline
from src.Dl_Project5.pipeline.stage04_evaluation import EvaluationPipeline

STAGE_NAME="Data Ingestion"
try:
    logger.info(f"Stage {STAGE_NAME} started... ")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed SUCCESSFULLY... ")
except Exception as e:
    raise e

STAGE_NAME="Prepare Base Model"
try:
    logger.info(f"Stage Name {STAGE_NAME} started...")
    obj=PrepareBaseModel_Training_Pipeline()    
    obj.main()
    logger.info(f"Stage Name {STAGE_NAME} Completed SUCCESSFULLY...")
except Exception as e:
    raise e

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e