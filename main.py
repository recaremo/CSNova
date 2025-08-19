import sys
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from gui.main_window import MainWindow
from config.settings import load_settings
from gui.start_window import StartWindow

def main():
    init_schema()  # Tabellen erzeugen
    settings = load_settings()
    language = settings.get("language", "de")

    app = QApplication(sys.argv)
    #window = MainWindow(language=language)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()

