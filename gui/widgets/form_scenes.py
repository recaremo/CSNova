from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class ScenesForm(QWidget):
    """
    Form widget for scene data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_scenes.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "scene_title", "label_key": "scene_title", "default_label": "Title", "type": "text"},
                {"name": "scene_number", "label_key": "scene_number", "default_label": "Number", "type": "spin", "max": 9999},
                {"name": "scene_summary", "label_key": "scene_summary", "default_label": "Summary", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("scene_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="scene",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ScenesForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ScenesForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("ScenesForm save triggered.")