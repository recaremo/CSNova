
.. title:: Codices Scriptoria Nova

Codices Scriptoria Nova (CSNova)
================================

1. Ziel
-------

Entwicklung einer plattformübergreifenden Desktop‑Anwendung (Linux, Windows, macOS) für Autor:innen zur Planung, Organisation und kreativen Unterstützung von Buchprojekten. Die Software kombiniert datenbankgestützte Projektverwaltung, moderne GUI, integrierte KI‑Features und einen individuellen Reader, der multimediale Inhalte, Animationen und 3D-Modelle darstellen kann.

2. Hauptfunktionen
------------------

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
-------------------

* Programmiersprache: Python (für Logik, KI‑Anbindung, Datenbankzugriffe)
* GUI‑Framework: PySide6 (Qt6)
* Datenbank: SQLite (später erweiterbar auf PostgreSQL/MySQL)
* Deployment: PyInstaller → eigenständige Builds für Linux, Windows, macOS
* KI‑Integration: API‑Anbindung mit asynchronem Event‑Handling
* Exportmodule: ebooklib, reportlab, weasyprint
* Multimedia: QtMultimedia, QWebEngineView/QML für den Reader
* UI-Übersetzung: Menütexte als Variablen, Sprachdatenbank (Tabelle), dynamische Einstellungen

4. Projektfahrplan & Fortschritt
--------------------------------

1. **Installation** ✅  
2. **GUI‑Grundstruktur aufsetzen** 🔄  
3. **Datentabellen anlegen** 🔄  
4. **Datenbankverbindung testen** 🔄  
5. **Beispielprojekt einrichten** 🔄  
6. **Exportfunktion vorbereiten** 🔄  
7. **KI‑Modul initialisieren** 🔄  
8. **Sprachmodul vorbereiten** ⏳

4.1 Installation
~~~~~~~~~~~~~~~~

* Projektname „Codices Scriptoria Nova“ urheberrechtlich geprüft
* PNG-Logo erstellt
* Entwicklungsumgebung: Linux Mint, Visual Studio Code (englisch)
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

.. code-block:: bash

   frank@recaremo:~/Dokumente/CSNova$ tree -F ./
   ├── ai/
   │   ├── analysis.py
   │   ├── brainstorming.py
   │   ├── interview.py
   │   ├── modelle/
   │   └── prompts/
   ├── assets/
   │   ├── icons/
   │   └── media/
   ├── cli.py
   ├── config/
   │   ├── dev.py
   │   ├── prod.py
   │   └── settings.py
   ├── core/
   │   ├── database.py
   │   ├── logic/
   │   │   └── crud.py
   │   ├── models/
   │   │   ├── character.py
   │   │   ├── project.py
   │   │   └── scene.py
   │   └── services/
   ├── docs/
   ├── export/
   │   ├── csnova_export.py
   │   ├── ebub_export.py
   │   ├── html_export.py
   │   └── pdf_export.py
   ├── gui/
   │   ├── main_window.py
   │   ├── styles/
   │   ├── tabs/
   │   │   ├── character_tab.py
   │   │   ├── project_tab.py
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

4.2 GUI
~~~~~~~

* GUI-Framework: PySide6 (Qt6)
* Hauptfenster: main_window.py
* Tabs: character_tab.py, project_tab.py, scene_tab.py
* Widgets: dialog.py, listview.py
* Stylesheets: styles/
* Layout: responsiv, plattformabhängig
* Ziel: intuitive Bedienung, modulare Erweiterbarkeit

4.3 Tabellen
~~~~~~~~~~~~

Alle SQL-Tabellen findest du im Abschnitt „Tabellen“ deiner Seite – bereits im Python-Codeblock-Format.

5. Programm-Logo
----------------

5.1 Großes Logo
~~~~~~~~~~~~~~~

* Motiv: Geöffnetes Buch darüber eine schwebende Hand und Schreibfeder, die in das Buch schreiben. Das Buch ist 45° gegen den Uhrzeigersinn gedreht. Setzt das Buch im Verhältnis 2:1 zur Hand mit der Feder. Das gesamte Motiv ist von einem schlichten, einfachen Rahmen umgeben.
* Schriftzug: „Codices Scriptoria Nova“ in drei Zeilen
  * „Codices Scriptoria“ in mittelalterlicher Schrift, „C“ und „S“ in Lapislazuli-Blau
  * „Nova“ in moderner Schrift
  * Das Motiv ist auf der linken Seite – der Text befindet sich rechts davon und liegt außerhalb des Rahmens der das Motiv umgibt.
* Hintergrund: Pergamenttextur mit Gebrauchsspuren
* Stil: Albrecht Dürer, mittelalterlicher Holzdruck
* Komposition: Drittelregel oder Goldener Schnitt
* Besonderheiten: Kleine Unregelmäßigkeiten im Druckbild

**Prompt (englisch):**

.. code-block:: text

   A hand with quill pen writing in a book. Book is larger than the hand – approximately twice. Motif inside a simple frame. Right of the frame: three lines of black color text. First and second in medieval, third in modern font. First: Codices – C is capital in lapis lazuli blue. Second: Scriptoria – S is capital in lapis lazuli blue. Third: Nova – sans-serif, modern. Style: Albrecht Dürer – medieval woodcut. Background: old, used parchment with hairline fractures, fine cracks. Composition: rule of thirds or golden ratio. Include slight imperfections in the print texture.

5.2 Kleines Logo
~~~~~~~~~~~~~~~~

* Motiv: Geöffnetes Buch darüber eine schwebende Hand und Schreibfeder, die in das Buch schreiben. Das Buch ist 45° gegen den Uhrzeigersinn gedreht. Setzt das Buch im Verhältnis 2:1 zur Hand mit der Feder. Das gesamte Motiv ist von einem schlichten, einfachen Rahmen umgeben.
* Schriftzug: „Codices Scriptoria Nova“ in drei Zeilen
  * „Codices Scriptoria“ in mittelalterlicher Schrift, „C“ und „S“ in Lapislazuli-Blau
  * „Nova“ in moderner Schrift
  * Das Motiv ist auf der linken Seite – der Text befindet sich rechts davon und liegt außerhalb des Rahmens der das Motiv umgibt.
* Hintergrund: Pergamenttextur mit Gebrauchsspuren
* Stil: Albrecht Dürer, mittelalterlicher Holzdruck
* Komposition: Drittelregel oder Goldener Schnitt
* Besonderheiten: Kleine Unregelmäßigkeiten im Druckbild

**Prompt (englisch):**

.. code-block:: text

   A hand with quill pen writing in a book. Book is larger than the hand – approximately twice. Motif inside a simple frame. Right of the frame: two lines of black color text. First in medieval, second in modern font. First: CS. Second: Nova – sans-serif, modern. Style: Albrecht Dürer – medieval woodcut. Background: old, used parchment with hairline fractures, fine cracks. Composition: rule of thirds or golden ratio. Include slight imperfections in the print texture


6. Tutorials & Literatur, Quellen
---------------------------------

6.1 PySide6 & GUI-Entwicklung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Create GUI Applications with Python & Qt6 – Martin Fitzpatrick
* Modern UI mit PySide6 – komplette App
* Install & Setup PySide6 and Qt Designer
* PySide6 + SQLite integration – Qt‑Dokumentation

6.2 Datenbank & Migration
~~~~~~~~~~~~~~~~~~~~~~~~~~

* SQL für Einsteiger – Michael Kofler
* SQLite Tutorial – Jacek Artymiak
* SQLite Crash Course – freeCodeCamp
* Datenbankmigration mit Alembic – Heise Developer
* SQLAlchemy Getting Started

6.3 Multimedia & Animation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Multimedia Programming with Qt – Marco Piccolino
* QtMultimedia Tutorial – Audio & Video
* QML Animation Basics – Qt Academy
* QtMultimedia & QML – Best Practices
* PySide6 Animation Tutorial
* QtMultimedia Docs

6.4 Exportformate & Reader
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Creating EPUBs with ebooklib – Python Publishing Guide
* PDF-Export mit ReportLab – Python Tutorials
* HTML-Export mit WeasyPrint – Web2PDF mit CSS
* Reader-Entwicklung mit QWebEngineView – Qt Blog
* ebooklib Dokumentation
* ReportLab User Guide
* WeasyPrint Docs

6.5 KI-Integration
~~~~~~~~~~~~~~~~~~

* Hands-On AI with Python – Packt Publishing
* OpenAI API Integration – Python Tutorial
