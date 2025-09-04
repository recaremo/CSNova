from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class HelpPanel(QWidget):
    """
    Centralized help panel widget.
    Applies global style from preferences.
    All labels and help texts are translated via translator.py.
    """

    def __init__(self, translator, help_key="help_pr_01", parent=None):
        """
        Initializes the help panel with translated title and help text.
        help_key: Key for the help text in translations.json (e.g. 'help_pr_01').
        """
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.help_key = help_key
            self.setStyleSheet(load_form_style())

            layout = QVBoxLayout(self)
            layout.setContentsMargins(24, 24, 24, 24)
            layout.setSpacing(16)

            # Title label (translated, now dynamic)
            self.title_label = QLabel(self.translator.tr("help_wi_01"), self)
            self.title_label.setObjectName("helpPanelTitleLabel")
            layout.addWidget(self.title_label)

            # Help text (translated)
            self.help_text = QTextEdit(self)
            self.help_text.setReadOnly(True)
            self.help_text.setObjectName("helpPanelText")
            self.help_text.setText(self.translator.tr(self.help_key))
            layout.addWidget(self.help_text)

            layout.addStretch()
            self.setLayout(layout)
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing HelpPanel", e)

    def update_translations(self, help_key=None):
        """
        Updates all labels and help text after a language change or help topic change.
        If help_key is given, updates to the new help topic.
        Supports shortcut keys for common help topics and dynamic titles.
        """
        # Map shortcut topic names to translation keys and titles
        topic_map = {
            "projects": ("help_pr_02", "help_wi_02"),
            "characters": ("help_pr_03", "help_wi_03"),
            "objects": ("help_pr_04", "help_wi_04"),
            "locations": ("help_pr_05", "help_wi_05")
        }
        if help_key is not None:
            # Allow both direct translation keys and shortcut topic names
            if help_key in topic_map:
                self.help_key, title_key = topic_map[help_key]
                self.title_label.setText(self.translator.tr(title_key))
            else:
                self.help_key = help_key
                self.title_label.setText(self.translator.tr("help_wi_01"))
        else:
            # Default title
            self.title_label.setText(self.translator.tr("help_wi_01"))
        self.help_text.setText(self.translator.tr(self.help_key))