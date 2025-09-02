from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.widgets.form_toolbar import FormToolbar
from core.logger import log_section, log_subsection, log_info, log_exception

class CharactersForm(QWidget):
    def __init__(self, translator, parent=None):
        log_section("form_characters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            layout = QVBoxLayout(self)

            # Toolbar mit "character"-Prefix
            self.toolbar = FormToolbar(self.translator, "character", self)
            layout.addWidget(self.toolbar)

            # Beispiel für ein Label mit standard_key
            self.title_label = QLabel(self.translator.tr("character_title"), self)
            layout.addWidget(self.title_label)

            # Weitere Felder/Labels nach Bedarf, immer mit standard_key
            self.name_label = QLabel(self.translator.tr("character_name"), self)
            layout.addWidget(self.name_label)

            self.setLayout(layout)
            log_info("CharactersForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing CharactersForm", e)