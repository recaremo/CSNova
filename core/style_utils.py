import json
import os

def load_global_stylesheet(theme_style):
    css = ""
    for selector, props in theme_style.items():
        if not selector.isidentifier():
            css += selector + " {\n"
            for key, value in props.items():
                css += f"  {key}: {value};\n"
            css += "}\n"
    return css

def flatten_theme_dict(theme_dict):
    flat = {}
    def _flatten(d):
        for k, v in d.items():
            if isinstance(v, dict):
                _flatten(v)
            else:
                flat[k] = v
    _flatten(theme_dict)
    return flat

def fill_placeholders(style_dict, theme_dict):
    filled = {}
    flat = flatten_theme_dict(theme_dict)
    for selector, props in style_dict.items():
        filled_props = {}
        for key, value in props.items():
            if isinstance(value, str):
                try:
                    filled_props[key] = value.format(**flat)
                except Exception:
                    filled_props[key] = value
            else:
                filled_props[key] = value
        filled[selector] = filled_props
    return filled

def generate_csnova_styles(settings,
                           BASE_STYLE_FILE,
                           THEMES_STYLE_FILE,
                           CSNOVA_BASE_STYLE_FILE,
                           CSNOVA_THEMES_STYLE_FILE,
                           CSNOVA_FORMS_STYLE_FILE,
                           GUI_DIR):
    if not os.path.exists(BASE_STYLE_FILE):
        with open(BASE_STYLE_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)
    if not os.path.exists(THEMES_STYLE_FILE):
        with open(THEMES_STYLE_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)

    with open(BASE_STYLE_FILE, "r", encoding="utf-8") as f:
        base_styles = json.load(f)
    with open(THEMES_STYLE_FILE, "r", encoding="utf-8") as f:
        themes = json.load(f)
    style = settings["gui"].get("style", "modern")
    theme = settings["gui"].get("theme", "middle")
    theme_dict = themes.get(style, themes.get("modern", {})).get(theme, themes.get("modern", {}).get("middle", {}))

    base_style_filled = fill_placeholders(base_styles, theme_dict)
    theme_style_filled = fill_placeholders(themes, theme_dict)

    with open(CSNOVA_BASE_STYLE_FILE, "w", encoding="utf-8") as f:
        json.dump(base_style_filled, f, indent=2, ensure_ascii=False)
    with open(CSNOVA_THEMES_STYLE_FILE, "w", encoding="utf-8") as f:
        json.dump(theme_style_filled, f, indent=2, ensure_ascii=False)

    forms_style_path = GUI_DIR / "styles" / "forms_style.json"
    if forms_style_path.exists():
        with open(forms_style_path, "r", encoding="utf-8") as f:
            forms_styles = json.load(f)
        forms_style_filled = fill_placeholders(forms_styles, theme_dict)
        with open(CSNOVA_FORMS_STYLE_FILE, "w", encoding="utf-8") as f:
            json.dump(forms_style_filled, f, indent=2, ensure_ascii=False)

    combined_style = {**base_style_filled, **theme_style_filled}
    return combined_style

def save_user_settings(settings, USER_SETTINGS_FILE):
    try:
        with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2)
        return True
    except Exception:
        return False

def generate_translation_file(language_code, TRANSLATIONS_DIR):
    translations_path = TRANSLATIONS_DIR / "translations.json"
    target_path = TRANSLATIONS_DIR / f"translation_{language_code}.json"
    try:
        with open(translations_path, "r", encoding="utf-8") as f:
            all_translations = json.load(f)
        lang_translations = all_translations.get(language_code, {})
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(lang_translations, f, indent=2, ensure_ascii=False)
        return target_path
    except Exception as e:
        print(f"Error generating translation file: {e}")
        return None