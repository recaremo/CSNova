from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from gui.styles.form_styles import load_button_style
from core.logger import log_section, log_subsection, log_info, log_exception

class FormToolbar(QWidget):
    """
    Centralized toolbar widget for forms.
    Applies global button styles from preferences.
    All button labels are translated via translator.py.
    No local styles or translations are used.
    """

    def __init__(self, translator, form_prefix, parent=None):
        """
        Initializes the toolbar with translated buttons for form actions.
        """
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_button_style())

            layout = QHBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(10)

            # Define button keys for common actions
            self.button_keys = [
                "BtnNew", "BtnSave", "BtnDelete", "BtnPreview", "BtnNext"
            ]
            self.buttons = {}

            for key in self.button_keys:
                label_key = f"{form_prefix}{key}"
                btn = QPushButton(self.translator.tr(label_key), self)
                btn.setObjectName(label_key)
                self.buttons[key] = btn
                layout.addWidget(btn)

            layout.addStretch()
            self.setLayout(layout)
            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormToolbar", e)

    def update_translations(self):
        """
        Updates all button texts after a language change.
        """
        for key, btn in self.buttons.items():
            label_key = btn.objectName()
            btn.setText(self.translator.tr(label_key))