from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from core.lloger import log_section, log_subsection, log_info, log_error

class NavigationPanel(QWidget):
    def __init__(self, keys, translator, button_style, button_style_active, callbacks, parent=None):
        """
        keys: list of navigation keys (e.g. ["btn_project", "btn_characters", ...])
        translator: Translator instance for button texts
        button_style: style string for inactive buttons
        button_style_active: style string for active button
        callbacks: dict mapping keys to functions
        """
        log_section("navigation_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.button_style = button_style
            self.button_style_active = button_style_active
            self.callbacks = callbacks
            self.active_key = None
            self.layout = QVBoxLayout()
            self.buttons = {}

            for key in keys:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setStyleSheet(self.button_style)
                btn.setFixedSize(240, 70)
                btn.clicked.connect(lambda checked, k=key: self._on_nav_clicked(k))
                self.layout.addWidget(btn)
                self.buttons[key] = btn

            self.setLayout(self.layout)
            log_info("NavigationPanel initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing NavigationPanel: {str(e)}")

    def _on_nav_clicked(self, key):
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            # Reset all buttons to default style
            for k, btn in self.buttons.items():
                btn.setStyleSheet(self.button_style)
            # Set active button style
            self.buttons[key].setStyleSheet(self.button_style_active)
            self.active_key = key
            # Call the assigned callback
            if key in self.callbacks:
                self.callbacks[key]()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_error(f"Error in navigation click handler for '{key}': {str(e)}")