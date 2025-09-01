from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout, QWidget
)
from core.translator import Translator
from config.settings import load_settings, save_settings
from gui.styles.themes_style import THEMES, get_theme
from gui.styles.form_styles import load_button_style
from gui.styles.form_styles import load_global_stylesheet
from core.logger import log_section, log_subsection, log_info, log_exception

class PreferencesWindow(QDialog):
    DEFAULT_WIDTH  = 400
    DEFAULT_HEIGHT = 260

    LANGUAGE_NAMES = {
        "de": "Deutsch",
        "en": "English",
        "fr": "Français",
        "es": "Español"
    }

    STYLE_NAMES = {
        "oldschool": "Old-School",
        "vintage": "Vintage",
        "modern": "Modern",
        "future": "Future",
        "minimal": "Minimal"
}

    MODE_NAMES = {
        "light": "Light",
        "middle": "Middle",
        "dark": "Dark"
    }

    def __init__(self, parent=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = parent.translator
            self.settings   = load_settings()
            self.original_language = self.translator.lang

            self.setWindowTitle(self.translator.tr("menu_settings"))
            self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
            self.setStyleSheet(load_global_stylesheet())  # Apply global stylesheet
            self._init_ui()
            self._load_values()
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing PreferencesWindow", e)

    def _init_ui(self):
        log_subsection("_init_ui")
        try:
            # Language selection
            self.lang_label = QLabel(self.translator.tr("menu_language"), self)
            self.lang_combo = QComboBox(self)
            for code in self.LANGUAGE_NAMES:
                name = self.LANGUAGE_NAMES[code]
                self.lang_combo.addItem(name, userData=code)
            self.lang_combo.currentIndexChanged.connect(self._on_language_changed)

            # Style selection
            self.style_label = QLabel("Style", self)
            self.style_combo = QComboBox(self)
            for code in self.STYLE_NAMES:
                self.style_combo.addItem(self.STYLE_NAMES[code], userData=code)
            self.style_combo.currentIndexChanged.connect(self._on_style_or_mode_changed)

            # Mode selection
            self.mode_label = QLabel("Modus", self)
            self.mode_combo = QComboBox(self)
            for code in self.MODE_NAMES:
                self.mode_combo.addItem(self.MODE_NAMES[code], userData=code)
            self.mode_combo.currentIndexChanged.connect(self._on_style_or_mode_changed)

            # Buttons
            self.ok_button     = QPushButton(self)
            self.cancel_button = QPushButton(self)
            self.ok_button.clicked.connect(self._on_ok)
            self.cancel_button.clicked.connect(self._on_cancel)

            btn_layout = QHBoxLayout()
            btn_layout.addStretch()
            btn_layout.addWidget(self.ok_button)
            btn_layout.addWidget(self.cancel_button)

            main_layout = QVBoxLayout(self)
            main_layout.addWidget(self.lang_label)
            main_layout.addWidget(self.lang_combo)
            main_layout.addWidget(self.style_label)
            main_layout.addWidget(self.style_combo)
            main_layout.addWidget(self.mode_label)
            main_layout.addWidget(self.mode_combo)
            main_layout.addLayout(btn_layout)
            self.setLayout(main_layout)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI", e)

    def _load_values(self):
        log_subsection("_load_values")
        try:
            # Language
            lang = self.settings.get("language", "en")
            idx  = list(self.LANGUAGE_NAMES.keys()).index(lang) if lang in self.LANGUAGE_NAMES else 0
            self.lang_combo.setCurrentIndex(idx)
            # Style
            style = self.settings.get("style", "modern")
            idx = list(self.STYLE_NAMES.keys()).index(style) if style in self.STYLE_NAMES else 2  # modern als Default
            self.style_combo.setCurrentIndex(idx)
            # Mode
            mode = self.settings.get("mode", "light")
            idx = list(self.MODE_NAMES.keys()).index(mode) if mode in self.MODE_NAMES else 0
            self.mode_combo.setCurrentIndex(idx)
            self._update_ui_texts()
            self._update_preview()
            log_info("Values loaded and UI texts updated.")
        except Exception as e:
            log_exception("Error loading values", e)

    def _on_language_changed(self):
        log_subsection("_on_language_changed")
        try:
            index = self.lang_combo.currentIndex()
            code = self.lang_combo.itemData(index)
            self.translator.set_language(code)
            self._update_ui_texts()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language", e)

    def _on_style_or_mode_changed(self):
        self.setStyleSheet(load_global_stylesheet())  # Apply global stylesheet for the whole window
        self._update_preview()

    def _update_ui_texts(self):
        log_subsection("_update_ui_texts")
        try:
            self.setWindowTitle(self.translator.tr("menu_settings"))
            self.lang_label.setText(self.translator.tr("menu_language"))
            self.style_label.setText("Style")
            self.mode_label.setText("Modus")
            self.preview_label.setText("Vorschau:")
            self.ok_button.setText(self.translator.tr("action_save"))
            self.cancel_button.setText(self.translator.tr("action_cancel"))
            log_info("UI texts updated.")
        except Exception as e:
            log_exception("Error updating UI texts", e)

    def _update_preview(self):
        style_code = self.style_combo.itemData(self.style_combo.currentIndex())
        mode_code = self.mode_combo.itemData(self.mode_combo.currentIndex())
        style_dict = get_theme(style_code, mode_code)
        btn_style = load_button_style(font_size=16)
        self.preview_button.setStyleSheet(btn_style)

    def _on_ok(self):
        log_subsection("_on_ok")
        try:
            self.settings["language"] = self.lang_combo.itemData(self.lang_combo.currentIndex())
            self.settings["style"]    = self.style_combo.itemData(self.style_combo.currentIndex())
            self.settings["mode"]     = self.mode_combo.itemData(self.mode_combo.currentIndex())
            save_settings(self.settings)
            if self.parent() and hasattr(self.parent(), "_on_language_changed"):
                self.parent()._on_language_changed(self.settings["language"])
            self.accept()
            log_info("Settings saved and dialog accepted.")
        except Exception as e:
            log_exception("Error saving settings", e)

    def _on_cancel(self):
        log_subsection("_on_cancel")
        try:
            self.translator.set_language(self.original_language)
            if self.parent() and hasattr(self.parent(), "_on_language_changed"):
                self.parent()._on_language_changed(self.original_language)
            self.reject()
            log_info("Dialog canceled and language reverted.")
        except Exception as e:
            log_exception("Error canceling PreferencesWindow", e)