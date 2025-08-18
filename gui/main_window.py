# gui/main_window.py

from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QMenuBar, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from gui.tabs.project_tab import ProjectTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Codex Scriptoria Nova")
        self.setMinimumSize(1024, 768)

        self._create_menu_bar()
        self._create_tabs()

    def _create_menu_bar(self):
        menu_bar = QMenuBar(self)
        file_menu = QMenu("Datei", self)

        new_action = QAction("Neu", self)
        open_action = QAction("Öffnen", self)
        save_action = QAction("Speichern", self)
        exit_action = QAction("Beenden", self)
        exit_action.triggered.connect(self.close)

        file_menu.addActions([new_action, open_action, save_action, exit_action])
        menu_bar.addMenu(file_menu)
        self.setMenuBar(menu_bar)

    def _create_tabs(self):
        tabs = QTabWidget()
        tabs.addTab(ProjectTab(), "Projekt")
        tabs.addTab(QWidget(), "Charakter")
        tabs.addTab(QWidget(), "Szene")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(tabs)
        self.setCentralWidget(central_widget)


