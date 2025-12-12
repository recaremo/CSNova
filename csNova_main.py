# Standardbibliothek
import sys
import locale
import json
import tempfile
from typing import Optional, Dict, Any
from json import JSONDecodeError
from pathlib import Path
from datetime import datetime

# Drittanbieter
from PySide6.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout, QSplitter, QListWidget,
    QMainWindow, QComboBox, QLineEdit, QSpinBox, QTextEdit, QDateEdit, QCheckBox,
    QToolBar, QDockWidget, QDialog, QFontComboBox, QFileDialog, QMessageBox
)
from PySide6.QtGui import QIcon, QRegularExpressionValidator
from PySide6.QtCore import QDate, QRegularExpression
from PySide6 import QtUiTools, QtGui, QtCore

# Eigene Module
from config.dev import ASSETS_DIR, GUI_DIR
from config.settings import load_settings, save_settings
from core.logger import log_info, log_error, setup_logging, log_header, log_exception

# UI Files initialisieren
UI_FILES = {
    "main": GUI_DIR / "csNova.ui",
    "start": GUI_DIR / "csNova_Start.ui",
    "secure": GUI_DIR / "formSecure.ui",
    "projects": GUI_DIR / "csNova_Projects.ui",
    "characters": GUI_DIR / "csNova_Characters.ui",
    "objects": GUI_DIR / "csNova_Objects.ui",
    "locations": GUI_DIR / "csNova_Locations.ui",
    "storylines": GUI_DIR / "csNova_Storylines.ui",
    "editor": GUI_DIR / "csNova_Editor.ui",
    "preferences": GUI_DIR / "csNova_Preferences.ui",
    "help": GUI_DIR / "csNova_Help_Tips.ui"
}
# Globale Referenzen auf Fenster und Manager
class CSNovaApp:
    def __init__(self):
        self.main_window = None
        self.start_window = None
        self.help_window = None
        # Alle Daten-Manager
        self.references = None
        self.citations = None
        self.projects = None
        self.characters = None
        self.locations = None
        self.objects = None
        self.storylines = None
        self.ideas = None
        self.chapters = None
        # Backwards compatibility
        self.ref_manager = None
        self.cite_manager = None
app_state = CSNovaApp()

# Fensterereignisse verbinden, um UI-Einstellungen zu speichern
class DynamicWindow(QMainWindow):
    def __init__(self, settings_key, ui_file, splitter_name="mainSplitter", confirm_on_close=False):
        super().__init__()
        self.settings_key = settings_key
        self.confirm_on_close = confirm_on_close
        self._closing = False
        loader = QtUiTools.QUiLoader()
        ui = loader.load(str(ui_file))  # ohne parent laden

        # Falls die geladene .ui ein QMainWindow ist: übernehme dessen Komponenten
        if isinstance(ui, QMainWindow):
            # Central widget übernehmen
            central = ui.centralWidget()
            if central:
                central.setParent(self)
                self.setCentralWidget(central)
            else:
                ui.setParent(self)
                self.setCentralWidget(ui)

            # Menüleiste übernehmen
            try:
                menubar = ui.menuBar()
                if menubar:
                    menubar.setParent(self)
                    self.setMenuBar(menubar)
            except Exception:
                pass

            # Statusbar übernehmen
            try:
                statusbar = ui.statusBar()
                if statusbar:
                    statusbar.setParent(self)
                    self.setStatusBar(statusbar)
            except Exception:
                pass

            # Toolbars übernehmen
            try:
                for tb in ui.findChildren(QToolBar):
                    tb.setParent(self)
                    self.addToolBar(tb)
            except Exception:
                pass

            # DockWidgets übernehmen
            try:
                for dock in ui.findChildren(QDockWidget):
                    dock.setParent(self)
                    allowed = dock.allowedAreas()
                    area = None
                    for a in (QtCore.Qt.LeftDockWidgetArea, QtCore.Qt.RightDockWidgetArea,
                              QtCore.Qt.TopDockWidgetArea, QtCore.Qt.BottomDockWidgetArea):
                        if allowed & a:
                            area = a
                            break
                    if area is None:
                        area = QtCore.Qt.LeftDockWidgetArea
                    self.addDockWidget(area, dock)
            except Exception:
                pass

            # Fenster-Titel, Flags und Icon übernehmen
            try:
                title = ui.windowTitle()
                if title:
                    self.setWindowTitle(title)
            except Exception:
                pass
            try:
                flags = ui.windowFlags()
                self.setWindowFlags(flags)
            except Exception:
                pass
            try:
                icon = ui.windowIcon()
                if not icon.isNull():
                    self.setWindowIcon(icon)
            except Exception:
                pass

            ui.deleteLater()
        else:
            ui.setParent(self)
            self.setCentralWidget(ui)

        try:
            self.setWindowIcon(QIcon(str(ASSETS_DIR / "media" / "csnova.png")))
        except Exception:
            pass
        apply_ui_settings(self, settings_key, splitter_name=splitter_name)
        connect_dynamic_events(self, splitter_name=splitter_name)

    def save_window_settings(self):
        ui_settings = self.ui_settings.copy()
        if not self.isMaximized():
            size = self.size()
            ui_settings["win_width"] = size.width()
            ui_settings["win_height"] = size.height()
        ui_settings["win_maximized"] = self.isMaximized()
        settings = load_settings()
        settings[self.settings_key] = ui_settings
        save_settings(settings)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.save_window_settings()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            self.save_window_settings()
        super().changeEvent(event)

    @property
    def ui_settings(self):
        settings = load_settings()
        return settings.get(self.settings_key, {})

    def closeEvent(self, event):
        # If already in programmatic shutdown, accept and return
        if getattr(self, "_closing", False):
            event.accept()
            return

        if not getattr(self, "confirm_on_close", False):
            event.accept()
            return

        try:
            confirmed = show_secure_dialog(self, action="exit")
        except Exception as e:
            # Log the exception and do NOT accept — avoid unexpected close loops
            log_exception("Fehler beim Anzeigen des Sicherheitsdialogs beim Schließen", e)
            event.ignore()
            return

        if confirmed:
            # mark as closing so subsequent closeEvent calls don't re-open the dialog
            self._closing = True
            event.accept()
            QApplication.quit()
        else:
            event.ignore()

# Fensterereignisse verbinden, um UI-Einstellungen zu speichern
def connect_dynamic_events(window, splitter_name=None):
    if splitter_name and window.centralWidget() is not None:
        splitter = window.centralWidget().findChild(QSplitter, splitter_name)
        if splitter:
            def on_splitter_size_changed():
                settings = load_settings()
                ui_settings = settings.get(window.settings_key, {})
                ui_settings["win_splitter"] = splitter.sizes()
                settings[window.settings_key] = ui_settings
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
def show_secure_dialog(parent=None, action="exit", project_key=None) -> bool:

    # Versuche parent sinnvoll zu wählen
    parent_win = parent or QApplication.activeWindow() or getattr(app_state, "main_window", None)

    loader = QtUiTools.QUiLoader()
    content = None
    try:
        content = loader.load(str(UI_FILES["secure"]))
    except Exception as e:
        log_exception("show_secure_dialog: UI load failed", e)
        content = None

    # Fallback: QMessageBox (sichtbar, zuverlässig)
    if content is None:
        from PySide6.QtWidgets import QMessageBox
        msg = QMessageBox(parent_win)
        msg.setIcon(QMessageBox.Question)
        if action == "exit":
            text = "Möchten Sie das Programm wirklich beenden?"
        elif action.startswith("delete") and project_key:
            text = f"Möchten Sie '{project_key}' wirklich löschen?"
        else:
            text = "Bitte bestätigen."
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setWindowModality(QtCore.Qt.ApplicationModal)
        try:
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        except Exception:
            pass
        msg.raise_()
        msg.activateWindow()
        res = msg.exec()
        return res == QMessageBox.Yes

    # Erzeuge Dialog als child/transient (besseres Verhalten auf Wayland/X11)
    try:
        dialog = QDialog(parent_win)
        dialog.setModal(True)
        # Flags: Dialog + System menu + stay on top hint (WM-freundlich)
        flags = QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint
        dialog.setWindowFlags(flags)
        try:
            dialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        except Exception:
            pass
    except Exception as e:
        log_exception("show_secure_dialog: failed to create QDialog with parent", e)
        dialog = QDialog(None)
        dialog.setModal(True)

    # Packe geladenes UI ein
    try:
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(6, 6, 6, 6)
        content.setParent(dialog)
        layout.addWidget(content)
    except Exception as e:
        log_exception("show_secure_dialog: failed to place content into dialog", e)
        dialog = None

    if dialog is None:
        # fallback to message box
        from PySide6.QtWidgets import QMessageBox
        msg = QMessageBox(parent_win)
        msg.setText("Fehler beim Anzeigen des Bestätigungsdialogs.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
        return False

    # Finde Widgets und setze Texte / Verbindungen
    infoText = content.findChild(QLabel, "infoText")
    yes_btn = content.findChild(QWidget, "yesBtn")
    no_btn = content.findChild(QWidget, "noBtn")
  

    if action == "exit":
        if infoText:
            infoText.setText("Möchten Sie das Programm wirklich beenden?")
    elif action.startswith("delete") and infoText and project_key:
        infoText.setText(f"Möchten Sie '{project_key}' wirklich löschen?")

    # Verbinde vorhandene Buttons mit accept/reject
    if yes_btn and hasattr(yes_btn, "clicked"):
        yes_btn.clicked.connect(dialog.accept)
    if no_btn and hasattr(no_btn, "clicked"):
        no_btn.clicked.connect(dialog.reject)

    # Falls die UI keine Buttons (oder nicht funktionsfähige) enthält: eigene hinzufügen
    if (not yes_btn or not hasattr(yes_btn, "clicked")) or (not no_btn or not hasattr(no_btn, "clicked")):
        from PySide6.QtWidgets import QPushButton, QHBoxLayout
        btn_container = QWidget()
        hb = QHBoxLayout(btn_container)
        hb.addStretch()
        yes = QPushButton("Ja")
        no = QPushButton("Nein")
        yes.clicked.connect(dialog.accept)
        no.clicked.connect(dialog.reject)
        hb.addWidget(yes)
        hb.addWidget(no)
        layout.addWidget(btn_container)

    # Größe sicherstellen (sizeHint / Mindestgröße) — viele WM zeigen sonst nichts
    try:
        dialog.adjustSize()
        sh = dialog.sizeHint()
        minw = max(320, sh.width())
        minh = max(140, sh.height())
        dialog.resize(minw, minh)
        dialog.setMinimumSize(minw, minh)
    except Exception as e:
        log_exception("show_secure_dialog: sizing failed", e)

    # Sichtbar machen, Vordergrund erzwingen, Event-Loop kurz laufen lassen
    try:
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()
        QApplication.processEvents()
    except Exception as e:
        log_exception("show_secure_dialog: show/raise/activate failed", e)

    try:
        result = dialog.exec()
    except Exception as e:
        log_exception("show_secure_dialog: exec() failed", e)
        return False

    return result == QDialog.Accepted
# Globale Referenzen auf Fenster
def get_widget(parent, widget_type, name):
    try:
        # safe centralWidget access
        cw = None
        try:
            cw = parent.centralWidget()
        except Exception:
            cw = None
        widget = None
        if cw is not None:
            widget = cw.findChild(widget_type, name)
        if widget is None and hasattr(parent, "findChild"):
            widget = parent.findChild(widget_type, name)
        if widget is None:
            log_error(f"Widget '{name}' ({widget_type.__name__}) nicht gefunden im Fenster '{getattr(parent, 'windowTitle', lambda: '')()}'")
        return widget
    except Exception as e:
        log_exception(f"get_widget: Fehler beim Suchen von {name}", e)
        return None
# Hilfsfunktionen zum Setzen von Werten in Widgets
def set_text(parent, widget_type, name, value):
    widget = get_widget(parent, widget_type, name)
    if widget:
        if hasattr(widget, "setText"):
            widget.setText(value)
        elif hasattr(widget, "setPlainText"):
            widget.setPlainText(value)
# Setzt den aktuellen Index einer ComboBox
def set_index(parent, widget_type, name, index):
    widget = get_widget(parent, widget_type, name)
    if widget and hasattr(widget, "setCurrentIndex"):
        widget.setCurrentIndex(index)
# Setzt den Wert eines SpinBox-Widgets
def set_value(parent, widget_type, name, value):
    widget = get_widget(parent, widget_type, name)
    if widget and hasattr(widget, "setValue"):
        widget.setValue(value)
# Setzt den Checked-Status eines CheckBox-Widgets
def set_checked(parent, widget_type, name, checked):
    widget = get_widget(parent, widget_type, name)
    if widget and hasattr(widget, "setChecked"):
        widget.setChecked(checked)
# Findet ein Kind-Widget im zentralen Widget des Fensters
def winFindChild(window, widget_type, name):
    return get_widget(window, widget_type, name)
# Sicheres Laden von JSON-Dateien
def safe_load_json(path: Path, default: Any = None) -> Any:
    try:
        if not path.exists():
            return default if default is not None else {}
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (JSONDecodeError, OSError) as e:
        log_error(f"safe_load_json: failed to load {path}: {e}")
        return default if default is not None else {}
# Sicheres Speichern von JSON-Dateien
def safe_save_json(path: Path, data: Any) -> bool:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=str(path.parent)) as tf:
            json.dump(data, tf, ensure_ascii=False, indent=2)
            tmpname = tf.name
        Path(tmpname).replace(path)
        return True
    except Exception as e:
        log_exception(f"safe_save_json: failed to save {path}", e)
        return False
# Generiert den nächsten eindeutigen Key und eine fortlaufende ID
def get_next_id(data_dict, prefix):
    max_id = 0
    for key, entry in data_dict.items():
        # Extrahiere die Nummer aus dem Key oder aus dem Feld
        if key.startswith(prefix):
            try:
                num = int(key.replace(prefix, ""))
                max_id = max(max_id, num)
            except Exception:
                pass
        # Falls das Feld existiert
        if isinstance(entry, dict) and entry.get(f"{prefix[:-1]}", "").isdigit():
            num = int(entry[f"{prefix[:-1]}"])
            max_id = max(max_id, num)
    next_num = max_id + 1
    return f"{prefix}{next_num:02d}", str(next_num)
# Übersetzungs- / static JSON Cache
_TRANSLATION_CACHE: Dict[str, Any] = {}
# Lade Übersetzungen aus JSON-Dateien mit Caching
def load_translation(path: Path, language: str = "de", default_lang: str = "de") -> Any:
    key = f"{path}:{language}"
    if key in _TRANSLATION_CACHE:
        return _TRANSLATION_CACHE[key]
    data = safe_load_json(path, {})
    if isinstance(data, dict) and language in data:
        result = data[language]
    else:
        # fallback: default_lang or first value
        if isinstance(data, dict):
            result = data.get(default_lang, next(iter(data.values())) if data else {})
        else:
            result = data
    _TRANSLATION_CACHE[key] = result
    return result
# Füllt eine ComboBox mit Werten und setzt den ausgewählten Index oder Wert
def fill_combobox(combo: Optional[QComboBox], values: list, selected_index_or_value=0):
    if combo is None:
        return
    combo.clear()
    combo.addItems(list(values))
    if isinstance(selected_index_or_value, int):
        idx = selected_index_or_value if 0 <= selected_index_or_value < combo.count() else 0
    else:
        try:
            idx = values.index(selected_index_or_value)
        except Exception:
            idx = 0
    combo.setCurrentIndex(idx)


# -------------------------------------------------------------------------------------
# Grundlegende Mappings und Konstanten für Charaktere
# -------------------------------------------------------------------------------------
# Mapping der Charakterfelder zu Widget-Typen und Namen
CHARACTER_FIELD_MAP = {
        "character_status": (QComboBox, "comboBoxStatus"),
        "character_name": (QLineEdit, "lineEditName"),
        "character_firstname": (QLineEdit, "lineEditFirstName"),
        "character_nickname": (QLineEdit, "lineEditNickName"),
        "character_birthdate": (QLineEdit, "lineEditBorn"),
        "character_died": (QLineEdit, "lineEditDied"),
        "character_gender": (QComboBox, "comboBoxGender"),
        "character_sexOrientation": (QComboBox, "comboBoxSexOrientation"),
        "character_role": (QComboBox, "comboBoxRole"),
        "character_group": (QComboBox, "comboBoxGroup"),
        "character_development": (QTextEdit, "textEditDevelopmentNotes"),
        "character_notes": (QTextEdit, "textEditCharacterNotes"),
        "character_mother": (QLineEdit, "lineEditMother"),
        "character_father": (QLineEdit, "lineEditFather"),
        "character_referencePerson": (QLineEdit, "lineEditReferencePerson"),
        "character_siblings": (QTextEdit, "textEditSiblings"),
        "character_placeOfBirth": (QLineEdit, "lineEditPlaceOfBirth"),
        "character_country": (QLineEdit, "lineEditCountry"),
        "character_ethnicity": (QLineEdit, "lineEditEthnicity"),
        "character_ancestryNotes": (QTextEdit, "textEditAncestryNotes"),
        "character_school": (QTextEdit, "textEditSchool"),
        "character_university": (QTextEdit, "textEditUniversity"),
        "character_vocationalTraining": (QTextEdit, "textEditVocationalTraining"),
        "character_profession": (QTextEdit, "textEditProfession"),
        "character_artMusic": (QTextEdit, "textEditArtMusic"),
        "character_sports": (QTextEdit, "textEditSport"),
        "character_technology": (QTextEdit, "textEditTechnic"),
        "character_autodidact": (QTextEdit, "textEditAutodidact"),
        "character_educationNotes": (QTextEdit, "textEditEducationNotes"),
        "character_positiveCharacteristics": (QLineEdit, "lineEditPosCharacteristics"),
        "character_negativeCharacteristics": (QLineEdit, "lineEditNegCharacteristics"),
        "character_fears": (QLineEdit, "lineEditFears"),
        "character_weaknesses": (QLineEdit, "lineEditWeakness"),
        "character_strengths": (QLineEdit, "lineEditStrength"),
        "character_talents": (QLineEdit, "lineEditTalents"),
        "character_beliefs": (QLineEdit, "lineEditBelief"),
        "character_lifeGoals": (QLineEdit, "lineEditLifeGoal"),
        "character_motivation": (QLineEdit, "lineEditMotivation"),
        "character_behavior": (QLineEdit, "lineEditBehavior"),
        "character_personalityNotes": (QTextEdit, "textEditPersonalityNotes"),
        "character_height": (QSpinBox, "spinBoxSize"),
        "character_bodyType": (QComboBox, "comboBoxBodyType"),
        "character_stature": (QComboBox, "comboBoxStature"),
        "character_faceshape": (QComboBox, "comboBoxFaceShape"),
        "character_eyeshape": (QComboBox, "comboBoxEyeShape"),
        "character_eyesColor": (QLineEdit, "lineEditEyeColor"),
        "character_hair": (QLineEdit, "lineEditHair"),
        "character_hairColor": (QLineEdit, "lineEditHairColor"),
        "character_skinType": (QLineEdit, "lineEditSkin"),
        "character_skinColor": (QLineEdit, "lineEditSkinColor"),
        "character_charisma": (QLineEdit, "lineEditCharisma"),
        "character_specialFeatures": (QLineEdit, "lineEditSpecialFeatures"),
        "character_lookNotes": (QTextEdit, "textEditLookNotes"),
        "character_head": (QLineEdit, "lineEditHead"),
        "character_neck": (QLineEdit, "lineEditNeck"),
        "character_breast": (QLineEdit, "lineEditBreast"),
        "character_back": (QLineEdit, "lineEditBack"),
        "character_shoulder": (QLineEdit, "lineEditShoulders"),
        "character_upperarm": (QLineEdit, "lineEditUpperArm"),
        "character_elbow": (QLineEdit, "lineEditElbow"),
        "character_lowerarm": (QLineEdit, "lineEditLowerArms"),
        "character_wrist": (QLineEdit, "lineEditWrists"),
        "character_hand": (QLineEdit, "lineEditHand"),
        "character_finger": (QLineEdit, "lineEditFinger"),
        "character_hips": (QLineEdit, "lineEditHips"),
        "character_buttocks": (QLineEdit, "lineEditButtocks"),
        "character_upperleg": (QLineEdit, "lineEditUpperLeg"),
        "character_knee": (QLineEdit, "lineEditKnee"),
        "character_lowerleg": (QLineEdit, "lineEditLowerLeg"),
        "character_ankle": (QLineEdit, "lineEditAnkles"),
        "character_foot": (QLineEdit, "lineEditFeet"),
        "character_toe": (QLineEdit, "lineEditToes"),
        "character_bodyNotes": (QTextEdit, "textEditLookDetailsNotes"),
        "character_diagnoses": (QLineEdit, "lineEditDiagnosis"),
        "character_symptoms": (QLineEdit, "lineEditSymptoms"),
        "character_therapies": (QLineEdit, "lineEditTherapy"),
        "character_medications": (QLineEdit, "lineEditMedication"),
        "character_temperament": (QLineEdit, "lineEditTemperament"),
        "character_ethicValues": (QLineEdit, "lineEditEthicalValues"),
        "character_moralValues": (QLineEdit, "lineEditMoralValues"),
        "character_strengthsOfCharacter": (QLineEdit, "lineEditStrengthsOfCharacter"),
        "character_weaknessesOfCharacter": (QLineEdit, "lineEditWeaknessOfCharacter"),
        "character_selfimage": (QLineEdit, "lineEditSelfImage"),
        "character_humor": (QLineEdit, "lineEditHumor"),
        "character_aggressiveness": (QLineEdit, "lineEditAggressivness"),
        "character_traumas": (QLineEdit, "lineEditTrauma"),
        "character_Impressions": (QLineEdit, "lineEditImpression"),
        "character_socialization": (QLineEdit, "lineEditSocialization"),
        "character_norms": (QLineEdit, "lineEditNorms"),
        "character_taboos": (QLineEdit, "lineEditTaboos"),
        "character_psycheNotes": (QTextEdit, "textEditPsychologyNotes"),
    }
# Liest die Werte aus den Charakter-Widgets aus
def read_character_fields(window):
    character = {}
    for field, (widget_type, widget_name) in CHARACTER_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                character[field] = widget.text()
            elif isinstance(widget, QTextEdit):
                character[field] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                character[field] = widget.currentIndex()
            elif isinstance(widget, QSpinBox):
                character[field] = widget.value()
            elif isinstance(widget, QCheckBox):
                character[field] = widget.isChecked()
            elif isinstance(widget, QDateEdit):
                character[field] = widget.date().toString("yyyy-MM-dd")
    return character
# Setzut die Werte aus den Charakter-Widgets basierend auf einem Charakter-Dictionary
def update_character_fields(window, character):
    for field, (widget_type, widget_name) in CHARACTER_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        value = character.get(field, "")
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QSpinBox):
                try:
                    widget.setValue(int(value))
                except Exception:
                    widget.setValue(0)
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)
# Gibt eine leere Charakter-Datenstruktur zurück
def get_empty_character():
    return {
        "character_ID": "",
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
        "character_development": "",
        "character_notes": "",
        "character_mother": "",
        "character_father": "",
        "character_referencePerson": "",
        "character_siblings": "",
        "character_placeOfBirth": "",
        "character_country": "",
        "character_ethnicity": "",
        "character_ancestryNotes": "",
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
        "character_specialFeatures": "",
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
        "character_mainCharacter": False
    }

# -------------------------------------------------------------------------------------
# Grundlegende Mappings und Konstanten für Projekte
# -------------------------------------------------------------------------------------
# Mapping der Projektfelder zu Widget-Typen, Namen und Getter-Methoden
PROJECTS_FIELD_MAP = {
    "project_title": (QLineEdit, "lineEditProjectTitle", "text"),
    "project_subtitle": (QLineEdit, "lineEditProjectSubtitle", "text"),
    "project_author": (QLineEdit, "lineEditProjectAuthor", "text"),
    "project_premise": (QLineEdit, "lineEditProjectPremise", "text"),
    "project_target_group": (QComboBox, "comboBoxProjectTargetGroup", "currentIndex"),
    "project_narrative_perspective": (QComboBox, "comboBoxProjectNarrativePerspective", "currentIndex"),
    "project_style": (QComboBox, "comboBoxProjectStyle", "currentIndex"),
    "project_genre": (QComboBox, "comboBoxProjectGenre", "currentIndex"),
    "project_work_type": (QComboBox, "comboBoxProjectWorkingType", "currentIndex"),
    "project_motif": (QComboBox, "comboBoxProjectMotif", "currentIndex"),
    "project_begin_date": (QDateEdit, "dateEditProjectBegin", "date"),
    "project_deadline": (QDateEdit, "dateEditProjectDeadLine", "date"),
    "project_status": (QComboBox, "comboBoxProjectStatus", "currentIndex"),
    "project_word_goal": (QSpinBox, "spinBoxProjectWordsCount", "value"),
    "project_data_file": (QLineEdit, "lineEditProjectDataFile", "text"),
    "project_notes": (QTextEdit, "textEditProjectNotes", "toPlainText"),
    "project_publisher": (QComboBox, "comboBoxProjectPublisher", "currentIndex"),
    "project_editor": (QComboBox, "comboBoxProjectEditor", "currentIndex"),
    "project_isbn": (QLineEdit, "lineEditProjectISBN", "text"),
    "project_issn": (QLineEdit, "lineEditProjectISSN", "text")
}
# Liest die Werte aus den Projekt-Widgets aus
def read_project_fields(window):
    project = {}
    for field, (widget_type, widget_name, getter) in PROJECTS_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        if widget:
            if getter == "isChecked":
                project[field] = widget.isChecked()
            elif getter in ("value", "currentIndex"):
                project[field] = widget.__getattribute__(getter)()
            elif getter == "date":
                project[field] = widget.date().toString("yyyy-MM-dd")
            else:
                project[field] = widget.__getattribute__(getter)()
    return project
# Setzt die Werte der Projekt-Widgets basierend auf einem Projekt-Dictionary
def update_project_fields(window, project):
    for field, (widget_type, widget_name, _) in PROJECTS_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        value = project.get(field, "")
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QSpinBox):
                try:
                    widget.setValue(int(value))
                except Exception:
                    widget.setValue(0)
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)
# Gibt eine leere Projekt-Datenstruktur zurück
def get_empty_project():
    today_str = QDate.currentDate().toString("yyyy-MM-dd")
    return {
        "project_ID": "",
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
        "project_editor": 0,
        "project_isbn": "",
        "project_issn": ""
    }

# -------------------------------------------------------------------------------------
# Grundlegende Mappings und Konstanten für Objekte
# -------------------------------------------------------------------------------------
# Mapping der Objektfelder zu Widget-Typen und Namen
OBJECTS_FIELD_MAP = {
        "object_title": (QLineEdit, "titleObjects"),
        "object_status": (QComboBox, "comboBoxObjectsStatus"),
        "object_created": (QDateEdit, "dateEditCreatedObjects"),
        "object_modified": (QDateEdit, "dateEditEditedObjects"),
        "object_notes": (QTextEdit, "textDescriptionObjects"),


    }
# Liest die Werte aus den Objekt-Widgets aus
def read_object_fields(window):
    obj = {}
    for field, (widget_type, widget_name) in OBJECTS_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                obj[field] = widget.text()
            elif isinstance(widget, QTextEdit):
                obj[field] = widget.toPlainText()
            elif isinstance(widget, QDateEdit):
                obj[field] = widget.date().toString("yyyy-MM-dd")
            elif isinstance(widget, QComboBox):
                obj[field] = widget.currentIndex()
            elif isinstance(widget, QListWidget):
                obj[field] = [widget.item(i).text() for i in range(widget.count())]
    return obj
# Setzt die Werte aus den Objekt-Widgets basierend auf einem Objekt-Dictionary
def update_object_fields(window, obj):
    for field, (widget_type, widget_name) in OBJECTS_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        value = obj.get(field, "")
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QListWidget):
                widget.clear()
                if isinstance(value, list):
                    widget.addItems(value)
# Gibt eine leere Objekt-Datenstruktur zurück
def get_empty_object():
    return {
        "object_ID": "",
        "object_title": "",
        "object_status": 0,
        "object_created": "",
        "object_modified": "",
        "object_notes": ""
    }

# -------------------------------------------------------------------------------------
# Grundlegende Mappings und Konstanten für Locations
# -------------------------------------------------------------------------------------
# Mapping der Locationsfelder zu Widget-Typen und Namen
LOCATIONS_FIELD_MAP = {
        "location_title": (QLineEdit, "titleLocations"),
        "location_status": (QComboBox, "comboBoxLocationsStatus"),
        "location_created": (QDateEdit, "dateEditCreatedLocations"),
        "location_modified": (QDateEdit, "dateEditEditedLocations"),
        "location_notes": (QTextEdit, "textDescriptionLocations"),
    }
# Liest die Werte aus den Locations-Widgets aus
def read_location_fields(window):
    location = {}
    for field, (widget_type, widget_name) in LOCATIONS_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                location[field] = widget.text()
            elif isinstance(widget, QTextEdit):
                location[field] = widget.toPlainText()
            elif isinstance(widget, QDateEdit):
                location[field] = widget.date().toString("yyyy-MM-dd")
            elif isinstance(widget, QComboBox):
                location[field] = widget.currentIndex()
            elif isinstance(widget, QListWidget):
                location[field] = [widget.item(i).text() for i in range(widget.count())]
    return location
# Setzt die Werte aus den Locations-Widgets basierend auf einem Locations-Dictionary
def update_location_fields(window, location):
    for field, (widget_type, widget_name) in LOCATIONS_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        value = location.get(field, "")
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QListWidget):
                widget.clear()
                if isinstance(value, list):
                    widget.addItems(value)
# Gibt eine leere Locations-Datenstruktur zurück
def get_empty_location():
    return {
        "location_ID": "",
        "location_title": "",
        "location_status": 0,
        "location_created": "",
        "location_modified": "",
        "location_notes": ""
    }

# -------------------------------------------------------------------------------------
# Grundlegende Mappings und Konstanten für Storylines
# -------------------------------------------------------------------------------------
# Mapping der Storylinefelder zu Widget-Typen und Namen
STORYLINES_FIELD_MAP = {
        "storyline_title": (QLineEdit, "titleStorylines"),
        "storyline_status": (QComboBox, "comboBoxStorylinesStatus"),
        "storyline_created": (QDateEdit, "dateEditCreatedStorylines"),
        "storyline_modified": (QDateEdit, "dateEditEditedStorylines"),
        "storyline_notes": (QTextEdit, "textDescriptionStorylines"),
    }
# Liest die Werte aus den Storyline-Widgets aus
def read_storyline_fields(window):
    storyline = {}
    for field, (widget_type, widget_name) in STORYLINES_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                storyline[field] = widget.text()
            elif isinstance(widget, QTextEdit):
                storyline[field] = widget.toPlainText()
            elif isinstance(widget, QDateEdit):
                storyline[field] = widget.date().toString("yyyy-MM-dd")
            elif isinstance(widget, QComboBox):
                storyline[field] = widget.currentIndex()
            elif isinstance(widget, QListWidget):
                storyline[field] = [widget.item(i).text() for i in range(widget.count())]
    return storyline
# Setzt die Werte aus den Storyline-Widgets basierend auf einem Storyline-Dictionary
def update_storyline_fields(window, storyline):
    for field, (widget_type, widget_name) in STORYLINES_FIELD_MAP.items():
        widget = get_widget(window, widget_type, widget_name)
        value = storyline.get(field, "")
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QListWidget):
                widget.clear()
                if isinstance(value, list):
                    widget.addItems(value)
# Gibt eine leere Storyline-Datenstruktur zurück
def get_empty_storyline():
    return {
        "storyline_ID": "",
        "storyline_title": "",
        "storyline_status": 0,
        "storyline_created": "",
        "storyline_modified": "",
        "storyline_notes": ""
    }


# -------------------------------------------------------------------------------------
# Grundlegendes Mapping und Konstanten für Kaptiel und Szenen im Editor
# -------------------------------------------------------------------------------------
# Mapping der Kapitel- und Szenenfelder zu Widget-Typen und Namen
EDITOR_CHAPTER_MAP = {
        "chapter_title": (QLineEdit, "lineEditorChapterTitleText"),
        "chapter_premise": (QLineEdit, "lineEditorChapterPremise"),
        "chapter_status": (QComboBox, "comboBoxEditorChapterStatus"),
        "chapter_begin": (QDateEdit, "dateEditorChapterBegin"),
        "chapter_edited": (QDateEdit, "dateEditorChapterEdited"),
        "chapter_excerpt": (QTextEdit, "textEditEditorChapterExcerpt"),
        "chapter_notes": (QTextEdit, "textEditEditorChapterNotes"),
    }
EDITOR_SCENE_MAP = {
            "scene_title": (QLineEdit, "lineEditorSceneTitle"),
            "scene_premise": (QLineEdit, "lineEditorScenePremise"),
            "scene_status": (QComboBox, "comboBoxEditorSceneStatus"),
            "scene_begin": (QDateEdit, "dateEditorSceneBegin"),
            "scene_edited": (QDateEdit, "dateEditorSceneEdited"),
            "scene_order": (QSpinBox, "spinBoxEditorSceneOrder"),
            "scene_goal": (QLineEdit, "lineEditorSceneGoal"),
            "scene_result ": (QLineEdit, "lineEditorSceneResult"),
            "scene_storyline": (QComboBox, "comboBoxEditorSceneStoryline"),
            "scene_location": (QComboBox, "comboBoxEditorSceneLocation"),
            "scene_mood": (QLineEdit, "lineEditorceneMood"),
            "scene_duration": (QLineEdit, "lineEditorSceneDuration"),
            "scene_type": (QLineEdit, "lineEditorSceneType"),
            "scene_tags": (QTextEdit, "textEditorSceneTags"),
            "scene_characters": (QListWidget, "listWidgetEditorSceneCharacters"),
            "scene_objects": (QListWidget, "listWidgetEditorSceneObjects"),
            "scene_notes": (QTextEdit, "textEditorSceneNotes"),
            "scene_plain_text": (QTextEdit, "textEditorScenePlainText"),
        }   
# Liest die Werte aus den Kapitel-Widgets aus
def read_editor_chapter_fields(window):
    chapter = {}
    for field, (widget_type, widget_name) in EDITOR_CHAPTER_MAP.items():
        widget = winFindChild(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                chapter[field] = widget.text()
            elif isinstance(widget, QTextEdit):
                chapter[field] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                chapter[field] = widget.currentIndex()
            elif isinstance(widget, QDateEdit):
                chapter[field] = widget.date().toString("yyyy-MM-dd")
    return chapter
# Erstelle eine leere Kapitel-Datenstruktur zurück
def get_empty_chapter():
    return {
        "chapter_id": "",
        "chapter_title": "",
        "chapter_premise": "",
        "chapter_status": 0,
        "chapter_begin": "",
        "chapter_edited": "",
        "chapter_excerpt": "",
        "chapter_notes": ""
        # Szenen werden später hinzugefügt
    }
# Update Kapitel Felder
def update_editor_chapter_fields(window, chapter):
    for field, (widget_type, widget_name) in EDITOR_CHAPTER_MAP.items():
        widget = winFindChild(window, widget_type, widget_name)
        value = chapter.get(field, "")
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)
# Aktualisiere die Kapitel-Liste im Editor
def update_chapter_list_widget(window):
    chapter_data = getattr(window, "chapter_data", {})
    list_chapters = winFindChild(window, QListWidget, "listWidgetEditorChapters")
    if list_chapters:
        list_chapters.clear()
        for chap_key, chap in chapter_data.items():
            chap_id = chap.get("chapter_id", chap_key)
            chap_title = chap.get("chapter_title", "")
            list_chapters.addItem(f"{chap_id} - {chap_title}")
# Nächste freie Szenen-ID in einem Kapitel ermitteln
def get_next_project_scene_id(chapter_data):
    max_id = 0
    for chapter in chapter_data.values():
        for k, v in chapter.items():
            if k.startswith("scenes_id_"):
                try:
                    num = int(v.get("scene_id", "0"))
                    max_id = max(max_id, num)
                except Exception:
                    pass
    return str(max_id + 1)
# Liest die Werte aus den Szenen-Widgets aus
def read_editor_scene_fields(window, scene=None):
    if scene is None:
        scene = {}
    for field, (widget_type, widget_name) in EDITOR_SCENE_MAP.items():
        widget = winFindChild(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                scene[field] = widget.text()
            elif isinstance(widget, QTextEdit):
                if field == "scene_plain_text":
                    scene[field] = widget.toHtml()
                else:
                    scene[field] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                scene[field] = widget.currentIndex()
            elif isinstance(widget, QSpinBox):
                scene[field] = widget.value()
            elif isinstance(widget, QDateEdit):
                scene[field] = widget.date().toString("yyyy-MM-dd")
    # Charakter-ListView auslesen
    listview_characters = winFindChild(window, QListWidget, "listWidgetEditorSceneCharacters")
    if listview_characters:
        scene["scene_characters"] = [listview_characters.item(i).text() for i in range(listview_characters.count())]
    # Objekt-ListView auslesen
    listview_objects = winFindChild(window, QListWidget, "listWidgetEditorSceneObjects")
    if listview_objects:
        scene["scene_objects"] = [listview_objects.item(i).text() for i in range(listview_objects.count())]
    return scene
# Setzt die Werte aus den Szenen-Widgets basierend auf einem Szenen-Dictionary
def update_editor_scene_fields(window, scene):
    # Listen für Charaktere und Objekte immer initialisieren
    if "scene_characters" not in scene or not isinstance(scene["scene_characters"], list):
        scene["scene_characters"] = []
    if "scene_objects" not in scene or not isinstance(scene["scene_objects"], list):
        scene["scene_objects"] = []

    for field, (widget_type, widget_name) in EDITOR_SCENE_MAP.items():
        widget = winFindChild(window, widget_type, widget_name)
        value = scene.get(field, "")
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                if field == "scene_plain_text":
                    widget.setHtml(str(value))
                else:
                    widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QSpinBox):
                try:
                    widget.setValue(int(value))
                except Exception:
                    widget.setValue(0)
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)
    # Charakter-ListView füllen
    listview_characters = winFindChild(window, QListWidget, "listWidgetEditorSceneCharacters")
    if listview_characters:
        listview_characters.clear()
        for name in scene.get("scene_characters", []):
            listview_characters.addItem(name)

    # Objekt-ListView füllen
    listview_objects = winFindChild(window, QListWidget, "listWidgetEditorSceneObjects")
    if listview_objects:
        listview_objects.clear()
        for name in scene.get("scene_objects", []):
            listview_objects.addItem(name)
# Zeige die erste Szene eines Kapitels im Editor an
def show_first_scene_of_chapter(window, chapter):
    scene_keys = [k for k in chapter.keys() if k.startswith("scenes_id_")]
    label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
    if scene_keys:
        first_scene = chapter[scene_keys[0]]
        update_editor_scene_fields(window, first_scene)
        if label_scene_id:
            label_scene_id.setText(first_scene.get("scene_id", ""))
    else:
        # Leere Szene anzeigen
        empty_scene = {"scene_id": ""}
        update_editor_scene_fields(window, empty_scene)
        if label_scene_id:
            label_scene_id.setText("")
# Szenenbestellungen in allen Kapiteln neu nummerieren
def renumber_scene_orders(chapter_data):
    # Alle Szenen aller Kapitel nach scene_order sortieren und neu nummerieren
    all_scenes = []
    for chapter in chapter_data.values():
        for k, v in chapter.items():
            if k.startswith("scenes_id_"):
                all_scenes.append((chapter, k, v))
    # Sortieren nach scene_order (Fallback: scene_id)
    all_scenes.sort(key=lambda tup: int(tup[2].get("scene_order", tup[2].get("scene_id", "0"))))
    # Neu nummerieren
    for idx, (chapter, k, v) in enumerate(all_scenes, 1):
        v["scene_order"] = idx
# Nächste freie Szenenbestellung in einem Kapitel ermitteln
def get_next_scene_order(chapter):
    orders = [int(v.get("scene_order", "0")) for k, v in chapter.items() if k.startswith("scenes_id_")]
    return max(orders, default=0) + 1
# Aktualisiere die Informationslabels im Editor
def update_editor_info_labels(window, chapter=None, scene=None):
    # Kapitel
    label_chapter = winFindChild(window, QLabel, "labelEditorChapterText")
    if label_chapter:
        chapter_title = ""
        if chapter:
            chapter_title = chapter.get("chapter_title", "")
        else:
            # Versuche aus dem Feld zu lesen, falls kein Kapitel-Dict übergeben
            chapter_title_widget = winFindChild(window, QLineEdit, "lineEditorChapterTitleText")
            if chapter_title_widget:
                chapter_title = chapter_title_widget.text()
        label_chapter.setText(chapter_title)

    # Szene
    label_scene = winFindChild(window, QLabel, "labelEditorSceneText")
    if label_scene:
        scene_title = ""
        if scene:
            scene_title = scene.get("scene_title", "")
        else:
            # Versuche aus dem Feld zu lesen, falls kein Szene-Dict übergeben
            scene_title_widget = winFindChild(window, QLineEdit, "lineEditorSceneTitle")
            if scene_title_widget:
                scene_title = scene_title_widget.text()
        label_scene.setText(scene_title)
# Verbinde die Textformatierungs-Buttons mit dem Text-Editor
def connect_text_formatting_buttons(window, text_edit_name="textEditorScenePlainText"):
    text_edit = winFindChild(window, QTextEdit, text_edit_name)
    if not text_edit:
        text_edit = winFindChild(window, QTextEdit, "textEditorScenePlainText")
        if not text_edit:
            return
    
    # Buttons zuerst definieren!
    btn_bold = winFindChild(window, QWidget, "btnEditorBold")
    btn_italic = winFindChild(window, QWidget, "btnEditorItalic")
    btn_underline = winFindChild(window, QWidget, "btnEditorUnderline")
    btn_sup = winFindChild(window, QWidget, "btnEditorSuperscript")
    btn_sub = winFindChild(window, QWidget, "btnEditorSubscript")
    btn_bullet = winFindChild(window, QWidget, "btnEditorBulletList")
    btn_number = winFindChild(window, QWidget, "btnEditorNumberList")

    # Icons für Buttons setzen
    indent_icon = QIcon("assets/editor_icons/indent_icon.png")
    list_bullet_icon = QIcon("assets/editor_icons/list_bullet_icon.png")
    list_number_icon = QIcon("assets/editor_icons/list_numbered_icon.png")
    subscript_icon = QIcon("assets/editor_icons/subscript_icon.png")
    superscript_icon = QIcon("assets/editor_icons/superscript_icon.png")

    def update_format_buttons():
        cursor = text_edit.textCursor()
        fmt = cursor.charFormat()
        btn_bold.setChecked(fmt.fontWeight() == QtGui.QFont.Bold)
        btn_italic.setChecked(fmt.fontItalic())
        btn_underline.setChecked(fmt.fontUnderline())
        btn_sup.setChecked(fmt.verticalAlignment() == QtGui.QTextCharFormat.AlignSuperScript)
        btn_sub.setChecked(fmt.verticalAlignment() == QtGui.QTextCharFormat.AlignSubScript)
        block = cursor.block()
        current_list = block.textList()
        btn_bullet.setChecked(bool(current_list and current_list.format().style() == QtGui.QTextListFormat.ListDisc))
        btn_number.setChecked(bool(current_list and current_list.format().style() == QtGui.QTextListFormat.ListDecimal))

    # Ausschneiden
    btn_cut = winFindChild(window, QWidget, "btnEditorCut")
    if btn_cut:
        btn_cut.clicked.connect(text_edit.cut)
    # Kopieren
    btn_copy = winFindChild(window, QWidget, "btnEditorCopy")
    if btn_copy:
        btn_copy.clicked.connect(text_edit.copy)
    # Einfügen
    btn_paste = winFindChild(window, QWidget, "btnEditorPaste")
    if btn_paste:
        btn_paste.clicked.connect(text_edit.paste)
    
    # Fett
    btn_bold = winFindChild(window, QWidget, "btnEditorBold")
    if btn_bold:
        def set_bold():
            fmt = text_edit.currentCharFormat()
            fmt.setFontWeight(QtGui.QFont.Bold if fmt.fontWeight() != QtGui.QFont.Bold else QtGui.QFont.Normal)
            text_edit.setCurrentCharFormat(fmt)
            update_format_buttons()
        btn_bold.clicked.connect(set_bold)

    # Kursiv
    btn_italic = winFindChild(window, QWidget, "btnEditorItalic")
    if btn_italic:
        def set_italic():
            fmt = text_edit.currentCharFormat()
            fmt.setFontItalic(not fmt.fontItalic())
            text_edit.setCurrentCharFormat(fmt)
            update_format_buttons()
        btn_italic.clicked.connect(set_italic)

    # Unterstrichen
    btn_underline = winFindChild(window, QWidget, "btnEditorUnderline")
    if btn_underline:
        def set_underline():
            fmt = text_edit.currentCharFormat()
            fmt.setFontUnderline(not fmt.fontUnderline())
            text_edit.setCurrentCharFormat(fmt)
            update_format_buttons()
        btn_underline.clicked.connect(set_underline)

    # Linksbündig
    btn_left = winFindChild(window, QWidget, "btnEditorLeft")
    if btn_left:
        btn_left.clicked.connect(lambda: text_edit.setAlignment(QtCore.Qt.AlignLeft))
        update_format_buttons

    # Zentriert
    btn_center = winFindChild(window, QWidget, "btnEditorCenter")
    if btn_center:
        btn_center.clicked.connect(lambda: text_edit.setAlignment(QtCore.Qt.AlignCenter))
        update_format_buttons

    # Rechtsbündig
    btn_right = winFindChild(window, QWidget, "btnEditorRight")
    if btn_right:
        btn_right.clicked.connect(lambda: text_edit.setAlignment(QtCore.Qt.AlignRight))
        update_format_buttons()

    # Einzug
    btn_indent = winFindChild(window, QWidget, "bntEditorIndentet")
    if btn_indent:
        btn_indent.setIcon(QIcon(indent_icon))
        def indent():
            cursor = text_edit.textCursor()
            cursor.insertText("    ")
            update_format_buttons()
        btn_indent.clicked.connect(indent)

    # Hochgestellt (Toggle)
    btn_sup = winFindChild(window, QWidget, "btnEditorSuperscript")
    if btn_sup:
        btn_sup.setIcon(QIcon(superscript_icon))
        def set_superscript():
            cursor = text_edit.textCursor()
            fmt = cursor.charFormat()
            if fmt.verticalAlignment() == QtGui.QTextCharFormat.AlignSuperScript:
                fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
            else:
                fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
            cursor.mergeCharFormat(fmt)
            update_format_buttons()
        btn_sup.clicked.connect(set_superscript)

    # Tiefgestellt (Toggle)
    btn_sub = winFindChild(window, QWidget, "btnEditorSubscript")
    if btn_sub:
        btn_sub.setIcon(QIcon(subscript_icon))
        def set_subscript():
            cursor = text_edit.textCursor()
            fmt = cursor.charFormat()
            if fmt.verticalAlignment() == QtGui.QTextCharFormat.AlignSubScript:
                fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
            else:
                fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
            cursor.mergeCharFormat(fmt)
            update_format_buttons()
        btn_sub.clicked.connect(set_subscript)

    # Bullet-List (Toggle)
    btn_bullet = winFindChild(window, QWidget, "btnEditorBulletList")
    if btn_bullet:
        btn_bullet.setIcon(QIcon(list_bullet_icon))
        def bullet_list():
            cursor = text_edit.textCursor()
            block = cursor.block()
            current_list = block.textList()
            cursor.beginEditBlock()
            if current_list and current_list.format().style() == QtGui.QTextListFormat.ListDisc:
                # Entferne Liste
                fmt = QtGui.QTextBlockFormat()
                cursor.setBlockFormat(fmt)
            else:
                cursor.createList(QtGui.QTextListFormat.ListDisc)
            cursor.endEditBlock()
            update_format_buttons()
        btn_bullet.clicked.connect(bullet_list)

    # Number-List (Toggle)
    btn_number = winFindChild(window, QWidget, "btnEditorNumberList")
    if btn_number:
        btn_number.setIcon(QIcon(list_number_icon))
        def number_list():
            cursor = text_edit.textCursor()
            block = cursor.block()
            current_list = block.textList()
            cursor.beginEditBlock()
            if current_list and current_list.format().style() == QtGui.QTextListFormat.ListDecimal:
                # Entferne Liste
                fmt = QtGui.QTextBlockFormat()
                cursor.setBlockFormat(fmt)
            else:
                cursor.createList(QtGui.QTextListFormat.ListDecimal)
            cursor.endEditBlock()
            update_format_buttons()
        btn_number.clicked.connect(number_list)

    # Schriftart
    font_combo = winFindChild(window, QFontComboBox, "fontComboBoxEditor")
    if font_combo:
        def set_font(font):
            fmt = text_edit.currentCharFormat()
            fmt.setFont(font)
            text_edit.setCurrentCharFormat(fmt)
        font_combo.currentFontChanged.connect(set_font)

    # Schriftgröße
    spin_font_size = winFindChild(window, QSpinBox, "spinBoxFontSizeEditor")
    if spin_font_size:
        def set_font_size(size):
            fmt = text_edit.currentCharFormat()
            fmt.setFontPointSize(size)
            text_edit.setCurrentCharFormat(fmt)
        spin_font_size.valueChanged.connect(set_font_size)

    # Undo/Redo
    btn_undo = winFindChild(window, QWidget, "bntEditorUndo")
    if btn_undo:
        btn_undo.clicked.connect(text_edit.undo)
    btn_redo = winFindChild(window, QWidget, "bntEditorRedo")
    if btn_redo:
        btn_redo.clicked.connect(text_edit.redo)



    text_edit.cursorPositionChanged.connect(update_format_buttons)
    text_edit.selectionChanged.connect(update_format_buttons)
# Gibt eine leere Szenen-Datenstruktur zurück
def get_empty_scene():
    scene = {}
    new_id = get_next_project_scene_id(app_state.current_project.get("chapter_data", {}))
    today = QDate.currentDate().toString("yyyy-MM-dd")
    # Alle Felder initialisieren
    for field, (widget_type, widget_name) in EDITOR_SCENE_MAP.items():
        if widget_type == QLineEdit or widget_type == QTextEdit:
            scene[field] = ""
        elif widget_type == QComboBox or widget_type == QSpinBox:
            scene[field] = 0
        elif widget_type == QDateEdit:
            scene[field] = QDate.currentDate().toString("yyyy-MM-dd")
        else:
            scene[field] = ""
    # Pflichtfelder überschreiben
    scene["scene_id"] = new_id
    scene["scene_title"] = ""
    scene["scene_premise"] = ""
    scene["scene_status"] = 0
    scene["scene_begin"] = today
    scene["scene_edited"] = today
    scene["scene_order"] = get_next_scene_order(scene)
    scene["scene_word_count"] = ""
    scene["scene_order":] = 1
    scene["scene_goal"] = ""
    scene["scene_result"] = ""
    scene["scene_storyline"] = 0
    scene["scene_location"] = 0
    scene["scene_characters"] = []
    scene["scene_objects"] = []
    scene["scene_mood"] = ""
    scene["scene_duration"] = ""
    scene["scene_type"] = ""
    scene["scene_tags"] = ""
    scene["scene_notes"] = ""
    scene["scene_plain_text"] = ""
    return scene
# Stelle sicher, dass alle Felder in der Szenen-Datenstruktur vorhanden sind
def ensure_all_scene_fields(scene):
    for field, (widget_type, widget_name) in EDITOR_SCENE_MAP.items():
        if field not in scene:
            if widget_type == QLineEdit or widget_type == QTextEdit:
                scene[field] = ""
            elif widget_type == QComboBox or widget_type == QSpinBox:
                scene[field] = 0
            elif widget_type == QDateEdit:
                scene[field] = QDate.currentDate().toString("yyyy-MM-dd")
            else:
                scene[field] = ""
    return scene
# Fügt ein Element zu einer Liste hinzu oder entfernt es, falls bereits vorhanden 
def toggle_item_in_list(item_list, idx):
    """Fügt idx hinzu oder entfernt ihn, falls schon enthalten."""
    if idx in item_list:
        item_list.remove(idx)
    else:
        item_list.append(idx)
    return item_list

# Hauptfenster anzeigen
def show_main_window():
    window = DynamicWindow("main_ui", UI_FILES["main"], splitter_name="mainSplitter", confirm_on_close=True)
    app_state.main_window = window 
    # Icon setzen
    icon_path = ASSETS_DIR / "media" / "csnova.png"
    window.setWindowIcon(QIcon(str(icon_path)))

    # # Cover-Bild setzen
    # cover_label = winFindChild(window,QLabel, "coverImage")
    # if cover_label:
    #     pixmap_path = ASSETS_DIR / "media" / "Buchcover_csNova.png"
    #     pixmap = QtGui.QPixmap(str(pixmap_path))
    #     cover_label.setPixmap(pixmap)
    #     cover_label.setScaledContents(True)

    # Exit-Button verbinden
    exit_btn = winFindChild(window,QWidget, "exitBtncsNovaMain")
    if exit_btn:
        def on_exit_clicked():
            try:
                confirmed = show_secure_dialog(window, action="exit")
            except Exception as e:
                log_exception("main exit handler: show_secure_dialog raised", e)
                confirmed = False
            if confirmed:
                window._closing = True
                QApplication.quit()
        exit_btn.clicked.connect(on_exit_clicked)
    # Projektfenster verbinden
    projects_btn = winFindChild(window,QWidget, "projectBtncsNovaMain")
    if projects_btn:
        def open_projects():
            window.hide()      
            show_projects_window(parent=window)      
        projects_btn.clicked.connect(open_projects)

    # Charakterfenster verbinden
    characters_btn = winFindChild(window,QWidget, "characterBtncsNovaMain")
    if characters_btn:
        def open_characters():
            window.hide()      
            show_characters_window(parent=window)
        characters_btn.clicked.connect(open_characters)

    # Objektfenster verbinden
    objects_btn = winFindChild(window,QWidget, "objectBtncsNovaMain")
    if objects_btn:
        def open_objects():
            window.hide()      
            show_objects_window(parent=window)
        objects_btn.clicked.connect(open_objects)

    # Locationsfenster verbinden
    locations_btn = winFindChild(window,QWidget, "locationBtncsNovaMain")
    if locations_btn:
        def open_locations():
            window.hide()      
            show_locations_window(parent=window)
        locations_btn.clicked.connect(open_locations)

    # Storylinefenster verbinden
    storylines_btn = winFindChild(window,QWidget, "storylineBtncsNovaMain")
    if storylines_btn:
        def open_storylines():
            window.hide()      
            show_storylines_window(parent=window)
        storylines_btn.clicked.connect(open_storylines)

    # Editorfenster verbinden
    editor_btn = winFindChild(window,QWidget, "editorBtncsNovaMain")
    if editor_btn:
        def open_editor():
            window.hide()      
            show_editor_window(parent=window)
        editor_btn.clicked.connect(open_editor)

    # Preferences-Button verbinden
    preferences_btn = winFindChild(window,QWidget, "preferencesBtncsNovaMain")
    if preferences_btn:
        def open_preferences():
            window.hide()      
            show_preferences_window(parent=window)
        preferences_btn.clicked.connect(open_preferences)

    # Referenz-Management-Button verbinden
    references_btn = winFindChild(window,QWidget, "referencesBtncsNovaMain")
    if references_btn:
        def open_references():
            show_references_window(parent=window)
        references_btn.clicked.connect(open_references)
    else:
        # Falls kein Button im UI existiert, erstelle einen für Debugging
        log_info("⚠ Referenzen-Button 'referencesBtncsNovaMain' nicht im UI gefunden")

    # Hilfe-Button verbinden
    help_btn = winFindChild(window,QWidget, "helpBtncsNovaMain")
    if help_btn:
        def open_help():
            window.hide()
            show_help_window(parent=window)
        help_btn.clicked.connect(open_help)

    # Statistik berechnen und anzeigen
    stats = {
        "labelCountProjectsStatistic": len(safe_load_json(Path("data/projects/data_projects.json"), {})),
        "labelCountCharactersStatistic": len(safe_load_json(Path("data/characters/data_characters.json"), {})),
        "labelCountObjectsStatistic": len(safe_load_json(Path("data/objects/data_objects.json"), {})),
        "labelCountLocationsStatistic": len(safe_load_json(Path("data/locations/data_locations.json"), {})),
        "labelCountStorylinesStatistic": len(safe_load_json(Path("data/storylines/data_storylines.json"), {})),
    }
    
    # Referenzen-Statistik hinzufügen
    if app_state.ref_manager:
        try:
            ref_count = len(app_state.ref_manager.get_all_references())
            stats["labelCountReferencesStatistic"] = ref_count
            log_info(f"✓ {ref_count} Referenzen in Statistik geladen")
        except Exception as e:
            log_error(f"Konnte Referenzen-Statistik nicht laden: {e}")
            stats["labelCountReferencesStatistic"] = 0
    
    for label_name, value in stats.items():
        label = winFindChild(window, QLabel, label_name)
        if label:
            label.setText(str(value))

     # Aktuelles Projekt anzeigen
    settings = load_settings()
    last_project_key = settings.get("last_project")
    project_title = ""
    if last_project_key:
        projects_data = safe_load_json(Path("data/projects/data_projects.json"), {})
        project = projects_data.get(last_project_key)
        if project:
            project_title = project.get("project_title", "")
    label_current_project = winFindChild(window, QLabel, "labelActuellProject")
    if label_current_project:
        label_current_project.setText(project_title if project_title else "Kein Projekt ausgewählt")


    log_info("Hauptfenster erfolgreich geladen und angezeigt.")
    window.show()
    return window

# Startfenster anzeigen
def show_start_window(settings):
    window = DynamicWindow("start_ui", UI_FILES["start"], splitter_name="mainSplitter")
    app_state.start_window = window 

    # Icon setzen
    icon_path = ASSETS_DIR / "media" / "csnova.png"
    window.setWindowIcon(QIcon(str(icon_path)))

    # # Cover-Bild setzen
    # cover_label = winFindChild(window,QLabel, "coverImage")
    # if cover_label:
    #     pixmap_path = ASSETS_DIR / "media" / "Buchcover_csNova.png"
    #     pixmap = QtGui.QPixmap(str(pixmap_path))
    #     cover_label.setPixmap(pixmap)
    #     cover_label.setScaledContents(True)

    # Sprache aus settings oder System bestimmen
    language = settings.get("language", get_system_language())

    # ComboBoxen finden
    combo_language = winFindChild(window,QComboBox, "comboBoxLanguage")
    combo_theme = winFindChild(window,QComboBox, "comboBoxTheme")

    # Items für Sprache laden (sicher, mit Cache)
    languages = safe_load_json(Path("core/translations/comboBox/languages.json"), {})
    language_codes = list(languages.keys())
    language_items = list(languages.get(language, languages.get("de", {})).values())
    if combo_language:
        combo_language.clear()
        combo_language.addItems(language_items)
        # Vorbelegen, falls vorhanden (index in language_codes suchen)
        if "language" in settings:
            try:
                idx = language_codes.index(settings["language"])
                combo_language.setCurrentIndex(idx)
            except ValueError:
                combo_language.setCurrentIndex(0)

    # Items für Theme laden
    designs = load_translation(Path("core/translations/comboBox/design.json"), language)
    theme_items = list(designs.values() if isinstance(designs, dict) else designs)
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
    save_btn = winFindChild(window,QWidget, "saveBtn")
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
    exit_btn = winFindChild(window,QWidget, "exitBnt")
    if exit_btn:
        def on_exit_clicked():
            if show_secure_dialog(window, action="exit"):
                # markiere und beende die App sauber
                window._closing = True
                QApplication.quit()
        exit_btn.clicked.connect(on_exit_clicked)

    log_info("Startfenster erfolgreich geladen und angezeigt.")
    window.show()
    return window

# Projektfenster anzeigen
def show_projects_window(parent=None):
    try:
        # 1. Manager abrufen
        project_manager = app_state.projects
        
        # 2. Window laden
        window = DynamicWindow("projects_ui", UI_FILES["projects"], splitter_name="mainSplitter")
        settings = load_settings()
        language = settings.get("language", "en")
        
        # 3. State in window speichern
        window.project_manager = project_manager
        window.current_project_id = None
        window.project_keys_list = []
        
        # 4. Translation-Caches laden (einmalig)
        window.target_groups = load_translation(Path("core/translations/comboBox/targetGroups.json"), language)
        window.perspectives = load_translation(Path("core/translations/comboBox/narrativePerspective.json"), language)
        window.styles = load_translation(Path("core/translations/comboBox/style.json"), language)
        genres_root = load_translation(Path("core/translations/comboBox/genre.json"), language)
        window.genres = genres_root.get("book_genres", {}) if isinstance(genres_root, dict) else {}
        working_root = load_translation(Path("core/translations/comboBox/workingType.json"), language)
        window.working_types = working_root.get("book_working_types", {}) if isinstance(working_root, dict) else {}
        window.motifs = load_translation(Path("core/translations/comboBox/motif.json"), language)
        window.status = load_translation(Path("core/translations/comboBox/status.json"), language)
        publishers_root = safe_load_json(Path("core/translations/comboBox/publisher.json"), {})
        publishers = publishers_root.get("publishers", []) if isinstance(publishers_root, dict) else []
        window.publisher_names = [pub.get("name", "") for pub in publishers if pub.get("type") == "book"]
        editors_root = safe_load_json(Path("core/translations/comboBox/editor.json"), {})
        editors = editors_root.get("editors", []) if isinstance(editors_root, dict) else []
        window.editor_names = [ed.get("name", "") for ed in editors if ed.get("type") == "book"]
        
        # 5. Helper-Funktionen
        def refresh_projects_table():
            """Lädt alle Projekte aus dem Manager"""
            try:
                all_projects = project_manager.get_all()
                window.project_keys_list = list(all_projects.keys())
                
                if window.project_keys_list:
                    if not window.current_project_id or window.current_project_id not in window.project_keys_list:
                        window.current_project_id = window.project_keys_list[0]
                    
                    current_project = project_manager.get(window.current_project_id)
                    update_project_fields(window, current_project)
                    refresh_comboboxes(window, current_project)
                else:
                    log_info("Keine Projekte vorhanden.")
            except Exception as e:
                log_error(f"Fehler beim Aktualisieren der Projekte: {e}")
        
        def refresh_comboboxes(window, project):
            """Aktualisiert alle ComboBoxes mit korrekten Werten"""
            try:
                combo_target = winFindChild(window, QComboBox, "comboBoxProjectTargetGroup")
                fill_combobox(combo_target, list(window.target_groups.values()), 
                            project.get("target_group", "Allgemein"))
                
                combo_narrative = winFindChild(window, QComboBox, "comboBoxProjectNarrativePerspective")
                fill_combobox(combo_narrative, list(window.perspectives.values()),
                            project.get("narrative_perspective", "Ich-Perspektive"))
                
                combo_style = winFindChild(window, QComboBox, "comboBoxProjectStyle")
                fill_combobox(combo_style, list(window.styles.values()),
                            project.get("style", "Modern"))
                
                combo_genre = winFindChild(window, QComboBox, "comboBoxProjectGenre")
                fill_combobox(combo_genre, list(window.genres.values()),
                            project.get("genre", "Roman"))
                
                combo_work = winFindChild(window, QComboBox, "comboBoxProjectWorkingType")
                fill_combobox(combo_work, list(window.working_types.values()),
                            project.get("working_type", "Belletristik"))
                
                combo_motif = winFindChild(window, QComboBox, "comboBoxProjectMotif")
                fill_combobox(combo_motif, list(window.motifs.values()),
                            project.get("motif", "Liebe"))
                
                combo_status = winFindChild(window, QComboBox, "comboBoxProjectStatus")
                fill_combobox(combo_status, list(window.status.values()),
                            project.get("status", "Planung"))
                
                combo_publisher = winFindChild(window, QComboBox, "comboBoxProjectPublisher")
                fill_combobox(combo_publisher, window.publisher_names,
                            project.get("publisher", ""))
                
                combo_editor = winFindChild(window, QComboBox, "comboBoxProjectEditor")
                fill_combobox(combo_editor, window.editor_names,
                            project.get("editor", ""))
            except Exception as e:
                log_error(f"Fehler beim Aktualisieren der ComboBoxes: {e}")
        
        def update_project_fields(window, project):
            """Füllt das Formular mit Projekt-Daten"""
            try:
                title_field = winFindChild(window, QLineEdit, "lineEditProjectTitle")
                if title_field:
                    title_field.setText(project.get("title", ""))
                
                subtitle_field = winFindChild(window, QLineEdit, "lineEditProjectSubtitle")
                if subtitle_field:
                    subtitle_field.setText(project.get("subtitle", ""))
                
                author_field = winFindChild(window, QLineEdit, "lineEditProjectAuthor")
                if author_field:
                    author_field.setText(project.get("author", ""))
                
                premise_field = winFindChild(window, QLineEdit, "lineEditProjectPremise")
                if premise_field:
                    premise_field.setText(project.get("premise", ""))
                
                begin_field = winFindChild(window, QDateEdit, "dateEditProjectBegin")
                if begin_field:
                    begin_str = project.get("begin_date", "")
                    begin_field.setDate(QDate.fromString(begin_str, "yyyy-MM-dd") if begin_str else QDate.currentDate())
                
                deadline_field = winFindChild(window, QDateEdit, "dateEditProjectDeadLine")
                if deadline_field:
                    deadline_str = project.get("deadline_date", "")
                    deadline_field.setDate(QDate.fromString(deadline_str, "yyyy-MM-dd") if deadline_str else QDate.currentDate())
                
                words_spin = winFindChild(window, QSpinBox, "spinBoxProjectWordsCount")
                if words_spin:
                    words_spin.setValue(project.get("words_goal", 0))
                
                cover_field = winFindChild(window, QLineEdit, "lineEditProjectCoverImage")
                if cover_field:
                    cover_field.setText(project.get("cover_image", ""))
                
                datafile_field = winFindChild(window, QLineEdit, "lineEditProjectDataFile")
                if datafile_field:
                    datafile_field.setText(project.get("data_file", ""))
                
                notes_field = winFindChild(window, QTextEdit, "textEditProjectNotes")
                if notes_field:
                    notes_field.setText(project.get("notes", ""))
            except Exception as e:
                log_error(f"Fehler beim Füllen der Felder: {e}")
        
        def read_project_fields(window):
            """Liest die Formular-Werte und gibt sie als Dict zurück"""
            try:
                return {
                    "title": winFindChild(window, QLineEdit, "lineEditProjectTitle").text() if winFindChild(window, QLineEdit, "lineEditProjectTitle") else "",
                    "subtitle": winFindChild(window, QLineEdit, "lineEditProjectSubtitle").text() if winFindChild(window, QLineEdit, "lineEditProjectSubtitle") else "",
                    "author": winFindChild(window, QLineEdit, "lineEditProjectAuthor").text() if winFindChild(window, QLineEdit, "lineEditProjectAuthor") else "",
                    "premise": winFindChild(window, QLineEdit, "lineEditProjectPremise").text() if winFindChild(window, QLineEdit, "lineEditProjectPremise") else "",
                    "target_group": winFindChild(window, QComboBox, "comboBoxProjectTargetGroup").currentText() if winFindChild(window, QComboBox, "comboBoxProjectTargetGroup") else "",
                    "narrative_perspective": winFindChild(window, QComboBox, "comboBoxProjectNarrativePerspective").currentText() if winFindChild(window, QComboBox, "comboBoxProjectNarrativePerspective") else "",
                    "style": winFindChild(window, QComboBox, "comboBoxProjectStyle").currentText() if winFindChild(window, QComboBox, "comboBoxProjectStyle") else "",
                    "genre": winFindChild(window, QComboBox, "comboBoxProjectGenre").currentText() if winFindChild(window, QComboBox, "comboBoxProjectGenre") else "",
                    "working_type": winFindChild(window, QComboBox, "comboBoxProjectWorkingType").currentText() if winFindChild(window, QComboBox, "comboBoxProjectWorkingType") else "",
                    "motif": winFindChild(window, QComboBox, "comboBoxProjectMotif").currentText() if winFindChild(window, QComboBox, "comboBoxProjectMotif") else "",
                    "begin_date": winFindChild(window, QDateEdit, "dateEditProjectBegin").date().toString("yyyy-MM-dd") if winFindChild(window, QDateEdit, "dateEditProjectBegin") else "",
                    "deadline_date": winFindChild(window, QDateEdit, "dateEditProjectDeadLine").date().toString("yyyy-MM-dd") if winFindChild(window, QDateEdit, "dateEditProjectDeadLine") else "",
                    "status": winFindChild(window, QComboBox, "comboBoxProjectStatus").currentText() if winFindChild(window, QComboBox, "comboBoxProjectStatus") else "Planung",
                    "words_goal": winFindChild(window, QSpinBox, "spinBoxProjectWordsCount").value() if winFindChild(window, QSpinBox, "spinBoxProjectWordsCount") else 0,
                    "cover_image": winFindChild(window, QLineEdit, "lineEditProjectCoverImage").text() if winFindChild(window, QLineEdit, "lineEditProjectCoverImage") else "",
                    "data_file": winFindChild(window, QLineEdit, "lineEditProjectDataFile").text() if winFindChild(window, QLineEdit, "lineEditProjectDataFile") else "",
                    "notes": winFindChild(window, QTextEdit, "textEditProjectNotes").toPlainText() if winFindChild(window, QTextEdit, "textEditProjectNotes") else "",
                    "publisher": winFindChild(window, QComboBox, "comboBoxProjectPublisher").currentText() if winFindChild(window, QComboBox, "comboBoxProjectPublisher") else "",
                    "editor": winFindChild(window, QComboBox, "comboBoxProjectEditor").currentText() if winFindChild(window, QComboBox, "comboBoxProjectEditor") else "",
                    "isbn": winFindChild(window, QLineEdit, "lineEditProjectISBN").text() if winFindChild(window, QLineEdit, "lineEditProjectISBN") else "",
                    "issn": winFindChild(window, QLineEdit, "lineEditProjectISSN").text() if winFindChild(window, QLineEdit, "lineEditProjectISSN") else ""
                }
            except Exception as e:
                log_error(f"Fehler beim Lesen der Felder: {e}")
                return {}
        
        # 6. Speichern-Button
        save_btn = winFindChild(window, QWidget, "saveBtnProjects")
        if save_btn:
            def on_save_clicked():
                try:
                    if not window.current_project_id:
                        QMessageBox.warning(window, "Warnung", "Kein Projekt ausgewählt.")
                        return
                    
                    updated_data = read_project_fields(window)
                    project_manager.data[window.current_project_id].update(updated_data)
                    
                    if project_manager.save():
                        log_info(f"Projekt '{updated_data.get('title', window.current_project_id)}' erfolgreich gespeichert.")
                        QMessageBox.information(window, "Erfolg", "Projekt gespeichert.")
                    else:
                        log_error("Fehler beim Speichern des Projekts.")
                        QMessageBox.critical(window, "Fehler", "Fehler beim Speichern.")
                        
                except Exception as e:
                    log_error(f"Fehler beim Speichern: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Speichern: {e}")
            
            save_btn.clicked.connect(on_save_clicked)
        
        # 7. Neues Projekt Button
        new_btn = winFindChild(window, QWidget, "newBtnProjects")
        if new_btn:
            def on_new_clicked():
                try:
                    new_data = {
                        "title": "Neues Projekt",
                        "subtitle": "",
                        "author": "",
                        "premise": "",
                        "target_group": "Allgemein",
                        "narrative_perspective": "Ich-Perspektive",
                        "style": "Modern",
                        "genre": "Roman",
                        "working_type": "Belletristik",
                        "motif": "Liebe",
                        "begin_date": QDate.currentDate().toString("yyyy-MM-dd"),
                        "deadline_date": QDate.currentDate().toString("yyyy-MM-dd"),
                        "status": "Planung",
                        "words_goal": 80000,
                        "cover_image": "",
                        "data_file": "",
                        "notes": "",
                        "publisher": "",
                        "editor": "",
                        "isbn": "",
                        "issn": ""
                    }
                    new_id = project_manager.add(new_data)
                    window.current_project_id = new_id
                    log_info(f"Neues Projekt '{new_id}' erstellt.")
                    refresh_projects_table()
                    QMessageBox.information(window, "Erfolg", f"Neues Projekt erstellt: {new_id}")
                    
                except Exception as e:
                    log_error(f"Fehler beim Erstellen eines neuen Projekts: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Erstellen: {e}")
            
            new_btn.clicked.connect(on_new_clicked)
        
        # 8. Nächstes Projekt Button
        next_btn = winFindChild(window, QWidget, "nextBtnProjects")
        if next_btn:
            def on_next_clicked():
                try:
                    if not window.project_keys_list:
                        return
                    current_index = window.project_keys_list.index(window.current_project_id)
                    next_index = (current_index + 1) % len(window.project_keys_list)
                    window.current_project_id = window.project_keys_list[next_index]
                    next_project = project_manager.get(window.current_project_id)
                    update_project_fields(window, next_project)
                    refresh_comboboxes(window, next_project)
                    
                except Exception as e:
                    log_error(f"Fehler beim Navigieren: {e}")
            
            next_btn.clicked.connect(on_next_clicked)
        
        # 9. Vorheriges Projekt Button
        prev_btn = winFindChild(window, QWidget, "previousBtnProjects")
        if prev_btn:
            def on_prev_clicked():
                try:
                    if not window.project_keys_list:
                        return
                    current_index = window.project_keys_list.index(window.current_project_id)
                    prev_index = (current_index - 1) % len(window.project_keys_list)
                    window.current_project_id = window.project_keys_list[prev_index]
                    prev_project = project_manager.get(window.current_project_id)
                    update_project_fields(window, prev_project)
                    refresh_comboboxes(window, prev_project)
                    
                except Exception as e:
                    log_error(f"Fehler beim Navigieren: {e}")
            
            prev_btn.clicked.connect(on_prev_clicked)
        
        # 10. Projekt löschen Button
        delete_btn = winFindChild(window, QWidget, "deleteBtnProjects")
        if delete_btn:
            def on_delete_clicked():
                try:
                    if not window.current_project_id:
                        QMessageBox.warning(window, "Warnung", "Kein Projekt ausgewählt.")
                        return
                    
                    project_data = project_manager.get(window.current_project_id)
                    project_title = project_data.get("title", window.current_project_id)
                    
                    reply = QMessageBox.question(
                        window,
                        "Bestätigung",
                        f"Projekt '{project_title}' wirklich löschen?",
                        QMessageBox.Yes | QMessageBox.No
                    )
                    
                    if reply == QMessageBox.Yes:
                        project_manager.delete(window.current_project_id)
                        log_info(f"Projekt '{project_title}' gelöscht.")
                        refresh_projects_table()
                        QMessageBox.information(window, "Erfolg", f"Projekt '{project_title}' gelöscht.")
                        
                except Exception as e:
                    log_error(f"Fehler beim Löschen: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Löschen: {e}")
            
            delete_btn.clicked.connect(on_delete_clicked)
        
        # 11. Bild laden Button
        image_btn = winFindChild(window, QWidget, "imageBtnProjects")
        if image_btn:
            def on_image_clicked():
                try:
                    file_dialog = QFileDialog()
                    image_path, _ = file_dialog.getOpenFileName(
                        window,
                        "Bild wählen",
                        "",
                        "Bilder (*.png *.jpg *.jpeg *.bmp *.gif)"
                    )
                    if image_path:
                        cover_field = winFindChild(window, QLineEdit, "lineEditProjectCoverImage")
                        if cover_field:
                            cover_field.setText(image_path)
                            log_info(f"Coverbild ausgewählt: {image_path}")
                except Exception as e:
                    log_error(f"Fehler beim Öffnen des Bilddialogs: {e}")
            
            image_btn.clicked.connect(on_image_clicked)
        
        # 12. Exit-Button
        exit_btn = winFindChild(window, QWidget, "exitBtnProjects")
        if exit_btn:
            def on_exit_clicked():
                window.close()
                if parent:
                    parent.show()
            
            exit_btn.clicked.connect(on_exit_clicked)
        
        # 13. Close Event Handler
        def on_close_event(event):
            settings = load_settings()
            if window.current_project_id:
                settings["last_project"] = window.current_project_id
            save_settings(settings)
            event.accept()
            if parent:
                parent.show()
        
        window.closeEvent = on_close_event
        
        # Initiale Befüllung
        refresh_projects_table()
        window.show()
        
        log_info("Projekt-Fenster erfolgreich mit Manager geladen.")
        return window
        
    except Exception as e:
        log_error(f"Fehler in show_projects_window: {e}")
        QMessageBox.critical(None, "Fehler", f"Fehler beim Öffnen des Projekt-Fensters: {e}")
        return None

# Charakterfenster anzeigen
def show_characters_window(parent=None):
    try:
        # 1. Manager abrufen
        character_manager = app_state.characters
        
        # 2. Window laden
        window = DynamicWindow("characters_ui", UI_FILES["characters"], splitter_name="mainSplitter")
        settings = load_settings()
        language = settings.get("language", "en")
        
        # 3. State in window speichern
        window.character_manager = character_manager
        window.current_character_id = None
        window.character_keys_list = []
        
        # 4. Translation-Caches laden
        window.status = load_translation(Path("core/translations/comboBox/status.json"), language)
        window.gender = load_translation(Path("core/translations/comboBox/gender.json"), language)
        window.sexual_orientation = load_translation(Path("core/translations/comboBox/sex_orientation.json"), language)
        window.role = load_translation(Path("core/translations/comboBox/role.json"), language)
        window.group = load_translation(Path("core/translations/comboBox/group.json"), language)
        window.body_type = load_translation(Path("core/translations/comboBox/bodyType.json"), language)
        window.stature = load_translation(Path("core/translations/comboBox/stature.json"), language)
        window.face_shape = load_translation(Path("core/translations/comboBox/faceShape.json"), language)
        window.eye_shape = load_translation(Path("core/translations/comboBox/eyeShape.json"), language)
        
        # 5. Helper-Funktionen
        def refresh_characters_table():
            """Lädt alle Charaktere aus dem Manager"""
            try:
                all_characters = character_manager.get_all()
                window.character_keys_list = list(all_characters.keys())
                
                if window.character_keys_list:
                    if not window.current_character_id or window.current_character_id not in window.character_keys_list:
                        window.current_character_id = window.character_keys_list[0]
                    
                    current_character = character_manager.get(window.current_character_id)
                    update_character_fields(window, current_character)
                    refresh_comboboxes(window, current_character)
                else:
                    log_info("Keine Charaktere vorhanden.")
            except Exception as e:
                log_error(f"Fehler beim Aktualisieren der Charaktere: {e}")
        
        def refresh_comboboxes(window, character):
            """Aktualisiert alle ComboBoxes mit korrekten Werten"""
            try:
                combo_status = winFindChild(window, QComboBox, "comboBoxStatus")
                fill_combobox(combo_status, list(window.status.values()),
                            character.get("status", "Planung"))
                
                combo_gender = winFindChild(window, QComboBox, "comboBoxGender")
                fill_combobox(combo_gender, list(window.gender.values()),
                            character.get("gender", "Weiblich"))
                
                combo_sexual = winFindChild(window, QComboBox, "comboBoxSexOrientation")
                fill_combobox(combo_sexual, list(window.sexual_orientation.values()),
                            character.get("sexual_orientation", "Heterosexuell"))
                
                combo_role = winFindChild(window, QComboBox, "comboBoxRole")
                fill_combobox(combo_role, list(window.role.values()),
                            character.get("role", "Hauptcharakter"))
                
                combo_group = winFindChild(window, QComboBox, "comboBoxGroup")
                fill_combobox(combo_group, list(window.group.values()),
                            character.get("group", "Besetzung"))
                
                combo_body = winFindChild(window, QComboBox, "comboBoxBodyType")
                fill_combobox(combo_body, list(window.body_type.values()),
                            character.get("body_type", "Normal"))
                
                combo_stature = winFindChild(window, QComboBox, "comboBoxStature")
                fill_combobox(combo_stature, list(window.stature.values()),
                            character.get("stature", "Mittel"))
                
                combo_face = winFindChild(window, QComboBox, "comboBoxFaceShape")
                fill_combobox(combo_face, list(window.face_shape.values()),
                            character.get("face_shape", "Oval"))
                
                combo_eye = winFindChild(window, QComboBox, "comboBoxEyeShape")
                fill_combobox(combo_eye, list(window.eye_shape.values()),
                            character.get("eye_shape", "Normal"))
            except Exception as e:
                log_error(f"Fehler beim Aktualisieren der ComboBoxes: {e}")
        
        def update_character_fields(window, character):
            """Füllt das Formular mit Charakter-Daten"""
            try:
                # Basis-Felder
                first_name = winFindChild(window, QLineEdit, "lineEditFirstName")
                if first_name:
                    first_name.setText(character.get("first_name", ""))
                
                name = winFindChild(window, QLineEdit, "lineEditName")
                if name:
                    name.setText(character.get("name", ""))
                
                nickname = winFindChild(window, QLineEdit, "lineEditNickName")
                if nickname:
                    nickname.setText(character.get("nickname", ""))
                
                # Datums-Felder
                born = winFindChild(window, QLineEdit, "lineEditBorn")
                if born:
                    born.setText(character.get("birth_date", ""))
                
                died = winFindChild(window, QLineEdit, "lineEditDied")
                if died:
                    died.setText(character.get("death_date", ""))
                
                # Herkunft
                mother = winFindChild(window, QLineEdit, "lineEditMother")
                if mother:
                    mother.setText(character.get("mother", ""))
                
                father = winFindChild(window, QLineEdit, "lineEditFather")
                if father:
                    father.setText(character.get("father", ""))
                
                ref_person = winFindChild(window, QLineEdit, "lineEditReferencePerson")
                if ref_person:
                    ref_person.setText(character.get("reference_person", ""))
                
                siblings = winFindChild(window, QTextEdit, "textEditSiblings")
                if siblings:
                    siblings.setText(character.get("siblings", ""))
                
                place_birth = winFindChild(window, QLineEdit, "lineEditPlaceOfBirth")
                if place_birth:
                    place_birth.setText(character.get("place_of_birth", ""))
                
                country = winFindChild(window, QLineEdit, "lineEditCountry")
                if country:
                    country.setText(character.get("country", ""))
                
                ethnicity = winFindChild(window, QLineEdit, "lineEditEthnicity")
                if ethnicity:
                    ethnicity.setText(character.get("ethnicity", ""))
                
                ancestry_notes = winFindChild(window, QTextEdit, "textEditAncestryNotes")
                if ancestry_notes:
                    ancestry_notes.setText(character.get("ancestry_notes", ""))
                
                # Aussehen
                pos_char = winFindChild(window, QLineEdit, "lineEditPosCharacteristics")
                if pos_char:
                    pos_char.setText(character.get("positive_characteristics", ""))
                
                neg_char = winFindChild(window, QLineEdit, "lineEditNegCharacteristics")
                if neg_char:
                    neg_char.setText(character.get("negative_characteristics", ""))
                
                # Persönlichkeit
                strengths = winFindChild(window, QLineEdit, "lineEditStrengthsOfCharacter")
                if strengths:
                    strengths.setText(character.get("strengths", ""))
                
                weakness = winFindChild(window, QLineEdit, "lineEditWeaknessOfCharacter")
                if weakness:
                    weakness.setText(character.get("weakness", ""))
                
                # Notizen
                notes = winFindChild(window, QTextEdit, "textEditCharacterNotes")
                if notes:
                    notes.setText(character.get("notes", ""))
                
                dev_notes = winFindChild(window, QTextEdit, "textEditDevelopmentNotes")
                if dev_notes:
                    dev_notes.setText(character.get("development_notes", ""))
                
            except Exception as e:
                log_error(f"Fehler beim Füllen der Felder: {e}")
        
        def read_character_fields(window):
            """Liest die Formular-Werte und gibt sie als Dict zurück"""
            try:
                return {
                    "first_name": winFindChild(window, QLineEdit, "lineEditFirstName").text() if winFindChild(window, QLineEdit, "lineEditFirstName") else "",
                    "name": winFindChild(window, QLineEdit, "lineEditName").text() if winFindChild(window, QLineEdit, "lineEditName") else "",
                    "nickname": winFindChild(window, QLineEdit, "lineEditNickName").text() if winFindChild(window, QLineEdit, "lineEditNickName") else "",
                    "birth_date": winFindChild(window, QLineEdit, "lineEditBorn").text() if winFindChild(window, QLineEdit, "lineEditBorn") else "",
                    "death_date": winFindChild(window, QLineEdit, "lineEditDied").text() if winFindChild(window, QLineEdit, "lineEditDied") else "",
                    "status": winFindChild(window, QComboBox, "comboBoxStatus").currentText() if winFindChild(window, QComboBox, "comboBoxStatus") else "Planung",
                    "gender": winFindChild(window, QComboBox, "comboBoxGender").currentText() if winFindChild(window, QComboBox, "comboBoxGender") else "Weiblich",
                    "sexual_orientation": winFindChild(window, QComboBox, "comboBoxSexOrientation").currentText() if winFindChild(window, QComboBox, "comboBoxSexOrientation") else "Heterosexuell",
                    "role": winFindChild(window, QComboBox, "comboBoxRole").currentText() if winFindChild(window, QComboBox, "comboBoxRole") else "Hauptcharakter",
                    "group": winFindChild(window, QComboBox, "comboBoxGroup").currentText() if winFindChild(window, QComboBox, "comboBoxGroup") else "Besetzung",
                    "body_type": winFindChild(window, QComboBox, "comboBoxBodyType").currentText() if winFindChild(window, QComboBox, "comboBoxBodyType") else "Normal",
                    "stature": winFindChild(window, QComboBox, "comboBoxStature").currentText() if winFindChild(window, QComboBox, "comboBoxStature") else "Mittel",
                    "face_shape": winFindChild(window, QComboBox, "comboBoxFaceShape").currentText() if winFindChild(window, QComboBox, "comboBoxFaceShape") else "Oval",
                    "eye_shape": winFindChild(window, QComboBox, "comboBoxEyeShape").currentText() if winFindChild(window, QComboBox, "comboBoxEyeShape") else "Normal",
                    "mother": winFindChild(window, QLineEdit, "lineEditMother").text() if winFindChild(window, QLineEdit, "lineEditMother") else "",
                    "father": winFindChild(window, QLineEdit, "lineEditFather").text() if winFindChild(window, QLineEdit, "lineEditFather") else "",
                    "reference_person": winFindChild(window, QLineEdit, "lineEditReferencePerson").text() if winFindChild(window, QLineEdit, "lineEditReferencePerson") else "",
                    "siblings": winFindChild(window, QTextEdit, "textEditSiblings").toPlainText() if winFindChild(window, QTextEdit, "textEditSiblings") else "",
                    "place_of_birth": winFindChild(window, QLineEdit, "lineEditPlaceOfBirth").text() if winFindChild(window, QLineEdit, "lineEditPlaceOfBirth") else "",
                    "country": winFindChild(window, QLineEdit, "lineEditCountry").text() if winFindChild(window, QLineEdit, "lineEditCountry") else "",
                    "ethnicity": winFindChild(window, QLineEdit, "lineEditEthnicity").text() if winFindChild(window, QLineEdit, "lineEditEthnicity") else "",
                    "ancestry_notes": winFindChild(window, QTextEdit, "textEditAncestryNotes").toPlainText() if winFindChild(window, QTextEdit, "textEditAncestryNotes") else "",
                    "positive_characteristics": winFindChild(window, QLineEdit, "lineEditPosCharacteristics").text() if winFindChild(window, QLineEdit, "lineEditPosCharacteristics") else "",
                    "negative_characteristics": winFindChild(window, QLineEdit, "lineEditNegCharacteristics").text() if winFindChild(window, QLineEdit, "lineEditNegCharacteristics") else "",
                    "strengths": winFindChild(window, QLineEdit, "lineEditStrengthsOfCharacter").text() if winFindChild(window, QLineEdit, "lineEditStrengthsOfCharacter") else "",
                    "weakness": winFindChild(window, QLineEdit, "lineEditWeaknessOfCharacter").text() if winFindChild(window, QLineEdit, "lineEditWeaknessOfCharacter") else "",
                    "notes": winFindChild(window, QTextEdit, "textEditCharacterNotes").toPlainText() if winFindChild(window, QTextEdit, "textEditCharacterNotes") else "",
                    "development_notes": winFindChild(window, QTextEdit, "textEditDevelopmentNotes").toPlainText() if winFindChild(window, QTextEdit, "textEditDevelopmentNotes") else ""
                }
            except Exception as e:
                log_error(f"Fehler beim Lesen der Felder: {e}")
                return {}
        
        # 6. Speichern-Button
        save_btn = winFindChild(window, QWidget, "saveBtnCharacter")
        if save_btn:
            def on_save_clicked():
                try:
                    if not window.current_character_id:
                        QMessageBox.warning(window, "Warnung", "Kein Charakter ausgewählt.")
                        return
                    
                    updated_data = read_character_fields(window)
                    character_manager.data[window.current_character_id].update(updated_data)
                    
                    if character_manager.save():
                        char_name = updated_data.get("name", window.current_character_id)
                        log_info(f"Charakter '{char_name}' erfolgreich gespeichert.")
                        QMessageBox.information(window, "Erfolg", "Charakter gespeichert.")
                    else:
                        log_error("Fehler beim Speichern des Charakters.")
                        QMessageBox.critical(window, "Fehler", "Fehler beim Speichern.")
                        
                except Exception as e:
                    log_error(f"Fehler beim Speichern: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Speichern: {e}")
            
            save_btn.clicked.connect(on_save_clicked)
        
        # 7. Neuer Charakter Button
        new_btn = winFindChild(window, QWidget, "newBtnCharacter")
        if new_btn:
            def on_new_clicked():
                try:
                    new_data = {
                        "first_name": "Vorname",
                        "name": "Nachname",
                        "nickname": "",
                        "birth_date": "",
                        "death_date": "",
                        "status": "Planung",
                        "gender": "Weiblich",
                        "sexual_orientation": "Heterosexuell",
                        "role": "Hauptcharakter",
                        "group": "Besetzung",
                        "body_type": "Normal",
                        "stature": "Mittel",
                        "face_shape": "Oval",
                        "eye_shape": "Normal",
                        "mother": "",
                        "father": "",
                        "reference_person": "",
                        "siblings": "",
                        "place_of_birth": "",
                        "country": "",
                        "ethnicity": "",
                        "ancestry_notes": "",
                        "positive_characteristics": "",
                        "negative_characteristics": "",
                        "strengths": "",
                        "weakness": "",
                        "notes": "",
                        "development_notes": ""
                    }
                    new_id = character_manager.add(new_data)
                    window.current_character_id = new_id
                    log_info(f"Neuer Charakter '{new_id}' erstellt.")
                    refresh_characters_table()
                    QMessageBox.information(window, "Erfolg", f"Neuer Charakter erstellt: {new_id}")
                    
                except Exception as e:
                    log_error(f"Fehler beim Erstellen eines neuen Charakters: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Erstellen: {e}")
            
            new_btn.clicked.connect(on_new_clicked)
        
        # 8. Nächster Charakter Button
        next_btn = winFindChild(window, QWidget, "nextBtnCharacter")
        if next_btn:
            def on_next_clicked():
                try:
                    if not window.character_keys_list:
                        return
                    current_index = window.character_keys_list.index(window.current_character_id)
                    next_index = (current_index + 1) % len(window.character_keys_list)
                    window.current_character_id = window.character_keys_list[next_index]
                    next_character = character_manager.get(window.current_character_id)
                    update_character_fields(window, next_character)
                    refresh_comboboxes(window, next_character)
                    
                except Exception as e:
                    log_error(f"Fehler beim Navigieren: {e}")
            
            next_btn.clicked.connect(on_next_clicked)
        
        # 9. Vorheriger Charakter Button
        prev_btn = winFindChild(window, QWidget, "previousBtnCharacter")
        if prev_btn:
            def on_prev_clicked():
                try:
                    if not window.character_keys_list:
                        return
                    current_index = window.character_keys_list.index(window.current_character_id)
                    prev_index = (current_index - 1) % len(window.character_keys_list)
                    window.current_character_id = window.character_keys_list[prev_index]
                    prev_character = character_manager.get(window.current_character_id)
                    update_character_fields(window, prev_character)
                    refresh_comboboxes(window, prev_character)
                    
                except Exception as e:
                    log_error(f"Fehler beim Navigieren: {e}")
            
            prev_btn.clicked.connect(on_prev_clicked)
        
        # 10. Charakter löschen Button
        delete_btn = winFindChild(window, QWidget, "deleteBtnCharacter")
        if delete_btn:
            def on_delete_clicked():
                try:
                    if not window.current_character_id:
                        QMessageBox.warning(window, "Warnung", "Kein Charakter ausgewählt.")
                        return
                    
                    character_data = character_manager.get(window.current_character_id)
                    character_name = character_data.get("name", window.current_character_id)
                    
                    reply = QMessageBox.question(
                        window,
                        "Bestätigung",
                        f"Charakter '{character_name}' wirklich löschen?",
                        QMessageBox.Yes | QMessageBox.No
                    )
                    
                    if reply == QMessageBox.Yes:
                        character_manager.delete(window.current_character_id)
                        log_info(f"Charakter '{character_name}' gelöscht.")
                        refresh_characters_table()
                        QMessageBox.information(window, "Erfolg", f"Charakter '{character_name}' gelöscht.")
                        
                except Exception as e:
                    log_error(f"Fehler beim Löschen: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Löschen: {e}")
            
            delete_btn.clicked.connect(on_delete_clicked)
        
        # 11. Bild laden Button
        image_btn = winFindChild(window, QWidget, "imageBtnCharacter")
        if image_btn:
            def on_image_clicked():
                try:
                    file_dialog = QFileDialog()
                    image_path, _ = file_dialog.getOpenFileName(
                        window,
                        "Bild wählen",
                        "",
                        "Bilder (*.png *.jpg *.jpeg *.bmp *.gif)"
                    )
                    if image_path:
                        log_info(f"Charakterbild ausgewählt: {image_path}")
                except Exception as e:
                    log_error(f"Fehler beim Öffnen des Bilddialogs: {e}")
            
            image_btn.clicked.connect(on_image_clicked)
        
        # 12. Exit-Button
        exit_btn = winFindChild(window, QWidget, "exitBtnCharacter")
        if exit_btn:
            def on_exit_clicked():
                window.close()
                if parent:
                    parent.show()
            
            exit_btn.clicked.connect(on_exit_clicked)
        
        # 13. Close Event Handler
        def on_close_event(event):
            settings = load_settings()
            save_settings(settings)
            event.accept()
            if parent:
                parent.show()
        
        window.closeEvent = on_close_event
        
        # Initiale Befüllung
        refresh_characters_table()
        window.show()
        
        log_info("Charakter-Fenster erfolgreich mit Manager geladen.")
        return window
        
    except Exception as e:
        log_error(f"Fehler in show_characters_window: {e}")
        QMessageBox.critical(None, "Fehler", f"Fehler beim Öffnen des Charakter-Fensters: {e}")
        return None

# Objektfenster anzeigen
def show_objects_window(parent=None):
    window = DynamicWindow("objects_ui", UI_FILES["objects"], splitter_name="mainSplitter")
    settings = load_settings()
    language = settings.get("language", "en")
    window.show()

    # 2. Daten laden
    object_path = Path("data/objects/data_objects.json")
    object_data = safe_load_json(object_path, {})
    if not object_data:
        empty_object = get_empty_object()
        empty_object["object_ID"] = "1"
        object_data = {"object_ID_01": empty_object}
        safe_save_json(object_path, object_data)
    first_key = next(iter(object_data.keys()))
    window.current_object_key = first_key
    current_object = object_data[window.current_object_key]

    # Felder setzen
    update_object_fields(window, current_object)

    # Status-ComboBox füllen
    status = load_translation(Path("core/translations/comboBox/status.json"), language)
    combo_status = winFindChild(window, QComboBox, "comboBoxObjectsStatus")
    fill_combobox(combo_status, list(status.values()), current_object.get("object_status", 0))

    # --- Save-Button einbinden ---
    save_btn = winFindChild(window,QWidget, "saveBtnObjects")
    if save_btn:
        def on_save_clicked():
            object_data = safe_load_json(object_path, {})
            object_key = window.current_object_key
            obj = object_data.get(object_key, {})
            obj.update(read_object_fields(window))
            object_data[object_key] = obj
            safe_save_json(object_path, object_data)
            log_info(f"Objekt {object_key} erfolgreich gespeichert.")

        save_btn.clicked.connect(on_save_clicked)
    # --- Neuen Objekt Button einbinden ---
    new_btn = winFindChild(window,QWidget, "newBtnObjects")
    if new_btn:
        def on_new_clicked():
            object_data = safe_load_json(object_path, {})
            new_key, new_id = get_next_id(object_data, "object_ID_")
            empty_object = get_empty_object()
            empty_object["object_ID"] = new_id
            # Setze Erstellungs-/Bearbeitungsdatum
            today = QDate.currentDate().toString("yyyy-MM-dd")
            empty_object["object_created"] = today
            empty_object["object_modified"] = today
            object_data[new_key] = empty_object
            safe_save_json(object_path, object_data)
            log_info(f"Neues Objekt {new_key} erstellt.")
            window.current_object_key = new_key
            update_object_fields(window, empty_object)
        new_btn.clicked.connect(on_new_clicked)
    # --- nächster Objekt Button einbinden ---
    def on_next_clicked():
        object_data = safe_load_json(object_path, {})
        keys = list(object_data.keys())
        current_index = keys.index(window.current_object_key)
        next_index = (current_index + 1) % len(keys)
        next_key = keys[next_index]
        window.current_object_key = next_key
        next_object = object_data[next_key]
        update_object_fields(window, next_object)
    next_btn = winFindChild(window,QWidget, "nextBtnObjects")
    if next_btn:
        next_btn.clicked.connect(on_next_clicked)
    # --- vorheriger Objekt Button einbinden ---
    def on_prev_clicked():
        object_data = safe_load_json(object_path, {})
        keys = list(object_data.keys())
        current_index = keys.index(window.current_object_key)
        prev_index = (current_index - 1) % len(keys)
        prev_key = keys[prev_index]
        window.current_object_key = prev_key
        prev_object = object_data[prev_key]
        update_object_fields(window, prev_object)
    prev_btn = winFindChild(window,QWidget, "previousBtnObjects")
    if prev_btn:
        prev_btn.clicked.connect(on_prev_clicked)
    # --- Daten löschen Button einbinden ---
    def on_delete_clicked():
        object_data = safe_load_json(object_path, {})
        object_key = window.current_object_key
        object_name = object_data[object_key].get("object_title", object_key)
        def delete_object():
            nonlocal object_data, object_key, object_name
            if object_key in object_data:
                del object_data[object_key]
                safe_save_json(object_path, object_data)
                # log_info(f"Objekt {object_name} gelöscht.")
                # Nach dem Löschen: neuen Key setzen und Felder aktualisieren
                keys = list(object_data.keys())
                if keys:
                    idx = 0
                    if object_key in keys:
                        idx = keys.index(object_key)
                    elif window.current_object_key and window.current_object_key in keys:
                        idx = keys.index(window.current_object_key)
                    if idx >= len(keys):
                        idx = len(keys) - 1
                    window.current_object_key = keys[idx]
                    update_object_fields(window, object_data[window.current_object_key])
                else:
                    empty_object = get_empty_object()
                    update_object_fields(window, empty_object)
                    window.current_object_key = None
        if show_secure_dialog(window, action="delete_object", project_key=object_name):
            delete_object()
    delete_btn = winFindChild(window,QWidget, "deleteBtnObjects")
    if delete_btn:
        delete_btn.clicked.connect(on_delete_clicked)
    
    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnObjects")
    if exit_btn:
        def on_exit_clicked():
            window.close()
            if parent:
                parent.show()
        exit_btn.clicked.connect(on_exit_clicked)

    def on_close_event(event):
        settings = load_settings()
        save_settings(settings)
        event.accept()
        if parent:
            parent.show()
    window.closeEvent = on_close_event

    log_info("Objektfenster erfolgreich geladen und angezeigt.")
    return window

# Locationsfenster anzeigen
def show_locations_window(parent=None):
    """
    Fenster für Handlungsorte/Schauplätze mit Manager-Integration.
    Nutzt LocationManager statt direkter JSON-Operationen.
    """
    try:
        from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem
        from PySide6.QtCore import Qt
        from core.logger import log_info, log_error
        
        # Manager abrufen
        loc_manager = app_state.locations
        
        # Fenster laden
        window = DynamicWindow("locations_ui", UI_FILES["locations"], splitter_name="mainSplitter")
        settings = load_settings()
        language = settings.get("language", "en")
        window.show()
        
        # Speichere Manager und Parent für spätere Referenzen
        window.loc_manager = loc_manager
        window.current_location_id = None
        window.location_keys_list = []
        
        # Status-ComboBox füllen
        status = load_translation(Path("core/translations/comboBox/status.json"), language)
        combo_status = winFindChild(window, QComboBox, "comboBoxLocationsStatus")
        if combo_status:
            fill_combobox(combo_status, list(status.values()), 0)
        
        def refresh_locations_table():
            """Aktualisiert die Anzeige mit Daten aus dem Manager."""
            try:
                all_locations = loc_manager.get_all()
                window.location_keys_list = list(all_locations.keys())
                
                if not window.location_keys_list:
                    log_info("Keine Handlungsorte vorhanden.")
                    window.current_location_id = None
                    # Felder leeren
                    title_field = winFindChild(window, QLineEdit, "titleLocations")
                    if title_field:
                        title_field.clear()
                    desc_field = winFindChild(window, QTextEdit, "textDescriptionLocations")
                    if desc_field:
                        desc_field.clear()
                    return
                
                # Ersten Ort anzeigen oder aktuellen behalten
                if window.current_location_id is None or window.current_location_id not in window.location_keys_list:
                    window.current_location_id = window.location_keys_list[0]
                
                # Aktuelle Location laden und anzeigen
                current_location = loc_manager.get(window.current_location_id)
                if current_location:
                    update_location_fields(window, current_location)
                    
            except Exception as e:
                log_error(f"Fehler beim Aktualisieren der Tabelle: {e}")
                QMessageBox.critical(window, "Fehler", f"Fehler beim Laden der Daten: {e}")
        
        def update_location_fields(win, location_data):
            """Füllt die Formularfelder mit Ortsdaten."""
            try:
                title_field = winFindChild(win, QLineEdit, "titleLocations")
                if title_field:
                    title_field.setText(location_data.get("title", ""))
                
                desc_field = winFindChild(win, QTextEdit, "textDescriptionLocations")
                if desc_field:
                    desc_field.setPlainText(location_data.get("description", ""))
                
                created_date = winFindChild(win, QDateEdit, "dateEditCreatedLocations")
                if created_date and location_data.get("created_date"):
                    created_date.setDate(QDate.fromString(location_data["created_date"], "yyyy-MM-dd"))
                
                edited_date = winFindChild(win, QDateEdit, "dateEditEditedLocations")
                if edited_date and location_data.get("edited_date"):
                    edited_date.setDate(QDate.fromString(location_data["edited_date"], "yyyy-MM-dd"))
                
                status_combo = winFindChild(win, QComboBox, "comboBoxLocationsStatus")
                if status_combo:
                    status_text = location_data.get("status", "Planung")
                    index = status_combo.findText(status_text)
                    if index >= 0:
                        status_combo.setCurrentIndex(index)
                        
            except Exception as e:
                log_error(f"Fehler beim Füllen der Felder: {e}")
        
        def read_location_fields(win):
            """Liest die Formularfelder und gibt ein Dictionary zurück."""
            try:
                title_field = winFindChild(win, QLineEdit, "titleLocations")
                title = title_field.text() if title_field else ""
                
                desc_field = winFindChild(win, QTextEdit, "textDescriptionLocations")
                desc = desc_field.toPlainText() if desc_field else ""
                
                created_date = winFindChild(win, QDateEdit, "dateEditCreatedLocations")
                created = created_date.date().toString("yyyy-MM-dd") if created_date else ""
                
                edited_date = winFindChild(win, QDateEdit, "dateEditEditedLocations")
                edited = edited_date.date().toString("yyyy-MM-dd") if edited_date else ""
                
                status_combo = winFindChild(win, QComboBox, "comboBoxLocationsStatus")
                status = status_combo.currentText() if status_combo else "Planung"
                
                return {
                    "title": title,
                    "description": desc,
                    "created_date": created,
                    "edited_date": edited,
                    "status": status
                }
            except Exception as e:
                log_error(f"Fehler beim Lesen der Felder: {e}")
                return {}
        
        # --- Save-Button einbinden ---
        save_btn = winFindChild(window, QWidget, "saveBtnLocations")
        if save_btn:
            def on_save_clicked():
                try:
                    if not window.current_location_id:
                        QMessageBox.warning(window, "Warnung", "Kein Ort ausgewählt.")
                        return
                    
                    location_data = read_location_fields(window)
                    loc_manager.data[window.current_location_id].update(location_data)
                    loc_manager.save()
                    log_info(f"Ort '{location_data.get('title', window.current_location_id)}' erfolgreich gespeichert.")
                    QMessageBox.information(window, "Erfolg", "Ort erfolgreich gespeichert.")
                    
                except Exception as e:
                    log_error(f"Fehler beim Speichern: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Speichern: {e}")
            
            save_btn.clicked.connect(on_save_clicked)
        
        # --- Neuen Ort Button einbinden ---
        new_btn = winFindChild(window, QWidget, "newBtnLocations")
        if new_btn:
            def on_new_clicked():
                try:
                    new_data = {
                        "title": "Neuer Ort",
                        "description": "",
                        "status": "Planung",
                        "created_date": QDate.currentDate().toString("yyyy-MM-dd"),
                        "edited_date": QDate.currentDate().toString("yyyy-MM-dd")
                    }
                    new_id = loc_manager.add(new_data)
                    window.current_location_id = new_id
                    log_info(f"Neuer Ort '{new_id}' erstellt.")
                    refresh_locations_table()
                    QMessageBox.information(window, "Erfolg", f"Neuer Ort erstellt: {new_id}")
                    
                except Exception as e:
                    log_error(f"Fehler beim Erstellen eines neuen Ortes: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Erstellen: {e}")
            
            new_btn.clicked.connect(on_new_clicked)
        
        # --- Nächster Ort Button einbinden ---
        next_btn = winFindChild(window, QWidget, "nextBtnLocations")
        if next_btn:
            def on_next_clicked():
                try:
                    if not window.location_keys_list:
                        return
                    current_index = window.location_keys_list.index(window.current_location_id)
                    next_index = (current_index + 1) % len(window.location_keys_list)
                    window.current_location_id = window.location_keys_list[next_index]
                    next_location = loc_manager.get(window.current_location_id)
                    update_location_fields(window, next_location)
                    
                except Exception as e:
                    log_error(f"Fehler beim Navigieren: {e}")
            
            next_btn.clicked.connect(on_next_clicked)
        
        # --- Vorheriger Ort Button einbinden ---
        prev_btn = winFindChild(window, QWidget, "previousBtnLocations")
        if prev_btn:
            def on_prev_clicked():
                try:
                    if not window.location_keys_list:
                        return
                    current_index = window.location_keys_list.index(window.current_location_id)
                    prev_index = (current_index - 1) % len(window.location_keys_list)
                    window.current_location_id = window.location_keys_list[prev_index]
                    prev_location = loc_manager.get(window.current_location_id)
                    update_location_fields(window, prev_location)
                    
                except Exception as e:
                    log_error(f"Fehler beim Navigieren: {e}")
            
            prev_btn.clicked.connect(on_prev_clicked)
        
        # --- Ort löschen Button einbinden ---
        delete_btn = winFindChild(window, QWidget, "deleteBtnLocations")
        if delete_btn:
            def on_delete_clicked():
                try:
                    if not window.current_location_id:
                        QMessageBox.warning(window, "Warnung", "Kein Ort ausgewählt.")
                        return
                    
                    location_data = loc_manager.get(window.current_location_id)
                    location_title = location_data.get("title", window.current_location_id)
                    
                    reply = QMessageBox.question(
                        window,
                        "Bestätigung",
                        f"Ort '{location_title}' wirklich löschen?",
                        QMessageBox.Yes | QMessageBox.No
                    )
                    
                    if reply == QMessageBox.Yes:
                        loc_manager.delete(window.current_location_id)
                        log_info(f"Ort '{location_title}' gelöscht.")
                        refresh_locations_table()
                        QMessageBox.information(window, "Erfolg", f"Ort '{location_title}' gelöscht.")
                        
                except Exception as e:
                    log_error(f"Fehler beim Löschen: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Löschen: {e}")
            
            delete_btn.clicked.connect(on_delete_clicked)
        
        # --- Exit-Button einbinden ---
        exit_btn = winFindChild(window, QWidget, "exitBtnLocations")
        if exit_btn:
            def on_exit_clicked():
                window.close()
                if parent:
                    parent.show()
            
            exit_btn.clicked.connect(on_exit_clicked)
        
        # --- Close Event Handler ---
        def on_close_event(event):
            settings = load_settings()
            save_settings(settings)
            event.accept()
            if parent:
                parent.show()
        
        window.closeEvent = on_close_event
        
        # Initiale Befüllung
        refresh_locations_table()
        
        log_info("Handlungsorte-Fenster erfolgreich mit Manager geladen.")
        return window
        
    except Exception as e:
        log_error(f"Fehler in show_locations_window: {e}")
        QMessageBox.critical(None, "Fehler", f"Fehler beim Öffnen des Handlungsorte-Fensters: {e}")
        return None

# Storylinefenster anzeigen
def show_storylines_window(parent=None):
    try:
        # 1. Manager abrufen
        storyline_manager = app_state.storylines
        
        # 2. Window laden
        window = DynamicWindow("storylines_ui", UI_FILES["storylines"], splitter_name="mainSplitter")
        
        # 3. State in window speichern
        window.storyline_manager = storyline_manager
        window.current_storyline_id = None
        window.storyline_keys_list = []
        
        # 4. Helper-Funktionen
        def refresh_storylines_table():
            """Lädt alle Handlungsstränge aus dem Manager"""
            try:
                all_storylines = storyline_manager.get_all()
                window.storyline_keys_list = list(all_storylines.keys())
                
                if window.storyline_keys_list:
                    if not window.current_storyline_id or window.current_storyline_id not in window.storyline_keys_list:
                        window.current_storyline_id = window.storyline_keys_list[0]
                    
                    current_storyline = storyline_manager.get(window.current_storyline_id)
                    update_storyline_fields(window, current_storyline)
                    
                    # Status-ComboBox füllen
                    settings = load_settings()
                    language = settings.get("language", "en")
                    status = load_translation(Path("core/translations/comboBox/status.json"), language)
                    combo_status = winFindChild(window, QComboBox, "comboBoxStorylinesStatus")
                    
                    status_value = current_storyline.get("status", "Planung")
                    status_index = list(status.values()).index(status_value) if status_value in status.values() else 0
                    fill_combobox(combo_status, list(status.values()), status_index)
                else:
                    log_info("Keine Handlungsstränge vorhanden.")
            except Exception as e:
                log_error(f"Fehler beim Aktualisieren der Handlungsstränge: {e}")
        
        def update_storyline_fields(window, storyline):
            """Füllt das Formular mit Handlungsstrang-Daten"""
            try:
                title_field = winFindChild(window, QLineEdit, "titleStorylines")
                desc_field = winFindChild(window, QTextEdit, "textDescriptionStorylines")
                created_field = winFindChild(window, QDateEdit, "dateEditCreatedStorylines")
                edited_field = winFindChild(window, QDateEdit, "dateEditEditedStorylines")
                status_combo = winFindChild(window, QComboBox, "comboBoxStorylinesStatus")
                
                if title_field:
                    title_field.setText(storyline.get("title", ""))
                if desc_field:
                    desc_field.setText(storyline.get("description", ""))
                if created_field:
                    created_str = storyline.get("created_date", "")
                    created_field.setDate(QDate.fromString(created_str, "yyyy-MM-dd") if created_str else QDate.currentDate())
                if edited_field:
                    edited_str = storyline.get("edited_date", "")
                    edited_field.setDate(QDate.fromString(edited_str, "yyyy-MM-dd") if edited_str else QDate.currentDate())
                if status_combo:
                    status_combo.setCurrentText(storyline.get("status", "Planung"))
            except Exception as e:
                log_error(f"Fehler beim Füllen der Felder: {e}")
        
        def read_storyline_fields(window):
            """Liest die Formular-Werte und gibt sie als Dict zurück"""
            try:
                title_field = winFindChild(window, QLineEdit, "titleStorylines")
                desc_field = winFindChild(window, QTextEdit, "textDescriptionStorylines")
                created_field = winFindChild(window, QDateEdit, "dateEditCreatedStorylines")
                edited_field = winFindChild(window, QDateEdit, "dateEditEditedStorylines")
                status_combo = winFindChild(window, QComboBox, "comboBoxStorylinesStatus")
                
                return {
                    "title": title_field.text() if title_field else "",
                    "description": desc_field.toPlainText() if desc_field else "",
                    "created_date": created_field.date().toString("yyyy-MM-dd") if created_field else "",
                    "edited_date": edited_field.date().toString("yyyy-MM-dd") if edited_field else "",
                    "status": status_combo.currentText() if status_combo else "Planung"
                }
            except Exception as e:
                log_error(f"Fehler beim Lesen der Felder: {e}")
                return {}
        
        # 5. Speichern-Button
        save_btn = winFindChild(window, QWidget, "saveBtnStorylines")
        if save_btn:
            def on_save_clicked():
                try:
                    if not window.current_storyline_id:
                        QMessageBox.warning(window, "Warnung", "Kein Handlungsstrang ausgewählt.")
                        return
                    
                    updated_data = read_storyline_fields(window)
                    storyline_manager.data[window.current_storyline_id].update(updated_data)
                    
                    if storyline_manager.save():
                        log_info(f"Handlungsstrang '{updated_data.get('title', window.current_storyline_id)}' erfolgreich gespeichert.")
                        QMessageBox.information(window, "Erfolg", "Handlungsstrang gespeichert.")
                    else:
                        log_error("Fehler beim Speichern des Handlungsstrangs.")
                        QMessageBox.critical(window, "Fehler", "Fehler beim Speichern.")
                        
                except Exception as e:
                    log_error(f"Fehler beim Speichern: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Speichern: {e}")
            
            save_btn.clicked.connect(on_save_clicked)
        
        # 6. Neuen Handlungsstrang Button
        new_btn = winFindChild(window, QWidget, "newBtnStorylines")
        if new_btn:
            def on_new_clicked():
                try:
                    new_data = {
                        "title": "Neuer Handlungsstrang",
                        "description": "",
                        "status": "Planung",
                        "created_date": QDate.currentDate().toString("yyyy-MM-dd"),
                        "edited_date": QDate.currentDate().toString("yyyy-MM-dd")
                    }
                    new_id = storyline_manager.add(new_data)
                    window.current_storyline_id = new_id
                    log_info(f"Neuer Handlungsstrang '{new_id}' erstellt.")
                    refresh_storylines_table()
                    QMessageBox.information(window, "Erfolg", f"Neuer Handlungsstrang erstellt: {new_id}")
                    
                except Exception as e:
                    log_error(f"Fehler beim Erstellen eines neuen Handlungsstrangs: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Erstellen: {e}")
            
            new_btn.clicked.connect(on_new_clicked)
        
        # 7. Nächster Handlungsstrang Button
        next_btn = winFindChild(window, QWidget, "nextBtnStorylines")
        if next_btn:
            def on_next_clicked():
                try:
                    if not window.storyline_keys_list:
                        return
                    current_index = window.storyline_keys_list.index(window.current_storyline_id)
                    next_index = (current_index + 1) % len(window.storyline_keys_list)
                    window.current_storyline_id = window.storyline_keys_list[next_index]
                    next_storyline = storyline_manager.get(window.current_storyline_id)
                    update_storyline_fields(window, next_storyline)
                    
                except Exception as e:
                    log_error(f"Fehler beim Navigieren: {e}")
            
            next_btn.clicked.connect(on_next_clicked)
        
        # 8. Vorheriger Handlungsstrang Button
        prev_btn = winFindChild(window, QWidget, "previousBtnStorylines")
        if prev_btn:
            def on_prev_clicked():
                try:
                    if not window.storyline_keys_list:
                        return
                    current_index = window.storyline_keys_list.index(window.current_storyline_id)
                    prev_index = (current_index - 1) % len(window.storyline_keys_list)
                    window.current_storyline_id = window.storyline_keys_list[prev_index]
                    prev_storyline = storyline_manager.get(window.current_storyline_id)
                    update_storyline_fields(window, prev_storyline)
                    
                except Exception as e:
                    log_error(f"Fehler beim Navigieren: {e}")
            
            prev_btn.clicked.connect(on_prev_clicked)
        
        # 9. Handlungsstrang löschen Button
        delete_btn = winFindChild(window, QWidget, "deleteBtnStorylines")
        if delete_btn:
            def on_delete_clicked():
                try:
                    if not window.current_storyline_id:
                        QMessageBox.warning(window, "Warnung", "Kein Handlungsstrang ausgewählt.")
                        return
                    
                    storyline_data = storyline_manager.get(window.current_storyline_id)
                    storyline_title = storyline_data.get("title", window.current_storyline_id)
                    
                    reply = QMessageBox.question(
                        window,
                        "Bestätigung",
                        f"Handlungsstrang '{storyline_title}' wirklich löschen?",
                        QMessageBox.Yes | QMessageBox.No
                    )
                    
                    if reply == QMessageBox.Yes:
                        storyline_manager.delete(window.current_storyline_id)
                        log_info(f"Handlungsstrang '{storyline_title}' gelöscht.")
                        refresh_storylines_table()
                        QMessageBox.information(window, "Erfolg", f"Handlungsstrang '{storyline_title}' gelöscht.")
                        
                except Exception as e:
                    log_error(f"Fehler beim Löschen: {e}")
                    QMessageBox.critical(window, "Fehler", f"Fehler beim Löschen: {e}")
            
            delete_btn.clicked.connect(on_delete_clicked)
        
        # 10. Exit-Button
        exit_btn = winFindChild(window, QWidget, "exitBtnStorylines")
        if exit_btn:
            def on_exit_clicked():
                window.close()
                if parent:
                    parent.show()
            
            exit_btn.clicked.connect(on_exit_clicked)
        
        # 11. Close Event Handler
        def on_close_event(event):
            settings = load_settings()
            save_settings(settings)
            event.accept()
            if parent:
                parent.show()
        
        window.closeEvent = on_close_event
        
        # Initiale Befüllung
        refresh_storylines_table()
        window.show()
        
        log_info("Handlungsstränge-Fenster erfolgreich mit Manager geladen.")
        return window
        
    except Exception as e:
        log_error(f"Fehler in show_storylines_window: {e}")
        QMessageBox.critical(None, "Fehler", f"Fehler beim Öffnen des Handlungsstränge-Fensters: {e}")
        return None
    return window

# Editorfenster anzeigen
def show_editor_window(parent=None):
    window = DynamicWindow("editor_ui", UI_FILES["editor"], splitter_name="mainSplitter")
    window.show()

    # --- Daten für Comboboxen laden ---
    storyline_data = safe_load_json(Path("data/storylines/data_storylines.json"), {})
    location_data = safe_load_json(Path("data/locations/data_locations.json"), {})
    character_data = safe_load_json(Path("data/characters/data_characters.json"), {})
    object_data = safe_load_json(Path("data/objects/data_objects.json"), {})

    # Storylines: Titel
    storyline_titles = [v.get("storyline_title", "") for v in storyline_data.values()]
    # Locations: Titel
    location_titles = [v.get("location_title", "") for v in location_data.values()]
    # Characters: Name + Vorname
    character_names = [
        f"{v.get('character_name', '')} {v.get('character_firstname', '')}".strip()
        for v in character_data.values()]
    # Objects: Titel
    object_titles = [v.get("object_title", "") for v in object_data.values()]


    # --- Kapitel-/Szenenstruktur laden ---
    settings = load_settings()
    last_project_key = settings.get("last_project")
    chapters_dir = Path("data/chapters")
    projects_data = safe_load_json(Path("data/projects/data_projects.json"), {})
    project = projects_data.get(last_project_key, {})
    project_id = project.get("project_ID", last_project_key.split("_")[-1])
    project_name = project.get("project_title", f"project_{project_id}")
    safe_project_name = "".join(c for c in project_name if c.isalnum() or c in ("_", "-")).rstrip()
    project_dir = chapters_dir / f"project_{project_id}"
    project_dir.mkdir(parents=True, exist_ok=True)

    # Bestehende Datei suchen (beginnt mit "data_<projektname>_")
    chapter_files = sorted(project_dir.glob(f"data_{safe_project_name}_*.json"))
    if chapter_files:
        chapter_file = chapter_files[-1]  # Die zuletzt erstellte Datei nehmen (nach Datum sortiert)
    else:
        # Wenn keine Datei existiert, Vorlage kopieren und neuen Namen vergeben
        today_str = QDate.currentDate().toString("yyyyMMdd")
        chapter_file = project_dir / f"data_{safe_project_name}_{today_str}.json"
        template = safe_load_json(chapters_dir / "data_project_00.json", {})
        safe_save_json(chapter_file, template)

    chapter_data = safe_load_json(chapter_file, {})
    window.chapter_data = chapter_data
    window.chapter_file = chapter_file

    update_chapter_list_widget(window)

    # --- Erstes Kapitel und erste Szene bestimmen ---
    first_chapter_key = next(iter(chapter_data.keys()), None)
    first_chapter = chapter_data[first_chapter_key] if first_chapter_key else None
    scene_keys = [k for k in first_chapter.keys() if k.startswith("scenes_id_")] if first_chapter else []
    first_scene_key = scene_keys[0] if scene_keys else None
    first_scene = first_chapter[first_scene_key] if first_scene_key else None

    # --- Kapitel-Felder setzen ---
    for field, (widget_type, widget_name) in EDITOR_CHAPTER_MAP.items():
        value = first_chapter.get(field, "") if first_chapter else ""
        widget = winFindChild(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)

    # --- Szenen-Felder setzen ---
    for field, (widget_type, widget_name) in EDITOR_SCENE_MAP.items():
        value = first_scene.get(field, "") if first_scene else ""
        widget = winFindChild(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                if field == "scene_plain_text":
                    widget.setHtml(str(value))
                else:
                    widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                try:
                    widget.setCurrentIndex(int(value))
                except Exception:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QSpinBox):
                try:
                    widget.setValue(int(value))
                except Exception:
                    widget.setValue(0)
            elif isinstance(widget, QDateEdit):
                if value:
                    date = QDate.fromString(value, "yyyy-MM-dd")
                    if date.isValid():
                        widget.setDate(date)
    
    # --- Labels und Zusatzfelder setzen ---
    # Kapitel-ID
    label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
    if label_chapter_id and first_chapter:
        label_chapter_id.setText(first_chapter.get("chapter_id", ""))

    # Szenen-ID
    label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
    if label_scene_id and first_scene:
        label_scene_id.setText(first_scene.get("scene_id", ""))

    # Projektname
    label_project = winFindChild(window, QLabel, "labelEditorActualProject")
    if label_project:
        label_project.setText(project_name)

    # Wortanzahl im Editor
    plain_text_widget = winFindChild(window, QTextEdit, "textEditorScenePlainText")
    label_word_count = winFindChild(window, QLabel, "labelEditorSceneWordCount")
    if plain_text_widget and label_word_count:
        def update_word_count():
            text = plain_text_widget.toPlainText()
            count = len(text.split())
            label_word_count.setText(str(count))
        plain_text_widget.textChanged.connect(update_word_count)
        update_word_count()

    # Comboboxen füllen
    fill_combobox(
    winFindChild(window, QComboBox, "comboBoxEditorSceneStoryline"), storyline_titles)
    fill_combobox(
        winFindChild(window, QComboBox, "comboBoxEditorSceneLocation"), location_titles)
    fill_combobox(
        winFindChild(window, QComboBox, "comboBoxEditorSceneCharacter"), character_names)
    fill_combobox(
        winFindChild(window, QComboBox, "comboBoxEditorSceneObject"), object_titles)
    
    combo_character = winFindChild(window, QComboBox, "comboBoxEditorSceneCharacter")
    listview_characters = winFindChild(window, QListWidget, "listWidgetEditorSceneCharacters")
    if combo_character and listview_characters:
        def on_character_selected(idx):
            name = combo_character.itemText(idx)
            items = [listview_characters.item(i).text() for i in range(listview_characters.count())]
            if name in items:
                for i in range(listview_characters.count()):
                    if listview_characters.item(i).text() == name:
                        listview_characters.takeItem(i)
                        break
            else:
                listview_characters.addItem(name)
        combo_character.setEditable(False)
        combo_character.currentIndexChanged.connect(on_character_selected)

    combo_object = winFindChild(window, QComboBox, "comboBoxEditorSceneObject")
    listview_objects = winFindChild(window, QListWidget, "listWidgetEditorSceneObjects")
    if combo_object and listview_objects:
        def on_object_selected(idx):
            name = combo_object.itemText(idx)
            items = [listview_objects.item(i).text() for i in range(listview_objects.count())]
            if name in items:
                for i in range(listview_objects.count()):
                    if listview_objects.item(i).text() == name:
                        listview_objects.takeItem(i)
                        break
            else:
                listview_objects.addItem(name)
        combo_object.setEditable(False)
        combo_object.currentIndexChanged.connect(on_object_selected)
    
    update_editor_info_labels(window, first_chapter)

    connect_text_formatting_buttons(window)

    # --- Save-Button einbinden ---
    save_btn = winFindChild(window, QWidget, "saveBtnEditorChapter")
    if save_btn:
        def on_save_chapter():
            chapter_data = window.chapter_data
            # Aktuelle Kapitel-ID aus dem Label holen
            label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
            current_chapter_id = label_chapter_id.text() if label_chapter_id else ""
            # Passenden Key im Dict suchen
            current_key = None
            for k, v in chapter_data.items():
                if v.get("chapter_id", "") == current_chapter_id:
                    current_key = k
                    break
            if not current_key:
                return
            # Felder auslesen und speichern
            chapter = chapter_data[current_key]
            chapter.update(read_editor_chapter_fields(window))
            chapter_data[current_key] = chapter
            safe_save_json(window.chapter_file, chapter_data)
            log_info(f"Kapitel {current_key} erfolgreich gespeichert.")

            # Kapitel-Liste aktualisieren
            update_chapter_list_widget(window)

            # Szenen bestimmen und Felder/Labels aktualisieren
            scene_keys = [k for k in chapter.keys() if k.startswith("scenes_id_")]
            current_scene = chapter[scene_keys[0]] if scene_keys else None

            # Felder für Szene setzen
            update_editor_scene_fields(window, current_scene if current_scene else {})
            # Szenen-ID-Label aktualisieren
            label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
            if label_scene_id:
                label_scene_id.setText(current_scene.get("scene_id", "") if current_scene else "")

            # Info-Labels aktualisieren
            update_editor_info_labels(window, chapter, current_scene)
        save_btn.clicked.connect(on_save_chapter)

    # --- Neuer Kapitel-Button einbinden ---
    new_btn = winFindChild(window, QWidget, "newBtnEditorChapter")
    if new_btn:
        def on_new_chapter():
            chapter_data = window.chapter_data
            # Neuen Key und ID generieren
            new_key, new_id = get_next_id(chapter_data, "chapter_id_")
            empty_chapter = get_empty_chapter()
            empty_chapter["chapter_id"] = new_id
            # Optional: aktuelles Datum setzen
            today = QDate.currentDate().toString("yyyy-MM-dd")
            empty_chapter["chapter_begin"] = today
            empty_chapter["chapter_edited"] = today
            # Kapitel hinzufügen und speichern
            chapter_data[new_key] = empty_chapter
            safe_save_json(window.chapter_file, chapter_data)
            # Kapitel-Liste aktualisieren
            update_chapter_list_widget(window)
            # Felder im Editor setzen
            for field, (widget_type, widget_name) in EDITOR_CHAPTER_MAP.items():
                widget = winFindChild(window, widget_type, widget_name)
                value = empty_chapter.get(field, "")
                if widget:
                    if isinstance(widget, QLineEdit):
                        widget.setText(str(value))
                    elif isinstance(widget, QTextEdit):
                        widget.setPlainText(str(value))
                    elif isinstance(widget, QComboBox):
                        try:
                            widget.setCurrentIndex(int(value))
                        except Exception:
                            widget.setCurrentIndex(0)
                    elif isinstance(widget, QDateEdit):
                        if value:
                            date = QDate.fromString(value, "yyyy-MM-dd")
                            if date.isValid():
                                widget.setDate(date)
            # Kapitel-ID-Label aktualisieren
            update_editor_chapter_fields(window, empty_chapter)
            label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
            if label_chapter_id:
                label_chapter_id.setText(new_id)
            # Szene-Felder leeren
            update_editor_scene_fields(window, {})
            label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
            if label_scene_id:
                label_scene_id.setText("")
            update_editor_info_labels(window, empty_chapter, None)
            log_info(f"Neues Kapitel {new_key} angelegt.")
        
        new_btn.clicked.connect(on_new_chapter)

    # --- Next-Kapitel-Button einbinden ---
    next_btn = winFindChild(window, QWidget, "nextBtnEditorChapter")
    if next_btn:
        def on_next_chapter():
            chapter_data = window.chapter_data
            keys = list(chapter_data.keys())
            if not keys:
                return
            # Aktuelles Kapitel bestimmen
            current_id = winFindChild(window, QLabel, "labelEditorChapterID")
            current_key = None
            if current_id:
                for k, v in chapter_data.items():
                    if v.get("chapter_id", "") == current_id.text():
                        current_key = k
                        break
            if current_key and current_key in keys:
                idx = keys.index(current_key)
                next_idx = (idx + 1) % len(keys)
            else:
                next_idx = 0
            next_key = keys[next_idx]
            next_chapter = chapter_data[next_key]
            # Felder setzen
            update_editor_chapter_fields(window, next_chapter)
            scene_keys = [k for k in next_chapter.keys() if k.startswith("scenes_id_")]
            next_scene = next_chapter[scene_keys[0]] if scene_keys else None
            update_editor_scene_fields(window, next_scene if next_scene else {})
            label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
            if label_chapter_id:
                label_chapter_id.setText(next_chapter.get("chapter_id", ""))
            label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
            if label_scene_id:
                label_scene_id.setText(next_scene.get("scene_id", "") if next_scene else "")
            update_editor_info_labels(window, next_chapter, next_scene)
        next_btn.clicked.connect(on_next_chapter)

    # --- Prev-Kapitel-Button einbinden ---
    prev_btn = winFindChild(window, QWidget, "previousBtnEditorChapter")
    if prev_btn:
        def on_prev_chapter():
            chapter_data = window.chapter_data
            keys = list(chapter_data.keys())
            if not keys:
                return
            # Aktuelles Kapitel bestimmen
            current_id = winFindChild(window, QLabel, "labelEditorChapterID")
            current_key = None
            if current_id:
                for k, v in chapter_data.items():
                    if v.get("chapter_id", "") == current_id.text():
                        current_key = k
                        break
            if current_key and current_key in keys:
                idx = keys.index(current_key)
                prev_idx = (idx - 1) % len(keys)
            else:
                prev_idx = 0
            prev_key = keys[prev_idx]
            prev_chapter = chapter_data[prev_key]
            # Felder setzen
            update_editor_chapter_fields(window, prev_chapter)
            scene_keys = [k for k in prev_chapter.keys() if k.startswith("scenes_id_")]
            prev_scene = prev_chapter[scene_keys[0]] if scene_keys else None
            update_editor_scene_fields(window, prev_scene if prev_scene else {})
            label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
            if label_chapter_id:
                label_chapter_id.setText(prev_chapter.get("chapter_id", ""))
            label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
            if label_scene_id:
                label_scene_id.setText(prev_scene.get("scene_id", "") if prev_scene else "")
            update_editor_info_labels(window, prev_chapter, prev_scene)
        prev_btn.clicked.connect(on_prev_chapter)

    # --- Delete-Kapitel-Button einbinden ---
    delete_btn = winFindChild(window, QWidget, "deleteBtnEditorChapter")
    if delete_btn:
        def on_delete_chapter():
            chapter_data = window.chapter_data
            # Aktuelle Kapitel-ID aus dem Label holen
            label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
            current_chapter_id = label_chapter_id.text() if label_chapter_id else ""
            # Passenden Key im Dict suchen
            current_key = None
            for k, v in chapter_data.items():
                if v.get("chapter_id", "") == current_chapter_id:
                    current_key = k
                    break
            if not current_key:
                return
            # Bestätigungsdialog
            if not show_secure_dialog(window, action="delete_chapter", project_key=current_chapter_id):
                return
            # Kapitel löschen
            del chapter_data[current_key]
            safe_save_json(window.chapter_file, chapter_data)
            log_info(f"Kapitel {current_key} gelöscht.")
            # Kapitel-Liste im QListWidget aktualisieren
            update_chapter_list_widget(window)
            # Nächstes oder vorheriges Kapitel anzeigen
            keys = list(chapter_data.keys())
            if keys:
                # Wähle das nächste Kapitel, falls möglich, sonst das vorherige
                idx = 0
                if current_key in keys:
                    idx = keys.index(current_key)
                if idx >= len(keys):
                    idx = len(keys) - 1
                next_key = keys[idx]
                next_chapter = chapter_data[next_key]
                update_editor_chapter_fields(window, next_chapter)
                scene_keys = [k for k in next_chapter.keys() if k.startswith("scenes_id_")]
                next_scene = next_chapter[scene_keys[0]] if scene_keys else None
                update_editor_scene_fields(window, next_scene if next_scene else {})
                label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
                if label_chapter_id:
                    label_chapter_id.setText(next_chapter.get("chapter_id", ""))
                label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
                if label_scene_id:
                    label_scene_id.setText(next_scene.get("scene_id", "") if next_scene else "")
                update_editor_info_labels(window, next_chapter, next_scene)                

            else:
                # Keine Kapitel mehr vorhanden: Felder leeren
                for field, (widget_type, widget_name) in EDITOR_CHAPTER_MAP.items():
                    widget = winFindChild(window, widget_type, widget_name)
                    if widget:
                        if isinstance(widget, QLineEdit):
                            widget.clear()
                        elif isinstance(widget, QTextEdit):
                            widget.clear()
                        elif isinstance(widget, QComboBox):
                            widget.setCurrentIndex(0)
                        elif isinstance(widget, QDateEdit):
                            widget.setDate(QDate.currentDate())
                label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
                if label_chapter_id:
                    label_chapter_id.setText("")

        delete_btn.clicked.connect(on_delete_chapter)

    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnEditor")
    if exit_btn:
        def on_exit_clicked():
            window.close()
            if parent:
                parent.show()
        exit_btn.clicked.connect(on_exit_clicked)
    
    # --- Szenen-Buttons einbinden ---
    def get_current_chapter():
        chapter_data = window.chapter_data
        label_chapter_id = winFindChild(window, QLabel, "labelEditorChapterID")
        current_chapter_id = label_chapter_id.text() if label_chapter_id else ""
        for k, v in chapter_data.items():
            if v.get("chapter_id", "") == current_chapter_id:
                return v
        return None

    def get_current_scene_key_and_scene(chapter):
        label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
        current_scene_id = label_scene_id.text() if label_scene_id else ""
        scene_keys = [k for k in chapter.keys() if k.startswith("scenes_id_")]
        for k in scene_keys:
            if chapter[k].get("scene_id", "") == current_scene_id:
                return k, chapter[k], scene_keys
        # Fallback: erste Szene
        if scene_keys:
            return scene_keys[0], chapter[scene_keys[0]], scene_keys
        return None, None, scene_keys

    # --- Save Szene ---
    save_scene_btn = winFindChild(window, QWidget, "saveBtnEditorScene")
    if save_scene_btn:
        def on_save_scene():
            chapter = get_current_chapter()
            if not chapter:
                return
            scene_key, scene, scene_keys = get_current_scene_key_and_scene(chapter)
            if not scene_key:
                return
            scene.update(read_editor_scene_fields(window))
            scene = ensure_all_scene_fields(scene)
            update_editor_info_labels(window, chapter, scene)
            # Bearbeitet-Datum setzen
            today = QDate.currentDate().toString("yyyy-MM-dd")
            scene["scene_edited"] = today
            chapter[scene_key] = scene
            safe_save_json(window.chapter_file, window.chapter_data)
            log_info(f"Szene {scene_key} gespeichert.")
        save_scene_btn.clicked.connect(on_save_scene)

    new_scene_btn = winFindChild(window, QWidget, "newBtnEditorScene")
    if new_scene_btn:
        def on_new_scene():
            chapter_data = window.chapter_data
            chapter = get_current_chapter()
            if not chapter:
                return
            new_id = get_next_project_scene_id(chapter_data)
            new_key = f"scenes_id_{int(new_id):02d}"
            today = QDate.currentDate().toString("yyyy-MM-dd")
            empty_scene = {
                "scene_id": new_id,
                "scene_title": "",
                "scene_premise": "",
                "scene_status": 0,
                "scene_begin": today,
                "scene_edited": today,
                "scene_word_count": "",
                "scene_order": get_next_scene_order(chapter),
                "scene_goal": "",
                "scene_result ": "",
                "scene_storyline": 0,
                "scene_location": 0,
                "scene_characters": [],
                "scene_objects": [],
                "scene_mood": "",
                "scene_duration": "",
                "scene_type": "",
                "scene_tags": "",
                "scene_notes": "",
                "scene_plain_text": ""   
            }
            chapter[new_key] = empty_scene
            safe_save_json(window.chapter_file, chapter_data)
            update_editor_scene_fields(window, empty_scene)
            label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
            if label_scene_id:
                label_scene_id.setText(new_id)
            update_editor_info_labels(window, chapter, empty_scene)
            log_info(f"Neue Szene {new_key} angelegt.")
        new_scene_btn.clicked.connect(on_new_scene)

    # --- Next Szene ---
    next_scene_btn = winFindChild(window, QWidget, "nextBtnEditorScene")
    if next_scene_btn:
        def on_next_scene():
            chapter = get_current_chapter()
            if not chapter:
                return
            scene_key, scene, scene_keys = get_current_scene_key_and_scene(chapter)
            if not scene_keys:
                return
            idx = scene_keys.index(scene_key) if scene_key in scene_keys else 0
            next_idx = (idx + 1) % len(scene_keys)
            next_key = scene_keys[next_idx]
            next_scene = chapter[next_key]
            update_editor_scene_fields(window, next_scene)
            label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
            if label_scene_id:
                label_scene_id.setText(next_scene.get("scene_id", ""))
            update_editor_info_labels(window, chapter, next_scene)
        next_scene_btn.clicked.connect(on_next_scene)

    # --- Prev Szene ---
    prev_scene_btn = winFindChild(window, QWidget, "previousBtnEditorScene")
    if prev_scene_btn:
        def on_prev_scene():
            chapter = get_current_chapter()
            if not chapter:
                return
            scene_key, scene, scene_keys = get_current_scene_key_and_scene(chapter)
            if not scene_keys:
                return
            idx = scene_keys.index(scene_key) if scene_key in scene_keys else 0
            prev_idx = (idx - 1) % len(scene_keys)
            prev_key = scene_keys[prev_idx]
            prev_scene = chapter[prev_key]
            update_editor_scene_fields(window, prev_scene)
            label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
            if label_scene_id:
                label_scene_id.setText(prev_scene.get("scene_id", ""))
            update_editor_info_labels(window, chapter, prev_scene)
        prev_scene_btn.clicked.connect(on_prev_scene)

    # --- Delete Szene ---
    delete_scene_btn = winFindChild(window, QWidget, "deleteBtnEditorScene")
    if delete_scene_btn:
        def on_delete_scene():
            chapter = get_current_chapter()
            if not chapter:
                return
            scene_key, scene, scene_keys = get_current_scene_key_and_scene(chapter)
            if not scene_key:
                return
            label_scene_id = winFindChild(window, QLabel, "labelEditorSceneID")
            current_scene_id = label_scene_id.text() if label_scene_id else ""
            if not show_secure_dialog(window, action="delete_scene", project_key=current_scene_id):
                return
            del chapter[scene_key]
            renumber_scene_orders(window.chapter_data)
            safe_save_json(window.chapter_file, window.chapter_data)
            log_info(f"Szene {scene_key} gelöscht.")
            # Nächste Szene anzeigen oder Felder leeren
            scene_keys = [k for k in chapter.keys() if k.startswith("scenes_id_")]
            if scene_keys:
                next_scene = chapter[scene_keys[0]]
                update_editor_scene_fields(window, next_scene)
                if label_scene_id:
                    label_scene_id.setText(next_scene.get("scene_id", ""))
                update_editor_info_labels(window, chapter, next_scene)
            else:
                for field, (widget_type, widget_name) in EDITOR_SCENE_MAP.items():
                    widget = winFindChild(window, widget_type, widget_name)
                    if widget:
                        if isinstance(widget, QLineEdit):
                            widget.clear()
                        elif isinstance(widget, QTextEdit):
                            widget.clear()
                        elif isinstance(widget, QComboBox):
                            widget.setCurrentIndex(0)
                        elif isinstance(widget, QSpinBox):
                            widget.setValue(0)
                        elif isinstance(widget, QDateEdit):
                            widget.setDate(QDate.currentDate())
                if label_scene_id:
                    label_scene_id.setText("")
                update_editor_info_labels(window, chapter, None)
        delete_scene_btn.clicked.connect(on_delete_scene)    

    # -- Close Event überschreiben ---
    def on_close_event(event):
        settings = load_settings()
        save_settings(settings)
        event.accept()
        if parent:
            parent.show()
    window.closeEvent = on_close_event

    log_info("Editorfenster erfolgreich geladen und angezeigt.")
    return window

# Preferences-Fenster anzeigen
def show_preferences_window(parent=None):
    window = DynamicWindow("preferences_ui", UI_FILES["preferences"], splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnPreferences")
    if exit_btn:
        def on_exit_clicked():
            window.close()
            if parent:
                parent.show()
        exit_btn.clicked.connect(on_exit_clicked)   
    
    def on_close_event(event):
        settings = load_settings()
        save_settings(settings)
        event.accept()
        if parent:
            parent.show()
    window.closeEvent = on_close_event

    log_info("Einstellungen-Fenster erfolgreich geladen und angezeigt.")
    return window

# Hilfe-Fenster anzeigen
def show_help_window(parent=None):
    window = DynamicWindow("help_ui", UI_FILES["help"], splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnHelp")
    if exit_btn:
        def on_exit_clicked():
            window.close()
            if parent:
                parent.show()
        exit_btn.clicked.connect(on_exit_clicked)
    
    def on_close_event(event):
        settings = load_settings()
        save_settings(settings)
        event.accept()
        if parent:
            parent.show()
    window.closeEvent = on_close_event

    log_info("Hilfe-Fenster erfolgreich geladen und angezeigt.")
    return window

# Referenz-Verwaltungsfenster anzeigen
def show_references_window(parent=None):
    """
    Zeigt die Referenz-Verwaltungsschnittstelle.
    Ermöglicht Benutzern, Referenzen zu verwalten, zu validieren und Zitate zu generieren.
    """
    from PySide6.QtWidgets import (
        QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, 
        QTableWidgetItem, QMessageBox, QComboBox, QLineEdit, QLabel
    )
    from PySide6.QtCore import Qt
    
    dialog = QDialog(parent)
    dialog.setWindowTitle("Referenz-Verwaltung - CSNova")
    dialog.setGeometry(100, 100, 1000, 600)
    
    layout = QVBoxLayout()
    
    # === Header mit Buttons ===
    button_layout = QHBoxLayout()
    
    add_btn = QPushButton("Referenz hinzufügen")
    delete_btn = QPushButton("Löschen")
    validate_btn = QPushButton("Validieren")
    duplicate_btn = QPushButton("Duplikate prüfen")
    close_btn = QPushButton("Schließen")
    
    button_layout.addWidget(add_btn)
    button_layout.addWidget(delete_btn)
    button_layout.addWidget(validate_btn)
    button_layout.addWidget(duplicate_btn)
    button_layout.addStretch()
    button_layout.addWidget(close_btn)
    
    layout.addLayout(button_layout)
    
    # === Tabelle für Referenzen ===
    table = QTableWidget()
    table.setColumnCount(5)
    table.setHorizontalHeaderLabels(["ID", "Typ", "Titel", "Autoren", "Jahr"])
    table.setSelectionBehavior(table.SelectRows)
    layout.addWidget(table)
    
    # === Info-Bereich ===
    info_layout = QHBoxLayout()
    info_label = QLabel("Referenzen geladen: 0")
    citation_format_label = QLabel("Zitierformat:")
    citation_format = QComboBox()
    citation_format.addItems(["APA", "Harvard", "Oxford", "MLA", "Chicago", "Vancouver", "IEEE"])
    
    info_layout.addWidget(info_label)
    info_layout.addStretch()
    info_layout.addWidget(citation_format_label)
    info_layout.addWidget(citation_format)
    
    layout.addLayout(info_layout)
    
    # === Zitat-Anzeige ===
    citation_label = QLabel("Generiertes Zitat:")
    citation_text = QLineEdit()
    citation_text.setReadOnly(True)
    layout.addWidget(citation_label)
    layout.addWidget(citation_text)
    
    dialog.setLayout(layout)
    
    # === Funktionalität laden ===
    def load_references():
        """Lade Referenzen aus ReferenceManager"""
        try:
            if app_state.ref_manager is None:
                QMessageBox.warning(dialog, "Fehler", "ReferenceManager nicht initialisiert")
                return
            
            refs = app_state.ref_manager.get_all_references()
            table.setRowCount(len(refs))
            
            for row, (ref_id, ref_data) in enumerate(refs.items()):
                ref_type = ref_data.get("type", "?")
                title = ref_data.get("title", "?")
                authors = ref_data.get("authors", [])
                author_names = ", ".join([f"{a.get('name', '')} {a.get('initial', '')}" for a in authors]) if authors else "?"
                year = ref_data.get("year", "?")
                
                table.setItem(row, 0, QTableWidgetItem(ref_id))
                table.setItem(row, 1, QTableWidgetItem(ref_type))
                table.setItem(row, 2, QTableWidgetItem(title))
                table.setItem(row, 3, QTableWidgetItem(author_names))
                table.setItem(row, 4, QTableWidgetItem(year))
            
            info_label.setText(f"Referenzen geladen: {len(refs)}")
            table.resizeColumnsToContents()
            log_info(f"✓ {len(refs)} Referenzen in UI geladen")
        except Exception as e:
            log_exception("Fehler beim Laden von Referenzen", e)
            QMessageBox.critical(dialog, "Fehler", f"Konnte Referenzen nicht laden: {e}")
    
    def validate_references():
        """Validiere alle Referenzen"""
        try:
            if app_state.ref_manager is None:
                QMessageBox.warning(dialog, "Fehler", "ReferenceManager nicht initialisiert")
                return
            
            errors = app_state.ref_manager.validate_all()
            if not errors:
                QMessageBox.information(dialog, "Validierung", "✓ Alle Referenzen sind gültig!")
            else:
                error_msg = "Validierungsfehler gefunden:\n\n"
                for ref_id, error_list in errors.items():
                    error_msg += f"{ref_id}:\n  - " + "\n  - ".join(error_list) + "\n\n"
                QMessageBox.warning(dialog, "Validierungsfehler", error_msg)
            
            log_info(f"✓ Validierung durchgeführt: {len(errors)} Fehler")
        except Exception as e:
            log_exception("Fehler bei Validierung", e)
            QMessageBox.critical(dialog, "Fehler", f"Validierung fehlgeschlagen: {e}")
    
    def check_duplicates():
        """Prüfe auf doppelte Referenzen"""
        try:
            if app_state.ref_manager is None:
                QMessageBox.warning(dialog, "Fehler", "ReferenceManager nicht initialisiert")
                return
            
            duplicates = app_state.ref_manager.check_duplicates()
            if not duplicates:
                QMessageBox.information(dialog, "Duplikat-Prüfung", "✓ Keine Duplikate gefunden!")
            else:
                dup_msg = f"{len(duplicates)} Duplikat(e) gefunden:\n\n"
                for dup in duplicates:
                    dup_msg += f"  • {dup['ref1_id']} ↔ {dup['ref2_id']}\n"
                QMessageBox.warning(dialog, "Duplikate erkannt", dup_msg)
            
            log_info(f"✓ Duplikat-Prüfung: {len(duplicates)} gefunden")
        except Exception as e:
            log_exception("Fehler bei Duplikat-Prüfung", e)
            QMessageBox.critical(dialog, "Fehler", f"Duplikat-Prüfung fehlgeschlagen: {e}")
    
    def generate_citation():
        """Generiere Zitat für ausgewählte Referenz"""
        try:
            selected_rows = table.selectionModel().selectedRows()
            if not selected_rows:
                QMessageBox.warning(dialog, "Fehler", "Bitte wählen Sie eine Referenz aus")
                return
            
            if app_state.ref_manager is None or app_state.cite_manager is None:
                QMessageBox.warning(dialog, "Fehler", "Manager nicht initialisiert")
                return
            
            ref_id = table.item(selected_rows[0].row(), 0).text()
            ref = app_state.ref_manager.get_reference(ref_id)
            
            if not ref:
                QMessageBox.warning(dialog, "Fehler", f"Referenz {ref_id} nicht gefunden")
                return
            
            format_style = citation_format.currentText()
            citation = app_state.cite_manager.get_citation(ref, format_style)
            citation_text.setText(citation)
            log_info(f"✓ Zitat generiert: {ref_id} ({format_style})")
        except Exception as e:
            log_exception("Fehler bei Zitat-Generierung", e)
            QMessageBox.critical(dialog, "Fehler", f"Zitat konnte nicht generiert werden: {e}")
    
    # === Signal-Verbindungen ===
    close_btn.clicked.connect(dialog.close)
    validate_btn.clicked.connect(validate_references)
    duplicate_btn.clicked.connect(check_duplicates)
    table.itemSelectionChanged.connect(generate_citation)
    citation_format.currentTextChanged.connect(generate_citation)
    
    # === Initial laden ===
    load_references()
    
    dialog.exec()
    log_info("Referenz-Verwaltungsfenster geschlossen")
    return dialog

# Anwendung starten
def main(managers=None):
    """
    Haupteinsprungspunkt der CSNova Anwendung.
    
    Args:
        managers: Dictionary mit allen Manager-Instanzen aus initialize_all_managers()
                  oder Tuple (ref_manager, cite_manager) für Backwards Compatibility
    """
    setup_logging()
    log_header()
    log_info("Starte CSNova Anwendung")
    app = QApplication(sys.argv)
    
    # Speichere Manager in app_state für Zugriff aus UI-Komponenten
    if managers is not None:
        if isinstance(managers, dict):
            # Neue API: Dictionary mit allen Managern
            app_state.references = managers.get("references")
            app_state.citations = managers.get("citations")
            app_state.projects = managers.get("projects")
            app_state.characters = managers.get("characters")
            app_state.locations = managers.get("locations")
            app_state.objects = managers.get("objects")
            app_state.storylines = managers.get("storylines")
            app_state.ideas = managers.get("ideas")
            app_state.chapters = managers.get("chapters")
            # Backwards compatibility
            app_state.ref_manager = managers.get("references")
            app_state.cite_manager = managers.get("citations")
        elif isinstance(managers, tuple) and len(managers) == 2:
            # Alte API: Tuple (ref_manager, cite_manager)
            app_state.ref_manager = managers[0]
            app_state.cite_manager = managers[1]
            app_state.references = managers[0]
            app_state.citations = managers[1]

    try:
        settings = load_settings()
        log_info(f"Einstellungen geladen: {settings}")

        # Erster Start? Sprache setzen
        if "first_start" not in settings:
            settings["first_start"] = True
        if "language" not in settings:
            system_lang = get_system_language()
            settings["language"] = system_lang
            save_settings(settings)
            log_info(f"Sprache in Einstellungen gesetzt: {system_lang}")

        # Fenster anzeigen
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
