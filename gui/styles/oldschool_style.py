# Old-School style (Windows 10 inspired) with integrated modes

def get_style(mode):
    """
    Returns the style dictionary for the given mode.
    All parameters are defined directly in this file.
    """
    if mode == "light":
        return {
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
            "highlight": "#0078d7",  # Windows 10 blue
            "error": "#e81123"       # Windows error red
        }
    elif mode == "middle":
        return {
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
    elif mode == "dark":
        return {
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
    else:
        # fallback: light
        return {
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