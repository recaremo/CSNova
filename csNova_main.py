import sys
import locale
from PySide6.QtWidgets import (
    QApplication, QLabel, QWidget, 
    QVBoxLayout, QSizePolicy, QSplitter, 
    QMainWindow, QComboBox, QLineEdit, 
    QSpinBox, QTextEdit, QDateEdit)
from PySide6.QtGui import QFont, QIcon
from PySide6 import QtUiTools, QtGui, QtCore
from PySide6.QtCore import QDate
import json
from pathlib import Path
from config.dev import ASSETS_DIR, GUI_DIR
from config.settings import load_settings, save_settings
from core.logger import log_info, log_error, setup_logging, log_header, log_exception

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
def show_secure_dialog(parent=None):
    loader = QtUiTools.QUiLoader()
    secure_window = loader.load(str(SECURE_UI_FILE), parent)
    if secure_window is None:
        log_error(f"Konnte UI-Datei nicht laden: {SECURE_UI_FILE}")
        raise FileNotFoundError(f"Konnte UI-Datei nicht laden: {SECURE_UI_FILE}")
    secure_window.setFont(QFont("Arial", 12))
    secure_window.setWindowModality(QtGui.Qt.ApplicationModal)
    secure_window.setWindowFlags(QtGui.Qt.Dialog)
    secure_window.setStyleSheet("background-color: white;")
    yes_btn = secure_window.findChild(QWidget, "yesBtn")
    no_btn = secure_window.findChild(QWidget, "noBtn")
    if yes_btn:
        yes_btn.clicked.connect(QApplication.quit)
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
            secure_dialog = show_secure_dialog(window)
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

    # Exit-Button verbinden
    exit_btn = window.centralWidget().findChild(QWidget, "exitBnt")
    if exit_btn:
        def on_exit_clicked():
            secure_dialog = show_secure_dialog(window)
            secure_dialog.setWindowModality(QtGui.Qt.ApplicationModal)
        exit_btn.clicked.connect(on_exit_clicked)

    # Save-Button verbinden
    save_btn = window.centralWidget().findChild(QWidget, "saveBtn")
    if save_btn:
        def on_save_clicked():
            settings["first_start"] = False
            save_settings(settings)
            show_main_window()
            window.close()
        save_btn.clicked.connect(on_save_clicked)

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
    first_project = next(iter(projects_data.values()))

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
    fill_combobox(combo_target_group, list(target_groups.values()), first_project.get("project_target_group", 0))

    # 4. Erzählperspektive
    with open(Path("core/translations/narrativePerspective.json"), "r", encoding="utf-8") as f:
        perspectives = json.load(f)[language]
    combo_narrative = window.centralWidget().findChild(QComboBox, "comboBoxProjectNarrativePerspective")
    fill_combobox(combo_narrative, list(perspectives.values()), first_project.get("project_narrative_perspective", 0))

    # 5. Stil
    with open(Path("core/translations/style.json"), "r", encoding="utf-8") as f:
        styles = json.load(f)[language]
    combo_style = window.centralWidget().findChild(QComboBox, "comboBoxProjectStyle")
    fill_combobox(combo_style, list(styles.values()), first_project.get("project_style", 0))

    # 6. Genre
    with open(Path("core/translations/genre.json"), "r", encoding="utf-8") as f:
        genres = json.load(f)[language]["book_genres"]
    combo_genre = window.centralWidget().findChild(QComboBox, "comboBoxProjectGenre")
    fill_combobox(combo_genre, list(genres.values()), first_project.get("project_genre", 0))

    # 7. Arbeitstyp
    with open(Path("core/translations/workingType.json"), "r", encoding="utf-8") as f:
        working_types = json.load(f)[language]["book_working_types"]
    combo_work_type = window.centralWidget().findChild(QComboBox, "comboBoxProjectWorkingType")
    fill_combobox(combo_work_type, list(working_types.values()), first_project.get("project_work_type", 0))

    # 8. Motiv
    with open(Path("core/translations/motif.json"), "r", encoding="utf-8") as f:
        motifs = json.load(f)[language]
    combo_motif = window.centralWidget().findChild(QComboBox, "comboBoxProjectMotif")
    fill_combobox(combo_motif, list(motifs.values()), first_project.get("project_motif", 0))

    # 9. Status
    with open(Path("core/translations/status.json"), "r", encoding="utf-8") as f:
        status = json.load(f)[language]
    combo_status = window.centralWidget().findChild(QComboBox, "comboBoxProjectStatus")
    fill_combobox(combo_status, list(status.values()), first_project.get("project_status", 0))

    # 10. Verlag
    with open(Path("core/translations/publisher.json"), "r", encoding="utf-8") as f:
        publishers = json.load(f)["publishers"]
    publisher_names = [pub["name"] for pub in publishers if pub["type"] == "book"]
    combo_publisher = window.centralWidget().findChild(QComboBox, "comboBoxPublisher")
    fill_combobox(combo_publisher, publisher_names, first_project.get("project_publisher", 0))

    # Beispiel: Weitere Felder setzen
    window.centralWidget().findChild(QLineEdit, "lineEditProjectTitle").setText(first_project.get("project_title", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditProjectSubtitle").setText(first_project.get("project_subtitle", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditProjectAuthor").setText(first_project.get("project_author", ""))
    window.centralWidget().findChild(QLineEdit, "lineEditProjectPremise").setText(first_project.get("project_premise", ""))
    spin_box = window.centralWidget().findChild(QSpinBox, "spinBoxProjectWordsCount")
    if spin_box:
        spin_box.setValue(int(first_project.get("project_word_goal", 0)))
    notes_edit = window.centralWidget().findChild(QTextEdit, "textEditProjectNotes")
    if notes_edit:
        notes_edit.setPlainText(first_project.get("project_notes", ""))
    # Datum Beginn
    begin_date_edit = window.centralWidget().findChild(QDateEdit, "dateEditProjectBegin")
    if begin_date_edit:
        begin_str = first_project.get("project_begin_date", "")
        if begin_str:
            # Format: "yyyy-MM-dd"
            date = QDate.fromString(begin_str, "yyyy-MM-dd")
            if date.isValid():
                begin_date_edit.setDate(date)
    # Datum Deadline
    deadline_date_edit = window.centralWidget().findChild(QDateEdit, "dateEditProjectDeadLine")
    if deadline_date_edit:
        deadline_str = first_project.get("project_deadline", "")
        if deadline_str:
            date = QDate.fromString(deadline_str, "yyyy-MM-dd")
            if date.isValid():
                deadline_date_edit.setDate(date)

    # Buttons einbinden
    # --- Exit-Button einbinden ---
    exit_btn = window.centralWidget().findChild(QWidget, "exitBtnProjects")
    if exit_btn:
        exit_btn.clicked.connect(window.close)
    # --- Save-Button einbinden ---
    save_btn = window.centralWidget().findChild(QWidget, "saveBtnProjects")
    if save_btn:
        def on_save_clicked():
            # Lade aktuelle Projektdaten
            with open(Path("data/projects/data_projects.json"), "r", encoding="utf-8") as f:
                projects_data = json.load(f)
            # Hole das erste Projekt (oder das aktuell ausgewählte)
            project_key = next(iter(projects_data.keys()))
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
            log_info("Projekt erfolgreich gespeichert.")

        save_btn.clicked.connect(on_save_clicked)    

    return window

# Charakterfenster anzeigen
def show_characters_window(parent=None):
    window = DynamicWindow("characters_ui", CHARACTERS_UI_FILE, splitter_name="mainSplitter")
    window.show()
    log_info("Charakterfenster erfolgreich geladen und angezeigt.")
    return window

# Objektfenster anzeigen
def show_objects_window(parent=None):
    window = DynamicWindow("objects_ui", OBJECTS_UI_FILE, splitter_name="mainSplitter")
    window.show()
    log_info("Objektfenster erfolgreich geladen und angezeigt.")
    return window

# Locationsfenster anzeigen
def show_locations_window(parent=None):
    window = DynamicWindow("locations_ui", LOCATIONS_UI_FILE, splitter_name="mainSplitter")
    window.show()
    log_info("Locationsfenster erfolgreich geladen und angezeigt.")
    return window

# Storylinefenster anzeigen
def show_storylines_window(parent=None):
    window = DynamicWindow("storylines_ui", STORYLINES_UI_FILE, splitter_name="mainSplitter")
    window.show()
    log_info("Storylinefenster erfolgreich geladen und angezeigt.")
    return window

# Editorfenster anzeigen
def show_editor_window(parent=None):
    window = DynamicWindow("editor_ui", EDITOR_UI_FILE, splitter_name="mainSplitter")
    window.show()
    log_info(...)
    return window

# Preferences-Fenster anzeigen
def show_preferences_window(parent=None):
    window = DynamicWindow("preferences_ui", PREFERENCES_UI_FILE, splitter_name="mainSplitter")
    window.show()
    log_info("Einstellungen-Fenster erfolgreich geladen und angezeigt.")
    return window

# Hilfe-Fenster anzeigen
def show_help_window(parent=None):
    window = DynamicWindow("help_ui", HELP_UI_FILE, splitter_name="mainSplitter")
    window.show()
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
            settings["language"] = "de"
        system_lang = get_system_language()
        log_info(f"Systemsprache erkannt: {system_lang}")
        if settings.get("language") != system_lang:
            settings["language"] = system_lang
            save_settings(settings)
            log_info(f"Sprache in Einstellungen aktualisiert: {system_lang}")
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