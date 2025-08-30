from pathlib import Path
import json

# Import zentrale Logging-Funktionen
from core.lloger import log_section, log_subsection, log_info, log_error

LANGUAGES = ["de", "en", "fr", "es"]
TRANSLATIONS = {}

log_section("translations.py")
log_subsection("load_translations")

for lang in LANGUAGES:
    path = Path(__file__).parent / f"{lang}.json"
    try:
        with open(path, "r", encoding="utf-8") as f:
            TRANSLATIONS[lang] = json.load(f)
        log_info(f"Loaded translations for '{lang}' from {path}.")
    except Exception as e:
        log_error(f"Error loading translations for '{lang}' from {path}: {str(e)}")
        TRANSLATIONS[lang] = {}