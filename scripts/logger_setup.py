# scripts/logger_setup.py
import logging
from datetime import datetime
from pathlib import Path

# Ensure logs/ folder exists
Path("logs").mkdir(exist_ok=True)

# Log file name: logs/run_log_YYYY-MM-DD.log
log_file = f"logs/run_log_{datetime.now().strftime('%Y-%m-%d')}.log"

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Export this logger object
logger = logging.getLogger()