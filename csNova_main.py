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
    QToolBar, QDockWidget, QDialog
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
        "object_status": (QComboBox, "comboBoxObjectStatus"),
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
        "location_title": (QLineEdit, "lineEditLocations"),
        "location_status": (QComboBox, "comboBoxLocationStatus"),
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
        "storyline_status": (QComboBox, "comboBoxStorylineStatus"),
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
        projects_btn.clicked.connect(lambda: show_projects_window(window))

    # Charakterfenster verbinden
    characters_btn = winFindChild(window,QWidget, "characterBtncsNovaMain")
    if characters_btn:
        characters_btn.clicked.connect(lambda: show_characters_window(window))

    # Objektfenster verbinden
    objects_btn = winFindChild(window,QWidget, "objectBtncsNovaMain")
    if objects_btn:
        objects_btn.clicked.connect(lambda: show_objects_window(window))

    # Locationsfenster verbinden
    locations_btn = winFindChild(window,QWidget, "locationBtncsNovaMain")
    if locations_btn:
        locations_btn.clicked.connect(lambda: show_locations_window(window))

    # Storylinefenster verbinden
    storylines_btn = winFindChild(window,QWidget, "storylineBtncsNovaMain")
    if storylines_btn:
        storylines_btn.clicked.connect(lambda: show_storylines_window(window))

    # Editorfenster verbinden
    editor_btn = winFindChild(window,QWidget, "editorBtncsNovaMain")
    if editor_btn:
        editor_btn.clicked.connect(lambda: show_editor_window(window))

    # Preferences-Button verbinden
    preferences_btn = winFindChild(window,QWidget, "preferencesBtncsNovaMain")
    if preferences_btn:
        preferences_btn.clicked.connect(lambda: show_preferences_window(window))

    # Hilfe-Button verbinden
    help_btn = winFindChild(window,QWidget, "helpBtncsNovaMain")
    if help_btn:
        help_btn.clicked.connect(lambda: show_help_window(window))

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
            new_id = f"project_ID_{len(projects_data) + 1:02d}"
            empty_project = get_empty_project()
            empty_project["project_ID"] = str(len(projects_data) + 1)
            projects_data[new_id] = empty_project
            safe_save_json(projects_path, projects_data)
            log_info(f"Neues Projekt {new_id} angelegt.")
            window.current_project_key = new_id
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
    if exit_btn:
        exit_btn.clicked.connect(window.close)
    
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
            new_id = f"character_ID_{len(character_data) + 1:02d}"
            empty_char = get_empty_character()
            empty_char["character_ID"] = str(len(character_data) + 1)
            character_data[new_id] = empty_char
            safe_save_json(character_path, character_data)
            log_info(f"Neuer Charakter {new_id} erstellt.")
            window.current_character_key = new_id
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
        exit_btn.clicked.connect(window.close)

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
    combo_status = winFindChild(window, QComboBox, "comboBoxObjectStatus")
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
            new_id = f"object_ID_{len(object_data) + 1:02d}"
            empty_object = get_empty_object()
            empty_object["object_ID"] = str(len(object_data) + 1)
            object_data[new_id] = empty_object
            safe_save_json(object_path, object_data)
            log_info(f"Neues Objekt {new_id} erstellt.")
            window.current_object_key = new_id
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
        exit_btn.clicked.connect(window.close)

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
    combo_status = winFindChild(window, QComboBox, "comboBoxLocationStatus")
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
            new_id = f"location_ID_{len(location_data) + 1:02d}"
            empty_location = get_empty_location()
            empty_location["location_ID"] = str(len(location_data) + 1)
            location_data[new_id] = empty_location
            safe_save_json(locations_path, location_data)
            log_info(f"Neue Location {new_id} erstellt.")
            window.current_location_key = new_id
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
        exit_btn.clicked.connect(window.close) 

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
    combo_status = winFindChild(window, QComboBox, "comboBoxStorylineStatus")
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
            new_id = f"storyline_ID_{len(storyline_data) + 1:02d}"
            empty_storyline = get_empty_storyline()
            empty_storyline["storyline_ID"] = str(len(storyline_data) + 1)
            storyline_data[new_id] = empty_storyline
            safe_save_json(storylines_path, storyline_data)
            log_info(f"Neue Storyline {new_id} erstellt.")
            window.current_storyline_key = new_id
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
        exit_btn.clicked.connect(window.close)

    log_info("Storylinefenster erfolgreich geladen und angezeigt.")
    return window

# Editorfenster anzeigen
def show_editor_window(parent=None):
    window = DynamicWindow("editor_ui", UI_FILES["editor"], splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnEditor")
    if exit_btn:
        exit_btn.clicked.connect(window.close)

    log_info("Editorfenster erfolgreich geladen und angezeigt.")
    return window

# Preferences-Fenster anzeigen
def show_preferences_window(parent=None):
    window = DynamicWindow("preferences_ui", UI_FILES["preferences"], splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnPreferences")
    if exit_btn:
        exit_btn.clicked.connect(window.close)

    log_info("Einstellungen-Fenster erfolgreich geladen und angezeigt.")
    return window

# Hilfe-Fenster anzeigen
def show_help_window(parent=None):
    window = DynamicWindow("help_ui", UI_FILES["help"], splitter_name="mainSplitter")
    window.show()

    # --- Exit-Button einbinden ---
    exit_btn = winFindChild(window,QWidget, "exitBtnHelp")
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