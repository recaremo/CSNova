from gui.styles.base_style import render_css, CSS_TEMPLATES
from gui.styles.registry_style import get_current_style
from core.logger import log_section, log_subsection, log_info, log_exception

def load_global_stylesheet(style_code=None, mode_code=None):
    """
    Loads the global stylesheet for the application using the given style and mode.
    If style_code or mode_code are not provided, uses current settings.
    """
    log_section("form_styles.py")
    log_subsection("load_global_stylesheet")
    try:
        style = get_current_style(style_code, mode_code)
        # Render all CSS templates at once
        stylesheet = ""
        for key in CSS_TEMPLATES:
            stylesheet += CSS_TEMPLATES[key].format(**style)
        log_info("Global stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading global stylesheet", e)
        return ""

def load_button_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for buttons and toolbars.
    """
    log_section("form_styles.py")
    log_subsection("load_button_style")
    try:
        style = get_current_style(style_code, mode_code)
        css = CSS_TEMPLATES["button"].format(**style)
        css += CSS_TEMPLATES["toolbar"].format(**style)
        return css
    except Exception as e:
        log_exception("Error loading button stylesheet", e)
        return ""

def load_active_button_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for active buttons.
    """
    log_section("form_styles.py")
    log_subsection("load_active_button_style")
    try:
        style = get_current_style(style_code, mode_code)
        if "active_button" in CSS_TEMPLATES:
            return CSS_TEMPLATES["active_button"].format(**style)
        else:
            return CSS_TEMPLATES["button"].format(**style)
    except Exception as e:
        log_exception("Error loading active button stylesheet", e)
        return ""

def load_form_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for forms and input fields.
    """
    log_section("form_styles.py")
    log_subsection("load_form_style")
    try:
        style = get_current_style(style_code, mode_code)
        return CSS_TEMPLATES["form"].format(**style)
    except Exception as e:
        log_exception("Error loading form stylesheet", e)
        return ""