from src.Dl_Project5.config.configuration import ConfigurationManager
from src.Dl_Project5.components.data_ingestion import DataIngestion
from src.Dl_Project5 import logger

STAGE_NAME="Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingest_conf=config.get_data_ingestion_configuration()
        data_inge=DataIngestion(config=data_ingest_conf)
        data_inge.download_data()
        data_inge.extract_zip_file()

if __name__=='__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} started... ")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} Completed SUCCESSFULLY... ")
    except Exception as e:
        raise e


