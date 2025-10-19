import json
from pathlib import Path

TEMPLATE_PATH = "animals_template.html"
DATA_PATH = "animals_data.json"
OUTPUT_PATH = "animals.html"

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def build_animals_html_items(data):
    parts = []
    for animal in data:
        name = animal.get("name")
        locations = animal.get("locations") or []
        characteristics = animal.get("characteristics") or {}
        diet = characteristics.get("diet")
        type_ = characteristics.get("type")

        # Skip empty items entirely
        if not any([name, diet, locations, type_]):
            continue

        parts.append('<li class="cards__item">')
        # Title
        if name:
            parts.append(f'  <div class="card__title">{name}</div>')
        # Body text with labeled lines
        parts.append('  <p class="card__text">')
        if diet:
            parts.append(f'      <strong>Diet:</strong> {diet}<br/>')
        if locations:
            parts.append(f'      <strong>Location:</strong> {locations[0]}<br/>')
        if type_:
            parts.append(f'      <strong>Type:</strong> {type_}<br/>')
        parts.append('  </p>')
        parts.append('</li>')
    return "\n".join(parts)

def read_template(path):
    return Path(path).read_text(encoding="utf-8")

def write_output(path, content):
    Path(path).write_text(content, encoding="utf-8")

def main():
    data = load_data(DATA_PATH)
    items_html = build_animals_html_items(data)
    template = read_template(TEMPLATE_PATH)
    html_out = template.replace("__REPLACE_ANIMALS_INFO__", items_html)
    write_output(OUTPUT_PATH, html_out)
    print(f"Wrote {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
