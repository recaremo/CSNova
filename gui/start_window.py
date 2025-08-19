from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QSize
import os

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Codices Scriptoria Nova – Start")
        self.setMinimumSize(1920, 1080)

        # Stylesheet laden
        try:
            with open("gui/styles/buttons.qss") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("⚠️ Stylesheet 'buttons.qss' nicht gefunden.")

        self._setup_ui()

    def _setup_ui(self):
        # Hintergrundbild
        background_label = QLabel(self)
        background_path = os.path.join(os.path.dirname(__file__), "..", "assets", "media", "csNova_background_large.png")
        background_pixmap = QPixmap(background_path)
        if background_pixmap.isNull():
            print(f"⚠️ Hintergrundbild konnte nicht geladen werden: {background_path}")
        else:
            background_label.setPixmap(background_pixmap)
            background_label.setScaledContents(True)
            background_label.setGeometry(self.rect())
            background_label.lower()

        main_layout = QHBoxLayout(self)

        # Logo
        logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "media", "csNova_logo_main.png")
        logo_pixmap = QPixmap(logo_path)
        if logo_pixmap.isNull():
            print(f"⚠️ Logo konnte nicht geladen werden: {logo_path}")
        else:
            logo_label.setPixmap(logo_pixmap.scaled(450, 450, Qt.KeepAspectRatioByExpanding))

        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Logo-Container mit Abstand vom linken Rand
        logo_container = QVBoxLayout()
        logo_container.setContentsMargins(500, 0, 0, 0)  # Abstand links
        logo_container.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        logo_container.addWidget(logo_label)

        # Buttons
        button_layout = QVBoxLayout()
        button_layout.setSpacing(20)
        button_layout.setAlignment(Qt.AlignCenter)

        buttons = [
            ("Neues Projekt", "newProject", "Ein neues Buchprojekt starten", self.new_project),
            ("Projekt öffnen", "openProject", "Ein bestehendes Projekt laden", self.open_project),
            ("Einstellungen", "settings", "Sprache, Layout, Speicherpfade", self.open_settings),
            ("Tutorials", "tutorials", "Hilfeseiten und Beispiele anzeigen", self.open_tutorials),
            ("Beenden", "exit", "Anwendung schließen", self.close_app),
        ]

        for label, obj_name, tooltip, slot in buttons:
            btn = QPushButton(label)
            btn.setObjectName(obj_name)
            btn.setToolTip(tooltip)
            btn.setFixedSize(200, 50)
            btn.clicked.connect(slot)

            icon_path = os.path.join("assets", "icons", f"{obj_name}.png")
            icon = QIcon(icon_path)
            if not icon.isNull():
                btn.setIcon(icon)
                btn.setIconSize(QSize(24, 24))

            button_layout.addWidget(btn)

        # Layouts zusammenfügen
        main_layout.addLayout(logo_container, 3)
        main_layout.addLayout(button_layout, 7)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        for child in self.children():
            if isinstance(child, QLabel) and child.pixmap():
                child.setGeometry(self.rect())

    # Dummy-Methoden für Buttonaktionen
    def new_project(self):
        print("Neues Projekt starten")

    def open_project(self):
        print("Projekt öffnen")

    def open_settings(self):
        print("Einstellungen öffnen")

    def open_tutorials(self):
        print("Tutorials anzeigen")

    def close_app(self):
        self.close()
