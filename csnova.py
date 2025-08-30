import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings, save_settings
from gui.start_window import StartWindow

# Import central logging functions
from core.logger import setup_logging, log_header, log_section, log_subsection, log_info, log_error

def main():
    setup_logging()  # Only once at program start
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

        # Save updated language setting if changed
        if hasattr(window, "translator") and hasattr(window.translator, "lang"):
            updated_settings = load_settings()
            updated_settings["language"] = window.translator.lang
            save_settings(updated_settings)
            log_info(f"Language updated to '{window.translator.lang}' in settings.")

    except Exception as e:
        log_error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()