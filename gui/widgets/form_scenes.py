from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormScenes(QWidget):
    """
    FormScenes widget for editing scene data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the scenes form with dynamic fields and translations.
        """
        log_section("form_scenes.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load scene fields from form_fields.json
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
            scene_fields = fields_config.get("project_chapters_scenes", [])

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("Scene"),
                fields=scene_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="scene",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormScenes initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormScenes", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        self.form_widget.update_translations()