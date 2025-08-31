from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QSpinBox, QDateEdit
from gui.widgets.form_toolbar import FormToolbar
from core.logger import log_section, log_subsection, log_info, log_exception

class BaseFormWidget(QWidget):
    def __init__(self, title, fields, form_labels, toolbar_actions, form_prefix, translator, parent=None):
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator  # Set translator for toolbar and labels

            self.layout = QVBoxLayout()

            # Add toolbar first for consistent UI (always at the top)
            self.toolbar = FormToolbar(self.translator, form_prefix, self)
            if toolbar_actions:
                toolbar_actions(self.toolbar)
            self.layout.addWidget(self.toolbar)  # Toolbar should be added first!

            self.title_label = QLabel(title, self)
            self.layout.addWidget(self.title_label)

            self.form_layout = QFormLayout()
            self.inputs = {}

            for field in fields:
                label = form_labels.get(field["label_key"], field["default_label"])
                if field["type"] == "text":
                    input_widget = QLineEdit(self)
                elif field["type"] == "spin":
                    input_widget = QSpinBox(self)
                    if "max" in field:
                        input_widget.setMaximum(field["max"])
                elif field["type"] == "date":
                    input_widget = QDateEdit(self)
                else:
                    input_widget = QLineEdit(self)
                self.inputs[field["name"]] = input_widget
                self.form_layout.addRow(label, input_widget)

            self.layout.addLayout(self.form_layout)

            self.setLayout(self.layout)
            log_info("BaseFormWidget initialized successfully.")
        except Exception as e:
            log_exception("Error initializing BaseFormWidget", e)