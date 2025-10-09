import json
import os
from config.dev import START_INI_FILE  # Use the unified variable

def load_settings():
    # Import logging only inside the function to avoid circular import
    try:
        from core.logger import log_info
    except ImportError:
        log_info = lambda msg: None
    try:
        if os.path.exists(START_INI_FILE ):
            with open(START_INI_FILE , "r", encoding="utf-8") as f:
                settings = json.load(f)
                log_info(f"Settings loaded from {START_INI_FILE }.")
                return settings
        return {"language": "en"}
    except Exception:
        return {"language": "en"}

def save_settings(settings):
    try:
        from core.logger import log_info, log_exception
    except ImportError:
        log_info = lambda msg: None
        log_exception = lambda msg, exc=None: None
    try:
        json_str = json.dumps(settings, indent=2)
        log_info(f"Saving settings to {START_INI_FILE }.")
        log_info(f"JSON preview:\n{json_str}")
        with open(START_INI_FILE , "w", encoding="utf-8") as f:
            f.write(json_str)
        log_info("Settings saved successfully.")
    except Exception as e:
        log_exception("Error while saving settings", e)