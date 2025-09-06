from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from gui.widgets.form_toolbar import FormToolbar
from gui.widgets.form_center_start import FormCenterStart
from gui.widgets.form_projects import FormProjects
from gui.widgets.form_characters import FormCharacters
from gui.widgets.form_locations import FormLocations
from gui.widgets.form_objects import FormObjects
from gui.styles.python_gui_styles import apply_theme_style
from core.logger import log_section, log_subsection, log_info, log_exception

class CenterPanel(QWidget):
    """
    Central panel widget for main content area.
    Shows FormCenterStart on first launch, then dynamically displays the correct toolbar,
    heading, and form fields for each form type.
    All styles and formatting are loaded from the central style modules.
    """

    # Mapping for header translation keys
    HEADER_KEYS = {
        "projects": "proj_ma_01",
        "characters": "char_ma_01",
        "locations": "help_wi_05",
        "objects": "proj_ob_01"
    }

    def __init__(self, translator, parent=None, style=None):
        """
        Initializes the center panel with a stacked widget for dynamic content.
        Adds all available forms and shows the start/empty form initially.
        """
        log_section("center_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.style = style
            apply_theme_style(self, "panel", self.style)

            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(24, 24, 24, 24)
            self.layout.setSpacing(18)

            # Stacked widget for switching between forms
            self.stacked_widget = QStackedWidget(self)
            self.layout.addWidget(self.stacked_widget)
            self.setLayout(self.layout)

            # Dictionary to hold form widgets
            self.forms = {}

            # Add all available forms
            self.add_form("center_start", FormCenterStart(parent=self))
            self.add_form("projects", FormProjects(self.translator, parent=self))
            self.add_form("characters", FormCharacters(self.translator, parent=self))
            self.add_form("locations", FormLocations(self.translator, parent=self))
            self.add_form("objects", FormObjects(self.translator, parent=self))

            # Show the start/empty form initially
            self.stacked_widget.setCurrentWidget(self.forms["center_start"])

            log_info("CenterPanel initialized successfully and shows FormCenterStart.")
        except Exception as e:
            log_exception("Error initializing CenterPanel", e)

    def add_form(self, form_type, form_widget):
        """
        Adds a form widget to the stacked widget and keeps a reference for switching.
        """
        self.forms[form_type] = form_widget
        self.stacked_widget.addWidget(form_widget)

    def show_form(self, form_type):
        """
        Shows the selected form in the stacked widget.
        Dynamically adds toolbar and heading above the form fields.
        Uses correct translation keys for headings.
        """
        if form_type not in self.forms:
            log_info(f"Form type '{form_type}' not found in CenterPanel.")
            return

        # Remove previous toolbar and heading if present
        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget and widget != self.stacked_widget:
                self.layout.removeWidget(widget)
                widget.setParent(None)

        # Do not show toolbar or heading for the start/empty form
        if form_type != "center_start":
            # Dynamically create toolbar for the form
            toolbar = FormToolbar(self.translator, form_prefix=form_type, parent=self)
            self.layout.insertWidget(0, toolbar)
            apply_theme_style(toolbar, "panel", self.style)

            # Use correct translation key for heading
            header_key = self.HEADER_KEYS.get(form_type, "")
            heading_label = QLabel(self.translator.tr(header_key), self)
            heading_label.setObjectName("FormHeadingLabel")
            apply_theme_style(heading_label, "chip", self.style)
            self.layout.insertWidget(1, heading_label)

        # Show the form
        form_widget = self.forms[form_type]
        self.stacked_widget.setCurrentWidget(form_widget)

    def show_empty(self):
        """
        Shows the initial empty form (FormCenterStart).
        Removes any toolbar or heading.
        """
        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget and widget != self.stacked_widget:
                self.layout.removeWidget(widget)
                widget.setParent(None)
        self.stacked_widget.setCurrentWidget(self.forms["center_start"])

    def update_translations(self):
        """
        Updates all labels, headings, and toolbars after a language change.
        """
        for form in self.forms.values():
            if hasattr(form, "update_translations"):
                form.update_translations()
        # Update toolbar and heading for the current form
        current_index = self.stacked_widget.currentIndex()
        current_form_type = list(self.forms.keys())[current_index] if current_index >= 0 and current_index < len(self.forms) else None
        if current_form_type:
            self.show_form(current_form_type)