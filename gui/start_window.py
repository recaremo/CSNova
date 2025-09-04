import sys
import json
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import QTimer
from gui.preferences import PreferencesWindow
from core.translator import Translator
from gui.project_window import ProjectWindow
from gui.styles.form_styles import load_button_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import BG_IMAGE_PATH, USER_SETTINGS_FILE
from config.settings import load_settings

class StartWindow(QWidget):
    """
    Main window for CSNova application.
    Handles initialization, button layout, translations, and saving window settings.
    Robust error handling is implemented for all UI and file operations.
    """
    def __init__(self, default_language="en"):
        """
        Initializes the StartWindow.
        Loads settings, sets up translations, window size, background, and buttons.
        """
        log_section("start_window.py")
        log_subsection("__init__")
        try:
            super().__init__()
            self.settings = load_settings()
            lang = self.settings.get("language", default_language)
            self.translator = Translator(lang)
            self.setWindowTitle(self.translator.tr("WinStartTitle"))
            # Set window size from settings
            res = self.settings.get("screen_resolution", "1920x1080")
            w, h = [int(x) for x in res.split("x")]
            self.resize(w, h)
            self.setAutoFillBackground(False)
            try:
                self.bg_pixmap = QPixmap(str(BG_IMAGE_PATH))
            except Exception as e:
                log_exception("Error loading background image", e)
                self.bg_pixmap = QPixmap(w, h)
            self.pref_window = None
            # Load button layout values from settings
            self.BUTTON_WIDTH      = self.settings.get("start_window_bnt_width", 240)
            self.BUTTON_HEIGHT     = self.settings.get("start_window_bnt_height", 60)
            self.BUTTON_TOP_OFFSET = self.settings.get("start_window_bnt_top_offset", 270)
            self.BUTTON_LEFT_OFFSET= self.settings.get("start_window_bnt_left_offset", 1350)
            self.BUTTON_SPACING    = self.settings.get("start_window_bnt_spacing", 42)
            self._create_ui()
            self._retranslate_and_position()
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartWindow", e)

    def _create_ui(self):
        """
        Creates all main buttons for the start window and connects their signals.
        Applies drop shadow effects for better visuals.
        Robust error handling for UI creation.
        """
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
                try:
                    shadow = QGraphicsDropShadowEffect(btn)
                    shadow.setBlurRadius(10)
                    shadow.setXOffset(4)
                    shadow.setYOffset(4)
                    shadow.setColor(QColor(0, 0, 0, 80))
                    btn.setGraphicsEffect(shadow)
                except Exception as e:
                    log_exception("Error applying drop shadow effect", e)
                self.buttons.append(btn)
            # Connect button actions
            try:
                self.buttons[0].clicked.connect(self._new_project)
                self.buttons[1].clicked.connect(self._load_project)
                self.buttons[2].clicked.connect(self._open_preferences)
                self.buttons[3].clicked.connect(self._help)
                self.buttons[4].clicked.connect(self._exit_application)
            except Exception as e:
                log_exception("Error connecting button signals", e)
            log_info("UI created and buttons connected.")
        except Exception as e:
            log_exception("Error creating UI", e)

    def _open_preferences(self):
        """
        Opens the preferences dialog window.
        If already open, brings it to the front.
        Robust error handling for preferences window.
        """
        log_subsection("_open_preferences")
        try:
            if self.pref_window is None or not self.pref_window.isVisible():
                self.pref_window = PreferencesWindow(self)
                self.pref_window.show()
                log_info("Preferences window opened.")
            else:
                self.pref_window.raise_()
                self.pref_window.activateWindow()
                log_info("Preferences window focused.")
        except Exception as e:
            log_exception("Error opening preferences window", e)

    def _new_project(self):
        """
        Opens the project window for creating a new project.
        Hides the start window.
        Robust error handling for project window.
        """
        log_subsection("_new_project")
        try:
            log_info("Preparing new project...")
            self.project_window = ProjectWindow(translator=self.translator, parent=None, start_window=self)
            self.project_window.show()
            self.hide()
            QTimer.singleShot(100, lambda: self.hide())
            log_info("ProjectWindow shown and StartWindow hidden.")
        except Exception as e:
            log_exception("Error preparing new project", e)

    def _load_project(self):
        """
        Placeholder for loading an existing project.
        Robust error handling for load project.
        """
        log_subsection("_load_project")
        try:
            log_info("Preparing to load project...")
            # Implement loading logic here
        except Exception as e:
            log_exception("Error preparing to load project", e)

    def _help(self):
        """
        Placeholder for help and tutorial functionality.
        Robust error handling for help function.
        """
        log_subsection("_help")
        try:
            log_info("Preparing help function...")
            # Implement help logic here
        except Exception as e:
            log_exception("Error preparing help function", e)

    def _exit_application(self):
        """
        Exits the application.
        Robust error handling for application exit.
        """
        log_subsection("_exit_application")
        try:
            log_info("Exiting application...")
            QApplication.instance().quit()
        except Exception as e:
            log_exception("Error during application exit", e)

    def _on_language_changed(self, code):
        """
        Changes the application language and updates all translations.
        Robust error handling for language change.
        """
        log_subsection("_on_language_changed")
        try:
            self.translator.set_language(code)
            self.settings["language"] = code
            self._retranslate_and_position()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language", e)

    def _retranslate_and_position(self):
        """
        Updates all button texts and window title after a language change.
        Also updates button positions.
        Robust error handling for translation and positioning.
        """
        log_subsection("_retranslate_and_position")
        try:
            for key, btn in zip(self.button_keys, self.buttons):
                btn.setText(self.translator.tr(key))
            self.setWindowTitle(self.translator.tr("WinStartTitle"))
            self.update_button_positions()
            log_info("Button texts and window title updated.")
        except Exception as e:
            log_exception("Error updating translations and positions", e)

    def paintEvent(self, event):
        """
        Paints the background image, scaled to fit the window size.
        Robust error handling for painting.
        """
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
        """
        Handles window resize events.
        Updates button positions and saves new window settings.
        Robust error handling for resize event.
        """
        try:
            self.update_button_positions()
            self.save_window_settings()
            super().resizeEvent(event)
        except Exception as e:
            log_exception("Error handling resize event", e)
    
    def update_translations(self):
        """
        Updates translations after a language change.
        Called by PreferencesWindow.
        Robust error handling for translation update.
        """
        try:
            self.settings = load_settings()
            lang = self.settings.get("language", "en")
            self.translator.set_language(lang)
            self._retranslate_and_position()
        except Exception as e:
            log_exception("Error updating translations in StartWindow", e)
       
    def update_button_positions(self):
        """
        Calculates and sets the positions and sizes of all buttons
        based on the current window size and scaling.
        Robust error handling for button positioning.
        """
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
            font_px = max(10, int(bh * 0.4))
            style = load_button_style(font_px)
            for i, btn in enumerate(self.buttons):
                x = int(x_off)
                y = int(y_off + i * (bh + spacing))
                btn.setGeometry(x, y, bw, bh)
                btn.setStyleSheet(style)
            log_info("Button positions updated.")
        except Exception as e:
            log_exception("Error updating button positions", e)

    def save_window_settings(self):
        """
        Saves the current window size and button layout values to user_settings.json.
        Called after window resize.
        Robust error handling for saving window settings.
        """
        try:
            settings = load_settings()
            settings["screen_resolution"] = f"{self.width()}x{self.height()}"
            settings["start_window_bnt_width"] = self.BUTTON_WIDTH
            settings["start_window_bnt_height"] = self.BUTTON_HEIGHT
            settings["start_window_bnt_top_offset"] = self.BUTTON_TOP_OFFSET
            settings["start_window_bnt_left_offset"] = self.BUTTON_LEFT_OFFSET
            settings["start_window_bnt_spacing"] = self.BUTTON_SPACING
            with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=2)
            log_info("Window settings saved to user_settings.json.")
        except Exception as e:
            log_exception("Error saving window settings", e)

if __name__ == "__main__":
    """
    Main entry point for standalone execution of StartWindow.
    Initializes the application and shows the start window.
    Robust error handling for main execution.
    """
    log_section("start_window.py")
    log_subsection("__main__")
    try:
        app = QApplication(sys.argv)
        window = StartWindow()
        window.show()
        log_info("StartWindow shown.")
        sys.exit(app.exec())
    except Exception as e:
        log_exception("Error in main execution", e)