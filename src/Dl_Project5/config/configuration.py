from src.Dl_Project5.utils.common import create_directories,load_yaml
from src.Dl_Project5.constants import *
from src.Dl_Project5.entity.config_entity import DataIngestionConfig
from src.Dl_Project5.entity.config_entity import PreparaBaseModelConifig
from src.Dl_Project5.entity.config_entity import PrepareCallbacksConfig
from src.Dl_Project5.entity.config_entity import TrainingConfig
from src.Dl_Project5.entity.config_entity import EvaluationConfig
from pathlib import Path

import os

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config=load_yaml(config_filepath)
        self.params=load_yaml(params_file_path)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_configuration(self) -> DataIngestionConfig:

        create_directories([self.config.data_ingestion.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=self.config.data_ingestion.root_dir,
            source_url=self.config.data_ingestion.source_url,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir
        )

        return data_ingestion_config
    
    def get_prepara_basemodel_config(self)-> PreparaBaseModelConifig:
        
        create_directories([self.config.prepare_base_model.root_dir])

        prepare_base_model=PreparaBaseModelConifig(
            root_dir=self.config.prepare_base_model.root_dir,
            base_model_path=self.config.prepare_base_model.base_model_path,
            updated_base_model_path=self.config.prepare_base_model.updated_base_model_path,
            IMAGE_SIZE=self.params.IMAGE_SIZE,
            LEARNING_RATE=self.params.LEARNING_RATE,
            INCLUDE_TOP=self.params.INCLUDE_TOP,
            WEIGHTS=self.params.WEIGHTS,
            CLASSES=self.params.CLASSES

        )

        return prepare_base_model
    
    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chicken-fecal-images")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    
    def get_validation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model=Path("artifacts/training/model.h5"),
            training_data=Path("artifacts/data_ingestion/Chicken-fecal-images"),
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config
    
