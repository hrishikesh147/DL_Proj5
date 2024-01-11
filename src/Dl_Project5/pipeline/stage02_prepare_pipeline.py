from src.Dl_Project5.config.configuration import ConfigurationManager
from src.Dl_Project5.components.prepare_base_model import PrepareBaseModel
from src.Dl_Project5 import logger

class PrepareBaseModel_Training_Pipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepara_basemodel_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e
        
STAGE_NAME="Prepare base Model"

if __name__=="__main__":
    try:
        logger.info(f"Stage Name {STAGE_NAME} started...")
        obj=PrepareBaseModel_Training_Pipeline()    
        obj.main()
        logger.info(f"Stage Name {STAGE_NAME} Completed...")
    except Exception as e:
        raise e