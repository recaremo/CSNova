# Vintage style (cozy living room inspired) with integrated modes

def get_style(mode):
    """
    Returns the style dictionary for the given mode.
    All parameters are defined directly in this file.
    """
    if mode == "light":
        return {
            "background": "#f5eee6",      # warm beige
            "foreground": "#5a4632",      # dark brown
            "button": {
                "background": "#e2d3c3",
                "foreground": "#5a4632",
                "hover": "#d6c3a3",
                "active": "#cbb393"
            },
            "input": {
                "background": "#f8f3ed",
                "foreground": "#5a4632"
            },
            "border": "#cbb393",
            "highlight": "#b48a78",       # warm reddish brown
            "error": "#a94442"            # muted red
        }
    elif mode == "middle":
        return {
            "background": "#e9e2d3",
            "foreground": "#5a4632",
            "button": {
                "background": "#d6c3a3",
                "foreground": "#5a4632",
                "hover": "#cbb393",
                "active": "#b48a78"
            },
            "input": {
                "background": "#ede6d6",
                "foreground": "#5a4632"
            },
            "border": "#b48a78",
            "highlight": "#a67c52",
            "error": "#a94442"
        }
    elif mode == "dark":
        return {
            "background": "#3b2c23",
            "foreground": "#e2d3c3",
            "button": {
                "background": "#5a4632",
                "foreground": "#e2d3c3",
                "hover": "#7c624a",
                "active": "#a67c52"
            },
            "input": {
                "background": "#4e3b2a",
                "foreground": "#e2d3c3"
            },
            "border": "#7c624a",
            "highlight": "#b48a78",
            "error": "#a94442"
        }
    else:
        # fallback: light
        return {
            "background": "#f5eee6",
            "foreground": "#5a4632",
            "button": {
                "background": "#e2d3c3",
                "foreground": "#5a4632",
                "hover": "#d6c3a3",
                "active": "#cbb393"
            },
            "input": {
                "background": "#f8f3ed",
                "foreground": "#5a4632"
            },
            "border": "#cbb393",
            "highlight": "#b48a78",
            "error": "#a94442"
        }