# gui/main_window.py

from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QMenuBar, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from gui.tabs.project_tab import ProjectTab
from core.translations import TRANSLATIONS
from config.settings import save_settings

class MainWindow(QMainWindow):
    def __init__(self, language="de"):
        super().__init__()
        self.current_lang = language
        self.setWindowTitle("Codex Scriptoria Nova")
        self.setMinimumSize(1024, 768)

        self._create_menu_bar()
        self._create_tabs()

    def _create_menu_bar(self):
        tr = TRANSLATIONS[self.current_lang]

        menu_bar = QMenuBar(self)
        file_menu = QMenu(tr["menu_file"], self)

        settings_menu = QMenu(tr["menu_settings"], self)
        language_menu = QMenu(tr["menu_language"], self)

        languages = [("de", "Deutsch"), ("en", "English"), ("fr", "Français"), ("es", "Español")]
        for code, name in languages:
            lang_action = QAction(name, self)
            lang_action.triggered.connect(lambda checked, c=code: self.change_language(c))
            language_menu.addAction(lang_action)

        settings_menu.addMenu(language_menu)
        menu_bar.addMenu(settings_menu)

        new_action = QAction(tr["action_new"], self)
        open_action = QAction(tr["action_open"], self)
        save_action = QAction(tr["action_save"], self)
        exit_action = QAction(tr["action_exit"], self)
        exit_action.triggered.connect(self.close)

        file_menu.addActions([new_action, open_action, save_action, exit_action])
        menu_bar.addMenu(file_menu)
        self.setMenuBar(menu_bar)

    def change_language(self, lang_code):
        self.current_lang = lang_code
        save_settings({"language": lang_code})
        self.menuBar().clear()
        self._create_menu_bar()
        self._create_tabs()

    def _create_tabs(self):
        tr = TRANSLATIONS[self.current_lang]

        tabs = QTabWidget()
        tabs.addTab(ProjectTab(), tr["tab_project"])
        tabs.addTab(QWidget(), tr["tab_character"])
        tabs.addTab(QWidget(), tr["tab_scene"])

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(tabs)
        self.setCentralWidget(central_widget)
