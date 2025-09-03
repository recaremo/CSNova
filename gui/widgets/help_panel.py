from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class HelpPanel(QWidget):
    """
    Centralized help panel widget.
    Applies global style from preferences.
    All labels and help texts are translated via translator.py.
    No local styles or translations are used.
    """

    def __init__(self, translator, help_key="HelpHelpWindow", parent=None):
        """
        Initializes the help panel with translated title and help text.
        """
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            layout = QVBoxLayout(self)
            layout.setContentsMargins(24, 24, 24, 24)
            layout.setSpacing(16)

            # Title label (translated)
            self.title_label = QLabel(self.translator.tr("WinHelpTitle"), self)
            self.title_label.setObjectName("helpPanelTitleLabel")
            layout.addWidget(self.title_label)

            # Help text (translated)
            self.help_text = QTextEdit(self)
            self.help_text.setReadOnly(True)
            self.help_text.setObjectName("helpPanelText")
            self.help_text.setText(self.translator.help_text(help_key))
            layout.addWidget(self.help_text)

            layout.addStretch()
            self.setLayout(layout)
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing HelpPanel", e)

    def update_translations(self, help_key="HelpHelpWindow"):
        """
        Updates all labels and help text after a language change.
        """
        self.title_label.setText(self.translator.tr("WinHelpTitle"))
        self.help_text.setText(self.translator.help_text(help_key))