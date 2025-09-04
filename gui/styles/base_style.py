# Central CSS templates for all GUI components

CSS_TEMPLATES = {
    "window": """
        QWidget, QDialog {{
            background-color: {background};
            color: {foreground};
            font-family: {font_family};
            font-size: {font_size}px;
        }}
    """,
    "label": """
        QLabel {{
            color: {foreground};
            font-size: {font_size}px;
            background: transparent;
        }}
    """,
    "groupbox": """
        QGroupBox {{
            border: 1px solid {border};
            border-radius: {border_radius}px;
            margin-top: 10px;
            color: {foreground};
            font-size: {font_size}px;
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px 0 3px;
        }}
    """,
    "button": """
        QPushButton {{
            background-color: {button_bg};
            color: {button_fg};
            border-radius: {border_radius}px;
            border: 1px solid {border};
            font-size: {font_size}px;
            padding: 6px 18px;
        }}
        QPushButton:hover {{
            background-color: {button_hover};
        }}
        QPushButton:pressed {{
            background-color: {button_active};
        }}
        QPushButton:disabled {{
            background-color: #cccccc;
            color: #888888;
        }}
    """,
    "input": """
        QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QComboBox {{
            background-color: {input_bg};
            color: {input_fg};
            border-radius: {border_radius}px;
            border: 1px solid {border};
            font-size: {font_size}px;
            padding: 4px 8px;
            min-width: {input_width}px;
        }}
        QComboBox QAbstractItemView {{
            background-color: {input_bg};
            color: {input_fg};
            selection-background-color: {highlight};
        }}
    """,
    "tab": """
        QTabWidget::pane {{
            border: 1px solid {border};
            border-radius: {border_radius}px;
        }}
        QTabBar::tab {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            border-radius: {border_radius}px;
            padding: 6px 18px;
            font-size: {font_size}px;
        }}
        QTabBar::tab:selected {{
            background: {button_active};
            color: {highlight};
        }}
        QTabBar::tab:hover {{
            background: {button_hover};
        }}
    """,
    "list": """
        QListView, QTreeView {{
            background: {input_bg};
            color: {input_fg};
            border: 1px solid {border};
            border-radius: {border_radius}px;
            font-size: {font_size}px;
        }}
        QListView::item:selected, QTreeView::item:selected {{
            background: {highlight};
            color: {foreground};
        }}
    """,
    "table": """
        QTableView {{
            background: {input_bg};
            color: {input_fg};
            border: 1px solid {border};
            border-radius: {border_radius}px;
            font-size: {font_size}px;
            gridline-color: {border};
        }}
        QHeaderView::section {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
    """,
    "progress": """
        QProgressBar {{
            border: 1px solid {border};
            border-radius: {border_radius}px;
            text-align: center;
            background: {input_bg};
            color: {input_fg};
            font-size: {font_size}px;
        }}
        QProgressBar::chunk {{
            background-color: {highlight};
            width: 20px;
        }}
    """,
    "slider": """
        QSlider::groove:horizontal {{
            border: 1px solid {border};
            height: 8px;
            background: {input_bg};
            border-radius: 4px;
        }}
        QSlider::handle:horizontal {{
            background: {highlight};
            border: 1px solid {border};
            width: 18px;
            margin: -5px 0;
            border-radius: 9px;
        }}
    """,
    "splitter": """
        QSplitter::handle {{
            background: {border};
        }}
    """,
    "panel": """
        QWidget#NavigationPanel, QWidget#HelpPanel, QWidget#CenterPanel {{
            background: {background};
            color: {foreground};
            border-radius: {border_radius}px;
        }}
    """,
    "toolbar": """
        QToolBar {{
            background: {button_bg};
            border-bottom: 1px solid {border};
            spacing: 6px;
        }}
    """,
    "form": """
        QFormLayout QLabel {{
            color: {foreground};
            font-size: {font_size}px;
        }}
        QFormLayout QLineEdit, QFormLayout QDateEdit, QFormLayout QSpinBox {{
            background: {input_bg};
            color: {input_fg};
            border-radius: {border_radius}px;
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
    """,
    "tooltip": """
        QToolTip {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
    """,
    "menu": """
        QMenu {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
        QMenu::item:selected {{
            background: {highlight};
            color: {foreground};
        }}
    """,
    "contextmenu": """
        QMenu {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
        QMenu::item:selected {{
            background: {highlight};
            color: {foreground};
        }}
    """,
    "form_header": """
    QLabel#FormHeaderLabel {{
        font-size: 22px;
        font-weight: bold;
        color: {foreground};
        margin-bottom: 12px;
    }}
    """,
    "error": """
        QLabel#error, QLineEdit[error="true"], QTextEdit[error="true"] {{
            color: {error};
            border: 1px solid {error};
            background: #fff0f0;
        }}
    """
}

def extract_params(theme):
    """
    Converts the nested theme dict from themes_style.py into flat parameters for CSS rendering.
    Assumes all relevant values are set in the theme.
    """
    params = {}
    params.update({k: v for k, v in theme.items() if not isinstance(v, dict)})
    # Button
    button = theme.get("button", {})
    params["button_bg"] = button.get("background")
    params["button_fg"] = button.get("foreground")
    params["button_hover"] = button.get("hover")
    params["button_active"] = button.get("active")
    # Input
    input_ = theme.get("input", {})
    params["input_bg"] = input_.get("background")
    params["input_fg"] = input_.get("foreground")
    return params

def render_css(theme):
    """
    Renders the full CSS stylesheet for all GUI components using the given theme dict.
    """
    params = extract_params(theme)
    css = ""
    for key, template in CSS_TEMPLATES.items():
        css += template.format(**params)
    return css