from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_exception

class StorylinesForm(QWidget):
    """
    Form widget for storyline data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_storylines.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "storyline_title", "label_key": "storyline_title", "default_label": "Title", "type": "text"},
                {"name": "storyline_summary", "label_key": "storyline_summary", "default_label": "Summary", "type": "text"},
                {"name": "storyline_notes", "label_key": "storyline_notes", "default_label": "Notes", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("storyline_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="storyline",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("StorylinesForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StorylinesForm", e)

    def _on_save(self):
        """
        Handle save action for storyline form.
        """
        log_subsection("_on_save")
        try:
            title = self.form.inputs["storyline_title"].text()
            if not title:
                log_info("Validation failed: storyline_title is empty.")
                return
            # ...save logic...
            log_info("StorylinesForm save triggered.")
        except Exception as e:
            log_exception("Error during StorylinesForm save", e)