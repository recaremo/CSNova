from pathlib import Path
import sys

# Determine base directory (supports both frozen and script mode)
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

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
LOG_FILE = BASE_DIR / "csnova.log"