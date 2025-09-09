from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QComboBox, QSpinBox, QPlainTextEdit, QTabWidget, QTabBar
from PySide6.QtCore import Qt

def apply_theme_style(widget, widget_type, theme, extra=None):
    """
    Applies dynamic style to a widget based on widget_type and theme dict.
    Optionally merges extra dict for overrides.
    """
    style = theme.copy()
    if extra:
        style.update(extra)
    # Button
    if widget_type == "button":
        button_style = style.get("button", {})
        widget.setStyleSheet(f"""
            QPushButton {{
                background-color: {button_style.get('background', style.get('background', '#e7eaf3'))};
                color: {button_style.get('foreground', style.get('foreground', '#23272f'))};
                border-radius: {style.get('border_radius', 8)}px;
                border: {button_style.get('border', 'none')};
                font-size: {style.get('font_size', 14)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
                padding: 8px 24px;
            }}
            QPushButton:hover {{
                background-color: {button_style.get('hover', style.get('highlight', '#2563eb'))};
            }}
            QPushButton:pressed {{
                background-color: {button_style.get('active', style.get('highlight', '#2563eb'))};
            }}
            QPushButton:disabled {{
                background-color: #cccccc;
                color: #888888;
            }}
        """)
    # Floating Action Button
    elif widget_type == "fab":
        button_style = style.get("button", {})
        widget.setStyleSheet(f"""
            QPushButton {{
                background-color: {button_style.get('background', style.get('background', '#e7eaf3'))};
                color: {button_style.get('foreground', style.get('foreground', '#23272f'))};
                border-radius: 50%;
                border: {button_style.get('border', 'none')};
                font-size: {style.get('font_size', 14)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
                width: 48px;
                height: 48px;
            }}
            QPushButton:hover {{
                background-color: {button_style.get('hover', style.get('highlight', '#2563eb'))};
            }}
            QPushButton:pressed {{
                background-color: {button_style.get('active', style.get('highlight', '#2563eb'))};
            }}
        """)
    # Label
    elif widget_type == "label":
        widget.setStyleSheet(f"""
            QLabel {{
                color: {style.get('foreground', '#23272f')};
                font-size: {style.get('font_size', 14)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
                background: transparent;
            }}
        """)
    # Chip Label
    elif widget_type == "chip":
        chip_style = style.get("chip", {})
        widget.setStyleSheet(f"""
            QLabel {{
                background: {chip_style.get('background', '#e7eaf3')};
                color: {chip_style.get('foreground', '#2563eb')};
                border-radius: {style.get('border_radius', 8)}px;
                padding: 4px 12px;
                font-size: {style.get('font_size', 13)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
            }}
        """)
    # Input
    elif widget_type == "input":
        input_style = style.get("input", {})
        widget.setStyleSheet(f"""
            QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox {{
                background-color: {input_style.get('background', style.get('background', '#ffffff'))};
                color: {input_style.get('foreground', style.get('foreground', '#23272f'))};
                border-radius: {style.get('border_radius', 8)}px;
                border: 1px solid {style.get('border', '#cfd8dc')};
                font-size: {style.get('font_size', 14)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
                padding: 6px 12px;
                min-width: {style.get('input_width', 320)}px;
            }}
        """)
    # ComboBox
    elif widget_type == "combobox":
        input_style = style.get("input", {})
        widget.setStyleSheet(f"""
            QComboBox {{
                background-color: {input_style.get('background', style.get('background', '#ffffff'))};
                color: {input_style.get('foreground', style.get('foreground', '#23272f'))};
                border-radius: {style.get('border_radius', 8)}px;
                border: 1px solid {style.get('border', '#cfd8dc')};
                font-size: {style.get('font_size', 14)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
                padding: 6px 12px;
                min-width: {style.get('input_width', 320)}px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {input_style.get('background', style.get('background', '#ffffff'))};
                color: {input_style.get('foreground', style.get('foreground', '#23272f'))};
                selection-background-color: {style.get('highlight', '#2563eb')};
            }}
        """)
    # TabWidget/TabBar
    elif widget_type == "tab":
        widget.setStyleSheet(f"""
            QTabWidget::pane {{
                border: 1px solid {style.get('border', '#cfd8dc')};
                border-radius: {style.get('border_radius', 8)}px;
            }}
            QTabBar::tab {{
                background: {style.get('background', '#e7eaf3')};
                color: {style.get('foreground', '#23272f')};
                border: 1px solid {style.get('border', '#cfd8dc')};
                border-radius: {style.get('border_radius', 8)}px;
                padding: 8px 24px;
                font-size: {style.get('font_size', 14)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
            }}
            QTabBar::tab:selected {{
                background: {style.get('highlight', '#2563eb')};
                color: {style.get('foreground', '#e7eaf3')};
            }}
            QTabBar::tab:hover {{
                background: {style.get('highlight', '#60a5fa')};
            }}
        """)
    # Panel (z.B. QWidget als Panel)
    elif widget_type == "panel":
        widget.setStyleSheet(f"""
            QWidget {{
                background-color: {style.get('background', '#e7eaf3')};
                color: {style.get('foreground', '#23272f')};
                border-radius: {style.get('border_radius', 8)}px;
                font-size: {style.get('font_size', 14)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
            }}
        """)
    # CenterPanel (optional, falls spezielle Styles)
    elif widget_type == "center_panel":
        widget.setStyleSheet(f"""
            QWidget {{
                background-color: {style.get('background', '#e7eaf3')};
                color: {style.get('foreground', '#23272f')};
                border-radius: {style.get('border_radius', 8)}px;
                font-size: {style.get('font_size', 16)}px;
                font-family: {style.get('font_family', 'Arial, sans-serif')};
            }}
        """)
    # Add more widget types as needed...

def update_dynamic_styles(widgets, theme, window_size):
    """
    Dynamically update styles for a list of widgets based on theme and window size.
    """
    scale = max(window_size.width() / 1400, 1)
    dynamic_theme = theme.copy()
    dynamic_theme["font_size"] = int(theme.get("font_size", 14) * scale)
    dynamic_theme["input_width"] = int(theme.get("input_width", 320) * scale)
    dynamic_theme["border_radius"] = int(theme.get("border_radius", 8) * scale)
    # Update all widgets
    for widget, widget_type in widgets:
        apply_theme_style(widget, widget_type, dynamic_theme)