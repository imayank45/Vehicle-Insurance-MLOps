import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pathlib import Path

# Explicitly define the project root by moving three levels up from `logger.py`
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # Now correctly points to `C:\MLOps\Vehicle-Insurance-MLOps`

# Define logs directory inside project root
LOG_DIR = PROJECT_ROOT / 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Number of backup log files to keep

# Create log directory if it doesn't exist
LOG_DIR.mkdir(parents=True, exist_ok=True)
log_file_path = LOG_DIR / LOG_FILE

print(f"Log directory path: {LOG_DIR}")  # Debugging output


def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.
    """
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# Configure the logger when the module is imported
configure_logger()
