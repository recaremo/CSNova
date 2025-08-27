from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import QTimer
from core.translations import LANGUAGES, TRANSLATIONS
from gui.preferences import PreferencesWindow
from core.translator import Translator
from gui.project_window import ProjectWindow
from gui.styles.style_utils import load_button_style  # Import the style loader

import sys

class StartWindow(QWidget):
    DEFAULT_WIDTH        = 1920
    DEFAULT_HEIGHT       = 1080
    BUTTON_WIDTH         = 240
    BUTTON_HEIGHT        = 70
    BUTTON_TOP_OFFSET    = 220
    BUTTON_LEFT_OFFSET   = 1380
    BUTTON_SPACING       = 44

    def __init__(self, default_language="de"):
        super().__init__()
        # Set window title using translator
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

    def _create_ui(self):
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

        # Connect settings button
        self.buttons[2].clicked.connect(self._open_preferences)

        # Connect placeholder buttons
        self.buttons[0].clicked.connect(self._new_project_placeholder)
        self.buttons[1].clicked.connect(self._load_project_placeholder)
        self.buttons[3].clicked.connect(self._help_placeholder)

        # Connect exit button
        self.buttons[4].clicked.connect(self._exit_application)

    def _open_preferences(self):
        # Open preferences window only if not already open
        if self.pref_window is None or not self.pref_window.isVisible():
            self.pref_window = PreferencesWindow(self)
            self.pref_window.show()
        else:
            self.pref_window.raise_()
            self.pref_window.activateWindow()

    def _new_project_placeholder(self):
        print("Preparing new project...")
        self.project_window = ProjectWindow(parent=self, translator=self.translator)
        self.project_window.show()


    def _load_project_placeholder(self):
        print("Preparing to load project...")

    def _help_placeholder(self):
        print("Preparing help function...")

    def _exit_application(self):
        QApplication.instance().quit()

    def _on_language_changed(self, code):
        self.translator.set_language(code)
        self._retranslate_and_position()

    def _retranslate_and_position(self):
        # Update button texts and window title
        for key, btn in zip(self.button_keys, self.buttons):
            btn.setText(self.translator.tr(key))
        self.setWindowTitle(self.translator.tr("window_title"))
        self.update_button_positions()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow(default_language="de")
    window.show()
    sys.exit(app.exec())