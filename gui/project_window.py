from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QSplitter, QHBoxLayout
)
from gui.styles.style_utils import load_button_style, load_active_button_style
from core.translator import Translator
from config.settings import load_settings, save_settings
from core.translations.help_loader import load_help_texts
from core.translations.form_labels import load_form_labels
from gui.widgets.form_toolbar import FormToolbar
from gui.widgets.base_form_widget import BaseFormWidget
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.help_panel import HelpPanel

# Import central logging functions
from core.lloger import log_section, log_subsection, log_info, log_error

# Import central directories (for future resource loading if needed)
from config.dev import HELP_DIR, FORMS_DIR, ASSETS_DIR

class ProjectWindow(QWidget):
    BUTTON_WIDTH = 240
    BUTTON_HEIGHT = 70

    def __init__(self, translator=None, parent=None):
        log_section("project_window.py")
        log_subsection("__init__")
        try:
            self.translator = translator or Translator(default="en")
            super().__init__(parent)
            self.resize(1600, 900)
            self.setWindowTitle(self.translator.tr("project_window_title"))
            self.settings = load_settings()
            self.help_texts = load_help_texts(self.translator.lang)
            self.form_labels = load_form_labels(self.translator.lang)
            self.button_style = load_button_style(18)
            self.button_style_active = load_active_button_style(18)
            self.active_nav_key = None
            self._set_background()
            self._init_ui()
            log_info("ProjectWindow initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ProjectWindow: {str(e)}")

    def _set_background(self):
        log_subsection("_set_background")
        try:
            palette = self.palette()
            palette.setColor(QPalette.Window, QColor("#f0f0f0"))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
            log_info("Background set successfully.")
        except Exception as e:
            log_error(f"Error setting background: {str(e)}")

    def _init_ui(self):
        log_subsection("_init_ui")
        try:
            keys = [
                "btn_project", "btn_characters", "btn_storylines",
                "btn_chapters", "btn_scenes", "btn_objects", "btn_locations", "btn_exit"
            ]
            callbacks = {
                "btn_project": lambda: self._on_nav_clicked("btn_project", self._show_project_text),
                "btn_characters": lambda: self._on_nav_clicked("btn_characters", self._show_characters_text),
                "btn_storylines": lambda: self._on_nav_clicked("btn_storylines", self._show_storylines_text),
                "btn_chapters": lambda: self._on_nav_clicked("btn_chapters", self._show_chapters_text),
                "btn_scenes": lambda: self._on_nav_clicked("btn_scenes", self._show_scenes_text),
                "btn_objects": lambda: self._on_nav_clicked("btn_objects", self._show_objects_text),
                "btn_locations": lambda: self._on_nav_clicked("btn_locations", self._show_locations_text),
                "btn_exit": self._exit_application
            }
            self.navigation_panel = NavigationPanel(
                keys, self.translator, self.button_style, self.button_style_active, callbacks, self
            )

            self.help_panel = HelpPanel(self)

            # Placeholder for main content area
            self.input_area = QTextEdit()

            self.splitter = QSplitter(Qt.Horizontal)
            self.splitter.addWidget(self.navigation_panel)
            self.splitter.addWidget(self.input_area)
            self.splitter.addWidget(self.help_panel)
            self.splitter.setSizes(self.settings.get("splitter_sizes", [300, 900, 300]))

            layout = QHBoxLayout(self)
            layout.addWidget(self.splitter)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing UI: {str(e)}")

    def _on_nav_clicked(self, key, handler):
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            self.active_nav_key = key
            handler()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_error(f"Error in navigation click handler for '{key}': {str(e)}")

    def _show_project_text(self):
        log_subsection("_show_project_text")
        try:
            fields = [
                {"name": "title", "label_key": "project_title", "default_label": "Title", "type": "text"},
                {"name": "subtitle", "label_key": "project_subtitle", "default_label": "Subtitle", "type": "text"},
                {"name": "author", "label_key": "project_author", "default_label": "Author", "type": "text"},
                {"name": "premise", "label_key": "project_premise", "default_label": "Premise", "type": "text"},
                {"name": "genre", "label_key": "project_genre", "default_label": "Genre", "type": "text"},
                {"name": "narrative_perspective", "label_key": "project_narrative_perspective", "default_label": "Narrative Perspective", "type": "text"},
                {"name": "timeline", "label_key": "project_timeline", "default_label": "Timeline", "type": "text"},
                {"name": "target_group", "label_key": "project_target_group", "default_label": "Target Group", "type": "text"},
                {"name": "cover_image", "label_key": "project_cover_image", "default_label": "Cover Image", "type": "text"},
                {"name": "start_date", "label_key": "project_start_date", "default_label": "Start Date", "type": "date"},
                {"name": "deadline", "label_key": "project_deadline", "default_label": "Deadline", "type": "date"},
                {"name": "word_count_goal", "label_key": "project_word_count_goal", "default_label": "Word Count Goal", "type": "spin", "max": 100000},
            ]

            def toolbar_actions(toolbar):
                log_subsection("toolbar_actions: project")
                toolbar.new_action.triggered.connect(lambda: log_info("New project record triggered."))
                toolbar.delete_action.triggered.connect(lambda: log_info("Delete project record triggered."))
                toolbar.prev_action.triggered.connect(lambda: log_info("Previous project record triggered."))
                toolbar.next_action.triggered.connect(lambda: log_info("Next project record triggered."))
                toolbar.save_action.triggered.connect(self._save_project_form)

            form_widget = BaseFormWidget(
                title=self.form_labels.get("project_form_label", "Project"),
                fields=fields,
                form_labels=self.form_labels,
                toolbar_actions=toolbar_actions,
                parent=self
            )

            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, form_widget)

            key = "help_project"
            help_text = self.help_texts.get(key, "Help and information will be displayed here.")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Project form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying project form: {str(e)}")

    def _save_project_form(self):
        log_subsection("_save_project_form")
        try:
            log_info("Save project button clicked.")
            # Add logic to save project data here
        except Exception as e:
            log_error(f"Error saving project data: {str(e)}")

    def _show_characters_text(self):
        log_subsection("_show_characters_text")
        try:
            fields = [
                {"name": "character_name", "label_key": "character_name", "default_label": "Name", "type": "text"},
                {"name": "character_nickname", "label_key": "character_nickname", "default_label": "Nickname", "type": "text"},
                {"name": "character_gender", "label_key": "character_gender", "default_label": "Gender", "type": "text"},
                {"name": "character_age", "label_key": "character_age", "default_label": "Age", "type": "spin", "max": 120},
                {"name": "character_role", "label_key": "character_role", "default_label": "Role", "type": "text"},
                {"name": "character_description", "label_key": "character_description", "default_label": "Description", "type": "text"},
            ]

            def toolbar_actions(toolbar):
                log_subsection("toolbar_actions: character")
                toolbar.new_action.triggered.connect(lambda: log_info("New character triggered."))
                toolbar.delete_action.triggered.connect(lambda: log_info("Delete character triggered."))
                toolbar.prev_action.triggered.connect(lambda: log_info("Previous character triggered."))
                toolbar.next_action.triggered.connect(lambda: log_info("Next character triggered."))
                toolbar.save_action.triggered.connect(self._save_character_form)

            form_widget = BaseFormWidget(
                title=self.form_labels.get("character_form_label", "Character"),
                fields=fields,
                form_labels=self.form_labels,
                toolbar_actions=toolbar_actions,
                parent=self
            )

            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, form_widget)

            key = "help_characters"
            help_text = self.help_texts.get(key, "Help and information will be displayed here.")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Character form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying character form: {str(e)}")

    def _save_character_form(self):
        log_subsection("_save_character_form")
        try:
            log_info("Save character button clicked.")
            # Add logic to save character data here
        except Exception as e:
            log_error(f"Error saving character data: {str(e)}")

    def _show_storylines_text(self):
        log_subsection("_show_storylines_text")
        try:
            fields = [
                {"name": "storyline_title", "label_key": "storyline_title", "default_label": "Title", "type": "text"},
                {"name": "storyline_summary", "label_key": "storyline_summary", "default_label": "Summary", "type": "text"},
                {"name": "storyline_notes", "label_key": "storyline_notes", "default_label": "Notes", "type": "text"},
            ]

            def toolbar_actions(toolbar):
                log_subsection("toolbar_actions: storyline")
                toolbar.new_action.triggered.connect(lambda: log_info("New storyline triggered."))
                toolbar.delete_action.triggered.connect(lambda: log_info("Delete storyline triggered."))
                toolbar.prev_action.triggered.connect(lambda: log_info("Previous storyline triggered."))
                toolbar.next_action.triggered.connect(lambda: log_info("Next storyline triggered."))
                toolbar.save_action.triggered.connect(self._save_storyline_form)

            form_widget = BaseFormWidget(
                title=self.form_labels.get("storyline_form_label", "Storyline"),
                fields=fields,
                form_labels=self.form_labels,
                toolbar_actions=toolbar_actions,
                parent=self
            )

            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, form_widget)

            key = "help_storylines"
            help_text = self.help_texts.get(key, "Help and information will be displayed here.")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Storyline form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying storyline form: {str(e)}")

    def _save_storyline_form(self):
        log_subsection("_save_storyline_form")
        try:
            log_info("Save storyline button clicked.")
            # Add logic to save storyline data here
        except Exception as e:
            log_error(f"Error saving storyline data: {str(e)}")

    def _show_chapters_text(self):
        log_subsection("_show_chapters_text")
        try:
            fields = [
                {"name": "chapter_title", "label_key": "chapter_title", "default_label": "Title", "type": "text"},
                {"name": "chapter_number", "label_key": "chapter_number", "default_label": "Number", "type": "spin", "max": 999},
                {"name": "chapter_summary", "label_key": "chapter_summary", "default_label": "Summary", "type": "text"},
            ]

            def toolbar_actions(toolbar):
                log_subsection("toolbar_actions: chapter")
                toolbar.new_action.triggered.connect(lambda: log_info("New chapter triggered."))
                toolbar.delete_action.triggered.connect(lambda: log_info("Delete chapter triggered."))
                toolbar.prev_action.triggered.connect(lambda: log_info("Previous chapter triggered."))
                toolbar.next_action.triggered.connect(lambda: log_info("Next chapter triggered."))
                toolbar.save_action.triggered.connect(self._save_chapter_form)

            form_widget = BaseFormWidget(
                title=self.form_labels.get("chapter_form_label", "Chapter"),
                fields=fields,
                form_labels=self.form_labels,
                toolbar_actions=toolbar_actions,
                parent=self
            )

            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, form_widget)

            key = "help_chapters"
            help_text = self.help_texts.get(key, "Help and information will be displayed here.")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Chapter form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying chapter form: {str(e)}")

    def _save_chapter_form(self):
        log_subsection("_save_chapter_form")
        try:
            log_info("Save chapter button clicked.")
            # Add logic to save chapter data here
        except Exception as e:
            log_error(f"Error saving chapter data: {str(e)}")

    def _show_scenes_text(self):
        log_subsection("_show_scenes_text")
        try:
            fields = [
                {"name": "scene_title", "label_key": "scene_title", "default_label": "Title", "type": "text"},
                {"name": "scene_number", "label_key": "scene_number", "default_label": "Number", "type": "spin", "max": 9999},
                {"name": "scene_summary", "label_key": "scene_summary", "default_label": "Summary", "type": "text"},
            ]

            def toolbar_actions(toolbar):
                log_subsection("toolbar_actions: scene")
                toolbar.new_action.triggered.connect(lambda: log_info("New scene triggered."))
                toolbar.delete_action.triggered.connect(lambda: log_info("Delete scene triggered."))
                toolbar.prev_action.triggered.connect(lambda: log_info("Previous scene triggered."))
                toolbar.next_action.triggered.connect(lambda: log_info("Next scene triggered."))
                toolbar.save_action.triggered.connect(self._save_scene_form)

            form_widget = BaseFormWidget(
                title=self.form_labels.get("scene_form_label", "Scene"),
                fields=fields,
                form_labels=self.form_labels,
                toolbar_actions=toolbar_actions,
                parent=self
            )

            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, form_widget)

            key = "help_scenes"
            help_text = self.help_texts.get(key, "Help and information will be displayed here.")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Scene form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying scene form: {str(e)}")

    def _save_scene_form(self):
        log_subsection("_save_scene_form")
        try:
            log_info("Save scene button clicked.")
            # Add logic to save scene data here
        except Exception as e:
            log_error(f"Error saving scene data: {str(e)}")

    def _show_objects_text(self):
        log_subsection("_show_objects_text")
        try:
            fields = [
                {"name": "object_name", "label_key": "object_name", "default_label": "Name", "type": "text"},
                {"name": "object_type", "label_key": "object_type", "default_label": "Type", "type": "text"},
                {"name": "object_description", "label_key": "object_description", "default_label": "Description", "type": "text"},
            ]

            def toolbar_actions(toolbar):
                log_subsection("toolbar_actions: object")
                toolbar.new_action.triggered.connect(lambda: log_info("New object triggered."))
                toolbar.delete_action.triggered.connect(lambda: log_info("Delete object triggered."))
                toolbar.prev_action.triggered.connect(lambda: log_info("Previous object triggered."))
                toolbar.next_action.triggered.connect(lambda: log_info("Next object triggered."))
                toolbar.save_action.triggered.connect(self._save_object_form)

            form_widget = BaseFormWidget(
                title=self.form_labels.get("object_form_label", "Object"),
                fields=fields,
                form_labels=self.form_labels,
                toolbar_actions=toolbar_actions,
                parent=self
            )

            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, form_widget)

            key = "help_objects"
            help_text = self.help_texts.get(key, "Help and information will be displayed here.")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Object form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying object form: {str(e)}")

    def _save_object_form(self):
        log_subsection("_save_object_form")
        try:
            log_info("Save object button clicked.")
            # Add logic to save object data here
        except Exception as e:
            log_error(f"Error saving object data: {str(e)}")

    def _show_locations_text(self):
        log_subsection("_show_locations_text")
        try:
            fields = [
                {"name": "location_name", "label_key": "location_name", "default_label": "Name", "type": "text"},
                {"name": "location_type", "label_key": "location_type", "default_label": "Type", "type": "text"},
                {"name": "location_description", "label_key": "location_description", "default_label": "Description", "type": "text"},
            ]

            def toolbar_actions(toolbar):
                log_subsection("toolbar_actions: location")
                toolbar.new_action.triggered.connect(lambda: log_info("New location triggered."))
                toolbar.delete_action.triggered.connect(lambda: log_info("Delete location triggered."))
                toolbar.prev_action.triggered.connect(lambda: log_info("Previous location triggered."))
                toolbar.next_action.triggered.connect(lambda: log_info("Next location triggered."))
                toolbar.save_action.triggered.connect(self._save_location_form)

            form_widget = BaseFormWidget(
                title=self.form_labels.get("location_form_label", "Location"),
                fields=fields,
                form_labels=self.form_labels,
                toolbar_actions=toolbar_actions,
                parent=self
            )

            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, form_widget)

            key = "help_locations"
            help_text = self.help_texts.get(key, "Help and information will be displayed here.")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Location form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying location form: {str(e)}")

    def _save_location_form(self):
        log_subsection("_save_location_form")
        try:
            log_info("Save location button clicked.")
            # Add logic to save location data here
        except Exception as e:
            log_error(f"Error saving location data: {str(e)}")

    def _exit_application(self):
        log_subsection("_exit_application")
        try:
            self.close()
            log_info("Application exit triggered.")
        except Exception as e:
            log_error(f"Error during application exit: {str(e)}")

    def closeEvent(self, event):
        log_subsection("closeEvent")
        try:
            self.settings["splitter_sizes"] = self.splitter.sizes()
            save_settings(self.settings)
            event.accept()
            log_info("Splitter sizes saved and application closed.")
        except Exception as e:
            log_error(f"Error saving splitter sizes on close: {str(e)}")
            event.accept()