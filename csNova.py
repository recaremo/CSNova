import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings, save_settings
from gui.start_window import StartWindow
from gui.styles.form_styles import load_global_stylesheet

# Import central logging functions
from core.logger import setup_logging, log_header, log_section, log_subsection, log_info, log_error, log_exception

def main():
    setup_logging()  # Only once at program start
    log_header()
    log_section("csnova.py")
    log_subsection("main")
    try:
        log_info("Initializing database schema.")
        try:
            init_schema()
        except Exception as e:
            log_exception("Error initializing database schema", e)

        log_info("Loading settings.")
        try:
            settings = load_settings()
        except Exception as e:
            log_exception("Error loading settings", e)
            settings = {"language": "en"}

        language = settings.get("language", "en")
        log_info(f"Language set to '{language}'.")

        try:
            app = QApplication(sys.argv)
            app.setStyleSheet(load_global_stylesheet())  # Apply global stylesheet
            window = StartWindow(default_language=language)
            window.show()
            log_info("StartWindow shown.")
            app.exec()
        except Exception as e:
            log_exception("Error initializing GUI", e)

        # Save updated language setting if changed
        try:
            if hasattr(window, "translator") and hasattr(window.translator, "lang"):
                updated_settings = load_settings()
                updated_settings["language"] = window.translator.lang
                save_settings(updated_settings)
                log_info(f"Language updated to '{window.translator.lang}' in settings.")
        except Exception as e:
            log_exception("Error saving updated language setting", e)

    except Exception as e:
        log_exception("An error occurred in main()", e)

if __name__ == "__main__":
    main()