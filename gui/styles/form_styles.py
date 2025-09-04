from gui.styles.base_style import CSS_TEMPLATES
from gui.styles.registry_style import get_current_style
from core.logger import log_section, log_subsection, log_info, log_exception
import traceback

def load_global_stylesheet(style_code=None, mode_code=None):
    """
    Loads the global stylesheet for the application using the given style and mode.
    If style_code or mode_code are not provided, uses current settings.
    """
    log_section("form_styles.py")
    log_subsection("load_global_stylesheet")
    try:
        style = get_current_style(style_code, mode_code)
        if not style:
            log_exception("No style returned from get_current_style", f"style_code={style_code}, mode_code={mode_code}")
        stylesheet = ""
        for key in CSS_TEMPLATES:
            try:
                stylesheet += CSS_TEMPLATES[key].format(**style)
            except Exception as e:
                log_exception(f"Error formatting CSS template '{key}'", f"{e}\n{traceback.format_exc()}")
        log_info("Global stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading global stylesheet", f"{e}\n{traceback.format_exc()}")
        return ""

def load_button_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for buttons and toolbars.
    """
    log_section("form_styles.py")
    log_subsection("load_button_style")
    try:
        style = get_current_style(style_code, mode_code)
        if not style:
            log_exception("No style returned from get_current_style", f"style_code={style_code}, mode_code={mode_code}")
        css = ""
        try:
            css += CSS_TEMPLATES["button"].format(**style)
        except Exception as e:
            log_exception("Error formatting 'button' CSS template", f"{e}\n{traceback.format_exc()}")
        try:
            css += CSS_TEMPLATES["toolbar"].format(**style)
        except Exception as e:
            log_exception("Error formatting 'toolbar' CSS template", f"{e}\n{traceback.format_exc()}")
        return css
    except Exception as e:
        log_exception("Error loading button stylesheet", f"{e}\n{traceback.format_exc()}")
        return ""

def load_active_button_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for active buttons.
    """
    log_section("form_styles.py")
    log_subsection("load_active_button_style")
    try:
        style = get_current_style(style_code, mode_code)
        if not style:
            log_exception("No style returned from get_current_style", f"style_code={style_code}, mode_code={mode_code}")
        if "active_button" in CSS_TEMPLATES:
            try:
                return CSS_TEMPLATES["active_button"].format(**style)
            except Exception as e:
                log_exception("Error formatting 'active_button' CSS template", f"{e}\n{traceback.format_exc()}")
                return ""
        else:
            try:
                return CSS_TEMPLATES["button"].format(**style)
            except Exception as e:
                log_exception("Error formatting 'button' CSS template", f"{e}\n{traceback.format_exc()}")
                return ""
    except Exception as e:
        log_exception("Error loading active button stylesheet", f"{e}\n{traceback.format_exc()}")
        return ""

def load_form_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for forms and input fields, including header formatting.
    """
    log_section("form_styles.py")
    log_subsection("load_form_style")
    try:
        style = get_current_style(style_code, mode_code)
        if not style:
            log_exception("No style returned from get_current_style", f"style_code={style_code}, mode_code={mode_code}")
        css = ""
        try:
            css += CSS_TEMPLATES["form"].format(**style)
        except Exception as e:
            log_exception("Error formatting 'form' CSS template", f"{e}\n{traceback.format_exc()}")
        if "form_header" in CSS_TEMPLATES:
            try:
                css += CSS_TEMPLATES["form_header"].format(**style)
            except Exception as e:
                log_exception("Error formatting 'form_header' CSS template", f"{e}\n{traceback.format_exc()}")
        return css
    except Exception as e:
        log_exception("Error loading form stylesheet", f"{e}\n{traceback.format_exc()}")
        return ""