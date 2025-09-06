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
USER_SETTINGS_FILE    = CONFIG_DIR / "user_settings.json"
FORM_FIELDS_FILE = CORE_DIR / "config" / "form_fields.json"
BG_IMAGE_PATH    = ASSETS_DIR / "media" / "csNova_background_start.png"
BASE_STYLE_FILE = GUI_DIR / "styles" / "base_style.json"
THEMES_STYLE_FILE = GUI_DIR / "styles" / "themes_style.json"
CSNOVA_BASE_STYLE_FILE = GUI_DIR / "styles" / "csNova_base_style.json"
CSNOVA_FORMS_STYLE_FILE = GUI_DIR / "styles" / "csNova_forms_style.json"
CSNOVA_THEMES_STYLE_FILE = GUI_DIR / "styles" / "csNova_themes_style.json"

# Ensure directories exist (no logging here!)
for dir_path in [DATA_DIR, CONFIG_DIR, ASSETS_DIR, DOCS_DIR]:
    dir_path.mkdir(exist_ok=True)

LOG_FILE = BASE_DIR / "csnova.log"