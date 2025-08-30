from pathlib import Path
import os

# Import zentrale Logging-Funktionen
from core.lloger import log_section, log_subsection, log_info, log_error

def load_button_style(font_size):
    """
    Load button style from external QSS file and inject dynamic font size.
    """
    log_section("style_utils.py")
    log_subsection("load_button_style")
    try:
        style_path = Path(__file__).parent / "button_style.qss"
        if not os.path.exists(style_path):
            log_error(f"button_style.qss not found at {style_path}, using fallback style.")
            # Fallback style if file is missing
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
        with open(style_path, "r") as f:
            style = f.read()
        log_info("button_style.qss loaded successfully.")
        return style.replace("{font_size}", str(font_size))
    except Exception as e:
        log_error(f"Error loading button style: {str(e)}")
        # Fallback style in case of error
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
    Return style for the active navigation button.
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