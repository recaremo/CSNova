import sys
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings, save_settings

from gui.start_window import StartWindow

def main():
    try:
        # Initialisiere Datenbank und lade Einstellungen
        init_schema()
        settings = load_settings()
        language = settings.get("language", "en")

        # Starte Anwendung und öffne Startfenster
        app = QApplication(sys.argv)
        window = StartWindow(default_language=language)
        window.show()
        app.exec()

        # Sprache speichern, ohne andere Einstellungen zu überschreiben
        if hasattr(window, "translator") and hasattr(window.translator, "lang"):
            updated_settings = load_settings()
            updated_settings["language"] = window.translator.lang
            save_settings(updated_settings)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
