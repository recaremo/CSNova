import json
import os

def load_form_labels(language="en"):
    path = f"core/translations/forms/form_{language}.json"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
