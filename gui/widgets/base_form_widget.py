from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QDateEdit, QSpinBox
from gui.widgets.form_toolbar import FormToolbar
from gui.styles.form_styles import load_form_style

# Import zentrale Logging-Funktionen
from core.lloger import log_section, log_subsection, log_info, log_error

class BaseFormWidget(QWidget):
    def __init__(self, title, fields, form_labels, toolbar_actions, parent=None):
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            style = load_form_style(16)
            layout = QVBoxLayout()
            
            # Toolbar
            self.toolbar = FormToolbar(self)
            toolbar_actions(self.toolbar)
            layout.addWidget(self.toolbar)
            
            # Überschrift
            title_label = QLabel(title)
            title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 12px;")
            layout.addWidget(title_label)
            
            # Formlayout
            form_layout = QFormLayout()
            self.field_widgets = {}
            for field in fields:
                label_text = form_labels.get(field["label_key"], field["default_label"])
                if field["type"] == "text":
                    widget = QLineEdit()
                elif field["type"] == "date":
                    widget = QDateEdit()
                    widget.setCalendarPopup(True)
                elif field["type"] == "spin":
                    widget = QSpinBox()
                    widget.setMaximum(field.get("max", 100000))
                else:
                    continue
                widget.setStyleSheet(style)
                form_layout.addRow(label_text, widget)
                self.field_widgets[field["name"]] = widget
            layout.addLayout(form_layout)
            self.setLayout(layout)
            log_info("BaseFormWidget initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing BaseFormWidget: {str(e)}")