import json
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error
from config.dev import FORM_FIELDS_FILE

class ObjectsForm(QWidget):
    """
    Form widget for object data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_objects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Felder zentral aus JSON laden
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                all_fields = json.load(f)
            fields = all_fields.get("objects", [])

            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)

            self.form = BaseFormWidget(
                title=self.translator.tr("object"),
                fields=fields,
                toolbar_actions=toolbar_actions,
                form_prefix="object",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ObjectsForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ObjectsForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("ObjectsForm save triggered.")