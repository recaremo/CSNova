# core/translator.py

from core.translations.translations import TRANSLATIONS, LANGUAGES

# Import zentrale Logging-Funktionen
from core.lloger import log_section, log_subsection, log_info, log_error

class Translator:
    def __init__(self, default=""):
        log_section("translator.py")
        log_subsection("__init__")
        try:
            self.lang = default if default in LANGUAGES else LANGUAGES[0]
            log_info(f"Translator initialized with language '{self.lang}'.")
        except Exception as e:
            log_error(f"Error initializing Translator: {str(e)}")

    def set_language(self, lang_code):
        log_subsection("set_language")
        try:
            if lang_code in TRANSLATIONS:
                self.lang = lang_code
                log_info(f"Language set to '{lang_code}'.")
            else:
                log_error(f"Language code '{lang_code}' not found in TRANSLATIONS.")
        except Exception as e:
            log_error(f"Error setting language: {str(e)}")

    def tr(self, key):
        log_subsection("tr")
        try:
            value = TRANSLATIONS[self.lang].get(
                key, TRANSLATIONS["en"].get(key, key)
            )
            log_info(f"Translation for key '{key}': '{value}'")
            return value
        except Exception as e:
            log_error(f"Error translating key '{key}': {str(e)}")
            return key