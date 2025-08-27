from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QSizePolicy, QSplitter
)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from gui.styles.style_utils import load_button_style
from core.translator import Translator
from config.settings import load_settings, save_settings

class ProjectWindow(QWidget):
    BUTTON_WIDTH   = 240
    BUTTON_HEIGHT  = 70

    def __init__(self, translator=None, parent=None):
        self.translator = translator or Translator(default="en")
        super().__init__(parent)
        if parent is not None:
            self.resize(1600, 900)
        else:
            self.resize(1600, 900)
        self.setWindowTitle(self.translator.tr("project_window_title"))
        self.settings = load_settings()
        self._set_background()
        self._init_ui()

    def _set_background(self):
        # Set a neutral background color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#f0f0f0"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def _init_ui(self):
        # Left column: navigation buttons
        self.nav_layout = QVBoxLayout()
        self.nav_buttons = {}
        labels = [
            "Project", "Characters", "Storylines",
            "Chapters", "Scenes", "Objects", "Locations", "Exit"
        ]
        font_px = 18  # Match default font size from start_window.py
        style = load_button_style(font_px)
        for label in labels:
            btn = QPushButton(label)
            btn.setFixedSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            btn.setStyleSheet(style)
            self.nav_layout.addWidget(btn)
            self.nav_buttons[label] = btn

        # Connect exit button
        self.nav_buttons["Exit"].setText(self.translator.tr("btn_exit"))
        self.nav_buttons["Exit"].clicked.connect(self._exit_application)

        # Middle column: input area
        self.input_area = QTextEdit()
        self.input_area.setPlaceholderText("Enter project data here …")

        # Right column: help and info area
        self.help_area = QLabel("Help and information will be displayed here.")
        self.help_area.setWordWrap(True)
        self.help_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Create single splitter for three columns
        left_widget = QWidget()
        left_widget.setLayout(self.nav_layout)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(left_widget)
        self.splitter.addWidget(self.input_area)
        self.splitter.addWidget(self.help_area)

        saved_sizes = self.settings.get("splitter_sizes", [300, 900, 300])
        self.settings["splitter_sizes"] = saved_sizes
        self.splitter.setSizes(saved_sizes)
        self._last_sizes = saved_sizes.copy()

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.splitter)

    def _exit_application(self):
        self.close()

    def closeEvent(self, event):
        print("closeEvent triggered")  # ← Testausgabe
        current_sizes = self.splitter.sizes()
        print("Splitter sizes:", current_sizes)  # ← weitere Kontrolle
        self.settings["splitter_sizes"] = current_sizes
        save_settings(self.settings)
        event.accept()
        super().closeEvent(event)
