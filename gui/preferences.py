from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout
)
from core.translator import Translator
from config.settings import load_settings, save_settings
from core.logger import log_section, log_subsection, log_info, log_exception

class PreferencesWindow(QDialog):
    def __init__(self, parent=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = parent.translator if parent and hasattr(parent, "translator") else Translator()
            self.setWindowTitle(self.translator.tr("preference_title"))
            self.settings = load_settings()
            self._init_ui()
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing PreferencesWindow", e)

    def _init_ui(self):
        log_subsection("_init_ui")
        try:
            layout = QVBoxLayout(self)

            # Sprache
            lang_label = QLabel(self.translator.tr("preference_language"), self)
            self.lang_combo = QComboBox(self)
            self.lang_combo.addItems(["de", "en", "es"])
            self.lang_combo.setCurrentText(self.settings.get("language", "de"))
            layout.addWidget(lang_label)
            layout.addWidget(self.lang_combo)

            # Theme
            theme_label = QLabel(self.translator.tr("preference_theme"), self)
            self.theme_combo = QComboBox(self)
            self.theme_combo.addItems(["modern", "vintage"])
            self.theme_combo.setCurrentText(self.settings.get("style", "modern"))
            layout.addWidget(theme_label)
            layout.addWidget(self.theme_combo)

            # Buttons
            btn_layout = QHBoxLayout()
            self.save_btn = QPushButton(self.translator.tr("preference_save"), self)
            self.cancel_btn = QPushButton(self.translator.tr("preference_cancel"), self)
            btn_layout.addWidget(self.save_btn)
            btn_layout.addWidget(self.cancel_btn)
            layout.addLayout(btn_layout)

            self.setLayout(layout)

            self.save_btn.clicked.connect(self._on_save)
            self.cancel_btn.clicked.connect(self._on_cancel)
            self.lang_combo.currentTextChanged.connect(self._on_language_changed)
            self.theme_combo.currentTextChanged.connect(self._on_theme_changed)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI in PreferencesWindow", e)

    def _on_save(self):
        log_subsection("_on_save")
        try:
            self.settings["language"] = self.lang_combo.currentText()
            self.settings["style"] = self.theme_combo.currentText()
            save_settings(self.settings)
            self.accept()
            log_info("Settings saved and dialog accepted.")
        except Exception as e:
            log_exception("Error saving settings in PreferencesWindow", e)

    def _on_cancel(self):
        log_subsection("_on_cancel")
        try:
            self.reject()
            log_info("Dialog canceled and language reverted.")
        except Exception as e:
            log_exception("Error canceling PreferencesWindow", e)

    def _on_language_changed(self, code):
        log_subsection("_on_language_changed")
        try:
            self.translator.set_language(code)
            self.setWindowTitle(self.translator.tr("preference_title"))
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language in PreferencesWindow", e)

    def _on_theme_changed(self, theme):
        log_subsection("_on_theme_changed")
        try:
            # Theme-Änderung kann hier verarbeitet werden, falls nötig
            log_info(f"Theme changed to {theme}.")
        except Exception as e:
            log_exception("Error changing theme in PreferencesWindow", e)