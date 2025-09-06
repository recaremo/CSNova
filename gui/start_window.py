import json
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton
)
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import QTimer
from gui.preferences import PreferencesWindow
from gui.project_window import ProjectWindow
from gui.styles.python_gui_styles import apply_theme_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import BG_IMAGE_PATH, CSNOVA_BASE_STYLE_FILE, CSNOVA_THEMES_STYLE_FILE, CSNOVA_FORMS_STYLE_FILE, BASE_STYLE_FILE, THEMES_STYLE_FILE, USER_SETTINGS_FILE, GUI_DIR, TRANSLATIONS_DIR
from core.style_utils import generate_csnova_styles, load_global_stylesheet, save_user_settings, generate_translation_file

class StartWindow(QWidget):
    """
    Main window for CSNova application.
    Handles initialization, button layout, translations, and saving window settings.
    Uses combined styles from csNova_base_style.json and csNova_themes_style.json.
    """
    def __init__(self, translation_file, settings):
        log_section("start_window.py")
        log_subsection("__init__")
        try:
            super().__init__()
            # Lade die Styles erst hier, nach sicherer Generierung durch csNova.py
            with open(CSNOVA_BASE_STYLE_FILE, "r", encoding="utf-8") as f:
                base_style = json.load(f)
            with open(CSNOVA_THEMES_STYLE_FILE, "r", encoding="utf-8") as f:
                theme_style = json.load(f)
            self.combined_style = {**base_style, **theme_style}

            with open(translation_file, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
            self.settings = settings
            self.translation_file = translation_file

            # Settings für Layout aus settings (nicht aus combined_style!)
            self.BUTTON_WIDTH      = self.settings.get("window", {}).get("start_window_bnt_width", 240)
            self.BUTTON_HEIGHT     = self.settings.get("window", {}).get("start_window_bnt_height", 60)
            self.BUTTON_TOP_OFFSET = self.settings.get("window", {}).get("start_window_bnt_top_offset", 270)
            self.BUTTON_LEFT_OFFSET= self.settings.get("window", {}).get("start_window_bnt_left_offset", 1350)
            self.BUTTON_SPACING    = self.settings.get("window", {}).get("start_window_bnt_spacing", 42)
            res = self.settings.get("monitor", {}).get("screen_resolution", "1920x1080")
            w, h = [int(x) for x in res.split("x")]
            self.resize(w, h)
            self.setAutoFillBackground(False)
            try:
                self.bg_pixmap = QPixmap(str(BG_IMAGE_PATH))
            except Exception as e:
                log_exception("Error loading background image", e)
                self.bg_pixmap = QPixmap(w, h)
            self.pref_window = None
            self._create_ui()
            self._retranslate_and_position()
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartWindow", e)

    def _create_ui(self):
        log_subsection("_create_ui")
        try:
            self.button_keys = [
                "botn_st_01",
                "botn_st_02",
                "botn_st_03",
                "botn_st_04",
                "botn_st_05"
            ]
            self.buttons = []
            for key in self.button_keys:
                btn = QPushButton(parent=self)
                apply_theme_style(btn, "button", self.combined_style)
                self.buttons.append(btn)
            self.buttons[0].clicked.connect(self._new_project)
            self.buttons[1].clicked.connect(self._load_project)
            self.buttons[2].clicked.connect(self._open_preferences)
            self.buttons[3].clicked.connect(self._help)
            self.buttons[4].clicked.connect(self._exit_application)
            log_info("UI created and buttons connected.")
        except Exception as e:
            log_exception("Error creating UI", e)

    def _open_preferences(self):
        log_subsection("_open_preferences")
        try:
            if self.pref_window is None or not self.pref_window.isVisible():
                self.pref_window = PreferencesWindow(
                    self,
                    self.settings,
                    self.translation_file,
                    self.combined_style
                )
                self.pref_window.show()
                log_info("Preferences window opened.")
            else:
                self.pref_window.raise_()
                self.pref_window.activateWindow()
                log_info("Preferences window focused.")
        except Exception as e:
            log_exception("Error opening preferences window", e)

    def _new_project(self):
        log_subsection("_new_project")
        try:
            log_info("Preparing new project...")
            self.project_window = ProjectWindow(parent=None, start_window=self)
            self.project_window.show()
            self.hide()
            QTimer.singleShot(100, lambda: self.hide())
            log_info("ProjectWindow shown and StartWindow hidden.")
        except Exception as e:
            log_exception("Error preparing new project", e)

    def _load_project(self):
        log_subsection("_load_project")
        try:
            log_info("Preparing to load project...")
            # Implement loading logic here
        except Exception as e:
            log_exception("Error preparing to load project", e)

    def _help(self):
        log_subsection("_help")
        try:
            log_info("Preparing help function...")
            # Implement help logic here
        except Exception as e:
            log_exception("Error preparing help function", e)

    def _exit_application(self):
        log_subsection("_exit_application")
        try:
            log_info("Exiting application...")
            QApplication.instance().quit()
        except Exception as e:
            log_exception("Error during application exit", e)

    def _on_language_changed(self, code, translation_file):
        log_subsection("_on_language_changed")
        try:
            with open(translation_file, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
            self._retranslate_and_position()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language", e)

    def _retranslate_and_position(self):
        log_subsection("_retranslate_and_position")
        try:
            for key, btn in zip(self.button_keys, self.buttons):
                btn.setText(self.translations.get(key, key))
            self.setWindowTitle(self.translations.get("WinStartTitle", "CSNova"))
            self.update_button_positions()
            log_info("Button texts and window title updated.")
        except Exception as e:
            log_exception("Error updating translations and positions", e)

    def paintEvent(self, event):
        try:
            painter = QPainter(self)
            rect = self.contentsRect()
            w, h = rect.width(), rect.height()
            pw, ph = self.bg_pixmap.width(), self.bg_pixmap.height()
            scale = max(w / pw, h / ph)
            sw, sh = pw * scale, ph * scale
            x_off = rect.x() + (w - sw) / 2
            y_off = rect.y() + (h - sh) / 2
            painter.drawPixmap(
                int(x_off), int(y_off),
                int(sw),   int(sh),
                self.bg_pixmap
            )
            super().paintEvent(event)
        except Exception as e:
            log_exception("Error painting background", e)

    def resizeEvent(self, event):
        try:
            self.update_button_positions()
            super().resizeEvent(event)
        except Exception as e:
            log_exception("Error handling resize event", e)
    
    def update_button_positions(self):
        log_subsection("update_button_positions")
        try:
            rect = self.contentsRect()
            w, h = rect.width(), rect.height()
            pw, ph = self.bg_pixmap.width(), self.bg_pixmap.height()
            scale = max(w / pw, h / ph)
            sw, sh = pw * scale, ph * scale
            x_off = rect.x() + (w - sw) / 2 + self.BUTTON_LEFT_OFFSET * scale
            y_off = rect.y() + (h - sh) / 2 + self.BUTTON_TOP_OFFSET  * scale
            bw      = int(self.BUTTON_WIDTH   * scale)
            bh      = int(self.BUTTON_HEIGHT  * scale)
            spacing = int(self.BUTTON_SPACING * scale)
            for i, btn in enumerate(self.buttons):
                x = int(x_off)
                y = int(y_off + i * (bh + spacing))
                btn.setGeometry(x, y, bw, bh)
                apply_theme_style(btn, "button", self.combined_style)
            log_info("Button positions updated.")
        except Exception as e:
            log_exception("Error updating button positions", e)

    # Callback-Methoden für PreferencesWindow
    def on_style_changed(self, style):
        self.settings["gui"]["style"] = style
        self.combined_style = generate_csnova_styles(
            self.settings,
            BASE_STYLE_FILE,
            THEMES_STYLE_FILE,
            CSNOVA_BASE_STYLE_FILE,
            CSNOVA_THEMES_STYLE_FILE,
            CSNOVA_FORMS_STYLE_FILE,
            GUI_DIR
        )
        QApplication.instance().setStyleSheet(load_global_stylesheet(self.combined_style))
        for btn in self.buttons:
            apply_theme_style(btn, "button", self.combined_style)
        self._retranslate_and_position()
        save_user_settings(self.settings, USER_SETTINGS_FILE)

    def on_theme_changed(self, theme):
        self.settings["gui"]["theme"] = theme
        self.combined_style = generate_csnova_styles(
            self.settings,
            BASE_STYLE_FILE,
            THEMES_STYLE_FILE,
            CSNOVA_BASE_STYLE_FILE,
            CSNOVA_THEMES_STYLE_FILE,
            CSNOVA_FORMS_STYLE_FILE,
            GUI_DIR
        )
        QApplication.instance().setStyleSheet(load_global_stylesheet(self.combined_style))
        for btn in self.buttons:
            apply_theme_style(btn, "button", self.combined_style)
        self._retranslate_and_position()
        save_user_settings(self.settings, USER_SETTINGS_FILE)

    def on_language_changed(self, lang_code):
        self.settings["general"]["language"] = lang_code
        translation_file = generate_translation_file(lang_code, TRANSLATIONS_DIR)
        with open(translation_file, "r", encoding="utf-8") as f:
            self.translations = json.load(f)
        self._retranslate_and_position()
        save_user_settings(self.settings, USER_SETTINGS_FILE)