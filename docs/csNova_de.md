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
  - pyinstaller  

#### 4.1.1 Projektbaum

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
│   │   ├── character_groups
│   │   ├── character_groups.py
│   │   ├── character_main.py
│   │   ├── character_origin.py
│   │   ├── character_personality.py
│   │   ├── character_psychological_profile.py
│   │   ├── gender_data.py
│   │   ├── gender.py
│   │   ├── __init__.py
│   │   ├── project_chapters.py
│   │   ├── project_chapters_scenes.py
│   │   ├── project.py
│   │   ├── project_scenes_objects.py
│   │   ├── project_scenes_places.py
│   │   ├── project_storylines.py
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
│   │   │   ├── project_chapters.cpython-312.pyc
│   │   │   ├── project_chapters_scenes.cpython-312.pyc
│   │   │   ├── project.cpython-312.pyc
│   │   │   ├── project_scenes_objects.cpython-312.pyc
│   │   │   ├── project_scenes_places.cpython-312.pyc
│   │   │   ├── project_storylines.cpython-312.pyc
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
│   ├── csNova_00_de.md
│   ├── csNova_01-04_de.md
│   ├── csNova_05_de.md
│   ├── csNova_06_de.md
│   ├── csNova_07_de.md
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
│   ├── start_window.py
│   ├── styles/
│   │   ├── buttons.qss
│   │   ├── __pycache__/
│   │   │   └── style_utils.cpython-312.pyc
│   │   └── style_utils.py
│   ├── tabs/
│   │   ├── character_tab.py
│   │   ├── project_tab.py
│   │   ├── __pycache__/
│   │   │   └── project_tab.cpython-312.pyc
│   │   └── scene_tab.py
│   └── widgets/
│       ├── dialog.py
│       └── listview.py
├── .gitignore
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

# Import the table modules
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
    conn = sqlite3.connect(DB_PATH)
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
        ('Male', 'Identifies as male'),
        ('Female', 'Identifies as female'),
        ('Non-binary', 'Does not identify exclusively as male or female'),
        ('Transgender', 'Gender identity differs from assigned sex at birth'),
        ('Intersex', 'Born with physical sex characteristics that don’t fit typical definitions'),
        ('Agender', 'Does not identify with any gender'),
        ('Genderfluid', 'Gender identity varies over time'),
        ('Bigender', 'Identifies as two genders'),
        ('Other', 'Gender identity not listed above')
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
        project_story_objects INTEGER,
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
        project_storylines_title TEXT,
        project_storylines_description TEXT,
        project_storylines_notes TEXT
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
# table: project_scenes_objects
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

### 6.1 Hauptprogramm (csnova.py)

```python
import sys
from PySide6.QtWidgets import QApplication

from core.database import init_schema
from config.settings import load_settings, save_settings
from gui.start_window import StartWindow

def main():
    try:
        init_schema()
        settings = load_settings()
        language = settings.get("language", "en")

        app = QApplication(sys.argv)
        window = StartWindow(default_language=language)
        window.show()
        app.exec()

        if hasattr(window, "translator") and hasattr(window.translator, "lang"):
            updated_settings = load_settings()
            updated_settings["language"] = window.translator.lang
            save_settings(updated_settings)

    except Exception as e:
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
    return {"language": "en"}  # Fallback

def save_settings(settings):
    print("Saving to:", SETTINGS_FILE)
    try:
        json_str = json.dumps(settings, indent=2)
        print("JSON preview:\n", json_str)
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            f.write(json_str)
        print("Settings saved.")
    except Exception as e:
        print("❌ Error while saving settings:", e)

```

#### 6.1.2 Verzeichnisse (dev.py)

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
from core.translations.translations import LANGUAGES, TRANSLATIONS
from gui.preferences import PreferencesWindow
from core.translator import Translator
from gui.project_window import ProjectWindow
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

    def __init__(self, default_language="en"):
        super().__init__()
        # Set window title using translator
        self.translator = Translator(default=default_language)
        self.setWindowTitle(self.translator.tr("start_window_title"))
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
        self.project_window = ProjectWindow(translator=self.translator)
        self.project_window.show()
        QTimer.singleShot(100, lambda: self.hide())  # Nur verstecken, nicht schließen


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
        self.setWindowTitle(self.translator.tr("start_window_title"))
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
    window = StartWindow(default_language="en")
    window.show()
    sys.exit(app.exec())
```

#### 6.2.1 Translator (translator.py)

```python
# core/translator.py

from core.translations import TRANSLATIONS, LANGUAGES

class Translator:
    def __init__(self, default=""):
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
from pathlib import Path

def load_button_style(font_size):
    """
    Load button style from external QSS file and inject dynamic font size.
    """
    style_path = Path(__file__).parent / "button_style.qss"
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
  "action_cancel": "Abbrechen",
  "project_window_title": "Projekt Manager",
  "start_window_title": "Startseite"
}
```

#### 6.4.2 en.json

```json
{
        "btn_new_project": "New Project",
        "btn_load_project": "Open Project …",
        "btn_settings": "Settings",
        "btn_help": "Help/Tutorial",
        "btn_exit": "Exit",
        "menu_file": "File",
        "menu_edit": "Edit",
        "menu_help": "Help",
        "menu_settings": "Settings",
        "menu_language": "Language",
        "action_new": "New",
        "action_open": "Open",
        "action_save": "Save",
        "action_exit": "Exit",
        "tab_project": "Project",
        "tab_character": "Characters",
        "tab_scene": "Scenes",
        "btn_save": "Save",
        "tooltip_exit": "Exit application",
        "action_cancel": "Cancel",
        "project_window_title": "Project Manager",
        "start_window_title": "Start"
    }
```

#### 6.4.3 fr.json

```json
{
        "btn_new_project": "Nouveau projet", 
        "btn_load_project": "Ouvrir projet …",
        "btn_settings": "Paramètres",
        "btn_help": "Aide/Tutoriel",
        "btn_exit": "Quitter",
        "menu_file": "Fichier",
        "menu_edit": "Éditer",
        "menu_help": "Aide",
        "menu_settings": "Paramètres",
        "menu_language": "Langue",
        "action_new": "Nouveau",
        "action_open": "Ouvrir",
        "action_save": "Enregistrer",
        "action_exit": "Quitter",
        "tab_project": "Projet",
        "tab_character": "Personnages",
        "tab_scene": "Scènes",
        "btn_save": "Enregistrer",
        "tooltip_exit": "Quitter l'application",
        "action_cancel": "Annuler",
        "project_window_title": "Gestion de projet",
        "start_window_title": "Accueil"
    }
```

#### 6.4.4 es.json

```json
{
        "btn_new_project": "Nuevo proyecto",
        "btn_load_project": "Abrir proyecto …",
        "btn_settings": "Configuración",
        "btn_help": "Ayuda/Tutorial",
        "btn_exit": "Salir",
        "menu_file": "Archivo",
        "menu_edit": "Editar",
        "menu_help": "Ayuda",
        "menu_settings": "Configuración",
        "menu_language": "Idioma",
        "action_new": "Nuevo",
        "action_open": "Abrir",
        "action_save": "Guardar",
        "action_exit": "Salir",
        "tab_project": "Proyecto",
        "tab_character": "Personajes",
        "tab_scene": "Escenas",
        "btn_save": "Guardar",
        "tooltip_exit": "Salir de la aplicación",
        "action_cancel": "Cancelar",
        "project_window_title": "Gestor de proyectos",
        "start_window_title": "Inicio"
    }
```

#### 6.4.5 Programmeinstellungen (user_settings.json)

```json
{
  "language": "en",
  "splitter_sizes": [
    297,
    1089,
    184
  ]
}
```

#### 6.4.6 help_de.json
```json
{
    "help_project": "Geben Sie allgemeine Informationen zu Ihrem Schreibprojekt an, wie Titel, Genre und Ziele.",
    "help_characters": "Definieren Sie Ihre Charaktere: Namen, Rollen, Eigenschaften und Beziehungen.",
    "help_storylines": "Skizzieren Sie die Haupt-Handlungsstränge und deren Entwicklung im Laufe der Zeit.",
    "help_chapters": "Organisieren Sie Ihre Geschichte in Kapitel und beschreiben Sie deren Inhalt.",
    "help_scenes": "Beschreiben Sie einzelne Szenen, deren Zweck und Umgebung.",
    "help_objects": "Listen Sie wichtige Objekte und deren Bedeutung in der Geschichte auf.",
    "help_locations": "Beschreiben Sie die in Ihrer Geschichte verwendeten Orte, einschließlich Atmosphäre und Relevanz."
}
```

#### 6.4.6 help_en.json
```json
{
  "help_project": "Provide general information about your writing project, such as title, genre, and goals.",
  "help_characters": "Define your characters: names, roles, traits, and relationships.",
  "help_storylines": "Outline the main story arcs and how they develop over time.",
  "help_chapters": "Organize your story into chapters and describe their content.",
  "help_scenes": "Detail individual scenes, their purpose, and setting.",
  "help_objects": "List important objects and their significance in the story.",
  "help_locations": "Describe the locations used in your story, including atmosphere and relevance."
}
```

#### 6.4.7 help_es.json
```json
{
  "help_project": "Proporcione información general sobre su proyecto de escritura, como el título, el género y los objetivos.",
  "help_characters": "Defina sus personajes: nombres, roles, características y relaciones.",
  "help_storylines": "Esboce las tramas principales y cómo se desarrollan a lo largo del tiempo.",
  "help_chapters": "Organice su historia en capítulos y describa su contenido.",
  "help_scenes": "Describa las escenas individuales, su propósito y entorno.",
  "help_objects": "Enumere los objetos importantes y su significado dentro de la historia.",
  "help_locations": "Describa los lugares utilizados en su historia, incluyendo la atmósfera y su relevancia."
}
```

#### 6.4.8 help_fr.json
```json
{
  "help_project": "Fournissez des informations générales sur votre projet d’écriture, telles que le titre, le genre et les objectifs.",
  "help_characters": "Définissez vos personnages : noms, rôles, traits de caractère et relations.",
  "help_storylines": "Esquissez les intrigues principales et leur évolution au fil du temps.",
  "help_chapters": "Organisez votre histoire en chapitres et décrivez leur contenu.",
  "help_scenes": "Décrivez les scènes individuelles, leur objectif et leur environnement.",
  "help_objects": "Listez les objets importants et leur signification dans l’histoire.",
  "help_locations": "Décrivez les lieux utilisés dans votre histoire, y compris leur atmosphère et leur pertinence."
}
```

### 6.5 Datenbank (database.py)

```python
# database.py
import sqlite3
from config.dev import DB_PATH  
from core.tables.gender_data import data_gender
from core.tables.sex_orientation_data import sex_orientation_data

# import tables
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

### 6.6 .gitignore

```text
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*.so
*.pyd

# Virtual environments
.venv/
env/
venv/

# Editor/IDE files
.vscode/
.idea/
*.swp

# Distribution / packaging
build/
dist/
*.egg-info/
.eggs/

# Database files
data/*.db

# User settings and logs
config/user_settings.json
*.log

# OS files
.DS_Store
Thumbs.db

# Exported files
export/*.pdf
export/*.epub
export/*.html

# Python test cache
.pytest_cache/
```

### 6.7 Abhängigkeiten (requirements.txt)

```text
pyside6
ebooklib
weasyprint
reportlab
requests
asyncio
pyinstaller
```

### 6.8 Pyinstaller

```text
pyinstaller --onefile --windowed csnova.py \
  --add-data "core/translations:core/translations" \
  --add-data "core/tables:core/tables" \
  --add-data "data:data" \
  --add-data "assets:assets" \
  --add-data "config:config" \
  --add-data "gui/styles:gui/styles" \
  --add-data "docs:docs" \
  --add-data "ai:ai" \
  --add-data "export:export"
```

### 6.9 Setup (install_csnova.sh)

```sh
#!/bin/bash

echo "Installing CSNova..."

# 1. Check and install system dependencies
echo "Checking system dependencies..."
sudo apt update
sudo apt install -y libxcb-cursor0

# 2. Create installation directory
INSTALL_DIR="$HOME/CSNova 1.0"
mkdir -p "$INSTALL_DIR"

# 3. Copy csnova in executable
cp ./dist/csnova "$INSTALL_DIR/"

# 4. Copy all necessary folders and files
for folder in assets config core data docs gui ai export; do
    if [ -d "$folder" ]; then
        cp -r "$folder" "$INSTALL_DIR/"
    fi
done

# 5. Set executable permissions
chmod +x "$INSTALL_DIR/csnova"

echo "Installation complete!"
echo "You can start CSNova with:"
echo "$INSTALL_DIR/csnova"
```

### 6.10 Projektfenster (project_window.py)

```python
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

```

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

## 8. Lizenz
# Lizenzbedingungen für Codices Scriptoria Nova (CSNova)

## Einleitung

Die Lizenzstruktur von *Codices Scriptoria Nova* orientiert sich an der Welt mittelalterlicher Schreibstuben und spiegelt die Vielfalt moderner Autor:innen wider. Drei klar definierte Versionen – **Novitia**, **Magister** und **Collegium** – ermöglichen eine faire und transparente Nutzung der Software, abgestimmt auf individuelle und gemeinschaftliche Bedürfnisse.

## CSNova – Hauptanwendung

CSNova ist Open Source Software. Sie darf unter den Bedingungen der jeweiligen Version genutzt und weitergegeben werden.

### Lizenzübersicht

Es existieren drei Versionen:

- **CSNova Novitia** – eine **kostenlose Version** für die **nicht kommerzielle Nutzung**, z. B. durch angehende Autor:innen, zu Testzwecken oder in Bildungseinrichtungen (Schulen, Universitäten, Volkshochschulen und sonstige Bildungseinrichtungen).  
  *Die Nutzung setzt eine Registrierung voraus.*

- **CSNova Magister** – eine **kostenpflichtige Version** für einzelne Autor:innen, die das Programm professionell nutzen und ein Jahreseinkommen von über 50.000 € erzielen.  
  *Die Nutzung setzt eine Registrierung sowie den Erwerb einer gültigen Lizenz voraus.*  
  Das Jahreseinkommen bezieht sich auf Einnahmen aus schriftstellerischer Tätigkeit, die mit Hilfe der Software erzielt werden. Professionelle Nutzung bezeichnet den regelmäßigen Einsatz der Software zur Erstellung, Veröffentlichung oder Vermarktung literarischer Werke mit kommerziellem Zweck.

- **CSNova Collegium** – eine Version für Autor:innen, die im Team das Programm professionell nutzen.  
  *Die Nutzung setzt eine Registrierung sowie den Erwerb einer gültigen Lizenz voraus.*  
  Professionelle Nutzung bezeichnet den regelmäßigen Einsatz der Software zur Erstellung, Veröffentlichung oder Vermarktung literarischer Werke mit kommerziellem Zweck.

#### Zusammenfassung der Lizenzversionen

| Version              | Zielgruppe                         | Nutzungstyp                   | Lizenzstatus                         |
|----------------------|------------------------------------|--------------------------------|--------------------------------------|
| **CSNova Novitia**   | Lernende, Bildungseinrichtungen    | Nicht-kommerziell              | Kostenlos (mit Registrierung)        |
| **CSNova Magister**  | Einzelautor:innen mit Einkommen >50.000 € | Professionell (Einzelnutzung) | Kostenpflichtig (mit Registrierung) |
| **CSNova Collegium** | Autor:innen-Teams                  | Professionell (Teamnutzung)    | Kostenpflichtig (mit Registrierung) |

### Änderungen und Weitergabe

Änderungen am Quellcode dürfen **nur mit schriftlicher Zustimmung des Autors** vorgenommen werden. Alle modifizierten Versionen müssen ebenfalls unter einer **Open Source Lizenz** veröffentlicht werden.

Die Nutzung des Namens „CSNova“, „Codices Scriptoria Nova“, „CSNova Novitia“, „CSNova Magister“ oder „CSNova Collegium“ für modifizierte Versionen ist **nur mit schriftlicher Genehmigung des Autors** gestattet. Der Autor übernimmt **keine Haftung** für Schäden, die durch veränderte Versionen oder deren Inhalte entstehen – insbesondere nicht für Inhalte, die ohne seine Zustimmung verändert oder unter einem der genannten Namen veröffentlicht wurden.

## CSNova-Reader

Der CSNova-Reader ist **Open Source** und steht **ohne Lizenzgebühren** zur Verfügung. Die Nutzung unterliegt den unten genannten Einschränkungen.  
*Die Nutzung setzt eine Registrierung voraus.*

Er darf kostenfrei genutzt, kopiert und weitergegeben werden – sowohl privat als auch kommerziell.

### Einschränkungen der kommerziellen Nutzung

Der CSNova-Reader darf kommerziell genutzt werden, z. B. zur Erstellung und Veröffentlichung von Büchern, Editionen oder anderen Produkten.

Ein Verkauf oder Vertrieb des CSNova-Readers als eigenständiges Produkt ist **nicht gestattet**.

### Änderungen und Weitergabe

Änderungen am CSNova-Reader dürfen **nur mit schriftlicher Zustimmung des Autors** vorgenommen werden. Alle abgeleiteten Versionen müssen ebenfalls **dauerhaft kostenfrei nutzbar** bleiben.

Die Nutzung des Namens „CSNova“, „Codices Scriptoria Nova“, „CSNova-Reader“, „CSNova Novitia“, „CSNova Magister“ oder „CSNova Collegium“ für modifizierte Versionen des CSNova-Readers ist **nur mit schriftlicher Genehmigung des Autors** gestattet. Der Autor übernimmt **keine Haftung** für Schäden, die durch veränderte Versionen oder deren Inhalte entstehen – insbesondere nicht für Inhalte, die ohne seine Zustimmung verändert oder unter einem der genannten Namen veröffentlicht wurden.

## Allgemeine Hinweise

* Die Software wird ohne Gewähr bereitgestellt. Es besteht kein Anspruch auf Support oder Updates.
* Die Namensrechte an „CSNova“, „Codices Scriptoria Nova“, „CSNova-Reader“, „CSNova Novitia“, „CSNova Magister“ und „CSNova Collegium“ verbleiben beim Autor.
* Die Nutzung der Software setzt die Anerkennung dieser Lizenzbedingungen voraus.

© 2025 Frank Reiser  
Kontakt: reiserfrank@t-online.de
