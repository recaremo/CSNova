from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.widgets.form_toolbar import FormToolbar
from core.logger import log_section, log_subsection, log_info, log_exception

class ChaptersForm(QWidget):
    def __init__(self, translator, parent=None):
        log_section("form_chapters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            layout = QVBoxLayout(self)

            # Toolbar mit "chapter"-Prefix
            self.toolbar = FormToolbar(self.translator, "chapter", self)
            layout.addWidget(self.toolbar)

            # Beispiel für ein Label mit standard_key
            self.title_label = QLabel(self.translator.tr("chapter_title"), self)
            layout.addWidget(self.title_label)

            # Weitere Felder/Labels nach Bedarf, immer mit standard_key
            self.number_label = QLabel(self.translator.tr("chapter_number"), self)
            layout.addWidget(self.number_label)

            self.summary_label = QLabel(self.translator.tr("chapter_summary"), self)
            layout.addWidget(self.summary_label)

            self.setLayout(layout)
            log_info("ChaptersForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ChaptersForm", e)