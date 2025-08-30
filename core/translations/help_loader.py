import json
import os

# Import central logging functions
from core.lloger import log_section, log_subsection, log_info, log_error

# Import the central help directory
from config.dev import HELP_DIR

def load_help_texts(lang="en"):
    log_section("help_loader.py")
    log_subsection("load_help_texts")
    filename = f"help_{lang}.json"
    file_path = HELP_DIR / filename

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            help_texts = json.load(f)
            log_info(f"Help texts loaded for language '{lang}' from {file_path}.")
            return help_texts
    except Exception as e:
        log_error(f"Could not load help texts for language '{lang}': {e}")
        return {}