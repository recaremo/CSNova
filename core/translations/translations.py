from pathlib import Path
import json

LANGUAGES = ["de", "en", "fr", "es"]
TRANSLATIONS = {}

for lang in LANGUAGES:
    path = Path(__file__).parent / f"{lang}.json"
    with open(path, "r", encoding="utf-8") as f:
        TRANSLATIONS[lang] = json.load(f)