from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.form_styles import load_form_style

class FormCenterStart(QWidget):
    """
    Placeholder widget for the initial empty state of CenterPanel.
    Displays a message or nothing until a form is selected.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(load_form_style())
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)
        # Show placeholder text in the center
        label = QLabel("Hier Inhalte ergänzen", self)
        label.setObjectName("CenterStartLabel")
        label.setStyleSheet("font-size: 18px; color: #888; margin-top: 120px;")
        layout.addWidget(label)
        layout.addStretch()
        self.setLayout(layout)