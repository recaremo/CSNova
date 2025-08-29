def load_form_style(input_font_size=14, label_font_size=14, input_width=400):
    return f"""
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
