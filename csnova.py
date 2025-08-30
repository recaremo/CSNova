# Mainprogram csnova.py
import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings, save_settings
from gui.start_window import StartWindow

# Import zentrale Logging-Funktionen
from core.lloger import setup_logging, log_header, log_section, log_subsection, log_info, log_error

def main():
    setup_logging()  # Nur einmal beim Programmstart!
    log_header()
    log_section("csnova.py")
    log_subsection("main")
    try:
        log_info("Initializing database schema.")
        init_schema()
        log_info("Loading settings.")
        settings = load_settings()
        language = settings.get("language", "en")
        log_info(f"Language set to '{language}'.")

        app = QApplication(sys.argv)
        window = StartWindow(default_language=language)
        window.show()
        log_info("StartWindow shown.")
        app.exec()

        if hasattr(window, "translator") and hasattr(window.translator, "lang"):
            updated_settings = load_settings()
            updated_settings["language"] = window.translator.lang
            save_settings(updated_settings)
            log_info(f"Language updated to '{window.translator.lang}' in settings.")

    except Exception as e:
        log_error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()