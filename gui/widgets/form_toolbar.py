from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from gui.styles.form_styles import load_button_style
from core.logger import log_section, log_subsection, log_info, log_exception

class FormToolbar(QWidget):
    """
    Centralized toolbar widget for forms.
    Applies global button styles from preferences.
    All button labels are translated via translator.py.
    No local styles or translations are used.
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

    def __init__(self, translator, form_prefix, parent=None):
        """
        Initializes the toolbar with translated buttons for form actions.
        """
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_button_style())

            layout = QHBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(10)

            # Use correct button keys for the form type
            self.button_keys = self.BUTTON_KEY_MAP.get(form_prefix, [])
            self.buttons = {}

            for key in self.button_keys:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setObjectName(key)
                self.buttons[key] = btn
                layout.addWidget(btn)

            layout.addStretch()
            self.setLayout(layout)
            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormToolbar", e)

    def update_translations(self):
        """
        Updates all button texts after a language change.
        """
        for key, btn in self.buttons.items():
            btn.setText(self.translator.tr(key))