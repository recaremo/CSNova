from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class CharactersForm(QWidget):
    """
    Form widget for character data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_characters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "character_name", "label_key": "character_name", "default_label": "Name", "type": "text"},
                {"name": "character_nickname", "label_key": "character_nickname", "default_label": "Nickname", "type": "text"},
                {"name": "character_gender", "label_key": "character_gender", "default_label": "Gender", "type": "text"},
                {"name": "character_age", "label_key": "character_age", "default_label": "Age", "type": "spin", "max": 120},
                {"name": "character_role", "label_key": "character_role", "default_label": "Role", "type": "text"},
                {"name": "character_description", "label_key": "character_description", "default_label": "Description", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("character_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="character",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("CharactersForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing CharactersForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("CharactersForm save triggered.")