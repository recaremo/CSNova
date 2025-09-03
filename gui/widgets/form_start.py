from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class FormStart(QWidget):
    """
    Placeholder widget for the start screen after StartBtnNewProject is pressed.
    Applies global style from preferences.
    Displays only a translated label as placeholder.
    No local styles or translations are used.
    """

    def __init__(self, translator, parent=None):
        """
        Initializes the start form with a translated placeholder label.
        """
        log_section("form_start.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            layout = QVBoxLayout(self)
            layout.setContentsMargins(40, 40, 40, 40)
            layout.setSpacing(20)

            # Placeholder label (translated)
            self.placeholder_label = QLabel(self.translator.tr("WinStartTitle"), self)
            self.placeholder_label.setObjectName("startPlaceholderLabel")
            layout.addWidget(self.placeholder_label)
            layout.addStretch()

            self.setLayout(layout)
            log_info("FormStart initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormStart", e)

    def update_translations(self):
        """
        Updates the placeholder label after a language change.
        """
        self.placeholder_label.setText(self.translator.tr("WinStartTitle"))