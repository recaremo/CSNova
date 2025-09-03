from config.settings import load_settings
from gui.styles.themes_style import get_theme
from gui.styles.base_style import extract_params

def get_current_style(style_code=None, mode_code=None):
    """
    Loads the current style and mode from settings and returns a flat theme dictionary for CSS rendering.
    Falls back to 'modern' and 'light' if not found.
    """
    settings = load_settings()
    style = style_code if style_code else settings.get("style", "modern")
    mode = mode_code if mode_code else settings.get("mode", "light")
    theme = get_theme(style, mode)
    return extract_params(theme)