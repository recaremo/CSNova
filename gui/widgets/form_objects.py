from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.python_gui_styles import apply_theme_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormObjects(QWidget):
    """
    FormObjects widget for editing object data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    Robust error handling is implemented for file and JSON operations.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None, style=None):
        """
        Initializes the objects form with dynamic fields and translations.
        """
        log_section("form_objects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.style = style
            apply_theme_style(self, "panel", self.style)

            # Load object fields from form_fields.json with robust error handling
            try:
                with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                    fields_config = json.load(f)
                object_fields = fields_config.get("project_objects", [])
            except FileNotFoundError as fnf_error:
                log_exception("form_fields.json not found for FormObjects.", fnf_error)
                object_fields = []
            except json.JSONDecodeError as json_error:
                log_exception("JSON decode error in form_fields.json for FormObjects.", json_error)
                object_fields = []
            except Exception as e:
                log_exception("Unexpected error loading object fields in FormObjects.", e)
                object_fields = []

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=None,
                fields=object_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="objects",
                translator=self.translator,
                parent=self,
                style=self.style
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormObjects initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormObjects", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        try:
            self.form_widget.update_translations()
        except Exception as e:
            log_exception("Error updating translations in FormObjects", e)