## 6. - Programmecode

### 6.1 Hauptprogramm (main.py)

```python
import sys
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings, save_settings

from gui.start_window import StartWindow

def main():
    try:
        # --- Original code start ---
        init_schema()
        settings = load_settings()
        language = settings.get("language", "de")

        app = QApplication(sys.argv)
        # Pass default language to the start window
        window = StartWindow(default_language=language)
        window.show()
        app.exec()

        # Save language if it was changed
        if hasattr(window, "translator") and hasattr(window.translator, "lang"):
            settings["language"] = window.translator.lang
            save_settings(settings)
        # --- Original code end ---
    except Exception as e:
        # Catch and print any error that occurs
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

#### 6.1.1 Settings (setting.py)

```python
# config/settings.py

import json
import os

SETTINGS_FILE = "config/user_settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"language": "de"}  # Fallback

def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)
```

####6.1.2 Verzeichnisse (dev.py)

```python
# config/dev.py

from pathlib import Path
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "csnova.db"
```

### 6.2 Startfenster (start_window.py)

```python
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import QTimer
from core.translations import LANGUAGES, TRANSLATIONS
from gui.preferences import PreferencesWindow
from core.translator import Translator
from gui.styles.style_utils import load_button_style  # Import the style loader

import sys

class StartWindow(QWidget):
    DEFAULT_WIDTH        = 1920
    DEFAULT_HEIGHT       = 1080
    BUTTON_WIDTH         = 240
    BUTTON_HEIGHT        = 70
    BUTTON_TOP_OFFSET    = 220
    BUTTON_LEFT_OFFSET   = 1380
    BUTTON_SPACING       = 44

    def __init__(self, default_language="de"):
        super().__init__()
        # Set window title using translator
        self.translator = Translator(default=default_language)
        self.setWindowTitle(self.translator.tr("window_title"))
        self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
        self.setAutoFillBackground(False)
        self.bg_pixmap = QPixmap(
            "/home/frank/Dokumente/CSNova/assets/media/csNova_background_start.png"
        )

        self.pref_window = None  # Track preferences window
        self._create_ui()
        self._retranslate_and_position()

    def _create_ui(self):
        # Button keys for translation
        self.button_keys = [
            "btn_new_project",
            "btn_load_project",
            "btn_settings",
            "btn_help",
            "btn_exit"
        ]
        self.buttons = []
        for key in self.button_keys:
            btn = QPushButton(parent=self)
            shadow = QGraphicsDropShadowEffect(btn)
            shadow.setBlurRadius(10)
            shadow.setXOffset(4)
            shadow.setYOffset(4)
            shadow.setColor(QColor(0, 0, 0, 80))
            btn.setGraphicsEffect(shadow)
            self.buttons.append(btn)

        # Connect settings button
        self.buttons[2].clicked.connect(self._open_preferences)

        # Connect placeholder buttons
        self.buttons[0].clicked.connect(self._new_project_placeholder)
        self.buttons[1].clicked.connect(self._load_project_placeholder)
        self.buttons[3].clicked.connect(self._help_placeholder)

        # Connect exit button
        self.buttons[4].clicked.connect(self._exit_application)

    def _open_preferences(self):
        # Open preferences window only if not already open
        if self.pref_window is None or not self.pref_window.isVisible():
            self.pref_window = PreferencesWindow(self)
            self.pref_window.show()
        else:
            self.pref_window.raise_()
            self.pref_window.activateWindow()

    def _new_project_placeholder(self):
        print("Preparing new project...")

    def _load_project_placeholder(self):
        print("Preparing to load project...")

    def _help_placeholder(self):
        print("Preparing help function...")

    def _exit_application(self):
        QApplication.instance().quit()

    def _on_language_changed(self, code):
        self.translator.set_language(code)
        self._retranslate_and_position()

    def _retranslate_and_position(self):
        # Update button texts and window title
        for key, btn in zip(self.button_keys, self.buttons):
            btn.setText(self.translator.tr(key))
        self.setWindowTitle(self.translator.tr("window_title"))
        self.update_button_positions()

    def paintEvent(self, event):
        # Draw background image scaled and centered
        painter = QPainter(self)
        rect = self.contentsRect()
        w, h = rect.width(), rect.height()
        pw, ph = self.bg_pixmap.width(), self.bg_pixmap.height()
        scale = max(w / pw, h / ph)
        sw, sh = pw * scale, ph * scale
        x_off = rect.x() + (w - sw) / 2
        y_off = rect.y() + (h - sh) / 2
        painter.drawPixmap(
            int(x_off), int(y_off),
            int(sw),   int(sh),
            self.bg_pixmap
        )
        super().paintEvent(event)

    def resizeEvent(self, event):
        # Update button positions on resize
        self.update_button_positions()
        super().resizeEvent(event)

    def update_button_positions(self):
        # Dynamically position and style buttons
        rect = self.contentsRect()
        w, h = rect.width(), rect.height()
        pw, ph = self.bg_pixmap.width(), self.bg_pixmap.height()
        scale = max(w / pw, h / ph)
        sw, sh = pw * scale, ph * scale
        x_off = rect.x() + (w - sw) / 2 + self.BUTTON_LEFT_OFFSET * scale
        y_off = rect.y() + (h - sh) / 2 + self.BUTTON_TOP_OFFSET  * scale
        bw      = int(self.BUTTON_WIDTH   * scale)
        bh      = int(self.BUTTON_HEIGHT  * scale)
        spacing = int(self.BUTTON_SPACING * scale)
        font_px = max(10, int(bh * 0.4))
        style = load_button_style(font_px)  # Use the imported style loader
        for i, btn in enumerate(self.buttons):
            x = int(x_off)
            y = int(y_off + i * (bh + spacing))
            btn.setGeometry(x, y, bw, bh)
            btn.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow(default_language="de")
    window.show()
    sys.exit(app.exec())
```

#### 6.2.1 Translator (translator.py)

```python
# core/translator.py

from core.translations import TRANSLATIONS, LANGUAGES

class Translator:
    def __init__(self, default="de"):
        self.lang = default if default in LANGUAGES else LANGUAGES[0]

    def set_language(self, lang_code):
        if lang_code in TRANSLATIONS:
            self.lang = lang_code

    def tr(self, key):
        return TRANSLATIONS[self.lang].get(
            key, TRANSLATIONS["en"].get(key, key)
        )
```

#### 6.2.2 Styles (style_utils.py)

```python
import os

def load_button_style(font_size):
    """
    Load button style from external QSS file and inject dynamic font size.
    """
    style_path = "/home/frank/Dokumente/CSNova/styles/button_style.qss"
    if not os.path.exists(style_path):
        # Fallback style if file is missing
        return f"""
            QPushButton {{
                background-color: #d4c29c;
                color: #1a1a1a;
                font-size: {font_size}px;
                border: 2px solid #8b7d5c;
                border-radius: 10px;
                border-style: outset;
            }}
            QPushButton:hover {{
                background-color: #e8d9b5;
                border-color: #5c5138;
            }}
            QPushButton:pressed {{
                background-color: #c0aa7a;
                border-style: inset;
            }}
        """
    with open(style_path, "r") as f:
        style = f.read()
    # Replace placeholder for font size if present
    return style.replace("{font_size}", str(font_size))
```

#### 6.2.3 Buttons (buttons.qss)

```text
QPushButton {
    background-color: #d4c29c;
    color: #1a1a1a;
    font-size: 18px;
    border: 2px solid #8b7d5c;
    border-radius: 10px;
    border-style: outset;
}
QPushButton:hover {
    background-color: #e8d9b5;
    border-color: #5c5138;
}
QPushButton:pressed {
    background-color: #c0aa7a;
    border-style: inset;
}
```

### 6.3 Preferenzen (preferences.py)

```python
from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout
)
from core.translations import LANGUAGES, TRANSLATIONS
from config.settings import load_settings, save_settings

class PreferencesWindow(QDialog):
    DEFAULT_WIDTH  = 400
    DEFAULT_HEIGHT = 200

    LANGUAGE_NAMES = {
        "de": "Deutsch",
        "en": "English",
        "fr": "Français",
        "es": "Español"
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.translator = parent.translator
        self.settings   = load_settings()
        self.original_language = self.translator.lang

        self.setWindowTitle(self.translator.tr("menu_settings"))
        self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)

        self._init_ui()
        self._load_values()

    def _init_ui(self):
        self.lang_label = QLabel(self.translator.tr("menu_language"), self)

        self.lang_combo = QComboBox(self)
        for code in LANGUAGES:
            name = self.LANGUAGE_NAMES.get(code, code)
            self.lang_combo.addItem(name, userData=code)

        self.lang_combo.currentIndexChanged.connect(self._on_language_changed)

        self.ok_button     = QPushButton(self)
        self.cancel_button = QPushButton(self)

        self.ok_button.clicked.connect(self._on_ok)
        self.cancel_button.clicked.connect(self._on_cancel)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.ok_button)
        btn_layout.addWidget(self.cancel_button)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.lang_label)
        main_layout.addWidget(self.lang_combo)
        main_layout.addLayout(btn_layout)

    def _load_values(self):
        lang = self.settings.get("language", LANGUAGES[0])
        idx  = LANGUAGES.index(lang) if lang in LANGUAGES else 0
        self.lang_combo.setCurrentIndex(idx)
        self._update_ui_texts()

    def _on_language_changed(self):
        index = self.lang_combo.currentIndex()
        code = self.lang_combo.itemData(index)
        self.translator.set_language(code)
        self._update_ui_texts()

    def _update_ui_texts(self):
        self.setWindowTitle(self.translator.tr("menu_settings"))
        self.lang_label.setText(self.translator.tr("menu_language"))
        self.ok_button.setText(self.translator.tr("action_save"))
        self.cancel_button.setText(self.translator.tr("action_cancel"))

    def _on_ok(self):
        index = self.lang_combo.currentIndex()
        code = self.lang_combo.itemData(index)
        self.settings["language"] = code
        save_settings(self.settings)
        if self.parent() and hasattr(self.parent(), "_on_language_changed"):
            self.parent()._on_language_changed(code)
        self.accept()

    def _on_cancel(self):
        self.translator.set_language(self.original_language)
        if self.parent() and hasattr(self.parent(), "_on_language_changed"):
            self.parent()._on_language_changed(self.original_language)
        self.reject()age_changed(self.original_language)
        self.reject()
```

### 6.4 Translation (translation.py)

```python
from pathlib import Path
import json

LANGUAGES = ["de", "en", "fr", "es"]
TRANSLATIONS = {}

for lang in LANGUAGES:
    path = Path(__file__).parent / "translations" / f"{lang}.json"
    with open(path, "r", encoding="utf-8") as f:
        TRANSLATIONS[lang] = json.load(f)
```

#### 6.4.1 de.json

```json
{
  "btn_new_project":   "Neues Projekt",
  "btn_load_project":  "Projekt laden …",
  "btn_settings":      "Einstellungen",
  "btn_help":          "Hilfe/Tutorial",
  "btn_exit":          "Beenden",
  "menu_file":         "Datei",
  "menu_edit":         "Bearbeiten",
  "menu_help":         "Hilfe",
  "menu_settings":     "Einstellungen",
  "menu_language":     "Sprache",
  "action_new":        "Neu",
  "action_open":       "Öffnen",
  "action_save":       "Speichern",
  "action_exit":       "Beenden",
  "tab_project":       "Projekt",
  "tab_character":     "Charaktere",
  "tab_scene":         "Szenen",
  "btn_save":          "Speichern",
  "tooltip_exit":      "Programm beenden",
  "action_cancel":     "Abbrechen"
}
```

#### 6.4.2 en.json

```json
{
        "btn_new_project":   "New Project",
        "btn_load_project":  "Open Project …",
        "btn_settings":      "Settings",
        "btn_help":          "Help/Tutorial",
        "btn_exit":          "Exit",
        "menu_file":         "File",
        "menu_edit":         "Edit",
        "menu_help":         "Help",
        "menu_settings":     "Settings",
        "menu_language":     "Language",
        "action_new":        "New",
        "action_open":       "Open",
        "action_save":       "Save",
        "action_exit":       "Exit",
        "tab_project":       "Project",
        "tab_character":     "Characters",
        "tab_scene":         "Scenes",
        "btn_save":          "Save",
        "tooltip_exit":      "Exit application",
        "action_cancel":     "Cancel"
    }
```

#### 6.4.3 fr.json

```json
{
        "btn_new_project":   "Nouveau projet", 
        "btn_load_project":  "Ouvrir projet …",
        "btn_settings":      "Paramètres",
        "btn_help":          "Aide/Tutoriel",
        "btn_exit":          "Quitter",
        "menu_file":         "Fichier",
        "menu_edit":         "Éditer",
        "menu_help":         "Aide",
        "menu_settings":     "Paramètres",
        "menu_language":     "Langue",
        "action_new":        "Nouveau",
        "action_open":       "Ouvrir",
        "action_save":       "Enregistrer",
        "action_exit":       "Quitter",
        "tab_project":       "Projet",
        "tab_character":     "Personnages",
        "tab_scene":         "Scènes",
        "btn_save":          "Enregistrer",
        "tooltip_exit":      "Quitter l'application",
        "action_cancel":     "Annuler"
    }
```

#### 6.4.4 es.json

```json
{
        "btn_new_project":   "Nuevo proyecto",
        "btn_load_project":  "Abrir proyecto …",
        "btn_settings":      "Configuración",
        "btn_help":          "Ayuda/Tutorial",
        "btn_exit":          "Salir",
        "menu_file":         "Archivo",
        "menu_edit":         "Editar",
        "menu_help":         "Ayuda",
        "menu_settings":     "Configuración",
        "menu_language":     "Idioma",
        "action_new":        "Nuevo",
        "action_open":       "Abrir",
        "action_save":       "Guardar",
        "action_exit":       "Salir",
        "tab_project":       "Proyecto",
        "tab_character":     "Personajes",
        "tab_scene":         "Escenas",
        "btn_save":          "Guardar",
        "tooltip_exit":      "Salir de la aplicación",
        "action_cancel":     "Cancelar"
    }
```

#### 6.4.5 Spracheinstellung (user_settings.json)

```json
{
  "language": "en"
}
```

### 6.5 Datenbank (database.py)

```json
# database.py
import sqlite3
from config.dev import DB_PATH  
from core.tables.gender_data import data_gender
from core.tables.sex_orientation_data import sex_orientation_data

# Importiere die Tabellenmodule
from core.tables import (
    character_main,
    gender,
    sex_orientation,
    character_psychological_profile,
    character_origin,
    character_education,
    character_personality,
    character_appearance_main,
    character_appearance_detail,
    project,
    project_storylines,
    project_chapters,
    project_chapters_scenes,
    project_scenes_objects,
    project_scenes_places
)

def init_schema():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            # Enable foreign key support
            cursor.execute("PRAGMA foreign_keys = ON")

            # Initialize tables
            for module in [
                character_main,
                gender,
                sex_orientation,
                character_psychological_profile,
                character_origin,
                character_education,
                character_personality,
                character_appearance_main,
                character_appearance_detail,
                project,
                project_storylines,
                project_chapters,
                project_chapters_scenes,
                project_scenes_objects,
                project_scenes_places
            ]:
                module.create_table(cursor)
            
            # Insert seed data
            data_gender(cursor)
            sex_orientation_data(cursor)
            conn.commit()
    except Exception as e:
        print(f"An error occurred during database initialization: {e}")
```