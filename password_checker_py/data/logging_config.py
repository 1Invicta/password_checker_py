# [ logging_config.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import logging

from pathlib import         Path
from datetime import    datetime

LOGS_DIR = Path(__file__).parent / "logs"


def setup_logging( log_to_file: bool=False, log_dir: str | Path = LOGS_DIR, level=logging.INFO ):
    """Sets up logging system (log file system I/O)."""

    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    
    if root_logger.handlers:
        return

    if log_to_file:
        log_dir = Path(log_dir)
        log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        logfile = log_dir / f"pass_chk_py_{timestamp}.log"

        file_handler = logging.FileHandler(logfile, encoding="utf-8")
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

        root_logger.info("Logging to file: %s", logfile)
