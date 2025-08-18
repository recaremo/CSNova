# main.py

import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from core.database import init_schema

def main():
    init_schema()  # Tabellen erzeugen
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
