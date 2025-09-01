import json
from config.dev import TRANSLATIONS_DIR
from core.logger import log_section, log_subsection, log_info, log_exception

class Translator:
    def __init__(self, lang="en"):
        log_section("translator.py")
        log_subsection("__init__")
        self.lang = lang
        self.translations = {}
        self._load_translations()

    def _load_translations(self):
        log_subsection("_load_translations")
        try:
            path = TRANSLATIONS_DIR / "translations.json"
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for entry in data:
                if entry.get("ID") == self.lang:
                    self.translations = entry
                    break
            log_info(f"Translations loaded for language '{self.lang}'.")
        except Exception as e:
            log_exception("Error loading translations", e)
            self.translations = {}

    def set_language(self, lang_code):
        log_subsection("set_language")
        self.lang = lang_code
        self._load_translations()

    def tr(self, key):
        log_subsection("tr")
        # Flache Struktur oder gruppiert
        return (
            self.translations.get(key)
            or self.translations.get("form_labels", {}).get(key)
            or self.translations.get("help_texts", {}).get(key)
            or key
        )

    def form_label(self, key):
        log_subsection("form_label")
        # Erst gruppiert, dann flach
        return (
            self.translations.get("form_labels", {}).get(key)
            or self.translations.get(key)
            or key
        )

    def help_text(self, key):
        log_subsection("help_text")
        # Erst gruppiert, dann flach
        return (
            self.translations.get("help_texts", {}).get(key)
            or self.translations.get(key)
            or key
        )

    @property
    def form_labels(self):
        # Gibt alle Label-Keys als Dictionary zurück (gruppiert oder flach)
        if "form_labels" in self.translations:
            return self.translations["form_labels"]
        # Fallback: alle Keys mit typischen Label-Namen
        return {k: v for k, v in self.translations.items() if any(x in k for x in ["label", "btn", "title", "name"])}