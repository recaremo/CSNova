from config.settings import load_settings
from gui.styles.oldschool_style import get_style as get_oldschool_style
from gui.styles.vintage_style import get_style as get_vintage_style
from gui.styles.modern_style import get_style as get_modern_style
from gui.styles.future_style import get_style as get_future_style
from core.logger import log_section, log_subsection, log_info, log_exception

STYLE_FUNCTIONS = {
    "oldschool": get_oldschool_style,
    "vintage": get_vintage_style,
    "modern": get_modern_style,
    "future": get_future_style
}

def get_current_style():
    log_section("form_styles.py")
    log_subsection("get_current_style")
    try:
        settings = load_settings()
        style_code = settings.get("style", "modern")
        mode_code = settings.get("mode", "light")
        style_func = STYLE_FUNCTIONS.get(style_code, get_modern_style)
        style = style_func(mode_code)
        log_info(f"Loaded style: {style_code}, mode: {mode_code}")
        return style
    except Exception as e:
        log_exception("Error loading current style", e)
        # Fallback: modern light
        return get_modern_style("light")

def load_global_stylesheet(font_size=14):
    log_section("form_styles.py")
    log_subsection("load_global_stylesheet")
    try:
        style = get_current_style()
        stylesheet = f"""
            /* Buttons */
            QPushButton, QToolButton {{
                background-color: {style['button']['background']};
                color: {style['button']['foreground']};
                font-size: {font_size}px;
                border: 2px solid {style['border']};
                border-radius: 8px;
            }}

            QPushButton:hover, QToolButton:hover {{
                background-color: {style['button']['hover']};
            }}
            QPushButton:pressed, QToolButton:pressed {{
                background-color: {style['button']['active']};
            }}
            QPushButton:disabled, QToolButton:disabled {{
                background-color: {style['border']};
                color: {style['input']['foreground']};
            }}
            
            /* Tabs */
            QTabWidget::pane {{
                border: 1px solid {style['border']};
            }}
            QTabBar::tab {{
                background: {style['button']['background']};
                color: {style['button']['foreground']};
                border-radius: 8px;
                min-width: 120px;
                padding: 8px;
            }}
            QTabBar::tab:selected {{
                background: {style['highlight']};
                color: {style['button']['foreground']};
            }}

            /* ListViews & TreeViews */
            QListView, QTreeView {{
                background-color: {style['input']['background']};
                color: {style['input']['foreground']};
                border: 1px solid {style['border']};
                selection-background-color: {style['highlight']};
                selection-color: {style['button']['foreground']};
            }}

            /* Inputfields */
            QLineEdit, QTextEdit, QPlainTextEdit, QComboBox, QSpinBox, QDateEdit {{
                background-color: {style['input']['background']};
                color: {style['input']['foreground']};
                border: 1px solid {style['border']};
                border-radius: 4px;
                font-size: {font_size}px;
                padding: 6px;
            }}

            /* Labels & GroupBoxes */
            QLabel, QGroupBox {{
                color: {style['foreground']};
                font-size: {font_size}px;
            }}

            /* Tooltips */
            QToolTip {{
                background-color: {style['highlight']};
                color: {style['background']};
                border: 1px solid {style['border']};
            }}

            /* Splitter handle (for visible side lines) */
            QSplitter::handle {{
                background: {style['border']};
                border: 1px solid {style['highlight']};
                width: 8px;
            }}
            QSplitter::handle:hover {{
                background: {style['highlight']};
            }}

            /* Panels */
            QWidget#NavigationPanel, QWidget#HelpPanel, QWidget#CenterPanel {{
                background-color: {style['background']};
                border: 1px solid {style['border']};
                border-radius: 8px;
            }}
        """
        log_info("Global stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading global stylesheet", e)
        return ""

def load_button_style(font_size=14):
    log_section("form_styles.py")
    log_subsection("load_button_style")
    try:
        style = get_current_style()
        stylesheet = f"""
            QToolBar {{
                background: {style['background']};
                border-bottom: 1px solid {style['border']};
                min-height: 44px;
                padding-top: 6px;
                padding-bottom: 6px;
            }}

            QToolButton {{
                min-width: 36px;
                min-height: 36px;
                padding: 6px 12px;
                font-size: {font_size}px;
                qproperty-toolButtonStyle: ToolButtonTextBesideIcon;
            }}

            QToolButton:hover {{
                background-color: {style['button']['hover']};
            }}
            QToolButton:pressed {{
                background-color: {style['button']['active']};
            }}
            QPushButton {{
                background-color: {style['button']['background']};
                color: {style['button']['foreground']};
                font-size: {font_size}px;
                border: 2px solid {style['border']};
                border-radius: 8px;
            }}
            QPushButton:hover {{
                background-color: {style['button']['hover']};
            }}
            QPushButton:pressed {{
                background-color: {style['button']['active']};
            }}
            QPushButton:disabled {{
                background-color: {style['border']};
                color: {style['input']['foreground']};
            }}
        """
        log_info("Button stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading button stylesheet", e)
        return ""

def load_active_button_style(font_size=16):
    log_section("form_styles.py")
    log_subsection("load_active_button_style")
    try:
        style = get_current_style()
        stylesheet = f"""
            QPushButton {{
                background-color: {style['highlight']};
                color: {style['button']['foreground']};
                font-size: {font_size}px;
                border: 2px solid {style['border']};
                border-radius: 8px;
                font-weight: bold;
            }}
        """
        log_info("Active button stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading active button stylesheet", e)
        return ""

def load_form_style(input_font_size=14, label_font_size=14, input_width=400):
    log_section("form_styles.py")
    log_subsection("load_form_style")
    try:
        style = get_current_style()
        stylesheet = f"""
            QLineEdit, QDateEdit, QSpinBox {{
                padding: 6px;
                border: 1px solid {style['border']};
                border-radius: 4px;
                background-color: {style['input']['background']};
                color: {style['input']['foreground']};
                font-size: {input_font_size}px;
                font-family: 'Segoe UI', sans-serif;
                min-width: {input_width}px;
                max-width: {input_width}px;
            }}

            QLabel {{
                font-size: {label_font_size}px;
                color: {style['foreground']};
            }}

            QFormLayout {{
                margin: 12px;
            }}
        """
        log_info("Form stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading form stylesheet", e)
        return ""