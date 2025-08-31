from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout, QWidget
)
from core.translator import Translator
from config.settings import load_settings, save_settings

# Importiere die Style-Module
from gui.styles.oldschool_style import get_style as get_oldschool_style
from gui.styles.vintage_style import get_style as get_vintage_style
from gui.styles.modern_style import get_style as get_modern_style
from gui.styles.future_style import get_style as get_future_style

from core.logger import log_section, log_subsection, log_info, log_error

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
        "future": "Future"
    }

    STYLE_FUNCTIONS = {
        "oldschool": get_oldschool_style,
        "vintage": get_vintage_style,
        "modern": get_modern_style,
        "future": get_future_style
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

            self._init_ui()
            self._load_values()
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing PreferencesWindow: {str(e)}")

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

            # Style preview (Button)
            self.preview_label = QLabel("Vorschau:", self)
            self.preview_button = QPushButton("Beispiel-Button", self)
            self.preview_button.setFixedSize(180, 40)

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
            main_layout.addWidget(self.preview_label)
            main_layout.addWidget(self.preview_button)
            main_layout.addLayout(btn_layout)
            self.setLayout(main_layout)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing UI: {str(e)}")

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
            log_error(f"Error loading values: {str(e)}")

    def _on_language_changed(self):
        log_subsection("_on_language_changed")
        try:
            index = self.lang_combo.currentIndex()
            code = self.lang_combo.itemData(index)
            self.translator.set_language(code)
            self._update_ui_texts()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_error(f"Error changing language: {str(e)}")

    def _on_style_or_mode_changed(self):
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
            log_error(f"Error updating UI texts: {str(e)}")

    def _update_preview(self):
        # Zeigt den Style und Modus direkt am Beispiel-Button
        style_code = self.style_combo.itemData(self.style_combo.currentIndex())
        mode_code = self.mode_combo.itemData(self.mode_combo.currentIndex())
        style_func = self.STYLE_FUNCTIONS.get(style_code, get_modern_style)
        style_dict = style_func(mode_code)
        # Beispiel: Button-Style als CSS generieren
        btn_style = f"""
            QPushButton {{
                background-color: {style_dict['button']['background']};
                color: {style_dict['button']['foreground']};
                border: 2px solid {style_dict['border']};
                border-radius: 8px;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {style_dict['button']['hover']};
            }}
            QPushButton:pressed {{
                background-color: {style_dict['button']['active']};
            }}
        """
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
            log_error(f"Error saving settings: {str(e)}")

    def _on_cancel(self):
        log_subsection("_on_cancel")
        try:
            self.translator.set_language(self.original_language)
            if self.parent() and hasattr(self.parent(), "_on_language_changed"):
                self.parent()._on_language_changed(self.original_language)
            self.reject()
            log_info("Dialog canceled and language reverted.")
        except Exception as e:
            log_error(f"Error initializing PreferencesWindow: {str(e)}")