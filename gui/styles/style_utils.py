# Utility functions for generating button styles based on the selected style and mode.

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

def load_button_style(font_size=16):
    """
    Returns the style string for default buttons with dynamic font size,
    using the currently selected style and mode.
    """
    style = get_current_style()
    return f"""
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
    """

def load_active_button_style(font_size=16):
    """
    Returns the style string for active navigation buttons,
    using the currently selected style and mode.
    """
    style = get_current_style()
    return f"""
        QPushButton {{
            background-color: {style['highlight']};
            color: {style['button']['foreground']};
            font-size: {font_size}px;
            border: 2px solid {style['border']};
            border-radius: 8px;
            font-weight: bold;
        }}
    """