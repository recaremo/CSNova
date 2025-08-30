import json
from config.dev import TRANSLATIONS_DIR, FORMS_DIR, HELP_DIR
from core.logger import log_section, log_subsection, log_info, log_error

class Translator:
    def __init__(self, lang="en"):
        log_section("translator.py")
        log_subsection("__init__")
        try:
            self.lang = lang
            self.translations = self._load_json(TRANSLATIONS_DIR / f"{lang}.json")
            self.form_labels = self._load_json(FORMS_DIR / f"form_{lang}.json")
            self.help_texts = self._load_json(HELP_DIR / f"help_{lang}.json")
            log_info(f"Translator initialized with language '{self.lang}'.")
        except Exception as e:
            log_error(f"Error initializing Translator: {str(e)}")

    def _load_json(self, path):
        log_subsection(f"_load_json: {path}")
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                log_info(f"Loaded translations from {path}")
                return data
        except Exception as e:
            log_error(f"Error loading {path}: {e}")
            return {}

    def set_language(self, lang_code):
        log_subsection("set_language")
        try:
            self.lang = lang_code
            self.translations = self._load_json(TRANSLATIONS_DIR / f"{lang_code}.json")
            self.form_labels = self._load_json(FORMS_DIR / f"form_{lang_code}.json")
            self.help_texts = self._load_json(HELP_DIR / f"help_{lang_code}.json")
            log_info(f"Language set to '{lang_code}'.")
        except Exception as e:
            log_error(f"Error setting language: {str(e)}")

    def tr(self, key):
        log_subsection("tr")
        try:
            value = self.translations.get(key, key)
            log_info(f"Translation for key '{key}': '{value}'")
            return value
        except Exception as e:
            log_error(f"Error translating key '{key}': {str(e)}")
            return key

    def form_label(self, key):
        log_subsection("form_label")
        try:
            value = self.form_labels.get(key, key)
            log_info(f"Form label for key '{key}': '{value}'")
            return value
        except Exception as e:
            log_error(f"Error getting form label for key '{key}': {str(e)}")
            return key

    def help_text(self, key):
        log_subsection("help_text")
        try:
            value = self.help_texts.get(key, "Help and information will be displayed here.")
            log_info(f"Help text for key '{key}': '{value}'")
            return value
        except Exception as e:
            log_error(f"Error getting help text for key '{key}': {str(e)}")
            return "Help and information will be displayed here."