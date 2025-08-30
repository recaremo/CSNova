from PySide6.QtWidgets import QWidget, QVBoxLayout
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class StartForm(QWidget):
    """
    Completely empty form widget for the start window.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_start.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Empty layout
            layout = QVBoxLayout()
            self.setLayout(layout)

            log_info("StartForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing StartForm: {str(e)}")