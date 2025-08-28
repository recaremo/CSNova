import os
from pathlib import Path

def load_button_style(font_size):
    """
    Load button style from external QSS file and inject dynamic font size.
    """
    style_path = Path(__file__).parent / "button_style.qss"
    if not os.path.exists(style_path):
        # Fallback style if file is missing
        return f"""
            QPushButton {{
                background-color: #d4c29c;
                color: #1a1a1a;
                font-size: 18px;
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
    # Replace placeholder for font size if present
    return style.replace("{font_size}", str(font_size))