from PySide6.QtWidgets import QWidget, QSplitter, QHBoxLayout
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.help_panel import HelpPanel
from core.logger import log_section, log_subsection, log_info, log_exception

class CenterPanel(QWidget):
    def __init__(self, navigation_panel, content_widget, help_panel, parent=None):
        log_section("center_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("CenterPanel")  # For stylesheet targeting

            # Create main splitter
            splitter = QSplitter()
            splitter.setObjectName("MainSplitter")

            # Add panels to splitter
            splitter.addWidget(navigation_panel)
            splitter.addWidget(content_widget)
            splitter.addWidget(help_panel)

            # Set initial splitter sizes (optional)
            splitter.setSizes([200, 800, 200])

            # Layout
            layout = QHBoxLayout(self)
            layout.addWidget(splitter)
            self.setLayout(layout)
            log_info("CenterPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing CenterPanel", e)