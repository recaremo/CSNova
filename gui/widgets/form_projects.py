from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_exception

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
                {"name": "premise", "label_key": "project_premise", "default_label": "Premise", "type": "text"},
                {"name": "genre", "label_key": "project_genre", "default_label": "Genre", "type": "text"},
                {"name": "narrative_perspective", "label_key": "project_narrative_perspective", "default_label": "Narrative Perspective", "type": "text"},
                {"name": "timeline", "label_key": "project_timeline", "default_label": "Timeline", "type": "text"},
                {"name": "target_group", "label_key": "project_target_group", "default_label": "Target Group", "type": "text"},
                {"name": "start_date", "label_key": "project_start_date", "default_label": "Start Date", "type": "date"},
                {"name": "deadline", "label_key": "project_deadline", "default_label": "Deadline", "type": "date"},
                {"name": "word_count_goal", "label_key": "project_word_count_goal", "default_label": "Word Count Goal", "type": "spin", "max": 1000000},
                {"name": "cover_image", "label_key": "project_cover_image", "default_label": "Cover Image", "type": "text"},
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
            log_exception("Error initializing ProjectForm", e)

    def _on_save(self):
        """
        Handle save action for project form.
        """
        log_subsection("_on_save")
        try:
            title = self.form.inputs["title"].text()
            if not title:
                log_info("Validation failed: title is empty.")
                return
            # ...save logic...
            log_info("ProjectForm save triggered.")
        except Exception as e:
            log_exception("Error during ProjectForm save", e)