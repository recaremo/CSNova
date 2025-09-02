from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFormLayout,
    QLineEdit, QSpinBox, QDateEdit, QComboBox
)
from gui.widgets.form_toolbar import FormToolbar
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class BaseFormWidget(QWidget):
    def __init__(self, title, fields, toolbar_actions, form_prefix, translator, parent=None):
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Hauptlayout
            main_layout = QVBoxLayout()

            # Toolbar linksbündig über die gesamte Breite
            self.toolbar = FormToolbar(self.translator, form_prefix, self)
            if toolbar_actions:
                toolbar_actions(self.toolbar)
            main_layout.addWidget(self.toolbar)
            main_layout.addSpacing(12)

            # Formularfelder
            self.form_layout = QFormLayout()
            self.inputs = {}

            for field in fields:
                if field.get("type") == "header":
                    # Überschrift erzeugen (großes, fettes Label)
                    header_text = self.translator.tr(field["label_key"])
                    header_label = QLabel(header_text if header_text else field.get("default_label", ""), self)
                    header_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 12px;")
                    self.form_layout.addRow(header_label)
                    continue  # Keine Eingabe für Header-Felder

                label_text = self.translator.tr(field["label_key"])
                label = QLabel(label_text if label_text else field.get("default_label", ""), self)
                input_widget = None

                if field["type"] == "text":
                    input_widget = QLineEdit(self)
                    if "max_length" in field:
                        input_widget.setMaxLength(field["max_length"])
                elif field["type"] == "spin":
                    input_widget = QSpinBox(self)
                    if "max" in field:
                        input_widget.setMaximum(field["max"])
                    if "min" in field:
                        input_widget.setMinimum(field["min"])
                elif field["type"] == "date":
                    input_widget = QDateEdit(self)
                elif field["type"] == "select":
                    input_widget = QComboBox(self)
                    for option in field.get("options", []):
                        input_widget.addItem(str(option))
                else:
                    input_widget = QLineEdit(self)

                self.inputs[field["name"]] = input_widget
                self.form_layout.addRow(label, input_widget)

            main_layout.addLayout(self.form_layout)
            main_layout.addStretch()

            self.setLayout(main_layout)
            log_info("BaseFormWidget initialized successfully.")
        except Exception as e:
            log_exception("Error initializing BaseFormWidget", e)