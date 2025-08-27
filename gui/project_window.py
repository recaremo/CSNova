from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QSizePolicy
)
from PySide6.QtGui import QPalette, QColor
from gui.styles.style_utils import load_button_style
from core.translator import Translator

class ProjectWindow(QWidget):
    BUTTON_WIDTH   = 240
    BUTTON_HEIGHT  = 70

    def __init__(self, parent=None, translator=None):
        self.translator = translator or Translator(default="en")
        super().__init__(parent)
        self.setWindowTitle(self.translator.tr("project_window_title"))
        self.resize(parent.width(), parent.height())
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
            "Chapters", "Scenes", "Objects", "Places", "Exit"
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

        # Main layout: horizontal split
        main_layout = QHBoxLayout(self)
        main_layout.addLayout(self.nav_layout, 1)
        main_layout.addWidget(self.input_area, 2)
        main_layout.addWidget(self.help_area, 1)

    def _exit_application(self):
        QApplication.instance().quit()