from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QSplitter, QHBoxLayout,
    QFormLayout, QLineEdit, QDateEdit, QSpinBox
)
from gui.styles.style_utils import load_button_style
from gui.styles.form_styles import load_form_style  # Style for form fields
from core.translator import Translator
from config.settings import load_settings, save_settings
from core.translations.help_loader import load_help_texts
from core.translations.form_labels import load_form_labels  # Load translated form labels

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
        self._set_background()
        self._init_ui()

    def _set_background(self):
        # Set the background color of the window
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#f0f0f0"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def _init_ui(self):
        # Create navigation buttons
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

        # Create main content and help areas
        self.input_area = QTextEdit()
        self.help_area = QLabel()
        self.help_area.setWordWrap(True)

        left_widget = QWidget()
        left_widget.setLayout(self.nav_layout)

        # Create horizontal splitter layout: navigation | content | help
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(left_widget)
        self.splitter.addWidget(self.input_area)
        self.splitter.addWidget(self.help_area)
        self.splitter.setSizes(self.settings.get("splitter_sizes", [300, 900, 300]))

        layout = QHBoxLayout(self)
        layout.addWidget(self.splitter)

        # Connect navigation buttons to their respective handlers
        self.nav_buttons["btn_project"].clicked.connect(self._show_project_text)
        self.nav_buttons["btn_characters"].clicked.connect(self._show_characters_text)
        self.nav_buttons["btn_storylines"].clicked.connect(self._show_storylines_text)
        self.nav_buttons["btn_chapters"].clicked.connect(self._show_chapters_text)
        self.nav_buttons["btn_scenes"].clicked.connect(self._show_scenes_text)
        self.nav_buttons["btn_objects"].clicked.connect(self._show_objects_text)
        self.nav_buttons["btn_locations"].clicked.connect(self._show_locations_text)
        self.nav_buttons["btn_exit"].clicked.connect(self._exit_application)

    def _update_content(self, section):
        # Replace current content widget with QTextEdit if needed
        if not isinstance(self.splitter.widget(1), QTextEdit):
            old_widget = self.splitter.widget(1)
            if old_widget:
                old_widget.setParent(None)
            self.splitter.insertWidget(1, self.input_area)

        # Ensure help area is present
        if self.splitter.count() < 3:
            self.splitter.addWidget(self.help_area)

        # Update content and help text
        self.input_area.setPlainText(f"[{section}]\n\nEnter {section.lower()} data here …")
        key = f"help_{section.lower()}"
        help_text = self.help_texts.get(key, "Help and information will be displayed here.")
        self.help_area.setText(help_text)
        self.splitter.setSizes([300, 900, 300])

    def _show_project_text(self):
        print("✅ Project form triggered")
        form_layout = QFormLayout()
        self.fields = {}
        style = load_form_style(16)

        # Load translated form title
        form_title = self.form_labels.get("project_form_label", "Project")
        title_label = QLabel(form_title)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 12px;")

        # Create text fields with translated labels
        for field in [
            "title", "subtitle", "author", "premise",
            "genre", "narrative_perspective", "timeline", "target_group", "cover_image"
        ]:
            line = QLineEdit()
            line.setStyleSheet(style)
            label_key = f"project_{field}"
            label_text = self.form_labels.get(label_key, field.replace("_", " ").title())
            form_layout.addRow(label_text, line)
            self.fields[field] = line

        # Create date fields with translated labels
        for field in ["start_date", "deadline"]:
            label_key = f"project_{field}"
            label_text = self.form_labels.get(label_key, field.replace("_", " ").title())
            date_edit = QDateEdit()
            date_edit.setCalendarPopup(True)
            date_edit.setStyleSheet(style)
            form_layout.addRow(label_text, date_edit)
            self.fields[field] = date_edit

        # Create spinbox for word count goal
        label_key = "project_word_count_goal"
        label_text = self.form_labels.get(label_key, "Word Count Goal")
        goal_spin = QSpinBox()
        goal_spin.setMaximum(100000)
        goal_spin.setStyleSheet(style)
        form_layout.addRow(label_text, goal_spin)
        self.fields["word_count_goal"] = goal_spin

        # Create save button with translated label
        save_label = self.form_labels.get("project_btn_save", "Save")
        save_button = QPushButton(save_label)
        save_button.setFixedSize(120, 40)
        save_button.setStyleSheet("font-size: 14px; padding: 6px;")
        save_button.clicked.connect(self._save_project_form)

        # Assemble layout with title, form, and save button
        form_widget = QWidget()
        form_container = QVBoxLayout()
        form_container.addWidget(title_label)
        form_container.addLayout(form_layout)
        form_container.addWidget(save_button, alignment=Qt.AlignRight)
        form_widget.setLayout(form_container)

        # Replace current content widget with the form
        old_widget = self.splitter.widget(1)
        if old_widget:
            old_widget.setParent(None)
        self.splitter.insertWidget(1, form_widget)

        # Ensure help area is present
        if self.splitter.count() < 3:
            self.splitter.addWidget(self.help_area)

        self.splitter.setSizes([300, 900, 300])

        key = "help_project"
        help_text = self.help_texts.get(key, "Help and information will be displayed here.")
        self.help_area.setText(help_text)

    def _save_project_form(self):
        print("💾 Save button clicked")
        # Placeholder for future save logic

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
        # Close the application
        self.close()

    def closeEvent(self, event):
        # Save splitter sizes before closing
        self.settings["splitter_sizes"] = self.splitter.sizes()
        save_settings(self.settings)
        event.accept()
