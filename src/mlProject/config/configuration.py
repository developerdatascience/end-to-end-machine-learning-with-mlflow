from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import (DataIngestionConfig, 
                                            DataValidationConfig,
                                            DataTransformationConfig)



class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_ingestion_data_config(self) ->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])
        return DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            unzip_data_dir= config.unzip_data_dir,
            all_schema=schema
        )
    
    def get_data_transformation_config(self) ->DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])
        return DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path
        )