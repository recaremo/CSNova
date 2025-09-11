from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QSplitter
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import json
import os
from config.dev import ASSETS_DIR
from core.logger import log_info, log_error, log_exception, log_call

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
# Funktion zum dynamischen Import der apply_theme_style Funktion
def load_python_gui_styles():
    """Importiert die apply_theme_style Funktion aus python_gui_styles.py."""
    try:
        from gui.styles.python_gui_styles import apply_theme_style
        log_info("Imported apply_theme_style from python_gui_styles.py")
        return apply_theme_style
    except Exception as e:
        log_exception("Error importing apply_theme_style from python_gui_styles.py", e)
        return None

@log_call
# StartWindow Klasse
class StartWindow(QMainWindow):
    def __init__(self, settings, translation_file, theme_file):
        super().__init__()
        self.settings = settings
        self.translation_file = translation_file
        self.theme_file = theme_file
        # 1. Lade Einstellungen
        self.gui_settings = settings.get("gui", {})
        self.general_settings = settings.get("general", {})
        self.window_settings = settings.get("start_window", {})
        self.panel_settings = settings.get("panels", {})

        # 2. Lade Theme und Übersetzungen
        self.theme = load_json_file(self.theme_file)
        if not self.theme:
            log_error("Theme konnte nicht geladen werden, Standardfarben werden verwendet.")
        self.base_style = load_json_file(os.path.join(os.path.dirname(self.theme_file), "base_style.json"))
        if not self.base_style:
            log_error("Base Style konnte nicht geladen werden, Standardwerte werden verwendet.")
        self.apply_theme_style = load_python_gui_styles()
        if not self.apply_theme_style:
            log_error("apply_theme_style konnte nicht importiert werden, Styles werden nicht angewendet.")

        self.translations = load_json_file(self.translation_file)
        if not self.translations:
            log_error("Übersetzungsdatei ist leer oder konnte nicht geladen werden.")
        self.language = self.general_settings.get("language", "de")

        # 3. Initialisiere UI
        self.init_ui()

    # Funktion zum Abrufen von Übersetzungen
    @log_call
    def get_translation(self, key, default=""):
        """Gibt den übersetzten Text für den aktuellen Sprachcode zurück."""
        try:
            return self.translations.get(key, default)
        except Exception as e:
            log_exception(f"Error getting translation for key '{key}'", e)
            return default

    # Initialisiere die Benutzeroberfläche

    def init_ui(self):
        """Initialisiert das Startfenster, bindet Theme/Styles und Übersetzungen ein und erzeugt 3 Panels mit anpassbarer Breite.
        Im left_panel wird ein Bild oben zentriert angezeigt und dynamisch an die Panelbreite angepasst (nur horizontales Stretching, Höhe proportional zur Breite).
        Panels erhalten explizite Ränder für bessere Optik."""
        try:
            # Fenstergröße und Titel
            width = self.window_settings.get("width", 800)
            height = self.window_settings.get("height", 600)
            self.resize(width, height)
            title_key = "WinStartTitle"
            window_title = self.get_translation(title_key, "Codices Scriptoria Nova - CSNova")
            self.setWindowTitle(window_title)

            # Splitter für Panels
            splitter = QSplitter(Qt.Horizontal, self)
            splitter.setStyleSheet(f"QSplitter::handle {{ background: {self.theme.get('splitter_handle_bg', '#888d92')}; }}")
            panel_names = ["left_panel", "center_panel", "right_panel"]
            panel_widgets = []

            # Für das dynamische Bild im left_panel
            image_label = None
            pixmap = None

            for panel_idx, panel_name in enumerate(panel_names):
                panel_widget = QWidget()
                panel_layout = QVBoxLayout(panel_widget)
                panel_layout.setContentsMargins(10, 10, 10, 10)
                panel_layout.setSpacing(10)
                panel_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

                label = QLabel(self.get_translation(f"{panel_name}_label", panel_name), panel_widget)
                label.setAlignment(Qt.AlignCenter)
                if self.apply_theme_style and self.theme:
                    self.apply_theme_style(label, "label", self.theme)
                panel_layout.addWidget(label)

                # Bild im left_panel mit proportionaler Höhe (nur horizontales Stretching)
                if panel_name == "left_panel":
                    image_path = ASSETS_DIR / "media" / "csNova_background_start.png"
                    image_label = QLabel(panel_widget)
                    image_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                    pixmap = QPixmap(str(image_path))
                    image_label.setPixmap(pixmap)
                    panel_layout.addWidget(image_label)
                    panel_layout.setStretch(panel_layout.count() - 1, 1)

                    # Logging nur einmal beim Initialisieren
                    log_info(f"Breite Originalbild: {pixmap.width()} - Höhe Originalbild: {pixmap.height()}")

                    # Initiales Setzen des Bildes mit Breite aus Settings
                    splitter_sizes = self.panel_settings.get("splitter_sizes", [200, 400, 200])
                    initial_width = splitter_sizes[0] - 20  # 10px links/rechts Rand
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

                # Setze Objekt-Namen und wende spezifische Styles an
                if panel_name == "center_panel":
                    panel_widget.setObjectName("CenterPanel")
                    if self.apply_theme_style and self.theme:
                        self.apply_theme_style(panel_widget, "panel", {**self.theme, "background": self.theme.get("center_bg", self.theme.get("background"))})
                elif panel_name == "left_panel":
                    panel_widget.setObjectName("NavigationPanel")
                    if self.apply_theme_style and self.theme:
                        self.apply_theme_style(panel_widget, "panel", {**self.theme, "background": self.theme.get("nav_bg", self.theme.get("background"))})
                elif panel_name == "right_panel":
                    panel_widget.setObjectName("HelpPanel")
                    if self.apply_theme_style and self.theme:
                        self.apply_theme_style(panel_widget, "panel", {**self.theme, "background": self.theme.get("help_bg", self.theme.get("background"))})

                panel_widgets.append(panel_widget)
                splitter.addWidget(panel_widget)

            # Splitter-Größen aus Settings anwenden
            splitter_sizes = self.panel_settings.get("splitter_sizes", [200, 400, 200])
            if len(splitter_sizes) == 3:
                splitter.setSizes(splitter_sizes)
            else:
                log_error("splitter_sizes in user_settings.json sind ungültig oder fehlen. Standardwerte werden verwendet.")

            # Dynamische Anpassung des Bildes bei Splitterbewegung
            if image_label and pixmap:
                def update_image_on_splitter_move(pos, index):
                    breite_left_panel = panel_widgets[0].width() - 20
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
                splitter.splitterMoved.connect(update_image_on_splitter_move)

            # Layout für das Hauptfenster
            central_widget = QWidget(self)
            layout = QVBoxLayout(central_widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(splitter)
            self.setCentralWidget(central_widget)

            # Theme/Styles auf das Hauptfenster anwenden
            if self.apply_theme_style and self.theme:
                self.apply_theme_style(self, "panel", self.theme)

            log_info("StartWindow UI mit 3 Panels, Splitter und gestretchtem Bild initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartWindow UI.", e)

    def run(self):
        log_info("StartWindow wird angezeigt.")
        self.show()