from PySide6.QtWidgets import QWidget, QToolBar, QHBoxLayout, QWidget
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize
from core.logger import log_section, log_subsection, log_info, log_exception
from gui.styles.form_styles import load_button_style

class FormToolbar(QWidget):
    def __init__(self, translator, form_prefix, parent=None):
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.toolbar = QToolBar(self)
            self.toolbar.setStyleSheet(load_button_style())
            self.toolbar.setIconSize(QSize(32, 32))

            # Spacer for left margin
            left_spacer = QWidget()
            left_spacer.setFixedWidth(10)
            self.toolbar.addWidget(left_spacer)

            self.translator = translator

            # Create actions with translated labels
            self.new_action = QAction(self.translator.form_label(f"{form_prefix}_btn_new"), self)
            self.delete_action = QAction(self.translator.form_label(f"{form_prefix}_btn_delete"), self)
            self.prev_action = QAction(self.translator.form_label(f"{form_prefix}_btn_preview"), self)
            self.next_action = QAction(self.translator.form_label(f"{form_prefix}_btn_next"), self)
            self.save_action = QAction(self.translator.form_label(f"{form_prefix}_btn_save"), self)

            # Optionally set icons if available
            # self.new_action.setIcon(QIcon("icons/new.png"))
            # self.delete_action.setIcon(QIcon("icons/delete.png"))
            # self.prev_action.setIcon(QIcon("icons/prev.png"))
            # self.next_action.setIcon(QIcon("icons/next.png"))
            # self.save_action.setIcon(QIcon("icons/save.png"))

            # Add actions and spacing between buttons
            actions = [
                self.new_action,
                self.delete_action,
                self.prev_action,
                self.next_action,
                self.save_action
            ]
            for i, action in enumerate(actions):
                self.toolbar.addAction(action)
                if i < len(actions) - 1:
                    spacer = QWidget()
                    spacer.setFixedWidth(8)  # Space between buttons
                    self.toolbar.addWidget(spacer)

            layout = QHBoxLayout(self)
            layout.addWidget(self.toolbar)
            self.setLayout(layout)
            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormToolbar", e)