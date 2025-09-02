from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from gui.styles.form_styles import load_button_style, load_active_button_style
from core.logger import log_section, log_subsection, log_info, log_exception

class NavigationPanel(QWidget):
    def __init__(self, keys, translator, parent=None, callbacks=None):
        log_section("navigation_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("NavigationPanel")
            self.translator = translator
            self.callbacks = callbacks or {}
            self.active_key = None
            self.layout = QVBoxLayout()
            self.buttons = {}

            button_style = load_button_style()
            button_style_active = load_active_button_style()

            for key in keys:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setStyleSheet(button_style)
                btn.setFixedSize(240, 70)
                btn.clicked.connect(lambda checked, k=key: self._on_nav_clicked(k))
                self.layout.addWidget(btn)
                self.buttons[key] = btn

            self.setLayout(self.layout)
            log_info("NavigationPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing NavigationPanel", e)

    def _on_nav_clicked(self, key):
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            button_style = load_button_style()
            button_style_active = load_active_button_style()
            for k, btn in self.buttons.items():
                btn.setStyleSheet(button_style)
            self.buttons[key].setStyleSheet(button_style_active)
            self.active_key = key
            if key in self.callbacks:
                self.callbacks[key]()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_exception(f"Error in navigation click handler for '{key}'", e)