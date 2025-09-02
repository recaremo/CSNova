from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.form_styles import load_global_stylesheet
from core.logger import log_section, log_subsection, log_info, log_exception

class HelpPanel(QWidget):
    def __init__(self, help_text="", parent=None):
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("HelpPanel")
            self.setStyleSheet(load_global_stylesheet())
            self.layout = QVBoxLayout()
            # Sicherstellen, dass help_text ein String ist
            self.help_label = QLabel(str(help_text), self)
            self.help_label.setWordWrap(True)
            self.layout.addWidget(self.help_label)
            self.setLayout(self.layout)
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing HelpPanel", e)

    def set_help_text(self, text):
        log_subsection("set_help_text")
        try:
            # Sicherstellen, dass text ein String ist
            self.help_label.setText(str(text))
            log_info("HelpPanel help text updated.")
        except Exception as e:
            log_exception("Error updating help text in HelpPanel", e)