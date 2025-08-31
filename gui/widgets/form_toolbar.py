from PySide6.QtWidgets import QWidget, QToolBar, QHBoxLayout, QWidget
from PySide6.QtGui import QAction, QIcon
from core.logger import log_section, log_subsection, log_info, log_exception
from gui.styles.form_styles import get_current_style
from PySide6.QtCore import QSize

class FormToolbar(QWidget):
    def __init__(self, translator, form_prefix, parent=None):
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            toolbar_style = """
                QToolBar {
                    background: #7A8B8B;
                    border-bottom: 1px solid #cfcfcf;
                    min-height: 52px;
                    padding-top: 8px;
                    padding-bottom: 8px;
                }
                QToolButton {
                    min-width: 32px;
                    min-height: 32px;
                    padding: 8px 16px;
                    font-size: 14px;
                    qproperty-toolButtonStyle: ToolButtonTextBesideIcon;
                }
            """
            self.toolbar = QToolBar(self)
            self.toolbar.setStyleSheet(toolbar_style)
            self.toolbar.setIconSize(QSize(32, 32))

            # Spacer for left margin
            left_spacer = QWidget()
            left_spacer.setFixedWidth(10)
            self.toolbar.addWidget(left_spacer)

            self.translator = translator
            style = get_current_style()
            icon_factory = style.get("icon_factory", lambda name: QIcon())

            def safe_icon(name):
                icon = icon_factory(name)
                return icon if isinstance(icon, QIcon) else QIcon()

            # Create actions
            self.new_action = QAction(self.translator.form_label(f"{form_prefix}_btn_new"), self)
            self.delete_action = QAction(self.translator.form_label(f"{form_prefix}_btn_delete"), self)
            self.prev_action = QAction(self.translator.form_label(f"{form_prefix}_btn_preview"), self)
            self.next_action = QAction(self.translator.form_label(f"{form_prefix}_btn_next"), self)
            self.save_action = QAction(self.translator.form_label(f"{form_prefix}_btn_save"), self)

            self.new_action.setIcon(safe_icon("new"))
            self.delete_action.setIcon(safe_icon("delete"))
            self.prev_action.setIcon(safe_icon("prev"))
            self.next_action.setIcon(safe_icon("next"))
            self.save_action.setIcon(safe_icon("save"))

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