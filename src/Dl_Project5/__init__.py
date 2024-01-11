import logging
import sys
import os

log_dir="logs"
os.makedirs(log_dir,exist_ok=True)
log_filepath=os.path.join(log_dir,"running_logs.log")

logging.basicConfig(
    format='[%(asctime)s: %(levelname)s: %(message)s]',
    level=logging.INFO,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger()