import sys
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings
from gui.start_window import StartWindow

def main():
    init_schema()
    settings = load_settings()
    language = settings.get("language", "de")

    app = QApplication(sys.argv)
    # Übergebe Default-Sprache an das Startfenster
    window = StartWindow(default_language=language)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()