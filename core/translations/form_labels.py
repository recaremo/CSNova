import json
import os

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error

# Import the central forms directory
from config.dev import FORMS_DIR

def load_form_labels(language="en"):
    log_section("form_labels.py")
    log_subsection("load_form_labels")
    path = FORMS_DIR / f"form_{language}.json"
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                labels = json.load(f)
                log_info(f"Form labels loaded for language '{language}' from {path}.")
                return labels
        else:
            log_error(f"Form labels file not found: {path}")
            return {}
    except Exception as e:
        log_error(f"Error loading form labels for language '{language}': {e}")
        return {}