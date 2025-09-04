from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QApplication
)
from core.translator import Translator
from config.settings import load_settings, save_settings
from core.logger import log_section, log_subsection, log_info, log_exception
import json

from gui.styles.form_styles import load_global_stylesheet

class PreferencesWindow(QDialog):
    """
    PreferencesWindow: Dialog for user settings such as language, style and theme.
    All options and translations are loaded centrally from form_fields.json and translations.json.
    Styles and themes are applied immediately in the preferences window and globally.
    Robust error handling is implemented for file and UI operations.
    """

    def __init__(self, parent=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = parent.translator if parent and hasattr(parent, "translator") else Translator()
            self.setWindowTitle(self.translator.tr("PrefWinTitle"))
            self.setMinimumSize(500, 320)
            self.settings = load_settings()
            self.original_settings = self.settings.copy()  # Save original settings for cancel
            self._load_fields()
            self._init_ui()
            self._apply_current_style(global_apply=True)
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing PreferencesWindow", e)

    def _load_fields(self):
        """
        Loads preference field definitions from form_fields.json.
        Robust error handling for file operations.
        """
        try:
            with open("/home/frank/Dokumente/CSNova/core/config/form_fields.json", "r", encoding="utf-8") as f:
                self.form_fields = json.load(f).get("preferences", [])
        except FileNotFoundError as fnf_error:
            log_exception("form_fields.json not found in PreferencesWindow.", fnf_error)
            self.form_fields = []
        except json.JSONDecodeError as json_error:
            log_exception("JSON decode error in form_fields.json for PreferencesWindow.", json_error)
            self.form_fields = []
        except Exception as e:
            log_exception("Unexpected error loading form_fields.json in PreferencesWindow.", e)
            self.form_fields = []

    def _init_ui(self):
        """
        Initializes all UI elements for the preferences dialog.
        All options are loaded from central sources. Layout is compact and buttons are at the bottom.
        Robust error handling for UI initialization.
        """
        log_subsection("_init_ui")
        try:
            main_layout = QVBoxLayout(self)
            main_layout.setSpacing(8)
            main_layout.setContentsMargins(24, 18, 24, 18)

            self.combos = {}
            self.labels = {}

            # Dynamically create fields from form_fields.json
            for field in self.form_fields:
                label = QLabel(self.translator.tr(field.get("label_key", "")), self)
                combo = QComboBox(self)
                option_labels = []
                option_keys = []
                for opt in field.get("options", []):
                    option_labels.append(self.translator.tr(opt.get("label_key", "")))
                    option_keys.append(opt.get("key", ""))
                combo.addItems(option_labels)
                # Set current value from settings
                current_value = self.settings.get(field.get("datafield_name", "").replace("preference_", ""), option_keys[0] if option_keys else "")
                try:
                    idx = option_keys.index(current_value)
                except ValueError:
                    idx = 0
                combo.setCurrentIndex(idx)
                main_layout.addWidget(label)
                main_layout.addWidget(combo)
                self.combos[field.get("name", "")] = (combo, option_keys)
                self.labels[field.get("name", "")] = label

                # Connect style and theme changes to handlers
                if field.get("name", "") == "style":
                    combo.currentIndexChanged.connect(self._on_style_changed)
                if field.get("name", "") == "theme":
                    combo.currentIndexChanged.connect(self._on_theme_changed)

            main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

            # Action buttons at the bottom
            btn_layout = QHBoxLayout()
            btn_layout.setSpacing(15)
            btn_layout.setContentsMargins(0, 0, 0, 0)
            self.save_btn = QPushButton(self.translator.tr("PreferenceActionSave"), self)
            self.cancel_btn = QPushButton(self.translator.tr("PreferenceActionCancel"), self)
            btn_layout.addStretch(1)
            btn_layout.addWidget(self.save_btn)
            btn_layout.addWidget(self.cancel_btn)
            btn_layout.addStretch(1)
            main_layout.addLayout(btn_layout)

            self.setLayout(main_layout)

            # Connect signals to slots for user interaction
            self.save_btn.clicked.connect(self._on_save)
            self.cancel_btn.clicked.connect(self._on_cancel)
            # Language change updates translations
            if "language" in self.combos:
                self.combos["language"][0].currentIndexChanged.connect(self._on_language_changed)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI in PreferencesWindow", e)

    def _apply_current_style(self, global_apply=False):
        """
        Applies the currently selected style and theme to the preferences window.
        If global_apply is True, applies the style globally to the application.
        Robust error handling for stylesheet application.
        """
        try:
            style = self.settings.get("style", "modern")
            mode = self.settings.get("mode", "light")
            stylesheet = load_global_stylesheet(style, mode)
            self.setStyleSheet(stylesheet)
            if global_apply:
                QApplication.instance().setStyleSheet(stylesheet)
        except Exception as e:
            log_exception("Error applying stylesheet in PreferencesWindow", e)

    def update_translations(self):
        """
        Updates all UI texts after a language change.
        Also updates translated items in all comboboxes.
        Robust error handling for translation updates.
        """
        try:
            self.setWindowTitle(self.translator.tr("PrefWinTitle"))
            for field in self.form_fields:
                name = field.get("name", "")
                self.labels[name].setText(self.translator.tr(field.get("label_key", "")))
                combo, option_keys = self.combos[name]
                combo.blockSignals(True)
                combo.clear()
                for opt in field.get("options", []):
                    combo.addItem(self.translator.tr(opt.get("label_key", "")))
                # Set current value from settings
                current_value = self.settings.get(field.get("datafield_name", "").replace("preference_", ""), option_keys[0] if option_keys else "")
                try:
                    idx = option_keys.index(current_value)
                except ValueError:
                    idx = 0
                combo.setCurrentIndex(idx)
                combo.blockSignals(False)
            self.save_btn.setText(self.translator.tr("PreferenceActionSave"))
            self.cancel_btn.setText(self.translator.tr("PreferenceActionCancel"))
            self._apply_current_style(global_apply=True)
        except Exception as e:
            log_exception("Error updating translations in PreferencesWindow", e)

    def _on_save(self):
        """
        Saves the selected settings and closes the dialog.
        Notifies parent window to update translations if possible.
        Robust error handling for saving settings.
        """
        log_subsection("_on_save")
        try:
            for field in self.form_fields:
                name = field.get("name", "")
                combo, option_keys = self.combos[name]
                self.settings[field.get("datafield_name", "").replace("preference_", "")] = option_keys[combo.currentIndex()]
            save_settings(self.settings)
            # Notify parent to update translations if method exists
            if hasattr(self.parent(), "update_translations"):
                self.parent().update_translations()
            self._apply_current_style(global_apply=True)
            self.accept()
            log_info("Settings saved and dialog accepted.")
        except Exception as e:
            log_exception("Error saving settings in PreferencesWindow", e)

    def _on_cancel(self):
        """
        Cancels the dialog and reverts any unsaved changes.
        Restores original settings and translations.
        Robust error handling for cancel operation.
        """
        log_subsection("_on_cancel")
        try:
            self.settings = self.original_settings.copy()
            # Restore original language in translator
            original_lang = self.original_settings.get("language", "de")
            self.translator.set_language(original_lang)
            self.update_translations()
            self._apply_current_style(global_apply=True)
            self.reject()
            log_info("Dialog canceled and settings reverted.")
        except Exception as e:
            log_exception("Error canceling PreferencesWindow", e)

    def _on_language_changed(self, idx):
        """
        Handles language change event and updates translations.
        Sets the language immediately in settings.
        Robust error handling for language change.
        """
        log_subsection("_on_language_changed")
        try:
            combo, option_keys = self.combos["language"]
            lang_code = option_keys[idx]
            self.translator.set_language(lang_code)
            self.settings["language"] = lang_code  # Set immediately!
            self.update_translations()
            log_info(f"Language changed to {lang_code}.")
        except Exception as e:
            log_exception("Error changing language in PreferencesWindow", e)

    def _on_style_changed(self, idx):
        """
        Applies the selected style immediately to the preferences window and globally.
        Robust error handling for style change.
        """
        log_subsection("_on_style_changed")
        try:
            combo, option_keys = self.combos["style"]
            style_key = option_keys[idx].replace("style_", "")
            self.settings["style"] = style_key
            mode = self.settings.get("mode", "light")
            self._apply_current_style(global_apply=True)
            log_info(f"Style changed to {style_key}.")
        except Exception as e:
            log_exception("Error changing style in PreferencesWindow", e)

    def _on_theme_changed(self, idx):
        """
        Applies the selected theme immediately to the preferences window and globally.
        Robust error handling for theme change.
        """
        log_subsection("_on_theme_changed")
        try:
            combo, option_keys = self.combos["theme"]
            mode_key = option_keys[idx].replace("theme_", "")
            self.settings["mode"] = mode_key
            style = self.settings.get("style", "modern")
            self._apply_current_style(global_apply=True)
            log_info(f"Theme changed to {mode_key}.")
        except Exception as e:
            log_exception("Error changing theme in PreferencesWindow", e)