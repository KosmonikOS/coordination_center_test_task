import logging
import os
from datetime import datetime


def setup_logging():
    """Configure logging to file with timestamp."""
    log_filename = f"logs/app_{datetime.now().strftime('%Y%m%d')}.log"
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Add console handler to also show logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)
