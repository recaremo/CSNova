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
    QApplication, QLabel, QWidget, QVBoxLayout, QSizePolicy, QSplitter, QListWidget,
    QMainWindow, QComboBox, QLineEdit, QSpinBox, QTextEdit, QDateEdit, QCheckBox,
    QToolBar, QDockWidget, QDialog, QPlainTextEdit
)
from PySide6.QtGui import QFont, QIcon, QRegularExpressionValidator, QPixmap
from PySide6.QtCore import QDate, QRegularExpression, QTimer, QEvent
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
# Globale Referenzen auf Fenster
class CSNovaApp:
    def __init__(self):
        self.main_window = None
        self.start_window = None
        self.help_window = None
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
            "scene_character": (QComboBox, "comboBoxEditorSceneCharacter"),
            "scene_object": (QComboBox, "comboBoxEditorSceneObject"),
            "scene_mood": (QLineEdit, "lineEditorceneMood"),
            "scene_duration": (QLineEdit, "lineEditorSceneDuration"),
            "scene_type": (QLineEdit, "lineEditorSceneType"),
            "scene_tags": (QTextEdit, "textEditorSceneTags"),
            "scene_notes": (QTextEdit, "textEditorSceneNotes"),
            "scene_plain_text": (QPlainTextEdit, "plainTextEditorScenePlainText"),
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
def read_editor_scene_fields(window):
    scene = {}
    for field, (widget_type, widget_name) in EDITOR_SCENE_MAP.items():
        widget = winFindChild(window, widget_type, widget_name)
        if widget:
            if isinstance(widget, QLineEdit):
                scene[field] = widget.text()
            elif isinstance(widget, QTextEdit):
                scene[field] = widget.toPlainText()
            elif isinstance(widget, QPlainTextEdit):
                scene[field] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                scene[field] = widget.currentIndex()
            elif isinstance(widget, QSpinBox):
                scene[field] = widget.value()
            elif isinstance(widget, QDateEdit):
                scene[field] = widget.date().toString("yyyy-MM-dd")
    return scene
# Setzt die Werte aus den Szenen-Widgets basierend auf einem Szenen-Dictionary
def update_editor_scene_fields(window, scene):
    for field, (widget_type, widget_name) in EDITOR_SCENE_MAP.items():
        widget = winFindChild(window, widget_type, widget_name)
        value = scene.get(field, "")
        if widget:
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QPlainTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                try:
                    # Korrektur: Setze den gespeicherten Index oder Wert
                    if isinstance(value, int):
                        widget.setCurrentIndex(value)
                    else:
                        idx = widget.findText(str(value))
                        widget.setCurrentIndex(idx if idx >= 0 else 0)
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
# Nächste freie Szenenbestellung in einem Kapitel ermitteln
def get_next_scene_order(chapter):
    orders = [int(v.get("scene_order", "0")) for k, v in chapter.items() if k.startswith("scenes_id_")]
    return max(orders, default=0) + 1
# Aktualisiere die Informationslabels im Editor
def update_editor_info_labels(window, chapter=None, scene=None):
    # Storyline
    storyline_combo = winFindChild(window, QComboBox, "comboBoxEditorSceneStoryline")
    label_storyline = winFindChild(window, QLabel, "labelEditorStorylineText")
    if storyline_combo and label_storyline:
        label_storyline.setText(storyline_combo.currentText())

    # Location
    location_combo = winFindChild(window, QComboBox, "comboBoxEditorSceneLocation")
    label_location = winFindChild(window, QLabel, "labelEditorLocationText")
    if location_combo and label_location:
        label_location.setText(location_combo.currentText())

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
# ...existing code...

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
    languages = safe_load_json(Path("core/translations/languages.json"), {})
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
    designs = load_translation(Path("core/translations/design.json"), language)
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
    window = DynamicWindow("projects_ui", UI_FILES["projects"], splitter_name="mainSplitter")
    window.show()
    log_info("Projektfenster erfolgreich geladen und angezeigt.")

    # 1. Sprache ermitteln
    settings = load_settings()
    language = settings.get("language", "de")

    # 2. Daten laden
    projects_path = Path("data/projects/data_projects.json")
    projects_data = safe_load_json(projects_path, {})
    if not projects_data:
        empty_project = get_empty_project()
        empty_project["project_ID"] = "1"
        projects_data = {"project_ID_01": empty_project}
        safe_save_json(projects_path, projects_data)

    first_key = next(iter(projects_data.keys()))
    window.current_project_key = first_key
    current_project = projects_data[window.current_project_key]
    # 3. Zielgruppe
    target_groups = load_translation(Path("core/translations/targetGroups.json"), language)
    combo_target_group = winFindChild(window,QComboBox, "comboBoxProjectTargetGroup")
    fill_combobox(combo_target_group, list(target_groups.values()), current_project.get("project_target_group", 0))
    # 4. Erzählperspektive
    perspectives = load_translation(Path("core/translations/narrativePerspective.json"), language)
    combo_narrative = winFindChild(window,QComboBox, "comboBoxProjectNarrativePerspective")
    fill_combobox(combo_narrative, list(perspectives.values()), current_project.get("project_narrative_perspective", 0))
    # 5. Stil
    styles = load_translation(Path("core/translations/style.json"), language)
    combo_style = winFindChild(window,QComboBox, "comboBoxProjectStyle")
    fill_combobox(combo_style, list(styles.values()), current_project.get("project_style", 0))
    # 6. Genre
    genres_root = load_translation(Path("core/translations/genre.json"), language)
    genres = genres_root.get("book_genres", {}) if isinstance(genres_root, dict) else {}
    combo_genre = winFindChild(window,QComboBox, "comboBoxProjectGenre")
    fill_combobox(combo_genre, list(genres.values()), current_project.get("project_genre", 0))
    # 7. Arbeitstyp
    working_root = load_translation(Path("core/translations/workingType.json"), language)
    working_types = working_root.get("book_working_types", {}) if isinstance(working_root, dict) else {}
    combo_work_type = winFindChild(window, QComboBox, "comboBoxProjectWorkingType")
    fill_combobox(combo_work_type, list(working_types.values()), current_project.get("project_work_type", 0))
    # 8. Motiv
    motifs = load_translation(Path("core/translations/motif.json"), language)
    combo_motif = winFindChild(window,QComboBox, "comboBoxProjectMotif")
    fill_combobox(combo_motif, list(motifs.values()), current_project.get("project_motif", 0))
    # 9. Status
    status = load_translation(Path("core/translations/status.json"), language)
    combo_status = winFindChild(window,QComboBox, "comboBoxProjectStatus")
    fill_combobox(combo_status, list(status.values()), current_project.get("project_status", 0))
    # 10. Verlag
    publishers_root = safe_load_json(Path("core/translations/publisher.json"), {})
    publishers = publishers_root.get("publishers", []) if isinstance(publishers_root, dict) else []
    publisher_names = [pub.get("name", "") for pub in publishers if pub.get("type") == "book"]
    combo_publisher = winFindChild(window,QComboBox, "comboBoxProjectPublisher")
    fill_combobox(combo_publisher, publisher_names, current_project.get("project_publisher", 0))
    # 11. Editor
    editors_root = safe_load_json(Path("core/translations/editor.json"), {})
    editors = editors_root.get("editors", []) if isinstance(editors_root, dict) else []
    editor_names = [ed.get("name", "") for ed in editors if ed.get("type") == "book"]
    combo_editor = winFindChild(window,QComboBox, "comboBoxProjectEditor")
    fill_combobox(combo_editor, editor_names, current_project.get("project_editor", 0))

    # Felder setzen
    update_project_fields(window, current_project)
   

    # Buttons einbinden
    # --- New-Button einbinden ---
    new_btn = winFindChild(window,QWidget, "newBtnProjects")
    if new_btn:
        def on_new_clicked():
            projects_data = safe_load_json(projects_path, {})
            new_key, new_id = get_next_id(projects_data, "project_ID_")
            empty_project = get_empty_project()
            empty_project["project_ID"] = new_id
            projects_data[new_key] = empty_project
            safe_save_json(projects_path, projects_data)
            log_info(f"Neues Projekt {new_key} angelegt.")
            window.current_project_key = new_key
            update_project_fields(window, empty_project)
        new_btn.clicked.connect(on_new_clicked)

    # --- Next-Button ---
    next_btn = winFindChild(window,QWidget, "nextBtnProjects")
    if next_btn:
        def on_next_clicked():
            projects_data = safe_load_json(projects_path, {})
            keys = list(projects_data.keys())
            current_index = keys.index(window.current_project_key)
            next_index = (current_index + 1) % len(keys)
            next_key = keys[next_index]
            window.current_project_key = next_key
            next_project = projects_data[next_key]
            update_project_fields(window, next_project)
        next_btn.clicked.connect(on_next_clicked)

    # --- Previous-Button ---
    previous_btn = winFindChild(window,QWidget, "previousBtnProjects")
    if previous_btn:
        def on_previous_clicked():
            projects_data = safe_load_json(projects_path, {})
            keys = list(projects_data.keys())
            current_index = keys.index(window.current_project_key)
            previous_index = (current_index - 1) % len(keys)
            previous_key = keys[previous_index]
            window.current_project_key = previous_key
            previous_project = projects_data[previous_key]
            update_project_fields(window, previous_project)
        previous_btn.clicked.connect(on_previous_clicked) 

    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnProjects")
    if exit_btn and parent:
        def on_exit_clicked():
            window.close()
            parent.show()
        exit_btn.clicked.connect(on_exit_clicked)

    def on_close_event(event):
        settings = load_settings()
        settings["last_project"] = window.current_project_key
        save_settings(settings)
        event.accept()
        if parent:
            parent.show()
    window.closeEvent = on_close_event

    # --- Delete-Button einbinden ---
    def on_delete_clicked():
        projects_data = safe_load_json(projects_path, {})
        project_key = window.current_project_key
        project_title = projects_data[project_key].get("project_title", project_key)
        def delete_project():
            nonlocal projects_data, project_key, project_title
            if project_key in projects_data:
                del projects_data[project_key]
                # Speichern der geänderten Daten
                safe_save_json(projects_path, projects_data)
                log_info(f"Projekt {project_title} gelöscht.")
                # Nach dem Löschen: neuen Key setzen und Felder aktualisieren
                keys = list(projects_data.keys())
                if keys:
                    # Wähle den nächsten Projekt-Key (oder den ersten, falls Index zu groß)
                    idx = 0
                    if project_key in keys:
                        idx = keys.index(project_key)
                    elif window.current_project_key and window.current_project_key in keys:
                        idx = keys.index(window.current_project_key)
                    if idx >= len(keys):
                        idx = len(keys) - 1
                    window.current_project_key = keys[idx]
                    update_project_fields(window, projects_data[window.current_project_key])
                else:
                    empty_project = get_empty_project()
                    update_project_fields(window, empty_project)
                    window.current_project_key = None
        # Blockierender Bestätigungsdialog; delete_project() nur bei Bestätigung ausführen
        if show_secure_dialog(window, action="delete_project", project_key=project_title):
            delete_project()
    delete_btn = winFindChild(window,QWidget, "deleteBtnProjects")
    if delete_btn:
        delete_btn.clicked.connect(on_delete_clicked)
    
    # --- Save-Button einbinden ---
    save_btn = winFindChild(window,QWidget, "saveBtnProjects")
    if save_btn:
        def on_save_clicked():
            projects_data = safe_load_json(projects_path, {})
            project_key = window.current_project_key  # <-- immer aktueller Key!
            project = projects_data[project_key]

            # Sammle alle Eingabewerte aus dem Fenster
            project.update(read_project_fields(window))

            # Speichere die Daten zurück
            safe_save_json(projects_path, projects_data)
            log_info(f"Projekt {project_key} erfolgreich gespeichert.")

        save_btn.clicked.connect(on_save_clicked)    

    return window

# Charakterfenster anzeigen
def show_characters_window(parent=None):
    window = DynamicWindow("characters_ui", UI_FILES["characters"], splitter_name="mainSplitter")
    window.show()

    # 1. Sprache ermitteln
    settings = load_settings()
    language = settings.get("language", "de")

    # 2. Daten laden
    character_path = Path("data/characters/data_characters.json")
    character_data = safe_load_json(character_path, {})

    # Wenn keine Charaktere vorhanden sind, einen leeren anlegen
    if not character_data:
        empty_char = get_empty_character()
        empty_char["character_ID"] = "1"
        character_data = {"character_ID_01": empty_char}
        safe_save_json(character_path, character_data)
        
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

    # Validator für Datumsfelder erstellen (wird für birth und died verwendet)
    regex = QRegularExpression(r"^\d{1,2}\.\d{1,2}\.\d{1,4}( v\. Chr\.)?$|^\d{1,4}( v\. Chr\.)?$")
    validator = QRegularExpressionValidator(regex)

    birthdate_edit = winFindChild(window,QLineEdit, "lineEditBorn")
    if birthdate_edit:
        birthdate_edit.setValidator(validator)
        birthdate_edit.setText(current_character.get("character_birthdate", ""))
        birthdate_edit.textChanged.connect(update_age_label)

    died_edit = winFindChild(window,QLineEdit, "lineEditDied")
    if died_edit:
        died_edit.setValidator(validator)
        died_edit.setText(current_character.get("character_died", ""))
        died_edit.textChanged.connect(update_age_label)

    # Alter berechnen
    birth_value = current_character.get("character_birthdate", "")
    died_value = current_character.get("character_died", "")
    age_value = calculate_age(birth_value, died_value)

    label_age = winFindChild(window,QLabel, "labelAgeValue")
    if label_age:
        label_age.setText(age_value)

    # Status
    status = load_translation(Path("core/translations/status.json"), language)
    combo_status = winFindChild(window,QComboBox, "comboBoxStatus")
    fill_combobox(combo_status, list(status.values()), current_character.get("character_status", 0))
    # 3. Geschlecht
    gender = load_translation(Path("core/translations/gender.json"), language)
    combo_gender = winFindChild(window,QComboBox, "comboBoxGender")
    fill_combobox(combo_gender, list(gender.values()), current_character.get("character_gender", 0))
    # 4. Sexualität
    sexual_orientation = load_translation(Path("core/translations/sex_orientation.json"), language)
    combo_sexual_orientation = winFindChild(window,QComboBox, "comboBoxSexOrientation")
    fill_combobox(combo_sexual_orientation, list(sexual_orientation.values()), current_character.get("character_sexOrientation", 0))
    # 5. Rolle 
    role = load_translation(Path("core/translations/role.json"), language)
    combo_role = winFindChild(window,QComboBox, "comboBoxRole")
    fill_combobox(combo_role, list(role.values()), current_character.get("character_role", 0))
    # 6. Gruppe
    group = load_translation(Path("core/translations/group.json"), language)
    combo_group = winFindChild(window,QComboBox, "comboBoxGroup")
    fill_combobox(combo_group, list(group.values()), current_character.get("character_group", 0))
    # 7. Körperbau
    body_type = load_translation(Path("core/translations/bodyType.json"), language)
    combo_body_type = winFindChild(window,QComboBox, "comboBoxBodyType")
    fill_combobox(combo_body_type, list(body_type.values()), current_character.get("character_bodyType", 0))
    # 8. Statur
    stature = load_translation(Path("core/translations/stature.json"), language)
    combo_stature = winFindChild(window,QComboBox, "comboBoxStature")
    fill_combobox(combo_stature, list(stature.values()), current_character.get("character_stature", 0))
    # 9. Gesichtsform
    face_shape = load_translation(Path("core/translations/faceShape.json"), language)
    combo_face_shape = winFindChild(window,QComboBox, "comboBoxFaceShape")
    fill_combobox(combo_face_shape, list(face_shape.values()), current_character.get("character_faceshape", 0))
    # 10. Augenform
    eye_shape = load_translation(Path("core/translations/eyeShape.json"), language)
    combo_eye_shape = winFindChild(window,QComboBox, "comboBoxEyeShape")
    fill_combobox(combo_eye_shape, list(eye_shape.values()), current_character.get("character_eyeshape", 0))

    # Felder setzen
    update_character_fields(window, current_character)


    # --- Save-Button einbinden ---
    save_btn = winFindChild(window,QWidget, "saveBtnCharacter")
    if save_btn:
        def on_save_clicked():
            character_data = safe_load_json(character_path, {})
            character_key = window.current_character_key
            character = character_data[character_key]
            character.update(read_character_fields(window))
            safe_save_json(character_path, character_data)
            log_info(f"Charakter {character_key} erfolgreich gespeichert.")

        save_btn.clicked.connect(on_save_clicked)

    # --- Daten löschen Button einbinden ---
    def on_delete_clicked():
        character_data = safe_load_json(character_path, {})
        character_key = window.current_character_key
        character_name = character_data[character_key].get("character_name", character_key)
        def delete_character():
            nonlocal character_data, character_key, character_name
            if character_key in character_data:
                del character_data[character_key]
                safe_save_json(character_path, character_data)
                log_info(f"Charakter {character_name} gelöscht.")
                # Nach dem Löschen: neuen Key setzen und Felder aktualisieren
                keys = list(character_data.keys())
                if keys:
                    idx = 0
                    if character_key in keys:
                        idx = keys.index(character_key)
                    elif window.current_character_key and window.current_character_key in keys:
                        idx = keys.index(window.current_character_key)
                    if idx >= len(keys):
                        idx = len(keys) - 1
                    window.current_character_key = keys[idx]
                    update_character_fields(window, character_data[window.current_character_key])
                else:
                    empty_char = get_empty_character()
                    update_character_fields(window, empty_char)
                    window.current_character_key = None
        if show_secure_dialog(window, action="delete_character", project_key=character_name):
            delete_character()

    delete_btn = winFindChild(window,QWidget, "deleteBtnCharacter")
    if delete_btn:
        delete_btn.clicked.connect(on_delete_clicked)

    # --- Neuen Charakter Button einbinden ---
    new_btn = winFindChild(window,QWidget, "newBtnCharacter")
    if new_btn:
        def on_new_clicked():
            character_data = safe_load_json(character_path, {})
            new_key, new_id = get_next_id(character_data, "character_ID_")
            empty_char = get_empty_character()
            empty_char["character_ID"] = new_id
            character_data[new_key] = empty_char
            safe_save_json(character_path, character_data)
            log_info(f"Neuer Charakter {new_key} erstellt.")
            window.current_character_key = new_key
            update_character_fields(window, empty_char)
        new_btn.clicked.connect(on_new_clicked)
         
    # --- nächster Charakter Button einbinden ---
    def on_next_clicked():
        character_data = safe_load_json(character_path, {})
        keys = list(character_data.keys())
        current_index = keys.index(window.current_character_key)
        next_index = (current_index + 1) % len(keys)
        next_key = keys[next_index]
        window.current_character_key = next_key
        next_character = character_data[next_key]
        update_character_fields(window, next_character)  # <--- Fenster übergeben!
    next_btn = winFindChild(window,QWidget, "nextBtnCharacter")
    if next_btn:
        next_btn.clicked.connect(on_next_clicked)

    def on_prev_clicked():
        character_data = safe_load_json(character_path, {})
        keys = list(character_data.keys())
        current_index = keys.index(window.current_character_key)
        prev_index = (current_index - 1) % len(keys)
        prev_key = keys[prev_index]
        window.current_character_key = prev_key
        prev_character = character_data[prev_key]
        update_character_fields(window, prev_character)  # <--- Fenster übergeben!
    prev_btn = winFindChild(window,QWidget, "previousBtnCharacter")
    if prev_btn:
        prev_btn.clicked.connect(on_prev_clicked)

    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnCharacter")
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

    log_info("Charakterfenster erfolgreich geladen und angezeigt.")
    return window

# Objektfenster anzeigen
def show_objects_window(parent=None):
    window = DynamicWindow("objects_ui", UI_FILES["objects"], splitter_name="mainSplitter")
    window.show()

    #1. Sprache ermitteln
    settings = load_settings()
    language = settings.get("language", "de")
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
    status = load_translation(Path("core/translations/status.json"), language)
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
    window = DynamicWindow("locations_ui", UI_FILES["locations"], splitter_name="mainSplitter")
    window.show()
    
    # 1. Sprache ermitteln
    settings = load_settings()
    language = settings.get("language", "de")
    # 2. Daten laden
    locations_path = Path("data/locations/data_locations.json")
    location_data = safe_load_json(locations_path, {})
    if not location_data:
        empty_location = get_empty_location()
        empty_location["location_ID"] = "1"
        location_data = {"location_ID_01": empty_location}
        safe_save_json(locations_path, location_data)
    first_key = next(iter(location_data.keys()))
    window.current_location_key = first_key
    current_location = location_data[window.current_location_key]
    # Felder setzen
    update_location_fields(window, current_location)
    # Status-ComboBox füllen
    status = load_translation(Path("core/translations/status.json"), language)
    combo_status = winFindChild(window, QComboBox, "comboBoxLocationsStatus")
    fill_combobox(combo_status, list(status.values()), current_location.get("location_status", 0) if isinstance(current_location, dict) else 0)
    # --- Save-Button einbinden ---
    save_btn = winFindChild(window,QWidget, "saveBtnLocations")
    if save_btn:
        def on_save_clicked():
            location_data = safe_load_json(locations_path, {})
            location_key = window.current_location_key
            loc = location_data.get(location_key, {})
            loc.update(read_location_fields(window))
            location_data[location_key] = loc
            safe_save_json(locations_path, location_data)
            log_info(f"Location {location_key} erfolgreich gespeichert.")

        save_btn.clicked.connect(on_save_clicked)
    # --- Neuen Location Button einbinden ---
    new_btn = winFindChild(window,QWidget, "newBtnLocations")
    if new_btn:
        def on_new_clicked():
            location_data = safe_load_json(locations_path, {})
            new_key, new_id = get_next_id(location_data, "location_ID_")
            empty_location = get_empty_location()
            empty_location["location_ID"] = new_id
            today = QDate.currentDate().toString("yyyy-MM-dd")
            empty_location["location_created"] = today
            empty_location["location_modified"] = today
            location_data[new_key] = empty_location
            safe_save_json(locations_path, location_data)
            log_info(f"Neue Location {new_key} erstellt.")
            window.current_location_key = new_key
            update_location_fields(window, empty_location)
        new_btn.clicked.connect(on_new_clicked)
    # --- nächster Location Button einbinden ---
    def on_next_clicked():
        location_data = safe_load_json(locations_path, {})
        keys = list(location_data.keys())
        current_index = keys.index(window.current_location_key)
        next_index = (current_index + 1) % len(keys)
        next_key = keys[next_index]
        window.current_location_key = next_key
        next_location = location_data[next_key]
        update_location_fields(window, next_location)
    next_btn = winFindChild(window,QWidget, "nextBtnLocations")
    if next_btn:
        next_btn.clicked.connect(on_next_clicked)
    # --- vorheriger Location Button einbinden ---
    def on_prev_clicked():
        location_data = safe_load_json(locations_path, {})
        keys = list(location_data.keys())
        current_index = keys.index(window.current_location_key)
        prev_index = (current_index - 1) % len(keys)
        prev_key = keys[prev_index]
        window.current_location_key = prev_key
        prev_location = location_data[prev_key]
        update_location_fields(window, prev_location)
    prev_btn = winFindChild(window,QWidget, "previousBtnLocations")
    if prev_btn:
        prev_btn.clicked.connect(on_prev_clicked)
    # --- Daten löschen Button einbinden ---
    def on_delete_clicked():
        location_data = safe_load_json(locations_path, {})
        location_key = window.current_location_key
        location_name = location_data[location_key].get("location_title", location_key)
        def delete_location():
            nonlocal location_data, location_key, location_name
            if location_key in location_data:
                del location_data[location_key]
                safe_save_json(locations_path, location_data)
                log_info(f"Location {location_name} gelöscht.")
                # Nach dem Löschen: neuen Key setzen und Felder aktualisieren
                keys = list(location_data.keys())
                if keys:
                    idx = 0
                    if location_key in keys:
                        idx = keys.index(location_key)
                    elif window.current_location_key and window.current_location_key in keys:
                        idx = keys.index(window.current_location_key)
                    if idx >= len(keys):
                        idx = len(keys) - 1
                    window.current_location_key = keys[idx]
                    update_location_fields(window, location_data[window.current_location_key])
                else:
                    empty_location = get_empty_location()
                    update_location_fields(window, empty_location)
                    window.current_location_key = None
        if show_secure_dialog(window, action="delete_location", project_key=location_name):
            delete_location()
    delete_btn = winFindChild(window,QWidget, "deleteBtnLocations")
    if delete_btn:
        delete_btn.clicked.connect(on_delete_clicked)
    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnLocations")
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

    log_info("Locationsfenster erfolgreich geladen und angezeigt.")
    return window

# Storylinefenster anzeigen
def show_storylines_window(parent=None):
    window = DynamicWindow("storylines_ui", UI_FILES["storylines"], splitter_name="mainSplitter")
    window.show()

    # 1. Sprache ermitteln
    settings = load_settings()
    language = settings.get("language", "de")
    # 2. Daten laden
    storylines_path = Path("data/storylines/data_storylines.json")
    storyline_data = safe_load_json(storylines_path, {})
    if not storyline_data:
        empty_storyline = get_empty_storyline()
        empty_storyline["storyline_ID"] = "1"
        storyline_data["storyline_ID_01"] = empty_storyline
        safe_save_json(storylines_path, storyline_data)
    first_key = next(iter(storyline_data.keys()))
    window.current_storyline_key = first_key
    current_storyline = storyline_data[window.current_storyline_key]
    # Felder setzen
    update_storyline_fields(window, current_storyline)
    # Status-ComboBox füllen
    status = load_translation(Path("core/translations/status.json"), language)
    combo_status = winFindChild(window, QComboBox, "comboBoxStorylinesStatus")
    fill_combobox(combo_status, list(status.values()), current_storyline.get("storyline_status", 0) if isinstance(current_storyline, dict) else 0)
    # --- Save-Button einbinden ---
    save_btn = winFindChild(window,QWidget, "saveBtnStorylines")
    if save_btn:
        def on_save_clicked():
            storyline_data = safe_load_json(storylines_path, {})
            storyline_key = window.current_storyline_key
            story = storyline_data.get(storyline_key, {})
            story.update(read_storyline_fields(window))
            storyline_data[storyline_key] = story
            safe_save_json(storylines_path, storyline_data)
            log_info(f"Storyline {storyline_key} erfolgreich gespeichert.")

        save_btn.clicked.connect(on_save_clicked)
    # --- Neuen Storyline Button einbinden ---
    new_btn = winFindChild(window,QWidget, "newBtnStorylines")
    if new_btn:
        def on_new_clicked():
            storyline_data = safe_load_json(storylines_path, {})
            new_key, new_id = get_next_id(storyline_data, "storyline_ID_")
            empty_storyline = get_empty_storyline()
            empty_storyline["storyline_ID"] = new_id
            today = QDate.currentDate().toString("yyyy-MM-dd")
            empty_storyline["storyline_created"] = today
            empty_storyline["storyline_modified"] = today
            storyline_data[new_key] = empty_storyline
            safe_save_json(storylines_path, storyline_data)
            log_info(f"Neue Storyline {new_key} erstellt.")
            window.current_storyline_key = new_key
            update_storyline_fields(window, empty_storyline)
        new_btn.clicked.connect(on_new_clicked)
    # --- nächster Storyline Button einbinden ---
    def on_next_clicked():
        storyline_data = safe_load_json(storylines_path, {})
        keys = list(storyline_data.keys())
        current_index = keys.index(window.current_storyline_key)
        next_index = (current_index + 1) % len(keys)
        next_key = keys[next_index]
        window.current_storyline_key = next_key
        next_storyline = storyline_data[next_key]
        update_storyline_fields(window, next_storyline)
    next_btn = winFindChild(window,QWidget, "nextBtnStorylines")
    if next_btn:
        next_btn.clicked.connect(on_next_clicked)
    # --- vorheriger Storyline Button einbinden ---
    def on_prev_clicked():
        storyline_data = safe_load_json(storylines_path, {})
        keys = list(storyline_data.keys())
        current_index = keys.index(window.current_storyline_key)
        prev_index = (current_index - 1) % len(keys)
        prev_key = keys[prev_index]
        window.current_storyline_key = prev_key
        prev_storyline = storyline_data[prev_key]
        update_storyline_fields(window, prev_storyline)
    prev_btn = winFindChild(window,QWidget, "previousBtnStorylines")
    if prev_btn:
        prev_btn.clicked.connect(on_prev_clicked)
    # --- Daten löschen Button einbinden ---
    def on_delete_clicked():
        storyline_data = safe_load_json(storylines_path, {})
        storyline_key = window.current_storyline_key
        storyline_name = storyline_data[storyline_key].get("storyline_title", storyline_key)
        def delete_storyline():
            nonlocal storyline_data, storyline_key, storyline_name
            if storyline_key in storyline_data:
                del storyline_data[storyline_key]
                safe_save_json(storylines_path, storyline_data)
                log_info(f"Storyline {storyline_name} gelöscht.")
                # Nach dem Löschen: neuen Key setzen und Felder aktualisieren
                keys = list(storyline_data.keys())
                if keys:
                    idx = 0
                    if storyline_key in keys:
                        idx = keys.index(storyline_key)
                    elif window.current_storyline_key and window.current_storyline_key in keys:
                        idx = keys.index(window.current_storyline_key)
                    if idx >= len(keys):
                        idx = len(keys) - 1
                    window.current_storyline_key = keys[idx]
                    update_storyline_fields(window, storyline_data[window.current_storyline_key])
                else:
                    empty_storyline = get_empty_storyline()
                    update_storyline_fields(window, empty_storyline)
                    window.current_storyline_key = None
        if show_secure_dialog(window, action="delete_storyline", project_key=storyline_name):
            delete_storyline()
    delete_btn = winFindChild(window,QWidget, "deleteBtnStorylines")
    if delete_btn:
        delete_btn.clicked.connect(on_delete_clicked)    
    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnStorylines")
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

    log_info("Storylinefenster erfolgreich geladen und angezeigt.")
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
                widget.setPlainText(str(value))
            elif isinstance(widget, QPlainTextEdit):
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
    plain_text_widget = winFindChild(window, QPlainTextEdit, "plainTextEditorScenePlainText")
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
    
    update_editor_info_labels(window, first_chapter)

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
                "scene_begin": today,
                "scene_edited": today,
                "scene_order": get_next_scene_order(chapter)
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
                        elif isinstance(widget, QPlainTextEdit):
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

# Anwendung starten
def main():
    setup_logging()
    log_header()
    log_info("Starte CSNova Anwendung")
    app = QApplication(sys.argv)

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
            start_window = show_start_window(settings)
        else:
            log_info("Lade Hauptfenster.")
            main_window = show_main_window()

        sys.exit(app.exec())

    except Exception as e:
        log_exception("Fehler beim Start der Anwendung", e)
        sys.exit(1)

if __name__ == "__main__":
    main()