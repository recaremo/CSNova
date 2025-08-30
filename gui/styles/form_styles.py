from core.lloger import log_section, log_subsection, log_info, log_error

def load_form_style(input_font_size=14, label_font_size=14, input_width=400):
    log_section("form_styles.py")
    log_subsection("load_form_style")
    try:
        style = f"""
            QLineEdit, QDateEdit, QSpinBox {{
                padding: 6px;
                border: 1px solid #aaa;
                border-radius: 4px;
                background-color: #ffffff;
                font-size: {input_font_size}px;
                font-family: 'Segoe UI', sans-serif;
                min-width: {input_width}px;
                max-width: {input_width}px;
            }}

            QLabel {{
                font-size: {label_font_size}px;
                color: #333;
            }}

            QFormLayout {{
                margin: 12px;
            }}
        """
        log_info("Form style generated successfully.")
        return style
    except Exception as e:
        log_error(f"Error generating form style: {str(e)}")
        # Fallback style
        return f"""
            QLineEdit, QDateEdit, QSpinBox {{
                padding: 6px;
                border: 1px solid #aaa;
                border-radius: 4px;
                background-color: #ffffff;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
                min-width: 400px;
                max-width: 400px;
            }}

            QLabel {{
                font-size: 14px;
                color: #333;
            }}

            QFormLayout {{
                margin: 12px;
            }}
        """