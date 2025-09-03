from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class CenterPanel(QWidget):
    """
    Central panel widget for main content area.
    Applies global style from preferences.
    All labels and texts are translated via translator.py.
    All formatting and field definitions should come from form_fields.json.
    No local styles or translations are used.
    """

    def __init__(self, translator, parent=None):
        """
        Initializes the center panel with a stacked widget for dynamic content.
        """
        log_section("center_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(0, 0, 0, 0)
            self.layout.setSpacing(0)

            # Central stacked widget for switching content
            self.stacked_widget = QStackedWidget(self)
            self.layout.addWidget(self.stacked_widget)

            # Example: Add a default label (translated)
            self.default_label = QLabel(self.translator.tr("WinEditorTitle"), self)
            self.default_label.setObjectName("centerPanelDefaultLabel")
            self.stacked_widget.addWidget(self.default_label)

            self.setLayout(self.layout)
            log_info("CenterPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing CenterPanel", e)

    def update_translations(self):
        """
        Updates all labels and texts after a language change.
        """
        self.default_label.setText(self.translator.tr("WinEditorTitle"))