from dataclasses import dataclass
from pathlib import Path
import os
import urllib.request as requests
import zipfile

from mlProject.constants import *
from mlProject.utils.common import create_directories, read_yaml
from mlProject import logger
from mlProject.utils.common import get_size


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


class ConfigurationManager:
    def __init__(self, 
                 config_filepath: CONFIG_FILE_PATH,
                 params_filepath: PARAMS_FILE_PATH,
                 schema_filepath: SCHEMA_FILE_PATH) ->None:

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

    
    def get_ingestion_data_config(self) ->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
