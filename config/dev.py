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
USER_SETTINGS_FILE = CONFIG_DIR / "user_settings.json"
FORM_FIELDS_FILE   = CORE_DIR / "config" / "form_fields.json"
BASE_STYLE_FILE    = GUI_DIR / "styles" / "base_style.json"

# Theme file dictionary for dynamic access
THEME_FILES = {
    "Future_dark":    GUI_DIR / "styles" / "theme_Future_dark.json",
    "Future_light":   GUI_DIR / "styles" / "theme_Future_light.json",
    "Future_neutral": GUI_DIR / "styles" / "theme_Future_neutral.json",
    "Modern_dark":    GUI_DIR / "styles" / "theme_Modern_dark.json",
    "Modern_light":   GUI_DIR / "styles" / "theme_Modern_light.json",
    "Modern_neutral": GUI_DIR / "styles" / "theme_Modern_neutral.json",
    "Minimal_dark":   GUI_DIR / "styles" / "theme_Minimal_dark.json",
    "Minimal_light":  GUI_DIR / "styles" / "theme_Minimal_light.json",
    "Minimal_neutral":GUI_DIR / "styles" / "theme_Minimal_neutral.json",
    "Oldschool_dark": GUI_DIR / "styles" / "theme_Oldschool_dark.json",
    "Oldschool_light":GUI_DIR / "styles" / "theme_Oldschool_light.json",
    "Oldschool_neutral":GUI_DIR / "styles" / "theme_Oldschool_neutral.json",
    "Vintage_dark":   GUI_DIR / "styles" / "theme_Vintage_dark.json",
    "Vintage_light":  GUI_DIR / "styles" / "theme_Vintage_light.json",
    "Vintage_neutral":GUI_DIR / "styles" / "theme_Vintage_neutral.json"
}

LOG_FILE = BASE_DIR / "csnova.log"

# Ensure directories exist (no logging here!)
for dir_path in [DATA_DIR, CONFIG_DIR, ASSETS_DIR, DOCS_DIR, GUI_DIR, CORE_DIR, TRANSLATIONS_DIR, TABLES_DIR]:
    dir_path.mkdir(exist_ok=True)