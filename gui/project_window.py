from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QSplitter, QHBoxLayout,
    QFormLayout, QLineEdit, QDateEdit, QSpinBox
)
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

        # Button connections
        self.nav_buttons["btn_project"].clicked.connect(self._show_project_text)
        self.nav_buttons["btn_characters"].clicked.connect(self._show_characters_text)
        self.nav_buttons["btn_storylines"].clicked.connect(self._show_storylines_text)
        self.nav_buttons["btn_chapters"].clicked.connect(self._show_chapters_text)
        self.nav_buttons["btn_scenes"].clicked.connect(self._show_scenes_text)
        self.nav_buttons["btn_objects"].clicked.connect(self._show_objects_text)
        self.nav_buttons["btn_locations"].clicked.connect(self._show_locations_text)
        self.nav_buttons["btn_exit"].clicked.connect(self._exit_application)

    def _update_content(self, section):
        if not isinstance(self.splitter.widget(1), QTextEdit):
            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, self.input_area)

        if self.splitter.count() < 3:
            self.splitter.addWidget(self.help_area)

        self.input_area.setPlainText(f"[{section}]\n\nEnter {section.lower()} data here …")
        key = f"help_{section.lower()}"
        help_text = self.help_texts.get(key, "Help and information will be displayed here.")
        self.help_area.setText(help_text)
        self.splitter.setSizes([300, 900, 300])

    def _show_project_text(self):
        print("✅ Project form triggered")
        form_layout = QFormLayout()
        self.fields = {}

        for field in [
            "project_title", "project_subtitle", "project_premise",
            "project_genre", "project_narrative_perspective", "timeline"
        ]:
            line = QLineEdit()
            form_layout.addRow(field.replace("_", " ").title(), line)
            self.fields[field] = line

        for field in ["project_start_date", "project_deadline"]:
            date_edit = QDateEdit()
            date_edit.setCalendarPopup(True)
            form_layout.addRow(field.replace("_", " ").title(), date_edit)
            self.fields[field] = date_edit

        goal_spin = QSpinBox()
        goal_spin.setMaximum(100000)
        form_layout.addRow("Words Count Goal", goal_spin)
        self.fields["project_words_count_goal"] = goal_spin

        form_widget = QWidget()
        form_widget.setLayout(form_layout)

        old_widget = self.splitter.widget(1)
        if old_widget:
            old_widget.setParent(None)
        self.splitter.insertWidget(1, form_widget)

        if self.splitter.count() < 3:
            self.splitter.addWidget(self.help_area)

        self.splitter.setSizes([300, 900, 300])

        key = "help_project"
        help_text = self.help_texts.get(key, "Help and information will be displayed here.")
        self.help_area.setText(help_text)

    def _show_characters_text(self):
        print("🧪 Characters button clicked")
        self._update_content("Characters")

    def _show_storylines_text(self):
        print("🧪 Storylines button clicked")
        self._update_content("Storylines")

    def _show_chapters_text(self):
        print("🧪 Chapters button clicked")
        self._update_content("Chapters")

    def _show_scenes_text(self):
        print("🧪 Scenes button clicked")
        self._update_content("Scenes")

    def _show_objects_text(self):
        print("🧪 Objects button clicked")
        self._update_content("Objects")

    def _show_locations_text(self):
        print("🧪 Locations button clicked")
        self._update_content("Locations")

    def _exit_application(self):
        self.close()

    def closeEvent(self, event):
        self.settings["splitter_sizes"] = self.splitter.sizes()
        save_settings(self.settings)
        event.accept()
