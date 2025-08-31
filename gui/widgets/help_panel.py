from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.form_styles import get_current_style
from core.logger import log_section, log_subsection, log_info, log_exception

class HelpPanel(QWidget):
    def __init__(self, parent=None):
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("HelpPanel")
            self.layout = QVBoxLayout()
            self.label = QLabel("Help and information will be displayed here.", self)
            self.label.setWordWrap(True)
            self.layout.addWidget(self.label)
            self.setLayout(self.layout)
            self.apply_style()
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing HelpPanel", e)

    def set_help_text(self, text):
        log_subsection("set_help_text")
        try:
            self.label.setText(text)
            log_info("Help text updated in HelpPanel.")
        except Exception as e:
            log_exception("Error updating help text", e)

    def apply_style(self):
        """
        Applies the current style to the help panel.
        """
        try:
            style = get_current_style()
            self.setStyleSheet(f"""
                QWidget {{
                    background-color: {style['background']};
                }}
                QLabel {{
                    color: {style['foreground']};
                    font-size: 15px;
                    padding: 8px;
                }}
            """)
            log_info("HelpPanel style applied.")
        except Exception as e:
            log_exception("Error applying style in HelpPanel", e)