from config.settings import load_settings
from gui.styles.themes_style import get_theme

def get_current_style():
    """
    Loads the current style and mode from settings and returns the theme dictionary.
    Falls back to 'modern' and 'light' if not found.
    """
    settings = load_settings()
    style_code = settings.get("style", "modern")
    mode_code = settings.get("mode", "light")
    return get_theme(style_code, mode_code)