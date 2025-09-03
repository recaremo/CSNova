import sys
import json
from PySide6.QtWidgets import QApplication
from core.translator import Translator
from config.dev import USER_SETTINGS_FILE
from gui.start_window import StartWindow
from core.logger import log_section, log_subsection, log_info, log_exception
from gui.styles.form_styles import load_global_stylesheet

def load_language():
    """
    Loads the language from user_settings.json, defaults to 'en' if not set.
    """
    try:
        with open(USER_SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
        return settings.get("language", "en")
    except Exception as e:
        log_exception("Error loading language from user_settings.json", e)
        return "en"

def main():
    log_section("csNova.py")
    log_subsection("main")
    try:
        app = QApplication(sys.argv)
        app.setStyleSheet(load_global_stylesheet())
        language = load_language()
        translator = Translator(language)
        window = StartWindow(default_language=language)
        window.show()
        log_info("csNova main window shown.")
        sys.exit(app.exec())
    except Exception as e:
        log_exception("Error in csNova main execution", e)

if __name__ == "__main__":
    main()