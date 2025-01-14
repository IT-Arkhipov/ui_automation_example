import logging

import os
from datetime import datetime

from selenium_framework.automationexercise import project_folder

log_folder = os.path.join(project_folder, "logs")
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_file_name = os.path.join(log_folder, f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logger = logging.getLogger()

logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)8s] %(message)s', datefmt="%d/%m %H:%M:%S")
handler = logging.FileHandler(log_file_name, 'w', encoding='utf-8')
handler.setFormatter(formatter)
logger.addHandler(handler)
