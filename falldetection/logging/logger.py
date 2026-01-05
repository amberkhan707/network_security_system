import logging
import os
from datetime import datetime

# 1. Log file name (timestamp based)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Logs directory (ONLY folder path)
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# 3. Full log file path
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# 4. Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
