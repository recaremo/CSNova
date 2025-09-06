from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
)
import json
from gui.styles.python_gui_styles import apply_theme_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import (
    CSNOVA_BASE_STYLE_FILE, CSNOVA_THEMES_STYLE_FILE, CSNOVA_FORMS_STYLE_FILE,
    BASE_STYLE_FILE, THEMES_STYLE_FILE, USER_SETTINGS_FILE, GUI_DIR, TRANSLATIONS_DIR, FORM_FIELDS_FILE
)
from core.style_utils import (
    generate_csnova_styles,
    save_user_settings,
    generate_translation_file
)
from pathlib import Path

class PreferencesWindow(QDialog):
    """
    Dialog für Benutzereinstellungen wie Sprache, Style und Theme.
    Lädt zentrale Styles und Themes aus den generierten JSON-Dateien.
    Änderungen werden über einen Callback ans Hauptfenster weitergegeben.
    """

    def __init__(self, parent, settings, translation_file, combined_style=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.settings = settings
            if translation_file is None:
                raise ValueError("translation_file must be a valid file path string.")
            if isinstance(translation_file, Path):
                translation_file = str(translation_file)
            if not isinstance(translation_file, (str, bytes)):
                raise ValueError("translation_file must be a valid file path string.")
            self.translation_file = translation_file

            self._load_translations()
            if combined_style is not None:
                self.combined_style = combined_style
            else:
                self._load_styles()

            self.setWindowTitle(self.translations.get("PrefWinTitle", "Einstellungen"))
            self.resize(
                self.settings.get("preferences_window", {}).get("width", 500),
                self.settings.get("preferences_window", {}).get("height", 320)
            )
            self._load_fields()
            self._init_ui()
            self._apply_current_style()
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing PreferencesWindow", e)
            self.translations = {}
            self.combined_style = {}

    def _load_translations(self):
        try:
            with open(self.translation_file, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
        except Exception as e:
            log_exception("Error loading translations in PreferencesWindow", e)
            self.translations = {}

    def _load_styles(self):
        try:
            with open(CSNOVA_BASE_STYLE_FILE, "r", encoding="utf-8") as f:
                base_style = json.load(f)
            with open(CSNOVA_THEMES_STYLE_FILE, "r", encoding="utf-8") as f:
                theme_style = json.load(f)
            self.combined_style = {**base_style, **theme_style}
        except Exception as e:
            log_exception("Error loading styles in PreferencesWindow", e)
            self.combined_style = {}

    def _load_fields(self):
        try:
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                self.form_fields = json.load(f).get("preferences", [])
        except Exception as e:
            log_exception("Error loading form_fields.json in PreferencesWindow.", e)
            self.form_fields = []

    def _init_ui(self):
        log_subsection("_init_ui")
        try:
            main_layout = QVBoxLayout(self)
            main_layout.setSpacing(8)
            main_layout.setContentsMargins(24, 18, 24, 18)

            self.combos = {}
            self.labels = {}

            for field in self.form_fields:
                label = QLabel(self.translations.get(field.get("label_key", ""), field.get("label_key", "")), self)
                combo = QComboBox(self)
                option_labels = []
                option_keys = []
                for opt in field.get("options", []):
                    option_labels.append(self.translations.get(opt.get("label_key", ""), opt.get("label_key", "")))
                    option_keys.append(opt.get("key", ""))

                combo.addItems(option_labels)

                # Sichere Initialisierung der aktuellen Werte
                name = field.get("name", "")
                if name == "language":
                    current_value = self.settings.get("general", {}).get("language", option_keys[0])
                elif name == "style":
                    current_value = self.settings.get("gui", {}).get("style", option_keys[0])
                elif name == "theme":
                    current_value = self.settings.get("gui", {}).get("theme", option_keys[0])
                else:
                    current_value = option_keys[0]

                try:
                    idx = option_keys.index(current_value)
                except ValueError:
                    idx = 0
                combo.setCurrentIndex(idx)

                main_layout.addWidget(label)
                main_layout.addWidget(combo)
                self.combos[name] = (combo, option_keys)
                self.labels[name] = label

                if name == "style":
                    combo.currentIndexChanged.connect(self._on_style_changed)
                if name == "theme":
                    combo.currentIndexChanged.connect(self._on_theme_changed)

            main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

            btn_layout = QHBoxLayout()
            btn_layout.setSpacing(15)
            btn_layout.setContentsMargins(0, 0, 0, 0)
            self.save_btn = QPushButton(self.translations.get("PreferenceActionSave", "Speichern"), self)
            self.cancel_btn = QPushButton(self.translations.get("PreferenceActionCancel", "Abbrechen"), self)
            btn_layout.addStretch(1)
            btn_layout.addWidget(self.save_btn)
            btn_layout.addWidget(self.cancel_btn)
            btn_layout.addStretch(1)
            main_layout.addLayout(btn_layout)

            self.setLayout(main_layout)

            self.save_btn.clicked.connect(self._on_save)
            self.cancel_btn.clicked.connect(self._on_cancel)
            if "language" in self.combos:
                self.combos["language"][0].currentIndexChanged.connect(self._on_language_changed)

            try:
                apply_theme_style(self.save_btn, "button", self.combined_style)
                apply_theme_style(self.cancel_btn, "button", self.combined_style)
            except Exception as e:
                log_exception("Error applying theme style to preferences buttons", e)

            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI in PreferencesWindow", e)

    def _apply_current_style(self):
        try:
            apply_theme_style(self.save_btn, "button", self.combined_style)
            apply_theme_style(self.cancel_btn, "button", self.combined_style)
        except Exception as e:
            log_exception("Error applying stylesheet in PreferencesWindow", e)

    def update_translations(self):
        try:
            self.setWindowTitle(self.translations.get("PrefWinTitle", "Einstellungen"))
            for field in self.form_fields:
                name = field.get("name", "")
                self.labels[name].setText(self.translations.get(field.get("label_key", ""), field.get("label_key", "")))
                combo, option_keys = self.combos[name]
                combo.blockSignals(True)
                combo.clear()
                for opt in field.get("options", []):
                    combo.addItem(self.translations.get(opt.get("label_key", ""), opt.get("label_key", "")))
                if name == "language":
                    current_value = self.settings.get("general", {}).get("language", option_keys[0])
                elif name == "style":
                    current_value = self.settings.get("gui", {}).get("style", option_keys[0])
                elif name == "theme":
                    current_value = self.settings.get("gui", {}).get("theme", option_keys[0])
                else:
                    current_value = option_keys[0]
                try:
                    idx = option_keys.index(current_value)
                except ValueError:
                    idx = 0
                combo.setCurrentIndex(idx)
                combo.blockSignals(False)
            self.save_btn.setText(self.translations.get("PreferenceActionSave", "Speichern"))
            self.cancel_btn.setText(self.translations.get("PreferenceActionCancel", "Abbrechen"))
            self._apply_current_style()
        except Exception as e:
            log_exception("Error updating translations in PreferencesWindow", e)

    def _on_save(self):
        log_subsection("_on_save")
        try:
            for field in self.form_fields:
                name = field.get("name", "")
                combo, option_keys = self.combos[name]
                selected = option_keys[combo.currentIndex()]
                if name == "language":
                    self.settings.setdefault("general", {})["language"] = selected
                elif name == "style":
                    self.settings.setdefault("gui", {})["style"] = selected
                elif name == "theme":
                    self.settings.setdefault("gui", {})["theme"] = selected
            # Entferne flache Keys, falls vorhanden
            self.settings.pop("language", None)
            self.settings.pop("style", None)
            self.settings.pop("theme", None)
            save_user_settings(self.settings, USER_SETTINGS_FILE)
            if hasattr(self.parent(), "on_preferences_saved"):
                self.parent().on_preferences_saved(self.settings)
            self.accept()
            log_info("Settings saved and dialog accepted.")
        except Exception as e:
            log_exception("Error saving settings in PreferencesWindow", e)

    def _on_cancel(self):
        log_subsection("_on_cancel")
        try:
            self.reject()
            log_info("Dialog canceled and settings reverted.")
        except Exception as e:
            log_exception("Error canceling PreferencesWindow", e)

    def _on_language_changed(self, idx):
        log_subsection("_on_language_changed")
        try:
            combo, option_keys = self.combos["language"]
            lang_code = option_keys[idx]
            self.settings.setdefault("general", {})["language"] = lang_code
            translation_file = generate_translation_file(lang_code, TRANSLATIONS_DIR)
            self.translation_file = str(translation_file)
            self._load_translations()
            self.update_translations()
            save_user_settings(self.settings, USER_SETTINGS_FILE)
            if hasattr(self.parent(), "on_language_changed"):
                self.parent().on_language_changed(lang_code)
            log_info(f"Language changed to {lang_code}.")
        except Exception as e:
            log_exception("Error changing language in PreferencesWindow", e)

    def _on_style_changed(self, idx):
        log_subsection("_on_style_changed")
        try:
            combo, option_keys = self.combos["style"]
            style_key = option_keys[idx]
            self.settings.setdefault("gui", {})["style"] = style_key
            generate_csnova_styles(
                self.settings,
                BASE_STYLE_FILE,
                THEMES_STYLE_FILE,
                CSNOVA_BASE_STYLE_FILE,
                CSNOVA_THEMES_STYLE_FILE,
                CSNOVA_FORMS_STYLE_FILE,
                GUI_DIR
            )
            self._load_styles()
            self._apply_current_style()
            save_user_settings(self.settings, USER_SETTINGS_FILE)
            if hasattr(self.parent(), "on_style_changed"):
                self.parent().on_style_changed(style_key)
            log_info(f"Style changed to {style_key}.")
        except Exception as e:
            log_exception("Error changing style in PreferencesWindow", e)

    def _on_theme_changed(self, idx):
        log_subsection("_on_theme_changed")
        try:
            combo, option_keys = self.combos["theme"]
            mode_key = option_keys[idx]
            self.settings.setdefault("gui", {})["theme"] = mode_key
            generate_csnova_styles(
                self.settings,
                BASE_STYLE_FILE,
                THEMES_STYLE_FILE,
                CSNOVA_BASE_STYLE_FILE,
                CSNOVA_THEMES_STYLE_FILE,
                CSNOVA_FORMS_STYLE_FILE,
                GUI_DIR
            )
            self._load_styles()
            self._apply_current_style()
            save_user_settings(self.settings, USER_SETTINGS_FILE)
            if hasattr(self.parent(), "on_theme_changed"):
                self.parent().on_theme_changed(mode_key)
            log_info(f"Theme changed to {mode_key}.")
        except Exception as e:
            log_exception("Error changing theme in PreferencesWindow", e)

    def closeEvent(self, event):
        width = self.width()
        height = self.height()
        self.settings.setdefault("preferences_window", {})
        self.settings["preferences_window"]["width"] = width
        self.settings["preferences_window"]["height"] = height
        save_user_settings(self.settings, USER_SETTINGS_FILE)
        if hasattr(self.parent(), "on_preferences_saved"):
            self.parent().on_preferences_saved(self.settings)
        super().closeEvent(event)