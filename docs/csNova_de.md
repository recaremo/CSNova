# Codices Scriptoria Nova (CSNova)

## 1. Ziel

Entwicklung einer plattformübergreifenden Desktop‑Anwendung (Linux, Windows, macOS) für Autor:innen zur Planung, Organisation und kreativen Unterstützung von Buchprojekten. Die Software kombiniert datenbankgestützte Projektverwaltung, moderne GUI, integrierte KI‑Features und einen individuellen Reader, der multimediale Inhalte, Animationen und 3D-Modelle darstellen kann.

### 1.1 KI-Anweisungen

1. Verzichte auf die Simulation von Gefühlen, Empathie und Humor.  
2. Antworten sind rational, sachlich und ausschließlich auf die Frage bezogen.  
3. Füge keine Inhalte hinzu und verzichte auf Vorschläge, wenn nicht explizit dazu aufgefordert: "Mache mir alternative Vorschläge"  
4. Füge der Seite keine Inhalte hinzu. Alle Antworten, Korrekturen und Veränderungsvorschläge erfolgen ausschließlich hier im Chat.  
5. Die im Punkt 4 vorgeschlagenen Änderungen werden der Seite nur hinzugefügt, wenn eine explizite Aufforderung erfolgt: "Füge die Änderungen der Seite hinzu"

## 2. Hauptfunktionen

- Projektverwaltung: Anlegen, Bearbeiten und Archivieren von Buchprojekten  
- Charakterdatenbank: Haupt- und Nebentabellen (Physiognomie, Psychologie, Ausbildung, Herkunft, …)  
- Kapitel- & Szeneverwaltung inkl. Handlungsstränge, Zeitlinien, Orte, Gegenstände  
- Beziehungs- und Mindmap‑Modul (Charaktere, Gruppen, Verbindungen)  
- Statistiken & Übersichten (Steckbriefe, ToDo‑Listen, Fortschritt)  
- Integrierte Schreib‑Tipps, Genre‑Guides, Quellenverwaltung, Brainstorming‑Tools  
- Multimedia‑Integration (Bilder, Audio, Video, Animationen)  
- Export in diverse Formate (EPUB, PDF, HTML, eigenes Reader‑Format)  
- Custom Multimedia‑Reader mit responsivem Layout pro Plattform  
- KI‑Interviewfunktion für Figurenentwicklung, Plotideen, Textanalyse  
- Sprachen: Deutsch (Standard), Englisch, Französisch, Spanisch  
- Rechtschreibprüfung: Deutsch, Englisch  
- Dynamische Sprachauswahl mit automatischer Anpassung aller Menü- und UI-Texte

## 3. Technische Basis

- Programmiersprache: Python (für Logik, KI‑Anbindung, Datenbankzugriffe)  
- GUI‑Framework: PySide6 (Qt6)  
- Datenbank: SQLite (später erweiterbar auf PostgreSQL/MySQL)  
- Deployment: PyInstaller → eigenständige Builds für Linux, Windows, macOS  
- KI‑Integration: API‑Anbindung mit asynchronem Event‑Handling  
- Exportmodule: ebooklib, reportlab, weasyprint  
- Multimedia: QtMultimedia, QWebEngineView/QML für den Reader  
- UI-Übersetzung: Menütexte als Variablen, Sprachdatenbank (Tabelle), dynamische Einstellungen

## 4. Projektfahrplan & Fortschritt

### Übersicht

- Installation  
- GUI‑Grundstruktur aufsetzen  
- Datentabellen anlegen  
- Datenbankverbindung testen  
- Beispielprojekt einrichten  
- Exportfunktion vorbereiten  
- KI‑Modul initialisieren  
- Sprachmodul vorbereiten  

### 4.1 Installation

- Projektname „Codices Scriptoria Nova“ urheberrechtlich geprüft  
- PNG-Logo erstellt  
- Entwicklungsumgebung: Linux Mint, Visual Studio Code (englisch), QT Designer, QT Design Studio, GIMP  
- Sprache: Python  
- VSC installiert, Python-AddOn eingebunden  
- AddOns:  
  - Black Formatter  
  - Github Pull Requests  
  - isort  
  - Jupyter  
  - Pylance  
  - Python Debugger  
  - Python Environments  
- GitHub-Verbindung aktiv  
- venv eingerichtet, Tools installiert:  
  - pyside6  
  - ebooklib  
  - weasyprint  
  - reportlab  
  - requests  
  - asyncio  
  - libxcb-cursor0  

```text
├── ./ai
│   ├── ./ai/analysis.py
│   ├── ./ai/brainstorming.py
│   ├── ./ai/interview.py
│   ├── ./ai/modelle
│   └── ./ai/prompts
├── ./assets
│   ├── ./assets/icons
│   └── ./assets/media
│       ├── ./assets/media/csNova_background_middle.png
│       ├── ./assets/media/csNova_background_start.png
│       └── ./assets/media/csNova_logo_main.png
├── ./cli.py
├── ./config
│   ├── ./config/dev.py
│   ├── ./config/prod.py
│   ├── ./config/__pycache__
│   │   ├── ./config/__pycache__/dev.cpython-312.pyc
│   │   └── ./config/__pycache__/settings.cpython-312.pyc
│   ├── ./config/settings.py
│   └── ./config/user_settings.json
├── ./core
│   ├── ./core/database.py
│   ├── ./core/logic
│   │   └── ./core/logic/crud.py
│   ├── ./core/models
│   │   ├── ./core/models/character.py
│   │   ├── ./core/models/project.py
│   │   └── ./core/models/scene.py
│   ├── ./core/__pycache__
│   │   ├── ./core/__pycache__/database.cpython-312.pyc
│   │   └── ./core/__pycache__/translations.cpython-312.pyc
│   ├── ./core/services
│   └── ./core/translations.py
├── ./data
│   └── ./data/csnova.db
├── ./docs
│   ├── ./docs/ai_prompt_background_l.txt
│   ├── ./docs/ai_prompt_background_s.txt
│   ├── ./docs/ai_prompt_background_xl.txt
│   ├── ./docs/ai_prompt_logo_big.txt
│   ├── ./docs/ai_prompt_logo_small.txt
│   ├── ./docs/csNova_de.rst
│   ├── ./docs/csNova_en.rst
│   ├── ./docs/csNova_es.rst
│   └── ./docs/csNova_fr.rst
├── ./export
│   ├── ./export/csnova_export.py
│   ├── ./export/epub_export.py
│   ├── ./export/html_export.py
│   └── ./export/pdf_export.py
├── ./gui
│   ├── ./gui/main_window.py
│   ├── ./gui/__pycache__
│   │   ├── ./gui/__pycache__/main_window.cpython-312.pyc
│   │   └── ./gui/__pycache__/start_window.cpython-312.pyc
│   ├── ./gui/start_window.py
│   ├── ./gui/styles
│   │   └── ./gui/styles/buttons.qss
│   ├── ./gui/tabs
│   │   ├── ./gui/tabs/character_tab.py
│   │   ├── ./gui/tabs/project_tab.py
│   │   ├── ./gui/tabs/__pycache__
│   │   │   └── ./gui/tabs/__pycache__/project_tab.cpython-312.pyc
│   │   └── ./gui/tabs/scene_tab.py
│   ├── ./gui/ui
│   │   └── ./gui/ui/start_window.ui
│   └── ./gui/widgets
│       ├── ./gui/widgets/dialog.py
│       └── ./gui/widgets/listview.py
├── ./license.md
├── ./main.py
├── ./readme.md
├── ./setup.py
└── ./tests
└── ./tests/conftest.py

### 4.2 GUI

* GUI-Framework: PySide6 (Qt6)
* Hauptprogramm: main.py
* Startfenster: start_window.py
* Referenzen: preferences.py
* Übersetzungen: translation.py
* Tabs: character_tab.py, project_tab.py, scene_tab.py
* Widgets: [dialog.py](https://dialog.py), [listview.py](https://listview.py)
* Stylesheets: styles/
* Layout: responsiv, plattformabhängig
* Ziel: intuitive Bedienung, modulare Erweiterbarkeit

#### 4.2.1 Hauptprogramm

```python
import sys
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings
from gui.start_window import StartWindow

def main():
    init_schema()
    settings = load_settings()
    language = settings.get("language", "de")

    app = QApplication(sys.argv)
    # Übergebe Default-Sprache an das Startfenster
    window = StartWindow(default_language=language)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


#### 4.2.1 Startfenster (start_window.py)

In diesem Abschnitt wird das Startfenster so konfiguriert, dass das gesamte Fenster-Background das Bild  
`/home/frank/Dokumente/CSNova/assets/media/csNova_background_start.png` verwendet.

```python
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPalette, QBrush, QPixmap, QPainter
from PySide6.QtCore import Qt, QTimer
from core.translations import LANGUAGES, TRANSLATIONS
from gui.preferences import PreferencesWindow
import sys

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
        self.setWindowTitle("Codices Scriptoria Nova (CSNova)")
        self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
        self.setAutoFillBackground(False)
        self.bg_pixmap = QPixmap(
            "/home/frank/Dokumente/CSNova/assets/media/csNova_background_start.png"
        )

        self.translator = Translator(default=default_language)
        self._create_ui()
        QTimer.singleShot(0, self._retranslate_and_position)

    def _create_ui(self):
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

        # Einstellungen-Button verbinden
        self.buttons[2].clicked.connect(self._open_preferences)

    def _open_preferences(self):
        self.pref_window = PreferencesWindow(self)
        self.pref_window.show()

    def _on_language_changed(self, code):
        self.translator.set_language(code)
        self._retranslate_and_position()

    def _retranslate_and_position(self):
        for key, btn in zip(self.button_keys, self.buttons):
            btn.setText(self.translator.tr(key))
        self.update_button_positions()

    def paintEvent(self, event):
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
        self.update_button_positions()
        super().resizeEvent(event)

    def update_button_positions(self):
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
        for i, btn in enumerate(self.buttons):
            x = int(x_off)
            y = int(y_off + i * (bh + spacing))
            btn.setGeometry(x, y, bw, bh)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: #d4c29c;
                    color: #1a1a1a;
                    font-size: {font_px}px;
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
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow(default_language="de")
    window.show()
    sys.exit(app.exec())


#### 4.2.2 Preferenzen (preferences.py)

```python
from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout
)
from core.translations import LANGUAGES, TRANSLATIONS
from config.settings import load_settings, save_settings

class PreferencesWindow(QDialog):
    # Größe des Dialogs
    DEFAULT_WIDTH  = 400
    DEFAULT_HEIGHT = 200

    # Anzeige-Namen in der ComboBox (Deutsch-Namen)
    LANGUAGE_NAMES = {
        "de": "Deutsch",
        "en": "Englisch",
        "fr": "Französisch",
        "es": "Spanisch"
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.translator = parent.translator
        self.settings   = load_settings()

        # Dialog einstellen
        self.setWindowTitle(self.translator.tr("menu_settings"))
        self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)

        # UI aufbauen
        self._init_ui()
        self._load_values()

    def _init_ui(self):
        # Label „Sprache“
        self.lang_label = QLabel(self.translator.tr("menu_language"), self)

        # ComboBox mit German-Namen, userData = Sprachcode
        self.lang_combo = QComboBox(self)
        for code in LANGUAGES:
            name = self.LANGUAGE_NAMES.get(code, code)
            self.lang_combo.addItem(name, userData=code)

        # Bei Änderung sofort umschalten
        self.lang_combo.currentIndexChanged.connect(self._on_language_changed)

        # OK und Abbrechen
        self.ok_button     = QPushButton(
            self.translator.tr("action_save"), self
        )
        self.cancel_button = QPushButton(
            self.translator.tr("action_cancel"), self
        )

        self.ok_button.clicked.connect(self._on_ok)
        self.cancel_button.clicked.connect(self.reject)

#### 4.2.3 Translation (translation.py)


### 4.3 Tabellen

Auflistungen der erstellten Tabellen in Python:

#### 4.3.1 Haupttabelle: character_main

```python
# Haupttabelle: character_main
cursor.execute("""
CREATE TABLE IF NOT EXISTS character_main (
    character_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    first_name TEXT,
    nick_name TEXT,
    born DATE,
    age INTEGER,
    role TEXT,
    status TEXT,
    gender_ID INTEGER,
    sex_orientation_ID INTEGER,
    notes TEXT
);
""")

##### 4.3.1.1 Referenztabelle: gender

```python
# Referenztabelle: gender
cursor.execute("""
CREATE TABLE IF NOT EXISTS gender (
    gender_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT,
    short_description TEXT
);
""")

##### 4.3.1.2 Referenztabelle: sex_orientation

```python
# Referenztabelle: sex_orientation
cursor.execute("""
CREATE TABLE IF NOT EXISTS sex_orientation (
    sex_orientation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    sex_orientation TEXT,
    short_description TEXT
);
""")

##### 4.3.1.3 Untertabelle: psychological_profile

```python
# Untertabellen (Beispiel: psychological_profile)
cursor.execute("""
CREATE TABLE IF NOT EXISTS psychological_profile (
    profile_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    character_ID INTEGER,
    diagnosis TEXT,
    symptoms TEXT,
    therapy TEXT,
    medication TEXT,
    temperament TEXT,
    values_set TEXT,
    moral_concepts TEXT,
    character_strength TEXT,
    character_weakness TEXT,
    self_image TEXT,
    fears TEXT,
    notes TEXT,
    FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
);
""")

## 5. Programm-Logo

### 5.1 Großes Logo
 
* Motiv: Geöffnetes Buch darüber eine schwebende Hand und Schreibfeder, die in das Buch schreiben. Das Buch ist 45° gegen den Uhrzeigersinn gedreht. Setzt das Buch im Verhältnis 2:1 zur Hand mit der Feder. Das gesamte Motiv ist von einem schlichten, einfachen Rahmen umgeben.  
- Schriftzug: „Codices Scriptoria Nova“ in drei Zeilen  
- „Codices Scriptoria“ in mittelalterlicher Schrift, „C“ und „S“ in Lapislazuli-Blau  
- „Nova“ in moderner Schrift  
- Das Motiv ist auf der linken Seite – der Text befindet sich rechts davon und liegt außerhalb des Rahmens der das Motiv umgibt.  
- Hintergrund: Pergamenttextur mit Gebrauchsspuren  
- Stil: Albrecht Dürer, mittelalterlicher Holzdruck  
- Komposition: Drittelregel oder Goldener Schnitt  
- Besonderheiten: Kleine Unregelmäßigkeiten im Druckbild  

### 5.2 Kleines Logo

- Motiv: Geöffnetes Buch darüber eine schwebende Hand und Schreibfeder, die in das Buch schreiben. Das Buch ist 45° gegen den Uhrzeigersinn gedreht. Setzt das Buch im Verhältnis 2:1 zur Hand mit der Feder. Das gesamte Motiv ist von einem schlichten, einfachen Rahmen umgeben.  
- Schriftzug: „CS” und “Nova“ in zwei Zeilen  
- „CS“ in mittelalterlicher Schrift, „Nova“ in moderner Schrift  
- Das Motiv ist auf der linken Seite – der Text befindet sich rechts davon und liegt außerhalb des Rahmens der das Motiv umgibt.  
- Hintergrund: Pergamenttextur mit Gebrauchsspuren  
- Stil: Albrecht Dürer, mittelalterlicher Holzdruck  
- Komposition: Drittelregel oder Goldener Schnitt  
- Besonderheiten: Kleine Unregelmäßigkeiten im Druckbild  

## 6. Tutorials & Literatur, Quellen

### 6.1 PySide6 & GUI-Entwicklung

- Create GUI Applications with Python & Qt6 – Martin Fitzpatrick  
- Modern UI mit PySide6 – komplette App  
- Install & Setup PySide6 and Qt Designer  
- PySide6 + SQLite integration – Qt‑Dokumentation  

### 6.2 Datenbank & Migration

- SQL für Einsteiger – Michael Kofler  
- SQLite Tutorial – Jacek Artymiak  
- SQLite Crash Course – freeCodeCamp  
- Datenbankmigration mit Alembic – Heise Developer  
- SQLAlchemy Getting Started  

### 6.3 Multimedia & Animation

- Multimedia Programming with Qt – Marco Piccolino  
- QtMultimedia Tutorial – Audio & Video  
- QML Animation Basics – Qt Academy  
- Multimedia & QML – Best Practices  
- PySide6 Animation Tutorial  
- QtMultimedia Docs  

### 6.4 Exportformate & Reader

- Creating EPUBs with ebooklib – Python Publishing Guide  
- PDF-Export mit ReportLab – Python Tutorials  
- HTML-Export mit WeasyPrint – Web2PDF mit CSS  
- Reader-Entwicklung mit QWebEngineView – Qt Blog  
- ebooklib Dokumentation  
- ReportLab User Guide  
- WeasyPrint Docs  

### 6.5 KI-Integration

- Hands-On AI with Python – Packt Publishing  
- OpenAI API Integration – Python Tutorial  
