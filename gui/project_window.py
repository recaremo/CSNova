from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSplitter, QHBoxLayout

from gui.styles.form_styles import load_button_style, load_active_button_style, load_global_stylesheet
from core.translator import Translator
from config.settings import load_settings, save_settings
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.help_panel import HelpPanel

# Import modular forms
from gui.widgets.form_projects import ProjectForm
from gui.widgets.form_characters import CharactersForm
from gui.widgets.form_storylines import StorylinesForm
from gui.widgets.form_chapters import ChaptersForm
from gui.widgets.form_scenes import ScenesForm
from gui.widgets.form_objects import ObjectsForm
from gui.widgets.form_locations import LocationsForm
from gui.widgets.form_start import StartForm

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error, log_exception

class ProjectWindow(QWidget):
    BUTTON_WIDTH = 240
    BUTTON_HEIGHT = 70

    def __init__(self, translator=None, parent=None, start_window=None):
        log_section("project_window.py")
        log_subsection("__init__")
        try:
            self.translator = translator or Translator(lang="en")
            super().__init__(parent)
            self.resize(1600, 900)
            self.setWindowTitle(self.translator.tr("project_window_title"))
            self.settings = load_settings()
            self.button_style = load_button_style(18)
            self.button_style_active = load_active_button_style(18)
            self.active_nav_key = None
            self.start_window = start_window
            self.setStyleSheet(load_global_stylesheet())  # Apply global stylesheet

            # Initialisiere splitter direkt am Anfang!
            self.splitter = QSplitter(Qt.Horizontal)
            self.splitter.setObjectName("MainSplitter")   # For splitter styling

            self._set_background()
            self._init_ui()
            log_info("ProjectWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectWindow", e)

    def _set_background(self):
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
        log_subsection("_init_ui")
        try:
            keys = [
                "btn_project", "btn_characters", "btn_storylines",
                "btn_chapters", "btn_scenes", "btn_objects", "btn_locations", "btn_exit"
            ]
            callbacks = {
                "btn_project": lambda: self._on_nav_clicked("btn_project", self._show_project_form),
                "btn_characters": lambda: self._on_nav_clicked("btn_characters", self._show_characters_form),
                "btn_storylines": lambda: self._on_nav_clicked("btn_storylines", self._show_storylines_form),
                "btn_chapters": lambda: self._on_nav_clicked("btn_chapters", self._show_chapters_form),
                "btn_scenes": lambda: self._on_nav_clicked("btn_scenes", self._show_scenes_form),
                "btn_objects": lambda: self._on_nav_clicked("btn_objects", self._show_objects_form),
                "btn_locations": lambda: self._on_nav_clicked("btn_locations", self._show_locations_form),
                "btn_exit": self._exit_application
            }
            self.navigation_panel = NavigationPanel(
                keys, self.translator, self.button_style, self.button_style_active, callbacks, self
            )

            self.help_panel = HelpPanel(self)
            # Start with project form
            self.form_widget = StartForm(self.translator, self)

            self.splitter.addWidget(self.navigation_panel)
            self.splitter.addWidget(self.form_widget)
            self.splitter.addWidget(self.help_panel)
            self.splitter.setSizes(self.settings.get("splitter_sizes", [300, 900, 300]))

            layout = QHBoxLayout(self)
            layout.addWidget(self.splitter)
            self.setLayout(layout)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI", e)

    def _on_nav_clicked(self, key, handler):
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            self.active_nav_key = key
            handler()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_exception(f"Error in navigation click handler for '{key}'", e)

    def _show_project_form(self):
        log_subsection("_show_project_form")
        try:
            form_widget = ProjectForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_project")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Project form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying project form", e)

    def _show_characters_form(self):
        log_subsection("_show_characters_form")
        try:
            form_widget = CharactersForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_characters")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Characters form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying characters form", e)

    def _show_storylines_form(self):
        log_subsection("_show_storylines_form")
        try:
            form_widget = StorylinesForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_storylines")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Storylines form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying storylines form", e)

    def _show_chapters_form(self):
        log_subsection("_show_chapters_form")
        try:
            form_widget = ChaptersForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_chapters")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Chapters form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying chapters form", e)

    def _show_scenes_form(self):
        log_subsection("_show_scenes_form")
        try:
            form_widget = ScenesForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_scenes")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Scenes form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying scenes form", e)

    def _show_objects_form(self):
        log_subsection("_show_objects_form")
        try:
            form_widget = ObjectsForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_objects")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Objects form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying objects form", e)

    def _show_locations_form(self):
        log_subsection("_show_locations_form")
        try:
            form_widget = LocationsForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_locations")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Locations form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying locations form", e)

    def _replace_form_widget(self, new_widget):
        """
        Replace the current form widget in the splitter.
        """
        old_widget = self.splitter.widget(1)
        if old_widget:
            old_widget.setParent(None)
        self.splitter.insertWidget(1, new_widget)

    def _exit_application(self):
        log_subsection("_exit_application")
        try:
            if self.start_window:
                self.start_window.show()
            self.close()
            log_info("Application exit triggered, StartWindow shown.")
        except Exception as e:
            log_exception("Error during application exit", e)

    def closeEvent(self, event):
        log_subsection("closeEvent")
        try:
            self.settings["splitter_sizes"] = self.splitter.sizes()
            save_settings(self.settings)
            event.accept()
            log_info("Splitter sizes saved and application closed.")
        except Exception as e:
            log_exception("Error saving splitter sizes on close", e)
            event.accept()