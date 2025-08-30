from PySide6.QtWidgets import QWidget, QToolBar, QHBoxLayout
from PySide6.QtGui import QAction
from core.logger import log_section, log_subsection, log_info, log_error

class FormToolbar(QWidget):
    def __init__(self, translator, form_prefix, parent=None):
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.toolbar = QToolBar(self)
            self.translator = translator
            # Use form_prefix like "project", "character", etc.
            self.new_action = QAction(self.translator.form_label(f"{form_prefix}_btn_new"), self)
            self.delete_action = QAction(self.translator.form_label(f"{form_prefix}_btn_delete"), self)
            self.prev_action = QAction(self.translator.form_label(f"{form_prefix}_btn_preview"), self)
            self.next_action = QAction(self.translator.form_label(f"{form_prefix}_btn_next"), self)
            self.save_action = QAction(self.translator.form_label(f"{form_prefix}_btn_save"), self)

            self.toolbar.addAction(self.new_action)
            self.toolbar.addAction(self.delete_action)
            self.toolbar.addAction(self.prev_action)
            self.toolbar.addAction(self.next_action)
            self.toolbar.addAction(self.save_action)

            layout = QHBoxLayout(self)
            layout.addWidget(self.toolbar)
            self.setLayout(layout)
            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing FormToolbar: {str(e)}")