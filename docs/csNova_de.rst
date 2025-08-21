.. title:: Codices Scriptoria Nova

Codices Scriptoria Nova (CSNova)
================================

1. Ziel
=======

Entwicklung einer plattformübergreifenden Desktop‑Anwendung (Linux, Windows, macOS) für Autor:innen zur Planung, Organisation und kreativen Unterstützung von Buchprojekten. Die Software kombiniert datenbankgestützte Projektverwaltung, moderne GUI, integrierte KI‑Features und einen individuellen Reader, der multimediale Inhalte, Animationen und 3D-Modelle darstellen kann.

1.1 KI-Anweisungen
------------------

1. Verzichte auf die Simulation von Gefühlen, Empathie und Humor.
2. Antworten sind rational, sachlich und ausschließlich auf die Frage bezogen.
3. Füge keine Inhalte hinzu und verzichte auf Vorschläge, wenn nicht explizit dazu aufgefordert: "Mache mir alternative Vorschläge"
4. Füge der Seite keine Inhalte hinzu. Alle Antworten, Korrekturen und Veränderungsvorschläge erfolgen ausschließlich hier im Chat.
5. Die im Punkt 4 vorgeschlagenen Änderungen werden der Seite nur hinzugefügt, wenn eine explizite Aufforderung erfolgt: "Füge die Änderungen der Seite hinzu"

2. Hauptfunktionen
==================

 * Projektverwaltung: Anlegen, Bearbeiten und Archivieren von Buchprojekten
 * Charakterdatenbank: Haupt- und Nebentabellen (Physiognomie, Psychologie, Ausbildung, Herkunft, …)
 * Kapitel- & Szeneverwaltung inkl. Handlungsstränge, Zeitlinien, Orte, Gegenstände
 * Beziehungs- und Mindmap‑Modul (Charaktere, Gruppen, Verbindungen)
 * Statistiken & Übersichten (Steckbriefe, ToDo‑Listen, Fortschritt)
 * Integrierte Schreib‑Tipps, Genre‑Guides, Quellenverwaltung, Brainstorming‑Tools
 * Multimedia‑Integration (Bilder, Audio, Video, Animationen)
 * Export in diverse Formate (EPUB, PDF, HTML, eigenes Reader‑Format)
 * Custom Multimedia‑Reader mit responsivem Layout pro Plattform
 * KI‑Interviewfunktion für Figurenentwicklung, Plotideen, Textanalyse
 * Sprachen: Deutsch (Standard), Englisch, Französisch, Spanisch
 * Rechtschreibprüfung: Deutsch, Englisch
 * Dynamische Sprachauswahl mit automatischer Anpassung aller Menü- und UI-Texte

3. Technische Basis
===================

 * Programmiersprache: Python (für Logik, KI‑Anbindung, Datenbankzugriffe)
 * GUI‑Framework: PySide6 (Qt6)
 * Datenbank: SQLite (später erweiterbar auf PostgreSQL/MySQL)
 * Deployment: PyInstaller → eigenständige Builds für Linux, Windows, macOS
 * KI‑Integration: API‑Anbindung mit asynchronem Event‑Handling
 * Exportmodule: ebooklib, reportlab, weasyprint
 * Multimedia: QtMultimedia, QWebEngineView/QML für den Reader
 * UI-Übersetzung: Menütexte als Variablen, Sprachdatenbank (Tabelle), dynamische Einstellungen

4. Projektfahrplan & Fortschritt
================================
Übersicht:

 * Installation
 * GUI‑Grundstruktur aufsetzen
 * Datentabellen anlegen
 * Datenbankverbindung testen
 * Beispielprojekt einrichten
 * Exportfunktion vorbereiten
 * KI‑Modul initialisieren
 * Sprachmodul vorbereiten

4.1 Installation
----------------

 * Projektname „Codices Scriptoria Nova“ urheberrechtlich geprüft
 * PNG-Logo erstellt
 * Entwicklungsumgebung: Linux Mint, Visual Studio Code (englisch), QT Designer, QT Design Studio, GIMP.
 * Sprache: Python
 * VSC installiert, Python-AddOn eingebunden
 * AddOns:

   * Black Formatter
   * Github Pull Requests
   * isort
   * Jupyter
   * Pylance
   * Python Debugger
   * Python Environments
 * GitHub-Verbindung aktiv
 * venv eingerichtet, Tools installiert:

   * pyside6
   * ebooklib
   * weasyprint
   * reportlab
   * requests
   * asyncio
   * libxcb-cursor0

.. code-block:: text

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

4.2 GUI
-------

 * GUI-Framework: PySide6 (Qt6)
 * Hauptfenster: main_window.py
 * Tabs: character_tab.py, project_tab.py, scene_tab.py
 * Widgets: dialog.py, listview.py
 * Stylesheets: styles/
 * Layout: responsiv, plattformabhängig
 * Ziel: intuitive Bedienung, modulare Erweiterbarkeit

4.2.1 start_windows.ui
~~~~~~~~~~~~~~~~~~~~~~

Format: 1920x1080

Hintergrundbild: csNova_background_start.png im Verzeichnis /assets/media/

Stylesheet-Vorschlag:

.. code-block:: css

   QWidget { border-image: url(/home/frank/Dokumente/CSNova/assets/media/csNova_background_start.png) 0 0 0 0 stretch stretch; }
   QPushButton { background-color: transparent; color: #1a1a1a; font-family: "Garamond"; font-size: 18px; border: 2px solid #1a1a1a; border-radius: 6px; padding: 6px 12px; }
   QPushButton:hover { background-color: #e0d8c0; color: #000000; border-color: #000000; }
   QLabel { color: #1a1a1a; font-family: "Garamond"; font-size: 20px; background-color: transparent; }

4.3 Tabellen
------------

Auflistungen der erstellten Tabellen in Python:

4.3.1 Haupttabelle: character_main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

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

4.3.1.1 Referenztabelle: gender
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Referenztabelle: gender
   cursor.execute("""
   CREATE TABLE IF NOT EXISTS gender (
       gender_ID INTEGER PRIMARY KEY AUTOINCREMENT,
       gender TEXT,
       short_description TEXT
   );
   """)

4.3.1.2 Referenztabelle: sex_orientation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Referenztabelle: sex_orientation
   cursor.execute("""
   CREATE TABLE IF NOT EXISTS sex_orientation (
       sex_orientation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
       sex_orientation TEXT,
       short_description TEXT
   );
   """)

4.3.1.3 Untertabellen: psychological_profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   
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

5. Programm-Logo
================

5.1 Großes Logo
---------------

 * Motiv: Geöffnetes Buch darüber eine schwebende Hand und Schreibfeder, die in das Buch schreiben. Das Buch ist 45° gegen den Uhrzeigersinn gedreht. Setzt das Buch im Verhältnis 2:1 zur Hand mit der Feder. Das gesamte Motiv ist von einem schlichten, einfachen Rahmen umgeben.
 * Schriftzug: „Codices Scriptoria Nova“ in drei Zeilen
 * „Codices Scriptoria“ in mittelalterlicher Schrift, „C“ und „S“ in Lapislazuli-Blau
 * „Nova“ in moderner Schrift
 * Das Motiv ist auf der linken Seite – der Text befindet sich rechts davon und liegt außerhalb des Rahmens der das Motiv umgibt.
 * Hintergrund: Pergamenttextur mit Gebrauchsspuren
 * Stil: Albrecht Dürer, mittelalterlicher Holzdruck
 * Komposition: Drittelregel oder Goldener Schnitt
 * Besonderheiten: Kleine Unregelmäßigkeiten im Druckbild

5.2 Kleines Logo
----------------

 * Motiv: Geöffnetes Buch darüber eine schwebende Hand und Schreibfeder, die in das Buch schreiben. Das Buch ist 45° gegen den Uhrzeigersinn gedreht. Setzt das Buch im Verhältnis 2:1 zur Hand mit der Feder. Das gesamte Motiv ist von einem schlichten, einfachen Rahmen umgeben.
 * Schriftzug: „CS” und “Nova“ in zwei Zeile
 * „CS“ in mittelalterlicher Schrift, „Nova“ in moderner Schrift
 * Das Motiv ist auf der linken Seite – der Text befindet sich rechts davon und liegt außerhalb des Rahmens der das Motiv umgibt.
 * Hintergrund: Pergamenttextur mit Gebrauchsspuren
 * Stil: Albrecht Dürer, mittelalterlicher Holzdruck
 * Komposition: Drittelregel oder Goldener Schnitt
 * Besonderheiten: Kleine Unregelmäßigkeiten im Druckbild

6.Tutorials & Literatur, Quellen
================================

6.1 PySide6 & GUI-Entwicklung
-----------------------------

Create GUI Applications with Python & Qt6 – Martin Fitzpatrick

Modern UI mit PySide6 – komplette App

Install & Setup PySide6 and Qt Designer

PySide6 + SQLite integration – Qt‑Dokumentation


6.2 Datenbank & Migration
--------------------------
 * SQL für Einsteiger – Michael Kofler
 * SQLite Tutorial – Jacek Artymiak
 * SQLite Crash Course – freeCodeCamp
 * Datenbankmigration mit Alembic – Heise Developer
 * SQLAlchemy Getting Started

6.3 Multimedia & Animation
--------------------------
 * Multimedia Programming with Qt – Marco Piccolino
 * QtMultimedia Tutorial – Audio & Video
 * QML Animation Basics – Qt Academy
 * Multimedia & QML – Best Practices
 * PySide6 Animation Tutorial
 * QtMultimedia Docs

6.4 Exportformate & Reader
--------------------------

 * Creating EPUBs with ebooklib – Python Publishing Guide
 * PDF-Export mit ReportLab – Python Tutorials
 * HTML-Export mit WeasyPrint – Web2PDF mit CSS
 * Reader-Entwicklung mit QWebEngineView – Qt Blog
 * ebooklib Dokumentation
 * ReportLab User Guide
 * WeasyPrint Docs

6.5 KI-Integration
~~~~~~~~~~~~~~~~~~~

 * Hands-On AI with Python – Packt Publishing
 * OpenAI API Integration – Python Tutorial
