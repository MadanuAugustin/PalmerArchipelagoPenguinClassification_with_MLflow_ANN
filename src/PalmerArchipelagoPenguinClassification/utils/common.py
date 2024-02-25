from pathlib import Path
from box import ConfigBox
import yaml
from loggerFile.logger import logger
import os
import json
from typing import Any
import joblib



def read_yaml(yaml_path : Path) -> ConfigBox:
    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {yaml_path} loaded successfully...!')
            return ConfigBox(content)

    except:
        pass


def create_directories(directories_path : list, verbose = True):
    for path in directories_path:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f'created directory at : {path}')



def save_json(path : Path, data : dict):

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'json file saved at : {path}...!')



def load_json(path : Path) -> ConfigBox:

    with open(path) as f:
        content = json.load(f)

    logger.info(f'json file loaded successfully at : {path}...!')

    return ConfigBox(content)



def save_bin(data : Any, path : Path):

    joblib.dump(value = data, filename=path)
    logger.info(f'joblib file saved at : {path}...!')



def load_bin(path : Path) -> Any : 
    data = joblib.load(path)
    logger.info(f'joblib file loaded successfully at : {path}')
    return data



def get_size(path : Path) -> str:

    file_size = round(os.path.getsize(path)/1024)
    return f'{file_size} Kb'




