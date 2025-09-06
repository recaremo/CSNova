import sys
import json
import os
from config.dev import (
    GUI_DIR, USER_SETTINGS_FILE, BASE_STYLE_FILE, THEMES_STYLE_FILE,
    CSNOVA_BASE_STYLE_FILE, CSNOVA_THEMES_STYLE_FILE, CSNOVA_FORMS_STYLE_FILE, TRANSLATIONS_DIR
)
from core.style_utils import (
    generate_csnova_styles,
    load_global_stylesheet,
    save_user_settings,
    generate_translation_file
)
import locale
from PySide6.QtWidgets import QApplication
from gui.start_window import StartWindow
from core.logger import log_section, log_subsection, log_info, log_exception

DEFAULT_SETTINGS = {
    "monitor": {
        "screen_resolution": "1920x1080",
        "screen_dpi": 96,
        "scale_factor": 1.0
    },
    "window": {
        "start_window_bnt_width": 240,
        "start_window_bnt_height": 60,
        "start_window_bnt_top_offset": 270,
        "start_window_bnt_left_offset": 1350,
        "start_window_bnt_spacing": 42
    },
    "preferences_window": {
        "width": 500,
        "height": 320
    },
    "panels": {
        "splitter_sizes": [
            200,
            1200,
            520
        ]
    },
    "gui": {
        "style": "modern",
        "theme": "middle"
    },
    "general": {
        "language": "en"
    },
    "help": {
        "show_help_panel": True,
        "show_button_hints": True,
        "show_start_image": True
    }
}

def detect_system_language():
    lang, encoding = locale.getlocale()
    if lang:
        return lang.split('_')[0]
    return "en"

def deep_update(target, defaults):
    for key, value in defaults.items():
        if key not in target:
            target[key] = value
        elif isinstance(value, dict) and isinstance(target[key], dict):
            deep_update(target[key], value)

def load_or_create_user_settings():
    if os.path.exists(USER_SETTINGS_FILE):
        with open(USER_SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
        deep_update(settings, DEFAULT_SETTINGS)
    else:
        settings = json.loads(json.dumps(DEFAULT_SETTINGS))
        system_lang = detect_system_language()
        settings["general"]["language"] = system_lang
        with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2)
    return settings

def initialize_screen_settings(settings, app):
    log_section("csNova.py")
    log_subsection("initialize_screen_settings")
    try:
        screen = app.primaryScreen()
        size = screen.size()
        dpi = screen.logicalDotsPerInch()
        scale_factor = dpi / 96

        settings["monitor"]["screen_resolution"] = f"{size.width()}x{size.height()}"
        settings["monitor"]["screen_dpi"] = dpi
        settings["monitor"]["scale_factor"] = scale_factor

        settings["window"]["start_window_bnt_width"] = int(240 * scale_factor)
        settings["window"]["start_window_bnt_height"] = int(60 * scale_factor)
        settings["window"]["start_window_bnt_top_offset"] = int(270 * scale_factor)
        settings["window"]["start_window_bnt_left_offset"] = int(1350 * scale_factor)
        settings["window"]["start_window_bnt_spacing"] = int(42 * scale_factor)

        save_user_settings(settings, USER_SETTINGS_FILE)
        log_info("Screen settings initialized and saved.")
    except Exception as e:
        log_exception("Error initializing screen settings", str(e))

def check_and_update_screen_settings(settings, app):
    log_section("csNova.py")
    log_subsection("check_and_update_screen_settings")
    try:
        screen = app.primaryScreen()
        size = screen.size()
        dpi = screen.logicalDotsPerInch()
        current_resolution = f"{size.width()}x{size.height()}"
        current_dpi = dpi

        if (settings["monitor"].get("screen_resolution") != current_resolution or
            settings["monitor"].get("screen_dpi") != current_dpi):
            settings["monitor"]["screen_resolution_changed"] = True
            initialize_screen_settings(settings, app)
            log_info("Screen resolution or DPI changed, settings updated.")
        else:
            settings["monitor"]["screen_resolution_changed"] = False

        return settings
    except Exception as e:
        log_exception("Error checking/updating screen settings", str(e))
        return settings

def ensure_style_files(settings):
    # Erzeuge alle notwendigen Style-Dateien, falls sie fehlen
    if not os.path.exists(CSNOVA_BASE_STYLE_FILE) or not os.path.exists(CSNOVA_THEMES_STYLE_FILE):
        generate_csnova_styles(settings)
    # Forms-Styles werden in generate_csnova_styles() behandelt

def main():
    log_section("csNova.py")
    log_subsection("main")
    try:
        app = QApplication(sys.argv)
        app.setStyle("Fusion")

        settings = load_or_create_user_settings()
        language_code = settings["general"].get("language", "en")
        settings = check_and_update_screen_settings(settings, app)
        translation_file = generate_translation_file(language_code, TRANSLATIONS_DIR)

        # Erzeuge alle notwendigen Style-Dateien, falls sie fehlen
        ensure_style_files(settings)

        # Korrektur: Styles mit Platzhalterersetzung generieren und verwenden!
        combined_style = generate_csnova_styles(
            settings,
            BASE_STYLE_FILE,
            THEMES_STYLE_FILE,
            CSNOVA_BASE_STYLE_FILE,
            CSNOVA_THEMES_STYLE_FILE,
            CSNOVA_FORMS_STYLE_FILE,
            GUI_DIR
        )
        #print(load_global_stylesheet(combined_style))  # Debug-Ausgabe

        app.setStyleSheet(load_global_stylesheet(combined_style))

        window = StartWindow(
            translation_file=translation_file,
            settings=settings
        )
        window.show()

        log_info("CSNova main window shown.")
        sys.exit(app.exec())
    except Exception as e:
        log_exception("Error in csNova main execution", str(e))

if __name__ == "__main__":
    main()