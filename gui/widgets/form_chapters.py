from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class ChaptersForm(QWidget):
    """
    Form widget for chapter data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_chapters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "chapter_title", "label_key": "chapter_title", "default_label": "Title", "type": "text"},
                {"name": "chapter_number", "label_key": "chapter_number", "default_label": "Number", "type": "spin", "max": 999},
                {"name": "chapter_summary", "label_key": "chapter_summary", "default_label": "Summary", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("chapter_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="chapter",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ChaptersForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ChaptersForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("ChaptersForm save triggered.")