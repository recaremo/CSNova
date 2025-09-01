from config.settings import load_settings
from gui.styles.base_style import render_css, DEFAULTS
from gui.styles.registry_style import get_current_style
from core.logger import log_section, log_subsection, log_info, log_exception

def load_global_stylesheet(font_size=14):
    """
    Loads the global stylesheet for the application using the current style and mode.
    """
    log_section("form_styles.py")
    log_subsection("load_global_stylesheet")
    try:
        style = get_current_style()
        style["font_size"] = font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        style["input_width"] = DEFAULTS["input_width"]

        # Combine all relevant templates
        button_css = render_css("button", style)
        input_css = render_css("input", style)
        tab_css = render_css("tab", style)
        listview_css = render_css("listview", style)
        label_css = render_css("label", style)
        tooltip_css = render_css("tooltip", style)
        splitter_css = render_css("splitter", style)
        panel_css = render_css("panel", style)
        toolbar_css = render_css("toolbar", style)
        form_css = render_css("form", style)

        # Concatenate all CSS parts
        stylesheet = (
            button_css +
            input_css +
            tab_css +
            listview_css +
            label_css +
            tooltip_css +
            splitter_css +
            panel_css +
            toolbar_css +
            form_css
        )
        log_info("Global stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading global stylesheet", e)
        return ""

def load_button_style(font_size=14):
    """
    Loads the stylesheet for buttons and toolbars.
    """
    log_section("form_styles.py")
    log_subsection("load_button_style")
    try:
        style = get_current_style()
        style["font_size"] = font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        return render_css("button", style) + render_css("toolbar", style)
    except Exception as e:
        log_exception("Error loading button stylesheet", e)
        return ""

def load_active_button_style(font_size=16):
    """
    Loads the stylesheet for active buttons.
    """
    log_section("form_styles.py")
    log_subsection("load_active_button_style")
    try:
        style = get_current_style()
        style["font_size"] = font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        return render_css("active_button", style)
    except Exception as e:
        log_exception("Error loading active button stylesheet", e)
        return ""

def load_form_style(input_font_size=14, label_font_size=14, input_width=400):
    """
    Loads the stylesheet for forms and input fields.
    """
    log_section("form_styles.py")
    log_subsection("load_form_style")
    try:
        style = get_current_style()
        style["font_size"] = input_font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        style["input_width"] = input_width
        return render_css("form", style)
    except Exception as e:
        log_exception("Error loading form stylesheet", e)
        return ""