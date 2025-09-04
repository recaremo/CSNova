import sys
import json
from PySide6.QtWidgets import QApplication
from core.translator import Translator
from config.dev import USER_SETTINGS_FILE
from gui.start_window import StartWindow
from core.logger import log_section, log_subsection, log_info, log_exception
from gui.styles.form_styles import load_global_stylesheet

# Default settings used as fallback if user_settings.json is missing or incomplete
DEFAULT_SETTINGS = {
    "first_start": True,
    "screen_resolution": "1920x1080",
    "screen_dpi": 96,
    "scale_factor": 1.0,
    "language": "en",
    "style": "style_modern",
    "theme": "theme_neutral",
    "splitter_sizes": [
    200,
    1200,
    520
  ],
    "mode": "neutral",
    "start_window_bnt_width": 240,
    "start_window_bnt_height": 60,
    "start_window_bnt_top_offset": 270,
    "start_window_bnt_left_offset": 1350,
    "start_window_bnt_spacing": 42
}

def load_user_settings():
    """
    Loads user settings from user_settings.json.
    If loading fails or keys are missing, uses DEFAULT_SETTINGS as fallback.
    Logs success or error.
    """
    try:
        with open(USER_SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
        # Fill missing keys with defaults
        for key, value in DEFAULT_SETTINGS.items():
            if key not in settings:
                settings[key] = value
                log_info(f"Missing key '{key}' set to default: {value}")
        log_info("user_settings.json loaded successfully.")
        return settings
    except Exception as e:
        log_exception("Error loading user_settings.json, using defaults.", e)
        return DEFAULT_SETTINGS.copy()

def save_user_settings(settings):
    """
    Saves user settings to user_settings.json.
    Logs success or error.
    """
    try:
        with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2)
        log_info("user_settings.json saved successfully.")
    except Exception as e:
        log_exception("Error saving user_settings.json", e)

def initialize_screen_settings(settings, app):
    """
    Initializes and saves screen-dependent settings (resolution, DPI, scale factor, button positions)
    for the first program start or after a screen change.
    """
    screen = app.primaryScreen()
    size = screen.size()
    dpi = screen.logicalDotsPerInch()
    scale_factor = dpi / 96  # 96 DPI is standard

    settings["screen_resolution"] = f"{size.width()}x{size.height()}"
    settings["screen_dpi"] = dpi
    settings["scale_factor"] = scale_factor

    # Adjust button values according to scale factor
    settings["start_window_bnt_width"] = int(240 * scale_factor)
    settings["start_window_bnt_height"] = int(60 * scale_factor)
    settings["start_window_bnt_top_offset"] = int(270 * scale_factor)
    settings["start_window_bnt_left_offset"] = int(1350 * scale_factor)
    settings["start_window_bnt_spacing"] = int(42 * scale_factor)

    settings["first_start"] = False
    save_user_settings(settings)
    log_info("Screen settings initialized and saved.")

def check_and_update_screen_settings(settings, app):
    """
    Checks if the screen resolution or DPI has changed.
    If changed, re-initializes and saves screen-dependent settings.
    """
    screen = app.primaryScreen()
    size = screen.size()
    dpi = screen.logicalDotsPerInch()
    current_resolution = f"{size.width()}x{size.height()}"
    current_dpi = dpi

    # Check for changes in resolution or DPI
    if (settings.get("screen_resolution") != current_resolution or
        settings.get("screen_dpi") != current_dpi):
        settings["screen_resolution_changed"] = True
        initialize_screen_settings(settings, app)
        log_info("Screen resolution or DPI changed, settings updated.")
    else:
        settings["screen_resolution_changed"] = False

    return settings

def main():
    """
    Main entry point for CSNova.
    Loads and checks user settings, initializes screen settings if needed,
    and starts the main window.
    """
    log_section("csNova.py")
    log_subsection("main")
    try:
        app = QApplication(sys.argv)
        app.setStyleSheet(load_global_stylesheet())

        settings = load_user_settings()
        # If first_start is True, initialize screen settings
        if settings.get("first_start", True):
            initialize_screen_settings(settings, app)
        else:
            settings = check_and_update_screen_settings(settings, app)

        language = settings.get("language", "en")
        translator = Translator(language)
        window = StartWindow(default_language=language)
        window.show()
        log_info("CSNova main window shown.")
        sys.exit(app.exec())
    except Exception as e:
        log_exception("Error in csNova main execution", e)

if __name__ == "__main__":
    main()