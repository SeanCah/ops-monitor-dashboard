import logging
import os


LOG_FILE = "logs/app.log"


def setup_logger():
    """
    Configure logging for the application.
    """
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("ops_monitor")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger