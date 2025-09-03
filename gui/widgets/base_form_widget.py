import json
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFormLayout,
    QLineEdit, QSpinBox, QDateEdit, QComboBox
)
from gui.widgets.form_toolbar import FormToolbar
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE

class BaseFormWidget(QWidget):
    """
    Generic form widget: loads all fields and labels from form_fields.json,
    translates all labels and options dynamically via translator.py,
    updates labels and options after language change.
    All styles are applied centrally via form_styles.py.
    """

    def __init__(self, title, fields, toolbar_actions, form_prefix, translator, parent=None):
        """
        Initializes the form widget with dynamic fields, translations, and toolbar.
        """
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            main_layout = QVBoxLayout()

            # Toolbar
            self.toolbar = FormToolbar(self.translator, form_prefix, self)
            if toolbar_actions:
                toolbar_actions(self.toolbar)
                main_layout.addWidget(self.toolbar)
                main_layout.addSpacing(12)

            # Form fields
            self.form_layout = QFormLayout()
            self.inputs = {}
            self.labels = {}
            self.option_keys = {}

            for field in fields:
                if field.get("type") == "header":
                    header_text = self.translator.tr(field["label_key"])
                    header_label = QLabel(header_text if header_text else field.get("default_label", ""), self)
                    # Use centralized style for header if available, else fallback
                    header_label.setProperty("header", True)
                    self.form_layout.addRow(header_label)
                    continue

                label_text = self.translator.tr(field["label_key"])
                label = QLabel(label_text if label_text else field.get("default_label", ""), self)
                self.labels[field["name"]] = label
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
                    self.option_keys[field["name"]] = []
                    for option in field.get("options", []):
                        # Use translated label for each option
                        option_label = self.translator.tr(option.get("label_key", str(option)))
                        input_widget.addItem(option_label)
                        self.option_keys[field["name"]].append(option.get("key", option_label))
                elif field["type"] == "display":
                    input_widget = QLabel("", self)
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

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        for field_name, label in self.labels.items():
            # Find the field definition for this label
            field = next((f for f in self.inputs if f == field_name), None)
            if field:
                label_key = None
                # Try to get label_key from form_fields.json if available
                # This assumes you pass the fields array to the widget and can access it here
                # If not, you may need to store label_keys in self.labels
                label_key = getattr(label, "label_key", None)
                if not label_key:
                    # Fallback: try to get from label text
                    label_key = field_name
                label.setText(self.translator.tr(label_key))

            # Update options for QComboBox
            input_widget = self.inputs.get(field_name)
            if isinstance(input_widget, QComboBox) and field_name in self.option_keys:
                input_widget.blockSignals(True)
                input_widget.clear()
                for idx, option_key in enumerate(self.option_keys[field_name]):
                    # Try to get the label_key from form_fields.json options
                    option_label = self.translator.tr(option_key)
                    input_widget.addItem(option_label)
                input_widget.blockSignals(False)