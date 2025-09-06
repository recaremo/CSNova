from PySide6.QtWidgets import (
    QGraphicsDropShadowEffect, QWidget, QPushButton, QLabel
)
from PySide6.QtGui import QColor, QIcon
from PySide6.QtCore import QPropertyAnimation, Qt
from core.logger import log_section, log_subsection, log_info, log_exception

def apply_drop_shadow(widget: QWidget, style: dict, blur_radius=10, x_offset=4, y_offset=4, color_str=None):
    log_section("python_gui_styles.py")
    log_subsection("apply_drop_shadow")
    try:
        color_str = color_str or style.get('button', {}).get('shadow_color') or style.get('shadow_color') or "#888888"
        color = QColor(color_str)
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(blur_radius)
        shadow.setXOffset(x_offset)
        shadow.setYOffset(y_offset)
        shadow.setColor(color)
        widget.setGraphicsEffect(shadow)
        log_info(f"Drop shadow applied: blur_radius={blur_radius}, x_offset={x_offset}, y_offset={y_offset}, color={color_str}")
    except Exception as e:
        log_exception("Error in apply_drop_shadow", str(e))

def animate_widget_opacity(widget: QWidget, style: dict, start=None, end=1.0, duration=None):
    log_section("python_gui_styles.py")
    log_subsection("animate_widget_opacity")
    try:
        start = start if start is not None else style.get('panel_opacity', 0.95)
        duration = duration if duration is not None else 400
        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(duration)
        animation.setStartValue(start)
        animation.setEndValue(end)
        animation.start()
        log_info(f"Widget opacity animated: start={start}, end={end}, duration={duration}")
        return animation
    except Exception as e:
        log_exception("Error in animate_widget_opacity", str(e))
        return None

def style_button(button: QPushButton, style: dict):
    log_section("python_gui_styles.py")
    log_subsection("style_button")
    try:
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {style.get('button_bg', style.get('button', {}).get('background', '#e7eaf3'))};
                color: {style.get('button_fg', style.get('button', {}).get('foreground', '#1a1a1a'))};
                border: {style.get('button', {}).get('border', 'none')};
                border-radius: {style.get('border_radius', 8)}px;
                font-size: {style.get('font_size', 14)}px;
                font-family: {style.get('font_family', 'Segoe UI, Arial, sans-serif')};
                padding: 6px 18px;
            }}
            QPushButton:hover {{
                background-color: {style.get('button_hover', style.get('button', {}).get('hover', '#d0d6e6'))};
            }}
            QPushButton:pressed {{
                background-color: {style.get('button_active', style.get('button', {}).get('active', '#b6c2e1'))};
            }}
        """)
        apply_drop_shadow(
            button,
            style=style,
            blur_radius=10,
            x_offset=2,
            y_offset=4,
            color_str=style.get('button', {}).get('shadow_color', style.get('shadow_color'))
        )
        log_info("Button styled.")
    except Exception as e:
        log_exception("Error in style_button", str(e))

def style_chip(label: QLabel, style: dict):
    log_section("python_gui_styles.py")
    log_subsection("style_chip")
    try:
        chip_bg = style.get('chip_bg', style.get('chip', {}).get('background', '#e7eaf3'))
        chip_fg = style.get('chip_fg', style.get('chip', {}).get('foreground', '#2563eb'))
        label.setStyleSheet(f"""
            QLabel {{
                background: {chip_bg};
                color: {chip_fg};
                border-radius: 16px;
                padding: 4px 12px;
                font-size: {style.get('font_size', 14)}px;
            }}
        """)
        log_info("Chip styled.")
    except Exception as e:
        log_exception("Error in style_chip", str(e))

def style_panel(widget: QWidget, style: dict):
    log_section("python_gui_styles.py")
    log_subsection("style_panel")
    try:
        widget.setStyleSheet(f"""
            QWidget {{
                background-color: {style.get('background', '#f3f6fd')};
                color: {style.get('foreground', '#1a1a1a')};
                border-radius: {style.get('border_radius', 8)}px;
            }}
        """)
        opacity = style.get('panel_opacity', 0.95)
        animate_widget_opacity(widget, style=style, start=opacity, end=1.0, duration=600)
        log_info("Panel styled.")
    except Exception as e:
        log_exception("Error in style_panel", str(e))

def style_link(label: QLabel, style: dict):
    log_section("python_gui_styles.py")
    log_subsection("style_link")
    try:
        link_fg = style.get('link_fg', style.get('link', {}).get('foreground', '#1976d2'))
        link_hover = style.get('link_hover', style.get('link', {}).get('hover', '#1565c0'))
        label.setStyleSheet(f"""
            QLabel {{
                color: {link_fg};
                text-decoration: underline;
                font-size: {style.get('font_size', 14)}px;
                background: transparent;
            }}
            QLabel:hover {{
                color: {link_hover};
            }}
        """)
        log_info("Link styled.")
    except Exception as e:
        log_exception("Error in style_link", str(e))

def style_icon_button(button: QPushButton, style: dict, icon_path=None):
    log_section("python_gui_styles.py")
    log_subsection("style_icon_button")
    try:
        link_hover = style.get('link_hover', style.get('link', {}).get('hover', '#1565c0'))
        button.setStyleSheet(f"""
            QPushButton {{
                background: none;
                border: none;
                color: {style.get('button_fg', '#1976d2')};
                font-size: {style.get('font_size', 14)}px;
            }}
            QPushButton:hover {{
                color: {link_hover};
            }}
        """)
        if icon_path:
            button.setIcon(QIcon(icon_path))
            button.setIconSize(button.size() * 0.7)
        log_info("Icon button styled.")
    except Exception as e:
        log_exception("Error in style_icon_button", str(e))

def apply_theme_style(widget, element_type, style: dict, icon_path=None):
    log_section("python_gui_styles.py")
    log_subsection("apply_theme_style")
    try:
        theme = style.get("theme", "modern")
        # Kombiniere Basis- und Theme-Styles falls nötig
        # Die Styles werden bereits als kombiniertes Dict übergeben

        if element_type == "button":
            style_button(widget, style)
        elif element_type == "chip":
            style_chip(widget, style)
        elif element_type == "panel":
            style_panel(widget, style)
        elif element_type == "link":
            style_link(widget, style)
        elif element_type == "icon_button":
            style_icon_button(widget, style, icon_path)
        log_info(f"Applied theme style: theme={theme}, element_type={element_type}")
    except Exception as e:
        log_exception("Error in apply_theme_style", str(e))