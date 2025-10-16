import sys
import locale
from PySide6.QtWidgets import (
    QApplication, QLabel, QWidget, 
    QVBoxLayout, QSizePolicy, QSplitter, 
    QMainWindow, QComboBox, QLineEdit, 
    QSpinBox, QTextEdit, QDateEdit,
    QCheckBox)
from PySide6.QtGui import QFont, QIcon, QRegularExpressionValidator
from PySide6 import QtUiTools, QtGui, QtCore
from PySide6.QtCore import QDate, QRegularExpression
import json
from pathlib import Path
from config.dev import ASSETS_DIR, GUI_DIR
from config.settings import load_settings, save_settings
from core.logger import log_info, log_error, setup_logging, log_header, log_exception
from datetime import datetime

UI_FILE = GUI_DIR / "csNova.ui"
START_UI_FILE = GUI_DIR / "csNova_Start.ui"
SECURE_UI_FILE = GUI_DIR / "formSecure.ui"
PROJECTS_UI_FILE = GUI_DIR / "csNova_Projects.ui"
CHARACTERS_UI_FILE = GUI_DIR / "csNova_Characters.ui"
OBJECTS_UI_FILE = GUI_DIR / "csNova_Objects.ui"
LOCATIONS_UI_FILE = GUI_DIR / "csNova_Locations.ui"
STORYLINES_UI_FILE = GUI_DIR / "csNova_Storylines.ui"
EDITOR_UI_FILE = GUI_DIR / "csNova_Editor.ui"
PREFERENCES_UI_FILE = GUI_DIR / "csNova_Preferences.ui"
HELP_UI_FILE = GUI_DIR / "csNova_Help_Tips.ui"

main_window_ref = None
start_window_ref = None
help_window_ref = None

# Fensterereignisse verbinden, um UI-Einstellungen zu speichern
class DynamicWindow(QMainWindow):
    def __init__(self, settings_key, ui_file, splitter_name="mainSplitter"):
        super().__init__()
        self.settings_key = settings_key
        loader = QtUiTools.QUiLoader()
        ui = loader.load(str(ui_file), self)
        self.setCentralWidget(ui)
        self.setWindowIcon(QIcon(str(ASSETS_DIR / "media" / "csnova.png")))
        self.setWindowFlags(QtGui.Qt.Window)
        apply_ui_settings(self, settings_key, splitter_name=splitter_name)
        connect_dynamic_events(self, splitter_name=splitter_name)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        settings = load_settings()
        ui_settings = settings.get(self.settings_key, {})
        if not self.isMaximized():
            size = self.size()
            ui_settings["win_width"] = size.width()
            ui_settings["win_height"] = size.height()
        settings[self.settings_key] = ui_settings
        save_settings(settings)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            settings = load_settings()
            ui_settings = settings.get(self.settings_key, {})
            ui_settings["win_maximized"] = self.isMaximized()
            settings[self.settings_key] = ui_settings
            save_settings(settings)
        super().changeEvent(event)
# Splitter-Events verbinden, um Positionen zu speichern
def connect_dynamic_events(self, splitter_name=None):
    if splitter_name:
        splitter = self.centralWidget().findChild(QSplitter, splitter_name)
        if splitter:
            def on_splitter_size_changed():
                settings = load_settings()
                ui_settings = settings.get(self.settings_key, {})
                ui_settings["win_splitter"] = splitter.sizes()
                settings[self.settings_key] = ui_settings
                save_settings(settings)
            splitter.splitterMoved.connect(lambda pos, index: on_splitter_size_changed())

# Alter berechnen aus Geburts- und Sterbedatum
def calculate_age(birth_str, died_str):
    # Versuche das Datum zu parsen (Format: TT.MM.JJJJ)
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, "%d.%m.%Y")
        except Exception:
            return None

    birth_date = parse_date(birth_str)
    died_date = parse_date(died_str)

    if birth_date:
        if died_date:
            age = died_date.year - birth_date.year - ((died_date.month, died_date.day) < (birth_date.month, birth_date.day))
        else:
            today = datetime.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return str(age)
    return ""

# Welche Sprache verwendet das System?
def get_system_language():
    lang_tuple = locale.getlocale()
    lang = lang_tuple[0] if lang_tuple and lang_tuple[0] else "en"
    return lang.split('_')[0]

# UI-Einstellungen laden und anwenden
def apply_ui_settings(window, settings_key, splitter_name=None):
    settings = load_settings()
    ui_settings = settings.get(settings_key, {})
    # Fenstergröße und Maximierung
    if ui_settings.get("win_maximized", False):
        window.showMaximized()
    else:
        width = ui_settings.get("win_width", 800)
        height = ui_settings.get("win_height", 600)
        window.resize(width, height)
    # Splitter-Positionen setzen nach dem Anzeigen
    if splitter_name and "win_splitter" in ui_settings:
        def set_splitter_sizes():
            splitter = window.findChild(QSplitter, splitter_name)
            if splitter:
                splitter.setSizes(ui_settings["win_splitter"])
        QtCore.QTimer.singleShot(0, set_splitter_sizes)

# Sicherheitsabfrage vor dem Beenden
def show_secure_dialog(parent=None, action="exit", project_key=None, on_confirm=None):
    loader = QtUiTools.QUiLoader()
    secure_window = loader.load(str(SECURE_UI_FILE), parent)
    if secure_window is None:
        log_error(f"Konnte UI-Datei nicht laden: {SECURE_UI_FILE}")
        raise FileNotFoundError(f"Konnte UI-Datei nicht laden: {SECURE_UI_FILE}")
    secure_window.setFont(QFont("Arial", 12))
    secure_window.setWindowModality(QtGui.Qt.ApplicationModal)
    secure_window.setWindowFlags(QtGui.Qt.Dialog)
    secure_window.setStyleSheet("background-color: white;")

    infoText = secure_window.findChild(QLabel, "infoText")
    yes_btn = secure_window.findChild(QWidget, "yesBtn")
    no_btn = secure_window.findChild(QWidget, "noBtn")

    if action == "exit":
        if infoText:
            infoText.setText("Möchten Sie das Programm wirklich beenden?")
        if yes_btn:
            yes_btn.clicked.connect(QApplication.quit)
        if no_btn:
            no_btn.clicked.connect(secure_window.close)
    elif action == "delete_project":
        if infoText and project_key:
            infoText.setText(f"Möchten Sie das Projekt '{project_key}' wirklich löschen?")
        if yes_btn and on_confirm:
            yes_btn.clicked.connect(lambda: (on_confirm(), secure_window.close()))
        if no_btn:
            no_btn.clicked.connect(secure_window.close)
    elif action == "delete_character":
        if infoText and project_key:
            infoText.setText(f"Möchten Sie den Charakter '{project_key}' wirklich löschen?")
        if yes_btn and on_confirm:
            yes_btn.clicked.connect(lambda: (on_confirm(), secure_window.close()))
        if no_btn:
            no_btn.clicked.connect(secure_window.close)

    secure_window.show()
    log_info("Sicherheitsdialog erfolgreich geladen und angezeigt.")
    return secure_window

def show_main_window():
    global main_window_ref
    window = DynamicWindow("main_ui", UI_FILE, splitter_name="mainSplitter")
    main_window_ref = window  # Referenz halten!

    # Icon setzen
    icon_path = ASSETS_DIR / "media" / "csnova.png"
    window.setWindowIcon(QIcon(str(icon_path)))

    # Cover-Bild setzen
    cover_label = window.centralWidget().findChild(QLabel, "coverImage")
    if cover_label:
        pixmap_path = ASSETS_DIR / "media" / "Buchcover_csNova.png"
        pixmap = QtGui.QPixmap(str(pixmap_path))
        cover_label.setPixmap(pixmap)
        cover_label.setScaledContents(True)

    # Exit-Button verbinden
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtncsNovaMain")
    if exit_btn:
        def on_exit_clicked():
            secure_dialog = show_secure_dialog(window, action="exit")
            secure_dialog.setWindowModality(QtGui.Qt.ApplicationModal)
        exit_btn.clicked.connect(on_exit_clicked)

    # Projektfenster verbinden
    projects_btn = window.centralWidget().findChild(QWidget, "projectBtncsNovaMain")
    if projects_btn:
        projects_btn.clicked.connect(lambda: show_projects_window(window))

    # Charakterfenster verbinden
    characters_btn = window.centralWidget().findChild(QWidget, "characterBtncsNovaMain")
    if characters_btn:
        characters_btn.clicked.connect(lambda: show_characters_window(window))

    # Objektfenster verbinden
    objects_btn = window.centralWidget().findChild(QWidget, "objectBtncsNovaMain")
    if objects_btn:
        objects_btn.clicked.connect(lambda: show_objects_window(window))

    # Locationsfenster verbinden
    locations_btn = window.centralWidget().findChild(QWidget, "locationBtncsNovaMain")
    if locations_btn:
        locations_btn.clicked.connect(lambda: show_locations_window(window))

    # Storylinefenster verbinden
    storylines_btn = window.centralWidget().findChild(QWidget, "storylineBtncsNovaMain")
    if storylines_btn:
        storylines_btn.clicked.connect(lambda: show_storylines_window(window))

    # Editorfenster verbinden
    editor_btn = window.centralWidget().findChild(QWidget, "editorBtncsNovaMain")
    if editor_btn:
        editor_btn.clicked.connect(lambda: show_editor_window(window))

    # Preferences-Button verbinden
    preferences_btn = window.centralWidget().findChild(QWidget, "preferencesBtncsNovaMain")
    if preferences_btn:
        preferences_btn.clicked.connect(lambda: show_preferences_window(window))

    # Hilfe-Button verbinden
    help_btn = window.centralWidget().findChild(QWidget, "helpBtncsNovaMain")
    if help_btn:
        help_btn.clicked.connect(lambda: show_help_window(window))

    log_info("Hauptfenster erfolgreich geladen und angezeigt.")
    window.show()
    return window

# Startfenster anzeigen
def show_start_window(settings):
    global start_window_ref
    window = DynamicWindow("start_ui", START_UI_FILE, splitter_name="mainSplitter")
    start_window_ref = window  # Referenz halten!

    # Icon setzen
    icon_path = ASSETS_DIR / "media" / "csnova.png"
    window.setWindowIcon(QIcon(str(icon_path)))

    # Cover-Bild setzen
    cover_label = window.centralWidget().findChild(QLabel, "coverImage")
    if cover_label:
        pixmap_path = ASSETS_DIR / "media" / "Buchcover_csNova.png"
        pixmap = QtGui.QPixmap(str(pixmap_path))
        cover_label.setPixmap(pixmap)
        cover_label.setScaledContents(True)

    # Sprache aus settings oder System bestimmen
    language = settings.get("language", get_system_language())

    # ComboBoxen finden
    combo_language = window.centralWidget().findChild(QComboBox, "comboBoxLanguage")
    combo_theme = window.centralWidget().findChild(QComboBox, "comboBoxTheme")

    # Items für Sprache laden
    with open(Path("core/translations/languages.json"), "r", encoding="utf-8") as f:
        languages = json.load(f)
    language_codes = list(languages.keys())
    language_items = list(languages.get(language, languages["de"]).values())
    if combo_language:
        combo_language.clear()
        combo_language.addItems(language_items)
        # Vorbelegen, falls vorhanden
        if "language" in settings:
            try:
                idx = language_items.index(settings["language"])
                combo_language.setCurrentIndex(idx)
            except ValueError:
                combo_language.setCurrentIndex(0)

    # Items für Theme laden
    with open(Path("core/translations/design.json"), "r", encoding="utf-8") as f:
        designs = json.load(f)
    theme_items = list(designs.get(language, designs["de"]).values())
    if combo_theme:
        combo_theme.clear()
        combo_theme.addItems(theme_items)
        # Vorbelegen, falls vorhanden
        if "theme" in settings:
            try:
                idx = theme_items.index(settings["theme"])
                combo_theme.setCurrentIndex(idx)
            except ValueError:
                combo_theme.setCurrentIndex(0)

    # Save-Button verbinden
    save_btn = window.centralWidget().findChild(QWidget, "saveBtn")
    if save_btn:
        def on_save_clicked():
            # Sprache speichern
            if combo_language:
                idx = combo_language.currentIndex()
                settings["language"] = language_codes[idx]
            # Theme speichern
            if combo_theme:
                settings["theme"] = combo_theme.currentText()
            settings["first_start"] = False
            save_settings(settings)
            window.close()
            show_main_window()
        save_btn.clicked.connect(on_save_clicked)

    # Exit-Button verbinden
    exit_btn = window.centralWidget().findChild(QWidget, "exitBnt")
    if exit_btn:
        def on_exit_clicked():
            show_secure_dialog(window, action="exit")
        exit_btn.clicked.connect(on_exit_clicked)

    log_info("Startfenster erfolgreich geladen und angezeigt.")
    window.show()
    return window

# Projektfenster anzeigen
def show_projects_window(parent=None):
    window = DynamicWindow("projects_ui", PROJECTS_UI_FILE, splitter_name="mainSplitter")
    window.show()
    log_info("Projektfenster erfolgreich geladen und angezeigt.")

    # 1. Sprache ermitteln
    settings = load_settings()
    language = settings.get("language", "de")

    # 2. Daten laden
    with open(Path("data/projects/data_projects.json"), "r", encoding="utf-8") as f:
        projects_data = json.load(f)

    if not projects_data:
        # Erstes Projekt anlegen, falls keine vorhanden
        today_str = QDate.currentDate().toString("yyyy-MM-dd")
        projects_data["project_ID_01"] = {
            "project_ID": "1",
            "project_title": "",
            "project_subtitle": "",
            "project_author": "",
            "project_premise": "",
            "project_target_group": 0,
            "project_narrative_perspective": 0,
            "project_style": 0,
            "project_genre": 0,
            "project_work_type": 0,
            "project_motif": 0,
            "project_begin_date": today_str,
            "project_deadline": today_str,
            "project_status": 0,
            "project_word_goal": 0,
            "project_cover_image": "",
            "project_data_file": "",
            "project_notes": "",
            "project_publisher": 0,
            "project_editor": "",
            "project_isbn": "",
            "project_issn": ""
        }
        # Speichern
        with open(Path("data/projects/data_projects.json"), "w", encoding="utf-8") as f:
            json.dump(projects_data, f, ensure_ascii=False, indent=2)

    first_key = next(iter(projects_data.keys()))
    window.current_project_key = first_key
    current_project = projects_data[window.current_project_key]

    def fill_combobox(combo, values, selected_index_or_value):
        combo.clear()
        combo.addItems(values)
        # Wenn selected_index_or_value ein int ist, setze direkt den Index
        if isinstance(selected_index_or_value, int):
            index = selected_index_or_value if 0 <= selected_index_or_value < len(values) else 0
        else:
            try:
                index = values.index(selected_index_or_value)
            except ValueError:
                index = 0
        combo.setCurrentIndex(index)

    # 3. Zielgruppe
    with open(Path("core/translations/targetGroups.json"), "r", encoding="utf-8") as f:
        target_groups = json.load(f)[language]
    combo_target_group = window.centralWidget().findChild(QComboBox, "comboBoxProjectTargetGroup")
    fill_combobox(combo_target_group, list(target_groups.values()), current_project.get("project_target_group", 0))

    # 4. Erzählperspektive
    with open(Path("core/translations/narrativePerspective.json"), "r", encoding="utf-8") as f:
        perspectives = json.load(f)[language]
    combo_narrative = window.centralWidget().findChild(QComboBox, "comboBoxProjectNarrativePerspective")
    fill_combobox(combo_narrative, list(perspectives.values()), current_project.get("project_narrative_perspective", 0))

    # 5. Stil
    with open(Path("core/translations/style.json"), "r", encoding="utf-8") as f:
        styles = json.load(f)[language]
    combo_style = window.centralWidget().findChild(QComboBox, "comboBoxProjectStyle")
    fill_combobox(combo_style, list(styles.values()), current_project.get("project_style", 0))

    # 6. Genre
    with open(Path("core/translations/genre.json"), "r", encoding="utf-8") as f:
        genres = json.load(f)[language]["book_genres"]
    combo_genre = window.centralWidget().findChild(QComboBox, "comboBoxProjectGenre")
    fill_combobox(combo_genre, list(genres.values()), current_project.get("project_genre", 0))

    # 7. Arbeitstyp
    with open(Path("core/translations/workingType.json"), "r", encoding="utf-8") as f:
        working_types = json.load(f)[language]["book_working_types"]
    combo_work_type = window.centralWidget().findChild(QComboBox, "comboBoxProjectWorkingType")
    fill_combobox(combo_work_type, list(working_types.values()), current_project.get("project_work_type", 0))

    # 8. Motiv
    with open(Path("core/translations/motif.json"), "r", encoding="utf-8") as f:
        motifs = json.load(f)[language]
    combo_motif = window.centralWidget().findChild(QComboBox, "comboBoxProjectMotif")
    fill_combobox(combo_motif, list(motifs.values()), current_project.get("project_motif", 0))

    # 9. Status
    with open(Path("core/translations/status.json"), "r", encoding="utf-8") as f:
        status = json.load(f)[language]
    combo_status = window.centralWidget().findChild(QComboBox, "comboBoxProjectStatus")
    fill_combobox(combo_status, list(status.values()), current_project.get("project_status", 0))

    # 10. Verlag
    with open(Path("core/translations/publisher.json"), "r", encoding="utf-8") as f:
        publishers = json.load(f)["publishers"]
    publisher_names = [pub["name"] for pub in publishers if pub["type"] == "book"]
    combo_publisher = window.centralWidget().findChild(QComboBox, "comboBoxPublisher")
    fill_combobox(combo_publisher, publisher_names, current_project.get("project_publisher", 0))

    # Felder setzen
    window.centralWidget().findChild(QLineEdit, "lineEditProjectTitle").setText(current_project.get("project_title", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditProjectSubtitle").setText(current_project.get("project_subtitle", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditProjectAuthor").setText(current_project.get("project_author", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditProjectPremise").setText(current_project.get("project_premise", ""))
    spin_box = window.centralWidget().findChild(QSpinBox, "spinBoxProjectWordsCount")
    if spin_box:
        spin_box.setValue(int(current_project.get("project_word_goal", 0)))
    notes_edit = window.centralWidget().findChild(QTextEdit, "textEditProjectNotes")
    if notes_edit:
        notes_edit.setPlainText(current_project.get("project_notes", ""))
    # Datum Beginn
    begin_date_edit = window.centralWidget().findChild(QDateEdit, "dateEditProjectBegin")
    if begin_date_edit:
        begin_str = current_project.get("project_begin_date", "")
        if begin_str:
            # Format: "yyyy-MM-dd"
            date = QDate.fromString(begin_str, "yyyy-MM-dd")
            if date.isValid():
                begin_date_edit.setDate(date)
    # Datum Deadline
    deadline_date_edit = window.centralWidget().findChild(QDateEdit, "dateEditProjectDeadLine")
    if deadline_date_edit:
        deadline_str = current_project.get("project_deadline", "")
        if deadline_str:
            date = QDate.fromString(deadline_str, "yyyy-MM-dd")
            if date.isValid():
                deadline_date_edit.setDate(date)

    # Buttons einbinden
    # --- New-Button einbinden ---
    new_btn = window.centralWidget().findChild(QWidget, "newBtnProjects")
    if new_btn:
        def on_new_clicked():
            # Neues Projekt anlegen
            with open(Path("data/projects/data_projects.json"), "r", encoding="utf-8") as f:
                projects_data = json.load(f)
            # Neuen Key erzeugen
            new_id = f"project_ID_{len(projects_data) + 1:02d}"
            today_str = QDate.currentDate().toString("yyyy-MM-dd")
            # Leeren Datensatz anlegen
            projects_data[new_id] = {
                "project_ID": str(len(projects_data) + 1),
                "project_title": "",
                "project_subtitle": "",
                "project_author": "",
                "project_premise": "",
                "project_target_group": 0,
                "project_narrative_perspective": 0,
                "project_style": 0,
                "project_genre": 0,
                "project_work_type": 0,
                "project_motif": 0,
                "project_begin_date": today_str,
                "project_deadline": today_str,
                "project_status": 0,
                "project_word_goal": 0,
                "project_cover_image": "",
                "project_data_file": "",
                "project_notes": "",
                "project_publisher": 0,
                "project_editor": "",
                "project_isbn": "",
                "project_issn": ""
            }
            # Speichern
            with open(Path("data/projects/data_projects.json"), "w", encoding="utf-8") as f:
                json.dump(projects_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neues Projekt {new_id} angelegt.")

            # Felder im Fenster leeren und aktuelles Datum setzen
            window.centralWidget().findChild(QLineEdit, "lineEditProjectTitle").setText("")
            window.centralWidget().findChild(QLineEdit, "lineEditProjectSubtitle").setText("")
            window.centralWidget().findChild(QLineEdit, "lineEditProjectAuthor").setText("")
            window.centralWidget().findChild(QLineEdit, "lineEditProjectPremise").setText("")
            window.centralWidget().findChild(QComboBox, "comboBoxProjectTargetGroup").setCurrentIndex(0)
            window.centralWidget().findChild(QComboBox, "comboBoxProjectNarrativePerspective").setCurrentIndex(0)
            window.centralWidget().findChild(QComboBox, "comboBoxProjectStyle").setCurrentIndex(0)
            window.centralWidget().findChild(QComboBox, "comboBoxProjectGenre").setCurrentIndex(0)
            window.centralWidget().findChild(QComboBox, "comboBoxProjectWorkingType").setCurrentIndex(0)
            window.centralWidget().findChild(QComboBox, "comboBoxProjectMotif").setCurrentIndex(0)
            window.centralWidget().findChild(QComboBox, "comboBoxProjectStatus").setCurrentIndex(0)
            window.centralWidget().findChild(QComboBox, "comboBoxPublisher").setCurrentIndex(0)
            window.centralWidget().findChild(QSpinBox, "spinBoxProjectWordsCount").setValue(0)
            window.centralWidget().findChild(QLineEdit, "lineEditProjectCoverImage").setText("")
            window.centralWidget().findChild(QLineEdit, "lineEditProjectDataFile").setText("")
            window.centralWidget().findChild(QLineEdit, "lineEditISBN").setText("")
            window.centralWidget().findChild(QLineEdit, "lineEditISSN").setText("")
            notes_edit = window.centralWidget().findChild(QTextEdit, "textEditProjectNotes")
            if notes_edit:
                notes_edit.setPlainText("")
            begin_date_edit = window.centralWidget().findChild(QDateEdit, "dateEditProjectBegin")
            if begin_date_edit:
                begin_date_edit.setDate(QDate.currentDate())
            deadline_date_edit = window.centralWidget().findChild(QDateEdit, "dateEditProjectDeadLine")
            if deadline_date_edit:
                deadline_date_edit.setDate(QDate.currentDate())

            # Aktuellen Projekt-Key setzen
            window.current_project_key = new_id

        new_btn.clicked.connect(on_new_clicked)

    # --- Felder neu laden ---
    def update_project_fields(project):
        window.centralWidget().findChild(QLineEdit, "lineEditProjectTitle").setText(project.get("project_title", ""))
        window.centralWidget().findChild(QLineEdit, "lineEditProjectSubtitle").setText(project.get("project_subtitle", ""))
        window.centralWidget().findChild(QLineEdit, "lineEditProjectAuthor").setText(project.get("project_author", ""))
        window.centralWidget().findChild(QLineEdit, "lineEditProjectPremise").setText(project.get("project_premise", ""))
        window.centralWidget().findChild(QComboBox, "comboBoxProjectTargetGroup").setCurrentIndex(project.get("project_target_group", 0))
        window.centralWidget().findChild(QComboBox, "comboBoxProjectNarrativePerspective").setCurrentIndex(project.get("project_narrative_perspective", 0))
        window.centralWidget().findChild(QComboBox, "comboBoxProjectStyle").setCurrentIndex(project.get("project_style", 0))
        window.centralWidget().findChild(QComboBox, "comboBoxProjectGenre").setCurrentIndex(project.get("project_genre", 0))
        window.centralWidget().findChild(QComboBox, "comboBoxProjectWorkingType").setCurrentIndex(project.get("project_work_type", 0))
        window.centralWidget().findChild(QComboBox, "comboBoxProjectMotif").setCurrentIndex(project.get("project_motif", 0))
        window.centralWidget().findChild(QComboBox, "comboBoxProjectStatus").setCurrentIndex(project.get("project_status", 0))
        window.centralWidget().findChild(QComboBox, "comboBoxPublisher").setCurrentIndex(project.get("project_publisher", 0))
        window.centralWidget().findChild(QSpinBox, "spinBoxProjectWordsCount").setValue(int(project.get("project_word_goal", 0)))
        window.centralWidget().findChild(QLineEdit, "lineEditProjectCoverImage").setText(project.get("project_cover_image", ""))
        window.centralWidget().findChild(QLineEdit, "lineEditProjectDataFile").setText(project.get("project_data_file", ""))
        window.centralWidget().findChild(QLineEdit, "lineEditISBN").setText(project.get("project_isbn", ""))
        window.centralWidget().findChild(QLineEdit, "lineEditISSN").setText(project.get("project_issn", ""))
        notes_edit = window.centralWidget().findChild(QTextEdit, "textEditProjectNotes")
        if notes_edit:
            notes_edit.setPlainText(project.get("project_notes", ""))
        begin_date_edit = window.centralWidget().findChild(QDateEdit, "dateEditProjectBegin")
        if begin_date_edit:
            begin_str = project.get("project_begin_date", "")
            if begin_str:
                date = QDate.fromString(begin_str, "yyyy-MM-dd")
                if date.isValid():
                    begin_date_edit.setDate(date)
        deadline_date_edit = window.centralWidget().findChild(QDateEdit, "dateEditProjectDeadLine")
        if deadline_date_edit:
            deadline_str = project.get("project_deadline", "")
            if deadline_str:
                date = QDate.fromString(deadline_str, "yyyy-MM-dd")
                if date.isValid():
                    deadline_date_edit.setDate(date)

    # --- Next-Button ---
    next_btn = window.centralWidget().findChild(QWidget, "nextBtnProjects")
    if next_btn:
        def on_next_clicked():
            with open(Path("data/projects/data_projects.json"), "r", encoding="utf-8") as f:
                projects_data = json.load(f)
            keys = list(projects_data.keys())
            current_index = keys.index(window.current_project_key)
            next_index = (current_index + 1) % len(keys)
            next_key = keys[next_index]
            window.current_project_key = next_key
            next_project = projects_data[next_key]
            update_project_fields(next_project)
        next_btn.clicked.connect(on_next_clicked)

    # --- Previous-Button ---
    previous_btn = window.centralWidget().findChild(QWidget, "previousBtnProjects")
    if previous_btn:
        def on_previous_clicked():
            with open(Path("data/projects/data_projects.json"), "r", encoding="utf-8") as f:
                projects_data = json.load(f)
            keys = list(projects_data.keys())
            current_index = keys.index(window.current_project_key)
            previous_index = (current_index - 1) % len(keys)
            previous_key = keys[previous_index]
            window.current_project_key = previous_key
            previous_project = projects_data[previous_key]
            update_project_fields(previous_project)
        previous_btn.clicked.connect(on_previous_clicked) 

    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnProjects")
    if exit_btn:
        exit_btn.clicked.connect(window.close)
    
    # --- Delete-Button einbinden ---
    delete_btn = window.centralWidget().findChild(QWidget, "deleteBtnProjects")
    if delete_btn:
        def on_delete_clicked():
            with open(Path("data/projects/data_projects.json"), "r", encoding="utf-8") as f:
                projects_data = json.load(f)
            project_key = window.current_project_key
            project_title = projects_data[project_key].get("project_title", project_key)
            def delete_project():
                if project_key in projects_data:
                    del projects_data[project_key]
                    with open(Path("data/projects/data_projects.json"), "w", encoding="utf-8") as f:
                        json.dump(projects_data, f, ensure_ascii=False, indent=2)
                    log_info(f"Projekt {project_title} gelöscht.")
                    # Optional: Nächstes Projekt anzeigen oder Felder leeren
            show_secure_dialog(window, action="delete_project", project_key=project_title, on_confirm=delete_project)
        delete_btn.clicked.connect(on_delete_clicked)   
    
    # --- Save-Button einbinden ---
    save_btn = window.centralWidget().findChild(QWidget, "saveBtnProjects")
    if save_btn:
        def on_save_clicked():
            with open(Path("data/projects/data_projects.json"), "r", encoding="utf-8") as f:
                projects_data = json.load(f)
            project_key = window.current_project_key  # <-- immer aktueller Key!
            project = projects_data[project_key]

            # Sammle alle Eingabewerte aus dem Fenster
            project["project_title"] = window.centralWidget().findChild(QLineEdit, "lineEditProjectTitle").text()
            project["project_subtitle"] = window.centralWidget().findChild(QLineEdit, "lineEditProjectSubtitle").text()
            project["project_author"] = window.centralWidget().findChild(QLineEdit, "lineEditProjectAuthor").text()
            project["project_premise"] = window.centralWidget().findChild(QLineEdit, "lineEditProjectPremise").text()
            project["project_target_group"] = window.centralWidget().findChild(QComboBox, "comboBoxProjectTargetGroup").currentIndex()
            project["project_narrative_perspective"] = window.centralWidget().findChild(QComboBox, "comboBoxProjectNarrativePerspective").currentIndex()
            project["project_style"] = window.centralWidget().findChild(QComboBox, "comboBoxProjectStyle").currentIndex()
            project["project_genre"] = window.centralWidget().findChild(QComboBox, "comboBoxProjectGenre").currentIndex()
            project["project_work_type"] = window.centralWidget().findChild(QComboBox, "comboBoxProjectWorkingType").currentIndex()
            project["project_motif"] = window.centralWidget().findChild(QComboBox, "comboBoxProjectMotif").currentIndex()
            project["project_status"] = window.centralWidget().findChild(QComboBox, "comboBoxProjectStatus").currentIndex()
            project["project_publisher"] = window.centralWidget().findChild(QComboBox, "comboBoxPublisher").currentIndex()
            project["project_word_goal"] = window.centralWidget().findChild(QSpinBox, "spinBoxProjectWordsCount").value()
            project["project_notes"] = window.centralWidget().findChild(QTextEdit, "textEditProjectNotes").toPlainText()
            project["project_cover_image"] = window.centralWidget().findChild(QLineEdit, "lineEditProjectCoverImage").text()
            project["project_data_file"] = window.centralWidget().findChild(QLineEdit, "lineEditProjectDataFile").text()
            project["project_isbn"] = window.centralWidget().findChild(QLineEdit, "lineEditISBN").text()
            project["project_issn"] = window.centralWidget().findChild(QLineEdit, "lineEditISSN").text()
            # Datum ggf. als String speichern
            begin_date = window.centralWidget().findChild(QDateEdit, "dateEditProjectBegin")
            if begin_date:
                project["project_begin_date"] = begin_date.date().toString("yyyy-MM-dd")
            deadline_date = window.centralWidget().findChild(QDateEdit, "dateEditProjectDeadLine")
            if deadline_date:
                project["project_deadline"] = deadline_date.date().toString("yyyy-MM-dd")

            # Speichere die Daten zurück
            with open(Path("data/projects/data_projects.json"), "w", encoding="utf-8") as f:
                json.dump(projects_data, f, ensure_ascii=False, indent=2)
            log_info(f"Projekt {project_key} erfolgreich gespeichert.")

        save_btn.clicked.connect(on_save_clicked)    

    return window

# Charakterfenster anzeigen
def show_characters_window(parent=None):
    window = DynamicWindow("characters_ui", CHARACTERS_UI_FILE, splitter_name="mainSplitter")
    window.show()

    # 1. Sprache ermitteln
    settings = load_settings()
    language = settings.get("language", "de")

    # 2. Daten laden
    with open(Path("data/characters/data_characters.json"), "r", encoding="utf-8") as f:
        character_data = json.load(f)

    if not character_data:
        # Ersten Charakter anlegen, falls keine vorhanden
        character_data["character_ID_01"] = {
        "character_ID": "1",
        "character_name": "",
        "character_firstname": "",
        "character_nickname": "",
        "character_birthdate": "",
        "character_died": "",
        "character_gender": 0,
        "character_sexOrientation": 0,
        "character_role": 0,
        "character_group": 0,
        "character_development": "",
        "character_notes": "",
        "character_image":"",
        "character_images": [],
        "character_mother": "",
        "character_father": "",
        "character_referencePerson": "",
        "character_siblings": "",
        "character_placeOfBirth": "",
        "character_country": "",
        "character_ethnicity": "",
        "character_ancestryNotes ": "",
        "character_school": "",
        "character_university": "",
        "character_vocationalTraining": "",
        "character_profession": "",
        "character_artMusic": "",
        "character_sports": "",
        "character_technology": "",
        "character_autodidact": "",
        "character_educationNotes": "",
        "character_positiveCharacteristics": "",
        "character_negativeCharacteristics": "",
        "character_fears": "",
        "character_weaknesses": "",
        "character_strengths": "",
        "character_talents": "",
        "character_beliefs": "",
        "character_lifeGoals": "",
        "character_motivation": "",
        "character_behavior": "",
        "character_personalityNotes": "",
        "character_height": 175,
        "character_bodyType": 0,
        "character_stature": 0,
        "character_faceshape": 0,
        "character_eyeshape": 0,
        "character_eyesColor": "",
        "character_hair": "",
        "character_hairColor": "",
        "character_skinType": "",
        "character_skinColor": "",
        "character_charisma": "",
        "charactert_specialFeatures": "",
        "character_lookNotes": "",
        "character_head": "",
        "character_neck": "",
        "character_breast": "",
        "character_back": "",
        "character_shoulder": "",
        "character_upperarm": "",
        "character_elbow": "",
        "character_lowerarm": "",
        "character_wrist": "",
        "character_hand": "",
        "character_finger": "",
        "character_hips": "",
        "character_buttocks": "",
        "character_upperleg": "",
        "character_knee": "",
        "character_lowerleg": "",
        "character_ankle": "",
        "character_foot": "",
        "character_toe": "",
        "character_bodyNotes": "",
        "character_diagnoses": "",
        "character_symptoms": "",
        "character_therapies": "",
        "character_medications": "",
        "character_temperament": "",
        "character_ethicValues": "",
        "character_moralValues": "",
        "character_strengthsOfCharacter": "",
        "character_weaknessesOfCharacter": "",
        "character_selfimage": "",
        "character_humor": "",
        "character_aggressiveness": "",
        "character_traumas": "",
        "character_Impressions": "",
        "character_socialization": "",
        "character_norms": "",
        "character_taboos": "",
        "character_psycheNotes": ""
        }
        # Speichern
        with open(Path("data/characters/data_characters.json"), "w", encoding="utf-8") as f:
            json.dump(character_data, f, ensure_ascii=False, indent=2)
        
    first_key = next(iter(character_data.keys()))
    window.current_character_key = first_key
    current_character = character_data[window.current_character_key]

    # Alter-Label aktualisieren
    def update_age_label():
        birth_str = birthdate_edit.text()
        died_str = died_edit.text()
        age_value = calculate_age(birth_str, died_str)
        if label_age:
            label_age.setText(age_value)

    birthdate_edit = window.centralWidget().findChild(QLineEdit, "lineEditBorn")
    if birthdate_edit:
        regex = QRegularExpression(r"^\d{1,2}\.\d{1,2}\.\d{1,4}( v\. Chr\.)?$|^\d{1,4}( v\. Chr\.)?$")
        validator = QRegularExpressionValidator(regex)
        birthdate_edit.setValidator(validator)
        birthdate_edit.setText(current_character.get("character_birthdate", ""))
        birthdate_edit.textChanged.connect(update_age_label)

    died_edit = window.centralWidget().findChild(QLineEdit, "lineEditDied")
    if died_edit:
        died_edit.setValidator(validator)
        died_edit.setText(current_character.get("character_died", ""))
        died_edit.textChanged.connect(update_age_label)

    # Alter berechnen
    birth_value = current_character.get("character_birthdate", "")
    died_value = current_character.get("character_died", "")
    age_value = calculate_age(birth_value, died_value)

    label_age = window.centralWidget().findChild(QLabel, "labelAgeValue")
    if label_age:
        label_age.setText(age_value)

    def fill_combobox(combo, values, selected_index_or_value):
        combo.clear()
        combo.addItems(values)
        # Wenn selected_index_or_value ein int ist, setze direkt den Index
        if isinstance(selected_index_or_value, int):
            index = selected_index_or_value if 0 <= selected_index_or_value < len(values) else 0
        else:
            try:
                index = values.index(selected_index_or_value)
            except ValueError:
                index = 0
        combo.setCurrentIndex(index)
    
    # ComboBoxen füllen
    # Status
    with open(Path("core/translations/status.json"), "r", encoding="utf-8") as f:
        status = json.load(f)[language]
    combo_status = window.centralWidget().findChild(QComboBox, "comboBoxStatus")
    fill_combobox(combo_status, list(status.values()), current_character.get("character_status", 0))
    # 2. Alter
    # 3. Geschlecht
    with open(Path("core/translations/gender.json"), "r", encoding="utf-8") as f:
        gender = json.load(f)[language]
    combo_gender = window.centralWidget().findChild(QComboBox, "comboBoxGender")
    fill_combobox(combo_gender, list(gender.values()), current_character.get("character_gender", 0))
    # 4. Sexualität
    with open(Path("core/translations/sex_orientation.json"), "r", encoding="utf-8") as f:
        sexual_orientation = json.load(f)[language]
    combo_sexual_orientation = window.centralWidget().findChild(QComboBox, "comboBoxSexOrientation")
    fill_combobox(combo_sexual_orientation, list(sexual_orientation.values()), current_character.get("character_sexOrientation", 0))
    # 5. Rolle 
    with open(Path("core/translations/role.json"), "r", encoding="utf-8") as f:
        role = json.load(f)[language]
    combo_role = window.centralWidget().findChild(QComboBox, "comboBoxRole")
    fill_combobox(combo_role, list(role.values()), current_character.get("character_role", 0))
    # 6. Gruppe
    with open(Path("core/translations/group.json"), "r", encoding="utf-8") as f:
        group = json.load(f)[language]
    combo_group = window.centralWidget().findChild(QComboBox, "comboBoxGroup")
    fill_combobox(combo_group, list(group.values()), current_character.get("character_group", 0))
    # 7. Körperbau
    with open(Path("core/translations/bodyType.json"), "r", encoding="utf-8") as f:
        body_type = json.load(f)[language]
    combo_body_type = window.centralWidget().findChild(QComboBox, "comboBoxBodyType")
    fill_combobox(combo_body_type, list(body_type.values()), current_character.get("character_bodyType", 0))
    # 8. Statur
    with open(Path("core/translations/stature.json"), "r", encoding="utf-8") as f:
        stature = json.load(f)[language]
    combo_stature = window.centralWidget().findChild(QComboBox, "comboBoxStature")
    fill_combobox(combo_stature, list(stature.values()), current_character.get("character_stature", 0))
    # 9. Gesichtsform
    with open(Path("core/translations/faceShape.json"), "r", encoding="utf-8") as f:
        face_shape = json.load(f)[language]
    combo_face_shape = window.centralWidget().findChild(QComboBox, "comboBoxFaceShape")
    fill_combobox(combo_face_shape, list(face_shape.values()), current_character.get("character_faceshape", 0))
    # 10. Augenform
    with open(Path("core/translations/eyeShape.json"), "r", encoding="utf-8") as f:
        eye_shape = json.load(f)[language]
    combo_eye_shape = window.centralWidget().findChild(QComboBox, "comboBoxEyeShape")
    fill_combobox(combo_eye_shape, list(eye_shape.values()), current_character.get("character_eyeshape", 0))

    # Felder setzen
    window.centralWidget().findChild(QLineEdit, "lineEditName").setText(current_character.get("character_name", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditFirstName").setText(current_character.get("character_firstname", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditNickName").setText(current_character.get("character_nickname", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditBorn").setText(current_character.get("character_birthdate", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditDied").setText(current_character.get("character_died", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditMother").setText(current_character.get("character_mother", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditFather").setText(current_character.get("character_father", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditReferencePerson").setText(current_character.get("character_referencePerson", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditPlaceOfBirth").setText(current_character.get("character_placeOfBirth", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditCountry").setText(current_character.get("character_country", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditEthnicity").setText(current_character.get("character_ethnicity", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditPosCharacteristics").setText(current_character.get("character_positiveCharacteristics", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditNegCharacteristics").setText(current_character.get("character_negativeCharacteristics", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditFears").setText(current_character.get("character_fears", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditWeakness").setText(current_character.get("character_weaknesses", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditStrength").setText(current_character.get("character_strengths", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditTalents").setText(current_character.get("character_talents", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditBelief").setText(current_character.get("character_beliefs", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditLifeGoal").setText(current_character.get("character_lifeGoals", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditMotivation").setText(current_character.get("character_motivation", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditBehavior").setText(current_character.get("character_behavior", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditEyeColor").setText(current_character.get("character_eyesColor", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditHair").setText(current_character.get("character_hair", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditHairColor").setText(current_character.get("character_hairColor", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditSkin").setText(current_character.get("character_skinType", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditSkinColor").setText(current_character.get("character_skinColor", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditCharisma").setText(current_character.get("character_charisma", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditSpecialFeatures").setText(current_character.get("charactert_specialFeatures", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditHead").setText(current_character.get("character_head", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditNeck").setText(current_character.get("character_neck", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditBreast").setText(current_character.get("character_breast", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditBack").setText(current_character.get("character_back", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditShoulders").setText(current_character.get("character_shoulder", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditUpperArm").setText(current_character.get("character_upperarm", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditElbow").setText(current_character.get("character_elbow", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditLowerArms").setText(current_character.get("character_lowerarm", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditWrists").setText(current_character.get("character_wrist", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditHand").setText(current_character.get("character_hand", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditFinger").setText(current_character.get("character_finger", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditHips").setText(current_character.get("character_hips", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditButtocks").setText(current_character.get("character_buttocks", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditUpperLeg").setText(current_character.get("character_upperleg", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditKnee").setText(current_character.get("character_knee", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditLowerLeg").setText(current_character.get("character_lowerleg", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditAnkles").setText(current_character.get("character_ankle", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditFeet").setText(current_character.get("character_foot", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditToes").setText(current_character.get("character_toe", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditDiagnosis").setText(current_character.get("character_diagnoses", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditSymptoms").setText(current_character.get("character_symptoms", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditTherapy").setText(current_character.get("character_therapies", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditMedication").setText(current_character.get("character_medications", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditTemperament").setText(current_character.get("character_temperament", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditEthicalValues").setText(current_character.get("character_ethicValues", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditMoralValues").setText(current_character.get("character_moralValues", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditStrengthsOfCharacter").setText(current_character.get("character_strengthsOfCharacter", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditWeaknessOfCharacter").setText(current_character.get("character_weaknessesOfCharacter", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditSelfImage").setText(current_character.get("character_selfimage", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditHumor").setText(current_character.get("character_humor", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditAggressivness").setText(current_character.get("character_aggressiveness", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditTrauma").setText(current_character.get("character_traumas", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditImpression").setText(current_character.get("character_Impressions", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditSocialization").setText(current_character.get("character_socialization", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditNorms").setText(current_character.get("character_norms", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditTaboos").setText(current_character.get("character_taboos", ""))
    
    window.centralWidget().findChild(QSpinBox, "spinBoxSize").setValue(int(current_character.get("character_height", 175)))
    window.centralWidget().findChild(QCheckBox, "checkBoxMainCharacter").setChecked(current_character.get("character_mainCharacter", False))
    # Notizfelder
    notes_edit = window.centralWidget().findChild(QTextEdit, "textEditCharacterNotes")
    if notes_edit:
        notes_edit.setPlainText(current_character.get("character_notes", ""))
    development_edit = window.centralWidget().findChild(QTextEdit, "textEditDevelopmentNotes")
    if development_edit:
        development_edit.setPlainText(current_character.get("character_development", ""))
    siblings_edit = window.centralWidget().findChild(QTextEdit, "textEditSiblings")
    if siblings_edit:
        siblings_edit.setPlainText(current_character.get("character_siblings", ""))
    ancestry_edit = window.centralWidget().findChild(QTextEdit, "textEditAncestryNotes")
    if ancestry_edit:
        ancestry_edit.setPlainText(current_character.get("character_ancestryNotes ", ""))
    school_edit = window.centralWidget().findChild(QTextEdit, "textEditSchool")
    if school_edit:
        school_edit.setPlainText(current_character.get("character_school", ""))
    university_edit = window.centralWidget().findChild(QTextEdit, "textEditUniversity")
    if university_edit:
        university_edit.setPlainText(current_character.get("character_university", ""))
    vocational_edit = window.centralWidget().findChild(QTextEdit, "textEditVocationalTraining")
    if vocational_edit:
        vocational_edit.setPlainText(current_character.get("character_vocationalTraining", ""))
    profession_edit = window.centralWidget().findChild(QTextEdit, "textEditProfession")
    if profession_edit:
        profession_edit.setPlainText(current_character.get("character_profession", ""))
    art_edit = window.centralWidget().findChild(QTextEdit, "textEditArtMusic")
    if art_edit:
        art_edit.setPlainText(current_character.get("character_artMusic", ""))
    sports_edit = window.centralWidget().findChild(QTextEdit, "textEditSports")
    if sports_edit:
        sports_edit.setPlainText(current_character.get("character_sports", ""))
    technology_edit = window.centralWidget().findChild(QTextEdit, "textEditTechnology")
    if technology_edit:
        technology_edit.setPlainText(current_character.get("character_technology", ""))
    autodidact_edit = window.centralWidget().findChild(QTextEdit, "textEditAutodidact")
    if autodidact_edit:
        autodidact_edit.setPlainText(current_character.get("character_autodidact", ""))
    education_notes_edit = window.centralWidget().findChild(QTextEdit, "textEditEducationNotes")
    if education_notes_edit:
        education_notes_edit.setPlainText(current_character.get("character_educationNotes", ""))
    personality_notes_edit = window.centralWidget().findChild(QTextEdit, "textEditPersonalityNotes")
    if personality_notes_edit:
        personality_notes_edit.setPlainText(current_character.get("character_personalityNotes", ""))
    look_notes_edit = window.centralWidget().findChild(QTextEdit, "textEditLookNotes")
    if look_notes_edit:
        look_notes_edit.setPlainText(current_character.get("character_lookNotes", ""))
    look_details_notes_edit = window.centralWidget().findChild(QTextEdit, "textEditLookDetailsNotes")
    if look_details_notes_edit:
        look_details_notes_edit.setPlainText(current_character.get("character_bodyNotes", ""))
    psyche_notes_edit = window.centralWidget().findChild(QTextEdit, "textEditPsychologyNotes")
    if psyche_notes_edit:
        psyche_notes_edit.setPlainText(current_character.get("character_psycheNotes", ""))


    # --- Save-Button einbinden ---
    save_btn = window.centralWidget().findChild(QWidget, "saveBtnCharacter")
    if save_btn:
        def on_save_clicked():
            with open(Path("data/characters/data_characters.json"), "r", encoding="utf-8") as f:
                character_data = json.load(f)
            character_key = window.current_character_key  # <-- immer aktueller Key!
            character = character_data[character_key]

            # Sammle alle Eingabewerte aus dem Fenster
            character["character_name"] = window.centralWidget().findChild(QLineEdit, "lineEditName").text()
            character["character_firstname"] = window.centralWidget().findChild(QLineEdit, "lineEditFirstName").text()
            character["character_nickname"] = window.centralWidget().findChild(QLineEdit, "lineEditNickName").text()
            character["character_birthdate"] = window.centralWidget().findChild(QLineEdit, "lineEditBorn").text()
            character["character_died"] = window.centralWidget().findChild(QLineEdit, "lineEditDied").text()
            character["character_gender"] = window.centralWidget().findChild(QComboBox, "comboBoxGender").currentIndex()
            character["character_sexOrientation"] = window.centralWidget().findChild(QComboBox, "comboBoxSexOrientation").currentIndex()
            character["character_status"] = window.centralWidget().findChild(QComboBox, "comboBoxStatus").currentIndex()
            character["character_role"] = window.centralWidget().findChild(QComboBox, "comboBoxRole").currentIndex()
            character["character_group"] = window.centralWidget().findChild(QComboBox, "comboBoxGroup").currentIndex()
            character["character_mother"] = window.centralWidget().findChild(QLineEdit, "lineEditMother").text()
            character["character_father"] = window.centralWidget().findChild(QLineEdit, "lineEditFather").text()
            character["character_referencePerson"] = window.centralWidget().findChild(QLineEdit, "lineEditReferencePerson").text()
            character["character_siblings"] = window.centralWidget().findChild(QTextEdit, "textEditSiblings").toPlainText()
            character["character_placeOfBirth"] = window.centralWidget().findChild(QLineEdit, "lineEditPlaceOfBirth").text()
            character["character_country"] = window.centralWidget().findChild(QLineEdit, "lineEditCountry").text()
            character["character_ethnicity"] = window.centralWidget().findChild(QLineEdit, "lineEditEthnicity").text()
            character["character_ancestryNotes "] = window.centralWidget().findChild(QTextEdit, "textEditAncestryNotes").toPlainText()
            character["character_school"] = window.centralWidget().findChild(QTextEdit, "textEditSchool").toPlainText()
            character["character_university"] = window.centralWidget().findChild(QTextEdit, "textEditUniversity").toPlainText()
            character["character_vocationalTraining"] = window.centralWidget().findChild(QTextEdit, "textEditVocationalTraining").toPlainText()
            character["character_profession"] = window.centralWidget().findChild(QTextEdit, "textEditProfession").toPlainText()
            character["character_artMusic"] = window.centralWidget().findChild(QTextEdit, "textEditArtMusic").toPlainText()
            character["character_sports"] = window.centralWidget().findChild(QTextEdit, "textEditSport").toPlainText()
            character["character_technology"] = window.centralWidget().findChild(QTextEdit, "textEditTechnic").toPlainText()
            character["character_autodidact"] = window.centralWidget().findChild(QTextEdit, "textEditAutodidact").toPlainText()
            character["character_educationNotes"] = window.centralWidget().findChild(QTextEdit, "textEditEducationNotes").toPlainText()
            character["character_positiveCharacteristics"] = window.centralWidget().findChild(QLineEdit, "lineEditPosCharacteristics").text()
            character["character_negativeCharacteristics"] = window.centralWidget().findChild(QLineEdit, "lineEditNegCharacteristics").text()
            character["character_fears"] = window.centralWidget().findChild(QLineEdit, "lineEditFears").text()
            character["character_weaknesses"] = window.centralWidget().findChild(QLineEdit, "lineEditWeakness").text()
            character["character_strengths"] = window.centralWidget().findChild(QLineEdit, "lineEditStrength").text()
            character["character_talents"] = window.centralWidget().findChild(QLineEdit, "lineEditTalents").text()
            character["character_beliefs"] = window.centralWidget().findChild(QLineEdit, "lineEditBelief").text()
            character["character_lifeGoals"] = window.centralWidget().findChild(QLineEdit, "lineEditLifeGoal").text()
            character["character_motivation"] = window.centralWidget().findChild(QLineEdit, "lineEditMotivation").text()
            character["character_behavior"] = window.centralWidget().findChild(QLineEdit, "lineEditBehavior").text()
            character["character_personalityNotes"] = window.centralWidget().findChild(QTextEdit, "textEditPersonalityNotes").toPlainText()
            character["character_height"] = window.centralWidget().findChild(QSpinBox, "spinBoxSize").value()
            character["character_bodyType"] = window.centralWidget().findChild(QComboBox, "comboBoxBodyType").currentIndex()
            character["character_stature"] = window.centralWidget().findChild(QComboBox, "comboBoxStature").currentIndex()
            character["character_faceshape"] = window.centralWidget().findChild(QComboBox, "comboBoxFaceShape").currentIndex()
            character["character_eyeshape"] = window.centralWidget().findChild(QComboBox, "comboBoxEyeShape").currentIndex()
            character["character_eyesColor"] = window.centralWidget().findChild(QLineEdit, "lineEditEyeColor").text()
            character["character_hair"] = window.centralWidget().findChild(QLineEdit, "lineEditHair").text()
            character["character_hairColor"] = window.centralWidget().findChild(QLineEdit, "lineEditHairColor").text()
            character["character_skinType"] = window.centralWidget().findChild(QLineEdit, "lineEditSkin").text()
            character["character_skinColor"] = window.centralWidget().findChild(QLineEdit, "lineEditSkinColor").text()
            character["character_charisma"] = window.centralWidget().findChild(QLineEdit, "lineEditCharisma").text()
            character["charactert_specialFeatures"] = window.centralWidget().findChild(QLineEdit, "lineEditSpecialFeatures").text()
            character["character_lookNotes"] = window.centralWidget().findChild(QTextEdit, "textEditLookNotes").toPlainText()
            character["character_head"] = window.centralWidget().findChild(QLineEdit, "lineEditHead").text()
            character["character_neck"] = window.centralWidget().findChild(QLineEdit, "lineEditNeck").text()
            character["character_breast"] = window.centralWidget().findChild(QLineEdit, "lineEditBreast").text()
            character["character_back"] = window.centralWidget().findChild(QLineEdit, "lineEditBack").text()
            character["character_shoulder"] = window.centralWidget().findChild(QLineEdit, "lineEditShoulders").text()
            character["character_upperarm"] = window.centralWidget().findChild(QLineEdit, "lineEditUpperArm").text()
            character["character_elbow"] = window.centralWidget().findChild(QLineEdit, "lineEditElbow").text()
            character["character_lowerarm"] = window.centralWidget().findChild(QLineEdit, "lineEditLowerArms").text()
            character["character_wrist"] = window.centralWidget().findChild(QLineEdit, "lineEditWrists").text()
            character["character_hand"] = window.centralWidget().findChild(QLineEdit, "lineEditHand").text()
            character["character_finger"] = window.centralWidget().findChild(QLineEdit, "lineEditFinger").text()
            character["character_hips"] = window.centralWidget().findChild(QLineEdit, "lineEditHips").text()
            character["character_buttocks"] = window.centralWidget().findChild(QLineEdit, "lineEditButtocks").text()
            character["character_upperleg"] = window.centralWidget().findChild(QLineEdit, "lineEditUpperLeg").text()
            character["character_knee"] = window.centralWidget().findChild(QLineEdit, "lineEditKnee").text()
            character["character_lowerleg"] = window.centralWidget().findChild(QLineEdit, "lineEditLowerLeg").text()
            character["character_ankle"] = window.centralWidget().findChild(QLineEdit, "lineEditAnkles").text()
            character["character_foot"] = window.centralWidget().findChild(QLineEdit, "lineEditFeet").text()
            character["character_toe"] = window.centralWidget().findChild(QLineEdit, "lineEditToes").text()
            character["character_bodyNotes"] = window.centralWidget().findChild(QTextEdit, "textEditLookDetailsNotes").toPlainText()
            character["character_diagnoses"] = window.centralWidget().findChild(QLineEdit, "lineEditDiagnosis").text()
            character["character_symptoms"] = window.centralWidget().findChild(QLineEdit, "lineEditSymptoms").text()
            character["character_therapies"] = window.centralWidget().findChild(QLineEdit, "lineEditTherapy").text()
            character["character_medications"] = window.centralWidget().findChild(QLineEdit, "lineEditMedication").text()
            character["character_temperament"] = window.centralWidget().findChild(QLineEdit, "lineEditTemperament").text()
            character["character_ethicValues"] = window.centralWidget().findChild(QLineEdit, "lineEditEthicalValues").text()
            character["character_moralValues"] = window.centralWidget().findChild(QLineEdit, "lineEditMoralValues").text()
            character["character_strengthsOfCharacter"] = window.centralWidget().findChild(QLineEdit, "lineEditStrengthsOfCharacter").text()
            character["character_weaknessesOfCharacter"] = window.centralWidget().findChild(QLineEdit, "lineEditWeaknessOfCharacter").text()
            character["character_selfimage"] = window.centralWidget().findChild(QLineEdit, "lineEditSelfImage").text()
            character["character_humor"] = window.centralWidget().findChild(QLineEdit, "lineEditHumor").text()
            character["character_aggressiveness"] = window.centralWidget().findChild(QLineEdit, "lineEditAggressivness").text()
            character["character_traumas"] = window.centralWidget().findChild(QLineEdit, "lineEditTrauma").text()
            character["character_Impressions"] = window.centralWidget().findChild(QLineEdit, "lineEditImpression").text()
            character["character_socialization"] = window.centralWidget().findChild(QLineEdit, "lineEditSocialization").text()
            character["character_norms"] = window.centralWidget().findChild(QLineEdit, "lineEditNorms").text()
            character["character_taboos"] = window.centralWidget().findChild(QLineEdit, "lineEditTaboos").text()
            character["character_psycheNotes"] = window.centralWidget().findChild(QTextEdit, "textEditPsychologyNotes").toPlainText()
            character["character_mainCharacter"] = window.centralWidget().findChild(QCheckBox, "checkBoxMainCharacter").isChecked()
            character["character_notes"] = window.centralWidget().findChild(QTextEdit, "textEditCharacterNotes").toPlainText()
            character["character_development"] = window.centralWidget().findChild(QTextEdit, "textEditDevelopmentNotes").toPlainText()

            with open(Path("data/characters/data_characters.json"), "w", encoding="utf-8") as f:
                json.dump(character_data, f, ensure_ascii=False, indent=2)
            log_info(f"Charakter {character_key} erfolgreich gespeichert.")

        save_btn.clicked.connect(on_save_clicked)

    # --- Daten löschen Button einbinden ---
    delete_btn = window.centralWidget().findChild(QWidget, "deleteBtnCharacter")
    if delete_btn:
        def on_delete_clicked():
            with open(Path("data/characters/data_characters.json"), "r", encoding="utf-8") as f:
                character_data = json.load(f)
            character_key = window.current_character_key
            character_name = character_data[character_key].get("character_name", character_key)
            def delete_character():
                if character_key in character_data:
                    del character_data[character_key]
                    with open(Path("data/characters/data_characters.json"), "w", encoding="utf-8") as f:
                        json.dump(character_data, f, ensure_ascii=False, indent=2)
                    log_info(f"Charakter {character_name} gelöscht.")
                    # Optional: Nächsten Charakter anzeigen oder Felder leeren
            show_secure_dialog(window, action="delete_character", project_key=character_name, on_confirm=delete_character)
        delete_btn.clicked.connect(on_delete_clicked)

    # --- Neuen Charakter Button einbinden ---
    new_btn = window.centralWidget().findChild(QWidget, "newBtnCharacter")
    if new_btn:
        def on_new_clicked():
            with open(Path("data/characters/data_characters.json"), "r", encoding="utf-8") as f:
                character_data = json.load(f)
            # Neuen Key erzeugen
            new_id = f"character_ID_{len(character_data) + 1:02d}"
            # Leeren Datensatz anlegen
            character_data[new_id] = {
                "character_ID": str(len(character_data) + 1),
                "character_name": "",
                "character_firstname": "",
                "character_nickname": "",
                "character_birthdate": "",
                "character_died": "",
                "character_gender": 0,
                "character_sexOrientation": 0,
                "character_status": 0,
                "character_role": 0,
                "character_group": 0,
                "character_mother": "",
                "character_father": "",
                "character_referencePerson": "",
                "character_siblings": "",
                "character_placeOfBirth": "",
                "character_country": "",
                "character_ethnicity": "",
                "character_ancestryNotes ": "",
                "character_school": "",
                "character_university": "",
                "character_vocationalTraining": "",
                "character_profession": "",
                "character_artMusic": "",
                "character_sports": "",
                "character_technology": "",
                "character_autodidact": "",
                "character_educationNotes": "",
                "character_positiveCharacteristics": "",
                "character_negativeCharacteristics": "",
                "character_fears": "",
                "character_weaknesses": "",
                "character_strengths": "",
                "character_talents": "",
                "character_beliefs": "",
                "character_lifeGoals": "",
                "character_motivation": "",
                "character_behavior": "",
                "character_personalityNotes": "",
                "character_height": 175,
                "character_bodyType": 0,
                "character_stature": 0,
                "character_faceshape": 0,
                "character_eyeshape": 0,
                "character_eyesColor": "",
                "character_hair": "",
                "character_hairColor": "",
                "character_skinType": "",
                "character_skinColor": "",
                "character_charisma": "",
                "charactert_specialFeatures": "",
                "character_lookNotes": "",
                "character_head": "",
                "character_neck": "",
                "character_breast": "",
                "character_back": "",
                "character_shoulder": "",
                "character_upperarm": "",
                "character_elbow": "",
                "character_lowerarm": "",
                "character_wrist": "",
                "character_hand": "",
                "character_finger": "",
                "character_hips": "",
                "character_buttocks": "",
                "character_upperleg": "",
                "character_knee": "",
                "character_lowerleg": "",
                "character_ankle": "",
                "character_foot": "",
                "character_toe": "",
                "character_bodyNotes": "",
                "character_diagnoses": "",
                "character_symptoms": "",
                "character_therapies": "",
                "character_medications": "",
                "character_temperament": "",
                "character_ethicValues": "",
                "character_moralValues": "",
                "character_strengthsOfCharacter": "",
                "character_weaknessesOfCharacter": "",
                "character_selfimage": "",
                "character_humor": "",
                "character_aggressiveness": "",
                "character_traumas": "",
                "character_Impressions": "",
                "character_socialization": "",
                "character_norms": "",
                "character_taboos": "",
                "character_psycheNotes": "",
                "character_mainCharacter": False,
                "character_notes": "",
                "character_development": ""
            }
            # Speichern
            with open(Path("data/characters/data_characters.json"), "w", encoding="utf-8") as f:
                json.dump(character_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neuer Charakter {new_id} erstellt.")
            window.current_character_key = new_id
            # Felder leeren
            line_edits = window.centralWidget().findChildren(QLineEdit)
            text_edits = window.centralWidget().findChildren(QTextEdit)
            for widget in line_edits + text_edits:
                widget.clear()
            for combo in window.centralWidget().findChildren(QComboBox):
                combo.setCurrentIndex(0)
            for spin in window.centralWidget().findChildren(QSpinBox):
                spin.setValue(175 if spin.objectName() == "spinBoxSize" else 0)
            for check in window.centralWidget().findChildren(QCheckBox):
                check.setChecked(False)
        new_btn.clicked.connect(on_new_clicked)


    # --- nächster Charakter Button einbinden ---

    # --- vorheriger Charakter Button einbinden ---


    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnCharacter")
    if exit_btn:
        exit_btn.clicked.connect(window.close)

    log_info("Charakterfenster erfolgreich geladen und angezeigt.")
    return window

# Objektfenster anzeigen
def show_objects_window(parent=None):
    window = DynamicWindow("objects_ui", OBJECTS_UI_FILE, splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnObjects")
    if exit_btn:
        exit_btn.clicked.connect(window.close)

    log_info("Objektfenster erfolgreich geladen und angezeigt.")
    return window

# Locationsfenster anzeigen
def show_locations_window(parent=None):
    window = DynamicWindow("locations_ui", LOCATIONS_UI_FILE, splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnLocations")
    if exit_btn:
        exit_btn.clicked.connect(window.close) 

    log_info("Locationsfenster erfolgreich geladen und angezeigt.")
    return window

# Storylinefenster anzeigen
def show_storylines_window(parent=None):
    window = DynamicWindow("storylines_ui", STORYLINES_UI_FILE, splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnStorylines")
    if exit_btn:
        exit_btn.clicked.connect(window.close)

    log_info("Storylinefenster erfolgreich geladen und angezeigt.")
    return window

# Editorfenster anzeigen
def show_editor_window(parent=None):
    window = DynamicWindow("editor_ui", EDITOR_UI_FILE, splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnEditor")
    if exit_btn:
        exit_btn.clicked.connect(window.close)

    log_info(...)
    return window

# Preferences-Fenster anzeigen
def show_preferences_window(parent=None):
    window = DynamicWindow("preferences_ui", PREFERENCES_UI_FILE, splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnPreferences")
    if exit_btn:
        exit_btn.clicked.connect(window.close)

    log_info("Einstellungen-Fenster erfolgreich geladen und angezeigt.")
    return window

# Hilfe-Fenster anzeigen
def show_help_window(parent=None):
    window = DynamicWindow("help_ui", HELP_UI_FILE, splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnHelp")
    if exit_btn:
        exit_btn.clicked.connect(window.close)

    log_info("Hilfe-Fenster erfolgreich geladen und angezeigt.")
    return window

# Anwendung starten
def main():
    setup_logging()
    log_header()
    log_info("Starte CSNova Anwendung")
    app = QApplication(sys.argv)
    try:
        settings = load_settings()
        log_info(f"Einstellungen geladen: {settings}")
        if "first_start" not in settings:
            settings["first_start"] = True
        if "language" not in settings:
            # Nur beim ersten Start: Systemsprache erkennen und speichern
            system_lang = get_system_language()
            settings["language"] = system_lang
            save_settings(settings)
            log_info(f"Sprache in Einstellungen gesetzt: {system_lang}")
        # Ab hier wird immer nur der gespeicherte Wert verwendet!
        if settings.get("first_start", True):
            log_info("Erster Start erkannt, lade Startfenster.")
            show_start_window(settings)
        else:
            log_info("Lade Hauptfenster.")
            show_main_window()
        sys.exit(app.exec())
    except Exception as e:
        log_exception("Fehler beim Start der Anwendung", e)
        sys.exit(1)

if __name__ == "__main__":
    main()