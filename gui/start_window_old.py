from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import QTimer
from core.translations import LANGUAGES, TRANSLATIONS
from gui.preferences import PreferencesWindow
import sys

class Translator:
    def __init__(self, default="de"):
        self.lang = default if default in LANGUAGES else LANGUAGES[0]

    def set_language(self, lang_code):
        if lang_code in TRANSLATIONS:
            self.lang = lang_code

    def tr(self, key):
        return TRANSLATIONS[self.lang].get(
            key, TRANSLATIONS["en"].get(key, key)
        )

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
        self.setWindowTitle("Codices Scriptoria Nova (CSNova)")
        self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
        self.setAutoFillBackground(False)
        base_path = os.path.dirname(__file__)
        pix_path = os.path.join(base_path, "..", "assets", "media", "csNova_background_start.png")
        self.bg_pixmap = QPixmap(pix_path)
    

        self.translator = Translator(default=default_language)
        self._create_ui()
        QTimer.singleShot(0, self._retranslate_and_position)

    def _create_ui(self):
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

        # Einstellungen-Button verbinden
        self.buttons[2].clicked.connect(self._open_preferences)

        # Platzhalter für weitere Buttons
        self.buttons[0].clicked.connect(self._new_project_placeholder)
        self.buttons[1].clicked.connect(self._load_project_placeholder)
        self.buttons[3].clicked.connect(self._help_placeholder)

        # Beenden-Button verbinden
        self.buttons[4].clicked.connect(self._exit_application)

    def _open_preferences(self):
        self.pref_window = PreferencesWindow(self)
        self.pref_window.show()

    def _new_project_placeholder(self):
        print("Neues Projekt wird vorbereitet…")

    def _load_project_placeholder(self):
        print("Projekt laden wird vorbereitet…")

    def _help_placeholder(self):
        print("Hilfefunktion wird vorbereitet…")

    def _exit_application(self):
        QApplication.instance().quit()

    def _on_language_changed(self, code):
        self.translator.set_language(code)
        self._retranslate_and_position()

    def _retranslate_and_position(self):
        for key, btn in zip(self.button_keys, self.buttons):
            btn.setText(self.translator.tr(key))
        self.update_button_positions()

    def paintEvent(self, event):
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
        self.update_button_positions()
        super().resizeEvent(event)

    def update_button_positions(self):
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
        for i, btn in enumerate(self.buttons):
            x = int(x_off)
            y = int(y_off + i * (bh + spacing))
            btn.setGeometry(x, y, bw, bh)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: #d4c29c;
                    color: #1a1a1a;
                    font-size: {font_px}px;
                    border: 2px solid #8b7d5c;
                    border-radius: 10px;
                    border-style: outset;
                }}
                QPushButton:hover {{
                    background-color: #e8d9b5;
                    border-color: #5c5138;
                }}
                QPushButton:pressed {{
                    background-color: #c0aa7a;
                    border-style: inset;
                }}
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow(default_language="de")
    window.show()
    sys.exit(app.exec())