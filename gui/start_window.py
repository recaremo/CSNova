from PySide6.QtWidgets import (
    QMainWindow, QWidget, QSplitter, QVBoxLayout, QPushButton, QLabel, QComboBox, QHBoxLayout
)
from PySide6.QtCore import Qt
import json
from config.dev import BASE_STYLE_FILE, USER_SETTINGS_FILE, FORM_FIELDS_FILE, TRANSLATIONS_DIR
from core.logger import log_info, log_exception
from gui.styles.python_gui_styles import apply_theme_style
from pathlib import Path

class StartWindow(QMainWindow):
    """
    Hauptfenster für CSNova. Lädt alle relevanten Daten aus den Konfigurationsdateien
    und erstellt die GUI dynamisch und konsistent nach den aktuellen Einstellungen und Styles.
    """

    def __init__(self, settings, translation_file, theme_file):
        """
        Initialisiert das Hauptfenster und lädt die benötigten Daten.
        """
        super().__init__()
        try:
            self.settings = settings
            self.translation_file = translation_file
            self.theme_file = theme_file
            self.translation = self.load_json(translation_file)
            self.theme = self.load_json(theme_file)
            self.base_style = self.load_json(BASE_STYLE_FILE)
            self.form_fields = self.load_json(FORM_FIELDS_FILE)
            self.setWindowTitle(self.translation.get("WinStartTitle", "CSNova"))
            self.language_changed = False
            self.original_language = self.settings.get("general", {}).get("language", "de")
            self.current_language = self.original_language
            self.init_ui()
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartWindow.", e)

    def load_json(self, path):
        """
        Lädt eine JSON-Datei und gibt deren Inhalt als Dictionary zurück.
        Args:
            path (str): Pfad zur JSON-Datei.
        Returns:
            dict: Inhalt der Datei oder leeres Dict bei Fehler.
        """
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            log_info(f"Loaded JSON file: {path}")
            return data
        except Exception as e:
            log_exception(f"Error loading {path}", e)
            return {}

    def save_settings(self):
        """
        Speichert die aktuellen Einstellungen in user_settings.json.
        """
        try:
            with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
            log_info("user_settings.json updated from start_window.")
        except Exception as e:
            log_exception("Error saving user_settings.json from start_window", e)

    def load_translation_for_language(self, lang_key):
        """
        Lädt die Übersetzungsdatei für die angegebene Sprache.
        Erstellt sie, falls sie nicht existiert.
        """
        try:
            translation_path = TRANSLATIONS_DIR / f"translation_{lang_key}.json"
            if not translation_path.exists():
                # Fallback: Kopiere die Default-Übersetzungen aus csNova.py
                from csNova import LANGUAGE_DEFAULTS
                translation_content = LANGUAGE_DEFAULTS.get(lang_key, {})
                with open(translation_path, "w", encoding="utf-8") as f:
                    json.dump(translation_content, f, indent=2, ensure_ascii=False)
                log_info(f"Created translation file: {translation_path}")
            self.translation = self.load_json(translation_path)
            self.current_language = lang_key
            log_info(f"Loaded translation for language: {lang_key}")
        except Exception as e:
            log_exception(f"Error loading/creating translation file for {lang_key}", e)

    def refresh_center_panel_texts(self):
        """
        Aktualisiert alle Texte im Center Panel und Right Panel nach Sprachwechsel.
        """
        try:
            self.header_label.setText(self.translation.get("start_window_text_1", "CSNova"))
            flow_text_1 = " ".join([
                self.translation.get(f"start_window_text_{i}", "")
                for i in range(2, 8)
            ])
            self.flow_label_1.setText(flow_text_1)
            flow_text_2 = " ".join([
                self.translation.get(f"start_window_text_{i}", "")
                for i in range(8, 12)
            ])
            self.flow_label_2.setText(flow_text_2)
            # Center Panel Buttons: Korrekte Keys verwenden!
            self.save_btn.setText(self.translation.get("start_window_centerBtn_save", "Änderungen speichern"))
            self.defaults_btn.setText(self.translation.get("start_window_centerBtn_defaults", "Standardeinstellungen wiederherstellen"))
            self.next_btn.setText(self.translation.get("start_window_centerBtn_next", "weiter ..."))
            # ComboBox-Labels aktualisieren
            for idx, opt in enumerate(self.language_options):
                label = self.translation.get(opt["label_key"], opt["key"])
                self.combo.setItemText(idx, label)
            # Right Panel Buttons aktualisieren
            if hasattr(self, "right_panel_buttons"):
                for i, button in enumerate(self.right_panel_buttons, start=1):
                    key = f"botn_st_0{i}"
                    btn_text = self.translation.get(key, f"Button {i}")
                    button.setText(btn_text)
            log_info("Center and right panel texts refreshed for new language.")
        except Exception as e:
            log_exception("Error refreshing center/right panel texts.", e)

    def create_center_panel_layout(self):
        """
        Erstellt das Layout für das Center Panel mit dynamischen Fließtexten, Sprachwahl und Aktionsbuttons.
        Alle Styles und Optionen werden aus den geladenen Theme/Base-Style/Form-Fields übernommen.
        """
        try:
            layout = QVBoxLayout()
            spacing = self.theme.get("spacing", self.base_style.get("spacing", 18))
            layout.setSpacing(spacing)
            layout.setAlignment(Qt.AlignTop)

            # Header-Styles aus Theme/Base-Style
            header_style = self.theme.get("header", self.base_style.get("header", {}))
            font_size = header_style.get("font_size", self.theme.get("font_size", self.base_style.get("font_size", 28)))
            font_weight = header_style.get("font_weight", self.theme.get("font_weight", self.base_style.get("font_weight", "bold")))
            color = header_style.get("color", self.theme.get("foreground", self.base_style.get("foreground", "#222")))
            font_family = header_style.get("font_family", self.theme.get("font_family", self.base_style.get("font_family", "Arial, sans-serif")))
            margin_bottom = header_style.get("margin_bottom", self.theme.get("margin_bottom", self.base_style.get("margin_bottom", 18)))

            # Header
            self.header_label = QLabel(self.translation.get("start_window_text_1", "CSNova"))
            self.header_label.setWordWrap(True)
            self.header_label.setAlignment(Qt.AlignLeft)
            self.header_label.setStyleSheet(
                f"font-size: {font_size}px; font-weight: {font_weight}; color: {color};"
                f"margin-bottom: {margin_bottom}px; font-family: {font_family};"
            )
            layout.addWidget(self.header_label)
            layout.addSpacing(spacing)

            # Fließtext: start_window_text_2 bis start_window_text_7 als zusammenhängender Absatz
            flow_text_1 = " ".join([
                self.translation.get(f"start_window_text_{i}", "")
                for i in range(2, 8)
            ])
            self.flow_label_1 = QLabel(flow_text_1)
            self.flow_label_1.setWordWrap(True)
            self.flow_label_1.setAlignment(Qt.AlignLeft)
            apply_theme_style(self.flow_label_1, "label", self.theme)
            layout.addWidget(self.flow_label_1)
            layout.addSpacing(self.theme.get("spacing", self.base_style.get("spacing", 24)))

            # Sprachwahl-ComboBox zentriert, Optionen und Style aus form_fields.json und theme
            self.language_options = []
            for field in self.form_fields.get("preferences", []):
                if field.get("key") == "language":
                    self.language_options = field.get("options", [])
                    break
            if not self.language_options:
                self.language_options = [
                    {"key": "de", "label_key": "PreferenceLanguageDe"},
                    {"key": "en", "label_key": "PreferenceLanguageEn"},
                    {"key": "es", "label_key": "PreferenceLanguageEs"},
                    {"key": "fr", "label_key": "PreferenceLanguageFr"},
                ]
            self.combo = QComboBox()
            for opt in self.language_options:
                label = self.translation.get(opt["label_key"], opt["key"])
                self.combo.addItem(label, opt["key"])
            current_language = self.settings.get("general", {}).get("language", "de")
            idx = next((i for i, opt in enumerate(self.language_options) if opt["key"] == current_language), 0)
            self.combo.setCurrentIndex(idx)
            apply_theme_style(self.combo, "combobox", self.theme)
            self.combo.setMaximumWidth(self.theme.get("input_width", self.base_style.get("input_width", 220)))
            combo_layout = QHBoxLayout()
            combo_layout.addStretch()
            combo_layout.addWidget(self.combo)
            combo_layout.addStretch()
            layout.addLayout(combo_layout)
            layout.addSpacing(spacing)

            # Fließtext: start_window_text_8 bis start_window_text_11 als zusammenhängender Absatz
            flow_text_2 = " ".join([
                self.translation.get(f"start_window_text_{i}", "")
                for i in range(8, 12)
            ])
            self.flow_label_2 = QLabel(flow_text_2)
            self.flow_label_2.setWordWrap(True)
            self.flow_label_2.setAlignment(Qt.AlignLeft)
            apply_theme_style(self.flow_label_2, "label", self.theme)
            layout.addWidget(self.flow_label_2)

            # Aktionsbuttons zentriert am unteren Rand (jetzt 3 Buttons)
            button_layout = QHBoxLayout()
            button_layout.addStretch()
            self.save_btn = QPushButton(self.translation.get("start_window_centerBtn_save", "Änderungen speichern"))
            self.defaults_btn = QPushButton(self.translation.get("start_window_centerBtn_defaults", "Standardeinstellungen wiederherstellen"))
            self.next_btn = QPushButton(self.translation.get("start_window_centerBtn_next", "weiter ..."))
            apply_theme_style(self.save_btn, "button", self.theme)
            apply_theme_style(self.defaults_btn, "button", self.theme)
            apply_theme_style(self.next_btn, "button", self.theme)
            self.save_btn.setEnabled(False)
            self.defaults_btn.setEnabled(False)
            self.next_btn.setEnabled(True)  # "Weiter"-Button ist immer aktiv
            button_layout.addWidget(self.save_btn)
            button_layout.addSpacing(self.theme.get("button_spacing", self.base_style.get("button_spacing", 24)))
            button_layout.addWidget(self.defaults_btn)
            button_layout.addSpacing(self.theme.get("button_spacing", self.base_style.get("button_spacing", 24)))
            button_layout.addWidget(self.next_btn)
            button_layout.addStretch()
            layout.addSpacing(spacing)
            layout.addLayout(button_layout)

            # Sprachänderung-Callback
            def on_language_changed(index):
                selected_key = self.combo.itemData(index)
                if selected_key != self.original_language:
                    self.language_changed = True
                    # Temporär: Lade neue Übersetzungen und zeige sie an
                    self.load_translation_for_language(selected_key)
                    self.refresh_center_panel_texts()
                    log_info(f"Language changed to: {selected_key} (temporarily applied)")
                    self.update_action_buttons()
                else:
                    # Sprache zurückgesetzt
                    self.language_changed = False
                    self.load_translation_for_language(self.original_language)
                    self.refresh_center_panel_texts()
                    self.update_action_buttons()
            self.combo.currentIndexChanged.connect(on_language_changed)

            # Button-Callbacks
            def on_save_clicked():
                if self.language_changed:
                    # Speichere die neue Sprache als Standard
                    self.settings["general"]["language"] = self.current_language
                    self.save_settings()
                    self.original_language = self.current_language
                    self.language_changed = False
                    log_info(f"Settings saved. Language set to: {self.current_language}")
                    self.update_action_buttons()
            self.save_btn.clicked.connect(on_save_clicked)

            def on_restore_defaults_clicked():
                # Setze Sprache auf ursprüngliche Sprache zurück
                self.load_translation_for_language(self.original_language)
                self.refresh_center_panel_texts()
                idx = next((i for i, opt in enumerate(self.language_options) if opt["key"] == self.original_language), 0)
                self.combo.setCurrentIndex(idx)
                self.language_changed = False
                log_info("Settings restored to original language.")
                self.update_action_buttons()
            self.defaults_btn.clicked.connect(on_restore_defaults_clicked)

            def on_next_clicked():
                log_info("Next button clicked.")
                # Hier weitere Aktionen für den nächsten Schritt ergänzen
            self.next_btn.clicked.connect(on_next_clicked)

            # Hilfsfunktion zum Aktualisieren der Button-States
            def update_action_buttons():
                self.save_btn.setEnabled(self.language_changed)
                self.defaults_btn.setEnabled(self.language_changed)
            self.update_action_buttons = update_action_buttons

            self.update_action_buttons()
            return layout
        except Exception as e:
            log_exception("Error creating center panel layout.", e)
            return QVBoxLayout()

    def init_ui(self):
        """
        Initialisiert das UI: Splitter, Panels und Layouts.
        Alle Daten werden aus den generierten JSON-Dateien geladen.
        """
        try:
            splitter_sizes = self.settings.get("panels", {}).get("splitter_sizes", [200, 1200, 520])
            self.splitter = QSplitter(Qt.Horizontal)
            left_panel = QWidget()
            center_panel = QWidget()
            right_panel = QWidget()
            self.splitter.addWidget(left_panel)
            self.splitter.addWidget(center_panel)
            self.splitter.addWidget(right_panel)
            self.splitter.setSizes(splitter_sizes)

            self.apply_panel_style(left_panel)
            self.apply_panel_style(center_panel)
            self.apply_panel_style(right_panel)

            win_size = self.settings.get("start_window", {})
            width = win_size.get("width", 1920)
            height = win_size.get("height", 1080)

            center_panel.setLayout(self.create_center_panel_layout())

            # Beispiel: Buttons im rechten Panel, Texte aus Translation
            right_layout = QVBoxLayout()
            self.right_panel_buttons = []
            for i in range(1, 6):
                key = f"botn_st_0{i}"
                btn_text = self.translation.get(key, f"Button {i}")
                button = QPushButton(btn_text)
                apply_theme_style(button, "button", self.theme)
                right_layout.addWidget(button)
                self.right_panel_buttons.append(button)
            right_panel.setLayout(right_layout)
            
            main_widget = QWidget()
            main_layout = QVBoxLayout()
            main_layout.addWidget(self.splitter)
            main_widget.setLayout(main_layout)
            self.setCentralWidget(main_widget)

            self.resize(width, height)

            self.splitter.splitterMoved.connect(self.on_splitter_moved)
            self.resizeEvent = self.on_resize_event

            log_info("UI initialized in StartWindow.")
        except Exception as e:
            log_exception("Error initializing UI in StartWindow.", e)

    def apply_panel_style(self, panel):
        """
        Wendet das Theme und die Basis-Styles auf ein Panel an.
        Args:
            panel (QWidget): Das Panel, das gestylt werden soll.
        """
        try:
            style_dict = self.theme.copy()
            style_dict.update(self.base_style.get("QWidget", {}))
            apply_theme_style(panel, "panel", style_dict)
        except Exception as e:
            log_exception("Error applying panel style.", e)

    def on_splitter_moved(self, pos, index):
        """
        Speichert die neuen Splitter-Größen und passt die Center Panel-Breite an.
        Args:
            pos (int): Position des Splitters.
            index (int): Index des Splitters.
        """
        try:
            sizes = self.splitter.sizes()
            self.settings.setdefault("panels", {})
            self.settings["panels"]["splitter_sizes"] = sizes
            self.save_settings()
            self.update_center_panel_width()
            log_info(f"Splitter moved: {sizes}")
        except Exception as e:
            log_exception("Error handling splitter moved.", e)

    def on_resize_event(self, event):
        """
        Speichert die neue Fenstergröße und passt die Center Panel-Breite an.
        Args:
            event (QResizeEvent): Das Resize-Event.
        """
        try:
            size = self.size()
            self.settings.setdefault("start_window", {})
            self.settings["start_window"]["width"] = size.width()
            self.settings["start_window"]["height"] = size.height()
            self.save_settings()
            self.update_center_panel_width()
            log_info(f"Window resized: {size.width()}x{size.height()}")
            QMainWindow.resizeEvent(self, event)
        except Exception as e:
            log_exception("Error handling resize event.", e)

    def update_center_panel_width(self):
        """
        Setzt die maximale Breite aller Widgets im Center Panel dynamisch.
        """
        try:
            center_panel = self.splitter.widget(1)
            center_panel_width = center_panel.width()
            layout = center_panel.layout()
            for i in range(layout.count()):
                item = layout.itemAt(i)
                widget = item.widget()
                if widget:
                    widget.setMaximumWidth(center_panel_width)
            log_info(f"Center panel width updated: {center_panel_width}")
        except Exception as e:
            log_exception("Error updating center panel width.", e)

    def showEvent(self, event):
        """
        Wird beim Anzeigen des Fensters aufgerufen und setzt die Panel-Breite korrekt.
        """
        try:
            super().showEvent(event)
            self.update_center_panel_width()
        except Exception as e:
            log_exception("Error in showEvent.", e)

    def run(self):
        """
        Zeigt das Fenster an.
        """
        try:
            self.show()
            self.update_center_panel_width()
            log_info("StartWindow shown.")
        except Exception as e:
            log_exception("Error showing StartWindow.", e)