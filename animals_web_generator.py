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

        item_lines = []
        if name:
            item_lines.append(f"Name: {name}<br/>")
        if diet:
            item_lines.append(f"Diet: {diet}<br/>")
        if locations:
            item_lines.append(f"Location: {locations[0]}<br/>")
        if type_:
            item_lines.append(f"Type: {type_}<br/>")

        # Only add the <li> if there is any content
        if item_lines:
            parts.append('<li class="cards__item">')
            parts.extend(item_lines)
            parts.append("</li>")
    return "\n".join(parts)

def read_template(path):
    return Path(path).read_text(encoding="utf-8")

def write_output(path, content):
    Path(path).write_text(content, encoding="utf-8")

def main():
    data = load_data(DATA_PATH)
    items_html = build_animals_html_items(data)
    template = read_template(TEMPLATE_PATH)
    # Replace the placeholder with the generated <li> items
    html_out = template.replace("__REPLACE_ANIMALS_INFO__", items_html)
    # Write the result to animals.html
    write_output(OUTPUT_PATH, html_out)
    print(f"Wrote {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

