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