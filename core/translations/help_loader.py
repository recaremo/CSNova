import json
import os

def load_help_texts(lang="en"):
    filename = f"help_{lang}.json"
    base_path = os.path.join(os.path.dirname(__file__), "help")
    file_path = os.path.join(base_path, filename)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Could not load help texts for language '{lang}': {e}")
        return {}