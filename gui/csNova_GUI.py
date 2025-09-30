from PySide6.QtWidgets import (
    QTabWidget, QCheckBox,
    QTextEdit, QFileDialog,
    QMainWindow, QLineEdit,
    QDateEdit, QFormLayout,
    QSpinBox, QLabel,
    QWidget, QVBoxLayout,
    QSplitter, QPushButton,
    QSpacerItem, QSizePolicy,
    QDialog, QHBoxLayout,
    QApplication, QComboBox,
    QListWidget, QToolBar, 
    QGroupBox, QDoubleSpinBox
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QPixmap, QIcon, QAction, QFont, QTextListFormat, QTextCharFormat
import json
import re
import os
from pathlib import Path
import datetime
from config.dev import GUI_DIR, ASSETS_DIR, DATA_DIR, USER_SETTINGS_FILE, FORM_FIELDS_FILE, BASE_STYLE_FILE, THEME_FILES, TRANSLATIONS_DIR
from core.logger import log_info, log_error, log_exception, log_call, log_debug
from gui.styles.python_gui_styles import apply_theme_style
from csNova import LANGUAGE_DEFAULTS, THEMES_STYLES_DEFAULTS, LANGUAGE_DATA_COMBOBOX_DEFAULTS

# Hilfsfunktion für Listen-Logging
def log_list(title, items):
    log_info(f"{title}:\n" + "\n".join(f"  - {item}" for item in items))

# Funktion zum Laden von JSON-Dateien
def load_json_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            log_info(f"Loaded JSON file: {path} ({len(data)} keys)")
        elif isinstance(data, list):
            log_info(f"Loaded JSON file: {path} ({len(data)} items)")
        else:
            log_info(f"Loaded JSON file: {path} (type: {type(data)})")
        return data
    except Exception as e:
        log_exception(f"Error loading JSON file: {path}", e)
        return {}

# Funktion zum Anwenden des globalen Stylesheets auf die QApplication    
def apply_global_stylesheet(app, base_style_path, theme):
    with open(base_style_path, "r", encoding="utf-8") as f:
        base_styles = json.load(f)

    stylesheet_parts = []
    for selector, rules in base_styles.items():
        rule_str = ""
        for prop, value in rules.items():
            # Rekursive Ersetzung aller Platzhalter
            while True:
                replaced = False
                for key, theme_value in theme.items():
                    placeholder = "{" + key + "}"
                    if placeholder in value:
                        value = value.replace(placeholder, str(theme_value))
                        replaced = True
                if not replaced:
                    break
            # Nach Ersetzung: Prüfen, ob noch Platzhalter übrig sind
            if "{" in value and "}" in value:
                log_error(f"Unresolved placeholder in StyleSheet: {value} (selector: {selector}, prop: {prop})")
                value = ""
            rule_str += f"{prop}: {value}; "
        stylesheet_parts.append(f"{selector} {{ {rule_str} }}")

    full_stylesheet = "\n".join(stylesheet_parts)
    app.setStyleSheet(full_stylesheet)
    log_info(f"Globales Stylesheet angewendet aus Theme: {theme.get('theme_name', 'Unbekannt')} und Datei: {base_style_path} ({len(stylesheet_parts)} CSS-Regeln)")
    log_debug(f"Theme-Preview: {theme}")

def format_date_local(date_str, lang="de"):
    import datetime
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        return date_str
    if lang == "de":
        return dt.strftime("%d.%m.%Y")
    elif lang == "en":
        return dt.strftime("%m/%d/%Y")
    elif lang in ("es", "fr"):
        return dt.strftime("%d/%m/%Y")
    else:
        return date_str

# StartWindow Klasse
class StartWindow(QMainWindow):

    # ... andere Methoden ...
    def update_scene_word_count(self):
        if "scene_word_count" in self.scene_form_widgets:
            widget = self.scene_form_widgets["scene_word_count"]
            text = self.scene_plain_editor.toPlainText() if hasattr(self, "scene_plain_editor") else ""
            word_count = len(text.split())
            if isinstance(widget, QLabel):
                widget.setText(str(word_count))
            elif isinstance(widget, QSpinBox):
                widget.setValue(word_count)

    # Initialisierung der Panels
    def create_left_panel_with_header(self, header_key, default_text):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(10, 10, 10, 10)
        panel_layout.setSpacing(10)
        panel_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        header_text = self.get_translation(header_key, default_text)
        header_label = QLabel(header_text, panel_widget)
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        header_label.setObjectName("LeftPanelHeaderLabel")
        panel_layout.addWidget(header_label)

        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        log_info(f"Left panel with header '{header_key}' erstellt (Default: '{default_text}')")
        return panel_widget

    # Anzeige des jeweils ausgewählten left_panels über die Buttons in right_panel_start
    def show_left_panel(self, panel_index, left_panel_functions):
        splitter = self.centralWidget()
        if isinstance(splitter, QSplitter):
            new_left_panel = left_panel_functions[panel_index]()
            old_left_panel = splitter.widget(0)
            splitter.insertWidget(0, new_left_panel)
            splitter.setStretchFactor(0, 1)
            if old_left_panel is not None:
                old_left_panel.setParent(None)
            self.left_panel_widget = new_left_panel
            self.safe_apply_theme_style(new_left_panel, "panel", self.theme)
            log_info(f"Left panel {panel_index} ({left_panel_functions[panel_index].__name__}) wurde angezeigt. Splitter-Größen: {splitter.sizes()}")
            # Splitter-Größen wiederherstellen
            splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
            splitter.setSizes(splitter_sizes)

    # Anzeige des jeweils ausgewählten center_panels über die Buttons in right_panel_start
    def create_center_panel_with_header(self, header_key, default_text):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(10, 10, 10, 10)
        panel_layout.setSpacing(10)
        panel_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        header_text = self.get_translation(header_key, default_text)
        header_label = QLabel(header_text, panel_widget)
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        header_label.setObjectName("CenterPanelHeaderLabel")
        panel_layout.addWidget(header_label)

        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        log_info(f"Center panel with header '{header_key}' erstellt (Default: '{default_text}')")
        return panel_widget
    
    # Anzeige des jeweils ausgewählten center_panels über die Buttons in right_panel_start
    def show_center_panel(self, panel_index, center_panel_functions):
        splitter = self.centralWidget()
        if isinstance(splitter, QSplitter):
            new_center_panel = center_panel_functions[panel_index]()
            old_center_panel = splitter.widget(1)
            splitter.insertWidget(1, new_center_panel)
            splitter.setStretchFactor(1, 1)
            if old_center_panel is not None:
                old_center_panel.setParent(None)
            self.center_panel_widget = new_center_panel
            self.safe_apply_theme_style(new_center_panel, "panel", self.theme)
            log_info(f"center panel {panel_index} ({center_panel_functions[panel_index].__name__}) wurde angezeigt. Splitter-Größen: {splitter.sizes()}")
            # Splitter-Größen wiederherstellen
            splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
            splitter.setSizes(splitter_sizes)
    
    # Right Panels mit den jeweiligen Buttons
    def create_right_panel_character(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("CharacterWinHeader", "Character Management")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("CharacterPanelHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # Button-Konfiguration: (Key, Hint-Key)
        button_keys = [
            ("botn_ch_01", "botn_ch_01_hint"),
            ("botn_ch_02a", "botn_ch_02b_hint"),
            ("botn_ch_02b", "botn_ch_02b_hint"),
            ("botn_ch_03", "botn_ch_03_hint"),
            ("botn_ch_04", "botn_ch_04_hint"),
            ("botn_ch_05", "botn_ch_05_hint"),
        ]
        for i, (key, hint_key) in enumerate(button_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, f"botn_ch_{i:02d}", btn)
            # Hier kannst du später die Button-Handler ergänzen

        panel_widget.setObjectName("CharacterRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        return panel_widget
    
    # Anzeige des jeweils ausgewählten right_panels über die Buttons in right_panel_start
    def show_right_panel(self, panel_index, right_panel_functions):
        splitter = self.centralWidget()
        if isinstance(splitter, QSplitter):
            new_right_panel = right_panel_functions[panel_index]()
            old_right_panel = splitter.widget(2)
            splitter.insertWidget(2, new_right_panel)
            splitter.setStretchFactor(2, 1)
            if old_right_panel is not None:
                old_right_panel.setParent(None)
            self.right_panel_widget = new_right_panel
            self.safe_apply_theme_style(new_right_panel, "panel", self.theme)
            log_info(f"right panel {panel_index} ({right_panel_functions[panel_index].__name__}) wurde angezeigt. Splitter-Größen: {splitter.sizes()}")
            # Splitter-Größen wiederherstellen
            splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
            splitter.setSizes(splitter_sizes)
    
    # Change Event
    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
                start_window = self.settings.setdefault("start_window", {})
                if self.isMaximized():
                    start_window["is_maximized"] = True
                    # Maximierte Größe NICHT speichern!
                else:
                    # Fenster wurde gerade von maximiert auf normal gesetzt
                    window_width = start_window.get("width", 1920)
                    window_height = start_window.get("height", 1080)
                    self.resize(window_width, window_height)
                    start_window["is_maximized"] = False
                    start_window["width"] = window_width
                    start_window["height"] = window_height
                with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                    json.dump(self.settings, f, indent=2, ensure_ascii=False)
                log_info(f"Fensterstatus geändert: Maximized={start_window['is_maximized']}, Größe={self.width()}x{self.height()}")
        super().changeEvent(event)
    
    # Sicherheitsabfrage beim Beenden des Programms
    @log_call
    def show_secure_exit_dialog(self):    
        dialog = QDialog(self)
        dialog.setWindowTitle(self.get_translation("WinStartTitle", "CSNova"))
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        # Sicherheitsabfrage-Text
        label = QLabel(self.get_translation("secureExitTitle", "Do you really want to exit CSNova"), dialog)
        label.setAlignment(Qt.AlignCenter)
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(label, "label", self.theme)
        layout.addWidget(label)

        # Buttons
        btn_layout = QHBoxLayout()
        btn_yes = QPushButton(self.get_translation("botn_yes", "Yes"), dialog)
        btn_no = QPushButton(self.get_translation("botn_no", "No"), dialog)
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(btn_yes, "button", self.theme)
            self.apply_theme_style(btn_no, "button", self.theme)
        btn_layout.addWidget(btn_yes)
        btn_layout.addWidget(btn_no)
        layout.addLayout(btn_layout)

        # Dialog-Panel Style
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(dialog, "panel", self.theme)

        # Button-Logik
        btn_yes.clicked.connect(self.close)
        btn_no.clicked.connect(dialog.reject)

        dialog.exec()
   
    # Fenstergröße wurde verändert
    def resizeEvent(self, event):
        super().resizeEvent(event)
        start_window = self.settings.setdefault("start_window", {})
        if not self.isMaximized():
            start_window["width"] = self.width()
            start_window["height"] = self.height()
            with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
            log_info(f"Fenstergröße geändert: {self.width()}x{self.height()}")

    # Funktion zum sicheren Abrufen von Übersetzungen
    def on_language_changed(self, index):
        # Hole den Sprachcode aus den Items oder einer Mapping-Liste
        language_codes = ["de", "en", "fr", "es"]  # Beispiel, passe ggf. an
        new_language = language_codes[index]  
        self.change_language(new_language)

    # Update Texte in Center_panel_start
    def update_center_panel_start_texts(self):
        # Header aktualisieren
        if hasattr(self, "header_label"):
            self.header_label.setText(self.get_translation("startWinInfoHeader", "Codices Scriptoria Nova <br><br>"))

        # Info-Label 1 aktualisieren
        if hasattr(self, "info_label1"):
            info_text1 = self.get_translation(
                "startWinInfoText1",
                "Thank you for choosing <b>CSNova</b>! <br><br>"
                "CSNova is an open-source project designed to help you organize and manage your creative writing projects. <br>"
                "You can customize the program to fit your workflow. Additionally, CSNova has a clear philosophy: <br>"
                "'You don't have to learn how the program works - the program should <b>understand</b> how you want to work.' <br><br>"
                "Before you get started, you can make some basic settings: <br><br>"
                "- Choose your preferred language. <br>"
                "- Choose a theme for CSNova to use. <br><br>"
            )
            self.info_label1.setText(info_text1)

        # Sprach-Label aktualisieren
        if hasattr(self, "language_label"):
            self.language_label.setText(self.get_translation("comboBox_se_01", "Language"))
            self.language_label.setToolTip(self.get_translation("comboBox_se_01_hint", "Select your language."))

        # Sprach-ComboBox aktualisieren
        if hasattr(self, "language_combo"):
            language_items = [
                self.get_translation(f"comboBox_se_01_item_{i}", f"Language {i+1}")
                for i in range(self.language_combo.count())
            ]
            for i, item in enumerate(language_items):
                self.language_combo.setItemText(i, item)
            self.language_combo.setToolTip(self.get_translation("comboBox_se_01_hint", "Select your language."))

        # Theme-Label aktualisieren
        if hasattr(self, "theme_label"):
            self.theme_label.setText(self.get_translation("comboBox_se_02", "Theme"))
            self.theme_label.setToolTip(self.get_translation("comboBox_se_02_hint", "Select the theme."))

        # Theme-ComboBox aktualisieren
        if hasattr(self, "theme_combo"):
            theme_items = [
                self.get_translation(f"comboBox_se_02_item_{i}", f"Theme {i+1}")
                for i in range(self.theme_combo.count())
            ]
            for i, item in enumerate(theme_items):
                self.theme_combo.setItemText(i, item)
            self.theme_combo.setToolTip(self.get_translation("comboBox_se_02_hint", "Select the theme."))

        # Info-Label 2 aktualisieren
        if hasattr(self, "info_label2"):
            info_text2 = self.get_translation(
                "startWinInfoText2",
                "You can also change these and other settings later in the settings. <br><br>"
                "Once you've made your selections - and are satisfied - click <b>Save</b><br><br>"
                "You can restore the default settings by clicking <b>Reset</b>. <br>"
                "Or simply click <b>Next</b> to continue. <br><br>"
            )
            self.info_label2.setText(info_text2)

        # Buttons aktualisieren
        if hasattr(self, "btn_save"):
            self.btn_save.setText(self.get_translation("btn_save", "Save"))
            self.btn_save.setToolTip(self.get_translation("btn_save_hint", "Here you can save the current settings."))
        if hasattr(self, "btn_reset"):
            self.btn_reset.setText(self.get_translation("btn_reset", "Reset"))
            self.btn_reset.setToolTip(self.get_translation("btn_reset_hint", "Here you can reset the settings to the default settings."))
        if hasattr(self, "btn_continue"):
            self.btn_continue.setText(self.get_translation("btn_next", "Next"))
            self.btn_continue.setToolTip(self.get_translation("btn_next_hint", "Here you can proceed to the next step."))

        # Fenster-Titel aktualisieren
        self.setWindowTitle(self.get_translation("WinStartTitle", "CSNova"))

    # Update Texte in Right_panel_start
    def update_right_panel_start_texts(self):
        # Header aktualisieren
        if hasattr(self, "right_panel_header_label"):
            self.right_panel_header_label.setText(self.get_translation("startWinHeader", "Project Overview <br>"))

        # Navigationselemente 1-8 aktualisieren
        nav_keys = [
            ("botn_st_01", "botn_st_01_hint"),
            ("botn_st_02", "botn_st_02_hint"),
            ("botn_st_03", "botn_st_03_hint"),
            ("botn_st_04", "botn_st_04_hint"),
            ("botn_st_05", "botn_st_05_hint"),
            ("botn_st_06", "botn_st_06_hint"),
            ("botn_st_07", "botn_st_07_hint"),
            ("botn_st_08", "botn_st_08_hint"),
            ("botn_st_09", "botn_st_09_hint"),
        ]
        for i, (key, hint_key) in enumerate(nav_keys, start=1):
            btn_attr = f"botn_st_{i:02d}"
            if hasattr(self, btn_attr):
                btn = getattr(self, btn_attr)
                btn.setText(self.get_translation(key, f"Button {i}"))
                btn.setToolTip(self.get_translation(hint_key, ""))

        # Navigationselement 9 (Exit) aktualisieren
        if hasattr(self, "botn_st_10"):
            self.botn_st_09.setText(self.get_translation("botn_st_10", "Exit"))
            self.botn_st_09.setToolTip(self.get_translation("botn_st_10_hint", "Exit CSNova."))

        # Fenster-Titel aktualisieren
        self.setWindowTitle(self.get_translation("WinStartTitle", "CSNova"))
   
    # Funktion wenn über language_combo die Sprache geändert wird
    def change_language(self, new_language):
        language_codes = ["de", "en", "fr", "es"]
        if hasattr(self, "language_combo"):
            try:
                index = language_codes.index(new_language)
                self.language_combo.blockSignals(True)
                self.language_combo.setCurrentIndex(index)
                self.language_combo.blockSignals(False)
            except ValueError:
                self.language_combo.blockSignals(True)
                self.language_combo.setCurrentIndex(0)
                self.language_combo.blockSignals(False)

        # Neue Übersetzungsdatei laden und speichern
        translation_data = LANGUAGE_DEFAULTS.get(new_language, {})
        translation_path = TRANSLATIONS_DIR / f"translation_{new_language}.json"
        try:
            with open(translation_path, "w", encoding="utf-8") as f:
                json.dump(translation_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neue Übersetzungsdatei gespeichert: {translation_path}")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Übersetzungsdatei: {translation_path}", e)
            return

        # Neue Übersetzungsdatei für die ComboBox-Daten laden und speichern
        combobox_translation_data = LANGUAGE_DATA_COMBOBOX_DEFAULTS.get(new_language, {})
        combobox_translation_path = TRANSLATIONS_DIR / f"translation_data_combobox_{new_language}.json"
        try:
            with open(combobox_translation_path, "w", encoding="utf-8") as f:
                json.dump(combobox_translation_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neue ComboBox-Übersetzungsdatei gespeichert: {combobox_translation_path}")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der ComboBox-Übersetzungsdatei: {combobox_translation_path}", e)
            return

        # Übersetzungen temporär anwenden
        self.translations = translation_data
        self.translations_combobox = combobox_translation_data
        self.language = new_language

        # Texte der Panels aktualisieren
        self.update_center_panel_start_texts()
        self.update_right_panel_start_texts()

        if hasattr(self, "btn_save"):
            self.btn_save.setEnabled(True)
        if hasattr(self, "btn_reset"):
            self.btn_reset.setEnabled(True)

    # Funktion, wenn das Theme in der theme_combo geändert wird
    def on_theme_changed(self, index):
        # Hole den Theme-Namen aus den Items oder einer Mapping-Liste
        theme_names = ["Modern_neutral", "Modern_dark", "Modern_light", 
                       "OldSchool_neutral", "OldSchool_dark", "OldSchool_light", 
                       "Vintage_neutral", "Vintage_dark", "Vintage_light", 
                       "Future_neutral", "Future_dark", "Future_light",
                       "Minimal_neutral", "Minimal_dark", "Minimal_light"]  # Beispiel, passe ggf. an
        new_theme_name = theme_names[index]  
        self.change_theme(new_theme_name)   

    # Mapping liste wie in on_theme_changed 
    def change_theme(self, new_theme_name):
        theme_names = ["Modern_neutral", "Modern_dark", "Modern_light", 
                       "OldSchool_neutral", "OldSchool_dark", "OldSchool_light", 
                       "Vintage_neutral", "Vintage_dark", "Vintage_light", 
                       "Future_neutral", "Future_dark", "Future_light",
                       "Minimal_neutral", "Minimal_dark", "Minimal_light"]  # Beispiel, passe ggf. an
        if hasattr(self, "theme_combo"):
            try:
                index = theme_names.index(new_theme_name)
                self.theme_combo.blockSignals(True)
                self.theme_combo.setCurrentIndex(index)
                self.theme_combo.blockSignals(False)
            except ValueError:
                self.theme_combo.blockSignals(True)
                self.theme_combo.setCurrentIndex(0)
                self.theme_combo.blockSignals(False)

        # Neue Theme-Datei laden und speichern
        theme_data = THEMES_STYLES_DEFAULTS.get(new_theme_name, {})
        theme_path = THEME_FILES.get(new_theme_name)
        if not theme_path:
            theme_path = GUI_DIR / "styles" / f"theme_{new_theme_name}.json"
        try:
            with open(theme_path, "w", encoding="utf-8") as f:
                json.dump(theme_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neue Theme-Datei gespeichert: {theme_path}")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Theme-Datei: {theme_path}", e)
            return

        # Theme temporär anwenden
        self.theme = theme_data
        self.theme["theme_name"] = new_theme_name  # Füge den Theme-Namen hinzu

        # Globales Stylesheet anwenden
        apply_global_stylesheet(QApplication.instance(), self.base_style_path, self.theme)

        # Panels neu erstellen mit dem neuen Theme
        self.init_ui()

        # Wenn das Theme geändert wurde, sind die Buttons btn_save und btn_reset aktiv
        if hasattr(self, "btn_save"):
            self.btn_save.setEnabled(True)
        if hasattr(self, "btn_reset"):
            self.btn_reset.setEnabled(True)
    
    # Sichere Anwendung des Theme-Stils mit Fehlerbehandlung
    def safe_apply_theme_style(self, widget, style_type, theme):
        try:
            if self.apply_theme_style and theme:
                self.apply_theme_style(widget, style_type, theme)
        except Exception as e:
            log_exception(f"Fehler beim Anwenden des Theme-Stils auf {widget.objectName()}", e)

    # Einstellungen speichern
    def save_settings(self):
        try:
            # Prüfe, ob die Einstellungen für Sprache und Theme gespeichert werden sollen
            first_start = self.settings.get("general", {}).get("first_start", True)
            if first_start:
                # 1. Sprache aus language_combo
                language_codes = ["de", "en", "fr", "es"]
                if hasattr(self, "language_combo"):
                    lang_index = self.language_combo.currentIndex()
                    language = language_codes[lang_index]
                    self.settings["general"]["language"] = language
                    # KEINE Pfade mehr speichern!

                # 2. Theme aus theme_combo
                theme_names = [
                    "Modern_neutral", "Modern_dark", "Modern_light",
                    "OldSchool_neutral", "OldSchool_dark", "OldSchool_light",
                    "Vintage_neutral", "Vintage_dark", "Vintage_light",
                    "Future_neutral", "Future_dark", "Future_light",
                    "Minimal_neutral", "Minimal_dark", "Minimal_light"
                ]
                if hasattr(self, "theme_combo"):
                    theme_index = self.theme_combo.currentIndex()
                    theme_name = theme_names[theme_index]
                    self.settings["gui"]["style_theme"] = theme_name
                    # KEINE Pfade mehr speichern!

            # Fensterstatus und Größe speichern
            start_window = self.settings.setdefault("start_window", {})
            start_window["is_maximized"] = self.isMaximized()
            if not self.isMaximized():
                start_window["width"] = self.width()
                start_window["height"] = self.height()

            # Splitter-Größen
            panels = self.settings.setdefault("panels", {})
            splitter = self.centralWidget()
            if isinstance(splitter, QSplitter):
                panels["splitter_sizes"] = splitter.sizes()

            # Speichern in user_settings.json (immer über USER_SETTINGS_FILE!)
            with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
            log_info("Einstellungen erfolgreich gespeichert.")
            if hasattr(self, "btn_save"):
                self.btn_save.setEnabled(False)
        except Exception as e:
            log_exception("Fehler beim Speichern der Einstellungen", e)

    # Einstellungen zurücksetzen
    def reset_settings(self):
        try:
            # Lade die gespeicherten Einstellungen neu
            with open(USER_SETTINGS_FILE, "r", encoding="utf-8") as f:
                saved_settings = json.load(f)

            # 1. Sprache zurücksetzen
            language = saved_settings["general"]["language"]
            self.change_language(language)

            # 2. Theme zurücksetzen
            theme_name = saved_settings["gui"]["style_theme"]
            self.change_theme(theme_name)

            log_info("Sprache und Theme wurden auf die gespeicherten Werte zurückgesetzt.")
            self.btn_reset.setEnabled(False)
            self.btn_save.setEnabled(False)
        except Exception as e:
            log_exception("Fehler beim Zurücksetzen der Einstellungen", e)

    # Wechsel zum nächsten Schritt
    def go_to_next_step(self):
        try:
            self.settings["general"]["first_start"] = False
            with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
            log_info('"first_start" wurde auf False gesetzt und Einstellungen gespeichert.')

            splitter = self.centralWidget()
            if isinstance(splitter, QSplitter):
                new_center_panel = self.create_center_panel_start()
                old_center_panel = splitter.widget(1)
                splitter.insertWidget(1, new_center_panel)
                splitter.setStretchFactor(1, 1)
                if old_center_panel is not None:
                    old_center_panel.setParent(None)
                self.center_panel_widget = new_center_panel

                # Splitter-Größen aus den Settings setzen und Speichern unterdrücken
                splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
                splitter.setSizes(splitter_sizes)
            else:
                self.center_panel_widget = self.create_center_panel_start()
                self.setCentralWidget(self.center_panel_widget)

            log_info("Center-Panel wurde nach Next-Step aktualisiert und korrekt angezeigt.")
        except Exception as e:
            log_exception("Fehler beim Wechsel zum nächsten Schritt", e)
    
    # PANELS FUNKTIONEN - LEFT_PANEL
    # .............................................................. 
    # Dieses left_panel_start wird beim Systemstart angezeigt und beinhaltet das Programmlogo
    # und grundelegende Informationen: (c), Version, Autor, Lizenz und evtl. weitere Hinweise.
    def create_left_panel_start(self, splitter_sizes):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(10, 10, 10, 10)
        panel_layout.setSpacing(10)
        panel_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        """ label = QLabel(self.get_translation("left_panel_label", "left_panel"), panel_widget)
        label.setAlignment(Qt.AlignCenter)
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(label, "label", self.theme)
        panel_layout.addWidget(label) """

        image_path = ASSETS_DIR / "media" / "Buchcover_csNova.png"
        image_label = QLabel(panel_widget)
        image_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        pixmap = QPixmap(str(image_path))
        image_label.setPixmap(pixmap)
        panel_layout.addWidget(image_label)
        panel_layout.setStretch(panel_layout.count() - 1, 1)

        log_info(f"Breite Originalbild: {pixmap.width()} - Höhe Originalbild: {pixmap.height()}")

        initial_width = splitter_sizes[0] - 20
        if not pixmap.isNull():
            aspect_ratio = pixmap.height() / pixmap.width()
            neue_Höhe = int(initial_width * aspect_ratio)
            log_info(f"Initial Breite left_panel (aus Settings): {initial_width}")
            log_info(f"Initial Höhe Bild: {neue_Höhe}")
            scaled_pixmap = pixmap.scaled(
                initial_width,
                neue_Höhe,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            image_label.setPixmap(scaled_pixmap)

        panel_widget.setObjectName("PicturePanel")
        self.safe_apply_theme_style(panel_widget, "panel", {**self.theme, "background": self.theme.get("nav_bg", self.theme.get("background"))})
        copyright_label = QLabel("v 0.0.9 <br>(c) 2025 - CSNova - Frank Reiser", panel_widget)
        copyright_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        panel_layout.addWidget(copyright_label, alignment=Qt.AlignBottom)

        # Dynamische Anpassung des Bildes bei Splitterbewegung
        def update_image_on_splitter_move(pos, index):
            breite_left_panel = panel_widget.width() - 20
            if not pixmap.isNull():
                aspect_ratio = pixmap.height() / pixmap.width()
                neue_Breite = max(breite_left_panel, 1)
                neue_Höhe = int(neue_Breite * aspect_ratio)
                scaled_pixmap = pixmap.scaled(
                    neue_Breite,
                    neue_Höhe,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                image_label.setPixmap(scaled_pixmap)
            else:
                log_error("Fehler: Pixmap ist null, Bild konnte nicht geladen werden.")
        return panel_widget, update_image_on_splitter_move
    
    # Dieses left_panel_editor wird im Editor-Modus angezeigt und beinhaltet
    # die Inhalte aus den Tabellen: Charaktere, Orte, Objekte, Kapitel, Szenen
    def create_left_panel_editor(self):
        # ComboBox mit Data_*.json Dateien
        # Lade alle Data_*.json Dateien aus dem data-Verzeichnis
        characters_data = load_json_file(DATA_DIR / "Character_main.json")
        objects_data = load_json_file(DATA_DIR / "Objects.json")
        locations_data = load_json_file(DATA_DIR / "Locations.json")
        storylines_data = load_json_file(DATA_DIR / "Storylines.json")
        # Speichere die Items für die ComboBoxen
        character_items = [char.get("name", "") for char in characters_data.values()]
        object_items = [obj.get("ob_title", "") for obj in objects_data.values()]
        location_items = [loc.get("lo_title", "") for loc in locations_data.values()]
        storyline_items = [st.get("st_title", "") for st in storylines_data.values()]

        panel_widget = QWidget()
        panel_widget.setMinimumWidth(220)  # Mindestbreite für das Panel
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(10, 10, 10, 10)
        panel_layout.setSpacing(10)
        panel_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        tab_widget = QTabWidget(panel_widget)
        tab_widget.setTabPosition(QTabWidget.West)
        tab_widget.setMovable(False)
        tab_widget.setUsesScrollButtons(True)
        tab_widget.setElideMode(Qt.ElideRight)
        tab_widget.tabBar().setStyleSheet("""
            QTabBar::tab {
                min-height: 180px;
                max-height: 200px;
                min-width: 12px;
                max-width: 18px;
            }
        """)

        # Szenen-Tab dynamisch mit Feldern aus form_fields.json
        scenes_tab = QWidget()
        scenes_layout = QFormLayout(scenes_tab)
        scenes_layout.setSpacing(8)

        scene_field_names = [
            "scene_id", "scene_title", "scene_premise", "scene_goal", "scene_conflict", "scene_outcome",
            "scene_type", "scene_mood", "scene_duration", "scene_characters_involved", "scene_objects_involved",
            "scene_location_ID", "scene_storyline_ID", "scene_word_count", "scene_notes", "scene_order",
            "scene_status", "scene_creation_date", "scene_last_modified", "scene_tags"
        ]

        with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
            form_fields = json.load(f)
        scene_fields = form_fields.get("scenes", [])

        self.scene_form_widgets = {}
        for field in scene_fields:
            field_name = field.get("datafield_name")
            if not field_name or field_name not in scene_field_names:
                continue  # Nur Felder aus scene_field_names verwenden!
            label_text = self.get_translation(field.get("label_key", field_name), field_name)
            field_type = field.get("type", "text")

            if field_name == "scene_word_count":
                # Immer nur ein Label, kein Eingabefeld!
                widget = QLabel(scenes_tab)
                widget.setText("0")
                scenes_layout.addRow(label_text, widget)
                self.scene_form_widgets[field_name] = widget
                continue  # Rest überspringen!
            label_text = self.get_translation(field.get("label_key", field_name), field_name)
            field_type = field.get("type", "text")

            if field_name == "scene_characters_involved":
                widget = QComboBox(scenes_tab)
                widget.addItems(character_items)
                widget.setEditable(True)
            elif field_name == "scene_objects_involved":
                widget = QComboBox(scenes_tab)
                widget.addItems(object_items)
                widget.setEditable(True)
            elif field_name == "scene_location_ID":
                widget = QComboBox(scenes_tab)
                widget.addItems(location_items)
                widget.setEditable(True)
            elif field_name == "scene_storyline_ID":
                widget = QComboBox(scenes_tab)
                widget.addItems(storyline_items)
                widget.setEditable(True)
            elif field_type == "text":
                widget = QLineEdit(scenes_tab)
            elif field_type == "spin":
                widget = QSpinBox(scenes_tab)
            elif field_type == "date":
                widget = QDateEdit(scenes_tab)
            else:
                widget = QLineEdit(scenes_tab)

            scenes_layout.addRow(label_text, widget)
            self.scene_form_widgets[field_name] = widget

        tab_widget.addTab(scenes_tab, self.get_translation("proj_cs_header", "Szenen"))

        # Weitere Tabs als Platzhalter
        tab_definitions = [
            ("storylines", "proj_st_header"),
            ("characters", "char_ma_header"),
            ("objects", "proj_ob_header"),
            ("locations", "proj_lo_header"),
        ]
        for tab_key, label_key in tab_definitions:
            tab = QWidget()
            tab_layout = QVBoxLayout(tab)
            tab_layout.setAlignment(Qt.AlignTop)
            tab_label_text = self.get_translation(label_key, tab_key.capitalize())
            tab_label_widget = QLabel(tab_label_text)
            tab_label_widget.setAlignment(Qt.AlignCenter)
            tab_layout.addWidget(tab_label_widget)
            tab_widget.addTab(tab, tab_label_text)    
         
        panel_layout.addWidget(tab_widget)
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(tab_widget, "tab", self.theme)
        log_info("Tab 'Szenen' im linken Editor-Panel mit dynamischen Feldern angezeigt.")
        return panel_widget
    
        
    # Dieses left_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitet wird.
    def create_left_panel_project(self):
        return self.create_left_panel_with_header("proj_ma_header", "Projects")
    
    # Dieses left_panel_settings wird angezeigt, wenn die Einstellungen geöffnet werden.
    def create_left_panel_settings(self):
        splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
        panel_widget, _ = self.create_left_panel_start(splitter_sizes)
        return panel_widget
        
    # Dieses left_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitet wird.
    def create_left_panel_character(self):
        return self.create_left_panel_with_header("char_ma_header", "Characteres")

    # Dieses left_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitet wird.
    def create_left_panel_location(self):
        return self.create_left_panel_with_header("proj_lo_header", "Locations")
    
    # Dieses left_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitet wird.
    def create_left_panel_object(self):
        return self.create_left_panel_with_header("proj_ob_header", "Objects")

    # Diese left_panel_storylines wird angezeigt, wenn eine Storyline erstellt oder bearbeitet wird.
    def create_left_panel_storylines(self):
        return self.create_left_panel_with_header("proj_st_header", "Storylines")
    
    # Dieses left_panel_help wird angezeigt, wenn die Hilfe geöffnet wird.
    # Es wird vorerst das gleiche Panel wie left_panel_start verwendet.
    def create_left_panel_help(self):
        splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
        panel_widget, _ = self.create_left_panel_start(splitter_sizes)
        return panel_widget
    
    # Dieses left_panel_about wird angezeigt, wenn "Über" geöffnet wird.
    # Es wird vorerst das gleiche Panel wie left_panel_start verwendet.
    def create_left_panel_about(self):
        splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
        panel_widget, _ = self.create_left_panel_start(splitter_sizes)
        return panel_widget
    
    # ..............................................................
    # PANELS FUNKTIONEN - CENTER_PANEL
    # ..............................................................
    # Dieses center_panel_start wird beim Systemstart angezeigt und beinhaltet
    # grundlegende Informationen und Anpassungsmöglichkeiten für die Einstellungen: Sprache und Theme
    def create_center_panel_start(self):
        first_start = self.general_settings.get("first_start", True)
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("startWinInfoHeader", "Codices Scriptoria Nova <br><br>")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)
        self.header_label = header_label

        if first_start:
            # Info-Text 1
            info_text1 = self.get_translation(
                "startWinInfoText1",
                "Thank you for choosing <b>CSNova</b>! <br><br>"
                "CSNova is an open-source project designed to help you organize and manage your creative writing projects. <br>"
                "You can customize the program to fit your workflow. Additionally, CSNova has a clear philosophy: <br>"
                "'You don't have to learn how the program works - the program should <b>understand</b> how you want to work.' <br><br>"
                "Before you get started, you can make some basic settings: <br><br>"
                "- Choose your preferred language. <br>"
                "- Choose a theme for CSNova to use. <br><br>"
            )
            info_label1 = QLabel(info_text1, panel_widget)
            info_label1.setWordWrap(True)
            info_label1.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            info_label1.setTextFormat(Qt.RichText)
            panel_layout.addWidget(info_label1)
            self.info_label1 = info_label1

            # Sprach-Label und ComboBox
            language_label = QLabel(self.get_translation("comboBox_se_01", "Language"), panel_widget)
            language_label.setToolTip(self.get_translation("comboBox_se_01_hint", "Select your language."))
            panel_layout.addWidget(language_label)
            self.language_label = language_label

            language_combo = QComboBox(panel_widget)
            language_items = [
                self.get_translation(f"comboBox_se_01_item_{i}", f"Language {i+1}")
                for i in range(4)
            ]
            language_combo.addItems(language_items)
            language_combo.setToolTip(self.get_translation("comboBox_se_01_hint", "Select your language."))
            panel_layout.addWidget(language_combo)
            self.language_combo = language_combo
            language_codes = ["de", "en", "fr", "es"]
            current_language = self.language  # z.B. "en"
            try:
                lang_idx = language_codes.index(current_language)
            except ValueError:
                lang_idx = 0
            self.language_combo.blockSignals(True)
            self.language_combo.setCurrentIndex(lang_idx)
            self.language_combo.blockSignals(False)
            self.language_combo.currentIndexChanged.connect(self.on_language_changed)

            # Theme-Label und ComboBox
            theme_label = QLabel(self.get_translation("comboBox_se_02", "Theme"), panel_widget)
            theme_label.setToolTip(self.get_translation("comboBox_se_02_hint", "Select the theme."))
            panel_layout.addWidget(theme_label)
            self.theme_label = theme_label

            theme_combo = QComboBox(panel_widget)
            theme_items = [
                self.get_translation(f"comboBox_se_02_item_{i}", f"Design {i+1}")
                for i in range(15)
            ]
            theme_combo.addItems(theme_items)
            theme_combo.setToolTip(self.get_translation("comboBox_se_02_hint", "Select the theme."))
            panel_layout.addWidget(theme_combo)
            self.theme_combo = theme_combo

            # Mapping-Liste für Theme-Namen
            theme_names = [
                "Modern_neutral", "Modern_dark", "Modern_light",
                "OldSchool_neutral", "OldSchool_dark", "OldSchool_light",
                "Vintage_neutral", "Vintage_dark", "Vintage_light",
                "Future_neutral", "Future_dark", "Future_light",
                "Minimal_neutral", "Minimal_dark", "Minimal_light"
            ]

            # Setze den aktuellen Theme-Index in der ComboBox
            current_theme_name = self.theme.get("theme_name", theme_names[0])
            try:
                idx = theme_names.index(current_theme_name)
            except ValueError:
                idx = 0
            self.theme_combo.blockSignals(True)
            self.theme_combo.setCurrentIndex(idx)
            self.theme_combo.blockSignals(False)
            self.theme_combo.currentIndexChanged.connect(self.on_theme_changed)

            # Info-Text 2
            info_text2 = self.get_translation(
                "startWinInfoText2",
                "You can also change these and other settings later in the settings. <br><br>"
                "Once you've made your selections - and are satisfied - click <b>Save</b><br><br>"
                "You can restore the default settings by clicking <b>Reset</b>. <br>"
                "Or simply click <b>Next</b> to continue. <br><br>"
            )
            info_label2 = QLabel(info_text2, panel_widget)
            info_label2.setWordWrap(True)
            info_label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            info_label2.setTextFormat(Qt.RichText)
            panel_layout.addWidget(info_label2)
            self.info_label2 = info_label2

            # Spacer, damit die Buttons weiter unten sind
            panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

            # Button-Bereich unten
            button_layout = QHBoxLayout()
            button_layout.setSpacing(16)

            # Speichern-Button
            btn_save_text = self.get_translation("btn_save", "Save")
            btn_save_hint = self.get_translation("btn_save_hint", "Here you can save the current settings.")
            self.btn_save = QPushButton(btn_save_text, panel_widget)
            self.btn_save.setToolTip(btn_save_hint)
            self.btn_save.clicked.connect(self.save_settings)
            self.btn_save.setEnabled(False)
            button_layout.addWidget(self.btn_save)

            # Standardeinstellungen-Button
            btn_reset_text = self.get_translation("btn_reset", "Reset")
            btn_reset_hint = self.get_translation("btn_reset_hint", "Here you can reset the settings to the default settings.")
            self.btn_reset = QPushButton(btn_reset_text, panel_widget)
            self.btn_reset.setToolTip(btn_reset_hint)
            self.btn_reset.clicked.connect(self.reset_settings)
            self.btn_reset.setEnabled(False)
            button_layout.addWidget(self.btn_reset)

            # Weiter-Button
            btn_continue_text = self.get_translation("btn_next", "Next")
            btn_continue_hint = self.get_translation("btn_next_hint", "Here you can proceed to the next step.")
            self.btn_continue = QPushButton(btn_continue_text, panel_widget)
            self.btn_continue.setToolTip(btn_continue_hint)
            self.btn_continue.clicked.connect(self.go_to_next_step)
            button_layout.addWidget(self.btn_continue)

            panel_layout.addLayout(button_layout)

            panel_widget.setObjectName("WelcomePanel")
            self.safe_apply_theme_style(panel_widget, "panel", {**self.theme, "background": self.theme.get("nav_bg", self.theme.get("background"))})

        else:
            info_text = self.get_translation(
                "startWinInfoTextReturn",
                "Welcome back to CSNova!\n\n"
            )
            info_label = QLabel(info_text, panel_widget)
            info_label.setWordWrap(True)
            info_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            info_label.setTextFormat(Qt.RichText)
            panel_layout.addWidget(info_label)
            self.header_label = header_label
            self.info_label = info_label

        return panel_widget
   
    # Dieses center_panel_editor wird im Editor-Modus angezeigt und beinhaltet
    # die Textverarbeitung für die Szenen usw.
    def create_center_panel_editor(self):
        """Zeigt Toolbar und Editorfenster für scene_plain an."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setAlignment(Qt.AlignTop)

        toolbar1 = QToolBar()
        toolbar2 = QToolBar()
        toolbar1_keys = [
            ("toolbar_ed_01", "toolbar_ed_01_hint", self.set_undone),         # Rückgängig
            ("toolbar_ed_02", "toolbar_ed_02_hint", self.set_redone),         # Wiederherstellen
            ("toolbar_ed_03", "toolbar_ed_03_hint", self.cut_text),           # Ausschneiden
            ("toolbar_ed_04", "toolbar_ed_04_hint", self.copy_text),          # Kopieren
            ("toolbar_ed_05", "toolbar_ed_05_hint", self.paste_text),         # Einfügen
            ("toolbar_ed_06", "toolbar_ed_06_hint", self.set_bold),           # Fett
            ("toolbar_ed_07", "toolbar_ed_07_hint", self.set_italic),         # Kursiv
            ("toolbar_ed_08", "toolbar_ed_08_hint", self.set_underline),      # Unterstrichen
            ("toolbar_ed_09", "toolbar_ed_09_hint", self.set_superscript),    # Hochgestellt
            ("toolbar_ed_10", "toolbar_ed_10_hint", self.set_subscript),      # Tiefgestellt
            ("toolbar_ed_15", "toolbar_ed_15_hint", self.insert_bullet_list), # Aufzählung
            ("toolbar_ed_16", "toolbar_ed_16_hint", self.insert_number_list), # Nummerierung

        ]
        for key, hint_key, handler in toolbar1_keys:
            action = QAction(self.get_translation(key, key), self)
            action.setToolTip(self.get_translation(hint_key, ""))
            action.triggered.connect(handler)
            toolbar1.addAction(action)

        toolbar2_keys = [
            ("toolbar_ed_11", "toolbar_ed_11_hint", self.set_left_align),     # Linksbündig
            ("toolbar_ed_12", "toolbar_ed_12_hint", self.set_center_align),   # Zentriert
            ("toolbar_ed_13", "toolbar_ed_13_hint", self.set_right_align),    # Rechtsbündig  
            #("toolbar_ed_14", "toolbar_ed_14_hint", self.set_justify_align),  # Blocksatz
            ("toolbar_ed_17", "toolbar_ed_17_hint", self.set_font_style),     # Schriftart
            ("toolbar_ed_18", "toolbar_ed_18_hint", self.set_font_size),      # Schriftgröße
            ("toolbar_ed_19", "toolbar_ed_19_hint", self.set_text_color),     # Textfarbe
            ("toolbar_ed_20", "toolbar_ed_20_hint", self.set_highlight_color),# Hervorheben
            #("toolbar_ed_21", "toolbar_ed_21_hint", self.insert_glossar),     # Glossar
            #("toolbar_ed_22", "toolbar_ed_22_hint", self.insert_tags),        # Tags
        ]
        for key, hint_key, handler in toolbar2_keys:
            action = QAction(self.get_translation(key, key), self)
            action.setToolTip(self.get_translation(hint_key, ""))
            action.triggered.connect(handler)
            toolbar2.addAction(action)


        layout.addWidget(toolbar1)
        layout.addWidget(toolbar2)

        # Editorfenster für scene_plain
        self.scene_plain_editor = QTextEdit(panel)
        self.scene_plain_editor.textChanged.connect(self.update_scene_word_count)
        self.scene_plain_editor.setObjectName("ScenePlainEditor")
        self.scene_plain_editor.setMinimumHeight(400)
        layout.addWidget(self.scene_plain_editor)

        self.safe_apply_theme_style(self.scene_plain_editor, "editor", self.theme)
        self.safe_apply_theme_style(toolbar1, "toolbar", self.theme)

        return panel

    # Methoden für die Toolbar-Buttons:
    # Text hochstellen
    def set_superscript(self):
        """Markierten Text hochstellen (Superscript)."""
        if hasattr(self, "scene_plain_editor"):
            cursor = self.scene_plain_editor.textCursor()
            fmt = cursor.charFormat()
            fmt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)
            cursor.mergeCharFormat(fmt)
    # Text tiefstellen
    def set_subscript(self):
        """Markierten Text tiefstellen (Subscript)."""
        if hasattr(self, "scene_plain_editor"):
            cursor = self.scene_plain_editor.textCursor()
            fmt = cursor.charFormat()
            fmt.setVerticalAlignment(QTextCharFormat.AlignSubScript)
            cursor.mergeCharFormat(fmt)
    # Text linksbündig
    def set_left_align(self):
        """Text linksbündig ausrichten."""
        if hasattr(self, "scene_plain_editor"):
            self.scene_plain_editor.setAlignment(Qt.AlignLeft)
    # Text zentriert
    def set_center_align(self):
        """Text zentriert ausrichten."""
        if hasattr(self, "scene_plain_editor"):
            self.scene_plain_editor.setAlignment(Qt.AlignCenter)
    # Text rechtsbündig
    def set_right_align(self):
        """Text rechtsbündig ausrichten."""
        if hasattr(self, "scene_plain_editor"):
            self.scene_plain_editor.setAlignment(Qt.AlignRight)
    # Text Blocksatz
    def set_justify_align(self):
        """Text im Blocksatz ausrichten."""
        if hasattr(self, "scene_plain_editor"):
            self.scene_plain_editor.setAlignment(Qt.AlignJustify)
    # Text undo
    def set_undone(self):
        """Rückgängig machen im Editor."""
        if hasattr(self, "scene_plain_editor"):
            self.scene_plain_editor.undo()
    # Text redo
    def set_redone(self):
        """Wiederherstellen im Editor."""
        if hasattr(self, "scene_plain_editor"):
            self.scene_plain_editor.redo()
    # Text fett 
    def set_bold(self):
        cursor = self.scene_plain_editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontWeight(QFont.Bold if fmt.fontWeight() != QFont.Bold else QFont.Normal)
        cursor.setCharFormat(fmt)
    # Text kursivscene_id", 
    def set_italic(self):
        cursor = self.scene_plain_editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        cursor.setCharFormat(fmt)
    # Text unterstrichen
    def set_underline(self):
        cursor = self.scene_plain_editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        cursor.setCharFormat(fmt)
    # Text Bullet-List
    def insert_bullet_list(self):
        cursor = self.scene_plain_editor.textCursor()
        cursor.beginEditBlock()
        # Wenn Text markiert ist, wandle die markierten Zeilen in eine Liste um
        if cursor.hasSelection():
            cursor.createList(QTextListFormat.ListDisc)
        else:
            cursor.insertList(QTextListFormat.ListDisc)
        cursor.endEditBlock()
    # Text Numbered-List
    def insert_number_list(self):
        cursor = self.scene_plain_editor.textCursor()
        cursor.beginEditBlock()
        if cursor.hasSelection():
            cursor.createList(QTextListFormat.ListDecimal)
        else:
            cursor.insertList(QTextListFormat.ListDecimal)
        cursor.endEditBlock()
    # Schriftart ändern
    def set_font_style(self):
        # Beispiel: Setze Schriftart auf Arial
        cursor = self.scene_plain_editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontFamily("Arial")
        cursor.setCharFormat(fmt)
    # Schriftgröße ändern
    def set_font_size(self):
        # Beispiel: Setze Schriftgröße auf 16
        cursor = self.scene_plain_editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setFontPointSize(16)
        cursor.setCharFormat(fmt)
    # Textfarbe ändern
    def set_text_color(self):
        # Beispiel: Setze Textfarbe auf Blau
        cursor = self.scene_plain_editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setForeground(Qt.blue)
        cursor.setCharFormat(fmt)
    # Text hervorheben
    def set_highlight_color(self):
        # Beispiel: Setze Hintergrundfarbe auf Gelb
        cursor = self.scene_plain_editor.textCursor()
        fmt = cursor.charFormat()
        fmt.setBackground(Qt.yellow)
        cursor.setCharFormat(fmt)
    # Text ausschneiden
    def cut_text(self):
        self.scene_plain_editor.cut()
    # Text kopieren
    def copy_text(self):
        self.scene_plain_editor.copy()
    # Text einfügen
    def paste_text(self):
        self.scene_plain_editor.paste()

    # Dieses center_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitet wird.
    def create_center_panel_project(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Infotext
        info_label = QLabel(self.get_translation("project_overview_info", "All your projects are listed here. You can create a new project, edit an existing one, or delete a project."), panel_widget)
        info_label.setWordWrap(True)
        panel_layout.addWidget(info_label)

        # Projektliste
        from PySide6.QtWidgets import QListWidget
        project_list = QListWidget(panel_widget)
        #project_list.setMaximumWidth(400)
        #project_list.setMaximumHeight(600)
        project_files = sorted(DATA_DIR.glob("Project_*.json"))
        for file in project_files:
            if file.is_file():
                project_list.addItem(file.name)
        panel_layout.addWidget(project_list)
        self.project_list_widget = project_list
        panel_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        panel_widget.setObjectName("ProjectOverviewPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)

        self.project_list_widget.itemSelectionChanged.connect(self.update_project_buttons_state)

        return panel_widget

    # Formular zur Erstellung oder Bearbeitung eines Projekts
    def create_center_panel_project_form(self, project_data=None):
        import re
        panel_widget = QWidget()
        main_layout = QHBoxLayout(panel_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(16)

        # Formular-Layout (links)
        form_layout = QFormLayout()
        form_layout.setSpacing(12)
        form_layout.setContentsMargins(0, 0, 0, 0)

        # Bild-Label (rechts oben)
        self.project_image_label = QLabel(panel_widget)
        self.project_image_label.setFixedSize(400, 600)  # Größe nach Wunsch anpassen

        # --- Bild setzen: Cover oder Platzhalter ---
        cover_path = None
        placeholder_path = DATA_DIR / "placeholder_cover.png"
        cover_value = ""
        if project_data and "project_cover_image" in project_data:
            cover_value = project_data["project_cover_image"]
            if cover_value:
                cover_path = Path(cover_value)
                if not cover_path.exists():
                    cover_path = None
        if (not cover_value or not cover_path) and placeholder_path.exists():
            cover_path = placeholder_path

        if cover_path and cover_path.exists():
            pixmap = QPixmap(str(cover_path))
            if not pixmap.isNull():
                self.project_image_label.setPixmap(
                    pixmap.scaled(
                        self.project_image_label.width(),
                        self.project_image_label.height(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                )
            else:
                self.project_image_label.clear()
        else:
            self.project_image_label.clear()

        # Felder laden
        with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
            form_fields = json.load(f)
        project_fields = form_fields.get("projects", [])

        self.project_form_widgets = {}

        # Für project_file: Dateiname automatisch bestimmen, falls leer
        def get_auto_data_filename(project_data):
            title = (project_data.get("project_title") or "").strip()
            start_date = (project_data.get("project_startdate") or "").strip()
            safe_title = re.sub(r'[^A-Za-z0-9_\-]', '_', title) or "Unbenannt"
            date_digits = re.sub(r'\D', '', start_date) or "00000000"
            return f"Data_{safe_title}_{date_digits}.json"

        for field in project_fields:
            field_name = field.get("datafield_name")
            if not field_name:
                continue

            label_key = field.get("label_key", field_name)
            label_text = self.get_translation(label_key, field_name)
            field_type = field.get("type", "text")
            width = field.get("width")

            # Spezialfall: project_cover_image mit Button
            if field_name == "project_cover_image":
                widget = QLineEdit(panel_widget)
                if width:
                    try:
                        widget.setFixedWidth(int(width))
                    except Exception:
                        pass
                btn = QPushButton(self.get_translation("btn_load_image", "Load image"), panel_widget)
                btn.setFixedWidth(200)
                btn.clicked.connect(lambda _, w=widget: self.load_image_for_field(w))

                hbox = QHBoxLayout()
                hbox.setContentsMargins(0, 0, 0, 0)
                hbox.setSpacing(6)
                hbox.setAlignment(Qt.AlignVCenter)
                hbox.addWidget(widget, alignment=Qt.AlignVCenter)
                hbox.addWidget(btn, alignment=Qt.AlignVCenter)
                container = QWidget(panel_widget)
                container.setLayout(hbox)
                form_layout.addRow(label_text, container)
                self.project_form_widgets[field_name] = widget

                # Wert beim Laden setzen
                if project_data and field_name in project_data:
                    widget.setText(project_data[field_name])
                continue

            # Spezialfall: project_file (readonly, automatisch setzen)
            if field_name == "project_file":
                widget = QLineEdit(panel_widget)
                widget.setReadOnly(True)
                if width:
                    try:
                        widget.setFixedWidth(int(width))
                    except Exception:
                        pass
                value = ""
                if project_data and field_name in project_data:
                    value = project_data[field_name]
                if not value:
                    # Automatisch passenden Dateinamen eintragen
                    value = get_auto_data_filename(project_data or {})
                widget.setText(value)
                form_layout.addRow(label_text, widget)
                self.project_form_widgets[field_name] = widget
                continue

            # Standard-Widget-Erstellung
            if field_type == "text":
                if field.get("multiline"):
                    widget = QTextEdit(panel_widget)
                    if width:
                        try:
                            widget.setFixedWidth(int(width))
                        except Exception:
                            pass
                    widget.setMinimumHeight(60)
                else:
                    widget = QLineEdit(panel_widget)
                    if width:
                        try:
                            widget.setFixedWidth(int(width))
                        except Exception:
                            pass
            elif field_type == "combobox":
                widget = QComboBox(panel_widget)
                combo_key = field.get("combo_key")
                if combo_key and self.combobox_translations:
                    items = list(self.combobox_translations.get(combo_key, {}).values())
                    widget.addItems(items)
                    if items:
                        widget.setCurrentIndex(len(items) - 1)
            elif field_type == "spin":
                widget = QSpinBox(panel_widget)
                widget.setMaximum(field.get("max", 1000000))
                widget.setSingleStep(10000)
                widget.setValue(10000)
            elif field_type == "date":
                widget = QDateEdit(panel_widget)
                widget.setCalendarPopup(True)
                today = datetime.date.today()
                widget.setDate(today)
                if self.language == "de":
                    widget.setDisplayFormat("dd.MM.yyyy")
                elif self.language == "en":
                    widget.setDisplayFormat("MM dd yyyy")
                elif self.language == "fr":
                    widget.setDisplayFormat("dd/MM/yyyy")
                elif self.language == "es":
                    widget.setDisplayFormat("dd/MM/yyyy")
                else:
                    widget.setDisplayFormat("yyyy-MM-dd")
            else:
                widget = QLineEdit(panel_widget)

            if width:
                try:
                    widget.setFixedWidth(int(width))
                except Exception:
                    pass

            # Felder befüllen, falls Daten vorhanden
            if project_data and field_name in project_data:
                value = project_data[field_name]
                if isinstance(widget, QLineEdit):
                    widget.setText(value)
                elif isinstance(widget, QTextEdit):
                    widget.setPlainText(value)
                elif isinstance(widget, QComboBox):
                    idx = widget.findText(value)
                    if idx >= 0:
                        widget.setCurrentIndex(idx)
                elif isinstance(widget, QSpinBox):
                    try:
                        widget.setValue(int(value))
                    except Exception:
                        pass
                elif isinstance(widget, QDateEdit):
                    try:
                        fmt = widget.displayFormat().replace("dd", "%d").replace("MM", "%m").replace("yyyy", "%Y")
                        date = datetime.datetime.strptime(value, fmt)
                        widget.setDate(date.date())
                    except Exception:
                        widget.setDate(datetime.date.today())

            # project_file immer readonly
            if field_name == "project_file":
                widget.setReadOnly(True)

            form_layout.addRow(label_text, widget)
            self.project_form_widgets[field_name] = widget

        # Layout zusammenbauen
        main_layout.addLayout(form_layout, stretch=3)
        main_layout.addWidget(self.project_image_label, stretch=1, alignment=Qt.AlignTop)

        panel_widget.setObjectName("ProjectFormPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        return panel_widget
    
    # Bild für project_cover_image laden
    def load_image_for_field(self, widget):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            self.get_translation("select_image", "Select an image"),
            "",
            "Bilder (*.png *.jpg *.jpeg *.bmp *.gif);;Alle Dateien (*)"
        )
        placeholder_path = DATA_DIR / "placeholder_cover.png"
        if file_path:
            widget.setText(file_path)
            if hasattr(self, "project_image_label"):
                pixmap = QPixmap(file_path)
                if not pixmap.isNull():
                    self.project_image_label.setPixmap(
                        pixmap.scaled(
                            self.project_image_label.width(),
                            self.project_image_label.height(),
                            Qt.KeepAspectRatio,
                            Qt.SmoothTransformation
                        )
                    )
                else:
                    # Bild nicht gefunden, Platzhalter anzeigen
                    if placeholder_path.exists():
                        pixmap = QPixmap(str(placeholder_path))
                        self.project_image_label.setPixmap(
                            pixmap.scaled(
                                self.project_image_label.width(),
                                self.project_image_label.height(),
                                Qt.KeepAspectRatio,
                                Qt.SmoothTransformation
                            )
                        )
                    else:
                        self.project_image_label.clear()
        else:
            # Kein Bild ausgewählt, Platzhalter anzeigen
            if hasattr(self, "project_image_label") and placeholder_path.exists():
                pixmap = QPixmap(str(placeholder_path))
                self.project_image_label.setPixmap(
                    pixmap.scaled(
                        self.project_image_label.width(),
                        self.project_image_label.height(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                )
            elif hasattr(self, "project_image_label"):
                self.project_image_label.clear()    
    
    # Dieses center_panel_settings wird angezeigt, wenn die Einstellungs-
    # Oberfläche geöffnet wird.
    def create_center_panel_settings(self):
        panel_widget = QWidget()
        main_layout = QVBoxLayout(panel_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(16)
        main_layout.setAlignment(Qt.AlignTop)

        tab_widget = QTabWidget(panel_widget)
        tab_widget.setTabPosition(QTabWidget.North)

        # --- Tab 1: Allgemein ---
        tab_general = QWidget()
        tab_general_layout = QVBoxLayout(tab_general)
        tab_general_layout.setAlignment(Qt.AlignTop)

        language_label_1 = QLabel(self.get_translation("comboBox_se_01", "Language"), tab_general)
        language_label_1.setToolTip(self.get_translation("comboBox_se_01_hint", "Select your language."))
        tab_general_layout.addWidget(language_label_1)

        language_combo_1 = QComboBox(tab_general)
        language_items_1 = [
            self.get_translation(f"comboBox_se_01_item_{i}", f"Language {i+1}")
            for i in range(4)
        ]
        language_combo_1.addItems(language_items_1)
        language_combo_1.setToolTip(self.get_translation("comboBox_se_01_hint", "Select your language."))
        tab_general_layout.addWidget(language_combo_1)

        language_codes = ["de", "en", "fr", "es"]
        current_language = self.language
        try:
            lang_idx = language_codes.index(current_language)
        except ValueError:
            lang_idx = 0
        language_combo_1.blockSignals(True)
        language_combo_1.setCurrentIndex(lang_idx)
        language_combo_1.blockSignals(False)
        language_combo_1.currentIndexChanged.connect(
            lambda idx: self.on_settings_language_changed(idx)
        )

        theme_label_1 = QLabel(self.get_translation("comboBox_se_02", "Theme"), tab_general)
        theme_label_1.setToolTip(self.get_translation("comboBox_se_02_hint", "Select the theme."))
        tab_general_layout.addWidget(theme_label_1)

        theme_combo_1 = QComboBox(tab_general)
        theme_items_1 = [
            self.get_translation(f"comboBox_se_02_item_{i}", f"Design {i+1}")
            for i in range(15)
        ]
        theme_combo_1.addItems(theme_items_1)
        theme_combo_1.setToolTip(self.get_translation("comboBox_se_02_hint", "Select the theme."))
        tab_general_layout.addWidget(theme_combo_1)

        theme_names = [
            "Modern_neutral", "Modern_dark", "Modern_light",
            "OldSchool_neutral", "OldSchool_dark", "OldSchool_light",
            "Vintage_neutral", "Vintage_dark", "Vintage_light",
            "Future_neutral", "Future_dark", "Future_light",
            "Minimal_neutral", "Minimal_dark", "Minimal_light"
        ]
        current_theme_name = self.theme.get("theme_name", theme_names[0])
        try:
            idx = theme_names.index(current_theme_name)
        except ValueError:
            idx = 0
        theme_combo_1.blockSignals(True)
        theme_combo_1.setCurrentIndex(idx)
        theme_combo_1.blockSignals(False)
        theme_combo_1.currentIndexChanged.connect(
            lambda idx: self.on_settings_theme_changed(idx)
        )

        tab_widget.addTab(tab_general, self.get_translation("tab_se_01", "General"))

        # --- Tab 2: Bücher ---
        tab_books = QWidget()
        tab_books_layout = QHBoxLayout(tab_books)
        tab_books_layout.setAlignment(Qt.AlignTop)

        with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
            form_fields = json.load(f)
        fiction_fields = form_fields.get("fiction_template", [])
        nonfiction_fields = form_fields.get("nonfiction_template", [])

        region_keys = ["EU", "USA", "UK"]
        region_items = [
            self.get_translation(f"books_combo_item_{i:02d}", f"Region {i}")
            for i in range(1, 4)
        ]

        # --- Fiktion-Container ---
        fiktion_group = QGroupBox(self.get_translation("settings_books_fiction", "Fiktion"), tab_books)
        fiktion_layout = QVBoxLayout(fiktion_group)
        fiktion_layout.setAlignment(Qt.AlignTop)

        self.fiktion_region_combo = QComboBox(fiktion_group)
        self.fiktion_region_combo.addItems(region_items)
        fiktion_layout.addWidget(self.fiktion_region_combo)

        fiktion_region = region_keys[0]
        fiktion_template = self.settings.get(fiktion_region, {}).get("fiction_template", {})
        fiktion_form_widget, self.romane_format_widgets = self.create_book_format_form(
            fiktion_group, fiction_fields, fiktion_template, region=fiktion_region
        )
        fiktion_layout.addWidget(fiktion_form_widget)
        fiktion_group.setMinimumWidth(260)
        tab_books_layout.addWidget(fiktion_group)

        # --- Non-Fiktion-Container ---
        nonfiktion_group = QGroupBox(self.get_translation("settings_books_nonfiction", "Non-Fiktion"), tab_books)
        nonfiktion_layout = QVBoxLayout(nonfiktion_group)
        nonfiktion_layout.setAlignment(Qt.AlignTop)

        self.nonfiktion_region_combo = QComboBox(nonfiktion_group)
        self.nonfiktion_region_combo.addItems(region_items)
        nonfiktion_layout.addWidget(self.nonfiktion_region_combo)

        nonfiktion_region = region_keys[0]
        nonfiktion_template = self.settings.get(nonfiktion_region, {}).get("nonfiction_template", {})
        nonfiktion_form_widget, self.sachbuch_format_widgets = self.create_book_format_form(
            nonfiktion_group, nonfiction_fields, nonfiktion_template, region=nonfiktion_region
        )
        nonfiktion_layout.addWidget(nonfiktion_form_widget)
        nonfiktion_group.setMinimumWidth(260)
        tab_books_layout.addWidget(nonfiktion_group)

        def update_fiktion_form(idx):
            region = region_keys[idx]
            template = self.settings.get(region, {}).get("fiction_template", {})
            for i in reversed(range(fiktion_layout.count())):
                widget = fiktion_layout.itemAt(i).widget()
                if widget and widget != self.fiktion_region_combo:
                    fiktion_layout.removeWidget(widget)
                    widget.deleteLater()
            new_form_widget, self.romane_format_widgets = self.create_book_format_form(
                fiktion_group, fiction_fields, template, region=region
            )
            fiktion_layout.addWidget(new_form_widget)

        def update_nonfiktion_form(idx):
            region = region_keys[idx]
            template = self.settings.get(region, {}).get("nonfiction_template", {})
            for i in reversed(range(nonfiktion_layout.count())):
                widget = nonfiktion_layout.itemAt(i).widget()
                if widget and widget != self.nonfiktion_region_combo:
                    nonfiktion_layout.removeWidget(widget)
                    widget.deleteLater()
            new_form_widget, self.sachbuch_format_widgets = self.create_book_format_form(
                nonfiktion_group, nonfiction_fields, template, region=region
            )
            nonfiktion_layout.addWidget(new_form_widget)

        self.fiktion_region_combo.currentIndexChanged.connect(update_fiktion_form)
        self.nonfiktion_region_combo.currentIndexChanged.connect(update_nonfiktion_form)

        tab_widget.addTab(tab_books, self.get_translation("tab_se_02", "Bücher"))

        for i in range(3, 7):
            tab_key = f"tab_se_{i:02d}"
            tab_hint_key = f"tab_se_{i:02d}_hint"
            tab_label = self.get_translation(tab_key, f"Tab {i}")
            tab_hint = self.get_translation(tab_hint_key, "")

            tab = QWidget()
            tab_layout = QVBoxLayout(tab)
            tab_layout.setAlignment(Qt.AlignTop)
            label = QLabel(tab_label, tab)
            label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            tab_layout.addWidget(label)

            tab_widget.addTab(tab, tab_label)
            tab_widget.setTabToolTip(i-1, tab_hint)

        main_layout.addWidget(tab_widget)
        panel_widget.setObjectName("PreferencesPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(tab_widget, "tab", self.theme)
        return panel_widget

    # Hilfsfunktion, um verschachtelte Werte aus einem Dictionary zu lesen
    def get_nested_value(self, settings, path):
        parts = path.split(".")
        value = settings
        for part in parts:
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return None
        return value

    # Formular für Buchformat-Einstellungen erstellen
    def create_book_format_form(self, parent, form_fields, template_settings, region="EU"):
        from PySide6.QtWidgets import QSizePolicy

        main_layout = QVBoxLayout()
        widgets = {}

        for field in form_fields:
            field_name = field.get("datafield_name")
            if not field_name:
                continue
            label_key = field.get("label_key", field_name)
            label_text = self.get_translation(label_key, field_name)
            field_type = field.get("type", "text")
            width = int(field.get("width", 60))
            unit = field.get("unit", "")

            # --- Regionale Umrechnung für US ---
            display_unit = unit
            if region == "USA" and unit == "cm":
                display_unit = "inch"

            row_widget = QWidget(parent)
            row_layout = QHBoxLayout(row_widget)
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(8)

            label = QLabel(label_text, parent)
            label.setMinimumWidth(250)
            label.setMaximumWidth(290)
            label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

            if field_type == "combobox":
                widget = QComboBox(parent)
                combo_key = field.get("combo_key")
                if combo_key and hasattr(self, "combobox_translations"):
                    combo_dict = self.combobox_translations.get(combo_key, {})
                    widget.clear()
                    for key, value in combo_dict.items():
                        widget.addItem(value, key)
                elif field_name == "family" or field_name == "font_family":
                    combo_dict = self.combobox_translations.get("font_family", {})
                    widget.clear()
                    for key, value in combo_dict.items():
                        widget.addItem(value, key)
                widget.setMinimumWidth(width)
                widget.setMaximumWidth(80)
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

                # Wert aus user_settings.json (template_settings) setzen
                value = self.get_nested_value(template_settings, field_name)
                if value is not None:
                    idx = widget.findData(str(value))
                    if idx >= 0:
                        widget.setCurrentIndex(idx)
                    else:
                        widget.addItem(str(value), str(value))
                        widget.setCurrentIndex(widget.count() - 1)

            elif field_type == "spin":
                is_float = field.get("float", False)
                if is_float:
                    widget = QDoubleSpinBox(parent)
                    widget.setDecimals(int(field.get("decimals", 2)))
                    widget.setMinimum(float(field.get("min", 0)))
                    widget.setMaximum(float(field.get("max", 100)))
                    widget.setSingleStep(float(field.get("step", 0.1)))
                else:
                    widget = QSpinBox(parent)
                    widget.setMinimum(int(field.get("min", 0)))
                    widget.setMaximum(int(field.get("max", 100)))
                    widget.setSingleStep(int(field.get("step", 1)))
            else:
                widget = QLineEdit(parent)

            widget.setMinimumWidth(width)
            widget.setMaximumWidth(60)
            widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

            value = self.get_nested_value(template_settings, field_name)
            if value is not None:
                if isinstance(widget, QSpinBox):
                    widget.setValue(int(float(value)))
                elif isinstance(widget, QDoubleSpinBox):
                    widget.setValue(float(value))
                elif isinstance(widget, QComboBox):
                    idx = widget.findText(str(value))
                    if idx >= 0:
                        widget.setCurrentIndex(idx)
                else:
                    widget.setText(str(value))
           
            unit_label = QLabel(display_unit, parent)
            unit_label.setMinimumWidth(20)
            unit_label.setMaximumWidth(30)
            unit_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

            row_layout.addWidget(label)
            row_layout.addWidget(widget)
            row_layout.addWidget(unit_label)
            row_layout.addStretch(1)

            main_layout.addWidget(row_widget)
            widgets[field_name] = widget

        container = QWidget(parent)
        container.setLayout(main_layout)
        return container, widgets
    
    # Sprache ändern in den Einstellungen
    def on_settings_language_changed(self, index):
        # Hole den Sprachcode aus den Items oder einer Mapping-Liste
        language_codes = ["de", "en", "fr", "es"]  # Beispiel, passe ggf. an
        new_language = language_codes[index]  
        self.settings_change_language(new_language)
    
    # Sprache ändern in den Einstellungen
    def settings_change_language(self, new_language):
        # Übersetzungen laden und anwenden
        translation_data = LANGUAGE_DEFAULTS.get(new_language, {})
        translation_path = TRANSLATIONS_DIR / f"translation_{new_language}.json"
        try:
            with open(translation_path, "w", encoding="utf-8") as f:
                json.dump(translation_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neue Übersetzungsdatei gespeichert: {translation_path}")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Übersetzungsdatei: {translation_path}", e)
            return

        combobox_translation_data = LANGUAGE_DATA_COMBOBOX_DEFAULTS.get(new_language, {})
        combobox_translation_path = TRANSLATIONS_DIR / f"translation_data_combobox_{new_language}.json"
        try:
            with open(combobox_translation_path, "w", encoding="utf-8") as f:
                json.dump(combobox_translation_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neue ComboBox-Übersetzungsdatei gespeichert: {combobox_translation_path}")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der ComboBox-Übersetzungsdatei: {combobox_translation_path}", e)
            return

        self.translations = translation_data
        self.combobox_translations = combobox_translation_data
        self.language = new_language

        # Panels gezielt neu erstellen (Settings-Panel bleibt aktiv!)
        self.update_center_panel_settings_texts()
        self.update_right_panel_settings_texts()

    # Aktualisiere die Texte im Center-Panel der Einstellungen
    def update_center_panel_settings_texts(self):
        splitter = self.centralWidget()
        if not isinstance(splitter, QSplitter):
            return
        center_panel = splitter.widget(1)
        if not center_panel:
            return

        tab_widget = center_panel.findChild(QTabWidget)
        if not tab_widget:
            return

        # --- Tab 1: Allgemein ---
        tab_general = tab_widget.widget(0)
        if tab_general:
            labels = tab_general.findChildren(QLabel)
            combos = tab_general.findChildren(QComboBox)
            # Sprache
            if len(labels) > 0:
                labels[0].setText(self.get_translation("comboBox_se_01", "Language"))
                labels[0].setToolTip(self.get_translation("comboBox_se_01_hint", "Select your language."))
            if len(combos) > 0:
                language_items = [
                    self.get_translation(f"comboBox_se_01_item_{i}", f"Language {i+1}")
                    for i in range(combos[0].count())
                ]
                for i, item in enumerate(language_items):
                    combos[0].setItemText(i, item)
                combos[0].setToolTip(self.get_translation("comboBox_se_01_hint", "Select your language."))
            # Theme
            if len(labels) > 1:
                labels[1].setText(self.get_translation("comboBox_se_02", "Theme"))
                labels[1].setToolTip(self.get_translation("comboBox_se_02_hint", "Select the theme."))
            if len(combos) > 1:
                theme_items = [
                    self.get_translation(f"comboBox_se_02_item_{i}", f"Design {i+1}")
                    for i in range(combos[1].count())
                ]
                for i, item in enumerate(theme_items):
                    combos[1].setItemText(i, item)
                combos[1].setToolTip(self.get_translation("comboBox_se_02_hint", "Select the theme."))

        # --- Tab 2: Bücher ---
        tab_books = tab_widget.widget(1)
        if tab_books:
            group_boxes = tab_books.findChildren(QGroupBox)
            if len(group_boxes) >= 2:
                group_boxes[0].setTitle(self.get_translation("settings_books_fiction", "Fiction"))
                group_boxes[1].setTitle(self.get_translation("settings_books_nonfiction", "Non-Fiction"))
                region_items = [
                    self.get_translation(f"books_combo_item_{i:02d}", f"Region {i}")
                    for i in range(1, 4)
                ]
                # Fiktion
                fiktion_combo = group_boxes[0].findChild(QComboBox)
                if fiktion_combo:
                    for i, item in enumerate(region_items):
                        fiktion_combo.setItemText(i, item)
                # Non-Fiktion
                nonfiktion_combo = group_boxes[1].findChild(QComboBox)
                if nonfiktion_combo:
                    for i, item in enumerate(region_items):
                        nonfiktion_combo.setItemText(i, item)
                # Formular für Fiktion neu aufbauen
                fiktion_combo = group_boxes[0].findChild(QComboBox)
                if fiktion_combo:
                    region_idx = fiktion_combo.currentIndex()
                    region_keys = ["EU", "USA", "UK"]
                    region = region_keys[region_idx]
                    with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                        form_fields = json.load(f)
                    fiction_fields = form_fields.get("fiction_template", [])
                    template = self.settings.get(region, {}).get("fiction_template", {})
                    fiktion_layout = group_boxes[0].layout()
                    for i in reversed(range(fiktion_layout.count())):
                        widget = fiktion_layout.itemAt(i).widget()
                        if widget and widget != fiktion_combo:
                            fiktion_layout.removeWidget(widget)
                            widget.deleteLater()
                    new_form_widget, self.romane_format_widgets = self.create_book_format_form(
                        group_boxes[0], fiction_fields, template, region=region
                    )
                    fiktion_layout.addWidget(new_form_widget)
                # Formular für Non-Fiktion neu aufbauen
                nonfiktion_combo = group_boxes[1].findChild(QComboBox)
                if nonfiktion_combo:
                    region_idx = nonfiktion_combo.currentIndex()
                    region_keys = ["EU", "USA", "UK"]
                    region = region_keys[region_idx]
                    with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                        form_fields = json.load(f)
                    nonfiction_fields = form_fields.get("nonfiction_template", [])
                    template = self.settings.get(region, {}).get("nonfiction_template", {})
                    nonfiktion_layout = group_boxes[1].layout()
                    for i in reversed(range(nonfiktion_layout.count())):
                        widget = nonfiktion_layout.itemAt(i).widget()
                        if widget and widget != nonfiktion_combo:
                            nonfiktion_layout.removeWidget(widget)
                            widget.deleteLater()
                    new_form_widget, self.sachbuch_format_widgets = self.create_book_format_form(
                        group_boxes[1], nonfiction_fields, template, region=region
                    )
                    nonfiktion_layout.addWidget(new_form_widget)

        # Tab-Titel und Tooltips
        for i in range(tab_widget.count()):
            tab_key = f"tab_se_{i+1:02d}"
            tab_label = self.get_translation(tab_key, f"Tab {i+1}")
            tab_widget.setTabText(i, tab_label)
            tab_hint_key = f"tab_se_{i+1:02d}_hint"
            tab_hint = self.get_translation(tab_hint_key, "")
            tab_widget.setTabToolTip(i, tab_hint)

    # Aktualisiere die Texte im Right-Panel der Einstellungen
    def update_right_panel_settings_texts(self):
        splitter = self.centralWidget()
        if not isinstance(splitter, QSplitter):
            return
        right_panel = splitter.widget(2)
        if not right_panel:
            return

        # Suche alle Buttons im Right-Panel
        buttons = right_panel.findChildren(QPushButton)
        # Die Reihenfolge entspricht der Reihenfolge in create_right_panel_settings
        button_keys = [
            ("botn_se_01", "botn_se_01_hint"),
            ("botn_se_02", "botn_se_02_hint"),
            ("botn_se_03", "botn_se_03_hint"),  # Back
        ]
        for i, (key, hint_key) in enumerate(button_keys):
            if i < len(buttons):
                btn = buttons[i]
                btn.setText(self.get_translation(key, key))
                btn.setToolTip(self.get_translation(hint_key, ""))

        # Header aktualisieren
        header_label = right_panel.findChild(QLabel, "FormHeaderLabel")
        if header_label:
            header_label.setText(self.get_translation("SettingsWinHeader", "Settings"))

    def on_settings_theme_changed(self, index):
        # Hole den Theme-Namen aus den Items oder einer Mapping-Liste
        theme_names = ["Modern_neutral", "Modern_dark", "Modern_light", 
                       "OldSchool_neutral", "OldSchool_dark", "OldSchool_light", 
                       "Vintage_neutral", "Vintage_dark", "Vintage_light", 
                       "Future_neutral", "Future_dark", "Future_light",
                       "Minimal_neutral", "Minimal_dark", "Minimal_light"]  # Beispiel, passe ggf. an
        new_theme_name = theme_names[index]  
        self.settings_change_theme(new_theme_name)   

    def settings_change_theme(self, new_theme_name):
        theme_names = ["Modern_neutral", "Modern_dark", "Modern_light", 
                       "OldSchool_neutral", "OldSchool_dark", "OldSchool_light", 
                       "Vintage_neutral", "Vintage_dark", "Vintage_light", 
                       "Future_neutral", "Future_dark", "Future_light",
                       "Minimal_neutral", "Minimal_dark", "Minimal_light"]  # Beispiel, passe ggf. an
        if hasattr(self, "theme_combo"):
            try:
                index = theme_names.index(new_theme_name)
                self.theme_combo_1.blockSignals(True)
                self.theme_combo_1.setCurrentIndex(index)
                self.theme_combo_1.blockSignals(False)
            except ValueError:
                self.theme_combo_1.blockSignals(True)
                self.theme_combo_1.setCurrentIndex(0)
                self.theme_combo_1.blockSignals(False)

        # Neue Theme-Datei laden und speichern
        theme_data = THEMES_STYLES_DEFAULTS.get(new_theme_name, {})
        theme_path = THEME_FILES.get(new_theme_name)
        if not theme_path:
            theme_path = GUI_DIR / "styles" / f"theme_{new_theme_name}.json"
        try:
            with open(theme_path, "w", encoding="utf-8") as f:
                json.dump(theme_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neue Theme-Datei gespeichert: {theme_path}")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Theme-Datei: {theme_path}", e)
            return

        # Theme temporär anwenden
        self.theme = theme_data
        self.theme["theme_name"] = new_theme_name  # Füge den Theme-Namen hinzu

        # Globales Stylesheet anwenden
        apply_global_stylesheet(QApplication.instance(), self.base_style_path, self.theme)
    
    # Dieses center_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitet wird.
    def create_center_panel_character(self, character_data=None):
        import datetime

        panel_widget = QWidget()
        main_layout = QVBoxLayout(panel_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        # --- OBERER BEREICH: Hauptcharakter, Name, Vorname ---
        top_form = QFormLayout()
        top_form.setSpacing(8)
        self.character_form_widgets = {}

        upper_fields = ["main_character", "name", "first_name"]
        with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
            form_fields = json.load(f)
        character_fields = form_fields.get("characters", [])

        for field in character_fields:
            field_name = field.get("datafield_name")
            if field_name not in upper_fields:
                continue
            label_key = field.get("label_key", field_name)
            label_text = self.get_translation(label_key, field_name)
            field_type = field.get("type", "text")
            width = field.get("width")
            # Widget-Auswahl
            if field_type == "checkbox":
                widget = QCheckBox(panel_widget)
            else:
                widget = QLineEdit(panel_widget)
            if width:
                try:
                    widget.setFixedWidth(int(width))
                except Exception:
                    pass
            top_form.addRow(label_text, widget)
            self.character_form_widgets[field_name] = widget

        main_layout.addLayout(top_form)

        # --- TAB-BEREICH ---
        tab_widget = QTabWidget(panel_widget)
        tab_widget.setTabPosition(QTabWidget.North)

        tab_definitions = [
            ("char_ma_01", ["nick_name", "born", "died", "role_ID", "group_ID", "char_image", "gender_ID", "sexual_orientation_ID", "status_ID", "notes"]),
            ("char_or_01", ["origin_father", "origin_mother", "origin_siblings", "origin_reference_person", "origin_place_of_birth", "origin_notes"]),
            ("char_ed_01", ["education_school", "education_university", "education_vocational_training", "education_self_tought", "education_profession", "education_art_music", "education_sports","education_technology","education_notes"]),
            ("char_am_01", ["appearance_Height", "appearance_Body_type", "appearance_Stature", "appearance_Face_shape", "appearance_Eye_shape", "appearance_Eye_color", "appearance_Hair", "appearance_Hair_color", "appearance_Skin", "appearance_Aura", "appearance_Special_features", "appearance_Notes"]),
            ("char_ad_01", ["appearance_details_Head", "appearance_details_Neck", "appearance_details_Shoulders", "appearance_details_Arms", "appearance_details_Hands", "appearance_details_Fingers", "appearance_details_Chest", "appearance_details_Hips_Waist", "appearance_details_Buttocks", "appearance_details_Legs", "appearance_details_Feet", "appearance_details_Toes","appearance_details_notes"]),
            ("char_ps_01", ["personality_Positive_trait", "personality_Negative_trait", "personality_Fears", "personality_Weaknesses", "personality_Strengths", "personality_Talents", "personality_Belief_principle", "personality_Life_goal", "personality_Motivation", "personality_Behavior", "personality_Notes"]),
            ("char_pp_01", ["psychlogical_profile_Diagnosis", "psychlogical_profile_Symptoms", "psychlogical_profile_Therapy", "psychlogical_profile_Medication", "psychlogical_profile_Temperament", "psychlogical_profile_Values", "psychlogical_profile_Moral_concepts", "psychlogical_profile_Character_strength", "psychlogical_profile_Character_weakness", "psychlogical_profile_Self_image", "psychlogical_profile_Humor", "psychlogical_profile_Aggressiveness", "psychlogical_profile_Trauma", "psychlogical_profile_Imprint", "psychlogical_profile_Socialization", "psychlogical_profile_Norms", "psychlogical_profile_Taboos", "psychlogical_profile_Notes"]),
        ]

        # Altersberechnung mit Validierung (außerhalb des Feld-Loops, damit sie immer existiert)
        def update_age(*args):
            born_widget = self.character_form_widgets.get("born")
            died_widget = self.character_form_widgets.get("died")
            age_label = self.character_form_widgets.get("char_age")
            if not born_widget or not age_label:
                return

            birthdate = None
            died_date = None

            # Unterstützte Formate je nach Sprache
            if self.language == "de":
                formats = ["%d.%m.%Y", "%Y-%m-%d"]
            elif self.language == "en":
                formats = ["%m %d %Y", "%Y-%m-%d"]
            elif self.language in ("fr", "es"):
                formats = ["%d/%m/%Y", "%Y-%m-%d"]
            else:
                formats = ["%Y-%m-%d"]

            # Geburtsdatum parsen
            born_text = born_widget.text().strip()
            for fmt in formats:
                try:
                    birthdate = datetime.datetime.strptime(born_text, fmt).date()
                    break
                except Exception:
                    continue

            # Sterbedatum parsen (kann leer sein)
            died_text = died_widget.text().strip() if died_widget else ""
            for fmt in formats:
                try:
                    died_date = datetime.datetime.strptime(died_text, fmt).date()
                    break
                except Exception:
                    continue

            # Visuelle Validierung
            if born_text and not birthdate:
                born_widget.setStyleSheet("background-color: #ffcccc;")
            else:
                born_widget.setStyleSheet("")
            if died_widget:
                if died_text and not died_date:
                    died_widget.setStyleSheet("background-color: #ffcccc;")
                else:
                    died_widget.setStyleSheet("")

            if not birthdate:
                age_label.setText("")
                return
            if died_text and not died_date:
                age_label.setText(self.get_translation("char_age_invalid", "Ungültiges Sterbedatum"))
                return

            if died_date:
                age = died_date.year - birthdate.year - ((died_date.month, died_date.day) < (birthdate.month, birthdate.day))
            else:
                today = datetime.date.today()
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            age_label.setText(str(age))

        for tab_key, tab_fields in tab_definitions:
            tab = QWidget()
            tab_layout = QFormLayout(tab)
            tab_layout.setSpacing(8)
            for field in character_fields:
                field_name = field.get("datafield_name")
                if not field_name or (tab_fields and field_name not in tab_fields):
                    continue
                label_key = field.get("label_key", field_name)
                label_text = self.get_translation(label_key, field_name)
                field_type = field.get("type", "text")
                width = field.get("width")

                # Spezialfall: born/died als QLineEdit mit Validierung
                if field_name in ("born", "died"):
                    widget = QLineEdit(panel_widget)
                    # Setze Platzhalter je nach Sprache
                    if self.language == "de":
                        widget.setPlaceholderText("TT.MM.JJJJ")
                    elif self.language == "en":
                        widget.setPlaceholderText("MM DD YYYY")
                    elif self.language in ("fr", "es"):
                        widget.setPlaceholderText("JJ/MM/JJJJ")
                    else:
                        widget.setPlaceholderText("YYYY-MM-DD")
                    if width:
                        try:
                            widget.setFixedWidth(int(width))
                        except Exception:
                            pass
                    tab_layout.addRow(label_text, widget)
                    self.character_form_widgets[field_name] = widget

                    # Alter-Label (nur einmal anlegen!)
                    if "char_age" not in self.character_form_widgets:
                        age_label = self.get_translation("char_ma_08", "Alter")
                        age_value_label = QLabel(panel_widget)
                        age_value_label.setObjectName("CharAgeLabel")
                        age_value_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                        tab_layout.addRow(age_label, age_value_label)
                        self.character_form_widgets["char_age"] = age_value_label

                    # Signals verbinden (erst nach dem Loop update_age aufrufen!)
                    if field_name == "born":
                        widget.textChanged.connect(update_age)
                    if field_name == "died":
                        widget.textChanged.connect(update_age)
                    continue

                # Standard-Widget-Erstellung
                if field_type == "checkbox":
                    widget = QCheckBox(panel_widget)
                elif field_type == "combobox":
                    widget = QComboBox(panel_widget)
                    combo_key = field.get("combo_key")
                    if combo_key and self.combobox_translations:
                        items = list(self.combobox_translations.get(combo_key, {}).values())
                        widget.addItems(items)
                elif field_type == "date":
                    widget = QDateEdit(panel_widget)
                    widget.setCalendarPopup(True)
                elif field.get("multiline"):
                    widget = QTextEdit(panel_widget)
                    widget.setMinimumHeight(60)
                else:
                    widget = QLineEdit(panel_widget)
                if width:
                    try:
                        widget.setFixedWidth(int(width))
                    except Exception:
                        pass
                tab_layout.addRow(label_text, widget)
                self.character_form_widgets[field_name] = widget

            tab_widget.addTab(tab, self.get_translation(tab_key, tab_key))

        main_layout.addWidget(tab_widget)
        panel_widget.setObjectName("CharacterFormPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)

        # Altersberechnung initial ausführen (nachdem alle Widgets existieren)
        update_age()

        # Optional: Formular mit Daten befüllen
        if character_data:
            self.fill_character_form(character_data)

        return panel_widget
   
    # Dieses center_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitet wird.
    def create_center_panel_object(self, object_data=None):
        panel_widget = QWidget()
        main_layout = QVBoxLayout(panel_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        # Formular-Layout
        form_layout = QFormLayout()
        form_layout.setSpacing(8)
        self.object_form_widgets = {}

        # Felder laden
        with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
            form_fields = json.load(f)
        object_fields = form_fields.get("objects", [])

        for field in object_fields:
            field_name = field.get("datafield_name")
            if not field_name:
                continue
            label_key = field.get("label_key", field_name)
            label_text = self.get_translation(label_key, field_name)
            field_type = field.get("type", "text")
            width = field.get("width")

            # Widget-Auswahl
            if field_type == "checkbox":
                widget = QCheckBox(panel_widget)
            elif field_type == "combobox":
                widget = QComboBox(panel_widget)
                combo_key = field.get("combo_key")
                if combo_key and self.combobox_translations:
                    items = list(self.combobox_translations.get(combo_key, {}).values())
                    widget.addItems(items)
            elif field_type == "date":
                widget = QDateEdit(panel_widget)
                widget.setCalendarPopup(True)
                widget.setDate(datetime.date.today())
            elif field.get("multiline"):
                widget = QTextEdit(panel_widget)
                widget.setMinimumHeight(60)
            else:
                widget = QLineEdit(panel_widget)
            if width:
                try:
                    widget.setFixedWidth(int(width))
                except Exception:
                    pass

            # Wert beim Laden setzen
            if object_data and field_name in object_data:
                value = object_data[field_name]
                if isinstance(widget, QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, QTextEdit):
                    widget.setPlainText(str(value))
                elif isinstance(widget, QComboBox):
                    idx = widget.findText(str(value))
                    if idx >= 0:
                        widget.setCurrentIndex(idx)
                elif isinstance(widget, QCheckBox):
                    widget.setChecked(bool(value))
                elif isinstance(widget, QDateEdit):
                    try:
                        widget.setDate(datetime.date.fromisoformat(value))
                    except Exception:
                        widget.setDate(datetime.date.today())

            form_layout.addRow(label_text, widget)
            self.object_form_widgets[field_name] = widget

        main_layout.addLayout(form_layout)
        panel_widget.setObjectName("ObjectFormPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        return panel_widget

    # Dieses center_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitet wird.
    def create_center_panel_location(self, location_data=None):
        panel_widget = QWidget()
        main_layout = QVBoxLayout(panel_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        # Formular-Layout
        form_layout = QFormLayout()
        form_layout.setSpacing(8)
        self.location_form_widgets = {}

        # Felder laden
        with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
            form_fields = json.load(f)
        location_fields = form_fields.get("locations", [])

        for field in location_fields:
            field_name = field.get("datafield_name")
            if not field_name:
                continue
            label_key = field.get("label_key", field_name)
            label_text = self.get_translation(label_key, field_name)
            field_type = field.get("type", "text")
            width = field.get("width")

            # Widget-Auswahl
            if field_type == "checkbox":
                widget = QCheckBox(panel_widget)
            elif field_type == "combobox":
                widget = QComboBox(panel_widget)
                combo_key = field.get("combo_key")
                if combo_key and self.combobox_translations:
                    items = list(self.combobox_translations.get(combo_key, {}).values())
                    widget.addItems(items)
            elif field_type == "date":
                widget = QDateEdit(panel_widget)
                widget.setCalendarPopup(True)
                widget.setDate(datetime.date.today())
            elif field.get("multiline"):
                widget = QTextEdit(panel_widget)
                widget.setMinimumHeight(60)
            else:
                widget = QLineEdit(panel_widget)
            if width:
                try:
                    widget.setFixedWidth(int(width))
                except Exception:
                    pass

            # Wert beim Laden setzen
            if location_data and field_name in location_data:
                value = location_data[field_name]
                if isinstance(widget, QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, QTextEdit):
                    widget.setPlainText(str(value))
                elif isinstance(widget, QComboBox):
                    idx = widget.findText(str(value))
                    if idx >= 0:
                        widget.setCurrentIndex(idx)
                elif isinstance(widget, QCheckBox):
                    widget.setChecked(bool(value))
                elif isinstance(widget, QDateEdit):
                    try:
                        widget.setDate(datetime.date.fromisoformat(value))
                    except Exception:
                        widget.setDate(datetime.date.today())

            form_layout.addRow(label_text, widget)
            self.location_form_widgets[field_name] = widget

        main_layout.addLayout(form_layout)
        panel_widget.setObjectName("LocationFormPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        return panel_widget

    # Dieses center_panel_storylines wird angezeigt, wenn die Storylines bearbeitet werden sollen.
    def create_center_panel_storylines(self, storyline_data=None):
        panel_widget = QWidget()
        main_layout = QVBoxLayout(panel_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(16)
        
        # Formular-Layout
        form_layout = QFormLayout()
        form_layout.setSpacing(8)
        self.storyline_form_widgets = {}

        # Felder laden
        with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
            form_fields = json.load(f)
        storyline_fields = form_fields.get("storylines", [])

        for field in storyline_fields:
            field_name = field.get("datafield_name")
            if not field_name:
                continue
            label_key = field.get("label_key", field_name)
            label_text = self.get_translation(label_key, field_name)
            field_type = field.get("type", "text")
            width = field.get("width")

            # Widget-Auswahl
            if field_type == "checkbox":
                widget = QCheckBox(panel_widget)
            elif field_type == "combobox":
                widget = QComboBox(panel_widget)
                combo_key = field.get("combo_key")
                if combo_key and self.combobox_translations:
                    items = list(self.combobox_translations.get(combo_key, {}).values())
                    widget.addItems(items)
            elif field_type == "date":
                widget = QDateEdit(panel_widget)
                widget.setCalendarPopup(True)
                widget.setDate(datetime.date.today())
            elif field.get("multiline"):
                widget = QTextEdit(panel_widget)
                widget.setMinimumHeight(60)
            else:
                widget = QLineEdit(panel_widget)
            if width:
                try:
                    widget.setFixedWidth(int(width))
                except Exception:
                    pass

            # Wert beim Laden setzen
            if storyline_data and field_name in storyline_data:
                value = storyline_data[field_name]
                if isinstance(widget, QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, QTextEdit):
                    widget.setPlainText(str(value))
                elif isinstance(widget, QComboBox):
                    idx = widget.findText(str(value))
                    if idx >= 0:
                        widget.setCurrentIndex(idx)
                elif isinstance(widget, QCheckBox):
                    widget.setChecked(bool(value))
                elif isinstance(widget, QDateEdit):
                    try:
                        widget.setDate(datetime.date.fromisoformat(value))
                    except Exception:
                        widget.setDate(datetime.date.today())

            form_layout.addRow(label_text, widget)
            self.storyline_form_widgets[field_name] = widget  

        main_layout.addLayout(form_layout)
        panel_widget.setObjectName("StorylineFormPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        return panel_widget  

    # Dieses center_panel_help wird angezeigt, wenn die Hilfe geöffnet wird.
    def create_center_panel_help(self):
        return self.create_center_panel_with_header("help_lp_header", "Help")
    
    # Dieses center_panel_about wird angezeigt, wenn "Über" geöffnet wird.
    def create_center_panel_about(self):
        return self.create_center_panel_with_header("abou_lp_header", "About")
    
    # ..............................................................
    # PANELS FUNKTIONEN - RIGHT_PANEL
    # ..............................................................
    # Dieses right_panel_start wird beim Systemstart angezeigt und beinhaltet
    # die Navigation zum Aufruf von: Editor, Projekt, Einstellungen, Hilfe, Über
    def show_start_panels(self):
        splitter = self.centralWidget()
        if isinstance(splitter, QSplitter):
            # Left Panel zurücksetzen
            splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
            new_left_panel, update_left_panel_image = self.create_left_panel_start(splitter_sizes)
            old_left_panel = splitter.widget(0)
            splitter.insertWidget(0, new_left_panel)
            splitter.setStretchFactor(0, 1)
            if old_left_panel is not None:
                old_left_panel.setParent(None)
            self.left_panel_widget = new_left_panel
            self.safe_apply_theme_style(new_left_panel, "panel", self.theme)

            # Center Panel zurücksetzen
            new_center_panel = self.create_center_panel_start()
            old_center_panel = splitter.widget(1)
            splitter.insertWidget(1, new_center_panel)
            splitter.setStretchFactor(1, 1)
            if old_center_panel is not None:
                old_center_panel.setParent(None)
            self.center_panel_widget = new_center_panel
            self.safe_apply_theme_style(new_center_panel, "panel", self.theme)

            # Right Panel zurücksetzen
            new_right_panel = self.create_right_panel_start()
            old_right_panel = splitter.widget(2)
            splitter.insertWidget(2, new_right_panel)
            splitter.setStretchFactor(2, 1)
            if old_right_panel is not None:
                old_right_panel.setParent(None)
            self.right_panel_widget = new_right_panel
            self.safe_apply_theme_style(new_right_panel, "panel", self.theme)

            # Splitter-Größen wiederherstellen
            splitter.setSizes(splitter_sizes)
            log_info("Alle Panels wurden auf die Startansicht zurückgesetzt.")

    # Dieses right_panel_start wird beim Systemstart angezeigt und beinhaltet
    # die Navigation zum Aufruf von: Editor, Projekt, Einstellungen, Hilfe, Über
    def create_right_panel_start(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("startWinHeader", "Project Overview <br>")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # Mapping: Button-Index zu left_panel-Funktion
        self.left_panel_functions = [
            self.create_left_panel_project,
            self.create_left_panel_character,
            self.create_left_panel_object,
            self.create_left_panel_location,
            self.create_left_panel_storylines,
            self.create_left_panel_editor,
            self.create_left_panel_settings,
            self.create_left_panel_help,
            self.create_left_panel_about,
        ]
        # Mapping: Button-Index zu center_panel-Funktion
        self.center_panel_functions = [
            self.create_center_panel_project,
            self.create_center_panel_character,
            self.create_center_panel_object,
            self.create_center_panel_location,
            self.create_center_panel_storylines,
            self.create_center_panel_editor,
            self.create_center_panel_settings,
            self.create_center_panel_help,
            self.create_center_panel_about,
        ]

        self.right_panel_functions = [
            self.create_right_panel_project,
            self.create_right_panel_character,
            self.create_right_panel_object,
            self.create_right_panel_location,
            self.create_right_panel_storylines,
            self.create_right_panel_editor,
            self.create_right_panel_settings,
            self.create_right_panel_help,
            self.create_right_panel_about,
        ]

        # Navigationselemente 1-9
        nav_keys = [
            ("botn_st_01", "botn_st_01_hint"),
            ("botn_st_02", "botn_st_02_hint"),
            ("botn_st_03", "botn_st_03_hint"),
            ("botn_st_04", "botn_st_04_hint"),
            ("botn_st_05", "botn_st_05_hint"),
            ("botn_st_06", "botn_st_06_hint"),
            ("botn_st_07", "botn_st_07_hint"),
            ("botn_st_08", "botn_st_08_hint"),
            ("botn_st_09", "botn_st_09_hint"),
        ]

        for i, (key, hint_key) in enumerate(nav_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, f"botn_st_{i:02d}", btn)
            # Button-Handler verbinden
            btn.clicked.connect(
                lambda checked, idx=i-1: (
                self.show_left_panel(idx, self.left_panel_functions),
                self.show_center_panel(idx, self.center_panel_functions),
                self.show_right_panel(idx, self.right_panel_functions)
            ))

        # Spacer, damit Button 9 unten ist
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Navigationselement 9 (unten)
        btn9_text = self.get_translation("botn_st_10", "Exit")
        btn9_hint = self.get_translation("botn_st_10_hint", "Exit CSNova.")
        btn9 = QPushButton(btn9_text, panel_widget)
        btn9.setToolTip(btn9_hint)
        btn9.clicked.connect(self.show_secure_exit_dialog)
        panel_layout.addWidget(btn9, alignment=Qt.AlignBottom)
        self.botn_st_09 = btn9

        panel_widget.setObjectName("NavigationPanelStart")
        self.safe_apply_theme_style(panel_widget, "panel", {**self.theme, "background": self.theme.get("nav_bg", self.theme.get("background"))})

        self.right_panel_header_label = header_label

        return panel_widget
 
    # Dieses right_panel_editor wird im Editor-Modus angezeigt und beinhaltet
    # die Navigation, ob in left_panel die Charaktere, Orte, Objekte, Kapitel oder Szenen angezeigt werden sollen.
    # Außerdem wird hier der Editor-Modus beendet.
    def create_right_panel_editor(self):
        panel_widget = QWidget()
        panel_widget.setMinimumWidth(220)
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Label für die ComboBox
        data_label = QLabel(self.get_translation("proj_ma_header", "Projekte"), panel_widget)
        data_label.setAlignment(Qt.AlignLeft)
        panel_layout.addWidget(data_label)

        # ComboBox mit allen Data_*.json Dateien
        data_combo = QComboBox(panel_widget)
        data_files = sorted([
            f for f in os.listdir(str(DATA_DIR))
            if f.startswith("Data_") and f.endswith(".json")
        ])
        data_combo.addItems(data_files)
        panel_layout.addWidget(data_combo)
        self.data_file_combo = data_combo

        # Aktives Item aus user_settings.json setzen
        last_file_opened = self.settings.get("general", {}).get("last_file_opened", "")
        if last_file_opened in data_files:
            idx = data_files.index(last_file_opened)
            data_combo.setCurrentIndex(idx)

        # Kapitel-Liste
        self.chapter_list_widget = QListWidget(panel_widget)
        self.chapter_list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        panel_layout.addWidget(self.chapter_list_widget)

        # Kapitel-Formular
        with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
            form_fields = json.load(f)
        chapter_fields = form_fields.get("chapters", [])

        self.chapter_form_widgets = {}
        chapter_form = QFormLayout()
        for field in chapter_fields:
            field_name = field.get("datafield_name")
            if not field_name:
                continue
            label_key = field.get("label_key", field_name)
            label_text = self.get_translation(label_key, field_name)
            field_type = field.get("type", "text")
            width = field.get("width")

            if field_type == "text":
                if field.get("multiline"):
                    widget = QTextEdit(panel_widget)
                    widget.setMinimumHeight(60)
                else:
                    widget = QLineEdit(panel_widget)
            elif field_type == "spin":
                widget = QSpinBox(panel_widget)
                widget.setMaximum(field.get("max", 1000000))
            elif field_type == "date":
                widget = QDateEdit(panel_widget)
                widget.setCalendarPopup(True)
                widget.setDate(datetime.date.today())
            else:
                widget = QLineEdit(panel_widget)

            if width:
                try:
                    widget.setFixedWidth(width)
                except Exception:
                    pass

            chapter_form.addRow(label_text, widget)
            self.chapter_form_widgets[field_name] = widget

        panel_layout.addLayout(chapter_form)

        # --- Button-Konfiguration: (Key, Hint-Key) ---
        button_keys = [
            ("botn_ed_01", "botn_ed_01_hint"),  # neues Kapitel 
            ("botn_ed_02", "botn_ed_02_hint"),  # vor
            ("botn_ed_03", "botn_ed_03_hint"),  # zurück
            ("botn_ed_04", "botn_ed_04_hint"),  # Speichern
        ]
        buttons = []
        for i, (key, hint_key) in enumerate(button_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, f"botn_ed_{i:02d}", btn)
            buttons.append(btn)

        # --- Daten aus gewählter Datei laden ---
        def load_data_file(idx):
            if 0 <= idx < len(data_files):
                filename = data_files[idx]
                data_path = DATA_DIR / filename
                if data_path.exists():
                    data = load_json_file(data_path)
                    chapters = {k: v for k, v in data.items() if k.startswith("chapter_ID_")}
                    self.chapter_data = chapters
                    self.chapter_list_widget.clear()
                    for chapter_id, chapter in chapters.items():
                        chapter_title = chapter.get("chapter_title", chapter_id)
                        self.chapter_list_widget.addItem(f"{chapter_id}: {chapter_title}")

                    # Lade das aktuell ausgewählte Kapitel
                    def fill_chapter_and_scene():
                        selected_items = self.chapter_list_widget.selectedItems()
                        if selected_items:
                            selected_chapter_id = selected_items[0].text().split(":")[0]
                        else:
                            selected_chapter_id = sorted(chapters.keys())[0] if chapters else None

                        if selected_chapter_id:
                            chapter = chapters[selected_chapter_id]
                            # Kapitel-Felder laden
                            for field_name, widget in self.chapter_form_widgets.items():
                                value = chapter.get(field_name, "")
                                if isinstance(widget, QLineEdit):
                                    widget.setText(str(value))
                                elif isinstance(widget, QTextEdit):
                                    widget.setPlainText(str(value))
                                elif isinstance(widget, QComboBox):
                                    idx = widget.findText(str(value))
                                    widget.setCurrentIndex(idx if idx >= 0 else 0)
                                elif isinstance(widget, QSpinBox):
                                    try:
                                        widget.setValue(int(value))
                                    except Exception:
                                        pass
                                elif isinstance(widget, QDateEdit):
                                    try:
                                        widget.setDate(datetime.date.fromisoformat(value))
                                    except Exception:
                                        widget.setDate(datetime.date.today())

                            # Szenen-Felder laden (ALLE Felder!)
                            scenes = chapter.get("scenes", {})
                            first_scene_id = sorted(scenes.keys())[0] if scenes else None
                            scene = scenes.get(first_scene_id, {}) if first_scene_id else {}
                            lang = self.settings.get("general", {}).get("language", "de")
                            for field_name, widget in getattr(self, "scene_form_widgets", {}).items():
                                value = scene.get(field_name, "")
                                if field_name in ("scene_creation_date", "scene_last_modified"):
                                    value = format_date_local(value, lang)
                                if isinstance(widget, QLineEdit):
                                    widget.setText(str(value))
                                elif isinstance(widget, QTextEdit):
                                    widget.setPlainText(str(value))
                                elif isinstance(widget, QComboBox):
                                    idx = widget.findText(str(value))
                                    widget.setCurrentIndex(idx if idx >= 0 else 0)
                                elif isinstance(widget, QSpinBox):
                                    try:
                                        widget.setValue(int(value))
                                    except Exception:
                                        pass
                                elif isinstance(widget, QDateEdit):
                                    # Setze das Anzeigeformat!
                                    if lang == "de":
                                        widget.setDisplayFormat("dd.MM.yyyy")
                                    elif lang == "en":
                                        widget.setDisplayFormat("MM dd yyyy")
                                    elif lang in ("fr", "es"):
                                        widget.setDisplayFormat("dd/MM/yyyy")
                                    else:
                                        widget.setDisplayFormat("yyyy-MM-dd")
                                    try:
                                        widget.setDate(datetime.date.fromisoformat(value))
                                    except Exception:
                                        widget.setDate(datetime.date.today())
                                elif isinstance(widget, QListWidget):
                                    widget.clear()
                                    if isinstance(value, list):
                                        for v in value:
                                            widget.addItem(str(v))
                                # Editor-Feld für scene_plain
                                if hasattr(self, "scene_plain_editor") and scene:
                                    self.scene_plain_editor.setPlainText(str(scene.get("scene_plain", "")))
                                    self.update_scene_word_count()

                    # Handler für Kapitel-Auswahl
                    self.chapter_list_widget.itemSelectionChanged.connect(fill_chapter_and_scene)
                    fill_chapter_and_scene()

                    # last_file_opened in user_settings.json aktualisieren
                    self.settings.setdefault("general", {})
                    self.settings["general"]["last_file_opened"] = filename
                    with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                        json.dump(self.settings, f, indent=2, ensure_ascii=False)
                data_combo.currentIndexChanged.connect(load_data_file)
        if data_files:
            load_data_file(data_combo.currentIndex())

        # --- Save-Handler für den Save-Button ---
        def save_chapter_data():
            idx = self.data_file_combo.currentIndex()
            if 0 <= idx < self.data_file_combo.count():
                filename = self.data_file_combo.itemText(idx)
                data_path = DATA_DIR / filename
                # Lade bestehende Daten
                data = load_json_file(data_path)
                chapters = {k: v for k, v in data.items() if k.startswith("chapter_ID_")}
                chapter_ids = sorted(chapters.keys())
                current_chapter_id = chapter_ids[0] if chapter_ids else "chapter_ID_01"
                chapter = chapters.get(current_chapter_id, {})

                # Felder aus Kapitel-Form speichern
                for field_name, widget in self.chapter_form_widgets.items():
                    if isinstance(widget, QLineEdit):
                        chapter[field_name] = widget.text()
                    elif isinstance(widget, QTextEdit):
                        chapter[field_name] = widget.toPlainText()
                    elif isinstance(widget, QComboBox):
                        chapter[field_name] = widget.currentText()
                    elif isinstance(widget, QSpinBox):
                        chapter[field_name] = widget.value()
                    elif isinstance(widget, QDateEdit):
                        chapter[field_name] = widget.date().toString("yyyy-MM-dd")

                # Szenen speichern (ALLE Felder aus scene_form_widgets + Editor)
                scenes = chapter.get("scenes", {})
                scene_ids = sorted(scenes.keys())
                current_scene_id = scene_ids[0] if scene_ids else "scene_ID_01"
                scene = scenes.get(current_scene_id, {})

                # Felder aus scene_form_widgets speichern
                for field_name, widget in getattr(self, "scene_form_widgets", {}).items():
                    if isinstance(widget, QLineEdit):
                        scene[field_name] = widget.text()
                    elif isinstance(widget, QTextEdit):
                        scene[field_name] = widget.toPlainText()
                    elif isinstance(widget, QComboBox):
                        scene[field_name] = widget.currentText()
                    elif isinstance(widget, QSpinBox):
                        scene[field_name] = widget.value()
                    elif isinstance(widget, QDateEdit):
                        scene[field_name] = widget.date().toString("yyyy-MM-dd")
                    elif isinstance(widget, QListWidget):
                        scene[field_name] = [widget.item(i).text() for i in range(widget.count()) if widget.item(i).isSelected()]

                # Editor-Inhalt speichern
                if hasattr(self, "scene_plain_editor"):
                    scene["scene_plain"] = self.scene_plain_editor.toPlainText()

                scenes[current_scene_id] = scene
                chapter["scenes"] = scenes
                chapters[current_chapter_id] = chapter

                # Schreibe alle Kapitel zurück in die Datei
                with open(data_path, "w", encoding="utf-8") as f:
                    json.dump(chapters, f, indent=2, ensure_ascii=False)

                # last_file_opened in user_settings.json aktualisieren
                self.settings.setdefault("general", {})
                self.settings["general"]["last_file_opened"] = filename
                with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                    json.dump(self.settings, f, indent=2, ensure_ascii=False)

        # Save-Button ist botn_ed_03
        self.botn_ed_04.clicked.connect(save_chapter_data)

        # Spacer, damit der Zurück-Button unten steht
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Zurück-Button
        btn_back_text = self.get_translation("botn_ed_05", "Back")
        btn_back_hint = self.get_translation("botn_ed_05_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_ed_05 = btn_back
        btn_back.clicked.connect(lambda: self.show_start_panels())

        panel_widget.setObjectName("EditorRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(data_label, "label", self.theme)
        return panel_widget
    
    # Dieses right_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitet wird.
    # Es beinhaltet die Navigation zu den verschiedenen Projekt-Einstellungen und beendet den Projekt-Modus.
    def create_right_panel_project(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("ProjectWinHeader", "Project Management")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # Button-Konfiguration: (Key, Hint-Key)
        button_keys = [
            ("botn_fo_01", "botn_fo_01_hint"),  # Neues Projekt
            ("botn_fo_02", "botn_fo_02_hint"),  # Projekt laden
            ("botn_fo_03", "botn_fo_03_hint"),  # Projekt speichern
            ("botn_fo_04", "botn_fo_04_hint"),  # Projekt löschen
        ]
        for i, (key, hint_key) in enumerate(button_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, f"botn_fo_{i:02d}", btn)

        # Buttons initial deaktivieren (außer "Neues Projekt")
        self.botn_fo_02.setEnabled(False)
        self.botn_fo_03.setEnabled(False)
        self.botn_fo_04.setEnabled(False)

        # Button-Handler verbinden
        self.botn_fo_01.clicked.connect(self.show_project_form_new)
        self.botn_fo_02.clicked.connect(self.show_project_form_load)
        self.botn_fo_03.clicked.connect(self.on_create_project_clicked)
        self.botn_fo_04.clicked.connect(self.delete_selected_project)

        # Spacer, damit der Zurück-Button unten steht
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Zurück-Button
        btn_back_text = self.get_translation("botn_fo_05", "Back")
        btn_back_hint = self.get_translation("botn_fo_05_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_fo_05 = btn_back
        btn_back.clicked.connect(lambda: self.show_start_panels())

        panel_widget.setObjectName("ProjectRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)

        # --- Projektliste-Selection-Handler verbinden ---
        if hasattr(self, "project_list_widget"):
            #self.project_list_widget.itemSelectionChanged.connect(self.update_project_buttons_state)
            self.update_project_buttons_state()  # Initialer Zustand

        return panel_widget
    
    # Dieses right_panel_settings wird angezeigt, wenn die Einstellungen bearbeitet werden sollen.
    # Es beinhaltet die Navigation zu den verschiedenen Einstellungs-Kategorien und beendet den Einstellungs-Modus.
    def create_right_panel_settings(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("SettingsWinHeader", "Settings")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # --- Save-Button ---
        btn_save_text = self.get_translation("botn_se_01", "Save")
        btn_save_hint = self.get_translation("botn_se_01_hint", "Save all settings.")
        btn_save = QPushButton(btn_save_text, panel_widget)
        btn_save.setToolTip(btn_save_hint)
        panel_layout.addWidget(btn_save)
        self.botn_se_01 = btn_save

        # --- Reset-Button ---
        btn_reset_text = self.get_translation("botn_se_02", "Reset")
        btn_reset_hint = self.get_translation("botn_se_02_hint", "Reset settings to default.")
        btn_reset = QPushButton(btn_reset_text, panel_widget)
        btn_reset.setToolTip(btn_reset_hint)
        panel_layout.addWidget(btn_reset)
        self.botn_se_02 = btn_reset

        # Spacer, damit der Zurück-Button unten steht
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # --- Back-Button ---
        btn_back_text = self.get_translation("botn_se_03", "Back")
        btn_back_hint = self.get_translation("botn_se_03_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_se_03 = btn_back

        # Handler für Zurück-Button: Panels zurücksetzen
        btn_back.clicked.connect(lambda: self.show_start_panels())

        # --- Save-Handler: Speichere die aktuellen Format-Keys aus Tab 2 ---
        def save_settings_and_formats():
            # --- Fiktion ---
            region_fiction = None
            if hasattr(self, "fiktion_region_combo"):
                region_idx = self.fiktion_region_combo.currentIndex()
                region_keys = ["EU", "USA", "UK"]
                region_fiction = region_keys[region_idx]


            # --- NonFiktion ---
            region_nonfiction = None
            if hasattr(self, "nonfiktion_region_combo"):
                region_idx = self.nonfiktion_region_combo.currentIndex()
                region_keys = ["EU", "USA", "UK"]
                region_nonfiction = region_keys[region_idx]


            # --- In user_settings.json speichern ---
            self.settings.setdefault("general", {})
            self.settings["general"]["last_fiction_region_used"] = region_fiction
            self.settings["general"]["last_nonfiction_region_used"] = region_nonfiction

            with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)


        btn_save.clicked.connect(save_settings_and_formats)
        btn_reset.clicked.connect(self.reset_settings)

        panel_widget.setObjectName("SettingsRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        return panel_widget
        
    # Dieses right_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitet wird.
    # Es beinhaltet die Navigation zu den verschiedenen Charakter-Einstellungen und beendet den Charakter-Modus.
    def create_right_panel_character(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        header_text = self.get_translation("CharacterWinHeader", "Character Management")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        button_keys = [
            ("botn_ch_01", "botn_ch_01_hint"),  # Neuer Charakter
            ("botn_ch_02a", "botn_ch_02a_hint"),  # Charakter vorheriger
            ("botn_ch_02b", "botn_ch_02b_hint"),  # Charakter nächster
            ("botn_ch_03", "botn_ch_03_hint"),  # Charakter speichern
            ("botn_ch_04", "botn_ch_04_hint"),  # Charakter löschen
            ("botn_ch_06", "botn_ch_06_hint"),  # Charakter Bild laden
        ]
        for idx, (key, hint_key) in enumerate(button_keys):
                btn_text = self.get_translation(key, key)
                btn_hint = self.get_translation(hint_key, "")
                btn = QPushButton(btn_text, panel_widget)
                btn.setToolTip(btn_hint)
                panel_layout.addWidget(btn)
                setattr(self, key, btn)
                # Nach botn_ch_06 einen größeren Abstand einfügen
                if key == "botn_ch_06":
                    spacer = QWidget()
                    spacer.setFixedHeight(36)
                    panel_layout.addWidget(spacer)

        # Spacer
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Zurück-Button
        btn_back_text = self.get_translation("botn_ch_05", "Back")
        btn_back_hint = self.get_translation("botn_ch_05_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_ch_05 = btn_back
        btn_back.clicked.connect(self.show_start_panels)

        # Button-Handler
        self.botn_ch_01.clicked.connect(self.on_new_character_clicked)
        self.botn_ch_02a.clicked.connect(self.on_previous_character_clicked)
        self.botn_ch_02b.clicked.connect(self.on_next_character_clicked)
        self.botn_ch_03.clicked.connect(self.on_save_character_clicked)
        self.botn_ch_04.clicked.connect(self.on_delete_character_clicked)

        panel_widget.setObjectName("CharacterRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        return panel_widget

    # Dieses right_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitet wird.
    # Es beinhaltet die Navigation zu den verschiedenen Ort-Einstellungen und beendet den Ort-Modus.
    def create_right_panel_location(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("LocationWinHeader", "Location Management")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # Button-Konfiguration: (Key, Hint-Key)
        button_keys = [
            ("botn_lo_01", "botn_lo_01_hint"),
            ("botn_lo_02a", "botn_lo_02a_hint"),
            ("botn_lo_02b", "botn_lo_02b_hint"),
            ("botn_lo_03", "botn_lo_03_hint"),
            ("botn_lo_04", "botn_lo_04_hint"),
        ]
        for i, (key, hint_key) in enumerate(button_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, key, btn)

        # Button-Handler verbinden
        self.botn_lo_01.clicked.connect(self.on_new_location_clicked)
        self.botn_lo_02a.clicked.connect(self.on_previous_location_clicked)
        self.botn_lo_02b.clicked.connect(self.on_next_location_clicked)
        self.botn_lo_03.clicked.connect(self.on_save_location_clicked)
        self.botn_lo_04.clicked.connect(self.on_delete_location_clicked)


        # Spacer, damit der Zurück-Button unten steht
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Zurück-Button
        btn_back_text = self.get_translation("botn_lo_05", "Back")
        btn_back_hint = self.get_translation("botn_lo_05_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_lo_05 = btn_back

        # Handler für Zurück-Button: Panels zurücksetzen
        btn_back.clicked.connect(lambda: self.show_start_panels())

        panel_widget.setObjectName("LocationRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        return panel_widget
    
    # Dieses right_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitet wird.
    # Es beinhaltet die Navigation zu den verschiedenen Objekt-Einstellungen und beendet den Objekt-Modus.
    def create_right_panel_object(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("ObjectWinHeader", "Object Management")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # Button-Konfiguration: (Key, Hint-Key)
        button_keys = [
            ("botn_ob_01", "botn_ob_01_hint"),  # Neu
            ("botn_ob_02a", "botn_ob_02a_hint"),  # Vorheriges
            ("botn_ob_02b", "botn_ob_02b_hint"),  # Nächstes
            ("botn_ob_03", "botn_ob_03_hint"),  # Speichern
            ("botn_ob_04", "botn_ob_04_hint"),  # Löschen
        ]
        for i, (key, hint_key) in enumerate(button_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, key, btn)

        # Button-Handler verbinden
        self.botn_ob_01.clicked.connect(self.on_new_object_clicked)
        self.botn_ob_02a.clicked.connect(self.on_previous_object_clicked)
        self.botn_ob_02b.clicked.connect(self.on_next_object_clicked)
        self.botn_ob_03.clicked.connect(self.on_save_object_clicked)
        self.botn_ob_04.clicked.connect(self.on_delete_object_clicked)

        # Spacer, damit der Zurück-Button unten steht
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Zurück-Button
        btn_back_text = self.get_translation("botn_ob_05", "Back")
        btn_back_hint = self.get_translation("botn_ob_05_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_ob_05 = btn_back

        # Handler für Zurück-Button: Panels zurücksetzen
        btn_back.clicked.connect(lambda: self.show_start_panels())

        panel_widget.setObjectName("ObjectRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        return panel_widget

    # Dieses right_panel_storylines wird angezeigt, wenn die Storylines bearbeitet werden sollen.
    def create_right_panel_storylines(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("StorylinesWinHeader", "Storylines")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # Button-Konfiguration: (Key, Hint-Key)
        button_keys = [
            ("botn_sl_01", "botn_sl_01_hint"),
            ("botn_sl_02", "botn_sl_02_hint"),
            ("botn_sl_03", "botn_sl_03_hint"),
            ("botn_sl_04", "botn_sl_04_hint"),
            ("botn_sl_05", "botn_sl_05_hint")
        ]

        for i, (key, hint_key) in enumerate(button_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, f"botn_sl_{i:02d}", btn)

        # Button-Handler verbinden (NACH der Schleife!)
        self.botn_sl_01.clicked.connect(self.on_new_storyline_clicked)
        self.botn_sl_02.clicked.connect(self.on_previous_storyline_clicked)
        self.botn_sl_03.clicked.connect(self.on_next_storyline_clicked)
        self.botn_sl_04.clicked.connect(self.on_save_storyline_clicked)
        self.botn_sl_05.clicked.connect(self.on_delete_storyline_clicked)
        
        # Handler für Zurück-Button: Panels zurücksetzen
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Zurück-Button
        btn_back_text = self.get_translation("botn_sl_06", "Back")
        btn_back_hint = self.get_translation("botn_sl_06_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_st_09 = btn_back

        # Handler für Zurück-Button: Panels zurücksetzen
        btn_back.clicked.connect(lambda: self.show_start_panels())

        panel_widget.setObjectName("StorylinesRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)

        return panel_widget 
    
    # Dieses right_panel_help wird angezeigt, wenn die Hilfe geöffnet wird.
    def create_right_panel_help(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("HelpWinHeader", "Help")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # Button-Konfiguration: (Key, Hint-Key)
        button_keys = [
            ("botn_he_01", "botn_he_01_hint"),
            ("botn_he_02", "botn_he_02_hint"),
            ("botn_he_03", "botn_he_03_hint"),
            ("botn_he_04", "botn_he_04_hint"),
        ]
        for i, (key, hint_key) in enumerate(button_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, f"botn_he_{i:02d}", btn)
            # Hier kannst du später die Button-Handler ergänzen

        # Spacer, damit der Zurück-Button unten steht
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Zurück-Button
        btn_back_text = self.get_translation("botn_he_05", "Back")
        btn_back_hint = self.get_translation("botn_he_05_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_he_05 = btn_back

        # Handler für Zurück-Button: Panels zurücksetzen
        btn_back.clicked.connect(lambda: self.show_start_panels())

        panel_widget.setObjectName("HelpRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        return panel_widget
    
    # Dieses right_panel_about wird angezeigt, wenn "Über" geöffnet wird.
    def create_right_panel_about(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("AboutWinHeader", "About")
        header_label = QLabel(header_text, panel_widget)
        header_label.setObjectName("FormHeaderLabel")
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        panel_layout.addWidget(header_label)

        # Button-Konfiguration: (Key, Hint-Key)
        button_keys = [
            ("botn_ab_01", "botn_ab_01_hint"),
            ("botn_ab_02", "botn_ab_02_hint"),
            ("botn_ab_03", "botn_ab_03_hint"),
            ("botn_ab_04", "botn_ab_04_hint"),
            ("botn_ab_05", "botn_ab_05_hint"),
            ("botn_ab_06", "botn_ab_06_hint"),
        ]
        for i, (key, hint_key) in enumerate(button_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, f"botn_ab_{i:02d}", btn)
            # Hier kannst du später die Button-Handler ergänzen

        # Spacer, damit der Zurück-Button unten steht
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Zurück-Button (Button 7)
        btn_back_text = self.get_translation("botn_ab_07", "Back")
        btn_back_hint = self.get_translation("botn_ab_07_hint", "Back to main navigation.")
        btn_back = QPushButton(btn_back_text, panel_widget)
        btn_back.setToolTip(btn_back_hint)
        panel_layout.addWidget(btn_back, alignment=Qt.AlignBottom)
        self.botn_ab_07 = btn_back

        # Handler für Zurück-Button: Panels zurücksetzen
        btn_back.clicked.connect(lambda: self.show_start_panels())

        panel_widget.setObjectName("AboutRightPanel")
        self.safe_apply_theme_style(panel_widget, "panel", self.theme)
        self.safe_apply_theme_style(header_label, "label", self.theme)
        return panel_widget
    
    # ..............................................................
    # Zentrale Funktionen
    # ..............................................................

    # Sichere Abfrage zum Löschen von Projekten, Charakteren, Objekten, Orten, Storylines
    def show_secure_delete_dialog(self, delete_type, delete_data=None):
        """
        Zentrale Sicherheitsabfrage zum Löschen von Projekten, Charakteren, Objekten, Orten, Storylines.
        delete_type: "project", "character", "object", "location", "storyline"
        delete_data: z.B. Dateiname, ID, etc.
        """
        dialog = QDialog(self)
        dialog.setWindowTitle(self.get_translation("WinStartTitle", "CSNova"))
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        # Übersetzungen holen
        title = self.get_translation("secureDeleteTitle", "Do you really want to delete the following entry?")
        type_label = {
            "project": self.get_translation("proj_ma_header", "Project"),
            "character": self.get_translation("char_ma_header", "Character"),
            "object": self.get_translation("proj_ob_header", "Object"),
            "location": self.get_translation("proj_lo_header", "Location"),
            "storyline": self.get_translation("proj_st_header", "Storyline"),
        }.get(delete_type, delete_type.capitalize())
        yes = self.get_translation("botn_yes", "Yes")
        no = self.get_translation("botn_no", "No")

        # Detailtext (z.B. Name)
        detail = str(delete_data) if delete_data else ""

        # Sicherheitsabfrage-Text
        label = QLabel(f"{title}<br><br><b>{type_label}:</b> {detail}", dialog)
        label.setAlignment(Qt.AlignCenter)
        label.setTextFormat(Qt.RichText)
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(label, "label", self.theme)
        layout.addWidget(label)

        # Buttons
        btn_layout = QHBoxLayout()
        btn_yes = QPushButton(yes, dialog)
        btn_no = QPushButton(no, dialog)
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(btn_yes, "button", self.theme)
            self.apply_theme_style(btn_no, "button", self.theme)
        btn_layout.addWidget(btn_yes)
        btn_layout.addWidget(btn_no)
        layout.addLayout(btn_layout)

        if self.apply_theme_style and self.theme:
            self.apply_theme_style(dialog, "panel", self.theme)

        # Button-Logik
        def on_yes():
            dialog.accept()
            if delete_type == "project":
                self._delete_project(delete_data)
            elif delete_type == "character":
                self._delete_character(delete_data)
            elif delete_type == "object":
                self._delete_object(delete_data)
            elif delete_type == "location":
                self._delete_location(delete_data)
            elif delete_type == "storyline":
                self._delete_storyline(delete_data)
            # ...weitere Typen...

        btn_yes.clicked.connect(on_yes)
        btn_no.clicked.connect(dialog.reject)

        dialog.exec()
    
    # Erzeugt und befüllt die Projekt-Liste aus dem DATA_DIR.
    def create_chapter_list_widget(self):
        # Erzeugt und befüllt die Kapitel-Liste aus Chapters_scenes.json.
        chapter_list = QListWidget()
        chapters_data = load_json_file(DATA_DIR / "Chapters_scenes.json")
        chapter_ids = list(chapters_data.keys())
        for chapter_id in chapter_ids:
            chapter_title = chapters_data[chapter_id].get("chapter_title", chapter_id)
            chapter_list.addItem(f"{chapter_id}: {chapter_title}")
        return chapter_list
    
    # ..............................................................
    # PROJEKT FUNKTIONEN
    # ..............................................................
    
    # Aktualisiere den Zustand der Projekt-Buttons basierend auf der Auswahl
    def update_project_buttons_state(self):
        # Stelle sicher, dass die Buttons existieren
        if not (hasattr(self, "botn_fo_02")
            and hasattr(self, "botn_fo_03") 
            and hasattr(self, "botn_fo_04")):
            return

        # Prüfe, ob Projekte vorhanden und eines ausgewählt ist
        has_projects = self.project_list_widget.count() > 0
        selected = self.project_list_widget.selectedItems()
        enable = bool(selected) and has_projects

        self.botn_fo_02.setEnabled(enable)  # Projekt laden
        self.botn_fo_03.setEnabled(False)   # Speichern bleibt deaktiviert bis Änderung
        self.botn_fo_04.setEnabled(enable)  # Projekt löschen 

    # Lege ein neues Projekt an
    def on_create_project_clicked(self):
        import datetime
        import re

        # 1. Daten auslesen
        project_data = {}
        for field_name, widget in self.project_form_widgets.items():
            if isinstance(widget, QLineEdit):
                project_data[field_name] = widget.text()
            elif isinstance(widget, QTextEdit):
                project_data[field_name] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                project_data[field_name] = widget.currentText()
            elif isinstance(widget, QSpinBox):
                project_data[field_name] = widget.value()
            elif isinstance(widget, QDateEdit):
                project_data[field_name] = widget.date().toString(widget.displayFormat())
            else:
                project_data[field_name] = ""

        # 2. Dateinamen bestimmen
        title = project_data.get("project_title", "").strip()
        start_date = project_data.get("project_startdate", "").strip()
        safe_title = re.sub(r'[^A-Za-z0-9_\-]', '_', title) or "Unbenannt"
        date_digits = re.sub(r'\D', '', start_date) or "00000000"
        filename = f"Project_{safe_title}_{date_digits}.json"
        filepath = DATA_DIR / filename

        # 2a. Data-Dateinamen IMMER im Projekt speichern!
        data_filename = f"Data_{safe_title}_{date_digits}.json"
        project_data["project_file"] = data_filename
        # UND im Formular anzeigen, falls Feld vorhanden:
        if "project_file" in self.project_form_widgets:
            widget = self.project_form_widgets["project_file"]
            if isinstance(widget, QLineEdit):
                widget.setText(data_filename)

        # 3. Speichern
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(project_data, f, ensure_ascii=False, indent=2)
        log_info(f"Projekt gespeichert: {filepath}")

        # --- NEU: Kapitel-/Szenendaten übernehmen und speichern ---
        chapters_file = DATA_DIR / "Chapters_scenes.json"
        if chapters_file.exists():
            with open(chapters_file, "r", encoding="utf-8") as f:
                chapters_data = json.load(f)
            data_filename = f"Data_{safe_title}_{date_digits}.json"
            data_filepath = DATA_DIR / data_filename
            with open(data_filepath, "w", encoding="utf-8") as f:
                json.dump(chapters_data, f, ensure_ascii=False, indent=2)
            log_info(f"Projekt-Kapitel/Szenen-Daten gespeichert: {data_filepath}")
        else:
            log_error(f"Kapitel-/Szenendatei nicht gefunden: {chapters_file}")

        # 4. Speichern-Button wieder deaktivieren
        self.botn_fo_03.setEnabled(False)
        self.show_center_panel(0, self.center_panel_functions)

    # Lade ein bestehendes Projekt
    def show_project_form_new(self):
        splitter = self.centralWidget()
        if isinstance(splitter, QSplitter):
            # Speichere aktuelle Splitter-Größen
            splitter_sizes = splitter.sizes()
            new_center_panel = self.create_center_panel_project_form()
            old_center_panel = splitter.widget(1)
            splitter.insertWidget(1, new_center_panel)
            splitter.setStretchFactor(1, 1)
            if old_center_panel is not None:
                old_center_panel.setParent(None)
            self.center_panel_widget = new_center_panel
            self.safe_apply_theme_style(new_center_panel, "panel", self.theme)
            # Setze die Splitter-Größen zurück
            splitter.setSizes(splitter_sizes)
        # Nur Speichern-Button aktivieren, andere deaktivieren
        self.botn_fo_03.setEnabled(True)
        self.botn_fo_02.setEnabled(False)
        self.botn_fo_04.setEnabled(False)
        # Beobachte Änderungen im Formular, um Speichern-Button zu aktivieren
        for widget in self.project_form_widgets.values():
            if isinstance(widget, QLineEdit):
                widget.textChanged.connect(self.enable_save_button)
            elif isinstance(widget, QTextEdit):
                widget.textChanged.connect(self.enable_save_button)
            elif isinstance(widget, QComboBox):
                widget.currentIndexChanged.connect(self.enable_save_button)
            elif isinstance(widget, QSpinBox):
                widget.valueChanged.connect(self.enable_save_button)
            elif isinstance(widget, QDateEdit):
                widget.dateChanged.connect(self.enable_save_button)

    # Aktiviere den Speichern-Button, wenn Änderungen im Formular vorgenommen werden
    def enable_save_button(self):
        self.botn_fo_03.setEnabled(True)

    # Aktualisiere die Projektliste
    def update_project_list(self):
        # Zeigt alle Dateien aus dem DATA_DIR im ListView an (Dateiname, nicht Titel aus Datei).
        if hasattr(self, "project_list_widget"):
            self.project_list_widget.clear()
            # Zeige ALLE Dateien im data-Verzeichnis an
            for file in sorted(DATA_DIR.glob("Project_*.json")):
                if file.is_file():
                    self.project_list_widget.addItem(file.name)
    
    # Lade ein bestehendes Projekt        
    def show_project_form_load(self):
        selected_items = self.project_list_widget.selectedItems()
        if not selected_items:
            return
        filename = selected_items[0].text()
        file = DATA_DIR / filename
        if not file.exists():
            return
        try:
            with open(file, "r", encoding="utf-8") as f:
                project_data = json.load(f)
        except Exception as e:
            log_exception(f"Fehler beim Laden des Projekts: {file}", e)
            return

        splitter = self.centralWidget()
        if isinstance(splitter, QSplitter):
            # Speichere aktuelle Splitter-Größen
            splitter_sizes = splitter.sizes()
            new_center_panel = self.create_center_panel_project_form(project_data)
            old_center_panel = splitter.widget(1)
            splitter.insertWidget(1, new_center_panel)
            splitter.setStretchFactor(1, 1)
            if old_center_panel is not None:
                old_center_panel.setParent(None)
            self.center_panel_widget = new_center_panel
            self.safe_apply_theme_style(new_center_panel, "panel", self.theme)
            # Setze die Splitter-Größen zurück
            splitter.setSizes(splitter_sizes)

        # Speichern-Button deaktivieren, bis etwas geändert wird
        self.botn_fo_03.setEnabled(False)
        self.botn_fo_04.setEnabled(False)
        self.botn_fo_02.setEnabled(False)
        # Beobachte Änderungen im Formular
        for widget in self.project_form_widgets.values():
            if isinstance(widget, QLineEdit):
                widget.textChanged.connect(self.enable_save_button)
            elif isinstance(widget, QTextEdit):
                widget.textChanged.connect(self.enable_save_button)
            elif isinstance(widget, QComboBox):
                widget.currentIndexChanged.connect(self.enable_save_button)
            elif isinstance(widget, QSpinBox):
                widget.valueChanged.connect(self.enable_save_button)
            elif isinstance(widget, QDateEdit):
                widget.dateChanged.connect(self.enable_save_button)

        # 1. Ermittle den Projektnamen (Dateiname) und Datafilename
        last_project_opened = filename  # z.B. Project_xyz_date.json
        last_file_opened = project_data.get("project_file", "")

        # 2. Schreibe in user_settings.json
        self.settings.setdefault("general", {})
        self.settings["general"]["last_project_opened"] = last_project_opened
        self.settings["general"]["last_file_opened"] = last_file_opened
        with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=2, ensure_ascii=False)

    # Lösche das ausgewählte Projekt
    def delete_selected_project(self):
        selected_items = self.project_list_widget.selectedItems()
        if not selected_items:
            return
        filename = selected_items[0].text()
        self.show_secure_delete_dialog("project", filename)
    # Interne Löschfunktion
    def _delete_project(self, filename):
        file = DATA_DIR / filename
        try:
            if file.exists():
                file.unlink()
                log_info(f"Projekt gelöscht: {file}")
        except Exception as e:
            log_exception(f"Fehler beim Löschen der Datei: {file}", e)
        self.show_center_panel(0, self.center_panel_functions)
        self.update_project_buttons_state()

    # ..............................................................
    # Charakter FUNKTIONEN
    # ..............................................................

    # Lege einen neuen Charakter an
    def load_characters(self):
        file_path = DATA_DIR / "Character_main.json"
        if not file_path.exists():
            log_info(f"Charakterdatei nicht gefunden: {file_path}")
            return {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            log_info(f"Charakterdatei geladen: {file_path} ({len(data)} Einträge)")
            return data
        except Exception as e:
            log_exception(f"Fehler beim Laden der Charakterdatei: {file_path}", e)
            return {}
    # Speichere alle Charaktere
    def save_characters(self, characters):
        file_path = DATA_DIR / "Character_main.json"
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(characters, f, indent=2, ensure_ascii=False)
            log_info(f"Charakterdatei gespeichert: {file_path} ({len(characters)} Einträge)")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Charakterdatei: {file_path}", e)
    # Lösche den aktuellen Charakter
    def on_delete_character_clicked(self):
        if not self.current_character_id:
            return
        self.show_secure_delete_dialog("character", self.current_character_id)
    # Interne Löschfunktion    
    def _delete_character(self, character_id):
        characters = self.load_characters()
        if not characters or not character_id:
            log_error(f"Kein Charakter zum Löschen gefunden (ID: {character_id})")
            return
        if character_id in characters:
            del characters[character_id]
            self.save_characters(characters)
            log_info(f"Charakter gelöscht: {character_id}")
            # Nach dem Löschen: nächsten Charakter anzeigen, oder leeres Formular
            if characters:
                first_id = sorted(characters.keys())[0]
                self.current_character_id = first_id
                self.fill_character_form(characters[first_id])
            else:
                self.current_character_id = None
                empty_data = {k: "" for k in self.character_form_widgets}
                self.fill_character_form(empty_data)

    # Fülle das Charakter-Formular mit den Daten eines Charakters
    def fill_character_form(self, character_data):
        for field_name, widget in self.character_form_widgets.items():
            value = character_data.get(field_name, "")
            # --- Spezialfall: born/died als QLineEdit mit Datumsvalidierung ---
            if field_name in ("born", "died") and isinstance(widget, QLineEdit):
                widget.setText(str(value) if value else "")
                # Optional: Validierung und optische Hervorhebung
                text = widget.text().strip()
                if text:
                    # Unterstützte Formate je nach Sprache
                    if self.language == "de":
                        formats = ["%d.%m.%Y", "%Y-%m-%d"]
                    elif self.language == "en":
                        formats = ["%m %d %Y", "%Y-%m-%d"]
                    elif self.language in ("fr", "es"):
                        formats = ["%d/%m/%Y", "%Y-%m-%d"]
                    else:
                        formats = ["%Y-%m-%d"]
                    valid = False
                    for fmt in formats:
                        try:
                            _ = datetime.datetime.strptime(text, fmt).date()
                            valid = True
                            break
                        except Exception:
                            continue
                    if not valid:
                        widget.setStyleSheet("background-color: #ffcccc;")
                    else:
                        widget.setStyleSheet("")
                else:
                    widget.setStyleSheet("")
            # --- Alter-Label: wird automatisch berechnet, nicht setzen ---
            elif field_name == "char_age" and isinstance(widget, QLabel):
                continue
            # --- Standardfelder ---
            elif isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                idx = widget.findText(str(value))
                if idx >= 0:
                    widget.setCurrentIndex(idx)
                else:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    try:
                        widget.setDate(datetime.date.fromisoformat(value))
                    except Exception:
                        widget.setDate(widget.minimumDate())
                else:
                    widget.setDate(widget.minimumDate())

    # Lese die Daten aus dem Charakter-Formular aus
    def get_character_form_data(self):
        data = {}
        for field_name, widget in self.character_form_widgets.items():
            if field_name in ("born", "died") and isinstance(widget, QLineEdit):
                data[field_name] = widget.text().strip()
            if isinstance(widget, QLineEdit):
                data[field_name] = widget.text()
            elif isinstance(widget, QTextEdit):
                data[field_name] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                data[field_name] = widget.currentText()
            elif isinstance(widget, QCheckBox):
                data[field_name] = widget.isChecked()
            elif isinstance(widget, QDateEdit):
                data[field_name] = widget.date().toString("yyyy-MM-dd")
        return data

    # Handler für "Neuer Charakter" Button
    def on_new_character_clicked(self):
        # Leeres Formular anzeigen, keine ID setzen
        empty_data = {k: "" for k in self.character_form_widgets}
        self.current_character_id = None
        self.fill_character_form(empty_data)

    # Handler für "Charakter speichern" Button
    def on_save_character_clicked(self):
        characters = self.load_characters()
        data = self.get_character_form_data()
        if self.current_character_id and self.current_character_id in characters:
            # Bestehenden Charakter aktualisieren
            characters[self.current_character_id] = data
        else:
            # Neuen Charakter anlegen
            existing_ids = [int(k.split("_")[-1]) for k in characters.keys() if k.startswith("character_ID_")]
            next_id = max(existing_ids, default=0) + 1
            new_id = f"character_ID_{next_id:02d}"
            characters[new_id] = data
            self.current_character_id = new_id
        self.save_characters(characters)    

    # Handler für "Vorheriger Charakter" Button
    def on_previous_character_clicked(self):
        characters = self.load_characters()
        if not characters:
            return
        ids = sorted(characters.keys())
        if self.current_character_id in ids:
            idx = ids.index(self.current_character_id)
            new_idx = (idx - 1) % len(ids)
        else:
            new_idx = 0
        self.current_character_id = ids[new_idx]
        self.fill_character_form(characters[self.current_character_id])
    
    # Handler für "Nächster Charakter" Button
    def on_next_character_clicked(self):
        characters = self.load_characters()
        if not characters:
            return
        ids = sorted(characters.keys())
        if self.current_character_id in ids:
            idx = ids.index(self.current_character_id)
            new_idx = (idx + 1) % len(ids)
        else:
            new_idx = 0
        self.current_character_id = ids[new_idx]
        self.fill_character_form(characters[self.current_character_id])    
    
    # ..............................................................
    # Objekt FUNKTIONEN
    # ..............................................................
    
    # Lege ein neues Objekt an
    def load_objects(self):
        file_path = DATA_DIR / "Objects.json"
        if not file_path.exists():
            log_info(f"Objektdatei nicht gefunden: {file_path}")
            return {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            log_info(f"Objektdatei geladen: {file_path} ({len(data)} Einträge)")
            return data
        except Exception as e:
            log_exception(f"Fehler beim Laden der Objektdatei: {file_path}", e)
            return {}
    
    # Speichere alle Objekte
    def save_objects(self, objects):
        file_path = DATA_DIR / "Objects.json"
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(objects, f, indent=2, ensure_ascii=False)
            log_info(f"Objektdatei gespeichert: {file_path} ({len(objects)} Einträge)")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Objektdatei: {file_path}", e)

    # Lösche das aktuelle Objekt
    def on_delete_object_clicked(self):
        if not hasattr(self, "current_object_id") or not self.current_object_id:
            return
        self.show_secure_delete_dialog("object", self.current_object_id)

    # Interne Löschfunktion
    def _delete_object(self, object_id):
        objects = self.load_objects()
        if not objects or not object_id:
            log_error(f"Kein Objekt zum Löschen gefunden (ID: {object_id})")
            return
        if object_id in objects:
            del objects[object_id]
            self.save_objects(objects)
            log_info(f"Objekt gelöscht: {object_id}")
            # Nach dem Löschen: nächsten oder leeren Datensatz anzeigen
            if objects:
                first_id = sorted(objects.keys())[0]
                self.current_object_id = first_id
                self.fill_object_form(objects[first_id])
            else:
                self.current_object_id = None
                empty_data = {k: "" for k in self.object_form_widgets}
                self.fill_object_form(empty_data)

    # Fülle das Objekt-Formular mit den Daten eines Objekts
    def fill_object_form(self, object_data):
        for field_name, widget in self.object_form_widgets.items():
            value = object_data.get(field_name, "")
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                idx = widget.findText(str(value))
                if idx >= 0:
                    widget.setCurrentIndex(idx)
                else:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    try:
                        widget.setDate(datetime.date.fromisoformat(value))
                    except Exception:
                        widget.setDate(datetime.date.today())
                else:
                    widget.setDate(datetime.date.today())

    # Handler für "Neues Objekt" Button
    def on_new_object_clicked(self):
        empty_data = {k: "" for k in self.object_form_widgets}
        self.current_object_id = None
        self.fill_object_form(empty_data)

    # Handler für "Objekt speichern" Button
    def on_save_object_clicked(self):
        objects = self.load_objects()
        data = {}
        for field_name, widget in self.object_form_widgets.items():
            if isinstance(widget, QLineEdit):
                data[field_name] = widget.text()
            elif isinstance(widget, QTextEdit):
                data[field_name] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                data[field_name] = widget.currentText()
            elif isinstance(widget, QCheckBox):
                data[field_name] = widget.isChecked()
            elif isinstance(widget, QDateEdit):
                data[field_name] = widget.date().toString("yyyy-MM-dd")
        if self.current_object_id and self.current_object_id in objects:
            # Bestehendes Objekt aktualisieren
            objects[self.current_object_id] = data
        else:
            # Neues Objekt anlegen
            existing_ids = [int(k.split("_")[-1]) for k in objects.keys() if k.startswith("object_ID_")]
            next_id = max(existing_ids, default=0) + 1
            new_id = f"object_ID_{next_id:02d}"
            objects[new_id] = data
            self.current_object_id = new_id
        self.save_objects(objects)

    # Handler für "Vorheriges Objekt" Button
    def on_previous_object_clicked(self):
        objects = self.load_objects()
        if not objects:
            return
        ids = sorted(objects.keys())
        if self.current_object_id in ids:
            idx = ids.index(self.current_object_id)
            new_idx = (idx - 1) % len(ids)
        else:
            new_idx = 0
        self.current_object_id = ids[new_idx]
        self.fill_object_form(objects[self.current_object_id])

    # Handler für "Nächstes Objekt" Button
    def on_next_object_clicked(self):
        objects = self.load_objects()
        if not objects:
            return
        ids = sorted(objects.keys())
        if self.current_object_id in ids:
            idx = ids.index(self.current_object_id)
            new_idx = (idx + 1) % len(ids)
        else:
            new_idx = 0
        self.current_object_id = ids[new_idx]
        self.fill_object_form(objects[self.current_object_id])   

    # ..............................................................
    # Ort FUNKTIONEN
    # ..............................................................

    # Lege einen neuen Ort an
    def _delete_object(self, object_id):
        objects = self.load_objects()
        if not objects or not object_id:
            log_error(f"Kein Objekt zum Löschen gefunden (ID: {object_id})")
            return
        if object_id in objects:
            del objects[object_id]
            self.save_objects(objects)
            log_info(f"Objekt gelöscht: {object_id}")
    
    # Speichere alle Orte
    def save_locations(self, locations):
        file_path = DATA_DIR / "Locations.json"
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(locations, f, indent=2, ensure_ascii=False)
            log_info(f"Orte-Datei gespeichert: {file_path} ({len(locations)} Einträge)")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Orte-Datei: {file_path}", e)
    # Lade alle Orte
    def load_locations(self):
        file_path = DATA_DIR / "Locations.json"
        if not file_path.exists():
            log_info(f"Orte-Datei nicht gefunden: {file_path}")
            return {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            log_info(f"Orte-Datei geladen: {file_path} ({len(data)} Einträge)")
            return data
        except Exception as e:
            log_exception(f"Fehler beim Laden der Orte-Datei: {file_path}", e)
            return {}
        
    # Lösche den aktuellen Ort
    def on_delete_location_clicked(self):
        if not hasattr(self, "current_location_id") or not self.current_location_id:
            return
        self.show_secure_delete_dialog("location", self.current_location_id)
    # Interne Löschfunktion
    def _delete_location(self, location_id):
        locations = self.load_locations()
        if not locations or not location_id:
            log_error(f"Kein Ort zum Löschen gefunden (ID: {location_id})")
            return
        if location_id in locations:
            del locations[location_id]
            self.save_locations(locations)
            log_info(f"Ort gelöscht: {location_id}")
            # Nach dem Löschen: nächsten oder leeren Datensatz anzeigen
            if locations:
                first_id = sorted(locations.keys())[0]
                self.current_location_id = first_id
                self.fill_location_form(locations[first_id])
            else:
                self.current_location_id = None
                empty_data = {k: "" for k in self.location_form_widgets}
                self.fill_location_form(empty_data)
    
    # Fülle das Ort-Formular mit den Daten eines Ortes
    def fill_location_form(self, location_data):
        for field_name, widget in self.location_form_widgets.items():
            value = location_data.get(field_name, "")
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                idx = widget.findText(str(value))
                if idx >= 0:
                    widget.setCurrentIndex(idx)
                else:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    try:
                        widget.setDate(datetime.date.fromisoformat(value))
                    except Exception:
                        widget.setDate(datetime.date.today())
                else:
                    widget.setDate(datetime.date.today())

    # Handler für "Neuer Ort" Button
    def on_new_location_clicked(self):
        empty_data = {k: "" for k in self.location_form_widgets}
        self.current_location_id = None
        self.fill_location_form(empty_data)

    # Handler für "Ort speichern" Button
    def on_save_location_clicked(self):
        locations = self.load_locations()
        data = {}
        for field_name, widget in self.location_form_widgets.items():
            if isinstance(widget, QLineEdit):
                data[field_name] = widget.text()
            elif isinstance(widget, QTextEdit):
                data[field_name] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                data[field_name] = widget.currentText()
            elif isinstance(widget, QCheckBox):
                data[field_name] = widget.isChecked()
            elif isinstance(widget, QDateEdit):
                data[field_name] = widget.date().toString("yyyy-MM-dd")
        if self.current_location_id and self.current_location_id in locations:
            # Bestehenden Ort aktualisieren
            locations[self.current_location_id] = data
        else:
            # Neuen Ort anlegen
            existing_ids = [int(k.split("_")[-1]) for k in locations.keys() if k.startswith("location_ID_")]
            next_id = max(existing_ids, default=0) + 1
            new_id = f"location_ID_{next_id:02d}"
            locations[new_id] = data
            self.current_location_id = new_id
        self.save_locations(locations)

    # Handler für "Vorheriger Ort" Button
    def on_previous_location_clicked(self):
        locations = self.load_locations()
        if not locations:
            return
        ids = sorted(locations.keys())
        if self.current_location_id in ids:
            idx = ids.index(self.current_location_id)
            new_idx = (idx - 1) % len(ids)
        else:
            new_idx = 0
        self.current_location_id = ids[new_idx]
        self.fill_location_form(locations[self.current_location_id])

    # Handler für "Nächster Ort" Button
    def on_next_location_clicked(self):
        locations = self.load_locations()
        if not locations:
            return
        ids = sorted(locations.keys())
        if self.current_location_id in ids:
            idx = ids.index(self.current_location_id)
            new_idx = (idx + 1) % len(ids)
        else:
            new_idx = 0
        self.current_location_id = ids[new_idx]
        self.fill_location_form(locations[self.current_location_id])   

    # ..............................................................
    # Storyline FUNKTIONEN
    # ..............................................................

    # Lege eine neue Storyline an
    def load_storylines(self):
        file_path = DATA_DIR / "Storylines.json"
        if not file_path.exists():
            log_info(f"Storyline-Datei nicht gefunden: {file_path}")
            return {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            log_info(f"Storyline-Datei geladen: {file_path} ({len(data)} Einträge)")
            return data
        except Exception as e:
            log_exception(f"Fehler beim Laden der Storyline-Datei: {file_path}", e)
            return {}
    
    # Speichere alle Storylines
    def save_storylines(self, storylines):
        file_path = DATA_DIR / "Storylines.json"
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(storylines, f, indent=2, ensure_ascii=False)
            log_info(f"Storyline-Datei gespeichert: {file_path} ({len(storylines)} Einträge)")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Storyline-Datei: {file_path}", e)
    
    # Lösche die aktuelle Storyline
    def on_delete_storyline_clicked(self):
        if not hasattr(self, "current_storyline_id") or not self.current_storyline_id:
            return
        self.show_secure_delete_dialog("storyline", self.current_storyline_id)
    # Interne Löschfunktion
    def _delete_storyline(self, storyline_id):
        storylines = self.load_storylines()
        if not storylines or not storyline_id:
            log_error(f"Keine Storyline zum Löschen gefunden (ID: {storyline_id})")
            return
        if storyline_id in storylines:
            del storylines[storyline_id]
            self.save_storylines(storylines)
            log_info(f"Storyline gelöscht: {storyline_id}")
            # Nach dem Löschen: nächsten oder leeren Datensatz anzeigen
            if storylines:
                first_id = sorted(storylines.keys())[0]
                self.current_storyline_id = first_id
                self.fill_storyline_form(storylines[first_id])
            else:
                self.current_storyline_id = None
                empty_data = {k: "" for k in self.storyline_form_widgets}
                self.fill_storyline_form(empty_data)
        
    # Fülle das Storyline-Formular mit den Daten einer Storyline
    def fill_storyline_form(self, storyline_data):
        for field_name, widget in self.storyline_form_widgets.items():
            value = storyline_data.get(field_name, "")
            if isinstance(widget, QLineEdit):
                widget.setText(str(value))
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(value))
            elif isinstance(widget, QComboBox):
                idx = widget.findText(str(value))
                if idx >= 0:
                    widget.setCurrentIndex(idx)
                else:
                    widget.setCurrentIndex(0)
            elif isinstance(widget, QCheckBox):
                widget.setChecked(bool(value))
            elif isinstance(widget, QDateEdit):
                if value:
                    try:
                        widget.setDate(datetime.date.fromisoformat(value))
                    except Exception:
                        widget.setDate(datetime.date.today())
                else:
                    widget.setDate(datetime.date.today())

    # Handler für "Neue Storyline" Button
    def on_new_storyline_clicked(self):
        empty_data = {k: "" for k in self.storyline_form_widgets}
        self.current_storyline_id = None
        self.fill_storyline_form(empty_data)
    
    # Handler für "Storyline speichern" Button
    def on_save_storyline_clicked(self):
        storylines = self.load_storylines()
        data = {}
        for field_name, widget in self.storyline_form_widgets.items():
            if isinstance(widget, QLineEdit):
                data[field_name] = widget.text()
            elif isinstance(widget, QTextEdit):
                data[field_name] = widget.toPlainText()
            elif isinstance(widget, QComboBox):
                data[field_name] = widget.currentText()
            elif isinstance(widget, QCheckBox):
                data[field_name] = widget.isChecked()
            elif isinstance(widget, QDateEdit):
                data[field_name] = widget.date().toString("yyyy-MM-dd")
        if self.current_storyline_id and self.current_storyline_id in storylines:
            # Bestehende Storyline aktualisieren
            storylines[self.current_storyline_id] = data
        else:
            # Neue Storyline anlegen
            existing_ids = [int(k.split("_")[-1]) for k in storylines.keys() if k.startswith("storyline_ID_")]
            next_id = max(existing_ids, default=0) + 1
            new_id = f"storyline_ID_{next_id:02d}"
            storylines[new_id] = data
            self.current_storyline_id = new_id
        self.save_storylines(storylines)
    
    # Handler für "Vorherige Storyline" Button
    def on_previous_storyline_clicked(self):
        storylines = self.load_storylines()
        if not storylines:
            return
        ids = sorted(storylines.keys())
        if self.current_storyline_id in ids:
            idx = ids.index(self.current_storyline_id)
            new_idx = (idx - 1) % len(ids)
        else:
            new_idx = 0
        self.current_storyline_id = ids[new_idx]
        self.fill_storyline_form(storylines[self.current_storyline_id])

    # Handler für "Nächste Storyline" Button
    def on_next_storyline_clicked(self):
        storylines = self.load_storylines()
        if not storylines:
            return
        ids = sorted(storylines.keys())
        if self.current_storyline_id in ids:
            idx = ids.index(self.current_storyline_id)
            new_idx = (idx + 1) % len(ids)
        else:
            new_idx = 0
        self.current_storyline_id = ids[new_idx]
        self.fill_storyline_form(storylines[self.current_storyline_id])

    # --------------------------------------------------------------
    # --------------------------------------------------------------
    @log_call
    def init_ui(self):
        self.setWindowTitle(self.get_translation("WinStartTitle", "CSNova"))
        window_width = self.window_settings.get("width", 1200)
        window_height = self.window_settings.get("height", 800)
        is_maximized = self.window_settings.get("is_maximized", False)

        if is_maximized:
            self.showMaximized()
            log_info("Fenster wird maximiert geöffnet.")
        else:
            self.resize(window_width, window_height)
            self.setMinimumSize(800, 600)
            log_info(f"Fenstergröße aus Settings: {[window_width, window_height]}")

        splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
        log_info(f"Splitter-Größen aus Settings: {splitter_sizes}")

        # Erzeuge die Panels
        left_panel, update_left_panel_image = self.create_left_panel_start(splitter_sizes)
        center_panel = self.create_center_panel_start()
        right_panel = self.create_right_panel_start()

        self.left_panel_widget = left_panel
        self.center_panel_widget = center_panel
        self.right_panel_widget = right_panel

        splitter = QSplitter(Qt.Horizontal, self)
        splitter.addWidget(left_panel)
        splitter.addWidget(center_panel)
        splitter.addWidget(right_panel)

        def on_splitter_moved(pos, index):
            update_left_panel_image(pos, index)
            log_info("Splitter bewegt, speichere neue Größen.")
            self.save_settings()
        splitter.splitterMoved.connect(on_splitter_moved)

        self.setCentralWidget(splitter)
        splitter.setSizes(splitter_sizes)

        self.safe_apply_theme_style(left_panel, "panel", self.theme)
        self.safe_apply_theme_style(center_panel, "panel", self.theme)
        self.safe_apply_theme_style(right_panel, "panel", self.theme)

        log_info("UI erfolgreich initialisiert.")

    @log_call
    def __init__(self, settings, translation_file, theme_file):
        super().__init__()
        icon_path = ASSETS_DIR / "media" / "csnova.png"
        self.setWindowIcon(QIcon(str(icon_path)))
        self.current_character_id = None
        self.current_object_id = None
        self.current_location_id = None
        self.current_storyline_id = None
        self.settings = settings
        self.translation_file = translation_file
        self.theme_file = theme_file
        self.apply_theme_style = apply_theme_style
        self._was_maximized = settings.get("start_window", {}).get("is_maximized", False)
        self._restore_size_on_unmaximize = False
        
        # 1. Lade Einstellungen
        self.gui_settings = settings.get("gui", {})
        self.general_settings = settings.get("general", {})
        self.window_settings = settings.get("start_window", {})
        self.panel_settings = settings.get("panels", {})
        self.language = self.general_settings.get("language", "de")

        # 2. Lade Theme und Base-Style
        self.theme = load_json_file(self.theme_file)
        if self.theme:
            # Theme-Name ergänzen (Dateiname ohne Pfad und Endung)
            theme_name = Path(self.theme_file).stem
            self.theme["theme_name"] = theme_name
            log_info(f"Theme file geladen: {self.theme_file}")
            log_list("Theme keys", self.theme.keys())
        else:
            log_error("Theme konnte nicht geladen werden, Standardfarben werden verwendet.")

        self.base_style_path = BASE_STYLE_FILE
        self.base_style = load_json_file(BASE_STYLE_FILE)
        if self.base_style:
            log_info(f"Base style file geladen: {self.base_style_path}")
            log_list("Base style keys", self.base_style.keys())
        else:
            log_error("Base Style konnte nicht geladen werden, Standardwerte werden verwendet.")

        # 3. Wende das globale Stylesheet direkt auf die QApplication an
        app = self._get_qapplication_instance()
        if app and self.base_style and self.theme:
            apply_global_stylesheet(app, self.base_style_path, self.theme)
            log_info("Globales Stylesheet aus base_style.json und Theme angewendet.")
        else:
            log_error("Globales Stylesheet konnte nicht angewendet werden.")

        # 4. Lade Übersetzungen
        self.translations = load_json_file(self.translation_file)
        if self.translations:
            log_info(f"Translations geladen: {self.translation_file}")
            log_list("Translation keys", self.translations.keys())
        else:
            log_error("Übersetzungsdatei ist leer oder konnte nicht geladen werden.")

        combobox_translation_path = TRANSLATIONS_DIR / f"translation_data_combobox_{self.language}.json"

        self.combobox_translations = load_json_file(combobox_translation_path)
        if self.combobox_translations:
            log_info(f"ComboBox-Translations geladen: {combobox_translation_path}")
            log_list("ComboBox-Translation keys", self.combobox_translations.keys())
        else:
            log_error("ComboBox-Übersetzungsdatei ist leer oder konnte nicht geladen werden.")

        self.language = self.general_settings.get("language", "de")

        # 5. Initialisiere UI
        self.init_ui()

    # Hilfsfunktion, um die QApplication-Instanz zu bekommen
    def _get_qapplication_instance(self):
        # Hilfsfunktion, um die QApplication-Instanz zu bekommen
        #from PySide6.QtWidgets import QApplication
        return QApplication.instance()
    
    # Funktion zum Abrufen von Übersetzungen
    def get_translation(self, key, default=""):
        """Gibt die Übersetzung für einen Schlüssel zurück, falls vorhanden, sonst den Default-Wert."""
        return self.translations.get(key, default)

    def run(self):
        log_info("StartWindow wird angezeigt.")
        self.show()