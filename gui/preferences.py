from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout
)
from core.translations import LANGUAGES, TRANSLATIONS
from config.settings import load_settings, save_settings

class PreferencesWindow(QDialog):
    # Größe des Dialogs
    DEFAULT_WIDTH  = 400
    DEFAULT_HEIGHT = 200

    # Anzeige-Namen in der ComboBox (Deutsch-Namen)
    LANGUAGE_NAMES = {
        "de": "Deutsch",
        "en": "Englisch",
        "fr": "Französisch",
        "es": "Spanisch"
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.translator = parent.translator
        self.settings   = load_settings()

        # Dialog einstellen
        self.setWindowTitle(self.translator.tr("menu_settings"))
        self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)

        # UI aufbauen
        self._init_ui()
        self._load_values()

    def _init_ui(self):
        # Label „Sprache“
        self.lang_label = QLabel(self.translator.tr("menu_language"), self)

        # ComboBox mit German-Namen, userData = Sprachcode
        self.lang_combo = QComboBox(self)
        for code in LANGUAGES:
            name = self.LANGUAGE_NAMES.get(code, code)
            self.lang_combo.addItem(name, userData=code)

        # Bei Änderung sofort umschalten
        self.lang_combo.currentIndexChanged.connect(self._on_language_changed)

        # OK und Abbrechen
        self.ok_button     = QPushButton(
            self.translator.tr("action_save"), self
        )
        self.cancel_button = QPushButton(
            self.translator.tr("action_cancel"), self
        )

        self.ok_button.clicked.connect(self._on_ok)
        self.cancel_button.clicked.connect(self.reject)

        # Button-Leiste
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.ok_button)
        btn_layout.addWidget(self.cancel_button)

        # Gesamtlayout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.lang_label)
        main_layout.addWidget(self.lang_combo)
        main_layout.addLayout(btn_layout)

    def _load_values(self):
        # Aktuelle Sprache aus Settings vorwählen
        lang = self.settings.get("language", LANGUAGES[0])
        idx  = LANGUAGES.index(lang) if lang in LANGUAGES else 0
        self.lang_combo.setCurrentIndex(idx)

    def _on_language_changed(self, index):
        # Translator umschalten
        code = self.lang_combo.itemData(index)
        self.translator.set_language(code)
        # Texte im Dialog updaten
        self._update_ui_texts()

    def _update_ui_texts(self):
        # Fenster-Titel
        self.setWindowTitle(self.translator.tr("menu_settings"))
        # Label und Buttons
        self.lang_label.setText(self.translator.tr("menu_language"))
        self.ok_button.setText(self.translator.tr("action_save"))
        self.cancel_button.setText(self.translator.tr("action_cancel"))

    def _on_ok(self):
        # speichern
        code = self.lang_combo.currentData()
        self.settings["language"] = code
        save_settings(self.settings)
        # auch im Parent anwenden
        if self.parent() and hasattr(self.parent(), "_on_language_changed"):
            self.parent()._on_language_changed(code)
        self.accept()
