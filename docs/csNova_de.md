# Codices Scriptoria Nova (CSNova)

## Projektbeschreibung

CSNova ist eine umfassende Software für alle, die komplexe narrative Projekte planen, entwickeln und veröffentlichen möchten – von Romanautor:innen über Drehbuchautor:innen bis hin zu Game Writer:innen.

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
- Python 3.12+ empfohlen


## 1. Ziel

Entwicklung einer plattformübergreifenden Desktop‑Anwendung (Linux, Windows, macOS) für Autor:innen zur Planung, Organisation und kreativen Unterstützung von Buchprojekten. Die Software kombiniert datenbankgestützte Projektverwaltung, moderne GUI, integrierte KI‑Features und einen individuellen Reader, der multimediale Inhalte, Animationen und 3D-Modelle darstellen kann.

### 1.1 KI-Anweisungen

1. Verzichte auf die Simulation von Gefühlen, Empathie und Humor.  
2. Antworten sind rational, sachlich und ausschließlich auf die Frage bezogen.  
3. Füge keine Inhalte hinzu und verzichte auf Vorschläge, wenn nicht explizit dazu aufgefordert: "Mache mir alternative Vorschläge". Alle Antworten, Korrekturen und Veränderungsvorschläge erfolgen ausschließlich hier im Chat.  
4. Die im Punkt 4 vorgeschlagenen Änderungen werden der Seite nur hinzugefügt, wenn eine explizite Aufforderung erfolgt: "Füge die Änderungen der Seite hinzu"

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

* Installation  
* GUI‑Grundstruktur aufsetzen  
* Datentabellen anlegen  
* Datenbankverbindung testen  
* Beispielprojekt einrichten  
* Exportfunktion vorbereiten  
* KI‑Modul initialisieren  
* Sprachmodul vorbereiten  

---

### 4.1 Installation

* Projektname „Codices Scriptoria Nova“ urheberrechtlich geprüft  
* PNG-Logo erstellt  
* Entwicklungsumgebung: Linux Mint, Visual Studio Code (Englisch), QT Designer, QT Design Studio, GIMP  
* Sprache: Python  
* VSC installiert, Python-Add-on eingebunden  
* Add-ons:  
  * Black Formatter  
  * GitHub Pull Requests  
  * isort  
  * Jupyter  
  * Pylance  
  * Python Debugger  
  * Python Environments  
* GitHub-Verbindung aktiv  
* venv eingerichtet, Tools installiert:  
  * PySide6  
  * EbookLib  
  * WeasyPrint  
  * ReportLab  
  * Requests  
  * asyncio  
  * libxcb-cursor0  
  * PyInstaller  

#### 4.1.1 Projektbaum

```text
.
├── ai
│   ├── analysis.py
│   ├── brainstorming.py
│   ├── interview.py
│   ├── modelle
│   └── prompts
├── assets
│   ├── icons
│   └── media
│       ├── csNova_background_start.png
│       └── csNova_logo_main.png
├── build
│   └── csnova
│       ├── Analysis-00.toc
│       ├── base_library.zip
│       ├── csnova.pkg
│       ├── EXE-00.toc
│       ├── localpycs
│       ├── PKG-00.toc
│       ├── PYZ-00.pyz
│       ├── PYZ-00.toc
│       ├── warn-csnova.txt
│       └── xref-csnova.html
├── cli.py
├── config
│   ├── dev.py
│   ├── prod.py
│   ├── settings.py
│   └── user_settings.json
├── core
│   ├── database.py
│   ├── logger.py
│   ├── logic
│   │   └── crud.py
│   ├── models
│   │   ├── character.py
│   │   ├── project.py
│   │   └── scene.py
│   ├── services
│   ├── tables
│   │   ├── character_appearance_detail.py
│   │   ├── character_appearance_main.py
│   │   ├── character_education.py
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
│   │   ├── project_character_group_map.py
│   │   ├── project_character_storyline_map.py
│   │   ├── project_locations.py
│   │   ├── project_objects.py
│   │   ├── project.py
│   │   ├── project_scene_character_map.py
│   │   ├── project_scene_location_map.py
│   │   ├── project_scene_object_map.py
│   │   ├── project_scene_storyline_map.py
│   │   ├── project_storylines.py
│   │   ├── sex_orientation_data.py
│   │   └── sex_orientation.py
│   ├── translations
│   │   ├── de.json
│   │   ├── en.json
│   │   ├── es.json
│   │   ├── forms
│   │   │   ├── form_de.json
│   │   │   ├── form_en.json
│   │   │   ├── form_es.json
│   │   │   └── form_fr.json
│   │   ├── fr.json
│   │   └── help
│   │       ├── help_de.json
│   │       ├── help_en.json
│   │       ├── help_es.json
│   │       └── help_fr.json
│   └── translator.py
├── csnova.log
├── csnova.py
├── data
│   └── csnova.db
├── dist
│   └── csnova
├── docs
│   ├── csNova_de.md
│   └── index.md
├── export
│   ├── csnova_export.py
│   ├── epub_export.py
│   ├── html_export.py
│   └── pdf_export.py
├── gui
│   ├── preferences.py
│   ├── project_window.py
│   ├── start_window.py
│   ├── styles
│   │   ├── form_styles.py
│   │   ├── future_style.py
│   │   ├── modern_style.py
│   │   ├── oldschool_style.py
│   │   ├── style_utils.py
│   │   └── vintage_style.py
│   ├── tabs
│   │   ├── character_tab.py
│   │   ├── project_tab.py
│   │   └── scene_tab.py
│   └── widgets
│       ├── base_form_widget.py
│       ├── dialog.py
│       ├── form_chapters.py
│       ├── form_characters.py
│       ├── form_locations.py
│       ├── form_objects.py
│       ├── form_projects.py
│       ├── form_scenes.py
│       ├── form_start.py
│       ├── form_storylines.py
│       ├── form_toolbar.py
│       ├── help_panel.py
│       ├── listview.py
│       └── navigation_panel.py
├── install_csnova.sh
├── license.md
├── readme.md
├── requirements.txt
├── setup.py
└── tests
    └── conftest.py
```

### 4.2 GUI

* GUI-Framework: PySide6 (Qt6)
* Hauptprogramm: main.py
* Startfenster: start_window.py
* Referenzen: preferences.py
* Übersetzungen: translation.py
* Tabs: character_tab.py, project_tab.py, scene_tab.py
* Widgets: dialog.py, listview.py
* Stylesheets: styles/
* Layout: responsiv, plattformabhängig
* Ziel: intuitive Bedienung, modulare Erweiterbarkeit

### 4.3 Definitionen

#### Projekt

Ein Projekt beschreibt eine in sich geschlossene Geschichte mit einem definierten Anfang und Ende. Im Rahmen einer Serie kann ein Projekt einen Cliffhanger enthalten, der in einem Folgeprojekt weitergeführt wird.

- Enthält einen oder mehrere Charaktere, die auch in anderen Projekten auftreten können.
- Umfasst eine oder mehrere Storylines, die projektübergreifend fortgesetzt werden können.
- Beinhaltet Orte und Objekte, die auch in anderen Projekten relevant sein können.
- Besteht aus mehreren Kapiteln, die eindeutig diesem Projekt zugeordnet sind.
- Enthält Szenen, die jeweils einem Kapitel und damit eindeutig dem Projekt zugeordnet sind.
- Grundlegende Projektdaten sind in der Tabelle [5.4.1 project.py](#541-projectpy) erfasst.

#### Storyline

Eine Storyline beschreibt einen Handlungsstrang, der:

- sich über mehrere Projekte erstrecken kann,
- sich über Kapitel und Szenen hinweg entfaltet – linear oder nichtlinear, z. B.:
  - Storyline A: Kapitel 3, 9, 12
  - Storyline B: Kapitel 2, 4, 5
- mit Charakteren, Objekten und Orten verknüpft ist.

#### Kapitel

Kapitel strukturieren den Handlungsablauf eines Projekts und sind ausschließlich diesem Projekt zugeordnet.

- Kapitel verlaufen immer linear: 1, 2, 3, 4 …
- Sie enthalten eine oder mehrere Szenen, die diesem Kapitel eindeutig zugeordnet sind.
- Sie enthalten einen oder mehrere Charaktere, Objekte und Orte.

#### Szene

Szenen strukturieren den Handlungsablauf innerhalb eines Kapitels und sind diesem eindeutig zugeordnet.

- Sie enthalten einen oder mehrere Charaktere, Objekte und Orte.
- Sie können Teil einer oder mehrerer Storylines sein.

#### Charakter

Charaktere können innerhalb eines oder mehrerer Projekte eine Rolle spielen.

- Sie treten in einem oder mehreren Kapiteln und Szenen auf.
- Ihnen lassen sich beliebig viele Orte und Objekte zuordnen.
- Sie können Mitglied in einer oder mehreren Gruppen sein.
- Es gibt Haupt- und Nebencharaktere. Hauptcharaktere sind immer umfassend definiert und haben einen inneren Konflikt.

#### Gruppe

Gruppen bestehen aus zwei oder mehreren Charakteren.

- Sie können projektübergreifend bestehen.
- Sie haben eine definierte Struktur oder Dynamik (z. B. Familie, Team, Gegenspieler).

#### Objekt

Objekte sind Gegenstände, die für die Handlung eines oder mehrerer Projekte von Bedeutung sind.

- Sie können Charakteren, Szenen oder Storylines zugeordnet sein.
- Sie können symbolische, funktionale oder narrative Bedeutung haben.

#### Ort

Orte sind Schauplätze, an denen die Handlung eines Projekts stattfindet.

- Sie können mehrfach verwendet werden.
- Sie sind mit Szenen, Charakteren und Objekten verknüpft.


## 5. Tabellen

### 5.1 Hilfedateien

In diesem Kapitel sind die Translationstabellen für die Hilfedateien zusammengefasst

#### 5.1.1 help_de.json
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

#### 5.1.2 help_en.json
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

#### 5.1.3 help_es.json
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

#### 5.1.4 help_fr.json
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

### 5.2 GUI

In diesem Abschnitt sind die Translationstabellen für die GUI zusammengefasst.

#### 5.2.1 de.json

```json
{
    "btn_new_project": "Datenbanken",
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
    "project_window_title": "Datenbanken",
    "start_window_title": "Startseite"
}
```

#### 5.2.2 en.json

```json
{
    "btn_new_project": "Databases",
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
    "project_window_title": "Databases",
    "start_window_title": "Start"
}
```

#### 5.2.3 fr.json

```json
{
    "btn_new_project": "Bases de données", 
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
    "project_window_title": "Bases de données",
    "start_window_title": "Accueil"
}
```

#### 5.2.4 es.json

```json
{
    "btn_new_project": "Bases de datos",
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
    "project_window_title": "Bases de datos",
    "start_window_title": "Inicio"
}
```

#### 5.2.5 form_de.json

```json
{
    "project_form_label": "Projekt", 
    "project_btn_save": "Speichern", 
    "project_btn_delete": "Löschen",
    "project_btn_next": "Vor",
    "project_btn_preview": "Zurück",
    "project_btn_new": "Neu",
    "project_title": "Titel",
    "project_subtitle": "Untertitel",
    "project_author": "Autor",
    "project_premise": "Prämisse",
    "project_genre": "Genre",
    "project_narrative_perspective": "Erzählperspektive",
    "project_timeline": "Zeitlinie",
    "project_target_group": "Zielgruppe",
    "project_start_date": "Startdatum",
    "project_deadline": "Abgabedatum",
    "project_word_count_goal": "Ziel Wortanzahl",
    "project_cover_image": "Titelbild",
    "character_form_label": "Charakter",
    "character_btn_save": "Speichern",
    "character_btn_delete": "Löschen",
    "character_btn_next": "Vor",
    "character_btn_preview": "Zurück",
    "character_btn_new": "Neu",
    "character_name": "Name",
    "character_nickname": "Spitzname",
    "character_gender": "Geschlecht",
    "character_age": "Alter",
    "character_role": "Rolle",
    "character_description": "Beschreibung",
    "storyline_form_label": "Handlungsstrang",
    "storyline_btn_save": "Speichern",
    "storyline_btn_delete": "Löschen",
    "storyline_btn_next": "Vor",
    "storyline_btn_preview": "Zurück",
    "storyline_btn_new": "Neu",
    "storyline_title": "Titel",
    "storyline_summary": "Zusammenfassung",
    "storyline_notes": "Notizen",
    "chapter_form_label": "Kapitel",
    "chapter_btn_save": "Speichern",
    "chapter_btn_delete": "Löschen",
    "chapter_btn_next": "Vor",
    "chapter_btn_preview": "Zurück",
    "chapter_btn_new": "Neu",
    "chapter_title": "Titel",
    "chapter_number": "Nummer",
    "chapter_summary": "Zusammenfassung",
    "scene_form_label": "Szene",
    "scene_btn_save": "Speichern",
    "scene_btn_delete": "Löschen",
    "scene_btn_next": "Vor",
    "scene_btn_preview": "Zurück",
    "scene_btn_new": "Neu",
    "scene_title": "Titel",
    "scene_number": "Nummer",
    "scene_summary": "Zusammenfassung",
    "object_form_label": "Gegenstand",
    "object_btn_save": "Speichern",
    "object_btn_delete": "Löschen",
    "object_btn_next": "Vor",
    "object_btn_preview": "Zurück",
    "object_btn_new": "Neu",
    "object_name": "Name",
    "object_type": "Typ",
    "object_description": "Beschreibung",
    "location_form_label": "Ort",
    "location_btn_save": "Speichern",
    "location_btn_delete": "Löschen",
    "location_btn_next": "Vor",
    "location_btn_preview": "Zurück",
    "location_btn_new": "Neu",
    "location_name": "Name",
    "location_type": "Typ",
    "location_description": "Beschreibung"
}
```

#### 5.2.6 form_en.json

```json
{
    "project_form_label": "Project",
    "project_btn_save": "Save",
    "project_btn_delete": "Delete",
    "project_btn_next": "Next",
    "project_btn_preview": "Previous",
    "project_btn_new": "New",
    "project_title": "Title",
    "project_subtitle": "Subtitle",
    "project_author": "Author",
    "project_premise": "Premise",
    "project_genre": "Genre",
    "project_narrative_perspective": "Narrative Perspective",
    "project_timeline": "Timeline",
    "project_target_group": "Target Group",
    "project_start_date": "Start Date",
    "project_deadline": "Deadline",
    "project_word_count_goal": "Word Count Goal",
    "project_cover_image": "Cover Image",
    "character_form_label": "Character",
    "character_btn_save": "Save",
    "character_btn_delete": "Delete",
    "character_btn_next": "Next",
    "character_btn_preview": "Previous",
    "character_btn_new": "New",
    "character_name": "Name",
    "character_nickname": "Nickname",
    "character_gender": "Gender",
    "character_age": "Age",
    "character_role": "Role",
    "character_description": "Description",
    "storyline_form_label": "Storyline",
    "storyline_btn_save": "Save",
    "storyline_btn_delete": "Delete",
    "storyline_btn_next": "Next",
    "storyline_btn_preview": "Previous",
    "storyline_btn_new": "New",
    "storyline_title": "Title",
    "storyline_summary": "Summary",
    "storyline_notes": "Notes",
    "chapter_form_label": "Chapter",
    "chapter_btn_save": "Save",
    "chapter_btn_delete": "Delete",
    "chapter_btn_next": "Next",
    "chapter_btn_preview": "Previous",
    "chapter_btn_new": "New",
    "chapter_title": "Title",
    "chapter_number": "Number",
    "chapter_summary": "Summary",
    "scene_form_label": "Scene",
    "scene_btn_save": "Save",
    "scene_btn_delete": "Delete",
    "scene_btn_next": "Next",
    "scene_btn_preview": "Previous",
    "scene_btn_new": "New",
    "scene_title": "Title",
    "scene_number": "Number",
    "scene_summary": "Summary",
    "object_form_label": "Object",
    "object_btn_save": "Save",
    "object_btn_delete": "Delete",
    "object_btn_next": "Next",
    "object_btn_preview": "Previous",
    "object_btn_new": "New",
    "object_name": "Name",
    "object_type": "Type",
    "object_description": "Description",
    "location_form_label": "Location",
    "location_btn_save": "Save",
    "location_btn_delete": "Delete",
    "location_btn_next": "Next",
    "location_btn_preview": "Previous",
    "location_btn_new": "New",
    "location_name": "Name",
    "location_type": "Type",
    "location_description": "Description"
}
```

#### 5.2.7 form_es.json

```json
{
    "project_form_label": "Proyecto",
    "project_btn_save": "Guardar",
    "project_btn_delete": "Eliminar",
    "project_btn_next": "Siguiente",
    "project_btn_preview": "Anterior",
    "project_btn_new": "Nuevo",
    "project_title": "Título",
    "project_subtitle": "Subtítulo",
    "project_author": "Autor",
    "project_premise": "Premisa",
    "project_genre": "Género",
    "project_narrative_perspective": "Perspectiva narrativa",
    "project_timeline": "Cronología",
    "project_target_group": "Grupo objetivo",
    "project_start_date": "Fecha de inicio",
    "project_deadline": "Fecha límite",
    "project_word_count_goal": "Meta de palabras",
    "project_cover_image": "Imagen de portada",
    "character_form_label": "Personaje",
    "character_btn_save": "Guardar",
    "character_btn_delete": "Eliminar",
    "character_btn_next": "Siguiente",
    "character_btn_preview": "Anterior",
    "character_btn_new": "Nuevo",
    "character_name": "Nombre",
    "character_nickname": "Apodo",
    "character_gender": "Género",
    "character_age": "Edad",
    "character_role": "Rol",
    "character_description": "Descripción",
    "storyline_form_label": "Trama",
    "storyline_btn_save": "Guardar",
    "storyline_btn_delete": "Eliminar",
    "storyline_btn_next": "Siguiente",
    "storyline_btn_preview": "Anterior",
    "storyline_btn_new": "Nuevo",
    "storyline_title": "Título",
    "storyline_summary": "Resumen",
    "storyline_notes": "Notas",
    "chapter_form_label": "Capítulo",
    "chapter_btn_save": "Guardar",
    "chapter_btn_delete": "Eliminar",
    "chapter_btn_next": "Siguiente",
    "chapter_btn_preview": "Anterior",
    "chapter_btn_new": "Nuevo",
    "chapter_title": "Título",
    "chapter_number": "Número",
    "chapter_summary": "Resumen",
    "scene_form_label": "Escena",
    "scene_btn_save": "Guardar",
    "scene_btn_delete": "Eliminar",
    "scene_btn_next": "Siguiente",
    "scene_btn_preview": "Anterior",
    "scene_btn_new": "Nuevo",
    "scene_title": "Título",
    "scene_number": "Número",
    "scene_summary": "Resumen",
    "object_form_label": "Objeto",
    "object_btn_save": "Guardar",
    "object_btn_delete": "Eliminar",
    "object_btn_next": "Siguiente",
    "object_btn_preview": "Anterior",
    "object_btn_new": "Nuevo",
    "object_name": "Nombre",
    "object_type": "Tipo",
    "object_description": "Descripción",
    "location_form_label": "Lugar",
    "location_btn_save": "Guardar",
    "location_btn_delete": "Eliminar",
    "location_btn_next": "Siguiente",
    "location_btn_preview": "Anterior",
    "location_btn_new": "Nuevo",
    "location_name": "Nombre",
    "location_type": "Tipo",
    "location_description": "Descripción"
}
```

#### 5.2.8 form_fr.json

```json
{
    "project_form_label": "Projet",
    "project_btn_save": "Enregistrer",
    "project_btn_delete": "Supprimer",
    "project_btn_next": "Suivant",
    "project_btn_preview": "Précédent",
    "project_btn_new": "Nouveau",
    "project_title": "Titre",
    "project_subtitle": "Sous-titre",
    "project_author": "Auteur",
    "project_premise": "Prémisse",
    "project_genre": "Genre",
    "project_narrative_perspective": "Perspective narrative",
    "project_timeline": "Chronologie",
    "project_target_group": "Groupe cible",
    "project_start_date": "Date de début",
    "project_deadline": "Date limite",
    "project_word_count_goal": "Objectif de mots",
    "project_cover_image": "Image de couverture",
    "character_form_label": "Personnage",
    "character_btn_save": "Enregistrer",
    "character_btn_delete": "Supprimer",
    "character_btn_next": "Suivant",
    "character_btn_preview": "Précédent",
    "character_btn_new": "Nouveau",
    "character_name": "Nom",
    "character_nickname": "Surnom",
    "character_gender": "Genre",
    "character_age": "Âge",
    "character_role": "Rôle",
    "character_description": "Description",
    "storyline_form_label": "Intrigue",
    "storyline_btn_save": "Enregistrer",
    "storyline_btn_delete": "Supprimer",
    "storyline_btn_next": "Suivant",
    "storyline_btn_preview": "Précédent",
    "storyline_btn_new": "Nouveau",
    "storyline_title": "Titre",
    "storyline_summary": "Résumé",
    "storyline_notes": "Notes",
    "chapter_form_label": "Chapitre",
    "chapter_btn_save": "Enregistrer",
    "chapter_btn_delete": "Supprimer",
    "chapter_btn_next": "Suivant",
    "chapter_btn_preview": "Précédent",
    "chapter_btn_new": "Nouveau",
    "chapter_title": "Titre",
    "chapter_number": "Numéro",
    "chapter_summary": "Résumé",
    "scene_form_label": "Scène",
    "scene_btn_save": "Enregistrer",
    "scene_btn_delete": "Supprimer",
    "scene_btn_next": "Suivant",
    "scene_btn_preview": "Précédent",
    "scene_btn_new": "Nouveau",
    "scene_title": "Titre",
    "scene_number": "Numéro",
    "scene_summary": "Résumé",
    "object_form_label": "Objet",
    "object_btn_save": "Enregistrer",
    "object_btn_delete": "Supprimer",
    "object_btn_next": "Suivant",
    "object_btn_preview": "Précédent",
    "object_btn_new": "Nouveau",
    "object_name": "Nom",
    "object_type": "Type",
    "object_description": "Description",
    "location_form_label": "Lieu",
    "location_btn_save": "Enregistrer",
    "location_btn_delete": "Supprimer",
    "location_btn_next": "Suivant",
    "location_btn_preview": "Précédent",
    "location_btn_new": "Nouveau",
    "location_name": "Nom",
    "location_type": "Type",
    "location_description": "Description"
}
```
### 5.3 Character Tabellen

In diesem Abschnitt sind die Tabellen zur Erstellung von Charakteren zusammengefasst.

#### 5.3.1 character_main.py

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

##### 5.3.1.1 gender.py

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
##### gender_data.py

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

##### 5.3.1.2 sex_orientation.py

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
##### sex_orientation_data.py

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

#### 5.3.2 character_origin.py

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

#### 5.3.3 character_education.py

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

#### 5.3.4 character_personality.py

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

#### 5.3.5 character_psychological_profile.py

```python
# character_psychological_profile.py
# table: subtable for character_main
# description: psychological profile of a character
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

#### 5.3.6 character_appearance_main.py

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

#### 5.3.7 character_appearance_detail.py

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

#### 5.3.8 character_groups.py

```python
# character_groups.py
# table: subtable for character_main
# description: character membership in a group
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_groups (
        groups_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID),
        groups_title TEXT,
        groups_description TEXT
    );
    """)
```

### 5.4 Projektdatenbank

In diesem Abschnitt sind die Tabellen zur Erstellung von Projekten zusammengefasst.

#### 5.4.1 project.py

```python
# project.py
# table: project
# description: central project database, main statistic of work done
# project_words_count_days = How many words a day do I "have to" write
# project_days_count = How many days are left until the deadline
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_premise TEXT,
        project_title TEXT,
        project_subtitle TEXT,
        project_author TEXT,
        project_genre TEXT,
        project_cover_image TEXT,
        project_target_group TEXT,
        project_narrative_perspective TEXT,
        project_deadline DATE,
        project_start_date DATE,     
        project_words_count_goal INTEGER,
        project_words_count_days INTEGER,
        project_days_count INTEGER,  
        project_chapters INTEGER,
        project_scenes INTEGER,
        project_story_lines INTEGER,
        project_main_characters INTEGER,
        project_supporting_characters INTEGER,
        project_groups_characters INTEGER,
        project_story_places INTEGER,
        project_story_objects INTEGER,
        project_timeline TEXT
    );
    """)
```

#### 5.4.2 project_storylines.py

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
        project_storylines_transformation TEXT,
        project_storylines_timeline TEXT,
        project_storylines_notes TEXT
    );
    """)
```

#### 5.4.3 project_chapters.py

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
        project_chapters_title TEXT,
        FOREIGN KEY(project_ID) REFERENCES project(project_ID)
    );
    """)
```

#### 5.4.4 project_chapters_scenes.py

```python
# project_chapters_scenes.py
# # table: project_chapters_scenes
# description: scenes inside a chapter
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_chapters_scenes (
        project_chapters_scenes_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_chapters_ID INTEGER NOT NULL,
        project_chapters_scenes_premise TEXT,
        project_chapters_scenes_title TEXT,
        project_chapters_scenes_goal TEXT,
        project_chapters_scenes_conflict TEXT,
        project_chapters_scenes_outcome TEXT,
        project_chapters_scenes_type TEXT,
        project_chapters_scenes_mood TEXT,
        project_chapters_scenes_duration TEXT,
        project_chapters_scenes_main_characters TEXT,
        project_chapters_scenes_supporting_characters TEXT,
        project_chapters_scenes_places TEXT,
        project_chapters_scenes_text TEXT,
        FOREIGN KEY(project_chapters_ID) REFERENCES project_chapters(project_chapters_ID)
    );
    """)
```

#### 5.4.5 project_objects.py

```python
# project_objects.py
# table: project_objects
# description: objects can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_objects (
        project_objects_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_objects_title TEXT,
        project_objects_description TEXT
    );
    """)
```

#### 5.4.6 project_locations.py

```python
# project_locations.py
# table: project_locations
# description: locations can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_locations (
        project_locations_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_locations_title TEXT,
        project_locations_description TEXT
    );
    """)
```

### 5.5 Mapping

In diesem Abschnitt werden die gemappten Tabellen sowie deren Verbindungen übersichtlich dargestellt.

#### 5.5.1 project_scene_character_map.py
```python
# project_scene_character_map.py
# table: scene_character_map
# description: links characters to scenes

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scene_character_map (
        scene_character_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_ID INTEGER NOT NULL,
        character_ID INTEGER NOT NULL,
        role_in_scene TEXT,
        FOREIGN KEY(scene_ID) REFERENCES project_chapters_scenes(project_chapters_scenes_ID),
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

#### 5.5.2 project_scene_location_map.py
```python
# project_scene_location_map.py
# table: scene_location_map
# description: links locations to scenes

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scene_location_map (
        scene_location_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_ID INTEGER NOT NULL,
        location_ID INTEGER NOT NULL,
        FOREIGN KEY(scene_ID) REFERENCES project_chapters_scenes(project_chapters_scenes_ID),
        FOREIGN KEY(location_ID) REFERENCES project_locations(project_locations_ID)
    );
    """)
```

#### 5.5.3 scene_objects_map.py
```python
# scene_objects_map.py
# table: scene_objects_map
# description: links objects to scenes

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scene_objects_map (
        scene_object_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_ID INTEGER NOT NULL,
        object_ID INTEGER NOT NULL,
        FOREIGN KEY(scene_ID) REFERENCES project_chapters_scenes(project_chapters_scenes_ID),
        FOREIGN KEY(object_ID) REFERENCES project_objects(project_objects_ID)
    );
    """)
```

#### 5.5.4 project_scene_storyline_map.py
```python
# project_scene_storyline_map.py
# table: scene_storyline_map
# description: links scenes to storylines

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scene_storyline_map (
        scene_storyline_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_ID INTEGER NOT NULL,
        storyline_ID INTEGER NOT NULL,
        FOREIGN KEY(scene_ID) REFERENCES project_chapters_scenes(project_chapters_scenes_ID),
        FOREIGN KEY(storyline_ID) REFERENCES project_storylines(project_storylines_ID)
    );
    """)
```

#### 5.5.5 project_character_group_map.py
```python
# project_character_group_map.py
# table: character_group_map
# description: links characters to groups

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_group_map (
        character_group_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        group_ID INTEGER NOT NULL,
        role_in_group TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID),
        FOREIGN KEY(group_ID) REFERENCES character_groups(groups_ID)
    );
    """)
```

#### 5.5.6 project_charcter_storyline_map.py
```python
# project_character_storyline_map.py
# table: character_storyline_map
# description: links characters to storylines

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_storyline_map (
        character_storyline_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        storyline_ID INTEGER NOT NULL,
        role_in_storyline TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID),
        FOREIGN KEY(storyline_ID) REFERENCES project_storylines(project_storylines_ID)
    );
    """)
```

## 6. - Programmecode

In diesem Abschnitt sind alle Programmcodes zusammengefasst.

### 6.1 Hauptprogramm (csnova.py)

```python
# Main program csnova.py
import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings, save_settings
from gui.start_window import StartWindow

# Import central logging functions
from core.logger import setup_logging, log_header, log_section, log_subsection, log_info, log_error

def main():
    setup_logging()  # Only once at program start
    log_header()
    log_section("csnova.py")
    log_subsection("main")
    try:
        log_info("Initializing database schema.")
        init_schema()
        log_info("Loading settings.")
        settings = load_settings()
        language = settings.get("language", "en")
        log_info(f"Language set to '{language}'.")

        app = QApplication(sys.argv)
        window = StartWindow(default_language=language)
        window.show()
        log_info("StartWindow shown.")
        app.exec()

        # Save updated language setting if changed
        if hasattr(window, "translator") and hasattr(window.translator, "lang"):
            updated_settings = load_settings()
            updated_settings["language"] = window.translator.lang
            save_settings(updated_settings)
            log_info(f"Language updated to '{window.translator.lang}' in settings.")

    except Exception as e:
        log_error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### 6.2 Settings 
#### 6.2.1 setting.py

```python
# Load and save settings: which language was selected, settings for project_window
import json
import os

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error

# Import the central settings file path
from config.dev import SETTINGS_FILE

def load_settings():
    log_section("settings.py")
    log_subsection("load_settings")
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                settings = json.load(f)
                log_info(f"Settings loaded from {SETTINGS_FILE}.")
                return settings
        log_info("Settings file not found, using fallback settings.")
        return {"language": "en"}  # Fallback
    except Exception as e:
        log_error(f"Error loading settings: {e}")
        return {"language": "en"}

def save_settings(settings):
    log_section("settings.py")
    log_subsection("save_settings")
    try:
        json_str = json.dumps(settings, indent=2)
        log_info(f"Saving settings to {SETTINGS_FILE}.")
        log_info(f"JSON preview:\n{json_str}")
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            f.write(json_str)
        log_info("Settings saved successfully.")
    except Exception as e:
        log_error(f"Error while saving settings: {e}")
```

#### 6.2.2 dev.py

```python
from pathlib import Path
import sys

# Determine base directory (supports both frozen and script mode)
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

# Main directories
DATA_DIR         = BASE_DIR / "data"
CONFIG_DIR       = BASE_DIR / "config"
ASSETS_DIR       = BASE_DIR / "assets"
DOCS_DIR         = BASE_DIR / "docs"
GUI_DIR          = BASE_DIR / "gui"
CORE_DIR         = BASE_DIR / "core"
TRANSLATIONS_DIR = CORE_DIR / "translations"
TABLES_DIR       = CORE_DIR / "tables"

# Important files
DB_PATH          = DATA_DIR / "csnova.db"
SETTINGS_FILE    = CONFIG_DIR / "user_settings.json"
BG_IMAGE_PATH    = ASSETS_DIR / "media" / "csNova_background_start.png"

# Translation and help files
HELP_DIR         = TRANSLATIONS_DIR / "help"
FORMS_DIR        = TRANSLATIONS_DIR / "forms"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
CONFIG_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)
DOCS_DIR.mkdir(exist_ok=True)
LOG_FILE = BASE_DIR / "csnova.log"
```

#### 6.2.3 logger.py
```python
import datetime
from config.dev import LOG_FILE

def _write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def log_section(section):
    _write_log(f"\n=== [{datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] SECTION: {section} ===")

def log_subsection(subsection):
    _write_log(f"-- [{datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] SUBSECTION: {subsection}")

def log_info(message):
    _write_log(f"[INFO {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")

def log_error(message):
    _write_log(f"[ERROR {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")

def setup_logging():
    log_section("Logging started")

def log_header():
    _write_log("\n==================== CSNova Application Start ====================\n")
```

### 6.3 Datenbank
#### 6.3.1 database.py

```python
import sqlite3

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error

# Import the central database path
from config.dev import DB_PATH

from core.tables.gender_data import data_gender
from core.tables.sex_orientation_data import sex_orientation_data

# Import tables (these should use central paths if needed)
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
    project_objects,
    project_locations,
    project_scene_object_map,
    project_scene_location_map,
    project_scene_storyline_map,
    project_scene_character_map,
    project_character_storyline_map,
    project_character_group_map
)

def init_schema():
    log_section("database.py")
    log_subsection("init_schema")
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            log_info("Database connection established.")
            # Enable foreign key support
            cursor.execute("PRAGMA foreign_keys = ON")
            log_info("Foreign key support enabled.")

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
                project_objects,
                project_locations,
                project_scene_object_map,
                project_scene_location_map,
                project_scene_storyline_map,
                project_scene_character_map,
                project_character_storyline_map,
                project_character_group_map
            ]:
                module.create_table(cursor)
                log_info(f"Table created: {module.__name__}")

            # Insert seed data
            data_gender(cursor)
            log_info("Seed data for gender inserted.")
            sex_orientation_data(cursor)
            log_info("Seed data for sex orientation inserted.")
            conn.commit()
            log_info("Database schema initialized and committed successfully.")
    except Exception as e:
        log_error(f"An error occurred during database initialization: {e}")
```

### 6.4 Translation 

#### 6.4.1 user_settings.json

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

#### 6.4.2 Translator (translator.py)

```python
import json
from config.dev import TRANSLATIONS_DIR, FORMS_DIR, HELP_DIR
from core.logger import log_section, log_subsection, log_info, log_error

class Translator:
    def __init__(self, lang="en"):
        log_section("translator.py")
        log_subsection("__init__")
        try:
            self.lang = lang
            self.translations = self._load_json(TRANSLATIONS_DIR / f"{lang}.json")
            self.form_labels = self._load_json(FORMS_DIR / f"form_{lang}.json")
            self.help_texts = self._load_json(HELP_DIR / f"help_{lang}.json")
            log_info(f"Translator initialized with language '{self.lang}'.")
        except Exception as e:
            log_error(f"Error initializing Translator: {str(e)}")

    def _load_json(self, path):
        log_subsection(f"_load_json: {path}")
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                log_info(f"Loaded translations from {path}")
                return data
        except Exception as e:
            log_error(f"Error loading {path}: {e}")
            return {}

    def set_language(self, lang_code):
        log_subsection("set_language")
        try:
            self.lang = lang_code
            self.translations = self._load_json(TRANSLATIONS_DIR / f"{lang_code}.json")
            self.form_labels = self._load_json(FORMS_DIR / f"form_{lang_code}.json")
            self.help_texts = self._load_json(HELP_DIR / f"help_{lang_code}.json")
            log_info(f"Language set to '{lang_code}'.")
        except Exception as e:
            log_error(f"Error setting language: {str(e)}")

    def tr(self, key):
        log_subsection("tr")
        try:
            value = self.translations.get(key, key)
            log_info(f"Translation for key '{key}': '{value}'")
            return value
        except Exception as e:
            log_error(f"Error translating key '{key}': {str(e)}")
            return key

    def form_label(self, key):
        log_subsection("form_label")
        try:
            value = self.form_labels.get(key, key)
            log_info(f"Form label for key '{key}': '{value}'")
            return value
        except Exception as e:
            log_error(f"Error getting form label for key '{key}': {str(e)}")
            return key

    def help_text(self, key):
        log_subsection("help_text")
        try:
            value = self.help_texts.get(key, "Help and information will be displayed here.")
            log_info(f"Help text for key '{key}': '{value}'")
            return value
        except Exception as e:
            log_error(f"Error getting help text for key '{key}': {str(e)}")
            return "Help and information will be displayed here."
```
### 6.5 GUI
Module für das GUI.

#### 6.5.1 Styles
##### 6.5.1.1 oldschool_style.py

```python
# Old-School style (Windows 10 inspired) with integrated modes

def get_style(mode):
    """
    Returns the style dictionary for the given mode.
    All parameters are defined directly in this file.
    """
    if mode == "light":
        return {
            "background": "#ffffff",
            "foreground": "#222326",
            "button": {
                "background": "#f3f3f3",
                "foreground": "#222326",
                "hover": "#e5e5e5",
                "active": "#d0d0d0"
            },
            "input": {
                "background": "#f9f9f9",
                "foreground": "#222326"
            },
            "border": "#cfcfcf",
            "highlight": "#0078d7",  # Windows 10 blue
            "error": "#e81123"       # Windows error red
        }
    elif mode == "middle":
        return {
            "background": "#f3f3f3",
            "foreground": "#222326",
            "button": {
                "background": "#e5e5e5",
                "foreground": "#222326",
                "hover": "#d0d0d0",
                "active": "#bcbcbc"
            },
            "input": {
                "background": "#ededed",
                "foreground": "#222326"
            },
            "border": "#bcbcbc",
            "highlight": "#0078d7",
            "error": "#e81123"
        }
    elif mode == "dark":
        return {
            "background": "#1e1e1e",
            "foreground": "#f3f3f3",
            "button": {
                "background": "#2d2d2d",
                "foreground": "#f3f3f3",
                "hover": "#3c3c3c",
                "active": "#0078d7"
            },
            "input": {
                "background": "#252526",
                "foreground": "#f3f3f3"
            },
            "border": "#3c3c3c",
            "highlight": "#0078d7",
            "error": "#e81123"
        }
    else:
        # fallback: light
        return {
            "background": "#ffffff",
            "foreground": "#222326",
            "button": {
                "background": "#f3f3f3",
                "foreground": "#222326",
                "hover": "#e5e5e5",
                "active": "#d0d0d0"
            },
            "input": {
                "background": "#f9f9f9",
                "foreground": "#222326"
            },
            "border": "#cfcfcf",
            "highlight": "#0078d7",
            "error": "#e81123"
        }
```

##### 6.5.1.2 vintage_style.py

```python
# Vintage style (cozy living room inspired) with integrated modes

def get_style(mode):
    """
    Returns the style dictionary for the given mode.
    All parameters are defined directly in this file.
    """
    if mode == "light":
        return {
            "background": "#f5eee6",      # warm beige
            "foreground": "#5a4632",      # dark brown
            "button": {
                "background": "#e2d3c3",
                "foreground": "#5a4632",
                "hover": "#d6c3a3",
                "active": "#cbb393"
            },
            "input": {
                "background": "#f8f3ed",
                "foreground": "#5a4632"
            },
            "border": "#cbb393",
            "highlight": "#b48a78",       # warm reddish brown
            "error": "#a94442"            # muted red
        }
    elif mode == "middle":
        return {
            "background": "#e9e2d3",
            "foreground": "#5a4632",
            "button": {
                "background": "#d6c3a3",
                "foreground": "#5a4632",
                "hover": "#cbb393",
                "active": "#b48a78"
            },
            "input": {
                "background": "#ede6d6",
                "foreground": "#5a4632"
            },
            "border": "#b48a78",
            "highlight": "#a67c52",
            "error": "#a94442"
        }
    elif mode == "dark":
        return {
            "background": "#3b2c23",
            "foreground": "#e2d3c3",
            "button": {
                "background": "#5a4632",
                "foreground": "#e2d3c3",
                "hover": "#7c624a",
                "active": "#a67c52"
            },
            "input": {
                "background": "#4e3b2a",
                "foreground": "#e2d3c3"
            },
            "border": "#7c624a",
            "highlight": "#b48a78",
            "error": "#a94442"
        }
    else:
        # fallback: light
        return {
            "background": "#f5eee6",
            "foreground": "#5a4632",
            "button": {
                "background": "#e2d3c3",
                "foreground": "#5a4632",
                "hover": "#d6c3a3",
                "active": "#cbb393"
            },
            "input": {
                "background": "#f8f3ed",
                "foreground": "#5a4632"
            },
            "border": "#cbb393",
            "highlight": "#b48a78",
            "error": "#a94442"
        }
```

##### 6.5.1.3 modern_style.py

```python
# Modern style (Windows 11 inspired) with integrated modes

def get_style(mode):
    """
    Returns the style dictionary for the given mode.
    All parameters are defined directly in this file.
    """
    if mode == "light":
        return {
            "background": "#f3f6fd",      # very light blueish white
            "foreground": "#1a1a1a",      # almost black, but softer
            "button": {
                "background": "#e7eaf3",
                "foreground": "#1a1a1a",
                "hover": "#d0d6e6",
                "active": "#b6c2e1"
            },
            "input": {
                "background": "#ffffff",
                "foreground": "#1a1a1a"
            },
            "border": "#cfd8dc",
            "highlight": "#2563eb",       # modern blue accent
            "error": "#ef4444"            # modern error red
        }
    elif mode == "middle":
        return {
            "background": "#e0e5ef",
            "foreground": "#23272f",
            "button": {
                "background": "#cfd8dc",
                "foreground": "#23272f",
                "hover": "#b6c2e1",
                "active": "#2563eb"
            },
            "input": {
                "background": "#f3f6fd",
                "foreground": "#23272f"
            },
            "border": "#b6c2e1",
            "highlight": "#2563eb",
            "error": "#ef4444"
        }
    elif mode == "dark":
        return {
            "background": "#181a20",
            "foreground": "#e7eaf3",
            "button": {
                "background": "#23272f",
                "foreground": "#e7eaf3",
                "hover": "#2563eb",
                "active": "#1e293b"
            },
            "input": {
                "background": "#23272f",
                "foreground": "#e7eaf3"
            },
            "border": "#2563eb",
            "highlight": "#60a5fa",
            "error": "#ef4444"
        }
    else:
        # fallback: light
        return {
            "background": "#f3f6fd",
            "foreground": "#1a1a1a",
            "button": {
                "background": "#e7eaf3",
                "foreground": "#1a1a1a",
                "hover": "#d0d6e6",
                "active": "#b6c2e1"
            },
            "input": {
                "background": "#ffffff",
                "foreground": "#1a1a1a"
            },
            "border": "#cfd8dc",
            "highlight": "#2563eb",
            "error": "#ef4444"
        }
```

##### 6.5.1.4 future_style.py

```python
# Future style (glassmorphism, adaptive, modern) with integrated modes

def get_style(mode):
    """
    Returns the style dictionary for the given mode.
    All parameters are defined directly in this file.
    """
    if mode == "light":
        return {
            "background": "rgba(245, 250, 255, 0.85)",   # semi-transparent, glass effect
            "foreground": "#22223b",                     # deep blue-grey
            "button": {
                "background": "rgba(230, 240, 255, 0.95)",
                "foreground": "#22223b",
                "hover": "#b8c6db",
                "active": "#7f9acb"
            },
            "input": {
                "background": "rgba(255,255,255,0.95)",
                "foreground": "#22223b"
            },
            "border": "#a3bffa",
            "highlight": "#7f9acb",                      # soft futuristic blue
            "error": "#ff6b6b"                           # neon red
        }
    elif mode == "middle":
        return {
            "background": "rgba(210, 220, 235, 0.90)",
            "foreground": "#22223b",
            "button": {
                "background": "#b8c6db",
                "foreground": "#22223b",
                "hover": "#7f9acb",
                "active": "#a3bffa"
            },
            "input": {
                "background": "rgba(240,245,250,0.95)",
                "foreground": "#22223b"
            },
            "border": "#7f9acb",
            "highlight": "#a3bffa",
            "error": "#ff6b6b"
        }
    elif mode == "dark":
        return {
            "background": "rgba(30, 34, 45, 0.92)",
            "foreground": "#e0eaff",
            "button": {
                "background": "#22223b",
                "foreground": "#e0eaff",
                "hover": "#7f9acb",
                "active": "#a3bffa"
            },
            "input": {
                "background": "rgba(40,44,54,0.95)",
                "foreground": "#e0eaff"
            },
            "border": "#7f9acb",
            "highlight": "#a3bffa",
            "error": "#ff6b6b"
        }
    else:
        # fallback: light
        return {
            "background": "rgba(245, 250, 255, 0.85)",
            "foreground": "#22223b",
            "button": {
                "background": "rgba(230, 240, 255, 0.95)",
                "foreground": "#22223b",
                "hover": "#b8c6db",
                "active": "#7f9acb"
            },
            "input": {
                "background": "rgba(255,255,255,0.95)",
                "foreground": "#22223b"
            },
            "border": "#a3bffa",
            "highlight": "#7f9acb",
            "error": "#ff6b6b"
        }
```

##### 6.5.1.5 style_utils.py

```python
# Utility functions for generating button styles based on the selected style and mode.

from config.settings import load_settings
from gui.styles.oldschool_style import get_style as get_oldschool_style
from gui.styles.vintage_style import get_style as get_vintage_style
from gui.styles.modern_style import get_style as get_modern_style
from gui.styles.future_style import get_style as get_future_style

STYLE_FUNCTIONS = {
    "oldschool": get_oldschool_style,
    "vintage": get_vintage_style,
    "modern": get_modern_style,
    "future": get_future_style
}

def get_current_style():
    """
    Returns the style dictionary for the currently selected style and mode.
    Defaults to modern style and light mode if not set.
    """
    settings = load_settings()
    style_code = settings.get("style", "modern")
    mode_code = settings.get("mode", "light")
    style_func = STYLE_FUNCTIONS.get(style_code, get_modern_style)
    return style_func(mode_code)

def load_button_style(font_size=16):
    """
    Returns the style string for default buttons with dynamic font size,
    using the currently selected style and mode.
    """
    style = get_current_style()
    return f"""
        QPushButton {{
            background-color: {style['button']['background']};
            color: {style['button']['foreground']};
            font-size: {font_size}px;
            border: 2px solid {style['border']};
            border-radius: 8px;
        }}
        QPushButton:hover {{
            background-color: {style['button']['hover']};
        }}
        QPushButton:pressed {{
            background-color: {style['button']['active']};
        }}
    """

def load_active_button_style(font_size=16):
    """
    Returns the style string for active navigation buttons,
    using the currently selected style and mode.
    """
    style = get_current_style()
    return f"""
        QPushButton {{
            background-color: {style['highlight']};
            color: {style['button']['foreground']};
            font-size: {font_size}px;
            border: 2px solid {style['border']};
            border-radius: 8px;
            font-weight: bold;
        }}
    """
```

#### 6.5.1.6 form_styles.py

```python
# Generates the style string for form widgets based on the selected style and mode.

from config.settings import load_settings
from gui.styles.oldschool_style import get_style as get_oldschool_style
from gui.styles.vintage_style import get_style as get_vintage_style
from gui.styles.modern_style import get_style as get_modern_style
from gui.styles.future_style import get_style as get_future_style

STYLE_FUNCTIONS = {
    "oldschool": get_oldschool_style,
    "vintage": get_vintage_style,
    "modern": get_modern_style,
    "future": get_future_style
}

def get_current_style():
    """
    Returns the style dictionary for the currently selected style and mode.
    Defaults to modern style and light mode if not set.
    """
    settings = load_settings()
    style_code = settings.get("style", "modern")
    mode_code = settings.get("mode", "light")
    style_func = STYLE_FUNCTIONS.get(style_code, get_modern_style)
    return style_func(mode_code)

def load_form_style(input_font_size=14, label_font_size=14, input_width=400):
    """
    Returns the style string for form widgets with dynamic font size and width,
    using the currently selected style and mode.
    """
    style = get_current_style()
    return f"""
        QLineEdit, QDateEdit, QSpinBox {{
            padding: 6px;
            border: 1px solid {style['border']};
            border-radius: 4px;
            background-color: {style['input']['background']};
            color: {style['input']['foreground']};
            font-size: {input_font_size}px;
            font-family: 'Segoe UI', sans-serif;
            min-width: {input_width}px;
            max-width: {input_width}px;
        }}

        QLabel {{
            font-size: {label_font_size}px;
            color: {style['foreground']};
        }}

        QFormLayout {{
            margin: 12px;
        }}
    """
```

#### 6.5.2 Panels
##### 6.5.2.1 navigation_panel.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from core.logger import log_section, log_subsection, log_info, log_error

class NavigationPanel(QWidget):
    def __init__(self, keys, translator, button_style, button_style_active, callbacks, parent=None):
        log_section("navigation_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.button_style = button_style
            self.button_style_active = button_style_active
            self.callbacks = callbacks
            self.active_key = None
            self.layout = QVBoxLayout()
            self.buttons = {}

            for key in keys:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setStyleSheet(self.button_style)
                btn.setFixedSize(240, 70)
                btn.clicked.connect(lambda checked, k=key: self._on_nav_clicked(k))
                self.layout.addWidget(btn)
                self.buttons[key] = btn

            self.setLayout(self.layout)
            log_info("NavigationPanel initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing NavigationPanel: {str(e)}")

    def _on_nav_clicked(self, key):
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            # Reset all buttons to default style
            for k, btn in self.buttons.items():
                btn.setStyleSheet(self.button_style)
            # Set active button style
            self.buttons[key].setStyleSheet(self.button_style_active)
            self.active_key = key
            # Call the assigned callback
            if key in self.callbacks:
                self.callbacks[key]()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_error(f"Error in navigation click handler for '{key}': {str(e)}")
```

##### 6.5.2.2 help_panel.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.form_styles import get_current_style
from core.logger import log_section, log_subsection, log_info, log_error

class HelpPanel(QWidget):
    def __init__(self, parent=None):
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.layout = QVBoxLayout()
            self.label = QLabel("Help and information will be displayed here.", self)
            self.label.setWordWrap(True)
            self.layout.addWidget(self.label)
            self.setLayout(self.layout)
            self.apply_style()
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing HelpPanel: {str(e)}")

    def set_help_text(self, text):
        log_subsection("set_help_text")
        try:
            self.label.setText(text)
            log_info("Help text updated in HelpPanel.")
        except Exception as e:
            log_error(f"Error updating help text: {str(e)}")

    def apply_style(self):
        """
        Applies the current style to the help panel.
        """
        style = get_current_style()
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {style['background']};
            }}
            QLabel {{
                color: {style['foreground']};
                font-size: 15px;
                padding: 8px;
            }}
        """)
```

##### 6.5.2.3 center_panel.py

```python
```

### 6.5.3 Widgets
#### 6.5.3.1 form_toolbar.py

```python
from PySide6.QtWidgets import QWidget, QToolBar, QHBoxLayout
from PySide6.QtGui import QAction
from core.logger import log_section, log_subsection, log_info, log_error

class FormToolbar(QWidget):
    def __init__(self, translator, form_prefix, parent=None):
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.toolbar = QToolBar(self)
            self.translator = translator
            # Use form_prefix like "project", "character", etc.
            self.new_action = QAction(self.translator.form_label(f"{form_prefix}_btn_new"), self)
            self.delete_action = QAction(self.translator.form_label(f"{form_prefix}_btn_delete"), self)
            self.prev_action = QAction(self.translator.form_label(f"{form_prefix}_btn_preview"), self)
            self.next_action = QAction(self.translator.form_label(f"{form_prefix}_btn_next"), self)
            self.save_action = QAction(self.translator.form_label(f"{form_prefix}_btn_save"), self)

            self.toolbar.addAction(self.new_action)
            self.toolbar.addAction(self.delete_action)
            self.toolbar.addAction(self.prev_action)
            self.toolbar.addAction(self.next_action)
            self.toolbar.addAction(self.save_action)

            layout = QHBoxLayout(self)
            layout.addWidget(self.toolbar)
            self.setLayout(layout)
            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing FormToolbar: {str(e)}")
```

##### 6.5.3.2 base_form_widget.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QSpinBox, QDateEdit
from gui.widgets.form_toolbar import FormToolbar
from core.logger import log_section, log_subsection, log_info, log_error

class BaseFormWidget(QWidget):
    def __init__(self, title, fields, form_labels, toolbar_actions, form_prefix, parent=None):
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.layout = QVBoxLayout()
            self.title_label = QLabel(title, self)
            self.layout.addWidget(self.title_label)

            self.form_layout = QFormLayout()
            self.inputs = {}

            for field in fields:
                label = form_labels.get(field["label_key"], field["default_label"])
                if field["type"] == "text":
                    input_widget = QLineEdit(self)
                elif field["type"] == "spin":
                    input_widget = QSpinBox(self)
                    if "max" in field:
                        input_widget.setMaximum(field["max"])
                elif field["type"] == "date":
                    input_widget = QDateEdit(self)
                else:
                    input_widget = QLineEdit(self)
                self.inputs[field["name"]] = input_widget
                self.form_layout.addRow(label, input_widget)

            self.layout.addLayout(self.form_layout)

            self.toolbar = FormToolbar(self.translator, form_prefix, self)
            if toolbar_actions:
                toolbar_actions(self.toolbar)
            self.layout.addWidget(self.toolbar)

            self.setLayout(self.layout)
            log_info("BaseFormWidget initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing BaseFormWidget: {str(e)}")
```

##### 6.5.3.3 form_chapters.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class ChaptersForm(QWidget):
    """
    Form widget for chapter data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_chapters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "chapter_title", "label_key": "chapter_title", "default_label": "Title", "type": "text"},
                {"name": "chapter_number", "label_key": "chapter_number", "default_label": "Number", "type": "spin", "max": 999},
                {"name": "chapter_summary", "label_key": "chapter_summary", "default_label": "Summary", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("chapter_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="chapter",
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ChaptersForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ChaptersForm: {str(e)}")

    def _on_save(self):
        """
        Handle save action for chapter form.
        """
        log_subsection("_on_save")
        log_info("ChaptersForm save triggered.")
```

##### 6.5.3.4 form_characters.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class CharactersForm(QWidget):
    """
    Form widget for character data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_characters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "character_name", "label_key": "character_name", "default_label": "Name", "type": "text"},
                {"name": "character_nickname", "label_key": "character_nickname", "default_label": "Nickname", "type": "text"},
                {"name": "character_gender", "label_key": "character_gender", "default_label": "Gender", "type": "text"},
                {"name": "character_age", "label_key": "character_age", "default_label": "Age", "type": "spin", "max": 120},
                {"name": "character_role", "label_key": "character_role", "default_label": "Role", "type": "text"},
                {"name": "character_description", "label_key": "character_description", "default_label": "Description", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("character_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="character",
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("CharactersForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing CharactersForm: {str(e)}")

    def _on_save(self):
        """
        Handle save action for character form.
        """
        log_subsection("_on_save")
        log_info("CharactersForm save triggered.")
```

##### 6.5.3.5 form_locations.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class LocationsForm(QWidget):
    """
    Form widget for location data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_locations.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "location_name", "label_key": "location_name", "default_label": "Name", "type": "text"},
                {"name": "location_type", "label_key": "location_type", "default_label": "Type", "type": "text"},
                {"name": "location_description", "label_key": "location_description", "default_label": "Description", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("location_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="location",
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("LocationsForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing LocationsForm: {str(e)}")

    def _on_save(self):
        """
        Handle save action for location form.
        """
        log_subsection("_on_save")
        log_info("LocationsForm save triggered.")
```

##### 6.5.3.6 form_objects.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class ObjectsForm(QWidget):
    """
    Form widget for object data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_objects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "object_name", "label_key": "object_name", "default_label": "Name", "type": "text"},
                {"name": "object_type", "label_key": "object_type", "default_label": "Type", "type": "text"},
                {"name": "object_description", "label_key": "object_description", "default_label": "Description", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("object_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="object",
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ObjectsForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ObjectsForm: {str(e)}")

    def _on_save(self):
        """
        Handle save action for object form.
        """
        log_subsection("_on_save")
        log_info("ObjectsForm save triggered.")
```

##### 6.5.3.7 form_projects.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class ProjectForm(QWidget):
    """
    Form widget for project data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_projects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "title", "label_key": "project_title", "default_label": "Title", "type": "text"},
                {"name": "subtitle", "label_key": "project_subtitle", "default_label": "Subtitle", "type": "text"},
                {"name": "author", "label_key": "project_author", "default_label": "Author", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("project_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="project",
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ProjectForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ProjectForm: {str(e)}")

    def _on_save(self):
        """
        Handle save action for project form.
        """
        log_subsection("_on_save")
        log_info("ProjectForm save triggered.")
```

##### 6.5.3.8 form_scenes.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class ScenesForm(QWidget):
    """
    Form widget for scene data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_scenes.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "scene_title", "label_key": "scene_title", "default_label": "Title", "type": "text"},
                {"name": "scene_number", "label_key": "scene_number", "default_label": "Number", "type": "spin", "max": 9999},
                {"name": "scene_summary", "label_key": "scene_summary", "default_label": "Summary", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("scene_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="scene",
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ScenesForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ScenesForm: {str(e)}")

    def _on_save(self):
        """
        Handle save action for scene form.
        """
        log_subsection("_on_save")
        log_info("ScenesForm save triggered.")
```

##### 6.5.3.9 form_storylines.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class StorylinesForm(QWidget):
    """
    Form widget for storyline data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_storylines.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            fields = [
                {"name": "storyline_title", "label_key": "storyline_title", "default_label": "Title", "type": "text"},
                {"name": "storyline_summary", "label_key": "storyline_summary", "default_label": "Summary", "type": "text"},
                {"name": "storyline_notes", "label_key": "storyline_notes", "default_label": "Notes", "type": "text"},
                # ... add more fields as needed ...
            ]
            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)
            self.form = BaseFormWidget(
                title=self.translator.form_label("storyline_form_label"),
                fields=fields,
                form_labels=self.translator.form_labels,
                toolbar_actions=toolbar_actions,
                form_prefix="storyline",
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("StorylinesForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing StorylinesForm: {str(e)}")

    def _on_save(self):
        """
        Handle save action for storyline form.
        """
        log_subsection("_on_save")
        log_info("StorylinesForm save triggered.")
```

##### 6.5.3.10 form_start.py
```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error

class StartForm(QWidget):
    """
    Completely empty form widget for the start window.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_start.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Empty layout
            layout = QVBoxLayout()
            self.setLayout(layout)

            log_info("StartForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing StartForm: {str(e)}")
```

#### 6.5.4 Fenster
##### 6.5.4.1 start_window.py

```python
# Main window with buttons for creating a new project, loading an existing project,
# main settings for GUI positions and changing after resizing the window

from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import QTimer
from gui.preferences import PreferencesWindow
from core.translator import Translator
from gui.project_window import ProjectWindow
from gui.styles.style_utils import load_button_style

import sys

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error

# Import the central background image path
from config.dev import BG_IMAGE_PATH

class StartWindow(QWidget):
    DEFAULT_WIDTH        = 1920
    DEFAULT_HEIGHT       = 1080
    BUTTON_WIDTH         = 240
    BUTTON_HEIGHT        = 70
    BUTTON_TOP_OFFSET    = 220
    BUTTON_LEFT_OFFSET   = 1380
    BUTTON_SPACING       = 44

    def __init__(self, default_language="en"):
        log_section("start_window.py")
        log_subsection("__init__")
        try:
            super().__init__()
            self.translator = Translator(default_language)
            self.setWindowTitle(self.translator.tr("start_window_title"))
            self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
            self.setAutoFillBackground(False)
            self.bg_pixmap = QPixmap(str(BG_IMAGE_PATH))
            self.pref_window = None
            self._create_ui()
            self._retranslate_and_position()
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing StartWindow: {str(e)}")
            
    def _create_ui(self):
        log_subsection("_create_ui")
        try:
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

            # Connect new_project button
            self.buttons[0].clicked.connect(self._new_project)

            # Connect load_project button
            self.buttons[1].clicked.connect(self._load_project)

            # Connect settings button
            self.buttons[2].clicked.connect(self._open_preferences)

            # Connect help button
            self.buttons[3].clicked.connect(self._help)

            # Connect exit button
            self.buttons[4].clicked.connect(self._exit_application)
            log_info("UI created and buttons connected.")
        except Exception as e:
            log_error(f"Error creating UI: {str(e)}")

    def _open_preferences(self):
        log_subsection("_open_preferences")
        try:
            # Open preferences window only if not already open
            if self.pref_window is None or not self.pref_window.isVisible():
                self.pref_window = PreferencesWindow(self)
                self.pref_window.show()
                log_info("Preferences window opened.")
            else:
                self.pref_window.raise_()
                self.pref_window.activateWindow()
                log_info("Preferences window focused.")
        except Exception as e:
            log_error(f"Error opening preferences window: {str(e)}")

    def _new_project(self):
        log_subsection("_new_project")
        try:
            log_info("Preparing new project...")
            self.project_window = ProjectWindow(translator=self.translator)
            self.project_window.show()
            QTimer.singleShot(100, lambda: self.hide())
            log_info("ProjectWindow shown and StartWindow hidden.")
        except Exception as e:
            log_error(f"Error preparing new project: {str(e)}")

    def _load_project(self):
        log_subsection("_load_project")
        try:
            log_info("Preparing to load project...")
            # Implement loading logic here
        except Exception as e:
            log_error(f"Error preparing to load project: {str(e)}")

    def _help(self):
        log_subsection("_help")
        try:
            log_info("Preparing help function...")
            # Implement help logic here
        except Exception as e:
            log_error(f"Error preparing help function: {str(e)}")

    def _exit_application(self):
        log_subsection("_exit_application")
        try:
            log_info("Exiting application...")
            QApplication.instance().quit()
        except Exception as e:
            log_error(f"Error during application exit: {str(e)}")

    def _on_language_changed(self, code):
        log_subsection("_on_language_changed")
        try:
            self.translator.set_language(code)
            self._retranslate_and_position()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_error(f"Error changing language: {str(e)}")

    def _retranslate_and_position(self):
        log_subsection("_retranslate_and_position")
        try:
            # Update button texts and window title
            for key, btn in zip(self.button_keys, self.buttons):
                btn.setText(self.translator.tr(key))
            self.setWindowTitle(self.translator.tr("start_window_title"))
            self.update_button_positions()
            log_info("Button texts and window title updated.")
        except Exception as e:
            log_error(f"Error updating translations and positions: {str(e)}")

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
        log_subsection("update_button_positions")
        try:
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
            style = load_button_style(font_px)
            for i, btn in enumerate(self.buttons):
                x = int(x_off)
                y = int(y_off + i * (bh + spacing))
                btn.setGeometry(x, y, bw, bh)
                btn.setStyleSheet(style)
            log_info("Button positions updated.")
        except Exception as e:
            log_error(f"Error updating button positions: {str(e)}")

if __name__ == "__main__":
    log_section("start_window.py")
    log_subsection("__main__")
    try:
        app = QApplication(sys.argv)
        window = StartWindow(default_language="en")
        window.show()
        log_info("StartWindow shown.")
        sys.exit(app.exec())
     except Exception as e:
        log_error(f"Error in main: {str(e)}")
```
##### 6.5.4.2 preferences.py

```python
from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout, QWidget
)
from core.translator import Translator
from config.settings import load_settings, save_settings

# Importiere die Style-Module
from gui.styles.oldschool_style import get_style as get_oldschool_style
from gui.styles.vintage_style import get_style as get_vintage_style
from gui.styles.modern_style import get_style as get_modern_style
from gui.styles.future_style import get_style as get_future_style

from core.logger import log_section, log_subsection, log_info, log_error

class PreferencesWindow(QDialog):
    DEFAULT_WIDTH  = 400
    DEFAULT_HEIGHT = 260

    LANGUAGE_NAMES = {
        "de": "Deutsch",
        "en": "English",
        "fr": "Français",
        "es": "Español"
    }

    STYLE_NAMES = {
        "oldschool": "Old-School",
        "vintage": "Vintage",
        "modern": "Modern",
        "future": "Future"
    }

    STYLE_FUNCTIONS = {
        "oldschool": get_oldschool_style,
        "vintage": get_vintage_style,
        "modern": get_modern_style,
        "future": get_future_style
    }

    MODE_NAMES = {
        "light": "Light",
        "middle": "Middle",
        "dark": "Dark"
    }

    def __init__(self, parent=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = parent.translator
            self.settings   = load_settings()
            self.original_language = self.translator.lang

            self.setWindowTitle(self.translator.tr("menu_settings"))
            self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)

            self._init_ui()
            self._load_values()
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing PreferencesWindow: {str(e)}")

    def _init_ui(self):
        log_subsection("_init_ui")
        try:
            # Language selection
            self.lang_label = QLabel(self.translator.tr("menu_language"), self)
            self.lang_combo = QComboBox(self)
            for code in self.LANGUAGE_NAMES:
                name = self.LANGUAGE_NAMES[code]
                self.lang_combo.addItem(name, userData=code)
            self.lang_combo.currentIndexChanged.connect(self._on_language_changed)

            # Style selection
            self.style_label = QLabel("Style", self)
            self.style_combo = QComboBox(self)
            for code in self.STYLE_NAMES:
                self.style_combo.addItem(self.STYLE_NAMES[code], userData=code)
            self.style_combo.currentIndexChanged.connect(self._on_style_or_mode_changed)

            # Mode selection
            self.mode_label = QLabel("Modus", self)
            self.mode_combo = QComboBox(self)
            for code in self.MODE_NAMES:
                self.mode_combo.addItem(self.MODE_NAMES[code], userData=code)
            self.mode_combo.currentIndexChanged.connect(self._on_style_or_mode_changed)

            # Style preview (Button)
            self.preview_label = QLabel("Vorschau:", self)
            self.preview_button = QPushButton("Beispiel-Button", self)
            self.preview_button.setFixedSize(180, 40)

            # Buttons
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
            main_layout.addWidget(self.style_label)
            main_layout.addWidget(self.style_combo)
            main_layout.addWidget(self.mode_label)
            main_layout.addWidget(self.mode_combo)
            main_layout.addWidget(self.preview_label)
            main_layout.addWidget(self.preview_button)
            main_layout.addLayout(btn_layout)
            self.setLayout(main_layout)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing UI: {str(e)}")

    def _load_values(self):
        log_subsection("_load_values")
        try:
            # Language
            lang = self.settings.get("language", "en")
            idx  = list(self.LANGUAGE_NAMES.keys()).index(lang) if lang in self.LANGUAGE_NAMES else 0
            self.lang_combo.setCurrentIndex(idx)
            # Style
            style = self.settings.get("style", "modern")
            idx = list(self.STYLE_NAMES.keys()).index(style) if style in self.STYLE_NAMES else 2  # modern als Default
            self.style_combo.setCurrentIndex(idx)
            # Mode
            mode = self.settings.get("mode", "light")
            idx = list(self.MODE_NAMES.keys()).index(mode) if mode in self.MODE_NAMES else 0
            self.mode_combo.setCurrentIndex(idx)
            self._update_ui_texts()
            self._update_preview()
            log_info("Values loaded and UI texts updated.")
        except Exception as e:
            log_error(f"Error loading values: {str(e)}")

    def _on_language_changed(self):
        log_subsection("_on_language_changed")
        try:
            index = self.lang_combo.currentIndex()
            code = self.lang_combo.itemData(index)
            self.translator.set_language(code)
            self._update_ui_texts()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_error(f"Error changing language: {str(e)}")

    def _on_style_or_mode_changed(self):
        self._update_preview()

    def _update_ui_texts(self):
        log_subsection("_update_ui_texts")
        try:
            self.setWindowTitle(self.translator.tr("menu_settings"))
            self.lang_label.setText(self.translator.tr("menu_language"))
            self.style_label.setText("Style")
            self.mode_label.setText("Modus")
            self.preview_label.setText("Vorschau:")
            self.ok_button.setText(self.translator.tr("action_save"))
            self.cancel_button.setText(self.translator.tr("action_cancel"))
            log_info("UI texts updated.")
        except Exception as e:
            log_error(f"Error updating UI texts: {str(e)}")

    def _update_preview(self):
        # Zeigt den Style und Modus direkt am Beispiel-Button
        style_code = self.style_combo.itemData(self.style_combo.currentIndex())
        mode_code = self.mode_combo.itemData(self.mode_combo.currentIndex())
        style_func = self.STYLE_FUNCTIONS.get(style_code, get_modern_style)
        style_dict = style_func(mode_code)
        # Beispiel: Button-Style als CSS generieren
        btn_style = f"""
            QPushButton {{
                background-color: {style_dict['button']['background']};
                color: {style_dict['button']['foreground']};
                border: 2px solid {style_dict['border']};
                border-radius: 8px;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {style_dict['button']['hover']};
            }}
            QPushButton:pressed {{
                background-color: {style_dict['button']['active']};
            }}
        """
        self.preview_button.setStyleSheet(btn_style)

    def _on_ok(self):
        log_subsection("_on_ok")
        try:
            self.settings["language"] = self.lang_combo.itemData(self.lang_combo.currentIndex())
            self.settings["style"]    = self.style_combo.itemData(self.style_combo.currentIndex())
            self.settings["mode"]     = self.mode_combo.itemData(self.mode_combo.currentIndex())
            save_settings(self.settings)
            if self.parent() and hasattr(self.parent(), "_on_language_changed"):
                self.parent()._on_language_changed(self.settings["language"])
            self.accept()
            log_info("Settings saved and dialog accepted.")
        except Exception as e:
            log_error(f"Error saving settings: {str(e)}")

    def _on_cancel(self):
        log_subsection("_on_cancel")
        try:
            self.translator.set_language(self.original_language)
            if self.parent() and hasattr(self.parent(), "_on_language_changed"):
                self.parent()._on_language_changed(self.original_language)
            self.reject()
            log_info("Dialog canceled and language reverted.")
        except Exception as e:
            log_error(f"Error initializing PreferencesWindow: {str(e)}")
```

##### 6.5.4.3 project_window.py

```python
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSplitter, QHBoxLayout

from gui.styles.style_utils import load_button_style, load_active_button_style
from core.translator import Translator
from config.settings import load_settings, save_settings
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.help_panel import HelpPanel

# Import modular forms
from gui.widgets.form_projects import ProjectForm
from gui.widgets.form_characters import CharactersForm
from gui.widgets.form_storylines import StorylinesForm
from gui.widgets.form_chapters import ChaptersForm
from gui.widgets.form_scenes import ScenesForm
from gui.widgets.form_objects import ObjectsForm
from gui.widgets.form_locations import LocationsForm
from gui.widgets.form_start import StartForm

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error

class ProjectWindow(QWidget):
    BUTTON_WIDTH = 240
    BUTTON_HEIGHT = 70

    def __init__(self, translator=None, parent=None):
        log_section("project_window.py")
        log_subsection("__init__")
        try:
            self.translator = translator or Translator(lang="en")
            super().__init__(parent)
            self.resize(1600, 900)
            self.setWindowTitle(self.translator.tr("project_window_title"))
            self.settings = load_settings()
            self.button_style = load_button_style(18)
            self.button_style_active = load_active_button_style(18)
            self.active_nav_key = None
            self._set_background()
            self._init_ui()
            log_info("ProjectWindow initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ProjectWindow: {str(e)}")

    def _set_background(self):
        log_subsection("_set_background")
        try:
            palette = self.palette()
            palette.setColor(QPalette.Window, QColor("#f0f0f0"))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
            log_info("Background set successfully.")
        except Exception as e:
            log_error(f"Error setting background: {str(e)}")

    def _init_ui(self):
        log_subsection("_init_ui")
        try:
            keys = [
                "btn_project", "btn_characters", "btn_storylines",
                "btn_chapters", "btn_scenes", "btn_objects", "btn_locations", "btn_exit"
            ]
            callbacks = {
                "btn_project": lambda: self._on_nav_clicked("btn_project", self._show_project_form),
                "btn_characters": lambda: self._on_nav_clicked("btn_characters", self._show_characters_form),
                "btn_storylines": lambda: self._on_nav_clicked("btn_storylines", self._show_storylines_form),
                "btn_chapters": lambda: self._on_nav_clicked("btn_chapters", self._show_chapters_form),
                "btn_scenes": lambda: self._on_nav_clicked("btn_scenes", self._show_scenes_form),
                "btn_objects": lambda: self._on_nav_clicked("btn_objects", self._show_objects_form),
                "btn_locations": lambda: self._on_nav_clicked("btn_locations", self._show_locations_form),
                "btn_exit": self._exit_application
            }
            self.navigation_panel = NavigationPanel(
                keys, self.translator, self.button_style, self.button_style_active, callbacks, self
            )

            self.help_panel = HelpPanel(self)
            # Start with project form
            self.form_widget = StartForm(self.translator, self)

            self.splitter = QSplitter(Qt.Horizontal)
            self.splitter.addWidget(self.navigation_panel)
            self.splitter.addWidget(self.form_widget)
            self.splitter.addWidget(self.help_panel)
            self.splitter.setSizes(self.settings.get("splitter_sizes", [300, 900, 300]))

            layout = QHBoxLayout(self)
            layout.addWidget(self.splitter)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing UI: {str(e)}")

    def _on_nav_clicked(self, key, handler):
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            self.active_nav_key = key
            handler()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_error(f"Error in navigation click handler for '{key}': {str(e)}")

    def _show_project_form(self):
        log_subsection("_show_project_form")
        try:
            form_widget = ProjectForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_project")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Project form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying project form: {str(e)}")

    def _show_characters_form(self):
        log_subsection("_show_characters_form")
        try:
            form_widget = CharactersForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_characters")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Characters form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying characters form: {str(e)}")

    def _show_storylines_form(self):
        log_subsection("_show_storylines_form")
        try:
            form_widget = StorylinesForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_storylines")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Storylines form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying storylines form: {str(e)}")

    def _show_chapters_form(self):
        log_subsection("_show_chapters_form")
        try:
            form_widget = ChaptersForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_chapters")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Chapters form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying chapters form: {str(e)}")

    def _show_scenes_form(self):
        log_subsection("_show_scenes_form")
        try:
            form_widget = ScenesForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_scenes")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Scenes form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying scenes form: {str(e)}")

    def _show_objects_form(self):
        log_subsection("_show_objects_form")
        try:
            form_widget = ObjectsForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_objects")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Objects form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying objects form: {str(e)}")

    def _show_locations_form(self):
        log_subsection("_show_locations_form")
        try:
            form_widget = LocationsForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_locations")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Locations form displayed successfully.")
        except Exception as e:
            log_error(f"Error displaying locations form: {str(e)}")

    def _replace_form_widget(self, new_widget):
        """
        Replace the current form widget in the splitter.
        """
        old_widget = self.splitter.widget(1)
        if old_widget:
            old_widget.setParent(None)
        self.splitter.insertWidget(1, new_widget)

    def _exit_application(self):
        log_subsection("_exit_application")
        try:
            self.close()
            log_info("Application exit triggered.")
        except Exception as e:
            log_error(f"Error during application exit: {str(e)}")

    def closeEvent(self, event):
        log_subsection("closeEvent")
        try:
            self.settings["splitter_sizes"] = self.splitter.sizes()
            save_settings(self.settings)
            event.accept()
            log_info("Splitter sizes saved and application closed.")
        except Exception as e:
            log_error(f"Error saving splitter sizes on close: {str(e)}")
            event.accept()
```

## 7 Vorbereitungen für die Installation unter Linux-Mint

### 7.1 .gitignore

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

### 7.2 Abhängigkeiten (requirements.txt)

```text
pyside6
ebooklib
weasyprint
reportlab
requests
asyncio
pyinstaller
```

### 7.3 Pyinstaller

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

### 7.4 Setup (install_csnova.sh)

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

## 8. Tutorials & Literatur, Quellen

### 8.1 PySide6 & GUI-Entwicklung

- Create GUI Applications with Python & Qt6 – Martin Fitzpatrick  
- Modern UI mit PySide6 – komplette App  
- Install & Setup PySide6 and Qt Designer  
- PySide6 + SQLite integration – Qt‑Dokumentation  

### 8.2 Datenbank & Migration

- SQL für Einsteiger – Michael Kofler  
- SQLite Tutorial – Jacek Artymiak  
- SQLite Crash Course – freeCodeCamp  
- Datenbankmigration mit Alembic – Heise Developer  
- SQLAlchemy Getting Started  

### 8.3 Multimedia & Animation

- Multimedia Programming with Qt – Marco Piccolino  
- QtMultimedia Tutorial – Audio & Video  
- QML Animation Basics – Qt Academy  
- Multimedia & QML – Best Practices  
- PySide6 Animation Tutorial  
- QtMultimedia Docs  

### 8.4 Exportformate & Reader

- Creating EPUBs with ebooklib – Python Publishing Guide  
- PDF-Export mit ReportLab – Python Tutorials  
- HTML-Export mit WeasyPrint – Web2PDF mit CSS  
- Reader-Entwicklung mit QWebEngineView – Qt Blog  
- ebooklib Dokumentation  
- ReportLab User Guide  
- WeasyPrint Docs  

### 8.5 KI-Integration

- Hands-On AI with Python – Packt Publishing  
- OpenAI API Integration – Python Tutorial  


## 9. Lizenz
# Lizenzbedingungen für Codices Scriptoria Nova (CSNova)

## Verwendete Drittanbieter-Bibliotheken

Dieses Projekt verwendet folgende externe Bibliotheken:

- **PySide6** (LGPL)
- **ebooklib** (Apache License 2.0)
- **WeasyPrint** (BSD)
- **ReportLab** (BSD)
- **Requests** (Apache License 2.0)
- **asyncio** (Python Standard Library, PSF License)
- **PyInstaller** (GPL)

Die jeweiligen Lizenztexte finden Sie in den offiziellen Repositories der Bibliotheken.  
Es wurden keine Änderungen an den Originalquellen vorgenommen.


## Einleitung

Die Lizenzstruktur von *Codices Scriptoria Nova* orientiert sich an der Welt mittelalterlicher Schreibstuben und spiegelt die Vielfalt moderner Autor:innen wider. Drei klar definierte Versionen – **Novitia**, **Magister** und **Collegium** – ermöglichen eine faire und transparente Nutzung der Software, abgestimmt auf individuelle und gemeinschaftliche Bedürfnisse.

## CSNova – Hauptanwendung

CSNova ist Open Source Software. Sie darf unter den Bedingungen der jeweiligen Version genutzt und weitergegeben werden.

### Lizenzübersicht

Es existieren drei Versionen:

Die Nutzung aller drei Versionen setzt eine Registrierung voraus.

- **CSNova Novitia** – eine **kostenlose Version** für die **nicht kommerzielle Nutzung**, z. B. durch angehende Autor:innen, zu Testzwecken oder in Bildungseinrichtungen (Schulen, Universitäten, Volkshochschulen und sonstige Bildungseinrichtungen).  

- **CSNova Magister** – eine **kostenpflichtige Version** für einzelne Autor:innen, die das Programm professionell nutzen und ein Jahreseinkommen von über 50.000 € erzielen.  
 
  Das Jahreseinkommen bezieht sich auf Einnahmen aus schriftstellerischer Tätigkeit, die mithilfe der Software erzielt werden. Professionelle Nutzung bezeichnet den regelmäßigen Einsatz der Software zur Erstellung, Veröffentlichung oder Vermarktung literarischer Werke mit kommerziellem Zweck.

- **CSNova Collegium** – eine Version für Autor:innen, die im Team das Programm professionell nutzen.  

  Professionelle Nutzung bezeichnet den regelmäßigen Einsatz der Software zur Erstellung, Veröffentlichung oder Vermarktung literarischer Werke mit kommerziellem Zweck.

#### Zusammenfassung der Lizenzversionen

| Version              | Zielgruppe                         | Nutzungstyp                   | Lizenzstatus                         |
|----------------------|------------------------------------|--------------------------------|--------------------------------------|
| **CSNova Novitia**   | Lernende, Bildungseinrichtungen    | Nicht-kommerziell              | Kostenlos (mit Registrierung)        |
| **CSNova Magister**  | Einzelautor:innen mit Einkommen >50.000 € | Professionell (Einzelnutzung) | Kostenpflichtig (mit Registrierung) |
| **CSNova Collegium** | Autor:innen-Teams                  | Professionell (Teamnutzung)    | Kostenpflichtig (mit Registrierung) |

### Änderungen und Weitergabe 

Änderungen am Quellcode und die Weitergabe modifizierter Versionen sind gestattet, sofern die modifizierten Versionen ebenfalls unter einer Open Source Lizenz veröffentlicht werden. 

Die Nutzung des Namens „CSNova“, „Codices Scriptoria Nova“, „CSNova Novitia“, „CSNova Magister“ oder „CSNova Collegium“ für modifizierte Versionen ist nur mit schriftlicher Genehmigung des Autors gestattet. Der Autor übernimmt **keine Haftung** für Schäden, die durch veränderte Versionen oder deren Inhalte entstehen – nsbesondere nicht für Inhalte, die ohne seine Zustimmung verändert worden sind oder unter einem der genannten Namen veröffentlicht wurden.

## CSNova-Reader

Der CSNova-Reader ist **Open Source** und steht **ohne Lizenzgebühren** zur Verfügung. Die Nutzung unterliegt den unten genannten Einschränkungen.  
*Die Nutzung setzt eine Registrierung voraus.*

Er darf kostenfrei genutzt, kopiert und weitergegeben werden – sowohl privat als auch kommerziell.

### Einschränkungen der kommerziellen Nutzung

Der CSNova-Reader darf kommerziell genutzt werden, z.B. zur Veröffentlichung von Büchern, Editionen oder anderen Produkten.

Ein Verkauf oder Vertrieb des CSNova-Readers als eigenständiges Produkt ist **nicht gestattet**.

### Änderungen und Weitergabe

Änderungen am CSNova-Reader sind gestattet, sofern die modifizierten Versionen ebenfalls unter einer Open Source Lizenz veröffentlicht werden und dauerhaft kostenfrei nutzbar bleiben.

Die Nutzung des Namens „CSNova“, „Codices Scriptoria Nova“, „CSNova-Reader“, „CSNova Novitia“, „CSNova Magister“ oder „CSNova Collegium“ für modifizierte Versionen des CSNova-Readers ist **nur mit schriftlicher Genehmigung des Autors** gestattet. Der Autor übernimmt **keine Haftung** für Schäden, die durch veränderte Versionen oder deren Inhalte entstehen – insbesondere nicht für Inhalte, die ohne seine Zustimmung verändert oder unter einem der genannten Namen veröffentlicht wurden.

## Allgemeine Hinweise

* Die Software wird ohne Gewähr bereitgestellt. Es besteht kein Anspruch auf Support oder Updates.
* Die Namensrechte an „CSNova“, „Codices Scriptoria Nova“, „CSNova-Reader“, „CSNova Novitia“, „CSNova Magister“ und „CSNova Collegium“ verbleiben beim Autor.
* Die Nutzung der Software setzt die Anerkennung dieser Lizenzbedingungen voraus.

© 2025 Frank Reiser  
### Kontakt: [reiserfrank@t-online.de](mailto:reiserfrank@t-online.de)
