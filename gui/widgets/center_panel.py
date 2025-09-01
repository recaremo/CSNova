from PySide6.QtWidgets import QWidget, QSplitter, QHBoxLayout
from gui.widgets.navigation_panel import NavigationPanel
from gui.styles.form_styles import load_global_stylesheet
from core.logger import log_section, log_subsection, log_info, log_exception

class CenterPanel(QWidget):
    def __init__(self, navigation_panel, content_widget, help_panel, parent=None):
        log_section("center_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("CenterPanel")
            self.setStyleSheet(load_global_stylesheet())

            self.splitter = QSplitter(self)
            self.splitter.addWidget(navigation_panel)
            self.splitter.addWidget(content_widget)
            self.splitter.addWidget(help_panel)
            self.splitter.setSizes([200, 800, 200])  # Adjust as needed

            layout = QHBoxLayout(self)
            layout.addWidget(self.splitter)
            self.setLayout(layout)
            log_info("CenterPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing CenterPanel", e)