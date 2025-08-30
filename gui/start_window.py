# main window with buttons for create a new project, load an existing project
# main settings for GUI positions and changing after resizing the window
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import QTimer
from core.translations.translations import LANGUAGES, TRANSLATIONS
from gui.preferences import PreferencesWindow
from core.translator import Translator
from gui.project_window import ProjectWindow
from gui.styles.style_utils import load_button_style  # Import the style loader

import sys

# Import zentrale Logging-Funktionen
from core.lloger import log_section, log_subsection, log_info, log_error

class StartWindow(QWidget):
    DEFAULT_WIDTH        = 1920
    DEFAULT_HEIGHT       = 1080
    BUTTON_WIDTH         = 240
    BUTTON_HEIGHT        = 70
    BUTTON_TOP_OFFSET    = 220
    BUTTON_LEFT_OFFSET   = 1380
    BUTTON_SPACING       = 44

    def __init__(self, default_language="en"):
        log_section("start_window.py")
        log_subsection("__init__")
        try:
            super().__init__()
            self.translator = Translator(default=default_language)
            self.setWindowTitle(self.translator.tr("start_window_title"))
            self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
            self.setAutoFillBackground(False)
            self.bg_pixmap = QPixmap(
                "/home/frank/Dokumente/CSNova/assets/media/csNova_background_start.png"
            )

            self.pref_window = None  # Track preferences window
            self._create_ui()
            self._retranslate_and_position()
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing StartWindow: {str(e)}")

    def _create_ui(self):
        log_subsection("_create_ui")
        try:
            # Button keys for translation
            self.button_keys = [
                "btn_new_project",
                "btn_load_project",
                "btn_settings",
                "btn_help",
                "btn_exit"
            ]

            self.buttons = []
            for key in self.button_keys:
                btn = QPushButton(parent=self)
                shadow = QGraphicsDropShadowEffect(btn)
                shadow.setBlurRadius(10)
                shadow.setXOffset(4)
                shadow.setYOffset(4)
                shadow.setColor(QColor(0, 0, 0, 80))
                btn.setGraphicsEffect(shadow)
                self.buttons.append(btn)

            # Connect new_project button
            self.buttons[0].clicked.connect(self._new_project)

            # Connect load_project button
            self.buttons[1].clicked.connect(self._load_project)

            # Connect settings button
            self.buttons[2].clicked.connect(self._open_preferences)

            # Connect help button
            self.buttons[3].clicked.connect(self._help)

            # Connect exit button
            self.buttons[4].clicked.connect(self._exit_application)
            log_info("UI created and buttons connected.")
        except Exception as e:
            log_error(f"Error creating UI: {str(e)}")

    def _open_preferences(self):
        log_subsection("_open_preferences")
        try:
            # Open preferences window only if not already open
            if self.pref_window is None or not self.pref_window.isVisible():
                self.pref_window = PreferencesWindow(self)
                self.pref_window.show()
                log_info("Preferences window opened.")
            else:
                self.pref_window.raise_()
                self.pref_window.activateWindow()
                log_info("Preferences window focused.")
        except Exception as e:
            log_error(f"Error opening preferences window: {str(e)}")

    def _new_project(self):
        log_subsection("_new_project")
        try:
            log_info("Preparing new project...")
            self.project_window = ProjectWindow(translator=self.translator)
            self.project_window.show()
            QTimer.singleShot(100, lambda: self.hide())
            log_info("ProjectWindow shown and StartWindow hidden.")
        except Exception as e:
            log_error(f"Error preparing new project: {str(e)}")

    def _load_project(self):
        log_subsection("_load_project")
        try:
            log_info("Preparing to load project...")
            # Implement loading logic here
        except Exception as e:
            log_error(f"Error preparing to load project: {str(e)}")

    def _help(self):
        log_subsection("_help")
        try:
            log_info("Preparing help function...")
            # Implement help logic here
        except Exception as e:
            log_error(f"Error preparing help function: {str(e)}")

    def _exit_application(self):
        log_subsection("_exit_application")
        try:
            log_info("Exiting application...")
            QApplication.instance().quit()
        except Exception as e:
            log_error(f"Error during application exit: {str(e)}")

    def _on_language_changed(self, code):
        log_subsection("_on_language_changed")
        try:
            self.translator.set_language(code)
            self._retranslate_and_position()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_error(f"Error changing language: {str(e)}")

    def _retranslate_and_position(self):
        log_subsection("_retranslate_and_position")
        try:
            # Update button texts and window title
            for key, btn in zip(self.button_keys, self.buttons):
                btn.setText(self.translator.tr(key))
            self.setWindowTitle(self.translator.tr("start_window_title"))
            self.update_button_positions()
            log_info("Button texts and window title updated.")
        except Exception as e:
            log_error(f"Error updating translations and positions: {str(e)}")

    def paintEvent(self, event):
        # Draw background image scaled and centered
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

    def resizeEvent(self, event):
        # Update button positions on resize
        self.update_button_positions()
        super().resizeEvent(event)

    def update_button_positions(self):
        log_subsection("update_button_positions")
        try:
            # Dynamically position and style buttons
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
            style = load_button_style(font_px)  # Use the imported style loader
            for i, btn in enumerate(self.buttons):
                x = int(x_off)
                y = int(y_off + i * (bh + spacing))
                btn.setGeometry(x, y, bw, bh)
                btn.setStyleSheet(style)
            log_info("Button positions updated.")
        except Exception as e:
            log_error(f"Error updating button positions: {str(e)}")

if __name__ == "__main__":
    log_section("start_window.py")
    log_subsection("__main__")
    try:
        app = QApplication(sys.argv)
        window = StartWindow(default_language="en")
        window.show()
        log_info("StartWindow shown.")
        sys.exit(app.exec())
    except Exception as e:
        log_error(f"Error in main: {str(e)}")