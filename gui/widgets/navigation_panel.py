from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from core.logger import log_section, log_subsection, log_info, log_exception
from gui.styles.python_gui_styles import apply_theme_style

class NavigationPanel(QWidget):
    """
    Centralized navigation panel widget.
    Applies global style from preferences.
    All button labels are translated via translator.py.
    """

    def __init__(self, translator, nav_keys=None, parent=None, start_window=None, help_panel=None, center_panel=None, style=None):
        """
        Initializes the navigation panel with translated buttons.
        nav_keys: List of label_keys for navigation buttons.
        start_window: Reference to the StartWindow instance for back navigation.
        help_panel: Reference to the HelpPanel instance for updating help text.
        center_panel: Reference to the CenterPanel instance for switching forms.
        style: Combined style dict from csNova_base_style.json and csNova_themes_style.json.
        """
        log_section("navigation_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.start_window = start_window
            self.project_window = parent  # Save reference to the actual ProjectWindow
            self.help_panel = help_panel
            self.center_panel = center_panel
            self.style = style

            apply_theme_style(self, "panel", self.style)

            layout = QVBoxLayout(self)
            layout.setContentsMargins(12, 12, 12, 12)
            layout.setSpacing(14)  # slightly larger spacing

            self.buttons = {}
            if nav_keys is None:
                # Use keys from translations.json for project navigation
                nav_keys = [
                    "botn_fo_01",  # Project
                    "botn_fo_05",  # Main Characters
                    "botn_fo_08",  # Locations
                    "botn_fo_09",  # Objects
                    "botn_fo_10"   # Back
                ]

            # Add all buttons except the last one (Back) at the top
            for key in nav_keys[:-1]:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setObjectName(key)
                self.buttons[key] = btn
                layout.addWidget(btn)
                # Connect navigation buttons to update help and center panel
                btn.clicked.connect(lambda checked, k=key: self.handle_navigation_click(k))
                apply_theme_style(btn, "button", self.style)

            # Add a stretch to push the last button to the bottom
            layout.addStretch()

            # Add the last button (Back) at the bottom
            back_key = nav_keys[-1]
            back_btn = QPushButton(self.translator.tr(back_key), self)
            back_btn.setObjectName(back_key)
            self.buttons[back_key] = back_btn
            layout.addWidget(back_btn)
            apply_theme_style(back_btn, "button", self.style)

            # Connect back button to close project window and show start window
            back_btn.clicked.connect(self.go_back_to_start)

            self.setLayout(layout)
            log_info("NavigationPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing NavigationPanel", e)

    def go_back_to_start(self):
        """
        Closes the project window and shows the start window.
        """
        try:
            if self.start_window is not None and self.project_window is not None:
                self.project_window.close()
                self.start_window.show()
                log_info("Returned to StartWindow from ProjectWindow.")
        except Exception as e:
            log_exception("Error returning to StartWindow", e)

    def handle_navigation_click(self, nav_key):
        """
        Handles navigation button clicks: updates help panel and center panel.
        """
        self.update_help_panel(nav_key)
        self.update_center_panel(nav_key)

    def update_help_panel(self, nav_key):
        """
        Updates the help panel based on the navigation key.
        """
        if self.help_panel is not None:
            nav_to_topic = {
                "botn_fo_01": "projects",
                "botn_fo_05": "characters",
                "botn_fo_08": "locations",
                "botn_fo_09": "objects"
            }
            topic = nav_to_topic.get(nav_key)
            if topic:
                self.help_panel.update_translations(topic)

    def update_center_panel(self, nav_key):
        """
        Updates the center panel based on the navigation key.
        """
        if self.center_panel is not None:
            nav_to_form = {
                "botn_fo_01": "projects",
                "botn_fo_05": "characters",
                "botn_fo_08": "locations",
                "botn_fo_09": "objects"
            }
            form_type = nav_to_form.get(nav_key)
            if form_type:
                self.center_panel.show_form(form_type)

    def update_translations(self):
        """
        Updates all button texts after a language change.
        """
        for key, btn in self.buttons.items():
            btn.setText(self.translator.tr(key))