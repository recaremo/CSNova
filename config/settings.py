import json
import os

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error

# Import the central settings file path
from config.dev import SETTINGS_FILE

def load_settings():
    log_section("settings.py")
    log_subsection("load_settings")
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                settings = json.load(f)
                log_info(f"Settings loaded from {SETTINGS_FILE}.")
                return settings
        log_info("Settings file not found, using fallback settings.")
        return {"language": "en"}  # Fallback
    except Exception as e:
        log_error(f"Error loading settings: {e}")
        return {"language": "en"}

def save_settings(settings):
    log_section("settings.py")
    log_subsection("save_settings")
    try:
        json_str = json.dumps(settings, indent=2)
        log_info(f"Saving settings to {SETTINGS_FILE}.")
        log_info(f"JSON preview:\n{json_str}")
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            f.write(json_str)
        log_info("Settings saved successfully.")
    except Exception as e:
        log_error(f"Error while saving settings: {e}")