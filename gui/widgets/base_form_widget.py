import json
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QSpinBox, QDateEdit, QComboBox, QCheckBox, QTextEdit
)
from PySide6.QtCore import Qt
from gui.widgets.form_toolbar import FormToolbar
from gui.styles.python_gui_styles import apply_theme_style
from core.logger import log_section, log_subsection, log_info, log_exception, log_debug

class BaseFormWidget(QWidget):
    """
    Generic form widget: loads all fields and labels from form_fields.json,
    translates all labels and options dynamically via translator.py,
    updates labels and options after language change.
    All styles are applied centrally via python_gui_styles.py.
    Field-specific settings (e.g. width, max_length, multiline) are applied if present.
    """

    def __init__(self, title, fields, toolbar_actions, form_prefix, translator, parent=None, style=None):
        """
        Initializes the form widget with dynamic fields, translations, and toolbar.
        Applies field-specific settings such as width, max_length, multiline if defined in fields.
        Robust logging for all steps and errors.
        """
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.style = style
            apply_theme_style(self, "panel", self.style)

            main_layout = QVBoxLayout(self)
            main_layout.setSpacing(12)

            # Toolbar always shown
            try:
                self.toolbar = FormToolbar(self.translator, form_prefix, self, style=self.style)
                main_layout.addWidget(self.toolbar)
                if toolbar_actions:
                    toolbar_actions(self.toolbar)
                log_debug("Toolbar initialized and added.")
            except Exception as tb_err:
                log_exception("Error initializing or adding toolbar", tb_err)

            self.form_layout = QFormLayout()
            self.inputs = {}
            self.labels = {}
            self.option_keys = {}

            # Store fields for translation updates
            self._fields = fields

            for field in fields:
                try:
                    if "name" not in field or "type" not in field:
                        log_exception(f"Field missing 'name' or 'type': {field}")
                        continue
                    log_debug(f"Processing field: {field}")

                    if field.get("type") == "header":
                        header_text = self.translator.tr(field.get("label_key", ""))
                        header_label = QLabel(header_text if header_text else field.get("default_label", ""), self)
                        header_label.setObjectName("FormHeaderLabel")
                        header_label.setProperty("header", True)
                        apply_theme_style(header_label, "chip", self.style)
                        self.form_layout.addRow(header_label)
                        log_debug(f"Added header label for field '{field.get('name', '')}'.")
                        continue

                    label_text = self.translator.tr(field.get("label_key", ""))
                    label = QLabel(label_text if label_text else field.get("default_label", ""), self)
                    label.setProperty("label_key", field.get("label_key", ""))
                    self.labels[field["name"]] = label
                    input_widget = None

                    # --- Widget creation with field-specific settings ---
                    if field["type"] == "text":
                        input_widget = QLineEdit(self)
                        if "max_length" in field:
                            input_widget.setMaxLength(field["max_length"])
                        if "width" in field:
                            input_widget.setFixedWidth(field["width"])
                        apply_theme_style(input_widget, "input", self.style)
                    elif field["type"] == "spin":
                        input_widget = QSpinBox(self)
                        if "max" in field:
                            input_widget.setMaximum(field["max"])
                        if "min" in field:
                            input_widget.setMinimum(field["min"])
                        if "width" in field:
                            input_widget.setFixedWidth(field["width"])
                        apply_theme_style(input_widget, "input", self.style)
                    elif field["type"] == "date":
                        input_widget = QDateEdit(self)
                        if "width" in field:
                            input_widget.setFixedWidth(field["width"])
                        apply_theme_style(input_widget, "input", self.style)
                    elif field["type"] == "select":
                        input_widget = QComboBox(self)
                        self.option_keys[field["name"]] = []
                        for option in field.get("options", []):
                            option_label = self.translator.tr(option.get("label_key", str(option)))
                            input_widget.addItem(option_label)
                            self.option_keys[field["name"]].append(option.get("label_key", option_label))
                        if "width" in field:
                            input_widget.setFixedWidth(field["width"])
                        apply_theme_style(input_widget, "input", self.style)
                    elif field["type"] == "display":
                        input_widget = QLabel("", self)
                        if "width" in field:
                            input_widget.setFixedWidth(field["width"])
                        apply_theme_style(input_widget, "input", self.style)
                    elif field["type"] == "checkbox":
                        input_widget = QCheckBox(self)
                        if "width" in field:
                            input_widget.setFixedWidth(field["width"])
                        apply_theme_style(input_widget, "input", self.style)
                    elif field["type"] == "multiline":
                        input_widget = QTextEdit(self)
                        if "max_length" in field:
                            # Limit height visually, but not text length (Qt limitation)
                            input_widget.setMaximumHeight(120)
                        if "width" in field:
                            input_widget.setFixedWidth(field["width"])
                        apply_theme_style(input_widget, "input", self.style)
                    else:
                        log_exception(f"Unknown field type '{field['type']}' for field '{field['name']}'. Using QLineEdit as fallback.")
                        input_widget = QLineEdit(self)
                        if "width" in field:
                            input_widget.setFixedWidth(field["width"])
                        apply_theme_style(input_widget, "input", self.style)

                    self.inputs[field["name"]] = input_widget
                    self.form_layout.addRow(label, input_widget)
                    log_debug(f"Added widget for field '{field['name']}' of type '{field['type']}'.")
                except Exception as field_error:
                    import traceback
                    log_exception(f"Error processing field: {field}", traceback.format_exc())

            try:
                main_layout.addLayout(self.form_layout)
                main_layout.addStretch()
                self.setLayout(main_layout)
                log_info("BaseFormWidget initialized successfully.")
            except Exception as layout_error:
                import traceback
                log_exception("Error adding form layout or setting main layout", traceback.format_exc())
        except Exception as e:
            import traceback
            log_exception("Error initializing BaseFormWidget", traceback.format_exc())

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        Robust logging for translation errors.
        """
        log_subsection("update_translations")
        try:
            for field in self._fields:
                try:
                    field_name = field["name"]
                    if field.get("type") == "header":
                        # Update header label
                        for i in range(self.form_layout.count()):
                            item = self.form_layout.itemAt(i)
                            widget = item.widget()
                            if isinstance(widget, QLabel) and widget.property("header"):
                                widget.setText(self.translator.tr(field.get("label_key", "")))
                    else:
                        label = self.labels.get(field_name)
                        if label:
                            label.setText(self.translator.tr(field.get("label_key", "")))
                        input_widget = self.inputs.get(field_name)
                        if isinstance(input_widget, QComboBox) and field_name in self.option_keys:
                            input_widget.blockSignals(True)
                            input_widget.clear()
                            for option_label_key in self.option_keys[field_name]:
                                input_widget.addItem(self.translator.tr(option_label_key))
                            input_widget.blockSignals(False)
                except Exception as trans_error:
                    import traceback
                    log_exception(f"Error updating translation for field: {field}", traceback.format_exc())
            log_info("BaseFormWidget translations updated.")
        except Exception as e:
            import traceback
            log_exception("Error updating translations in BaseFormWidget", traceback.format_exc())