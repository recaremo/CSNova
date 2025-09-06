from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from gui.styles.python_gui_styles import apply_theme_style
from core.logger import log_section, log_subsection, log_info, log_exception

class FormToolbar(QWidget):
    """
    Centralized toolbar widget for forms.
    Applies global button styles from preferences and themes.
    All button labels are translated via translator.py.
    Button type and visibility are dynamically set based on the current style.
    """

    BUTTON_KEY_MAP = {
        "projects": [
            "botn_pr_01", "botn_pr_05", "botn_pr_02", "botn_pr_03", "botn_pr_04"
        ],
        "locations": [
            "botn_lo_01", "botn_lo_05", "botn_lo_02", "botn_lo_03", "botn_lo_04"
        ],
        "objects": [
            "botn_ob_01", "botn_ob_05", "botn_ob_02", "botn_ob_03", "botn_ob_04"
        ],
        "characters": [
            "botn_ch_01", "botn_ch_05", "botn_ch_02", "botn_ch_03", "botn_ch_04"
        ],
        "chapters": [
            "botn_ch_01", "botn_ch_05", "botn_ch_02", "botn_ch_03", "botn_ch_04"
        ],
        "scenes": [
            "botn_sc_01", "botn_sc_05", "botn_sc_02", "botn_sc_03", "botn_sc_04"
        ],
        "storylines": [
            "botn_sl_01", "botn_sl_05", "botn_sl_02", "botn_sl_03", "botn_sl_04"
        ],
        "groups": [
            "botn_cp_01", "botn_cp_05", "botn_cp_02", "botn_cp_03", "botn_cp_04"
        ]
    }

    def __init__(self, translator, form_prefix, parent=None, style=None):
        """
        Initializes the toolbar with translated buttons for form actions.
        Button type and visibility are set based on the current style.
        style: Combined style dict from csNova_base_style.json and csNova_themes_style.json.
        """
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.style = style if style is not None else {}

            button_style = self.style.get("button", {})
            button_visible = button_style.get("visible", True)
            button_shape = button_style.get("shape", "rectangle")

            layout = QHBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(10)

            self.button_keys = self.BUTTON_KEY_MAP.get(form_prefix, [])
            self.buttons = {}

            for idx, key in enumerate(self.button_keys):
                label_text = self.translator.tr(key)
                # FAB style
                if button_shape == "fab" and idx == 0 and button_visible:
                    btn = QPushButton(label_text, self)
                    btn.setObjectName("FloatingActionButton")
                    apply_theme_style(btn, "icon_button", self.style)
                    self.buttons[key] = btn
                    layout.addWidget(btn)
                # Rectangle style
                elif button_visible and button_shape == "rectangle":
                    btn = QPushButton(label_text, self)
                    btn.setObjectName(key)
                    apply_theme_style(btn, "button", self.style)
                    self.buttons[key] = btn
                    layout.addWidget(btn)
                # Circle style
                elif button_visible and button_shape == "circle":
                    btn = QPushButton(label_text, self)
                    btn.setObjectName(key)
                    apply_theme_style(btn, "icon_button", self.style)
                    self.buttons[key] = btn
                    layout.addWidget(btn)
                # Minimal style: show as link
                elif not button_visible:
                    link = QLabel(label_text, self)
                    link.setObjectName(f"link_{key}")
                    link.setProperty("link", True)
                    apply_theme_style(link, "link", self.style)
                    self.buttons[key] = link
                    layout.addWidget(link)
                # Add more shapes/types if needed

            layout.addStretch()
            self.setLayout(layout)
            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormToolbar", e)

    def update_translations(self):
        """
        Updates all button texts after a language change.
        """
        for key, widget in self.buttons.items():
            if hasattr(widget, "setText"):
                widget.setText(self.translator.tr(key))