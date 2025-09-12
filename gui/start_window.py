from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QSplitter, QPushButton, QSpacerItem, QSizePolicy, QDialog, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import json
import os
from config.dev import ASSETS_DIR
from core.logger import log_info, log_error, log_exception, log_call
from gui.styles.python_gui_styles import apply_theme_style

@log_call
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

@log_call
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
                # Falls keine Platzhalter mehr ersetzt wurden, abbrechen
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

@log_call
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
        label = QLabel(self.get_translation("secureExitTitle", "Möchtest du CSNova wirklich beenden?"), dialog)
        label.setAlignment(Qt.AlignCenter)
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(label, "label", self.theme)
        layout.addWidget(label)

        # Buttons
        btn_layout = QHBoxLayout()
        btn_yes = QPushButton(self.get_translation("botn_yes", "Ja"), dialog)
        btn_no = QPushButton(self.get_translation("botn_no", "Nein"), dialog)
        if self.apply_theme_style and self.theme:
            self.apply_theme_style(btn_yes, "button", self.theme)
            self.apply_theme_style(btn_no, "button", self.theme)
        btn_layout.addWidget(btn_yes)
        btn_layout.addWidget(btn_no)
        layout.addLayout(btn_layout)

        # Dialog-Panel Style
        #if self.apply_theme_style and self.theme:
        #    self.apply_theme_style(dialog, "panel", self.theme)

        # Button-Logik
        btn_yes.clicked.connect(self.close)
        btn_no.clicked.connect(dialog.reject)

        dialog.exec()
   
    # Funktion zum sicheren Anwenden von Theme/Style
    def safe_apply_theme_style(self, widget, widget_type, theme=None, extra=None):
        """Wendet Theme/Style sicher auf ein Widget an, falls möglich."""
        if self.apply_theme_style and (theme or self.theme):
            self.apply_theme_style(widget, widget_type, theme or self.theme, extra)

    # PANELS FUNKTIONEN (PLATZHALTER) - LEFT_PANEL
    # ..............................................................

    @log_call
    # Dieses left_panel_start wird beim Systemstart angezeigt und beinhaltet das Programmlogo
    # und grundelegende Informationen: (c), Version, Autor, Lizenz und evtl. weitere Hinweise.
    def create_left_panel_start(self, splitter_sizes):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(10, 10, 10, 10)
        panel_layout.setSpacing(10)
        panel_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        #label = QLabel(self.get_translation("left_panel_label", "left_panel"), panel_widget)
        #label.setAlignment(Qt.AlignCenter)
        #if self.apply_theme_style and self.theme:
        #    self.apply_theme_style(label, "label", self.theme)
        #panel_layout.addWidget(label)

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
    
    @log_call
    # Dieses left_panel_editor wird im Editor-Modus angezeigt und beinhaltet
    # die Inhalte aus den Tabellen: Charaktere, Orte, Objekte, Kapitel, Szenen
    def create_left_panel_editor(self):
        return QWidget()  # Placeholder for potential future functionality
    @log_call
    # Dieses left_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitert wird.
    def create_left_panel_project(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses left_panel_settings wird angezeigt, wenn die Einstellungen geöffnet werden.
    def create_left_panel_settings(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses left_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitert wird.
    def create_left_panel_character(self):
        return QWidget()  # Placeholder for potential future functionality 

    @log_call
    # Dieses left_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitert wird.
    def create_left_panel_location(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses left_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitert wird.
    def create_left_panel_object(self):
        return QWidget()  # Placeholder for potential future functionality

    # PANELS FUNKTIONEN (PLATZHALTER) - CENTER_PANEL
    # ..............................................................

    @log_call
    # Dieses center_panel_start wird beim Systemstart angezeigt und beinhaltet
    # grundlegende Informationen und Anpassungsmöglichkeiten für die Einstellungen: Sprache und Theme
    def create_center_panel_start(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses center_panel_editor wird im Editor-Modus angezeigt und beinhaltet
    # die Textverarbeitung für die Szenen usw.
    def create_center_panel_editor(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses center_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitert wird.
    def create_center_panel_project(self):
        return QWidget()  # Placeholder for potential future functionality  

    @log_call
    # Dieses center_panel_settings wird angezeigt, wenn die Einstellungen bearbeitet werden sollen.
    def create_center_panel_settings(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses center_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitert wird.
    def create_center_panel_character(self):
        return QWidget()  # Placeholder for potential future functionality  

    @log_call
    # Dieses center_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitert wird.
    def create_center_panel_location(self):
        return QWidget()  # Placeholder for potential future functionality  

    @log_call
    # Dieses center_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitert wird.
    def create_center_panel_object(self):
        return QWidget()  # Placeholder for potential future functionality  

    # PANELS FUNKTIONEN (PLATZHALTER) - RIGHT_PANEL
    # ..............................................................

    @log_call
    # Dieses right_panel_start wird beim Systemstart angezeigt und beinhaltet
    # die Navigation zum Aufruf von: Editor, Projekt, Einstellungen, Hilfe, Über
    def create_right_panel_start(self):
        panel_widget = QWidget()
        panel_layout = QVBoxLayout(panel_widget)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(16)
        panel_layout.setAlignment(Qt.AlignTop)

        # Header
        header_text = self.get_translation("startWinHeader", "Projektübersicht")
        header_label = QLabel(header_text, panel_widget)
        header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.safe_apply_theme_style(header_label, "header", self.theme)
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
        for key, hint_key in nav_keys:
            btn_text = self.get_translation(key, key)
            btn_hint = self.get_translation(hint_key, "")
            btn = QPushButton(btn_text, panel_widget)
            btn.setToolTip(btn_hint)
            self.safe_apply_theme_style(btn, "button", self.theme)
            panel_layout.addWidget(btn)

        # Spacer, damit Button 9 unten ist
        panel_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Navigationselement 9 (unten)
        btn9_text = self.get_translation("botn_st_09", "Beenden")
        btn9_hint = self.get_translation("botn_st_09_hint", "")
        btn9 = QPushButton(btn9_text, panel_widget)
        btn9.setToolTip(btn9_hint)
        self.safe_apply_theme_style(btn9, "button")
        btn9.clicked.connect(self.show_secure_exit_dialog)
        panel_layout.addWidget(btn9, alignment=Qt.AlignBottom)

        panel_widget.setObjectName("NavigationPanelStart")
        self.safe_apply_theme_style(panel_widget, "panel", {**self.theme, "background": self.theme.get("nav_bg", self.theme.get("background"))})

        return panel_widget

    @log_call
    # Dieses right_panel_editor wird im Editor-Modus angezeigt und beinhaltet
    # die Navigation, ob in left_panel die Charaktere, Orte, Objekte, Kapitel oder Szenen angezeigt werden sollen.
    # Außerdem wird hier der Editor-Modus beendet.
    def create_right_panel_editor(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses right_panel_project wird angezeigt, wenn ein Projekt erstellt oder bearbeitert wird.
    # Es beinhaltet die Navigation zu den verschiedenen Projekt-Einstellungen und beendet den Projekt-Modus.
    def create_right_panel_project(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses right_panel_settings wird angezeigt, wenn die Einstellungen bearbeitet werden sollen.
    # Es beinhaltet die Navigation zu den verschiedenen Einstellungs-Kategorien und beendet den Einstellungs-Modus.
    def create_right_panel_settings(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses right_panel_character wird angezeigt, wenn ein Charakter erstellt oder bearbeitert wird.
    # Es beinhaltet die Navigation zu den verschiedenen Charakter-Einstellungen und beendet den Charakter-Modus.
    def create_right_panel_character(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses right_panel_location wird angezeigt, wenn ein Ort erstellt oder bearbeitert wird.
    # Es beinhaltet die Navigation zu den verschiedenen Ort-Einstellungen und beendet den Ort-Modus.
    def create_right_panel_location(self):
        return QWidget()  # Placeholder for potential future functionality

    @log_call
    # Dieses right_panel_object wird angezeigt, wenn ein Objekt erstellt oder bearbeitert wird.
    # Es beinhaltet die Navigation zu den verschiedenen Objekt-Einstellungen und beendet den Objekt-Modus.
    def create_right_panel_object(self):
        return QWidget()  # Placeholder for potential future functionality

    # --------------------------------------------------------------           )
    # --------------------------------------------------------------

    def init_ui(self):
        # Setze den Fenstertitel und die Mindestgröße
        self.setWindowTitle(self.get_translation("WinStartTitle", "CSNova"))
        self.setMinimumSize(1200, 800)

        # Splitter-Größen aus den Settings oder Default
        splitter_sizes = self.window_settings.get("splitter_sizes", [300, 600, 300])

        # Erzeuge die Panels
        left_panel, update_left_panel_image = self.create_left_panel_start(splitter_sizes)
        center_panel = self.create_center_panel_start()
        right_panel = self.create_right_panel_start()

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

        # Wende Theme-Styles auf die Panels an
        self.safe_apply_theme_style(left_panel, "panel", self.theme)
        self.safe_apply_theme_style(center_panel, "panel", self.theme)
        self.safe_apply_theme_style(right_panel, "panel", self.theme)

        log_info("UI erfolgreich initialisiert.")

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
            log_info(f"Theme file loaded: {self.theme_file}")
            log_info(f"Theme keys: {list(self.theme.keys())}")
        else:
            log_error("Theme konnte nicht geladen werden, Standardfarben werden verwendet.")

        base_style_path = os.path.join(os.path.dirname(self.theme_file), "base_style.json")
        self.base_style = load_json_file(base_style_path)
        if self.base_style:
            log_info(f"Base style file loaded: {base_style_path}")
            log_info(f"Base style keys: {list(self.base_style.keys())}")
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
            log_info(f"Translations loaded: {self.translation_file}")
            log_info(f"Translation keys: {list(self.translations.keys())}")
        else:
            log_error("Übersetzungsdatei ist leer oder konnte nicht geladen werden.")

        self.language = self.general_settings.get("language", "de")

        # 5. Initialisiere UI
        self.init_ui()

    # Hilfsfunktion, um die QApplication-Instanz zu bekommen
    @log_call
    def _get_qapplication_instance(self):
        # Hilfsfunktion, um die QApplication-Instanz zu bekommen
        from PySide6.QtWidgets import QApplication
        return QApplication.instance()
    
    # Funktion zum Abrufen von Übersetzungen
    @log_call
    def get_translation(self, key, default=""):
        """Gibt die Übersetzung für einen Schlüssel zurück, falls vorhanden, sonst den Default-Wert."""
        return self.translations.get(key, default)

    def run(self):
        log_info("StartWindow wird angezeigt.")
        self.show()