from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormCharacters(QWidget):
    """
    FormCharacters widget for editing character data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    Robust error handling is implemented for file and JSON operations.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the characters form with dynamic fields and translations.
        """
        log_section("form_characters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load character fields from form_fields.json with robust error handling
            try:
                with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                    fields_config = json.load(f)
                character_fields = fields_config.get("character_main", [])
            except FileNotFoundError as fnf_error:
                log_exception("form_fields.json not found for FormCharacters.", fnf_error)
                character_fields = []
            except json.JSONDecodeError as json_error:
                log_exception("JSON decode error in form_fields.json for FormCharacters.", json_error)
                character_fields = []
            except Exception as e:
                log_exception("Unexpected error loading character fields in FormCharacters.", e)
                character_fields = []

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=None,
                fields=character_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="char_ma",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormCharacters initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormCharacters", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        try:
            self.form_widget.update_translations()
        except Exception as e:
            log_exception("Error updating translations in FormCharacters", e)