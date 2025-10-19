import json
from pathlib import Path

TEMPLATE_PATH = "animals_template.html"
DATA_PATH = "animals_data.json"
OUTPUT_PATH = "animals.html"

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def build_animals_text(data):
    lines = []
    for animal in data:
        name = animal.get("name")
        locations = animal.get("locations") or []
        characteristics = animal.get("characteristics") or {}
        diet = characteristics.get("diet")
        type_ = characteristics.get("type")

        # Append only existing fields
        if name:
            lines.append(f"Name: {name}")
        if diet:
            lines.append(f"Diet: {diet}")
        if locations:
            lines.append(f"Location: {locations[0]}")
        if type_:
            lines.append(f"Type: {type_}")

        # Blank line between animals
        lines.append("")
    return "\n".join(lines)

def read_template(path):
    return Path(path).read_text(encoding="utf-8")

def write_output(path, content):
    Path(path).write_text(content, encoding="utf-8")

def main():
    data = load_data(DATA_PATH)
    animals_info = build_animals_text(data)
    template = read_template(TEMPLATE_PATH)
    html_out = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    write_output(OUTPUT_PATH, html_out)
    print(f"Wrote {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
