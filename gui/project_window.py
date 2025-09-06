from PySide6.QtWidgets import QWidget, QSplitter, QHBoxLayout
from PySide6.QtCore import Qt
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.center_panel import CenterPanel
from gui.widgets.help_panel import HelpPanel
from config.settings import load_settings, save_settings
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import CSNOVA_BASE_STYLE_FILE, CSNOVA_THEMES_STYLE_FILE
from gui.styles.python_gui_styles import apply_theme_style
import json

class ProjectWindow(QWidget):
    """
    Main project window with three panels:
    - Left: NavigationPanel
    - Center: CenterPanel (main content)
    - Right: HelpPanel
    Uses centralized translation and style system.
    """

    def __init__(self, translator, parent=None, start_window=None):
        log_section("project_window.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.settings = load_settings()
            self.start_window = start_window

            # Load centralized styles
            with open(CSNOVA_BASE_STYLE_FILE, "r", encoding="utf-8") as f:
                base_style = json.load(f)
            with open(CSNOVA_THEMES_STYLE_FILE, "r", encoding="utf-8") as f:
                theme_style = json.load(f)
            self.combined_style = {**base_style, **theme_style}

            self.setWindowTitle(self.translator.tr("ProWinTitle"))

            # Use the current start window size from settings
            try:
                win_size = self.settings.get("screen_resolution", "1920x1080")
                w, h = [int(x) for x in win_size.split("x")]
                self.resize(w, h)
            except Exception as e:
                log_exception("Error reading screen resolution from settings", e)
                self.resize(1920, 1080)

            # Create center and help panels first
            try:
                self.center_panel = CenterPanel(self.translator, parent=self, style=self.combined_style)
            except Exception as e:
                log_exception("Error initializing CenterPanel", e)
                self.center_panel = None

            try:
                self.help_panel = HelpPanel(self.translator, parent=self, style=self.combined_style)
            except Exception as e:
                log_exception("Error initializing HelpPanel", e)
                self.help_panel = None

            # Pass help_panel and center_panel to NavigationPanel
            try:
                self.navigation_panel = NavigationPanel(
                    self.translator,
                    parent=self,
                    start_window=self.start_window,
                    help_panel=self.help_panel,
                    center_panel=self.center_panel,
                    style=self.combined_style
                )
            except Exception as e:
                log_exception("Error initializing NavigationPanel", e)
                self.navigation_panel = None

            # Create splitter for three panels
            try:
                self.splitter = QSplitter(self)
                self.splitter.setOrientation(Qt.Horizontal)
                if self.navigation_panel:
                    self.splitter.addWidget(self.navigation_panel)
                if self.center_panel:
                    self.splitter.addWidget(self.center_panel)
                if self.help_panel:
                    self.splitter.addWidget(self.help_panel)

                # Fallback for splitter sizes based on window width
                default_splitter_sizes = [
                    int(w * 0.18),  # left panel ~18%
                    int(w * 0.64),  # center panel ~64%
                    int(w * 0.18)   # right panel ~18%
                ]
                splitter_sizes = self.settings.get("splitter_sizes", default_splitter_sizes)
                self.splitter.setSizes(splitter_sizes)

                # Save splitter sizes on change
                self.splitter.splitterMoved.connect(self.save_splitter_sizes)
            except Exception as e:
                log_exception("Error initializing splitter", e)
                self.splitter = None

            # Layout
            try:
                layout = QHBoxLayout(self)
                layout.setContentsMargins(0, 0, 0, 0)
                if self.splitter:
                    layout.addWidget(self.splitter)
                self.setLayout(layout)
            except Exception as e:
                log_exception("Error initializing layout in ProjectWindow", e)

            # Apply global style to main window
            try:
                apply_theme_style(self, "panel", self.combined_style)
            except Exception as e:
                log_exception("Error applying global style to ProjectWindow", e)

            log_info("ProjectWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectWindow", e)

    def save_splitter_sizes(self, pos, index):
        """
        Saves the current splitter sizes to user_settings.json when the splitter is moved.
        Robust error handling for saving splitter sizes.
        """
        try:
            if self.splitter:
                sizes = self.splitter.sizes()
                self.settings["splitter_sizes"] = sizes
                save_settings(self.settings)
                log_info(f"Splitter sizes saved: {sizes}")
        except Exception as e:
            log_exception("Error saving splitter sizes", e)

    def update_translations(self):
        """
        Updates translations for all panels after a language change.
        Robust error handling for translation update.
        """
        try:
            self.setWindowTitle(self.translator.tr("ProWinTitle"))
            if self.navigation_panel:
                self.navigation_panel.update_translations()
            if self.center_panel:
                self.center_panel.update_translations()
            if self.help_panel:
                self.help_panel.update_translations()
        except Exception as e:
            log_exception("Error updating translations in ProjectWindow", e)