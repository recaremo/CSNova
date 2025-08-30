from core.logger import log_section, log_subsection, log_info, log_error

def load_button_style(font_size):
    """
    Returns the style string for default buttons with dynamic font size.
    """
    log_section("style_utils.py")
    log_subsection("load_button_style")
    try:
        style = f"""
            QPushButton {{
                background-color: #d4c29c;
                color: #1a1a1a;
                font-size: {font_size}px;
                border: 2px solid #8b7d5c;
                border-radius: 10px;
                border-style: outset;
            }}
            QPushButton:hover {{
                background-color: #e8d9b5;
                border-color: #5c5138;
            }}
            QPushButton:pressed {{
                background-color: #c0aa7a;
                border-style: inset;
            }}
        """
        log_info("Default button style generated.")
        return style
    except Exception as e:
        log_error(f"Error generating button style: {str(e)}")
        # Fallback style
        return f"""
            QPushButton {{
                background-color: #d4c29c;
                color: #1a1a1a;
                font-size: {font_size}px;
                border: 2px solid #8b7d5c;
                border-radius: 10px;
                border-style: outset;
            }}
            QPushButton:hover {{
                background-color: #e8d9b5;
                border-color: #5c5138;
            }}
            QPushButton:pressed {{
                background-color: #c0aa7a;
                border-style: inset;
            }}
        """

def load_active_button_style(font_size):
    """
    Returns the style string for active navigation buttons.
    """
    log_subsection("load_active_button_style")
    try:
        style = f"""
            QPushButton {{
                background-color: #6E8B3D;
                color: #1a1a1a;
                font-size: {font_size}px;
                border: 2px solid #5c5138;
                border-radius: 10px;
                border-style: outset;
                font-weight: bold;
            }}
        """
        log_info("Active button style generated.")
        return style
    except Exception as e:
        log_error(f"Error generating active button style: {str(e)}")
        # Fallback style
        return f"""
            QPushButton {{
                background-color: #6E8B3D;
                color: #1a1a1a;
                font-size: {font_size}px;
                border: 2px solid #5c5138;
                border-radius: 10px;
                border-style: outset;
                font-weight: bold;
            }}
        """