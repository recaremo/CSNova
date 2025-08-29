from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QSplitter, QHBoxLayout
)
from gui.styles.style_utils import load_button_style, load_active_button_style
from core.translator import Translator
from config.settings import load_settings, save_settings
from core.translations.help_loader import load_help_texts
from core.translations.form_labels import load_form_labels
from gui.widgets.form_toolbar import FormToolbar
from gui.widgets.base_form_widget import BaseFormWidget

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
        self.form_labels = load_form_labels(self.translator.lang)
        self.button_style = load_button_style(18)
        self.button_style_active = load_active_button_style(18)
        self.active_nav_key = None
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
        self.button_style = load_button_style(18)
        self.button_style_active = load_active_button_style(18)

        for key in keys:
            btn = QPushButton(self.translator.tr(key))
            btn.setFixedSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            btn.setStyleSheet(self.button_style)
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

        # Navigation mit Highlight
        self.nav_buttons["btn_project"].clicked.connect(lambda: self._on_nav_clicked("btn_project", self._show_project_text))
        self.nav_buttons["btn_characters"].clicked.connect(lambda: self._on_nav_clicked("btn_characters", self._show_characters_text))
        self.nav_buttons["btn_storylines"].clicked.connect(lambda: self._on_nav_clicked("btn_storylines", self._show_storylines_text))
        self.nav_buttons["btn_chapters"].clicked.connect(lambda: self._on_nav_clicked("btn_chapters", self._show_chapters_text))
        self.nav_buttons["btn_scenes"].clicked.connect(lambda: self._on_nav_clicked("btn_scenes", self._show_scenes_text))
        self.nav_buttons["btn_objects"].clicked.connect(lambda: self._on_nav_clicked("btn_objects", self._show_objects_text))
        self.nav_buttons["btn_locations"].clicked.connect(lambda: self._on_nav_clicked("btn_locations", self._show_locations_text))
        self.nav_buttons["btn_exit"].clicked.connect(self._exit_application)

    def _on_nav_clicked(self, key, handler):
        for k, btn in self.nav_buttons.items():
            btn.setStyleSheet(self.button_style)
        self.nav_buttons[key].setStyleSheet(self.button_style_active)
        self.active_nav_key = key
        handler()

    def _show_project_text(self):
        fields = [
            {"name": "title", "label_key": "project_title", "default_label": "Title", "type": "text"},
            {"name": "subtitle", "label_key": "project_subtitle", "default_label": "Subtitle", "type": "text"},
            {"name": "author", "label_key": "project_author", "default_label": "Author", "type": "text"},
            {"name": "premise", "label_key": "project_premise", "default_label": "Premise", "type": "text"},
            {"name": "genre", "label_key": "project_genre", "default_label": "Genre", "type": "text"},
            {"name": "narrative_perspective", "label_key": "project_narrative_perspective", "default_label": "Narrative Perspective", "type": "text"},
            {"name": "timeline", "label_key": "project_timeline", "default_label": "Timeline", "type": "text"},
            {"name": "target_group", "label_key": "project_target_group", "default_label": "Target Group", "type": "text"},
            {"name": "cover_image", "label_key": "project_cover_image", "default_label": "Cover Image", "type": "text"},
            {"name": "start_date", "label_key": "project_start_date", "default_label": "Start Date", "type": "date"},
            {"name": "deadline", "label_key": "project_deadline", "default_label": "Deadline", "type": "date"},
            {"name": "word_count_goal", "label_key": "project_word_count_goal", "default_label": "Word Count Goal", "type": "spin", "max": 100000},
        ]

        def toolbar_actions(toolbar):
            toolbar.new_action.triggered.connect(lambda: print("Neuer Datensatz"))
            toolbar.delete_action.triggered.connect(lambda: print("Datensatz löschen"))
            toolbar.prev_action.triggered.connect(lambda: print("Ein Datensatz zurück"))
            toolbar.next_action.triggered.connect(lambda: print("Ein Datensatz vor"))
            toolbar.save_action.triggered.connect(self._save_project_form)

        form_widget = BaseFormWidget(
            title=self.form_labels.get("project_form_label", "Project"),
            fields=fields,
            form_labels=self.form_labels,
            toolbar_actions=toolbar_actions,
            parent=self
        )

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

    def _save_project_form(self):
        print("💾 Save button clicked")
        # Hier kann die Speicherlogik ergänzt werden

    def _show_characters_text(self):
        self._update_content("Characters")

    def _show_storylines_text(self):
        self._update_content("Storylines")

    def _show_chapters_text(self):
        self._update_content("Chapters")

    def _show_scenes_text(self):
        self._update_content("Scenes")

    def _show_objects_text(self):
        self._update_content("Objects")

    def _show_locations_text(self):
        self._update_content("Locations")

    def _exit_application(self):
        self.close()

    def closeEvent(self, event):
        self.settings["splitter_sizes"] = self.splitter.sizes()
        save_settings(self.settings)
        event.accept()