# Generates the style string for form widgets based on the selected style and mode.

from config.settings import load_settings
from gui.styles.oldschool_style import get_style as get_oldschool_style
from gui.styles.vintage_style import get_style as get_vintage_style
from gui.styles.modern_style import get_style as get_modern_style
from gui.styles.future_style import get_style as get_future_style

STYLE_FUNCTIONS = {
    "oldschool": get_oldschool_style,
    "vintage": get_vintage_style,
    "modern": get_modern_style,
    "future": get_future_style
}

def get_current_style():
    """
    Returns the style dictionary for the currently selected style and mode.
    Defaults to modern style and light mode if not set.
    """
    settings = load_settings()
    style_code = settings.get("style", "modern")
    mode_code = settings.get("mode", "light")
    style_func = STYLE_FUNCTIONS.get(style_code, get_modern_style)
    return style_func(mode_code)

def load_form_style(input_font_size=14, label_font_size=14, input_width=400):
    """
    Returns the style string for form widgets with dynamic font size and width,
    using the currently selected style and mode.
    """
    style = get_current_style()
    return f"""
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