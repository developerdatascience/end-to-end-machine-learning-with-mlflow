import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import joblib
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read Yaml file and returns

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty") from e
    except Exception as e:
        raise e
    


@ensure_annotations
def load_json(path: Path, data: dict):
    """
    save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) ->Any:
    """
    Load binary file

    Args:
        path (Path): Path to binary file
    
    Returns:
        Any: Object stored in a file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) ->str:
    """get size in Kb
    Args:
        path (Path): path of the file
    Returns:
        str: size in  Kb
    """

    size_in_kb = round(os.path.getsize(filename=path)/1024)
    return f"~{size_in_kb} KB"