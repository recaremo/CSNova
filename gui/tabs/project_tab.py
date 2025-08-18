from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QHBoxLayout

class ProjectTab(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()

        title = QLabel("📘 Projektübersicht")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.project_list = QListWidget()
        layout.addWidget(self.project_list)

        button_layout = QHBoxLayout()
        self.new_button = QPushButton("Neu")
        self.edit_button = QPushButton("Bearbeiten")
        self.delete_button = QPushButton("Löschen")

        button_layout.addWidget(self.new_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)
