# Codices Scriptoria Nova (CSNova)

## Projektbeschreibung

CSNova ist eine umfassende Softwarelösung für Romanautor:innen, Drehbuchautor:innen, Game Writer:innen und alle, die komplexe narrative Projekte planen, entwickeln und veröffentlichen möchten.

## Funktionen im Überblick

### Projektverwaltung
- Beliebig viele Bücher und Serien verwalten
- Inhalte zwischen Projekten flexibel übertragen

### Charakterentwicklung
- Grundlagen, Morphologie, Psychologie
- Bilder und 3D-Charaktere
- Beziehungen und soziale Dynamiken
- Biografien, Hintergrundgeschichten, Motivationen
- Entwicklung über Zeit und Ereignisse
- Konflikte, Stärken, Schwächen
- KI-gestützte Vorschläge für realistische Verhaltensweisen und Dialoge

### Kapitel- und Szenenmanagement
- Strukturieren, erfassen und organisieren

### Weltenbau
- Handlungsorte, Gegenstände, Gruppen
- Timeline, Mindmaps und Schreibziele

### Recherche und Quellenverwaltung
- Integrierte Datenbank für Recherchen
- KI-gestützte Quellenanalyse und Generierung:
  - *„Erzeuge eine Tabelle mit wichtigen Theorien zur Quantenphysik von 1900–2025; Name der Entdecker:innen; Veröffentlichungsjahr; Zusammenfassung.“*
  - *„Beschreibung des Ortes XYZ um 1300; Persönlichkeiten; historische Ereignisse; Gebäude.“*

### Storyboard und Drehbucherstellung
- Automatische Generierung aus Kapiteln und Szenen

### Statistische Analyse
- Schreibverhalten, Textumfang, Fortschritt

### Stilistische Unterstützung
- Ich-Perspektive
- Personale und auktoriale Erzählweise
- Neutrale Erzähler:innen

### Interview-Modus
- Geführte Dateneingabe mit Erinnerungsfunktion
- KI-Unterstützung:
  - *„Erstelle ein Bild basierend auf der Charakterbeschreibung.“*
  - *„Was wäre ein realistischer chinesischer Name für diesen Charakter?“*

### Exportformate
- PDF
- EPUB
- CSNova-Readerformat:
  - Unterstützung für multimediale Inhalte, Animationen, Videos und interaktive Elemente
  - Der CSNova-Reader ist Open Source und wird lizenzfrei weitergegeben

### Videotutorials
- Verfügbar in Deutsch, Englisch, Französisch und Spanisch

### Integrierte Textverarbeitung
- Alle Daten direkt anzeigen und bearbeiten
- Copy/Paste ohne Programmwechsel

## Optional: Erweiterungen

### Kollaboration
- Gemeinsames Schreiben, Freigabe für Lektor:innen oder Co-Autor:innen

### Datensicherheit
- Lokale Speicherung, Backup-Funktion, Cloud-Optionen

### Systemvoraussetzungen
- Verfügbar für Windows, macOS und Linux
- Mobile Version in Entwicklung
- Mehrsprachige Benutzeroberfläche: Deutsch, Englisch, Französisch und Spanisch


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
├── ai/
│   ├── analysis.py
│   ├── brainstorming.py
│   ├── interview.py
│   ├── modelle/
│   └── prompts/
├── assets/
│   ├── icons/
│   └── media/
│       ├── csNova_background_start.png
│       └── csNova_logo_main.png
├── cli.py
├── config/
│   ├── dev.py
│   ├── prod.py
│   ├── __pycache__/
│   │   ├── dev.cpython-312.pyc
│   │   └── settings.cpython-312.pyc
│   ├── settings.py
│   └── user_settings.json
├── core/
│   ├── database.py
│   ├── logic/
│   │   └── crud.py
│   ├── models/
│   │   ├── character.py
│   │   ├── project.py
│   │   └── scene.py
│   ├── __pycache__/
│   │   ├── database.cpython-312.pyc
│   │   ├── translations.cpython-312.pyc
│   │   └── translator.cpython-312.pyc
│   ├── services/
│   ├── tables/
│   │   ├── character_appearance_detail.py
│   │   ├── character_appearance_main.py
│   │   ├── character_education.py
│   │   ├── character_main.py
│   │   ├── character_origin.py
│   │   ├── character_personality.py
│   │   ├── character_psychological_profile.py
│   │   ├── gender_data.py
│   │   ├── gender.py
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── character_appearance_detail.cpython-312.pyc
│   │   │   ├── character_appearance_main.cpython-312.pyc
│   │   │   ├── character_education.cpython-312.pyc
│   │   │   ├── character_main.cpython-312.pyc
│   │   │   ├── character_origin.cpython-312.pyc
│   │   │   ├── character_personality.cpython-312.pyc
│   │   │   ├── character_psychological_profile.cpython-312.pyc
│   │   │   ├── gender.cpython-312.pyc
│   │   │   ├── gender_data.cpython-312.pyc
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── sex_orientation.cpython-312.pyc
│   │   │   └── sex_orientation_data.cpython-312.pyc
│   │   ├── sex_orientation_data.py
│   │   └── sex_orientation.py
│   ├── translations/
│   │   ├── de.json
│   │   ├── en.json
│   │   ├── es.json
│   │   └── fr.json
│   ├── translations.py
│   └── translator.py
├── data/
│   └── csnova.db
├── docs/
│   └── csNova_de.md
├── export/
│   ├── csnova_export.py
│   ├── epub_export.py
│   ├── html_export.py
│   └── pdf_export.py
├── gui/
│   ├── preferences.py
│   ├── __pycache__/
│   │   ├── main_window.cpython-312.pyc
│   │   ├── preferences.cpython-312.pyc
│   │   └── start_window.cpython-312.pyc
│   ├── start_window_old.py
│   ├── start_window.py
│   ├── styles/
│   │   └── buttons.qss
│   ├── tabs/
│   │   ├── character_tab.py
│   │   ├── project_tab.py
│   │   ├── __pycache__/
│   │   │   └── project_tab.cpython-312.pyc
│   │   └── scene_tab.py
│   └── widgets/
│       ├── dialog.py
│       └── listview.py
├── license.md
├── main.py
├── readme.md
├── setup.py
└── tests/
    └── conftest.py
```

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

## 5. Tabellen

```python
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
    character_appearance_detail
)

def init_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fremdschlüssel aktivieren
    cursor.execute("PRAGMA foreign_keys = ON")

    # Tabellen initialisieren
    for module in [
        character_main,
        gender,
        sex_orientation,
        character_psychological_profile,
        character_origin,
        character_education,
        character_personality,
        character_appearance_main,
        character_appearance_detail
    ]:
        module.create_table(cursor)
    
    # Seed-Daten einfügen
    data_gender(cursor)
    data_sex_orientation(cursor)

    conn.commit()
    conn.close()
```

### 5.1 character_main.py

```python
# character_main.py
# table: character_main
# description: base stats for a character
# access to the tables: gender.py, sex_orientation.py
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_main (
        character_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        main_character BOOL,
        group_member TEXT,
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
```

#### 5.1.1 gender.py

```python
# gender.py
# table: gender_data.py
# description: the different types of gender that can be assigned to a character
# access from the tables: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gender (
        gender_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        short_description TEXT
    );
    """)
```
#### gender_data.py

```python
# gender_data.py
# description: data for gender.py

def data_gender(cursor):
    cursor.executemany("""
        INSERT INTO gender (gender, short_description)
        VALUES (?, ?)
    """, [
        #Data
    ])
```

#### 5.1.2 sex_orientation.py

```python
# sex_orientation.py
# table: sex_orientation_data.py
# description: the different types of sexual orientation that can be assigned to a character
# access from the tables: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sex_orientation (
        sex_orientation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        sex_orientation TEXT,
        short_description TEXT
    );
    """)
```
#### sex_orientation_data.py

```python
# sex_orientation_data.py
# description: data for sex_orientation.py

def sex_orientation_data(cursor):
    cursor.executemany("""
        INSERT INTO sex_orientation (sex_orientation, short_description)
        VALUES (?, ?)
    """, [
        ('Heterosexual', 'Attracted to the opposite gender'),
        ('Homosexual', 'Attracted to the same gender'),
        ('Bisexual', 'Attracted to both genders'),
        ('Asexual', 'Experiences little or no sexual attraction'),
        ('Pansexual', 'Attracted to people regardless of gender'),
        ('Queer', 'Non-normative sexual orientation'),
        ('Questioning', 'Exploring or unsure about sexual orientation')
    ])
```

#### 5.1.3 character_origin.py

```python
# character_origin.py
# table: subtable for character_main
# description: family and origin of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_origin (
        origin_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        father TEXT,
        mother TEXT,
        reference_person TEXT,
        siblings TEXT,
        birthplace TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

#### 5.1.4 character_education.py

```python
# character_education.py
# table: subtable for character_main
# description: educations of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_education (
        education_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        school TEXT,
        university TEXT,
        job_education TEXT,
        autodidactic TEXT,
        job TEXT,
        art_music TEXT,
        sport TEXT,
        technology TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

#### 5.1.5 character_personality.py

```python
# character_personality.py
# table: subtable for character_main
# description: personality of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_personality (
        personality_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        pos_characteristic TEXT,
        neg_characteristic TEXT,
        fears TEXT,
        weaknesses TEXT,
        strengths TEXT,
        talents TEXT,
        char_values TEXT,
        beliefs TEXT,
        life_goals TEXT,
        motivation TEXT,
        behavior TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

#### 5.1.6 character_psychological_profile.py

```python
# character_psychological_profile.py
# table: subtable for character_main
# description: psychological profil of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_psychological_profile (
        psychological_profile_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
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
        longing TEXT,
        anger TEXT,
        joy TEXT,
        stress_situation TEXT,
        motives_fears TEXT,
        duty_desire TEXT,
        ideal_reality TEXT,
        belonging TEXT,
        recognition TEXT,
        self_realization TEXT,
        psychological_control TEXT,
        freedom TEXT,
        love TEXT,
        power TEXT,
        knowledge TEXT,
        revenge TEXT,
        withdrawal TEXT,
        humor TEXT,
        aggression TEXT,
        security TEXT,
        trauma TEXT,
        formative_personality TEXT,
        socialization TEXT,
        norms TEXT,
        taboos TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

#### 5.1.7 character_appearance_main.py

```python
# character_appearance_main.py
# table: subtable for character_main
# description: main appearance of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_appearance_main (
        appearance_main_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        height TEXT,
        body_type TEXT,
        posture TEXT,
        face_shape TEXT,
        eye_shape TEXT,
        eye_color TEXT,
        hair TEXT,
        hair_color TEXT,
        skin TEXT,
        charisma TEXT,
        special_features TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

#### 5.1.8 character_appearance_detail.py

```python
# character_appearance_detail.py
# table: subtable for character_main
# description: more appearance details of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_appearance_detail (
        appearance_detail_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        head TEXT,
        neck TEXT,
        shoulder TEXT,
        arms TEXT,
        hands TEXT,
        finger TEXT,
        chest TEXT,
        hips_waist TEXT,
        buttocks TEXT,
        legs TEXT,
        feet TEXT,
        toes TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

#### 5.1.9 character_groups.py

```python
# character_groups.py
# table: subtable for character_main
# description: character memberchip in a group
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_groups (
        character_groups_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_groups_title TEXT,
        character_groups_description TEXT
    );
    """)
```

### 5.2 Projektdatenbank

#### 5.2.1 project.py

```python
# project.py
# table: project
# description: central project database, main statistic of work done
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_premise TEXT,
        project_words_count_goal INTEGER,
        project_words_count_days INTEGER,  
        project_deadlines DATE,
        project_chapters INTEGER,
        project_scenes INTEGER,
        project_story_lines INTEGER,
        project_main_characters INTEGER,
        project_supporting_characters INTEGER,
        project_groups_characters INTEGER,
        project_story_places INTEGER,
        project_story_opjects INTEGER,
        project_timeline TEXT,
        project_notes TEXT

    );
    """)
```

#### 5.2.2 project_storylines.py

```python
# project_storylines.py
# table: project_storylines
# description: storylines in project
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_storylines (
        project_storylines_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_storylines_premise TEXT,
        porject_storylines_title TEXT,
        project_storylines_description TEXT,
        project_storylines_notes TEXT,
    );
    """)
```

#### 5.2.3 project_chapters.py

```python
# project_chapters.py
# # table: project_chapters
# description: chapters inside a project
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_chapters (
        project_chapter_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_ID INTEGER NOT NULL,
        project_chapters_premise TEXT,
        project_chapters_titel TEXT,
        FOREIGN KEY(project_ID) REFERENCES project(project_ID)
    );
    """)
```

#### 5.2.4 project_chapter_scenes.py

```python
# project_chapter_scenes.py
# # table: project_chapter_scenes
# description: scenes inside a chapter
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_chapters_scenes (
        project_chapters_scenes_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_chapters_ID INTEGER NOT NULL,
        project_chapters_scenes_premise TEXT,
        project_chapters_scenes_titel TEXT,
        project_chapters_scenes_main_characters TEXT,
        project_chapters_scenes_supporting_character TEXT,
        project_chapters_scenes_places TEXT,
        project_chapters_scenes_text TEXT,
        FOREIGN KEY(project_chapters_ID) REFERENCES project_chapters(project_chapters_ID)
    );
    """)
```

##### 5.2.4.1 project_scenes_objects.py

```python
# project_scenes_objects.py
# table: project_scenes_sobjects
# description: objects can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_scenes_objects (
        project_scenes_object_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_chapters_scenes_ID INTEGER,
        project_scenes_objects_titel TEXT,
        project_scenes_objects_description TEXT,
        FOREIGN KEY(project_chapters_scenes_ID ) REFERENCES  project_chapters_scenes (project_chapters_scenes_ID)
    );
    """)
```

##### 5.2.4.2 project_scenes_places.py

```python
# project_scenes_places.py
# table: project_scenes_places
# description: places can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_scenes_places (
        scenes_places_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_chapters_scenes_ID INTEGER,
        scenes_places_titel TEXT,
        scenes_places_description TEXT,
        FOREIGN KEY(project_chapters_scenes_ID ) REFERENCES  project_chapters_scenes (project_chapters_scenes_ID)
    );
    """)
```

## 6. - Programmecode

### 6.1 Hauptprogramm (main.py)

```python
import sys
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings, save_settings

from gui.start_window import StartWindow

def main():
    init_schema()
    settings = load_settings()
    language = settings.get("language", "de")

    app = QApplication(sys.argv)
    # Übergebe Default-Sprache an das Startfenster
    window = StartWindow(default_language=language)
    window.show()
    app.exec()

    # Sprache speichern, falls geändert
    settings["language"] = window.translator.lang
    save_settings(settings)

if __name__ == "__main__":
    main()

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

### 6.2 Startfenster (start_window.py)

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
        self.reject()

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

#### 6.4.1 de.json

```json
{
  "btn_new_project": "Neues Projekt",
  "btn_load_project": "Projekt laden …",
  "btn_settings": "Einstellungen",
  "btn_help": "Hilfe/Tutorial",
  "btn_exit": "Beenden",
  "menu_file": "Datei",
  "menu_edit": "Bearbeiten",
  "menu_help": "Hilfe",
  "menu_settings": "Einstellungen",
  "menu_language": "Sprache",
  "action_new": "Neu",
  "action_open": "Öffnen",
  "action_save": "Speichern",
  "action_exit": "Beenden",
  "tab_project": "Projekt",
  "tab_character": "Charaktere",
  "tab_scene": "Szenen",
  "btn_save": "Speichern",
  "tooltip_exit": "Programm beenden",
  "action_cancel": "Abbrechen"
}

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
        "action_cancel": "Cancel"
    }

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
        "action_cancel": "Cancelar"
    }

#### 6.4.5 Spracheinstellung (user_settings.json)

```json
{
  "language": "en"
}

## 7. Tutorials & Literatur, Quellen

### 7.1 PySide6 & GUI-Entwicklung

- Create GUI Applications with Python & Qt6 – Martin Fitzpatrick  
- Modern UI mit PySide6 – komplette App  
- Install & Setup PySide6 and Qt Designer  
- PySide6 + SQLite integration – Qt‑Dokumentation  

### 7.2 Datenbank & Migration

- SQL für Einsteiger – Michael Kofler  
- SQLite Tutorial – Jacek Artymiak  
- SQLite Crash Course – freeCodeCamp  
- Datenbankmigration mit Alembic – Heise Developer  
- SQLAlchemy Getting Started  

### 7.3 Multimedia & Animation

- Multimedia Programming with Qt – Marco Piccolino  
- QtMultimedia Tutorial – Audio & Video  
- QML Animation Basics – Qt Academy  
- Multimedia & QML – Best Practices  
- PySide6 Animation Tutorial  
- QtMultimedia Docs  

### 7.4 Exportformate & Reader

- Creating EPUBs with ebooklib – Python Publishing Guide  
- PDF-Export mit ReportLab – Python Tutorials  
- HTML-Export mit WeasyPrint – Web2PDF mit CSS  
- Reader-Entwicklung mit QWebEngineView – Qt Blog  
- ebooklib Dokumentation  
- ReportLab User Guide  
- WeasyPrint Docs  

### 7.5 KI-Integration

- Hands-On AI with Python – Packt Publishing  
- OpenAI API Integration – Python Tutorial  
