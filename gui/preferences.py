from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout
)
from core.translations.translations import LANGUAGES, TRANSLATIONS
from config.settings import load_settings, save_settings

class PreferencesWindow(QDialog):
    DEFAULT_WIDTH  = 400
    DEFAULT_HEIGHT = 200

    LANGUAGE_NAMES = {
        "de": "Deutsch",
        "en": "English",
        "fr": "Français",
        "es": "Español"
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.translator = parent.translator
        self.settings   = load_settings()
        self.original_language = self.translator.lang

        self.setWindowTitle(self.translator.tr("menu_settings"))
        self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)

        self._init_ui()
        self._load_values()

    def _init_ui(self):
        self.lang_label = QLabel(self.translator.tr("menu_language"), self)

        self.lang_combo = QComboBox(self)
        for code in LANGUAGES:
            name = self.LANGUAGE_NAMES.get(code, code)
            self.lang_combo.addItem(name, userData=code)

        self.lang_combo.currentIndexChanged.connect(self._on_language_changed)

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
        main_layout.addLayout(btn_layout)

    def _load_values(self):
        lang = self.settings.get("language", LANGUAGES[0])
        idx  = LANGUAGES.index(lang) if lang in LANGUAGES else 0
        self.lang_combo.setCurrentIndex(idx)
        self._update_ui_texts()

    def _on_language_changed(self):
        index = self.lang_combo.currentIndex()
        code = self.lang_combo.itemData(index)
        self.translator.set_language(code)
        self._update_ui_texts()

    def _update_ui_texts(self):
        self.setWindowTitle(self.translator.tr("menu_settings"))
        self.lang_label.setText(self.translator.tr("menu_language"))
        self.ok_button.setText(self.translator.tr("action_save"))
        self.cancel_button.setText(self.translator.tr("action_cancel"))

    def _on_ok(self):
        index = self.lang_combo.currentIndex()
        code = self.lang_combo.itemData(index)
        self.settings["language"] = code
        save_settings(self.settings)
        if self.parent() and hasattr(self.parent(), "_on_language_changed"):
            self.parent()._on_language_changed(code)
        self.accept()

    def _on_cancel(self):
        self.translator.set_language(self.original_language)
        if self.parent() and hasattr(self.parent(), "_on_language_changed"):
            self.parent()._on_language_changed(self.original_language)
        self.reject()