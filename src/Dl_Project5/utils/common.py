from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from src.Dl_Project5 import logger
import yaml
import os
import json

def load_yaml(path_yaml: Path) -> ConfigBox:
    try:
        with open(path_yaml,"r") as p_yaml:
            p_yaml=yaml.safe_load(p_yaml)
            logger.info(f"{p_yaml} loaded successfully")
            return ConfigBox(p_yaml)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
def load_json(pat_json:Path) -> ConfigBox:
    try:
        with open(pat_json,"r") as f:
            f=json.load(f)
            logger.info(f"json file: {f} loaded successfully")
        return ConfigBox(f)
    
    except BoxValueError:
        raise ValueError("cannot be loaded as empty")
    except Exception as e:
        raise e
    
def create_directories(path_dir: list, verbose=True):
    try:
        for path in path_dir:
            os.makedirs(path, exist_ok=True)
            logger.info(f"created directory {path} successfully")

    except BoxValueError:
        raise ValueError("No directory present")
    except Exception as e:
        raise e
    
def save_json(path_json:Path,data:dict):
    try:
        with open(path_json,"w") as f:
            json.dump(data,f,indent=4)
            logger.info("json file saved successfully")

    except BoxValueError:
        raise ValueError("cannnot be saved")
    except Exception as e:
        raise e
    



    
    