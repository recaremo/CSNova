# config/dev.py
#folder structure of csnova
from pathlib import Path
import sys

# Import zentrale Logging-Funktionen (optional)
from core.lloger import log_section, log_subsection, log_info, log_error

log_section("dev.py")
log_subsection("path_setup")

try:
    if getattr(sys, 'frozen', False):
        BASE_DIR = Path(sys.executable).parent
        log_info(f"Running frozen, BASE_DIR set to {BASE_DIR}")
    else:
        BASE_DIR = Path(__file__).resolve().parent
        log_info(f"Running script, BASE_DIR set to {BASE_DIR}")

    DATA_DIR = BASE_DIR.parent / "data"
    DATA_DIR.mkdir(exist_ok=True)
    log_info(f"DATA_DIR ensured at {DATA_DIR}")

    DB_PATH = DATA_DIR / "csnova.db"
    log_info(f"DB_PATH set to {DB_PATH}")
except Exception as e:
    log_error(f"Error setting up paths in dev.py: {e}")