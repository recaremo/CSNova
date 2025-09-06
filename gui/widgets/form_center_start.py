from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.python_gui_styles import apply_theme_style

class FormCenterStart(QWidget):
    """
    Placeholder widget for the initial empty state of CenterPanel.
    Displays a message or nothing until a form is selected.
    Applies centralized style from preferences/themes.
    """

    def __init__(self, parent=None, style=None):
        super().__init__(parent)
        self.style = style
        apply_theme_style(self, "panel", self.style)

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