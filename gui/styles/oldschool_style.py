# Old-School style (Windows 10 inspired) with integrated modes
from PySide6.QtWidgets import QApplication, QStyle
from PySide6.QtGui import QIcon

def qt_icon(name):
    mapping = {
        "new": QStyle.SP_FileIcon,
        "delete": QStyle.SP_TrashIcon,
        "prev": QStyle.SP_ArrowBack,
        "next": QStyle.SP_ArrowForward,
        "save": QStyle.SP_DialogSaveButton
    }
    app = QApplication.instance()
    if name in mapping and app:
        return app.style().standardIcon(mapping[name])
    return QIcon()  # Immer ein QIcon zurückgeben!

def get_style(mode):
    # ...existing code...
    if mode == "light":
        style_dict = {
            "background": "#ffffff",
            "foreground": "#222326",
            "button": {
                "background": "#f3f3f3",
                "foreground": "#222326",
                "hover": "#e5e5e5",
                "active": "#d0d0d0"
            },
            "input": {
                "background": "#f9f9f9",
                "foreground": "#222326"
            },
            "border": "#cfcfcf",
            "highlight": "#0078d7",
            "error": "#e81123"
        }
        style_dict["icon_factory"] = qt_icon
        return style_dict
    elif mode == "middle":
        style_dict = {
            "background": "#f3f3f3",
            "foreground": "#222326",
            "button": {
                "background": "#e5e5e5",
                "foreground": "#222326",
                "hover": "#d0d0d0",
                "active": "#bcbcbc"
            },
            "input": {
                "background": "#ededed",
                "foreground": "#222326"
            },
            "border": "#bcbcbc",
            "highlight": "#0078d7",
            "error": "#e81123"
        }
        style_dict["icon_factory"] = qt_icon
        return style_dict
    elif mode == "dark":
        style_dict = {
            "background": "#1e1e1e",
            "foreground": "#f3f3f3",
            "button": {
                "background": "#2d2d2d",
                "foreground": "#f3f3f3",
                "hover": "#3c3c3c",
                "active": "#0078d7"
            },
            "input": {
                "background": "#252526",
                "foreground": "#f3f3f3"
            },
            "border": "#3c3c3c",
            "highlight": "#0078d7",
            "error": "#e81123"
        }
        style_dict["icon_factory"] = qt_icon
        return style_dict
    else:
        style_dict = {
            "background": "#ffffff",
            "foreground": "#222326",
            "button": {
                "background": "#f3f3f3",
                "foreground": "#222326",
                "hover": "#e5e5e5",
                "active": "#d0d0d0"
            },
            "input": {
                "background": "#f9f9f9",
                "foreground": "#222326"
            },
            "border": "#cfcfcf",
            "highlight": "#0078d7",
            "error": "#e81123"
        }
        style_dict["icon_factory"] = qt_icon
        return style_dict