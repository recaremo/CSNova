from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QSplitter, QPushButton, QSpacerItem, QSizePolicy, QDialog, QHBoxLayout, QApplication, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import json
import os
from config.dev import ASSETS_DIR
from core.logger import log_info, log_error, log_exception, log_call
from gui.styles.python_gui_styles import apply_theme_style
from csNova import LANGUAGE_DEFAULTS, THEMES_STYLES_DEFAULTS

# Hilfsfunktion für Listen-Logging
def log_list(title, items):
    log_info(f"{title}:\n" + "\n".join(f"  - {item}" for item in items))

# Funktion zum Laden von JSON-Dateien
def load_json_file(path):
    """Lädt eine JSON-Datei und gibt deren Inhalt als Dictionary zurück."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        log_info(f"Loaded JSON file: {path}")
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
                log_error(f"Unresolved placeholder in StyleSheet: {value}")
                value = ""  # Ungültige Regel entfernen
            rule_str += f"{prop}: {value}; "
        stylesheet_parts.append(f"{selector} {{ {rule_str} }}")

    full_stylesheet = "\n".join(stylesheet_parts)
    app.setStyleSheet(full_stylesheet)
    log_info(f"Globales Stylesheet angewendet aus Theme: {theme.get('theme_name', 'Unbekannt')} und Datei: {base_style_path}")
    log_info(f"Theme-Preview: {theme}")

# StartWindow Klasse
class StartWindow(QMainWindow):

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
        ]
        for i, (key, hint_key) in enumerate(nav_keys, start=1):
            btn_attr = f"botn_st_{i:02d}"
            if hasattr(self, btn_attr):
                btn = getattr(self, btn_attr)
                btn.setText(self.get_translation(key, f"Button {i}"))
                btn.setToolTip(self.get_translation(hint_key, ""))

        # Navigationselement 9 (Exit) aktualisieren
        if hasattr(self, "botn_st_09"):
            self.botn_st_09.setText(self.get_translation("botn_st_09", "Exit"))
            self.botn_st_09.setToolTip(self.get_translation("botn_st_09_hint", "Exit CSNova."))

        # Fenster-Titel aktualisieren
        self.setWindowTitle(self.get_translation("WinStartTitle", "CSNova"))
   
    # Funktion wenn über language_combo die Sprache geändert wird
    def change_language(self, new_language):
        # Mapping-Liste wie in on_language_changed
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
        translation_path = os.path.join(os.path.dirname(self.translation_file), f"translation_{new_language}.json")
        try:
            with open(translation_path, "w", encoding="utf-8") as f:
                json.dump(translation_data, f, ensure_ascii=False, indent=2)
            log_info(f"Neue Übersetzungsdatei gespeichert: {translation_path}")
        except Exception as e:
            log_exception(f"Fehler beim Speichern der Übersetzungsdatei: {translation_path}", e)
            return

        # Übersetzungen temporär anwenden
        self.translations = translation_data
        self.language = new_language

        # Texte der Panels aktualisieren
        self.update_center_panel_start_texts()
        #self.update_left_panel_texts()
        self.update_right_panel_start_texts()

        # Wenn die Sprache geändert wurde, sind die Buttons btn_save und btn_reset aktiv
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
        theme_path = os.path.join(os.path.dirname(self.theme_file), f"theme_{new_theme_name}.json")
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
            # 1. Sprache aus language_combo
            language_codes = ["de", "en", "fr", "es"]
            lang_index = self.language_combo.currentIndex()
            language = language_codes[lang_index]
            self.settings["general"]["language"] = language
            self.settings["general"]["file_path_lang"] = f"./core/translations/translation_{language}.json"

            # 2. Theme aus theme_combo
            theme_names = [
                "Modern_neutral", "Modern_dark", "Modern_light",
                "OldSchool_neutral", "OldSchool_dark", "OldSchool_light",
                "Vintage_neutral", "Vintage_dark", "Vintage_light",
                "Future_neutral", "Future_dark", "Future_light",
                "Minimal_neutral", "Minimal_dark", "Minimal_light"
            ]
            theme_index = self.theme_combo.currentIndex()
            theme_name = theme_names[theme_index]
            self.settings["gui"]["style_theme"] = theme_name
            self.settings["gui"]["file_path_gui"] = f"./gui/styles/theme_{theme_name}.json"

            # 3a. Fenstergröße
            width = self.width()
            height = self.height()
            self.settings["start_window"]["width"] = width
            self.settings["start_window"]["height"] = height

            # 3b. Splitter-Größen
            splitter = self.centralWidget()
            if isinstance(splitter, QSplitter):
                sizes = splitter.sizes()
                self.settings["panels"]["splitter_sizes"] = sizes

            # Speichern in user_settings.json
            with open("config/user_settings.json", "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
            log_info("Einstellungen erfolgreich gespeichert.")
            self.btn_save.setEnabled(False)
        except Exception as e:
            log_exception("Fehler beim Speichern der Einstellungen", e)

    def reset_settings(self):
        # Beispiel: Einstellungen zurücksetzen
        # Hier könntest du DEFAULT_SETTINGS laden und anwenden
        log_info("Einstellungen werden auf Standard zurückgesetzt.")
        # ...Logik zum Zurücksetzen...
        self.btn_reset.setEnabled(False)
        self.btn_save.setEnabled(True)

    def go_to_next_step(self):
        # Beispiel: Weiter zum nächsten Schritt
        log_info("Weiter-Button geklickt. Nächster Schritt wird ausgeführt.")
        # ...Logik für den nächsten Schritt...
    
    # PANELS FUNKTIONEN (PLATZHALTER) - LEFT_PANEL
    # ..............................................................

    
    # Dieses left_panel_start wird beim Systemstart angezeigt und beinhaltet das Programmlogo
    # und grundelegende Informationen: (c), Version, Autor, Lizenz und evtl. weitere Hinweise.
    def create_left_panel_start(self, splitter_sizes):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(10, 10, 10, 10)
        panel_layout.setSpacing(10)
        panel_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        label = QLabel(self.get_translation("left_panel_label", "left_panel"), panel_widget)
        label.setAlignment(Qt.AlignCenter)
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(label, "label", self.theme)
        panel_layout.addWidget(label)

        image_path = ASSETS_DIR / "media" / "csNova_background_start.png"
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
        return QWidget()  # Placeholder for potential future functionality
    
    # Dieses left_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitert wird.
    def create_left_panel_project(self):
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses left_panel_settings wird angezeigt, wenn die Einstellungen geöffnet werden.
    def create_left_panel_settings(self):
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses left_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitert wird.
    def create_left_panel_character(self):
        return QWidget()  # Placeholder for potential future functionality 

    
    # Dieses left_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitert wird.
    def create_left_panel_location(self):
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses left_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitert wird.
    def create_left_panel_object(self):
        return QWidget()  # Placeholder for potential future functionality

    # PANELS FUNKTIONEN (PLATZHALTER) - CENTER_PANEL
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
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses center_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitert wird.
    def create_center_panel_project(self):
        return QWidget()  # Placeholder for potential future functionality  

    
    # Dieses center_panel_settings wird angezeigt, wenn die Einstellungen bearbeitet werden sollen.
    def create_center_panel_settings(self):
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses center_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitert wird.
    def create_center_panel_character(self):
        return QWidget()  # Placeholder for potential future functionality  

    
    # Dieses center_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitert wird.
    def create_center_panel_location(self):
        return QWidget()  # Placeholder for potential future functionality  

    
    # Dieses center_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitert wird.
    def create_center_panel_object(self):
        return QWidget()  # Placeholder for potential future functionality  

    # PANELS FUNKTIONEN (PLATZHALTER) - RIGHT_PANEL
    # ..............................................................

    
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

        # Navigationselemente 1-8
        nav_keys = [
            ("botn_st_01", "botn_st_01_hint"),
            ("botn_st_02", "botn_st_02_hint"),
            ("botn_st_03", "botn_st_03_hint"),
            ("botn_st_04", "botn_st_04_hint"),
            ("botn_st_05", "botn_st_05_hint"),
            ("botn_st_06", "botn_st_06_hint"),
            ("botn_st_07", "botn_st_07_hint"),
            ("botn_st_08", "botn_st_08_hint"),
        ]
        for i, (key, hint_key) in enumerate(nav_keys, start=1):
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            panel_layout.addWidget(btn)
            setattr(self, f"botn_st_{i:02d}", btn)

        # Spacer, damit Button 9 unten ist
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Navigationselement 9 (unten)
        btn9_text = self.get_translation("botn_st_09", "Exit")
        btn9_hint = self.get_translation("botn_st_09_hint", "Exit CSNova.")
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
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses right_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitert wird.
    # Es beinhaltet die Navigation zu den verschiedenen Projekt-Einstellungen und beendet den Projekt-Modus.
    def create_right_panel_project(self):
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses right_panel_settings wird angezeigt, wenn die Einstellungen bearbeitet werden sollen.
    # Es beinhaltet die Navigation zu den verschiedenen Einstellungs-Kategorien und beendet den Einstellungs-Modus.
    def create_right_panel_settings(self):
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses right_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitert wird.
    # Es beinhaltet die Navigation zu den verschiedenen Charakter-Einstellungen und beendet den Charakter-Modus.
    def create_right_panel_character(self):
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses right_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitert wird.
    # Es beinhaltet die Navigation zu den verschiedenen Ort-Einstellungen und beendet den Ort-Modus.
    def create_right_panel_location(self):
        return QWidget()  # Placeholder for potential future functionality

    
    # Dieses right_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitert wird.
    # Es beinhaltet die Navigation zu den verschiedenen Objekt-Einstellungen und beendet den Objekt-Modus.
    def create_right_panel_object(self):
        return QWidget()  # Placeholder for potential future functionality

    # --------------------------------------------------------------           )
    # --------------------------------------------------------------
    @log_call
    def init_ui(self):
        # Setze den Fenstertitel und die Mindestgröße
        self.setWindowTitle(self.get_translation("WinStartTitle", "CSNova"))
        window_width = self.window_settings.get("width", 1200)
        window_height = self.window_settings.get("height", 800)
        window_size = [window_width, window_height]
        self.resize(*window_size)
        self.setMinimumSize(*window_size)
        log_info(f"Fenstergröße aus Settings: {window_size}")

        # Splitter-Größen aus den Settings oder Default
        splitter_sizes = self.panel_settings.get("splitter_sizes", [300, 600, 300])
        log_info(f"Splitter-Größen aus Settings: {splitter_sizes}")

        # Erzeuge die Panels
        left_panel, update_left_panel_image = self.create_left_panel_start(splitter_sizes)
        center_panel = self.create_center_panel_start()
        right_panel = self.create_right_panel_start()

        # Panels als Attribute speichern (für update_all_themes)
        self.left_panel_widget = left_panel
        self.center_panel_widget = center_panel
        self.right_panel_widget = right_panel

        # Splitter für die Hauptbereiche
        splitter = QSplitter(Qt.Horizontal, self)
        splitter.addWidget(left_panel)
        splitter.addWidget(center_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes(splitter_sizes)

        # Dynamische Bildanpassung bei Splitterbewegung
        def on_splitter_moved(pos, index):
            update_left_panel_image(pos, index)
        splitter.splitterMoved.connect(on_splitter_moved)

        # Setze das zentrale Widget
        self.setCentralWidget(splitter)

        # Wende Theme-Effekte auf die Panels an
        self.safe_apply_theme_style(left_panel, "panel", self.theme)
        self.safe_apply_theme_style(center_panel, "panel", self.theme)
        self.safe_apply_theme_style(right_panel, "panel", self.theme)

        log_info("UI erfolgreich initialisiert.")

    @log_call
    def __init__(self, settings, translation_file, theme_file):
        super().__init__()
        self.settings = settings
        self.translation_file = translation_file
        self.theme_file = theme_file
        self.apply_theme_style = apply_theme_style

        # 1. Lade Einstellungen
        self.gui_settings = settings.get("gui", {})
        self.general_settings = settings.get("general", {})
        self.window_settings = settings.get("start_window", {})
        self.panel_settings = settings.get("panels", {})

        # 2. Lade Theme und Base-Style
        self.theme = load_json_file(self.theme_file)
        if self.theme:
            # Theme-Name ergänzen (Dateiname ohne Pfad und Endung)
            theme_name = os.path.splitext(os.path.basename(self.theme_file))[0]
            self.theme["theme_name"] = theme_name
            log_info(f"Theme file geladen: {self.theme_file}")
            log_list("Theme keys", self.theme.keys())
        else:
            log_error("Theme konnte nicht geladen werden, Standardfarben werden verwendet.")

        base_style_path = os.path.join(os.path.dirname(self.theme_file), "base_style.json")
        self.base_style_path = base_style_path
        self.base_style = load_json_file(base_style_path)
        if self.base_style:
            log_info(f"Base style file geladen: {base_style_path}")
            log_list("Base style keys", self.base_style.keys())
        else:
            log_error("Base Style konnte nicht geladen werden, Standardwerte werden verwendet.")

        # 3. Wende das globale Stylesheet direkt auf die QApplication an
        app = self._get_qapplication_instance()
        if app and self.base_style and self.theme:
            apply_global_stylesheet(app, base_style_path, self.theme)
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