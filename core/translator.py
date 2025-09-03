import json
from config.dev import TRANSLATIONS_DIR
from core.logger import log_section, log_subsection, log_info, log_exception

class Translator:
    """
    Translator class for dynamic UI translation.
    Loads translations from translations.json and provides translation lookup for label_keys.
    Dependencies:
      - config.dev.TRANSLATIONS_DIR: Directory path for translations.json
      - core.logger: Logging functions for error and info tracking
    Used by:
      - All GUI forms and windows to translate labels, buttons, help texts, etc.
    """

    def __init__(self, lang="en"):
        """
        Initialize the Translator with a language code.
        Loads translations for the selected language.
        """
        log_section("translator.py")
        log_subsection("__init__")
        self.lang = lang
        self.translations = {}
        self._load_translations()

    def _load_translations(self):
        """
        Loads translations from translations.json for the current language.
        The file contains a dict with language codes as keys.
        Stores the translation dict for the selected language in self.translations.
        Logs errors if loading fails.
        """
        log_subsection("_load_translations")
        try:
            path = TRANSLATIONS_DIR / "translations.json"
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Get the translation dict for the current language
            self.translations = data.get(self.lang, {})
            log_info(f"Translations loaded for language '{self.lang}'.")
        except Exception as e:
            log_exception("Error loading translations", e)
            self.translations = {}

    def set_language(self, lang_code):
        """
        Change the language and reload translations.
        Used when the user switches the UI language.
        """
        log_subsection("set_language")
        self.lang = lang_code
        self._load_translations()

    def tr(self, label_key):
        """
        Translate a label_key using the loaded translations.
        If the key is not found, returns the key itself as fallback.
        Used by all forms and windows to get the correct UI label.
        """
        log_subsection("tr")
        return self.translations.get(label_key, label_key)

    def help_text(self, label_key):
        """
        Returns help text for a given label_key.
        Internally uses tr(), so it works for any key in translations.json.
        """
        log_subsection("help_text")
        return self.tr(label_key)