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
BASE_STYLE_FILE = GUI_DIR / "styles" / "base_style.json"
THEME_FUTURE_DARK_FILE = GUI_DIR / "styles" / "theme_Future_dark.json"
THEME_FUTURE_LIGHT_FILE = GUI_DIR / "styles" / "theme_Future_light.json"
THEME_FUTURE_NEUTRAL_FILE = GUI_DIR / "styles" / "theme_Future_neutral.json"
THEME_MODERN_DARK_FILE = GUI_DIR / "styles" / "theme_Modern_dark.json"
THEME_MODERN_LIGHT_FILE = GUI_DIR / "styles" / "theme_Modern_light.json"
THEME_MODERN_NEUTRAL_FILE = GUI_DIR / "styles" / "theme_Modern_neutral.json"
THEME_MINIMAL_DARK_FILE = GUI_DIR / "styles" / "theme_Minimal_dark.json"
THEME_MINIMAL_LIGHT_FILE = GUI_DIR / "styles" / "theme_Minimal_light.json"
THEME_MINIMAL_NEUTRAL_FILE = GUI_DIR / "styles" / "theme_Minimal_neutral.json"
THEME_OLDSCHOOL_DARK_FILE = GUI_DIR / "styles" / "theme_Oldschool_dark.json"
THEME_OLDSCHOOL_LIGHT_FILE = GUI_DIR / "styles" / "theme_Oldschool_light.json"
THEME_OLDSCHOOL_NEUTRAL_FILE = GUI_DIR / "styles" / "theme_Oldschool_neutral.json"
THEME_VINTAGE_DARK_FILE = GUI_DIR / "styles" / "theme_Vintage_dark.json"
THEME_VINTAGE_LIGHT_FILE = GUI_DIR / "styles" / "theme_Vintage_light.json"
THEME_VINTAGE_NEUTRAL_FILE = GUI_DIR / "styles" / "theme_Vintage_neutral.json"

# Ensure directories exist (no logging here!)
for dir_path in [DATA_DIR, CONFIG_DIR, ASSETS_DIR, DOCS_DIR]:
    dir_path.mkdir(exist_ok=True)

LOG_FILE = BASE_DIR / "csnova.log"