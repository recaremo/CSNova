# Central default parameters for stylesheets
DEFAULTS = {
    "border_radius": 8,
    "font_size": 14,
    "input_width": 400,
}

# Central CSS templates for all GUI components
CSS_TEMPLATES = {
    "button": """
        QPushButton, QToolButton {{
            background-color: {button_bg};
            color: {button_fg};
            font-size: {font_size}px;
            border: 2px solid {border};
            border-radius: {border_radius}px;
        }}
        QPushButton:hover, QToolButton:hover {{
            background-color: {button_hover};
        }}
        QPushButton:pressed, QToolButton:pressed {{
            background-color: {button_active};
        }}
        QPushButton:disabled, QToolButton:disabled {{
            background-color: {border};
            color: {input_fg};
        }}
    """,

    "active_button": """
        QPushButton {{
            background-color: {highlight};
            color: {button_fg};
            font-size: {font_size}px;
            border: 2px solid {border};
            border-radius: {border_radius}px;
            font-weight: bold;
        }}
    """,

    "input": """
        QLineEdit, QTextEdit, QPlainTextEdit, QComboBox, QSpinBox, QDateEdit {{
            background-color: {input_bg};
            color: {input_fg};
            border: 1px solid {border};
            border-radius: 4px;
            font-size: {font_size}px;
            padding: 6px;
            min-width: {input_width}px;
            max-width: {input_width}px;
        }}
    """,

    "tab": """
        QTabWidget::pane {{
            border: 1px solid {border};
        }}
        QTabBar::tab {{
            background: {button_bg};
            color: {button_fg};
            border-radius: {border_radius}px;
            min-width: 120px;
            padding: 8px;
        }}
        QTabBar::tab:selected {{
            background: {highlight};
            color: {button_fg};
        }}
    """,

    "listview": """
        QListView, QTreeView {{
            background-color: {input_bg};
            color: {input_fg};
            border: 1px solid {border};
            selection-background-color: {highlight};
            selection-color: {button_fg};
        }}
    """,

    "label": """
        QLabel, QGroupBox {{
            color: {foreground};
            font-size: {font_size}px;
        }}
    """,

    "tooltip": """
        QToolTip {{
            background-color: {highlight};
            color: {background};
            border: 1px solid {border};
        }}
    """,

    "splitter": """
        QSplitter::handle {{
            background: {border};
            border: 1px solid {highlight};
            width: 8px;
        }}
        QSplitter::handle:hover {{
            background: {highlight};
        }}
    """,

    "panel": """
        QWidget#NavigationPanel, QWidget#HelpPanel, QWidget#CenterPanel {{
            background-color: {background};
            border: 1px solid {border};
            border-radius: {border_radius}px;
        }}
    """,

    "toolbar": """
        QToolBar {{
            background: {background};
            border-bottom: 1px solid {border};
            min-height: 44px;
            padding-top: 6px;
            padding-bottom: 6px;
        }}
        QToolButton {{
            min-width: 36px;
            min-height: 36px;
            padding: 6px 12px;
            font-size: {font_size}px;
            qproperty-toolButtonStyle: ToolButtonTextBesideIcon;
        }}
        QToolButton:hover {{
            background-color: {button_hover};
        }}
        QToolButton:pressed {{
            background-color: {button_active};
        }}
    """,

    "form": """
        QLineEdit, QDateEdit, QSpinBox {{
            padding: 6px;
            border: 1px solid {border};
            border-radius: 4px;
            background-color: {input_bg};
            color: {input_fg};
            font-size: {font_size}px;
            font-family: 'Segoe UI', sans-serif;
            min-width: {input_width}px;
            max-width: {input_width}px;
        }}
        QLabel {{
            font-size: {font_size}px;
            color: {foreground};
        }}
        QFormLayout {{
            margin: 12px;
        }}
    """,
}

def render_css(template_name, style_dict, defaults=DEFAULTS):
    """
    Renders the requested CSS template with style parameters and defaults.
    """
    params = {**defaults, **style_dict}
    # Map template parameters for compatibility with all style dicts
    params.update({
        "button_bg": style_dict.get("button", {}).get("background", style_dict.get("button_bg", "#e7eaf3")),
        "button_fg": style_dict.get("button", {}).get("foreground", style_dict.get("button_fg", "#1a1a1a")),
        "button_hover": style_dict.get("button", {}).get("hover", style_dict.get("button_hover", "#d0d6e6")),
        "button_active": style_dict.get("button", {}).get("active", style_dict.get("button_active", "#b6c2e1")),
        "input_bg": style_dict.get("input", {}).get("background", style_dict.get("input_bg", "#ffffff")),
        "input_fg": style_dict.get("input", {}).get("foreground", style_dict.get("input_fg", "#1a1a1a")),
    })
    return CSS_TEMPLATES[template_name].format(**params)