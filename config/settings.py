# config/settings.py

import json
import os

SETTINGS_FILE = "config/user_settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"language": "en"}  # Fallback

def save_settings(settings):
    print("Saving to:", SETTINGS_FILE)
    try:
        json_str = json.dumps(settings, indent=2)
        print("JSON preview:\n", json_str)
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            f.write(json_str)
        print("Settings saved.")
    except Exception as e:
        print("❌ Error while saving settings:", e)
