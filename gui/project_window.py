from PySide6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QSizePolicy, QSplitter
)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

from gui.styles.style_utils import load_button_style
from core.translator import Translator
from config.settings import load_settings, save_settings
from core.translations.help_loader import load_help_texts

class ProjectWindow(QWidget):
    BUTTON_WIDTH = 240
    BUTTON_HEIGHT = 70

    def __init__(self, translator=None, parent=None):
        self.translator = translator or Translator(default="en")
        super().__init__(parent)
        self.resize(1600, 900)
        self.setWindowTitle(self.translator.tr("project_window_title"))
        self.settings = load_settings()
        self.help_texts = load_help_texts(self.translator.lang)
        self._set_background()
        self._init_ui()

    def _set_background(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#f0f0f0"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def _init_ui(self):
        self.nav_layout = QVBoxLayout()
        self.nav_buttons = {}
        keys = [
            "btn_project", "btn_characters", "btn_storylines",
            "btn_chapters", "btn_scenes", "btn_objects", "btn_locations", "btn_exit"
        ]
        style = load_button_style(18)
        for key in keys:
            btn = QPushButton(self.translator.tr(key))
            btn.setFixedSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            btn.setStyleSheet(style)
            self.nav_layout.addWidget(btn)
            self.nav_buttons[key] = btn

        self.nav_buttons["btn_exit"].clicked.connect(self._exit_application)

        self.input_area = QTextEdit()
        self.help_area = QLabel()
        self.help_area.setWordWrap(True)

        left_widget = QWidget()
        left_widget.setLayout(self.nav_layout)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(left_widget)
        self.splitter.addWidget(self.input_area)
        self.splitter.addWidget(self.help_area)
        self.splitter.setSizes(self.settings.get("splitter_sizes", [300, 900, 300]))

        layout = QHBoxLayout(self)
        layout.addWidget(self.splitter)

        # Button-Verbindungen
        self.nav_buttons["btn_project"].clicked.connect(lambda: self._update_content("Project"))
        self.nav_buttons["btn_characters"].clicked.connect(lambda: self._update_content("Characters"))
        self.nav_buttons["btn_storylines"].clicked.connect(lambda: self._update_content("Storylines"))
        self.nav_buttons["btn_chapters"].clicked.connect(lambda: self._update_content("Chapters"))
        self.nav_buttons["btn_scenes"].clicked.connect(lambda: self._update_content("Scenes"))
        self.nav_buttons["btn_objects"].clicked.connect(lambda: self._update_content("Objects"))
        self.nav_buttons["btn_locations"].clicked.connect(lambda: self._update_content("Places"))

    def _update_content(self, section):
        self.input_area.setPlainText(f"[{section}]\n\nEnter {section.lower()} data here …")
        self.help_area.setText(self.help_texts.get(section, "Help and information will be displayed here."))

    def _exit_application(self):
        self.close()

    def closeEvent(self, event):
        self.settings["splitter_sizes"] = self.splitter.sizes()
        save_settings(self.settings)
        event.accept()
