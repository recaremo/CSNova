import json
import re
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QColor
from core.logger import log_info, log_error, log_exception

def load_theme(theme_path):
    try:
        with open(theme_path, "r", encoding="utf-8") as f:
            theme = json.load(f)
        log_info(f"Theme loaded from {theme_path}: {list(theme.keys())}")
        return theme
    except Exception as e:
        log_exception(f"Failed to load theme from {theme_path}", e)
        return {}

def parse_shadow(shadow_str):
    # rgba-Format: "0 2px 12px rgba(37,99,235,0.08)"
    match = re.match(r"(\d+)\s+(\d+)px\s+(\d+)px\s+rgba\((\d+),(\d+),(\d+),([0-9.]+)\)", shadow_str)
    if match:
        offset_x = int(match.group(1))
        offset_y = int(match.group(2))
        blur_radius = int(match.group(3))
        r = int(match.group(4))
        g = int(match.group(5))
        b = int(match.group(6))
        a = float(match.group(7))
        color = QColor(r, g, b, int(a * 255))
        return offset_x, offset_y, blur_radius, color
    # Hex-Format: "0 0 0 2px #2563eb44"
    match = re.match(r"(\d+)\s+(\d+)\s+(\d+)\s+(\d+)px\s+#([0-9a-fA-F]{6})([0-9a-fA-F]{2})", shadow_str)
    if match:
        offset_x = int(match.group(1))
        offset_y = int(match.group(2))
        blur_radius = int(match.group(4))
        hex_color = match.group(5)
        alpha = int(match.group(6), 16)
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        color = QColor(r, g, b, alpha)
        return offset_x, offset_y, blur_radius, color
    log_error(f"Shadow string could not be parsed: {shadow_str}")
    return 0, 2, 12, QColor(0, 0, 0, 30)

def apply_panel_shadow(widget, theme):
    shadow = theme.get("panel_shadow")
    if shadow:
        try:
            effect = QGraphicsDropShadowEffect(widget)
            offset_x, offset_y, blur_radius, color = parse_shadow(shadow)
            effect.setOffset(offset_x, offset_y)
            effect.setBlurRadius(blur_radius)
            effect.setColor(color)
            widget.setGraphicsEffect(effect)
            log_info(f"Panel shadow applied to {widget}: {shadow}")
        except Exception as e:
            log_exception(f"Failed to apply panel shadow to {widget}", e)

def apply_card_shadow(widget, theme):
    shadow = theme.get("card_shadow")
    if shadow:
        try:
            effect = QGraphicsDropShadowEffect(widget)
            offset_x, offset_y, blur_radius, color = parse_shadow(shadow)
            effect.setOffset(offset_x, offset_y)
            effect.setBlurRadius(blur_radius)
            effect.setColor(color)
            widget.setGraphicsEffect(effect)
            log_info(f"Card shadow applied to {widget}: {shadow}")
        except Exception as e:
            log_exception(f"Failed to apply card shadow to {widget}", e)

def apply_avatar_shadow(widget, theme):
    shadow = theme.get("avatar_shadow")
    if shadow:
        try:
            effect = QGraphicsDropShadowEffect(widget)
            offset_x, offset_y, blur_radius, color = parse_shadow(shadow)
            effect.setOffset(offset_x, offset_y)
            effect.setBlurRadius(blur_radius)
            effect.setColor(color)
            widget.setGraphicsEffect(effect)
            log_info(f"Avatar shadow applied to {widget}: {shadow}")
        except Exception as e:
            log_exception(f"Failed to apply avatar shadow to {widget}", e)

def apply_badge_shadow(widget, theme):
    shadow = theme.get("badge_shadow")
    if shadow:
        try:
            effect = QGraphicsDropShadowEffect(widget)
            offset_x, offset_y, blur_radius, color = parse_shadow(shadow)
            effect.setOffset(offset_x, offset_y)
            effect.setBlurRadius(blur_radius)
            effect.setColor(color)
            widget.setGraphicsEffect(effect)
            log_info(f"Badge shadow applied to {widget}: {shadow}")
        except Exception as e:
            log_exception(f"Failed to apply badge shadow to {widget}", e)

def apply_animation(widget, theme):
    duration = theme.get("animation_duration")
    if duration:
        try:
            effect = QGraphicsOpacityEffect(widget)
            widget.setGraphicsEffect(effect)
            animation = QPropertyAnimation(effect, b"opacity")
            animation.setDuration(duration)
            animation.setStartValue(1.0)
            animation.setEndValue(0.5)
            log_info(f"Animation applied to {widget}: duration={duration}")
            return animation
        except Exception as e:
            log_exception(f"Failed to apply animation to {widget}", e)

def apply_focus_shadow(widget, theme):
    shadow = theme.get("focus_shadow")
    if shadow:
        try:
            offset_x, offset_y, blur_radius, color = parse_shadow(shadow)
            effect = QGraphicsDropShadowEffect(widget)
            effect.setOffset(offset_x, offset_y)
            effect.setBlurRadius(blur_radius)
            effect.setColor(color)
            widget.setGraphicsEffect(effect)
            log_info(f"Focus shadow applied to {widget}: {shadow}")
        except Exception as e:
            log_exception(f"Failed to apply focus shadow to {widget}", e)

def apply_disabled_opacity(widget, theme):
    opacity = theme.get("disabled_opacity")
    if opacity is not None and not widget.isEnabled():
        try:
            widget.setWindowOpacity(opacity)
            log_info(f"Disabled opacity applied to {widget}: {opacity}")
        except Exception as e:
            log_exception(f"Failed to apply disabled opacity to {widget}", e)

def apply_theme_style(widget, widget_type, theme, extra=None):
    """
    Hauptfunktion zum Anwenden aller nicht-Qt-kompatiblen Styles auf ein Widget.
    Zusätzlich werden Qt-StyleSheets für Buttons und Header gesetzt.
    """
    try:
        log_info(f"Applying theme style: widget_type={widget_type}, widget={widget}, theme_keys={list(theme.keys())}")

        # Schatten und Effekte
        if widget_type == "panel":
            apply_panel_shadow(widget, theme)
        elif widget_type == "card":
            apply_card_shadow(widget, theme)
        elif widget_type == "avatar":
            apply_avatar_shadow(widget, theme)
        elif widget_type == "badge":
            apply_badge_shadow(widget, theme)
        elif widget_type == "focus":
            apply_focus_shadow(widget, theme)
        elif widget_type == "disabled":
            apply_disabled_opacity(widget, theme)

        # Animationen
        if theme.get("animation_duration"):
            apply_animation(widget, theme)

        # Qt-StyleSheet für Buttons
        if widget_type == "button":
            style = f"""
            QPushButton {{
                background-color: {theme.get('button_bg', '#fff')};
                color: {theme.get('button_fg', '#222')};
                border-radius: {theme.get('button_radius', 4)}px;
                border: {theme.get('button_border', 'none')};
                font-size: {theme.get('button_font_size', 13)}px;
                padding: {theme.get('button_padding', '8px 24px')};
            }}
            QPushButton:hover {{
                background-color: {theme.get('button_hover', '#eee')};
            }}
            QPushButton:pressed {{
                background-color: {theme.get('button_active', '#ccc')};
            }}
            QPushButton:disabled {{
                background-color: {theme.get('button_disabled_bg', '#e5e5e5')};
                color: {theme.get('button_disabled_fg', '#888899')};
            }}
            """
            widget.setStyleSheet(style)
            log_info(f"Button stylesheet applied to {widget}: {style}")

        # Qt-StyleSheet für Header
        if widget_type == "header":
            style = f"""
            QLabel {{
                background-color: {theme.get('header_bg', '#fff')};
                color: {theme.get('header_fg', '#222')};
                font-size: {theme.get('header_font_size', 15)}px;
                border-bottom: {theme.get('header_border', 'none')};
            }}
            """
            widget.setStyleSheet(style)
            log_info(f"Header stylesheet applied to {widget}: {style}")

        # Qt-StyleSheet für Chips, Tabs, etc. können analog ergänzt werden

    except Exception as e:
        log_exception(f"Failed to apply theme style to {widget_type} ({widget})", e)

__all__ = ["apply_theme_style"]