from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class NavigationPanel(QWidget):
    """
    Centralized navigation panel widget.
    Applies global style from preferences.
    All button labels are translated via translator.py.
    No local styles or translations are used.
    """

    def __init__(self, translator, nav_keys=None, parent=None):
        """
        Initializes the navigation panel with translated buttons.
        nav_keys: List of label_keys for navigation buttons.
        """
        log_section("navigation_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            layout = QVBoxLayout(self)
            layout.setContentsMargins(12, 12, 12, 12)
            layout.setSpacing(10)

            self.buttons = {}
            if nav_keys is None:
                # Default navigation keys if not provided
                nav_keys = [
                    "ProBtnProject", "ProBtnCharacters", "ProBtnStorylines",
                    "ProBtnChapters", "ProBtnScenes", "ProBtnObjects",
                    "ProBtnLocations", "ProBtnExit"
                ]

            for key in nav_keys:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setObjectName(key)
                self.buttons[key] = btn
                layout.addWidget(btn)

            layout.addStretch()
            self.setLayout(layout)
            log_info("NavigationPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing NavigationPanel", e)

    def update_translations(self):
        """
        Updates all button texts after a language change.
        """
        for key, btn in self.buttons.items():
            btn.setText(self.translator.tr(key))