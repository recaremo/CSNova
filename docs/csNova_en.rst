.. title:: Codices Scriptoria Nova

Codices Scriptoria Nova (CSNova)
================================

1. Objective
------------

Development of a cross-platform desktop application (Linux, Windows, macOS) for authors to plan, organize, and creatively support book projects. The software combines database-driven project management, a modern GUI, integrated AI features, and a custom reader capable of displaying multimedia content, animations, and 3D models.

2. Key Features
---------------

* Project management: Create, edit, and archive book projects
* Character database: Primary and secondary tables (physiognomy, psychology, education, origin, …)
* Chapter & scene management including plotlines, timelines, locations, items
* Relationship and mind map module (characters, groups, connections)
* Statistics & overviews (profiles, to-do lists, progress tracking)
* Integrated writing tips, genre guides, source management, brainstorming tools
* Multimedia integration (images, audio, video, animations)
* Export to various formats (EPUB, PDF, HTML, proprietary reader format)
* Custom multimedia reader with responsive layout per platform
* AI interview function for character development, plot ideas, text analysis
* Languages: German, English, …
* Spell check: German, English

3. Technical Foundation
-----------------------

* Programming language: Python (for logic, AI integration, database access)
* GUI framework: PySide6 (Qt6)
* Database: SQLite (later expandable to PostgreSQL/MySQL)
* Deployment: PyInstaller → standalone builds for Linux, Windows, macOS
* AI integration: API connection with asynchronous event handling
* Export modules: ebooklib, reportlab, weasyprint
* Multimedia: QtMultimedia, QWebEngineView/QML for the reader

4. Project Roadmap & Progress
-----------------------------

1. **Installation** ✅  
2. **Set up basic GUI structure** 🔄  
3. **Create data tables** 🔄  
4. **Test database connection** 🔄  
5. **Prepare sample project** 🔄  
6. **Prepare export function** 🔄  
7. **Initialize AI module** 🔄  

4.1 Installation
~~~~~~~~~~~~~~~~

* Project name “Codices Scriptoria Nova” copyright-checked
* PNG logo created
* Development environment: Linux Mint, Visual Studio Code (English)
* Language: Python
* VSC installed, Python add-on integrated
* Add-ons:
  * Black Formatter
  * Github Pull Requests
  * isort
  * Jupyter
  * Pylance
  * Python Debugger
  * Python Environments
* GitHub connection active
* Virtual environment set up, tools installed:
  * pyside6
  * ebooklib
  * weasyprint
  * reportlab
  * requests
  * asyncio
  * libxcb-cursor0

::

   frank@recaremo:~/Documents/CSNova$ tree -F ./
   ├── ai/
   │   ├── analysis.py
   │   ├── brainstorming.py
   │   ├── interview.py
   │   ├── models/
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
   │   ├── epub_export.py
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

* GUI framework: PySide6 (Qt6)
* Main window: main_window.py
* Tabs: character_tab.py, project_tab.py, scene_tab.py
* Widgets: dialog.py, listview.py
* Stylesheets: styles/
* Layout: responsive, platform-dependent
* Goal: intuitive operation, modular expandability

4.3 Tables
~~~~~~~~~~

All SQL tables are listed in the “Tables” section of your page – already formatted as Python code blocks.

5. Program Logo
===============

5.1 Large Logo
~~~~~~~~~~~~~~

* Motif: Open book with a floating hand and quill writing into it. Book rotated 45° counterclockwise. Book is twice the size of the hand with quill. Entire motif enclosed in a simple frame.
* Text: “Codices Scriptoria Nova” in three lines
  * “Codices Scriptoria” in medieval font, “C” and “S” in lapis lazuli blue
  * “Nova” in modern font
  * Motif on the left – text on the right, outside the frame
* Background: Parchment texture with signs of wear
* Style: Albrecht Dürer, medieval woodcut
* Composition: Rule of thirds or golden ratio
* Details: Slight imperfections in the print texture

**Prompt (English):**

.. code-block:: text
A hand with quill pen writing in a book. Book is larger than the hand – approximately twice. Motif inside a simple frame. Right of the frame: three lines of black color text. First and second in medieval, third in modern font. First: Codices – C is capital in lapis lazuli blue. Second: Scriptoria – S is capital in lapis lazuli blue. Third: Nova – sans-serif, modern. Style: Albrecht Dürer – medieval woodcut. Background: old, used parchment with hairline fractures, fine cracks. Composition: rule of thirds or golden ratio. Include slight imperfections in the print texture.

5.1 Small Logo
~~~~~~~~~~~~~~

* Same motif as large logo
* Text: “Codices Scriptoria Nova” in two lines
  * “CS” in medieval font, “C” and “S” in lapis lazuli blue
  * “Nova” in modern font
  * Motif on the left – text on the right, outside the frame
* Background: Parchment texture with signs of wear
* Style: Albrecht Dürer, medieval woodcut
* Composition: Rule of thirds or golden ratio
* Details: Slight imperfections in the print texture

**Prompt (English):**

.. code-block:: text
A hand with quill pen writing in a book. Book is larger than the hand – approximately twice. Motif inside a simple frame. Right of the frame: two lines of black color text. First in medieval, second in modern font. First: CS. Second: Nova – sans-serif, modern. Style: Albrecht Dürer – medieval woodcut. Background: old, used parchment with hairline fractures, fine cracks. Composition: rule of thirds or golden ratio. Include slight imperfections in the print texture.
```

6. Tutorials & Literature, Sources
----------------------------------

6.1 PySide6 & GUI Development
-----------------------------

* Create GUI Applications with Python & Qt6 – Martin Fitzpatrick
* Modern UI with PySide6 – complete app
* Install & Setup PySide6 and Qt Designer
* PySide6 + SQLite integration – Qt documentation

6.2 Database & Migration
------------------------

* SQL for Beginners – Michael Kofler
* SQLite Tutorial – Jacek Artymiak
* SQLite Crash Course – freeCodeCamp
* Database migration with Alembic – Heise Developer
* SQLAlchemy Getting Started

6.3 Multimedia & Animation
--------------------------

* Multimedia Programming with Qt – Marco Piccolino
* QtMultimedia Tutorial – Audio & Video
* QML Animation Basics – Qt Academy
* QtMultimedia & QML – Best Practices
* PySide6 Animation Tutorial
* QtMultimedia Docs

6.4 Export Formats & Reader
---------------------------

* Creating EPUBs with ebooklib – Python Publishing Guide
* PDF Export with ReportLab – Python Tutorials
* HTML Export with WeasyPrint – Web2PDF with CSS
* Reader development with QWebEngineView – Qt Blog
* ebooklib Documentation
* ReportLab User Guide
* WeasyPrint Docs

6.5 AI Integration
~~~~~~~~~~~~~~~~~~

* Hands-On AI with Python – Packt Publishing
* OpenAI API Integration – Python Tutorial
```

