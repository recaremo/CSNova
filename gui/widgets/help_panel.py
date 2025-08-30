from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from core.logger import log_section, log_subsection, log_info, log_error

class HelpPanel(QWidget):
    def __init__(self, parent=None):
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.layout = QVBoxLayout()
            self.label = QLabel("Help and information will be displayed here.", self)
            self.label.setWordWrap(True)
            self.layout.addWidget(self.label)
            self.setLayout(self.layout)
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing HelpPanel: {str(e)}")

    def set_help_text(self, text):
        log_subsection("set_help_text")
        try:
            self.label.setText(text)
            log_info("Help text updated in HelpPanel.")
        except Exception as e:
            log_error(f"Error updating help text: {str(e)}")