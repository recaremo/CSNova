# Future style (glassmorphism, adaptive, modern) with integrated modes

def get_style(mode):
    """
    Returns the style dictionary for the given mode.
    All parameters are defined directly in this file.
    """
    if mode == "light":
        return {
            "background": "rgba(245, 250, 255, 0.85)",   # semi-transparent, glass effect
            "foreground": "#22223b",                     # deep blue-grey
            "button": {
                "background": "rgba(230, 240, 255, 0.95)",
                "foreground": "#22223b",
                "hover": "#b8c6db",
                "active": "#7f9acb"
            },
            "input": {
                "background": "rgba(255,255,255,0.95)",
                "foreground": "#22223b"
            },
            "border": "#a3bffa",
            "highlight": "#7f9acb",                      # soft futuristic blue
            "error": "#ff6b6b"                           # neon red
        }
    elif mode == "middle":
        return {
            "background": "rgba(210, 220, 235, 0.90)",
            "foreground": "#22223b",
            "button": {
                "background": "#b8c6db",
                "foreground": "#22223b",
                "hover": "#7f9acb",
                "active": "#a3bffa"
            },
            "input": {
                "background": "rgba(240,245,250,0.95)",
                "foreground": "#22223b"
            },
            "border": "#7f9acb",
            "highlight": "#a3bffa",
            "error": "#ff6b6b"
        }
    elif mode == "dark":
        return {
            "background": "rgba(30, 34, 45, 0.92)",
            "foreground": "#e0eaff",
            "button": {
                "background": "#22223b",
                "foreground": "#e0eaff",
                "hover": "#7f9acb",
                "active": "#a3bffa"
            },
            "input": {
                "background": "rgba(40,44,54,0.95)",
                "foreground": "#e0eaff"
            },
            "border": "#7f9acb",
            "highlight": "#a3bffa",
            "error": "#ff6b6b"
        }
    else:
        # fallback: light
        return {
            "background": "rgba(245, 250, 255, 0.85)",
            "foreground": "#22223b",
            "button": {
                "background": "rgba(230, 240, 255, 0.95)",
                "foreground": "#22223b",
                "hover": "#b8c6db",
                "active": "#7f9acb"
            },
            "input": {
                "background": "rgba(255,255,255,0.95)",
                "foreground": "#22223b"
            },
            "border": "#a3bffa",
            "highlight": "#7f9acb",
            "error": "#ff6b6b"
        }