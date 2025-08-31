# Modern style (Windows 11 inspired) with integrated modes

def get_style(mode):
    """
    Returns the style dictionary for the given mode.
    All parameters are defined directly in this file.
    """
    if mode == "light":
        return {
            "background": "#f3f6fd",      # very light blueish white
            "foreground": "#1a1a1a",      # almost black, but softer
            "button": {
                "background": "#e7eaf3",
                "foreground": "#1a1a1a",
                "hover": "#d0d6e6",
                "active": "#b6c2e1"
            },
            "input": {
                "background": "#ffffff",
                "foreground": "#1a1a1a"
            },
            "border": "#cfd8dc",
            "highlight": "#2563eb",       # modern blue accent
            "error": "#ef4444"            # modern error red
        }
    elif mode == "middle":
        return {
            "background": "#e0e5ef",
            "foreground": "#23272f",
            "button": {
                "background": "#cfd8dc",
                "foreground": "#23272f",
                "hover": "#b6c2e1",
                "active": "#2563eb"
            },
            "input": {
                "background": "#f3f6fd",
                "foreground": "#23272f"
            },
            "border": "#b6c2e1",
            "highlight": "#2563eb",
            "error": "#ef4444"
        }
    elif mode == "dark":
        return {
            "background": "#181a20",
            "foreground": "#e7eaf3",
            "button": {
                "background": "#23272f",
                "foreground": "#e7eaf3",
                "hover": "#2563eb",
                "active": "#1e293b"
            },
            "input": {
                "background": "#23272f",
                "foreground": "#e7eaf3"
            },
            "border": "#2563eb",
            "highlight": "#60a5fa",
            "error": "#ef4444"
        }
    else:
        # fallback: light
        return {
            "background": "#f3f6fd",
            "foreground": "#1a1a1a",
            "button": {
                "background": "#e7eaf3",
                "foreground": "#1a1a1a",
                "hover": "#d0d6e6",
                "active": "#b6c2e1"
            },
            "input": {
                "background": "#ffffff",
                "foreground": "#1a1a1a"
            },
            "border": "#cfd8dc",
            "highlight": "#2563eb",
            "error": "#ef4444"
        }