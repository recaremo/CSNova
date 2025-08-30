from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class LocationsForm(QWidget):
    """
    Form widget for location data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_locations.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "location_name", "label_key": "location_name", "default_label": "Name", "type": "text"},
                {"name": "location_type", "label_key": "location_type", "default_label": "Type", "type": "text"},
                {"name": "location_description", "label_key": "location_description", "default_label": "Description", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("location_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="location",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("LocationsForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing LocationsForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("LocationsForm save triggered.")