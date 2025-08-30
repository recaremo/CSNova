from pathlib import Path
import sys

# Import central logging functions (optional)
from core.lloger import log_section, log_subsection, log_info, log_error

log_section("dev.py")
log_subsection("path_setup")

try:
    # Determine base directory (supports both frozen and script mode)
    if getattr(sys, 'frozen', False):
        BASE_DIR = Path(sys.executable).parent
        log_info(f"Running frozen, BASE_DIR set to {BASE_DIR}")
    else:
        BASE_DIR = Path(__file__).resolve().parent.parent
        log_info(f"Running script, BASE_DIR set to {BASE_DIR}")

    # Main directories
    DATA_DIR         = BASE_DIR / "data"
    CONFIG_DIR       = BASE_DIR / "config"
    ASSETS_DIR       = BASE_DIR / "assets"
    DOCS_DIR         = BASE_DIR / "docs"
    GUI_DIR          = BASE_DIR / "gui"
    CORE_DIR         = BASE_DIR / "core"
    TRANSLATIONS_DIR = CORE_DIR / "translations"
    TABLES_DIR       = CORE_DIR / "tables"

    # Important files
    DB_PATH          = DATA_DIR / "csnova.db"
    SETTINGS_FILE    = CONFIG_DIR / "user_settings.json"
    BG_IMAGE_PATH    = ASSETS_DIR / "media" / "csNova_background_start.png"

    # Translation and help files
    HELP_DIR         = TRANSLATIONS_DIR / "help"
    FORMS_DIR        = TRANSLATIONS_DIR / "forms"

    # Ensure directories exist
    DATA_DIR.mkdir(exist_ok=True)
    CONFIG_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(exist_ok=True)
    DOCS_DIR.mkdir(exist_ok=True)

    log_info(f"DATA_DIR ensured at {DATA_DIR}")
    log_info(f"DB_PATH set to {DB_PATH}")
    log_info(f"SETTINGS_FILE set to {SETTINGS_FILE}")
    log_info(f"BG_IMAGE_PATH set to {BG_IMAGE_PATH}")
    log_info(f"TRANSLATIONS_DIR set to {TRANSLATIONS_DIR}")
    log_info(f"HELP_DIR set to {HELP_DIR}")
    log_info(f"FORMS_DIR set to {FORMS_DIR}")

except Exception as e:
    log_error(f"Error setting up paths in dev.py: {e}")