import json
import re

from deep_translator import GoogleTranslator


def translate_text_preserving_placeholders(text, translator):
    # Find placeholders like {name}, {0}, {user_name}
    placeholders = re.findall(r"\{[^}]+\}", text)

    # Replace them with temporary tokens
    temp_text = text
    for i, ph in enumerate(placeholders):
        temp_text = temp_text.replace(ph, f"__PH_{i}__")

    # Translate only if there's something besides placeholders
    translated = translator.translate(temp_text)

    # Put placeholders back
    for i, ph in enumerate(placeholders):
        translated = translated.replace(f"__PH_{i}__", ph)

    return translated


# === Main ===
with open("merged_english.json", "r", encoding="utf-8") as f:
    data = json.load(f)

translator = GoogleTranslator(source="fr", target="id")
translated = {}

for key, value in data.items():
    if isinstance(value, str):
        try:
            result = translate_text_preserving_placeholders(value, translator)
            translated[key] = result
            print(f"word: {value}\n→ translation: {result}\n")
        except Exception as e:
            print(f"Error translating key '{key}': {e}")
            translated[key] = value  # fallback to original
    else:
        translated[key] = value

with open("ina.json", "w", encoding="utf-8") as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print("✅ Translation complete! Saved as ina.json")
