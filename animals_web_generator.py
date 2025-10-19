import json
from pathlib import Path
from typing import Any, Dict, List

TEMPLATE_PATH = "animals_template.html"
DATA_PATH = "animals_data.json"
OUTPUT_PATH = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path: str) -> List[Dict[str, Any]]:
    """Load animals JSON data into a list of dicts."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal: Dict[str, Any]) -> str:
    """Serialize a single animal into a cards__item HTML block."""
    name = animal.get("name")
    locations = animal.get("locations") or []
    characteristics = animal.get("characteristics") or {}
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")

    # Skip completely empty records
    if not any([name, diet, locations, type_]):
        return ""

    lines: List[str] = []
    lines.append('<li class="cards__item">')
    if name:
        lines.append(f'  <div class="card__title">{name}</div>')
    lines.append('  <p class="card__text">')
    if diet:
        lines.append(f'      <strong>Diet:</strong> {diet}<br/>')
    if locations:
        lines.append(f'      <strong>Location:</strong> {locations[0]}<br/>')
    if type_:
        lines.append(f'      <strong>Type:</strong> {type_}<br/>')
    lines.append("  </p>")
    lines.append("</li>")
    return "\n".join(lines)


def build_animals_html_items(data: List[Dict[str, Any]]) -> str:
    """Serialize all animals into a single HTML string."""
    parts = []
    for animal in data:
        item_html = serialize_animal(animal)
        if item_html:
            parts.append(item_html)
    return "\n".join(parts)


def read_template(path: str) -> str:
    """Read the HTML template content."""
    return Path(path).read_text(encoding="utf-8")


def write_output(path: str, content: str) -> None:
    """Write the final HTML output to file."""
    Path(path).write_text(content, encoding="utf-8")


def generate_html(
    data_path: str = DATA_PATH,
    template_path: str = TEMPLATE_PATH,
    output_path: str = OUTPUT_PATH,
    placeholder: str = PLACEHOLDER,
) -> str:
    """High-level function: load data, serialize, inject into template, write file."""
    data = load_data(data_path)
    items_html = build_animals_html_items(data)
    template = read_template(template_path)
    html_out = template.replace(placeholder, items_html)
    write_output(output_path, html_out)
    return output_path


def main() -> None:
    out = generate_html()
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
