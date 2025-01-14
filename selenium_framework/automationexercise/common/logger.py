import logging
import os
import shutil

from datetime import datetime

from selenium_framework.automationexercise import project_folder
from selenium_framework.automationexercise.common.settings import settings


log_folder = os.path.join(project_folder, "logs")
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_file_name = os.path.join(log_folder, "_current.log")

if os.path.exists(log_file_name):
    backup_name = f"archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    backup_log_file = os.path.join(log_folder, backup_name)
    try:
        shutil.move(log_file_name, backup_log_file)
    except FileNotFoundError:
        pass

logger = logging.getLogger(__name__)

logger.setLevel(settings.logging_level)
formatter = logging.Formatter('%(asctime)s [%(levelname)8s] %(message)s', datefmt="%d/%m %H:%M:%S")
handler = logging.FileHandler(log_file_name, 'w', encoding='utf-8')
handler.setFormatter(formatter)
logger.addHandler(handler)
