from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSplitter, QHBoxLayout

from gui.styles.form_styles import load_button_style, load_active_button_style
from core.translator import Translator
from config.settings import load_settings, save_settings
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.help_panel import HelpPanel

from gui.widgets.form_projects import FormProjects
from gui.widgets.form_characters import FormCharacters
from gui.widgets.form_storylines import FormStorylines
from gui.widgets.form_chapters import FormChapters
from gui.widgets.form_scenes import FormScenes
from gui.widgets.form_objects import FormObjects
from gui.widgets.form_locations import FormLocations
from gui.widgets.form_start import FormStart

from core.logger import log_section, log_subsection, log_info, log_exception

class ProjectWindow(QWidget):
    BUTTON_WIDTH = 240
    BUTTON_HEIGHT = 70

    def __init__(self, translator=None, parent=None, start_window=None):
        """
        Main project window for csNova.
        Initializes navigation, help, and form panels.
        Applies global styles and translations.
        """
        log_section("project_window.py")
        log_subsection("__init__")
        try:
            self.translator = translator or Translator(lang="en")
            super().__init__(parent)
            self.resize(1600, 900)
            self.setWindowTitle(self.translator.tr("ProWinTitle"))
            self.settings = load_settings()
            self.button_style = load_button_style(18)
            self.button_style_active = load_active_button_style(18)
            self.active_nav_key = None
            self.start_window = start_window

            self.splitter = QSplitter(Qt.Horizontal)
            self.splitter.setObjectName("MainSplitter")

            self._set_background()
            self._init_ui()
            log_info("ProjectWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectWindow", e)

    def _set_background(self):
        """
        Sets the background color for the main window.
        """
        log_subsection("_set_background")
        try:
            palette = self.palette()
            palette.setColor(QPalette.Window, QColor("#f0f0f0"))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
            log_info("Background set successfully.")
        except Exception as e:
            log_exception("Error setting background", e)

    def _init_ui(self):
        """
        Initializes navigation, help, and form panels.
        """
        log_subsection("_init_ui")
        try:
            keys = [
                "ProBtnProject", "ProBtnCharacters", "ProBtnStorylines",
                "ProBtnChapters", "ProBtnScenes", "ProBtnObjects", "ProBtnLocations", "ProBtnExit"
            ]
            callbacks = {
                "ProBtnProject": lambda: self._on_nav_clicked("ProBtnProject", self._show_project_form),
                "ProBtnCharacters": lambda: self._on_nav_clicked("ProBtnCharacters", self._show_characters_form),
                "ProBtnStorylines": lambda: self._on_nav_clicked("ProBtnStorylines", self._show_storylines_form),
                "ProBtnChapters": lambda: self._on_nav_clicked("ProBtnChapters", self._show_chapters_form),
                "ProBtnScenes": lambda: self._on_nav_clicked("ProBtnScenes", self._show_scenes_form),
                "ProBtnObjects": lambda: self._on_nav_clicked("ProBtnObjects", self._show_objects_form),
                "ProBtnLocations": lambda: self._on_nav_clicked("ProBtnLocations", self._show_locations_form),
                "ProBtnExit": self._exit_application
            }
            self.navigation_panel = NavigationPanel(
                self.translator, keys, self, callbacks
            )

            self.help_panel = HelpPanel(self.translator, self)
            self.help_panel.set_help_text(self.translator.help_text("HelpNewProject"))
            self.form_widget = FormStart(self.translator, self)

            self.splitter.addWidget(self.navigation_panel)
            self.splitter.addWidget(self.form_widget)
            self.splitter.addWidget(self.help_panel)
            self.splitter.setSizes(self.settings.get("splitter_sizes", [300, 900, 300]))

            # Corrected layout assignment
            layout = QHBoxLayout()
            layout.addWidget(self.splitter)
            self.setLayout(layout)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI", e)

    def _on_nav_clicked(self, key, handler):
        """
        Handles navigation button clicks and displays the corresponding form.
        """
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            self.active_nav_key = key
            handler()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_exception(f"Error in navigation click handler for '{key}'", e)

    def _show_project_form(self):
        """
        Displays the project form.
        """
        log_subsection("_show_project_form")
        try:
            form_widget = FormProjects(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpProject")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Project form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying project form", e)

    def _show_characters_form(self):
        """
        Displays the characters form.
        """
        log_subsection("_show_characters_form")
        try:
            form_widget = FormCharacters(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpChars")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Characters form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying characters form", e)

    def _show_storylines_form(self):
        """
        Displays the storylines form.
        """
        log_subsection("_show_storylines_form")
        try:
            form_widget = FormStorylines(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpStorylines")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Storylines form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying storylines form", e)

    def _show_chapters_form(self):
        """
        Displays the chapters form.
        """
        log_subsection("_show_chapters_form")
        try:
            form_widget = FormChapters(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpChapters")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Chapters form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying chapters form", e)

    def _show_scenes_form(self):
        """
        Displays the scenes form.
        """
        log_subsection("_show_scenes_form")
        try:
            form_widget = FormScenes(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpScenes")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Scenes form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying scenes form", e)

    def _show_objects_form(self):
        """
        Displays the objects form.
        """
        log_subsection("_show_objects_form")
        try:
            form_widget = FormObjects(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpObjects")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Objects form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying objects form", e)

    def _show_locations_form(self):
        """
        Displays the locations form.
        """
        log_subsection("_show_locations_form")
        try:
            form_widget = FormLocations(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpLocations")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Locations form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying locations form", e)

    def _replace_form_widget(self, new_widget):
        """
        Replaces the current form widget in the splitter with a new one.
        """
        old_widget = self.splitter.widget(1)
        if old_widget:
            old_widget.setParent(None)
        self.splitter.insertWidget(1, new_widget)

    def _exit_application(self):
        """
        Handles application exit and shows the start window.
        """
        log_subsection("_exit_application")
        try:
            if self.start_window:
                self.start_window.show()
            self.close()
            log_info("Application exit triggered, StartWindow shown.")
        except Exception as e:
            log_exception("Error during application exit", e)

    def closeEvent(self, event):
        """
        Saves splitter sizes and handles window close event.
        """
        log_subsection("closeEvent")
        try:
            self.settings["splitter_sizes"] = self.splitter.sizes()
            save_settings(self.settings)
            event.accept()
            log_info("Splitter sizes saved and application closed.")
        except Exception as e:
            log_exception("Error saving splitter sizes on close", e)
            event.accept()