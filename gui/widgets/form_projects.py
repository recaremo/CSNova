from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class ProjectForm(QWidget):
    """
    Form widget for project data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_projects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "title", "label_key": "project_title", "default_label": "Title", "type": "text"},
                {"name": "subtitle", "label_key": "project_subtitle", "default_label": "Subtitle", "type": "text"},
                {"name": "author", "label_key": "project_author", "default_label": "Author", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("project_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="project",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ProjectForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ProjectForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("ProjectForm save triggered.")