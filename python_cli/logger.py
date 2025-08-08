import logging
from config import LOG_FILE

# Configurare logger
logger = logging.getLogger("math_service")
logger.setLevel(logging.DEBUG)

# Format mesaje
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Handler fișier log
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
